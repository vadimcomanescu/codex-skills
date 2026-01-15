---
name: senior-backend
description: "Backend engineering workflows for designing and implementing robust APIs and services: data modeling, authN/authZ, error handling, performance, migrations, observability, and operational safety. Use when building or reviewing backend code, defining API contracts, planning DB changes, or writing backend design docs."
---

# Senior Backend

Ship backend changes that are correct, observable, and easy to operate.

## Quick Start
1) Define contract first (API/events): inputs, outputs, errors, idempotency.
2) Define data ownership: schema changes, migrations, backfills, rollback.
3) Implement with safety:
   - validation, authZ, rate limits
   - structured errors + logging + metrics
4) Prove it: tests + a local “smoke path” + monitoring hooks.

## Optional tool: scaffold backend docs
```bash
python ~/.codex/skills/senior-backend/scripts/scaffold_backend_docs.py . --out docs/backend
```

## References
- API guidelines: `references/api-guidelines.md`

