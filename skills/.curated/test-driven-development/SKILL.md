---
name: test-driven-development
description: Test-driven development workflow (red → green → refactor) for features, bug fixes, and refactors. Use when implementing behavior changes and you want to drive design via tests, prevent regressions, and keep code modular and well-factored.
---

# Test-Driven Development

Write the test first, then write the smallest change that makes it pass, then refactor safely.

## Core loop
1) **Red**: write a failing test that expresses the desired behavior.
2) **Green**: implement the minimum change to pass.
3) **Refactor**: improve structure while keeping tests green.

## Quick Start
- Start from the public interface (API, function, UI behavior), not private helpers.
- Prefer “behavioral” test names (what), not “implementation” names (how).
- When fixing bugs: reproduce with a test first.

## Guardrails
- Don’t over-mock: prefer integration at boundaries; mock only slow/flaky externals.
- Keep tests deterministic: control time, randomness, and network.
- If a test is hard to write, your design likely needs an interface seam.

## References
- Common anti-patterns: `references/testing-anti-patterns.md`

