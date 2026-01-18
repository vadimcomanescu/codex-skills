---
name: code-reviewer
description: "High-signal code review workflow for pull requests and patches: correctness, readability, API/UX, performance, security, and maintainability. Use when reviewing diffs/PRs, writing review comments, proposing fixes, or producing a structured review report with actionable follow-ups."
---

# Code Reviewer

Give reviews that help the author ship safely and quickly.

## Quick Start
1) Understand intent: what’s the user-facing / system-facing change and why?
2) Review in this order:
   - Correctness (edge cases, invariants, error handling)
   - Safety (security + data handling + secrets)
   - Maintainability (structure, naming, interfaces)
   - Performance (hot paths, I/O, allocations, DB queries)
   - Tests (do they fail before the fix? do they cover the right behavior?)
3) Leave comments that are:
   - **Actionable** (what to change) + **why** (risk/benefit) + **scope** (must vs nice-to-have)

## Large diff triage (use when the change is big)
- Start with the entrypoints and high-risk files (auth, payments, data writes).
- Identify invariants the change must preserve, then hunt for violations.
- Skim for mechanical changes and collapse them; focus deep review on behavioral deltas.

## When to request changes
- Bugs or correctness issues that can ship user-impacting failures.
- Security/privacy regressions or data handling gaps.
- Missing or inadequate tests for new behavior or fixed bugs.

## Output format (recommended)
- **Summary**: what the change does
- **Major issues**: must-fix items (blockers)
- **Minor suggestions**: improvements / nits
- **Test plan**: how to validate locally/CI
- **Follow-ups**: tickets/cleanup that shouldn’t block merge

## Optional tool: generate a review report from git diff
From the repo you’re reviewing:
```bash
python ~/.codex/skills/code-reviewer/scripts/review_diff.py --base origin/main --out /tmp/review.md
```

## References
- Review checklist and comment style: `references/review-checklist.md`
