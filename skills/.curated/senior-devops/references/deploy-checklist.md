# Deployment Checklist

## Before deploy
- Build is reproducible (lockfiles, pinned versions, deterministic artifacts)
- Tests cover critical paths; smoke test exists
- Secrets are not in repo; config is documented

## During deploy
- Health checks and readiness probes
- Gradual rollout / canary if risk is high
- Observability dashboards open and watched

## After deploy
- Verify key user journeys
- Monitor error rates, latency, saturation
- Have a rollback plan and rehearse it

