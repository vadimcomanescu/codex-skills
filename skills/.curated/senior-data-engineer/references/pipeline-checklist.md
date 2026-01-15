# Pipeline Checklist

## Reliability
- Idempotent writes / safe retries
- Checkpointing and replay/backfill strategy
- Clear ownership and on-call response path

## Quality
- Basic checks: row count, null rates, schema drift
- Business checks: invariants (e.g., totals, monotonic counters)
- Bad-record handling: quarantine, dead-letter, or partial acceptance rules

## Observability
- Metrics: freshness, lag, volume, failure rate
- Logs: structured and correlated by run ID
- Lineage: at least document inputs/outputs

