#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules"}


def iter_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() in IMAGE_EXTS:
                yield p


def sha256(path: Path, max_bytes: int) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        remaining = max_bytes
        while True:
            chunk = f.read(min(1024 * 1024, remaining))
            if not chunk:
                break
            h.update(chunk)
            remaining -= len(chunk)
            if remaining <= 0:
                break
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory an image dataset folder (no ML deps).")
    parser.add_argument("target", help="Dataset directory")
    parser.add_argument("--out", help="Write JSON report to file (prints to stdout if omitted)")
    parser.add_argument("--hash-bytes", type=int, default=2_000_000, help="Bytes to hash per file (default: 2MB)")
    parser.add_argument("--max-files", type=int, default=200_000, help="Max files to scan (default: 200k)")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")

    by_ext: Dict[str, int] = {}
    by_parent: Dict[str, int] = {}
    sizes: List[int] = []
    hashes: Dict[str, List[str]] = {}

    count = 0
    for p in iter_files(root):
        count += 1
        if count > args.max_files:
            break
        ext = p.suffix.lower()
        by_ext[ext] = by_ext.get(ext, 0) + 1
        rel_parent = str(p.parent.relative_to(root))
        by_parent[rel_parent] = by_parent.get(rel_parent, 0) + 1
        try:
            sizes.append(p.stat().st_size)
        except Exception:
            pass

        try:
            h = sha256(p, args.hash_bytes)
            hashes.setdefault(h, []).append(str(p))
        except Exception:
            continue

    duplicates = {h: ps for h, ps in hashes.items() if len(ps) > 1}

    sizes_sorted = sorted(sizes)
    def pct(x: float) -> int:
        if not sizes_sorted:
            return 0
        i = int((len(sizes_sorted) - 1) * x)
        return sizes_sorted[i]

    report = {
        "target": str(root),
        "file_count": count,
        "by_extension": dict(sorted(by_ext.items(), key=lambda kv: (-kv[1], kv[0]))),
        "by_parent_dir_top20": dict(sorted(by_parent.items(), key=lambda kv: (-kv[1], kv[0]))[:20]),
        "size_bytes": {
            "min": sizes_sorted[0] if sizes_sorted else 0,
            "p50": pct(0.50),
            "p90": pct(0.90),
            "p99": pct(0.99),
            "max": sizes_sorted[-1] if sizes_sorted else 0,
        },
        "duplicate_hashes": {h: ps[:10] for h, ps in duplicates.items()},
        "duplicate_count": len(duplicates),
        "notes": [
            "Duplicates are detected by hashing the first N bytes (see --hash-bytes); confirm before deleting.",
            "Folder counts are by immediate parent relative to the dataset root.",
        ],
    }

    payload = json.dumps(report, indent=2)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload, encoding="utf-8")
        print(f"Wrote: {out_path}")
    else:
        print(payload)


if __name__ == "__main__":
    main()

