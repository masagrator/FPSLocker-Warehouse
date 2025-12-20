from github import Github
from urllib.request import Request, urlopen
import json
import re
import sys

class DATA:
    database = {}

def DownloadDatabase():
    g = Github()
    try:
        repo = g.get_repo("blawar/titledb")
    except:
        print("Github API requests limit was achieved.")
        print("We cannot check when last time file was updated.")
    else:
        commits = repo.get_commits(path="versions.txt")
        print("Last database update (YYYY/MM/DD):")
        print(commits[0].commit.committer.date)
        print("\n---\n")
    site = "https://github.com/blawar/titledb/raw/master/versions.txt"
    request_site = Request(site, headers={"User-Agent": "Mozilla/5.0"})
    text = urlopen(request_site).read().decode("ascii").split("\n")
    for line in text:
        if (line.find("id") != -1):
            continue
        array = line.rstrip("\n").rstrip("\r").split("|")
        if (len(array) < 3):
            continue
        if (array[2] == ""):
            continue
        DATA.database[array[0]] = int(int(array[2]) / 65536)
    site = "https://raw.githubusercontent.com/masagrator/version_dump/refs/heads/main/version_dump.txt"
    request_site = Request(site, headers={"User-Agent": "Mozilla/5.0"})
    text = urlopen(request_site).read().decode("ascii").split("\n")
    for line in text:
        if (line.find("id") != -1):
            continue
        array = line.rstrip("\n").rstrip("\r").split("|")
        if (len(array) < 3):
            continue
        if (array[2] == ""):
            continue
        version_value = int(int(array[2]) / 65536)
        if (array[0] not in DATA.database):
            DATA.database[array[0]] = version_value
        elif DATA.database[array[0]] < version_value:
            DATA.database[array[0]] = version_value

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
    pos = versionColumn.find(", v") + 3
    if (versionColumn.find("<br>") == -1):
        version = int(re.sub(r"\D", "", versionColumn[pos:pos+2]))
    else:
        pos = versionColumn.rfind("<br>")
        pos = versionColumn.find(", v", pos) + 3
        version = int(re.sub(r"\D", "", versionColumn[pos:pos+2]))
    try:
        latestUpdate = DATA.database[titleid[:13] + "800"]
    except:
        try:
            latestUpdate = DATA.database[titleid]
        except:
            print(f"Titleid not found: {titleid}")
            print(f"Title:{gameTitle}\n")
            continue
    if (version != latestUpdate):
        print(titleid)
        print(f"Title:{gameTitle}")
        print(f"Newest update: v{latestUpdate}")
        print(f"Latest patch: v{version}")
        if (line.count("`0100") > 1):
            print("Game has more than one titleid! Possible mismatch")

        print("---")

print("------------------------\n")
print("Searching for duplicated BIDs...")

site = "https://raw.githubusercontent.com/masagrator/FPSLocker-Warehouse/refs/heads/v4/README.md"
site2 = "https://github.com/blawar/titledb/raw/refs/heads/master/ncas.json"

print("Downloading ncas.json...")
request_site = Request(site2, headers={"User-Agent": "Mozilla/5.0"})
raw_dump = urlopen(request_site).read().decode("UTF-8")
print("Downloading finished.")
DUMP = json.loads(raw_dump)

BIDS = {}

for line in readme_dump:
    if line.find("| `0100") == -1:
        continue
    gameTitle = line.split("|")[1]
    pos = line.find("| `0100") + 3
    titleid = line[pos:pos+16].upper()
    if titleid[15:16] != "0":
        continue
    versionColumn = line.split("|")[3]
    pos2 = versionColumn.find(" `") + 2
    pos = versionColumn.find(", v") +3
    BID = versionColumn[pos2:pos2+16].upper()
    if (versionColumn.find("<br>") == -1):
        version = int(re.sub(r"\D", "", versionColumn[pos:pos+2]))
    else:
        pos = versionColumn.rfind("<br>")
        pos2 = versionColumn.find(" `", pos) + 2
        pos = versionColumn.find(", v", pos) + 3
        BID = versionColumn[pos2:pos2+16].upper()
        version = int(re.sub(r"\D", "", versionColumn[pos:pos+2]))
    if BID not in BIDS.keys():
        BIDS[BID] = 1
    else: BIDS[BID] += 1

BIDS_NOT_ENOUGH = []

keys = list(BIDS.keys())
len_keys = len(keys)
for i in range(len(keys)):
    if (i % 100 == 0): print("Step 1/3: %d/%d" % (i, len_keys), end="\r")
    count = raw_dump.count("\"%s" % keys[i])
    if (count > BIDS[keys[i]]):
        BIDS_NOT_ENOUGH.append(keys[i])

keys2 = list(DUMP.keys())
TIDS = {}
len_keys = len(keys2)
for i in range(len_keys):
    if (i % 10000 == 0): print("Step 2/3: %d/%d" % (i, len_keys), end="\r")
    if ("buildId" not in DUMP[keys2[i]].keys()):
        continue
    if (DUMP[keys2[i]]["buildId"] == None):
        continue
    if DUMP[keys2[i]]["buildId"][:16] not in TIDS:
        TIDS[DUMP[keys2[i]]["buildId"][:16]] = [DUMP[keys2[i]]["titleId"][:13] + "000"]
    else:
        string = DUMP[keys2[i]]["titleId"][:13] + "000"
        if (string not in TIDS[DUMP[keys2[i]]["buildId"][:16]]): TIDS[DUMP[keys2[i]]["buildId"][:16]].append(DUMP[keys2[i]]["titleId"][:13] + "000")

TIDS_found = {}
len_bid_keys = len(BIDS_NOT_ENOUGH)
for i in range(len_bid_keys):
    if (i % 100 == 0): print("Step 3/3: %d/%d" % (i, len_bid_keys), end="\r")
    if (len(TIDS[BIDS_NOT_ENOUGH[i]]) == 1):
        continue
    count = BIDS[keys[i]]
    for x in range(len(TIDS[BIDS_NOT_ENOUGH[i]])):
        if (readme_dump.count(BIDS_NOT_ENOUGH[i]) != count):
            TIDS_found[BIDS_NOT_ENOUGH[i]] = TIDS[BIDS_NOT_ENOUGH[i]]

print("                                                 ")

BLACKLIST = ["E4F041624093998D", "937209E79E2E0E5D", "473D222EB1BDAD47", "217C9ECF258C0312", "DFC7E8979528DE44", "2284DFB25F387719",
            "0F73F1D52820F90B", "6D9EA94F8AAC00A8", "3749BFEA64DC98DF", "AA9BF85240409E60", "4BC4A8A814FD46A4", "B151A224A429F9A7", "D27FD8A515077F34"]

tid_keys = list(TIDS_found.keys())
for i in range(len(tid_keys)):
    if (tid_keys[i] in BLACKLIST):
        continue
    print("BID:", tid_keys[i])
    for x in range(len(TIDS_found[tid_keys[i]])):
        print("TID %d: %s" % (x, TIDS_found[tid_keys[i]][x]))
    print("\n")

print("Script finished execution.")


