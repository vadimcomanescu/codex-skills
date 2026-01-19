---
name: file-organizer
description: Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort.
---

# File Organizer

Help users clean up folders with a safe, approval-first workflow.

## Quick Start
1) Confirm scope and exclusions (what to touch vs. avoid).
2) Inventory files and identify duplicates/outliers.
3) Propose a target structure and a dry-run move plan.
4) Execute only after explicit approval.

## Inventory Commands (examples)
```bash
ls -la <target>
find <target> -type f | wc -l
find <target> -type f -maxdepth 2 | sed 's/.*\.//' | sort | uniq -c | sort -rn | head
find <target> -type f -size +200M -print | head
```

## Organization Heuristics
- Group by **type** (docs, images, archives, media, code) or **purpose** (work/personal/archive).
- Prefer stable categories over time-based folders unless the user asks for dates.
- Keep “active” and “archive” separate to reduce clutter.

## Duplicates
- Identify by hash or exact filename+size.
- Always ask before deleting; suggest which to keep based on newest or largest.

## Guardrails
- Never move/delete without approval.
- Avoid renaming when it would break known tooling (build configs, scripts).
- For shared directories, ask before reorganizing.

## References
- Extended examples: `references/examples.md`

