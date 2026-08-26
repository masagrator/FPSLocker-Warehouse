import json
import sys
from pathlib import Path


def load_json(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[!] Error loading {filepath}: {e}")
        return {}


def extract_build_id(entry):
    """Extracts and standardizes the 32-character Build ID from a program NCA entry."""
    # Only Program NCAs (Type 1) contain executable Build IDs
    if entry.get("type") != 1:
        return None

    raw_id = entry.get("buildId")
    if not raw_id:
        return None

    # Truncate 64-character padded string to standard 32-char hex and lowercase
    clean_id = str(raw_id)[:32].lower()

    # Filter out empty or zeroed Build IDs
    if clean_id == "0" * 32 or not clean_id:
        return None

    return clean_id


def process_cnmts(cnmts_data):
    """Parses cnmts.json data into a structured lookup dictionary."""
    parsed_titles = {}

    for title_id, versions in cnmts_data.items():
        clean_tid = title_id.lower()
        parsed_titles[clean_tid] = {}

        for version_key, meta in versions.items():
            version_num = int(meta.get("version", version_key))
            build_ids = []

            for entry in meta.get("contentEntries", []):
                bid = extract_build_id(entry)
                if bid:
                    build_ids.append(bid)

            parsed_titles[clean_tid][version_num] = {
                "version": version_num,
                "buildIds": build_ids if build_ids else ["n/a"],
                "meta": meta,
            }

    return parsed_titles


def check_updates(cnmts_path, titledb_path):
    cnmts_data = load_json(cnmts_path)
    titledb_data = load_json(titledb_path)

    if not cnmts_data:
        print("[!] No valid CNMT data found to check.")
        return

    parsed_cnmts = process_cnmts(cnmts_data)

    print(f"\n{'Title ID':<18} | {'Latest Ver':<10} | {'Build ID':<34} | {'Status'}")
    print("-" * 80)

    for title_id, versions in parsed_cnmts.items():
        # Find the highest version present in local CNMT
        latest_version = max(versions.keys())
        ver_data = versions[latest_version]

        build_id_str = (
            ver_data["buildIds"][0] if ver_data["buildIds"] else "n/a"
        )

        # Compare against TitleDB if available
        remote_info = titledb_data.get(title_id, {})
        remote_latest_ver = int(remote_info.get("version", 0))

        if remote_latest_ver > latest_version:
            status = f"Update Available (v{remote_latest_ver})"
        elif remote_latest_ver == latest_version:
            status = "Up to date"
        else:
            status = "Local version newer / Unknown"

        print(
            f"{title_id:<18} | v{latest_version:<9} | {build_id_str:<34} | {status}"
        )


if __name__ == "__main__":
    cnmts_file = "cnmts.json"
    titledb_file = "titledb.json"

    check_updates(cnmts_file, titledb_file)
