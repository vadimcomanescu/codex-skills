#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


PATTERNS: List[re.Pattern[str]] = [
    re.compile(r"AKIA[0-9A-Z]{16}"),  # AWS access key id
    re.compile(r"-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----"),
    re.compile(r"(?i)\b(xox[baprs]-[0-9A-Za-z-]{10,})\b"),  # slack tokens
    re.compile(r"(?i)\bghp_[0-9A-Za-z]{30,}\b"),  # GitHub classic token
    re.compile(r"(?i)\bgithub_pat_[0-9A-Za-z_]{20,}\b"),  # GitHub fine-grained token
]

SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", "__pycache__", ".venv", "venv"}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    match: str


def iter_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_symlink():
                continue
            # Skip huge binaries by extension heuristic
            if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".gz", ".mp4"}:
                continue
            yield p


def scan_file(path: Path, max_bytes: int) -> List[Finding]:
    try:
        data = path.read_bytes()
    except Exception:
        return []
    if len(data) > max_bytes:
        return []
    text = data.decode("utf-8", errors="replace")
    findings: List[Finding] = []
    for i, line in enumerate(text.splitlines(), start=1):
        for pat in PATTERNS:
            m = pat.search(line)
            if m:
                findings.append(Finding(str(path), i, m.group(0)[:120]))
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan a directory for likely secrets (heuristic).")
    parser.add_argument("target", nargs="?", default=".", help="Directory to scan (default: .)")
    parser.add_argument("--max-bytes", type=int, default=300_000, help="Skip files larger than this (default: 300k)")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    parser.add_argument("--output", help="Write JSON output to a file")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")

    findings: List[Finding] = []
    for f in iter_files(root):
        findings.extend(scan_file(f, args.max_bytes))

    payload: Dict[str, object] = {
        "target": str(root),
        "count": len(findings),
        "findings": [f.__dict__ for f in findings],
    }

    if args.json or args.output:
        out = json.dumps(payload, indent=2)
        if args.output:
            Path(args.output).write_text(out, encoding="utf-8")
        else:
            print(out)
        return

    print(f"Target: {root}")
    print(f"Findings: {len(findings)}")
    for f in findings[:50]:
        print(f"- {f.path}:{f.line} {f.match}")
    if len(findings) > 50:
        print(f"(truncated; {len(findings) - 50} more)")


if __name__ == "__main__":
    main()
