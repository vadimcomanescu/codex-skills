# System Design Workflow (pragmatic)

## 1) Frame the problem (10–15 minutes)
- Primary user journey + success metrics
- The “one thing” that must not fail
- Constraints: latency, cost, compliance, timeline, team skills
- What’s already in the repo that must be reused?

## 2) Define boundaries
- What is in-scope vs out-of-scope?
- External dependencies and contracts
- Data ownership boundaries (who owns what data)

## 3) Draft the architecture (start coarse)
- Context diagram (actors + systems)
- Container diagram (major components)
- Communication styles: sync calls vs async events

## 4) Make the hard decisions explicit
Use ADRs for:
- Data store choices and schema ownership
- API style (REST vs GraphQL) and versioning
- Consistency model (strong vs eventual)
- Queue/eventing strategy and delivery guarantees

## 5) Stress the design
For each critical path, answer:
- Failure mode: what breaks?
- Detection: how do we know?
- Mitigation: retries/timeouts/circuit breakers/backpressure
- Recovery: rollback, replay, backfill, manual ops

## 6) Write the “operational story”
- Deployments, rollbacks, migrations
- Observability: logs/metrics/traces + alert thresholds
- SLOs and error budgets (if applicable)

## Review checklist
- One clear system boundary
- Clear ownership of data and contracts
- Stable interfaces (idempotency, pagination, auth)
- Defined scaling assumptions (what grows, what bottlenecks)
- A plan for migrations and rollback

