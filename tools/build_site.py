"""Build the Warehouse GitHub Pages site into _site/index.html.

Usage (from the repository root):
    python tools/build_site.py [--out _site] [--cache DIR] [--fragment]

--cache DIR   read versions.txt / version_dump.txt from DIR instead of downloading
--fragment    write only the page content (no <html>/<head>/<body>), for previews
"""
import argparse
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import warehouse_data as wd  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def build(repo=".", cache_dir=None):
    games = wd.parse_readme(os.path.join(repo, "README.md"))
    try:
        wd.apply_versions(games, wd.load_versions(cache_dir))
    except Exception as e:  # keep the site building even if a version source is down
        print(f"warning: version databases unavailable ({e}); outdated badges skipped")
        for g in games:
            g["newest"], g["outdated"] = None, False
    recent = wd.apply_history(games, repo)
    return {
        "built": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
        "issueNames": wd.ISSUES,
        "recent": recent,
        "games": games,
    }


def render(data, fragment=False):
    with open(os.path.join(HERE, "site_template.html"), encoding="utf-8") as f:
        html = f.read()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = html.replace("/*__DATA__*/null", payload)
    if fragment:
        head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
        head = re.sub(r"<meta[^>]*>\s*", "", head)
        body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
        html = head.strip() + "\n" + body.strip() + "\n"
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out", default="_site")
    ap.add_argument("--cache")
    ap.add_argument("--fragment", action="store_true")
    args = ap.parse_args()

    data = build(args.repo, args.cache)
    os.makedirs(args.out, exist_ok=True)
    out = os.path.join(args.out, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(data, args.fragment))
    with open(os.path.join(args.out, ".nojekyll"), "w"):
        pass
    outdated = sum(g["outdated"] for g in data["games"])
    print(f"Wrote {out}: {len(data['games'])} games, {outdated} with newer updates, "
          f"{len(data['recent'])} recent patches")


if __name__ == "__main__":
    main()
