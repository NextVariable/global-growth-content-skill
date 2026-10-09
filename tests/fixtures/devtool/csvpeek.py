"""Fixture tool: inspect a local UTF-8 CSV; no network or file writes."""

import argparse
import csv
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        with args.file.open(encoding="utf-8", newline="") as handle:
            rows = csv.reader(handle)
            header = next(rows, [])
            count = sum(1 for _ in rows)
    except (OSError, UnicodeError, csv.Error) as exc:
        parser.exit(2, f"csvpeek: {exc}\n")
    print(json.dumps({"header": header, "rows": count}, ensure_ascii=False))


if __name__ == "__main__":
    main()
