# Tech Decision Guide (fast matrices)

## API style
- **REST**: best default; simple, cacheable, easy tooling.
- **GraphQL**: strong when clients need flexible composition and you can invest in schema governance.
- **Events**: best for workflows, integrations, and “notify many consumers”.

## Data store
- **Postgres**: best default for relational + transactional workloads.
- **Document store**: when schema is highly variable and query patterns are simple.
- **Search**: use a search engine for full-text/ranking; don’t force it into OLTP.

## Caching
- Cache only when you can define:
  - Key strategy
  - TTL / invalidation
  - Staleness tolerance
  - Observability (hit rate, evictions, stampedes)

## Queues vs pub/sub
- **Queue**: work distribution, competing consumers, “do this task”.
- **Pub/Sub**: multiple consumers, “this happened”.
Always define delivery semantics (at-least-once is common) and idempotency strategy.

## Observability defaults
- Structured logs with correlation IDs
- Golden signals: latency, traffic, errors, saturation
- Trace critical paths end-to-end before adding more services

