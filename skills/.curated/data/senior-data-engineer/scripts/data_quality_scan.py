#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional


def _profile_csv(path: Path, max_rows: int) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        nulls = Counter()
        uniques: Dict[str, Counter[str]] = {k: Counter() for k in fields}
        rows = 0
        for row in reader:
            rows += 1
            if rows > max_rows:
                break
            for k in fields:
                v = (row.get(k) or "").strip()
                if v == "":
                    nulls[k] += 1
                else:
                    if len(uniques[k]) < 50:
                        uniques[k][v] += 1

    return {
        "format": "csv",
        "path": str(path),
        "rows_profiled": rows,
        "fields": fields,
        "null_counts": dict(nulls),
        "unique_samples_top50": {k: dict(v.most_common(10)) for k, v in uniques.items() if v},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Lightweight profiling for CSV files (no pandas).")
    parser.add_argument("path", help="CSV file path")
    parser.add_argument("--max-rows", type=int, default=50_000, help="Max rows to scan (default: 50k)")
    parser.add_argument("--out", help="Write JSON output to file (prints to stdout if omitted)")
    args = parser.parse_args()

    p = Path(args.path).resolve()
    if not p.exists():
        raise SystemExit(f"File does not exist: {p}")

    report = _profile_csv(p, args.max_rows)
    payload = json.dumps(report, indent=2, sort_keys=True)

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
        print(f"Wrote: {out}")
    else:
        print(payload)


if __name__ == "__main__":
    main()

