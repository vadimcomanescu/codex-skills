# Repository Guidelines

## Project Structure & Module Organization
This repository is a Codex skill catalog. Keep skills self-contained and organized under `skills/`:

- `skills/.experimental/<category>/<skill-name>/SKILL.md`: entrypoint and workflow for a single skill (required).
- `skills/.experimental/<category>/<skill-name>/references/`: optional docs/links the skill relies on.
- `skills/.experimental/<category>/<skill-name>/scripts/`: optional helper scripts used by the skill.
- `skills/.experimental/<category>/<skill-name>/assets/`: optional templates, examples, or UI assets.

When a skill is stable, promote it to `skills/.curated/<category>/<skill-name>/`.

Keep each skill self-contained. If you introduce shared utilities, place them in `shared/` and document the dependency in each skill’s `SKILL.md`.

## Build, Test, and Development Commands
No build/test automation is configured yet. Until it exists, use lightweight checks:

- `git status`: confirm only intended files changed.
- `git diff`: review the final patch before committing.
- `python scripts/validate_skills.py`: validate SKILL frontmatter, required files, and referenced paths.

If you add runnable code (Node/Python/etc.), add a single canonical entry point (e.g., `package.json` scripts or a `Makefile`) and update this section with commands like `make lint`, `make test`, and `make fmt`.

## Coding Style & Naming Conventions
- Indentation: 2 spaces for Markdown lists; avoid hard tabs.
- Filenames: use `kebab-case` for skill directories (e.g., `skills/.curated/design/frontend-design/`).
- Skill docs: keep `SKILL.md` task-focused, with numbered steps and short examples (commands and paths in backticks).
- For long examples or tutorials, move content to `references/examples.md` and link it from `SKILL.md`.
- Scripts: prefer small, composable scripts with clear usage (`--help` or header comments) and deterministic output.

## Testing Guidelines
When a skill includes executable scripts, add a minimal smoke test and document how to run it. Recommended patterns:

- Tests live in `skills/.experimental/<category>/<skill-name>/tests/` (or `skills/.curated/<category>/<skill-name>/tests/`) or a top-level `tests/`.
- Name tests by behavior (e.g., `test_generate_plan.sh`, `test_parse_config.py`).

## Commit & Pull Request Guidelines
There is no established Git history yet. Use clear, conventional commit messages:

- `feat: add <skill-name> skill`
- `fix: correct <skill-name> instructions`
- `docs: update contributor guidance`

For pull requests, include: a short summary, example usage (copy/pastable commands), and any assumptions/limitations. Never commit secrets; prefer `.env.example` and document required configuration.
