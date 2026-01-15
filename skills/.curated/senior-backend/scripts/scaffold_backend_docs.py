#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold backend design docs.")
    parser.add_argument("target", nargs="?", default=".", help="Project root (default: .)")
    parser.add_argument("--out", default="docs/backend", help="Output directory under project (default: docs/backend)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    out_dir = target / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parent.parent
    template = (skill_root / "assets" / "backend-design-template.md").read_text(encoding="utf-8")
    out_file = out_dir / "BACKEND_DESIGN.md"

    if out_file.exists() and not args.force:
        print(f"Exists (skip): {out_file}")
        return

    out_file.write_text(template, encoding="utf-8")
    print(f"Wrote: {out_file}")


if __name__ == "__main__":
    main()

