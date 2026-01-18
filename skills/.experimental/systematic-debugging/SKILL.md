---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

Always investigate root cause before proposing fixes.

## Core Rule
No fixes without root-cause investigation.

## Workflow
1) **Reproduce**: capture exact steps and error output.
2) **Localize**: find the smallest failing scope (file, test, input).
3) **Trace**: follow data and control flow to the first wrong state.
4) **Fix**: smallest change that addresses the root cause.
5) **Verify**: re-run the failing test/flow and any related checks.

## When stuck
- Add diagnostic logging at component boundaries.
- Create a minimal reproduction case.
- Use bisect to isolate the introduction point.

## References
- Root-cause tracing: `references/root-cause-tracing.md`
- Defense-in-depth fixes: `references/defense-in-depth.md`
- Condition-based waiting: `references/condition-based-waiting.md`
- Extended examples: `references/examples.md`

