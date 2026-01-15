#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def _read_asset(skill_root: Path, rel_path: str) -> str:
    return (skill_root / "assets" / rel_path).read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bootstrap architecture documentation (ARCHITECTURE.md + ADR template)."
    )
    parser.add_argument("target", nargs="?", default=".", help="Project root (default: .)")
    parser.add_argument(
        "--out",
        default="docs/architecture",
        help="Output directory under the target project (default: docs/architecture)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files if present",
    )
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    out_dir = target / args.out
    adr_dir = out_dir / "adr"
    out_dir.mkdir(parents=True, exist_ok=True)
    adr_dir.mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parent.parent

    architecture_md = out_dir / "ARCHITECTURE.md"
    adr_md = adr_dir / "0001-architecture-decision-record.md"
    context_mmd = out_dir / "context.mmd"

    files = [
        (architecture_md, _read_asset(skill_root, "architecture-template.md")),
        (adr_md, _read_asset(skill_root, "adr-template.md")),
        (context_mmd, _read_asset(skill_root, "mermaid-context-template.mmd")),
    ]

    for path, content in files:
        if path.exists() and not args.force:
            print(f"Exists (skip): {path}")
            continue
        path.write_text(content, encoding="utf-8")
        print(f"Wrote: {path}")


if __name__ == "__main__":
    main()

