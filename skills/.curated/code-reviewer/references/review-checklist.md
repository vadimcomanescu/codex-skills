# Review Checklist (high-signal)

## Correctness
- Does the code handle invalid inputs and error paths?
- Are there any behavior changes not reflected in docs/tests?
- Are concurrency and ordering assumptions explicit?

## Security
- Any secrets in code/config/logs?
- AuthZ: are permissions enforced server-side (not only in UI)?
- Input validation and injection risks (SQL/NoSQL/HTML/command)?

## Maintainability
- Names match intent; functions/classes have a single responsibility.
- Public interfaces are stable and hard to misuse.
- Logging is useful and not noisy; metrics/tracing where appropriate.

## Performance
- Any extra I/O, N+1 queries, unbounded loops, large allocations?
- Caching strategy (if any) has invalidation/TTL and observability.

## Tests
- Tests cover the risky logic and failure modes.
- Assertions are meaningful (not just snapshotting everything).
- Test names explain behavior (not implementation).

