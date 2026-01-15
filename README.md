# Codex Skills Catalog

Installable skills for Codex. This repo is structured as a skills “catalog”: each skill lives in its own folder under `skills/` and can be installed into `~/.codex/skills` via the built-in Skill Installer.

## Available Skills

| Skill | Tier | What it’s for | Install path |
| --- | --- | --- | --- |
| `code-reviewer` | curated | High-signal PR/diff review workflow + review report generator | `skills/.curated/code-reviewer` |
| `frontend-design` | curated | Next.js App Router–first UI redesigns with bold aesthetics, motion, and accessibility | `skills/.curated/frontend-design` |
| `security-compliance` | curated | Threat modeling, controls checklists, lightweight secrets scanning | `skills/.curated/security-compliance` |
| `senior-architect` | curated | System design + architecture docs (ADRs, Mermaid diagrams, trade-offs) and lightweight repo analysis | `skills/.curated/senior-architect` |
| `senior-backend` | curated | Backend API/service design workflows + backend design doc scaffold | `skills/.curated/senior-backend` |
| `senior-computer-vision` | curated | CV system workflow + dataset inventory tooling (no ML deps) | `skills/.curated/senior-computer-vision` |
| `senior-data-engineer` | curated | Pipeline/data contract workflows + lightweight CSV profiling | `skills/.curated/senior-data-engineer` |
| `senior-data-scientist` | curated | Metrics/experiments/modeling workflow + CSV profiling | `skills/.curated/senior-data-scientist` |
| `senior-devops` | curated | CI/CD, ops readiness, observability, safe deployments + repo ops inventory | `skills/.curated/senior-devops` |
| `senior-prompt-engineer` | curated | Prompt design + eval scaffolding | `skills/.curated/senior-prompt-engineer` |
| `senior-qa` | curated | Risk-based QA strategy + test plan scaffold | `skills/.curated/senior-qa` |
| `senior-secops` | curated | Incident/vuln triage workflow + log summary tooling | `skills/.curated/senior-secops` |
| `test-driven-development` | curated | TDD workflow (red/green/refactor) + testing anti-patterns | `skills/.curated/test-driven-development` |
| `webapp-testing` | curated | Local UI testing with Playwright + `with_server.py` helper | `skills/.curated/webapp-testing` |

## Install

### Option A: Install by URL (recommended)
In Codex, ask:

“Install the skill from `https://github.com/<owner>/<repo>/tree/main/skills/.curated/frontend-design`”

Swap the path to install a different skill (e.g., `skills/.curated/code-reviewer`).

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
