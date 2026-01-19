# Skills

This directory follows the same conventions as skill catalogs with category groupings:

- `skills/.experimental/<category>/<skill-name>/`: work-in-progress skills.
- `skills/.curated/<category>/<skill-name>/`: stable, recommended skills.

## Skill Folder Requirements
Each skill folder must contain:

- `SKILL.md`: the skill entrypoint (YAML frontmatter + instructions).
- `LICENSE.txt`: license for that skill’s contents.

Optional:
- `references/`: supporting docs used by the skill.
- `assets/`: templates/starter files.
- `scripts/`: helper scripts invoked by the skill.

## Naming
- Folder names use `kebab-case` and should match the skill’s frontmatter `name`.
- Example path: `skills/.curated/design/frontend-design/`.
