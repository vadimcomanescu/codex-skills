#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a QA test plan document.")
    parser.add_argument("target", nargs="?", default=".", help="Project root (default: .)")
    parser.add_argument("--out", default="docs/qa", help="Output directory under project (default: docs/qa)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")

    out_dir = root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parent.parent
    template = (skill_root / "assets" / "test-plan-template.md").read_text(encoding="utf-8")
    dst = out_dir / "TEST_PLAN.md"

    if dst.exists() and not args.force:
        print(f"Exists (skip): {dst}")
        return

    dst.write_text(template, encoding="utf-8")
    print(f"Wrote: {dst}")


if __name__ == "__main__":
    main()

