---
name: senior-qa
description: QA workflow for building test strategies and validating releases: risk-based testing, test pyramid decisions, E2E/integration/unit coverage, exploratory testing, and regression planning. Use when creating test plans, reviewing test coverage, triaging flaky tests, or preparing release sign-off criteria.
---

# Senior QA

Optimize for confidence per unit effort.

## Quick Start
1) Identify the risky user journeys (money, auth, data loss, critical flows).
2) Choose the right test layer:
   - unit for logic, integration for boundaries, E2E for key paths
3) Define a release test plan:
   - must-pass automated tests + focused manual checklist
4) Treat flakiness as a product bug: root-cause it and fix it.

## Optional tool: scaffold a test plan doc
```bash
python ~/.codex/skills/senior-qa/scripts/scaffold_test_plan.py . --out docs/qa --force
```

## References
- Test plan template: `references/test-plan.md`

