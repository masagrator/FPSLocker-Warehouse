"""Keep one GitHub issue listing games whose newest update is not covered yet.

The issue body is rewritten on every run. When games are newly found, a
comment lists them, so watchers get a notification only for real changes.

Usage (from the repository root):
    python tools/patch_needed.py [--dry-run] [--cache DIR]

Needs GITHUB_TOKEN (issues: write) and GITHUB_REPOSITORY unless --dry-run.
"""
import argparse
import datetime
import json
import os
import re
import sys
from urllib.request import Request, urlopen

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import warehouse_data as wd  # noqa: E402

LABEL = "patch-needed"
TITLE = "Games with newer updates than the Warehouse covers"
STATE_RE = re.compile(r"<!-- patch-needed-state (\{.*?\}) -->", re.S)
STATUS_TEXT = {"available": "✅", "unavailable": "❌", "not_needed": "◯"}
PAGES_URL = os.environ.get("PAGES_URL", "")


def api(method, path, body=None):
    url = f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "fpslocker-warehouse-patch-needed",
    })
    with urlopen(req, timeout=60) as r:
        raw = r.read()
    return json.loads(raw) if raw else None


def outdated_games(cache_dir=None):
    games = wd.parse_readme()
    wd.apply_versions(games, wd.load_versions(cache_dir))
    return [g for g in games if g["outdated"]]


def row(g, first_seen):
    last = g["builds"][-1]
    name = g["names"][0] + "".join(f" `{r}`" for r in g["regions"])
    if PAGES_URL:
        name = f"[{name}]({PAGES_URL.rstrip('/')}/#{g['tids'][0]})"
    return (f"| {name} | `{g['tids'][0]}` | {STATUS_TEXT.get(g['status'], '?')} | "
            f"v{last['vid']} ({last['ver']}) | v{g['newest']} | {first_seen} |")


def table(rows):
    head = ("| Game | Title ID | Status | Covered | Newest | Found |\n"
            "| --- | --- | --- | --- | --- | --- |")
    return head + "\n" + "\n".join(rows) if rows else "_None._"


def make_body(games, seen, state):
    patched = [g for g in games if g["status"] == "available"]
    other = [g for g in games if g["status"] != "available"]

    def order(items):  # newest finds first, then by name
        items = sorted(items, key=lambda g: g["names"][0].lower())
        return sorted(items, key=lambda g: seen[g["tids"][0]], reverse=True)

    today = datetime.date.today().isoformat()
    return "\n\n".join([
        f"Updated automatically on {today}. Each game here has a newer update than the "
        "newest version listed in README.md. The list is rebuilt every day, and games "
        "drop off once the README covers the newest version.",
        f"### Patch needs updating ({len(patched)})\n"
        "These games have a patch for an older version.\n\n"
        + table([row(g, seen[g["tids"][0]]) for g in order(patched)]),
        f"### Needs re-checking ({len(other)})\n"
        "These games had no patch or did not need one. The newest update may change that.\n\n"
        + table([row(g, seen[g["tids"][0]]) for g in order(other)]),
        f"<!-- patch-needed-state {json.dumps(state, sort_keys=True)} -->",
    ])


def find_issue():
    for state in ("open", "closed"):
        issues = api("GET", f"/issues?labels={LABEL}&state={state}&per_page=100")
        for i in issues:
            if "pull_request" not in i and i["title"] == TITLE:
                return i
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cache")
    args = ap.parse_args()

    games = outdated_games(args.cache)
    issue = None if args.dry_run else find_issue()
    old = {}
    if issue and issue.get("body"):
        m = STATE_RE.search(issue["body"])
        if m:
            old = json.loads(m.group(1))

    today = datetime.date.today().isoformat()
    current = {g["tids"][0]: f"{g['tids'][0]}:{g['newest']}" for g in games}
    # first-seen date per (title ID, newest version); a newer update resets it
    seen = {}
    new = []
    for g in games:
        tid = g["tids"][0]
        prev = old.get(current[tid])
        seen[tid] = prev or today
        if not prev:
            new.append(g)
    state = {current[t]: d for t, d in seen.items()}
    body = make_body(games, seen, state)

    if args.dry_run:
        print(body)
        print(f"\n--- {len(games)} games, {len(new)} new since last run (dry run, nothing sent)")
        return

    if issue is None:
        try:
            api("POST", "/labels", {"name": LABEL, "color": "d4a72c",
                                    "description": "Game update not covered by the Warehouse yet"})
        except Exception:
            pass  # label already exists
        issue = api("POST", "/issues", {"title": TITLE, "body": body, "labels": [LABEL]})
        print(f"Created issue #{issue['number']} with {len(games)} games")
        return

    api("PATCH", f"/issues/{issue['number']}", {"body": body,
                                                "state": "open" if games else "closed"})
    if new and old:  # no comment on the first run, the issue itself is the notice
        comment = (f"{len(new)} game(s) got an update that the Warehouse doesn't cover yet:\n\n"
                   + table([row(g, today) for g in new]))
        api("POST", f"/issues/{issue['number']}/comments", {"body": comment})
    print(f"Updated issue #{issue['number']}: {len(games)} games, {len(new)} new")


if __name__ == "__main__":
    main()
