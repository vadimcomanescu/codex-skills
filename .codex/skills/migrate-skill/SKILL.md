---
name: migrate-skill
description: Import external skills into this repo from a URL (single skill or directory). Use when migrating skills from other catalogs, ensuring correct structure, licensing, and validation.
---

# Migrate Skill

Use the $skill-creator skill to guide the creation/update workflow for each imported skill.

## Inputs to collect
1) Source URL.
   - Accept a direct skill folder URL or a directory containing multiple skills.
2) Scope.
   - Single skill or directory of skills (infer; ask if ambiguous).
3) Destination.
   - Tier: curated or experimental (default to experimental).
   - Category: one of `design`, `platform`, `data`, `quality`, `security`, `ai`, `product`, `devtools` (infer; ask if unclear).

## Migration workflow
1) Inspect the source at the URL and identify skill folders (`SKILL.md` + `LICENSE.txt`).
2) For each skill:
   - Place at `skills/.<tier>/<category>/<skill-name>/`.
   - Keep `SKILL.md` frontmatter limited to `name` and `description`.
   - Keep instructions concise, task-focused, with numbered steps.
   - Preserve attribution in `LICENSE.txt` (add upstream credits if present).
   - Keep skills self-contained; if shared utilities are needed, put them in `shared/` and reference from `SKILL.md`.
3) Run `python scripts/validate_skills.py` and fix any errors.
4) Summarize: what was imported, where it landed, and any assumptions/questions.
