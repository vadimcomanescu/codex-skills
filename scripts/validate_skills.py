#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOTS = [
    ROOT / "skills" / ".curated",
    ROOT / "skills" / ".experimental",
]


def iter_skill_dirs(root: Path) -> List[Path]:
    skill_dirs: List[Path] = []
    for entry in sorted(root.iterdir()):
        if not entry.is_dir():
            continue
        # Backwards-compatible: allow skills directly under the tier root.
        if (entry / "SKILL.md").exists():
            skill_dirs.append(entry)
            continue
        # Category folder: collect skills one level deeper.
        for subdir in sorted(entry.iterdir()):
            if not subdir.is_dir():
                continue
            if (subdir / "SKILL.md").exists():
                skill_dirs.append(subdir)
    return skill_dirs


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], List[str]]:
    errors: List[str] = []
    if not text.startswith("---\n"):
        return {}, ["Missing frontmatter start '---'"]
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, ["Missing frontmatter end '---'"]
    fm = parts[1].strip("\n")
    data: Dict[str, str] = {}
    for line in fm.splitlines():
        if "\t" in line:
            errors.append("Frontmatter contains tabs (use spaces)")
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"Invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, errors


def check_skill(skill_dir: Path) -> List[str]:
    errors: List[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"Missing SKILL.md in {skill_dir}"]
    text = skill_md.read_text(encoding="utf-8")
    fm, fm_errors = parse_frontmatter(text)
    errors.extend(fm_errors)

    keys = set(fm.keys())
    if keys != {"name", "description"}:
        errors.append(f"Frontmatter keys must be only name+description, got: {sorted(keys)}")

    name = fm.get("name")
    if not name:
        errors.append("Missing name in frontmatter")
    else:
        if name != skill_dir.name:
            errors.append(f"Skill name '{name}' does not match folder '{skill_dir.name}'")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
            errors.append(f"Skill name '{name}' must be lowercase/digits/hyphens, <=64 chars")

    description = fm.get("description")
    if not description:
        errors.append("Missing description in frontmatter")

    if not (skill_dir / "LICENSE.txt").exists():
        errors.append("Missing LICENSE.txt")

    # Check backtick paths referenced in SKILL.md (ignore fenced code blocks)
    text_no_fences = re.sub(r"```.*?```", "", text, flags=re.S)
    for match in re.findall(r"`([^`]+)`", text_no_fences):
        if any(match.startswith(p) for p in ("http://", "https://")):
            continue
        if match.startswith(("/", "~/")):
            continue
        if any(x in match for x in ("...", "<", ">", "://")):
            continue
        if " " in match or "\n" in match:
            continue
        if match in {"h1", "prefers-reduced-motion", "app/", "pages/", "next/link", "next/image", "next/font"}:
            continue
        if not match.startswith(("references/", "assets/", "scripts/")):
            continue
        candidate = skill_dir / match
        if not candidate.exists():
            errors.append(f"Referenced path missing: `{match}`")

    return errors


def main() -> None:
    missing_roots = [root for root in SKILLS_ROOTS if not root.exists()]
    if missing_roots:
        missing_list = ", ".join(str(root) for root in missing_roots)
        raise SystemExit(f"Missing skills directories: {missing_list}")

    all_errors: List[str] = []
    for root in SKILLS_ROOTS:
        for skill_dir in iter_skill_dirs(root):
            errs = check_skill(skill_dir)
            if errs:
                rel = skill_dir.relative_to(ROOT)
                all_errors.append(f"[{rel.as_posix()}]")
                all_errors.extend([f"  - {e}" for e in errs])

    if all_errors:
        print("Skill validation failed:\n" + "\n".join(all_errors))
        raise SystemExit(1)

    print("All skills validated OK.")


if __name__ == "__main__":
    main()
