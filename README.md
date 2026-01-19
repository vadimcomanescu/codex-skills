# Codex Skills Catalog

[![Validate Skills](https://github.com/vadimcomanescu/codex-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/vadimcomanescu/codex-skills/actions/workflows/validate-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Installable skills for Codex. This repository is a “skills catalog”: each skill lives under `skills/` and can be installed into your local Codex skills directory (typically `~/.codex/skills`).

## Contents
- [Install](#install)
- [Skills](#skills)
- [Experimental Skills](#experimental-skills)
- [Repository Layout](#repository-layout)
- [Validation](#validation)
- [Contributing](#contributing)
- [License](#license)

## Install

Codex skills can be installed directly from a GitHub folder path.

### Option A: Install by URL (recommended)
In Codex, ask:

“Install the skill from `https://github.com/vadimcomanescu/codex-skills/tree/main/skills/.curated/frontend-design`”

To install a different skill, swap the final path segment (e.g. `skills/.curated/code-reviewer`).
For experimental skills, use `skills/.experimental/<skill-name>` and expect breaking changes.

### Option B: Install by script (copy/paste)
```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo vadimcomanescu/codex-skills \
  --path skills/.curated/frontend-design
```

### Install multiple skills in one shot
```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo vadimcomanescu/codex-skills \
  --path skills/.curated/frontend-design \
  --path skills/.curated/code-reviewer \
  --path skills/.curated/security-compliance
```

Restart Codex after installing to pick up new skills.

## Skills

All skills listed below are in the `curated` tier (stable and recommended).

| Skill | What it’s for | Install path |
| --- | --- | --- |
| `code-reviewer` | High-signal PR/diff review workflow + review report generator | `skills/.curated/code-reviewer` |
| `frontend-design` | Next.js App Router–first UI redesigns with bold aesthetics, motion, accessibility, and AI-native UX patterns | `skills/.curated/frontend-design` |
| `information-architect` | Information architecture workflows: navigation, sitemaps, taxonomy, labeling, content models, and findability | `skills/.curated/information-architect` |
| `security-compliance` | Threat modeling, controls checklists, lightweight secrets scanning | `skills/.curated/security-compliance` |
| `senior-architect` | System design + architecture docs (ADRs, Mermaid diagrams, trade-offs) and lightweight repo analysis | `skills/.curated/senior-architect` |
| `senior-backend` | Backend API/service design workflows + backend design doc scaffold | `skills/.curated/senior-backend` |
| `senior-computer-vision` | CV system workflow + dataset inventory tooling (no ML deps) | `skills/.curated/senior-computer-vision` |
| `senior-data-engineer` | Pipeline/data contract workflows + lightweight CSV profiling | `skills/.curated/senior-data-engineer` |
| `senior-data-scientist` | Metrics/experiments/modeling workflow + CSV profiling | `skills/.curated/senior-data-scientist` |
| `senior-devops` | CI/CD, ops readiness, observability, safe deployments + repo ops inventory | `skills/.curated/senior-devops` |
| `senior-prompt-engineer` | Prompt design + eval scaffolding | `skills/.curated/senior-prompt-engineer` |
| `senior-qa` | Risk-based QA strategy + test plan scaffold | `skills/.curated/senior-qa` |
| `senior-secops` | Incident/vuln triage workflow + log summary tooling | `skills/.curated/senior-secops` |
| `test-driven-development` | TDD workflow (red/green/refactor) + testing anti-patterns | `skills/.curated/test-driven-development` |
| `webapp-testing` | Local UI testing with Playwright + `with_server.py` helper | `skills/.curated/webapp-testing` |

## Experimental Skills

Experimental skills are usable but still changing. Expect breaking changes to prompts, assets, or scripts.

| Skill | What it’s for | Install path |
| --- | --- | --- |
| `accessibility-auditor` | WCAG audits, ARIA implementation, inclusive design remediation | `skills/.experimental/accessibility-auditor` |
| `agents-crewai` | CrewAI agent team design and orchestration | `skills/.experimental/agents-crewai` |
| `api-integration-specialist` | Third-party API integrations with auth, retries, and rate limits | `skills/.experimental/api-integration-specialist` |
| `changelog-generator` | Turn git history into user-friendly changelogs | `skills/.experimental/changelog-generator` |
| `dispatching-parallel-agents` | Split complex tasks into parallel agent workloads | `skills/.experimental/dispatching-parallel-agents` |
| `error-resolver` | Reproduce, isolate, and fix failing errors safely | `skills/.experimental/error-resolver` |
| `feature-design-assistant` | Turn ideas into specs with scope, risks, and acceptance criteria | `skills/.experimental/feature-design-assistant` |
| `file-organizer` | Safe file/folder cleanup and organization workflows | `skills/.experimental/file-organizer` |
| `finishing-a-development-branch` | Finalize branches with clean status and checks | `skills/.experimental/finishing-a-development-branch` |
| `gh-address-comments` | Address GitHub PR comments with `gh` | `skills/.experimental/gh-address-comments` |
| `gh-fix-ci` | Inspect PR checks via `gh` and fix failing CI | `skills/.experimental/gh-fix-ci` |
| `git-commit-helper` | Craft clear, conventional commits | `skills/.experimental/git-commit-helper` |
| `meeting-insights-analyzer` | Extract communication insights from meeting transcripts | `skills/.experimental/meeting-insights-analyzer` |
| `planning-with-files` | Persistent markdown planning and tracking | `skills/.experimental/planning-with-files` |
| `product-manager-toolkit` | PRDs, RICE, discovery synthesis, prioritization | `skills/.experimental/product-manager-toolkit` |
| `senior-frontend` | Production frontend workflows and scaffolding | `skills/.experimental/senior-frontend` |
| `senior-fullstack` | Full-stack architecture and scaffolding workflows | `skills/.experimental/senior-fullstack` |
| `systematic-debugging` | Root-cause debugging before fixes | `skills/.experimental/systematic-debugging` |
| `ui-design-system` | Design system tooling and token generation | `skills/.experimental/ui-design-system` |
| `using-git-worktrees` | Create isolated git worktrees safely | `skills/.experimental/using-git-worktrees` |

## Repository Layout

This repo mirrors the common Codex “catalog” layout:
- `skills/.curated/`: stable, recommended skills.
- `skills/.experimental/`: works-in-progress (APIs and wording may change more frequently).

Each skill folder contains:
- `SKILL.md`: the entrypoint. YAML frontmatter is intentionally minimal (`name` + `description`).
- `LICENSE.txt`: license for that skill’s contents.
- Optional `references/`, `assets/`, and `scripts/`.

## Validation

Run the local validator before pushing:
```bash
python scripts/validate_skills.py
```

CI runs the same validator on PRs and pushes to `main`.

## Contributing

- Keep skills self-contained and avoid adding new runtime dependencies unless necessary.
- Prefer small, copy/pasteable assets that work in real repos (for `frontend-design`, assume Next.js **App Router**).
- Keep `SKILL.md` concise; move deep detail into `references/` (progressive disclosure).

## Sources & Acknowledgements

We keep a list of upstream sources we reference for ideas, patterns, and skills and acknowledge them here:

- `https://github.com/davila7/claude-code-templates`
- `https://github.com/anthropics/skills`
- `https://github.com/openai/skills`
- Run `python scripts/validate_skills.py` before opening a PR.

## License

Repository license: see `LICENSE`. Individual skills include a per-skill `LICENSE.txt`.
