#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple


LEVEL_RE = re.compile(r"\b(ERROR|WARN|WARNING|INFO|DEBUG|CRITICAL|FATAL)\b", re.I)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a text log file for quick triage.")
    parser.add_argument("path", help="Log file path")
    parser.add_argument("--out", help="Write JSON output to file (prints to stdout if omitted)")
    parser.add_argument("--max-lines", type=int, default=200_000, help="Max lines to scan (default: 200k)")
    args = parser.parse_args()

    p = Path(args.path).resolve()
    if not p.exists():
        raise SystemExit(f"File does not exist: {p}")

    levels = Counter()
    top_lines = Counter()

    lines = 0
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        lines += 1
        if lines > args.max_lines:
            break
        m = LEVEL_RE.search(line)
        if m:
            levels[m.group(1).upper()] += 1
        # normalize numbers/ids to reduce cardinality
        normalized = re.sub(r"\b[0-9a-f]{8,}\b", "<id>", line, flags=re.I)
        normalized = re.sub(r"\b\d+\b", "<n>", normalized)
        if len(normalized) < 300:
            top_lines[normalized] += 1

    report: Dict[str, Any] = {
        "path": str(p),
        "lines_scanned": lines,
        "levels": dict(levels),
        "top_lines": top_lines.most_common(20),
        "notes": [
            "This is a heuristic summary; use it to find patterns, then inspect raw logs around spikes.",
            "Consider correlating with request IDs, user IDs (if safe), and timestamps.",
        ],
    }

    payload = json.dumps(report, indent=2)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
        print(f"Wrote: {out}")
    else:
        print(payload)


if __name__ == "__main__":
    main()
