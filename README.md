# Codex Skills Catalog

Installable skills for Codex. This repo is structured as a skills “catalog”: each skill lives in its own folder under `skills/` and can be installed into `~/.codex/skills` via the built-in Skill Installer.

## Available Skills

| Skill | Tier | What it’s for | Install path |
| --- | --- | --- | --- |
| `frontend-design` | curated | Next.js App Router–first UI redesigns with bold aesthetics, motion, and accessibility | `skills/.curated/frontend-design` |

## Install

### Option A: Install by URL (recommended)
In Codex, ask:

“Install the skill from `https://github.com/<owner>/<repo>/tree/main/skills/.curated/frontend-design`”

### Option B: Install by script (copy/paste)
```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo <owner>/<repo> \
  --path skills/.curated/frontend-design
```

Restart Codex after installing to pick up new skills.

## Layout
- `skills/.curated/`: stable, recommended skills.
- `skills/.experimental/`: works-in-progress (may change more frequently).

Each skill folder contains:
- `SKILL.md`: the entrypoint (YAML frontmatter + workflow).
- `LICENSE.txt`: license for that skill’s contents.
- Optional `references/`, `assets/`, and `scripts/`.

## Contributing
- Keep skills self-contained and avoid adding new runtime dependencies unless necessary.
- Prefer small, copy/pasteable assets that work in real repos (for `frontend-design`, assume Next.js **App Router**).
- Update `AGENTS.md` when conventions change.

## License
Repository license: see `LICENSE`. Individual skills also include a per-skill `LICENSE.txt`.
