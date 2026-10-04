"""Shared data layer for the Warehouse page and the patch-needed tracker.

Reads README.md tables, git history of the patches folder, and the same
version databases CheckUpdate.py uses (titledb + version_dump).
"""
import os
import re
import subprocess
from urllib.request import Request, urlopen

PATCHES_DIR = "SaltySD/plugins/FPSLocker/patches"
VERSION_SOURCES = [
    "https://raw.githubusercontent.com/blawar/titledb/master/versions.txt",
    "https://raw.githubusercontent.com/masagrator/version_dump/refs/heads/main/version_dump.txt",
]

ISSUES = {
    "🔐": "Internal FPS lock",
    "📏": "Dynamic resolution",
    "⚔️": "Double buffer",
    "👄": "Lipsync",
    "⏱️": "Gameplay speed",
    "🏃": "Physics",
    "🛑": "Fake frames",
    "🌤️": "Graphics effects",
    "🖥️": "UI speed",
    "🖌️": "UI broken animations",
    "📺": "Cutscenes",
    "🎮": "Button polling",
    "🔢": "Logic",
    "🔧": "Hindered performance",
    "📷": "Camera",
}

LIST_LOCKED = "locked30"
LIST_OTHER = "other"

_TID_RE = re.compile(r"`([0-9A-Fa-f]{15,16})`")
_BUILD_RE = re.compile(
    r"`([0-9A-Fa-f]{16})`\s*\((?P<status>.*?),\s*v(?P<vid>\d+),\s*(?P<ver>[^)]*)\)"
)
_LINK_RE = re.compile(r"\]\(([^)]+\.yaml)\)")
_ISSUE_RE = re.compile(r"~~|\[([^\]]+)\]\(#[^)]*\)")
_REGION_RE = re.compile(r"`([^`]+)`")


def _clean_name(cell):
    lines = []
    regions = []
    for part in cell.split("<br>"):
        part = part.strip()
        if part.startswith("- "):
            part = part[2:]
        regions += _REGION_RE.findall(part)
        part = _REGION_RE.sub("", part).strip()
        if part:
            lines.append(part)
    return lines, regions


def _parse_status(text):
    if "✅" in text:
        return "available", False
    if "❌" in text:
        return "unavailable", "📌" in text
    if "◯" in text:
        return "not_needed", False
    return "unknown", False


def _parse_issues(cell):
    issues = []
    struck = False
    for m in _ISSUE_RE.finditer(cell):
        if m.group(0) == "~~":
            struck = not struck
            continue
        icon = m.group(1).strip()
        issues.append({"icon": icon, "name": ISSUES.get(icon, icon), "solved": struck})
    return issues


def parse_readme(path="README.md"):
    """Return a list of game dicts parsed from both README tables."""
    games = []
    current_list = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            if "<summary>" in line:
                current_list = LIST_LOCKED if "30 FPS locked" in line else LIST_OTHER
                continue
            if not line.startswith("| ") or current_list is None:
                continue
            cols = line.rstrip("\n").split("|")
            if len(cols) < 5:  # some rows have no trailing pipe
                continue
            name_cell, tid_cell, build_cell, issue_cell = cols[1], cols[2], cols[3], cols[4]
            tids = [t.upper() for t in _TID_RE.findall(tid_cell)]
            if not tids:
                continue  # header row
            names, regions = _clean_name(name_cell)
            builds = []
            for m in _BUILD_RE.finditer(build_cell):
                status, pinned = _parse_status(m.group("status"))
                builds.append({
                    "bid": m.group(1).upper(),
                    "status": status,
                    "pinned": pinned,
                    "vid": int(m.group("vid")),
                    "ver": m.group("ver").strip(),
                    "link": (_LINK_RE.search(m.group("status")) or [None, None])[1],
                })
            if not builds:
                continue
            latest = builds[-1]
            games.append({
                "names": names,
                "regions": regions,
                "tids": tids,
                "list": current_list,
                "builds": builds,
                "status": latest["status"],
                "pinned": latest["pinned"],
                "issues": _parse_issues(issue_cell),
            })
    return games


def _fetch(url, cache_dir=None):
    if cache_dir:
        local = os.path.join(cache_dir, url.rsplit("/", 1)[-1])
        if os.path.exists(local):
            with open(local, encoding="ascii", errors="replace") as f:
                return f.read()
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urlopen(req, timeout=120).read().decode("ascii", errors="replace")


