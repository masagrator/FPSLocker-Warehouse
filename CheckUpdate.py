from github import Github
from urllib.request import Request, urlopen
import json
import re

class DATA:
    database = {}
    cnmt_bids = {}

def DownloadDatabase():
    g = Github()
    try:
        repo = g.get_repo("blawar/titledb")
    except:
        print("Github API requests limit was achieved.")
        print("We cannot check when last time file was updated.")
    else:
        commits = repo.get_commits(path="versions.txt")
        print("Last titledb update (YYYY/MM/DD):")
        print(commits[0].commit.committer.date)
        print("\n---\n")
    try:
        repo = g.get_repo("masagrator/version_dump")
    except:
        print("Github API requests limit was achieved.")
        print("We cannot check when last time file was updated.")
    else:
        commits = repo.get_commits(path="version_dump.txt")
        print("Last version_dump update (YYYY/MM/DD):")
        print(commits[0].commit.committer.date)
        print("\n---\n")

    # 1. Download versions.txt
    site = "https://github.com/blawar/titledb/raw/master/versions.txt"
    request_site = Request(site, headers={"User-Agent": "Mozilla/5.0"})
    text = urlopen(request_site).read().decode("ascii").split("\n")
    for line in text:
        if line.find("id") != -1:
            continue
        array = line.rstrip("\n").rstrip("\r").split("|")
        if len(array) < 3 or array[2] == "":
            continue
        DATA.database[array[0]] = int(int(array[2]) / 65536)

    # 2. Download version_dump.txt
    site = "https://raw.githubusercontent.com/masagrator/version_dump/refs/heads/main/version_dump.txt"
    request_site = Request(site, headers={"User-Agent": "Mozilla/5.0"})
    text = urlopen(request_site).read().decode("ascii").split("\n")
    for line in text:
        if line.find("id") != -1:
            continue
        array = line.rstrip("\n").rstrip("\r").split("|")
        if len(array) < 3 or array[2] == "":
            continue
        version_value = int(int(array[2]) / 65536)
        if array[0] not in DATA.database:
            DATA.database[array[0]] = version_value
        elif DATA.database[array[0]] < version_value:
            DATA.database[array[0]] = version_value

    # 3. Download and parse cnmts.json
    print("Downloading cnmts.json...")
    site2 = "https://github.com/blawar/titledb/raw/refs/heads/master/cnmts.json"
    request_site = Request(site2, headers={"User-Agent": "Mozilla/5.0"})
    raw_dump = urlopen(request_site).read().decode("UTF-8")
    cnmt_dump = json.loads(raw_dump)

    def process_entry(tid, entry):
        if not isinstance(entry, dict):
            return
        bid = entry.get("buildId") or entry.get("buildid") or entry.get("bid")
        if not bid:
            return
        bid = str(bid)[:16].upper()
        ver = entry.get("version", 0)
        try:
            ver = int(ver)
        except (ValueError, TypeError):
            ver = 0
        ver = ver // 65536 if ver >= 65536 else ver

        tid = tid.upper()
        if tid not in DATA.cnmt_bids or ver >= DATA.cnmt_bids[tid]["version"]:
            DATA.cnmt_bids[tid] = {"version": ver, "bid": bid}

    if isinstance(cnmt_dump, dict):
        for key, val in cnmt_dump.items():
            if len(key) == 16:
                # Top level key is Title ID
                if isinstance(val, dict):
                    if any(k.lower() in ("buildid", "bid") for k in val.keys()):
                        process_entry(key, val)
                    else:
                        for sub_val in val.values():
                            process_entry(key, sub_val)
                elif isinstance(val, list):
                    for sub_val in val:
                        process_entry(key, sub_val)
            elif isinstance(val, dict):
                tid = val.get("titleId") or val.get("titleid") or val.get("id")
                if tid:
                    process_entry(str(tid), val)

print("Downloading database...")
DownloadDatabase()

file = open("README.md", "r", encoding="UTF-8")
readme_dump = file.readlines()
file.seek(0)
for line in file:
    if line.find("| `0100") == -1:
        continue
    gameTitle = line.split("|")[1]
    pos = line.find("| `0100") + 3
    titleid = line[pos:pos+16].upper()
    if titleid[15:16] != "0":
        continue

    versionColumn = line.split("|")[3]
    pos2 = versionColumn.find(" `") + 2
    pos = versionColumn.find(", v") + 3

    if versionColumn.find("<br>") == -1:
        readmeBID = versionColumn[pos2:pos2+16].upper()
        version = int(re.sub(r"\D", "", versionColumn[pos:pos+2]))
    else:
        pos = versionColumn.rfind("<br>")
        pos2 = versionColumn.find(" `", pos) + 2
        pos = versionColumn.find(", v", pos) + 3
        readmeBID = versionColumn[pos2:pos2+16].upper()
        version = int(re.sub(r"\D", "", versionColumn[pos:pos+2]))

    try:
        latestUpdate = DATA.database[titleid[:13] + "800"]
    except KeyError:
        try:
            latestUpdate = DATA.database[titleid]
        except KeyError:
            print(f"Titleid not found: {titleid}")
            print(f"Title:{gameTitle}")
            print("---")
            continue

    # Retrieve BID (checks Update TID ...800, exact TID, and Base TID ...000)
    update_tid = titleid[:13] + "800"
    base_tid = titleid[:13] + "000"

    if update_tid in DATA.cnmt_bids:
        newestBID = DATA.cnmt_bids[update_tid]["bid"]
    elif titleid in DATA.cnmt_bids:
        newestBID = DATA.cnmt_bids[titleid]["bid"]
    elif base_tid in DATA.cnmt_bids:
        newestBID = DATA.cnmt_bids[base_tid]["bid"]
    else:
        newestBID = "N/A"

    if version != latestUpdate:
        print(titleid)
        print(f"Title:{gameTitle}")
        print(f"Newest update: v{latestUpdate} ({newestBID})")
        print(f"Latest patch: v{version} ({readmeBID})")
        if line.count("`0100") > 1:
            print("Game has more than one titleid! Possible mismatch")

        print("---")
