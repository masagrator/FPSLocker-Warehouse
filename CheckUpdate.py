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
        

print("Downloading database...")
DownloadDatabase()

file = open("README.md", "r", encoding="UTF-8")
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
        version = int(re.sub("\D", "", versionColumn[pos:pos+2]))
    else:
        pos = versionColumn.rfind("<br>")
        pos = versionColumn.find(", v", pos) + 3
        version = int(re.sub("\D", "", versionColumn[pos:pos+2]))
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