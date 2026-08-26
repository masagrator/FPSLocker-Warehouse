#!/usr/bin/env python3
"""
titledb_buildid.py - resolve the newest BuildID (BID) for Switch title IDs
using blawar/titledb.

Why not ncas.json alone:
    ncas.json is keyed by NCA hash and each entry only carries
    {titleId, contentType, buildId, ...}. A title usually has MANY program
    NCAs with a buildId (one per update that was ever dumped), and nothing in
    the entry says which one is newest -- there is no version field.
    cnmts.json IS keyed by titleId -> version -> contentEntries[], so it
    provides the ordering. So: cnmts.json picks the NCA, ncas.json supplies
    the buildId.

    Update title ID = base title ID with the last 3 nibbles '000' -> '800'.
    Program NCA = contentEntries[].type == 1.
    Displayed version number vN = cnmt version / 65536.

versions.json (Nintendo's official version list) is used to tell whether the
newest update present in titledb is actually the newest update that exists.

Usage:
    python titledb_buildid.py 0100F2C0115B6000 0100E63013E60000
    python titledb_buildid.py --file ids.txt
    python titledb_buildid.py --file ids.txt --json out.json
    python titledb_buildid.py --check-warehouse        # diff vs FPSLocker-Warehouse
    python titledb_buildid.py --refresh 0100F2C0115B6000
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request

TITLEDB = "https://raw.githubusercontent.com/blawar/titledb/master/"
WAREHOUSE = ("https://raw.githubusercontent.com/masagrator/"
             "FPSLocker-Warehouse/master/README.md")
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "titledb_cache")
MAX_AGE = 12 * 3600  # re-download cached files older than this

PROGRAM = 1  # cnmt content entry type for the Program NCA


# --------------------------------------------------------------------------- #
# download / cache
# --------------------------------------------------------------------------- #
def fetch(url, name, refresh=False):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    fresh = (os.path.exists(path)
             and time.time() - os.path.getmtime(path) < MAX_AGE)
    if refresh or not fresh:
        sys.stderr.write("downloading %s ... " % name)
        sys.stderr.flush()
        req = urllib.request.Request(url, headers={"User-Agent": "titledb-buildid"})
        with urllib.request.urlopen(req) as r, open(path + ".tmp", "wb") as f:
            while True:
                chunk = r.read(1 << 20)
                if not chunk:
                    break
                f.write(chunk)
        os.replace(path + ".tmp", path)
        sys.stderr.write("ok\n")
    return path


def load_json(name, refresh=False):
    with open(fetch(TITLEDB + name, name, refresh), encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------- #
# core
# --------------------------------------------------------------------------- #
class TitleDB:
    def __init__(self, refresh=False):
        # keys in these files are not case-consistent, normalise to lowercase
        self.ncas = {k.lower(): v for k, v in load_json("ncas.json", refresh).items()}
        self.cnmts = {k.lower(): v for k, v in load_json("cnmts.json", refresh).items()}
        self.versions = {k.lower(): v for k, v in load_json("versions.json", refresh).items()}

    @staticmethod
    def update_id(title_id):
        """Base application ID -> its update ID (…000 -> …800)."""
        return title_id[:-3] + "800"

    def latest_known_version(self, title_id):
        """Newest version Nintendo has published, per versions.json."""
        entry = self.versions.get(title_id)
        if not isinstance(entry, dict) or not entry:
            return None, None
        v = max(entry, key=lambda x: int(x))
        return int(v), entry[v]  # (version, release date)

    def resolve(self, title_id):
        title_id = title_id.strip().lower()
        if not re.fullmatch(r"[0-9a-f]{16}", title_id):
            return {"titleId": title_id.upper(), "status": "invalid title id"}

        source = "update"
        cnmt = self.cnmts.get(self.update_id(title_id))
        if not cnmt:
            # no update ever released -> BID of the base game itself
            cnmt = self.cnmts.get(title_id)
            source = "base"
        if not cnmt:
            return {"titleId": title_id.upper(), "status": "not in titledb"}

        version = max(cnmt, key=lambda v: int(v))
        entry = cnmt[version]

        # An update can hold several program NCAs (multi-program titles such as
        # 0100670014482000/…001/…002). Prefer the one whose ncas.json titleId
        # matches exactly, otherwise fall back to the lowest contentIndex.
        candidates = []
        for ce in entry.get("contentEntries", []):
            if ce.get("type") != PROGRAM:
                continue
            nca_id = ce["ncaId"].lower()
            nca = self.ncas.get(nca_id, {})
            build_id = nca.get("buildId") or ce.get("buildId")
            if not build_id:
                continue
            candidates.append({
                "ncaTitleId": (nca.get("titleId") or "").lower(),
                "contentIndex": nca.get("contentIndex", 0),
                "ncaId": nca_id,
                "buildId": build_id,
            })
        if not candidates:
            return {"titleId": title_id.upper(),
                    "status": "no program NCA with a buildId"}

        exact = [c for c in candidates if c["ncaTitleId"] == title_id]
        pick = (exact or sorted(candidates, key=lambda c: c["contentIndex"]))[0]

        version = int(version)
        newest, date = self.latest_known_version(title_id)
        # titledb is a community dump: the newest update may simply not be in it yet
        up_to_date = None if newest is None else version >= newest

        return {
            "titleId": title_id.upper(),
            "status": "ok",
            "bid": pick["buildId"][:16],        # first 8 bytes, FPSLocker format
            "buildId": pick["buildId"],         # full 32-byte field
            "ncaId": pick["ncaId"],
            "version": version,
            "versionLabel": "v%d" % (version // 65536),
            "source": source,
            "latestKnownVersion": newest,
            "latestKnownVersionLabel": None if newest is None else "v%d" % (newest // 65536),
            "releaseDate": date,
            "upToDate": up_to_date,
        }


# --------------------------------------------------------------------------- #
# FPSLocker-Warehouse comparison
# --------------------------------------------------------------------------- #
def parse_warehouse(refresh=False):
    """titleId -> [BIDs in README order]; the last one is the newest listed."""
    path = fetch(WAREHOUSE, "FPSLocker_README.md", refresh)
    out = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\|[^|]*\|\s*`([0-9A-Fa-f]{16})`\s*\|(.*)", line)
            if not m:
                continue
            bids = re.findall(r"`([0-9A-Fa-f]{16})`\s*\(\[", m.group(2))
            if bids:
                out[m.group(1).upper()] = [b.upper() for b in bids]
    return out


# --------------------------------------------------------------------------- #
# output
# --------------------------------------------------------------------------- #
def fmt(r):
    if r["status"] != "ok":
        return "%s  %s" % (r["titleId"], r["status"])
    if r["upToDate"] is True:
        flag = "latest"
    elif r["upToDate"] is False:
        flag = "STALE, newest is %s" % r["latestKnownVersionLabel"]
    else:
        flag = "unknown (not in versions.json)"
    base = "" if r["source"] == "update" else "  [no update, base game BID]"
    return "%s  %s  %-4s  %s%s" % (r["titleId"], r["bid"], r["versionLabel"], flag, base)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("title_ids", nargs="*", help="16-hex-digit title IDs")
    p.add_argument("--file", help="file with one title ID per line")
    p.add_argument("--json", metavar="OUT", help="write full results as JSON")
    p.add_argument("--refresh", action="store_true", help="force re-download")
    p.add_argument("--check-warehouse", action="store_true",
                   help="compare every title in FPSLocker-Warehouse and list "
                        "the ones whose newest BID is missing there")
    args = p.parse_args()

    ids = [t.strip() for t in args.title_ids]
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            ids += [ln.split("#")[0].strip() for ln in f]
    ids = [i for i in ids if i]

    warehouse = parse_warehouse(args.refresh) if args.check_warehouse else None
    if args.check_warehouse and not ids:
        ids = sorted(warehouse)

    if not ids:
        p.error("no title IDs given")

    db = TitleDB(args.refresh)
    results = [db.resolve(t) for t in ids]

    if args.check_warehouse:
        missing, stale, unknown = [], [], []
        for r in results:
            if r["status"] != "ok":
                continue
            known = warehouse.get(r["titleId"], [])
            if r["bid"] in known:
                continue
            (stale if r["upToDate"] is False else missing).append((r, known))
        print("checked %d titles from FPSLocker-Warehouse\n" % len(results))
        print("--- newest BID exists in titledb but is NOT in the warehouse (%d)"
              % len(missing))
        for r, known in missing:
            print("  %s  %s  %s   warehouse newest: %s"
                  % (r["titleId"], r["bid"], r["versionLabel"],
                     known[-1] if known else "-"))
        print("\n--- titledb itself is behind, nothing to add yet (%d)" % len(stale))
        for r, known in stale:
            print("  %s  titledb %s, Nintendo %s"
                  % (r["titleId"], r["versionLabel"], r["latestKnownVersionLabel"]))
    else:
        for r in results:
            print(fmt(r))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        sys.stderr.write("wrote %s\n" % args.json)


if __name__ == "__main__":
    main()