def load_versions(cache_dir=None):
    """Map title ID -> newest version ID (raw version / 65536), as in CheckUpdate.py."""
    db = {}
    for url in VERSION_SOURCES:
        for line in _fetch(url, cache_dir).splitlines():
            parts = line.strip().split("|")
            if len(parts) < 3 or parts[0] == "id" or parts[2] == "":
                continue
            try:
                value = int(parts[2]) // 65536
            except ValueError:
                continue
            tid = parts[0].upper()
            if value > db.get(tid, -1):
                db[tid] = value
    return db


def apply_versions(games, db):
    """Add `newest` (version ID or None) and `outdated` to every game."""
    for g in games:
        tid = g["tids"][0]
        newest = None
        if len(tid) == 16 and tid.endswith("0"):  # same rule as CheckUpdate.py
            newest = db.get(tid[:13] + "800", db.get(tid))
        g["newest"] = newest
        g["outdated"] = newest is not None and newest > g["builds"][-1]["vid"]


def _git(args, repo="."):
    return subprocess.run(["git", "-C", repo, *args], check=True,
                          capture_output=True, text=True).stdout


def _iter_commits(log):
    """Yield (date, author, [paths]) from `git log --name-only` output with ^ markers."""
    date = author = None
    paths = []
    for line in log.split("\n"):  # not splitlines(): it treats \x1e/\x1f as breaks
        if line.startswith("\x1e"):
            if date:
                yield date, author, paths
            date, author = line[1:].split("\x1f", 1)
            paths = []
        elif line.strip():
            paths.append(line.strip())
    if date:
        yield date, author, paths


IGNORED_AUTHORS = {"github-actions[bot]", "dependabot[bot]"}


def apply_history(games, repo=".", recent_count=10):
    """Add `updated` + `contributors` per game and return the most recently added patches."""
    log = _git(["log", "--format=\x1e%cs\x1f%an", "--name-only", "--", PATCHES_DIR], repo)
    added_log = _git(["log", "--diff-filter=A", "--format=\x1e%cs\x1f%an", "--name-only",
                      "--", PATCHES_DIR], repo)

    folder_updated = {}
    folder_authors = {}
    for date, author, paths in _iter_commits(log):
        for p in paths:
            parts = p.split("/")
            if len(parts) < 6:
                continue
            tid = parts[4].upper()
            folder_updated.setdefault(tid, date)  # log is newest first
            if author not in IGNORED_AUTHORS:
                folder_authors.setdefault(tid, [])
                if author not in folder_authors[tid]:
                    folder_authors[tid].append(author)

    by_bid = {}
    for g in games:
        tid = g["tids"][0]
        g["updated"] = folder_updated.get(tid)
        g["contributors"] = folder_authors.get(tid, [])
        for b in g["builds"]:
            by_bid[(tid, b["bid"])] = (g, b)

    # One entry per build ID: regional editions often share one build and get
    # the same patch, so they are grouped instead of filling the list.
    groups = {}
    for date, author, paths in _iter_commits(added_log):
        for p in paths:
            m = re.search(r"/([0-9A-Fa-f]{16})/([0-9A-Fa-f]{16})\.yaml$", p)
            if not m:
                continue
            key = (m.group(1).upper(), m.group(2).upper())
            if key not in by_bid:
                continue
            g, b = by_bid[key]
            entry = groups.get(key[1])
            if entry is None:
                entry = groups[key[1]] = {"bid": key[1], "ver": b["ver"], "date": date,
                                          "author": author, "tids": [], "names": []}
            if key[0] not in entry["tids"]:
                entry["tids"].append(key[0])
                entry["names"].append(g["names"][0])

    recent = list(groups.values())[:recent_count]  # dict keeps newest-first order
    for e in recent:
        latin = [n for n in e["names"] if n.isascii()]
        e["name"] = (latin or e["names"])[0]
        e["tid"] = e["tids"][e["names"].index(e["name"])]
        e["editions"] = len(e["tids"])
        del e["names"]
    return recent


def resolve_yaml(games, repo="."):
    """Set build["yaml"] to the patch file's repo path (or None) and drop the raw README link.

    The README link wins when it points to an existing file; otherwise the
    standard <title ID>/<build ID>.yaml location is used.
    """
    for g in games:
        for b in g["builds"]:
            link = b.pop("link", None)
            b["yaml"] = None
            if b["status"] != "available":
                continue
            for path in (link, f"{PATCHES_DIR}/{g['tids'][0]}/{b['bid']}.yaml"):
                if path and os.path.isfile(os.path.join(repo, path)):
                    b["yaml"] = path
                    break
