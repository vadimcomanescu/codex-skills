---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans. Create isolated git worktrees with safe directory selection and baseline verification.
---

# Using Git Worktrees

Create isolated workspaces without disrupting the main working tree.

## Quick Start
1) Choose a worktree root (prefer `.worktrees/` if present).
2) Ensure the worktree path is ignored by git.
3) Create the worktree for the target branch.
4) Run project setup and verify clean status.

## Guardrails
- Don’t create worktrees in unignored paths.
- Keep one branch per worktree.
- Verify `git status` is clean before starting work.

## References
- Extended examples: `references/examples.md`
