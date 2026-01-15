#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def _maybe_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except Exception:
        return None


def _summarize(values: List[float]) -> Dict[str, Any]:
    if not values:
        return {}
    values_sorted = sorted(values)
    n = len(values_sorted)
    mean = sum(values_sorted) / n
    var = sum((x - mean) ** 2 for x in values_sorted) / n
    def pct(p: float) -> float:
        i = int((n - 1) * p)
        return values_sorted[i]
    return {
        "count": n,
        "min": values_sorted[0],
        "p50": pct(0.50),
        "p90": pct(0.90),
        "p99": pct(0.99),
        "max": values_sorted[-1],
        "mean": mean,
        "stdev": math.sqrt(var),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Quick CSV profiling (no pandas).")
    parser.add_argument("path", help="CSV file path")
    parser.add_argument("--max-rows", type=int, default=50_000, help="Max rows to scan (default: 50k)")
    parser.add_argument("--out", help="Write JSON output to file (prints to stdout if omitted)")
    args = parser.parse_args()

    p = Path(args.path).resolve()
    if not p.exists():
        raise SystemExit(f"File does not exist: {p}")

    with p.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        nulls = Counter()
        numerics: Dict[str, List[float]] = {k: [] for k in fields}
        top_values: Dict[str, Counter[str]] = {k: Counter() for k in fields}

        rows = 0
        for row in reader:
            rows += 1
            if rows > args.max_rows:
                break
            for k in fields:
                raw = (row.get(k) or "").strip()
                if raw == "":
                    nulls[k] += 1
                    continue
                if len(top_values[k]) < 100:
                    top_values[k][raw] += 1
                v = _maybe_float(raw)
                if v is not None and len(numerics[k]) < 100_000:
                    numerics[k].append(v)

    report: Dict[str, Any] = {
        "format": "csv",
        "path": str(p),
        "rows_profiled": rows,
        "fields": fields,
        "null_counts": dict(nulls),
        "numeric_summary": {k: _summarize(vs) for k, vs in numerics.items() if vs},
        "top_values": {k: dict(c.most_common(10)) for k, c in top_values.items() if c},
    }

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

