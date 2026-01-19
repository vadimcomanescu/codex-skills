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

“Install the skill from `https://github.com/vadimcomanescu/codex-skills/tree/main/skills/.curated/design/frontend-design`”

To install a different skill, swap the category + skill segments (e.g. `skills/.curated/quality/code-reviewer`).
For experimental skills, use `skills/.experimental/<category>/<skill-name>` and expect breaking changes.

### Option B: Install by script (copy/paste)
```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo vadimcomanescu/codex-skills \
  --path skills/.curated/design/frontend-design
```

### Install multiple skills in one shot
```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo vadimcomanescu/codex-skills \
  --path skills/.curated/design/frontend-design \
  --path skills/.curated/quality/code-reviewer \
  --path skills/.curated/security/security-compliance
```

Restart Codex after installing to pick up new skills.

## Skills

All skills listed below are in the `curated` tier (stable and recommended).

### Design (`design`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `frontend-design` | Next.js App Router–first UI redesigns with bold aesthetics, motion, accessibility, and AI-native UX patterns | `skills/.curated/design/frontend-design` |
| `information-architect` | Information architecture workflows: navigation, sitemaps, taxonomy, labeling, content models, and findability | `skills/.curated/design/information-architect` |

### Platform (`platform`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `senior-architect` | System design + architecture docs (ADRs, Mermaid diagrams, trade-offs) and lightweight repo analysis | `skills/.curated/platform/senior-architect` |
| `senior-backend` | Backend API/service design workflows + backend design doc scaffold | `skills/.curated/platform/senior-backend` |
| `senior-devops` | CI/CD, ops readiness, observability, safe deployments + repo ops inventory | `skills/.curated/platform/senior-devops` |

### Data (`data`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `senior-computer-vision` | CV system workflow + dataset inventory tooling (no ML deps) | `skills/.curated/data/senior-computer-vision` |
| `senior-data-engineer` | Pipeline/data contract workflows + lightweight CSV profiling | `skills/.curated/data/senior-data-engineer` |
| `senior-data-scientist` | Metrics/experiments/modeling workflow + CSV profiling | `skills/.curated/data/senior-data-scientist` |

### Quality (`quality`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `code-reviewer` | High-signal PR/diff review workflow + review report generator | `skills/.curated/quality/code-reviewer` |
| `senior-qa` | Risk-based QA strategy + test plan scaffold | `skills/.curated/quality/senior-qa` |
| `test-driven-development` | TDD workflow (red/green/refactor) + testing anti-patterns | `skills/.curated/quality/test-driven-development` |
| `webapp-testing` | Local UI testing with Playwright + `with_server.py` helper | `skills/.curated/quality/webapp-testing` |

### Security (`security`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `security-compliance` | Threat modeling, controls checklists, lightweight secrets scanning | `skills/.curated/security/security-compliance` |
| `senior-secops` | Incident/vuln triage workflow + log summary tooling | `skills/.curated/security/senior-secops` |

### AI (`ai`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `senior-prompt-engineer` | Prompt design + eval scaffolding | `skills/.curated/ai/senior-prompt-engineer` |

## Experimental Skills

Experimental skills are usable but still changing. Expect breaking changes to prompts, assets, or scripts.

### Design (`design`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `accessibility-auditor` | WCAG audits, ARIA implementation, inclusive design remediation | `skills/.experimental/design/accessibility-auditor` |
| `ui-design-system` | Design system tooling and token generation | `skills/.experimental/design/ui-design-system` |

### Platform (`platform`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `react-best-practices` | Vercel React/Next.js performance and architecture best practices | `skills/.experimental/platform/react-best-practices` |
| `senior-frontend` | Production frontend workflows and scaffolding | `skills/.experimental/platform/senior-frontend` |
| `senior-fullstack` | Full-stack architecture and scaffolding | `skills/.experimental/platform/senior-fullstack` |

### Quality (`quality`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `error-resolver` | Reproduce, isolate, and fix failing errors safely | `skills/.experimental/quality/error-resolver` |
| `gh-fix-ci` | Inspect PR checks via `gh` and fix failing CI | `skills/.experimental/quality/gh-fix-ci` |
| `systematic-debugging` | Root-cause debugging before fixes | `skills/.experimental/quality/systematic-debugging` |

### AI (`ai`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `audiocraft-audio-generation` | AudioCraft text-to-music and text-to-audio generation with MusicGen and AudioGen | `skills/.experimental/ai/audiocraft-audio-generation` |
| `agents-crewai` | CrewAI agent team design and orchestration | `skills/.experimental/ai/agents-crewai` |
| `api-integration-specialist` | Third-party API integrations with auth, retries, and rate limits | `skills/.experimental/ai/api-integration-specialist` |
| `dispatching-parallel-agents` | Split complex tasks into parallel agent workloads | `skills/.experimental/ai/dispatching-parallel-agents` |

### Product (`product`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `feature-design-assistant` | Turn ideas into specs with scope, risks, and acceptance criteria | `skills/.experimental/product/feature-design-assistant` |
| `meeting-insights-analyzer` | Extract communication insights from meeting transcripts | `skills/.experimental/product/meeting-insights-analyzer` |
| `planning-with-files` | Persistent markdown planning and tracking | `skills/.experimental/product/planning-with-files` |
| `product-manager-toolkit` | PRDs, RICE, discovery synthesis, prioritization | `skills/.experimental/product/product-manager-toolkit` |

### Devtools (`devtools`)
| Skill | What it’s for | Install path |
| --- | --- | --- |
| `changelog-generator` | Turn git history into user-friendly changelogs | `skills/.experimental/devtools/changelog-generator` |
| `file-organizer` | Safe file/folder cleanup and organization workflows | `skills/.experimental/devtools/file-organizer` |
| `finishing-a-development-branch` | Finalize branches with clean status and checks | `skills/.experimental/devtools/finishing-a-development-branch` |
| `gh-address-comments` | Address GitHub PR comments with `gh` | `skills/.experimental/devtools/gh-address-comments` |
| `git-commit-helper` | Craft clear, conventional commits | `skills/.experimental/devtools/git-commit-helper` |
| `using-git-worktrees` | Create isolated git worktrees safely | `skills/.experimental/devtools/using-git-worktrees` |

## Repository Layout

This repo mirrors the common Codex “catalog” layout with categories:
- `skills/.curated/<category>/<skill-name>/`: stable, recommended skills.
- `skills/.experimental/<category>/<skill-name>/`: works-in-progress (APIs and wording may change more frequently).

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
