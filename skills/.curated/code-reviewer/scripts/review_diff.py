#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple


RISK_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("TODO/FIXME", re.compile(r"\b(TODO|FIXME|HACK)\b")),
    ("potential secret", re.compile(r"(AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH) PRIVATE KEY)", re.I)),
    ("command execution", re.compile(r"\b(os\.system|subprocess\.|exec\(|eval\()")),
    ("unsafe serialization", re.compile(r"\b(pickle\.loads|yaml\.load\()")),
]


def _run(cmd: List[str]) -> str:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or f"Command failed: {' '.join(cmd)}")
    return p.stdout


def _git(args: List[str]) -> str:
    return _run(["git", *args])


def _changed_files(base: str) -> List[str]:
    out = _git(["diff", "--name-only", f"{base}...HEAD"])
    return [l.strip() for l in out.splitlines() if l.strip()]


def _diff_text(base: str, max_bytes: int) -> str:
    out = _git(["diff", f"{base}...HEAD"])
    data = out.encode("utf-8", errors="replace")
    if len(data) > max_bytes:
        data = data[:max_bytes] + b"\n\n# [truncated]\n"
    return data.decode("utf-8", errors="replace")


def _scan_risks(diff: str) -> List[str]:
    hits: List[str] = []
    for label, pat in RISK_PATTERNS:
        if pat.search(diff):
            hits.append(label)
    return hits


def _render_report(base: str, files: List[str], risks: List[str]) -> str:
    file_lines = "\n".join([f"- `{f}`" for f in files]) if files else "- (none)"
    risk_lines = "\n".join([f"- {r}" for r in risks]) if risks else "- (none detected)"

    return f"""# Code Review Report

## Summary
- What does this change do?
- What is the user/system impact?

## Changed files
{file_lines}

## Major issues (must-fix)
- [ ] (fill in)

## Minor suggestions (nice-to-have)
- [ ] (fill in)

## Risks detected (heuristic)
{risk_lines}

## Test plan
- [ ] How to run tests locally
- [ ] What to manually verify (if needed)

## Follow-ups
- [ ] (non-blocking cleanup)
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a review report from git diff.")
    parser.add_argument("--base", default="origin/main", help="Base ref to diff against (default: origin/main)")
    parser.add_argument("--out", default="/tmp/review.md", help="Output markdown path (default: /tmp/review.md)")
    parser.add_argument("--max-diff-bytes", type=int, default=400_000, help="Max diff bytes to scan (default: 400k)")
    args = parser.parse_args()

    try:
        _git(["rev-parse", "--is-inside-work-tree"])
    except Exception as e:
        raise SystemExit(f"Not a git repo (run from a repo root): {e}")

    files = _changed_files(args.base)
    diff = _diff_text(args.base, args.max_diff_bytes)
    risks = _scan_risks(diff)
    report = _render_report(args.base, files, risks)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
