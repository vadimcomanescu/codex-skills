#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a prompt + eval template directory.")
    parser.add_argument("target", nargs="?", default=".", help="Project root (default: .)")
    parser.add_argument("--out", default="evals/prompt_eval", help="Output directory under project")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")

    out_dir = root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    skill_root = Path(__file__).resolve().parent.parent
    prompt_src = (skill_root / "assets" / "prompt-template.md").read_text(encoding="utf-8")
    eval_src = (skill_root / "assets" / "eval-template.json").read_text(encoding="utf-8")

    prompt_dst = out_dir / "PROMPT.md"
    eval_dst = out_dir / "eval.json"

    for dst, content in [(prompt_dst, prompt_src), (eval_dst, eval_src)]:
        if dst.exists() and not args.force:
            print(f"Exists (skip): {dst}")
            continue
        dst.write_text(content, encoding="utf-8")
        print(f"Wrote: {dst}")


if __name__ == "__main__":
    main()

