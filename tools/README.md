# Warehouse page tools

| File | What it does |
| --- | --- |
| `build_site.py` | Builds the GitHub Pages site (`_site/index.html`) from `README.md`, git history of the patches folder, and titledb + version_dump. |
| `site_template.html` | Page layout, styles and script. The game data is injected at build time. Patch files are not copied into the site: the page loads each one from `raw.githubusercontent.com` (branch `v4`) only when someone opens that game. |
| `patch_needed.py` | Keeps one issue (label `patch-needed`) listing games whose newest update is newer than the newest version in `README.md`. |
| `warehouse_data.py` | Shared README parser, version lookup and git history helpers. |

## One-time setup

1. Settings → Pages → Build and deployment → Source: **GitHub Actions**.
2. Run the **Build Warehouse page and patch-needed list** workflow once from the Actions tab.

After that the page rebuilds on every push to `v4` that touches the README, patches or tools, and every day at 08:45 UTC. The daily run also updates the patch-needed issue. A comment is posted only when new games show up, so watchers get one notification per change.

## Run locally

```sh
python tools/build_site.py --out _site          # open _site/index.html
python tools/patch_needed.py --dry-run          # print the issue body, send nothing
```

Page links to a game use its title ID, for example `https://masagrator.github.io/FPSLocker-Warehouse/#0100E63013E60000`.
