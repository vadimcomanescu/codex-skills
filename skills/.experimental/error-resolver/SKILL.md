---
name: error-resolver
description: Use when debugging errors, crashes, or failing commands. Focus on reproducing the issue, isolating the root cause, and producing a minimal, safe fix with validation steps.
---

# Error Resolver

Diagnose failures methodically and propose safe, verified fixes.

## Quick Start
1) Reproduce and capture the exact error message.
2) Isolate the smallest repro or failing test.
3) Identify root cause before proposing changes.
4) Apply the smallest fix and re-verify.

## Debugging Checklist
- Read stack traces top-to-bottom.
- Check recent changes (diff, dependency updates).
- Validate environment (versions, env vars, config).
- Confirm inputs and assumptions.

## Fix Criteria
- Fix targets the root cause, not the symptom.
- Tests or manual verification are specified.
- Any side effects or trade-offs are called out.

## Guardrails
- Don’t apply changes without confirming the root cause.
- For production issues, include rollback steps.

## References
- Extended examples: `references/examples.md`

