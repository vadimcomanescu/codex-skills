---
name: senior-data-engineer
description: "Data engineering workflows for designing reliable pipelines and datasets: ingestion, transforms, orchestration, schema evolution, data contracts, quality checks, and observability. Use when building ETL/ELT, reviewing pipelines, defining warehouse/lake schemas, or diagnosing data quality incidents."
---

# Senior Data Engineer

Make data pipelines boring: predictable, observable, and recoverable.

## Quick Start
1) Define the data contract (schema + semantics + freshness + ownership).
2) Design the pipeline:
   - Inputs, transformations, outputs, backfills, and failure handling
3) Data quality: checks for nulls, ranges, uniqueness, and referential integrity.
4) Operational story: retries, checkpoints, alerting, and lineage.

## Optional tool: lightweight profiling for CSV/JSONL
```bash
python ~/.codex/skills/senior-data-engineer/scripts/data_quality_scan.py path/to/data.csv --out /tmp/data_profile.json
```

## References
- Data contract template: `references/data-contract.md`
- Pipeline checklist: `references/pipeline-checklist.md`

