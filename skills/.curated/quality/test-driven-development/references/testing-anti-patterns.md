# Testing Anti-Patterns (quick list)

- **Testing implementation details**: breaks on refactors and gives false confidence.
- **Over-mocking**: tests pass while the real system is broken.
- **Snapshot everything**: hides intent; use targeted assertions.
- **Flaky tests**: time/network/randomness not controlled; fix root cause immediately.
- **No failure-path tests**: errors and edge cases are where bugs live.
- **Slow test suites**: discourage running tests; keep unit tests fast and parallelize.

