---
name: senior-devops
description: "DevOps workflow for CI/CD, infrastructure, observability, reliability, and safe deployments. Use when designing deployment pipelines, reviewing infra changes, improving operational readiness (alerts/runbooks), or auditing a repo’s production-readiness signals."
---

# Senior DevOps

Make deployments repeatable and incidents survivable.

## Quick Start
1) Define the operational goal (latency, availability, cost) and deploy frequency.
2) Pipeline: build → test → package → deploy → verify → rollback.
3) Observability: logs/metrics/traces + alerts tied to user impact.
4) Runbooks: how to debug and how to roll back safely.

## Optional tool: repo ops inventory
```bash
python ~/.codex/skills/senior-devops/scripts/repo_ops_inventory.py . --out /tmp/ops_inventory.md
```

## References
- Deployment checklist: `references/deploy-checklist.md`

