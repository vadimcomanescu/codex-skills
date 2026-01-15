#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATES = [
    "IA.md",
    "SITEMAP.mmd",
    "NAVIGATION.md",
    "TAXONOMY.csv",
    "CONTENT_MODEL.md",
    "CONTENT_INVENTORY.csv",
    "DECISIONS.md",
]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold an information architecture documentation pack (docs/ia)."
    )
    parser.add_argument("target", nargs="?", default=".", help="Project root (default: .)")
    parser.add_argument("--out", default="docs/ia", help="Output directory under project (default: docs/ia)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")

    out_dir = root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parent.parent
    template_dir = skill_root / "assets" / "ia-docs"

    missing = [name for name in TEMPLATES if not (template_dir / name).exists()]
    if missing:
        raise SystemExit(f"Missing template(s) in {template_dir}: {', '.join(missing)}")

    for name in TEMPLATES:
        src = template_dir / name
        dst = out_dir / name

        if dst.exists() and not args.force:
            print(f"Exists (skip): {dst}")
            continue

        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Wrote: {dst}")


if __name__ == "__main__":
    main()

