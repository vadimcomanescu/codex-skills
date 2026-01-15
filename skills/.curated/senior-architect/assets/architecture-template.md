# Architecture

## Summary
1–2 paragraphs: what this system does and what “good” looks like.

## Goals / Non-goals
- Goals:
- Non-goals:

## Constraints
- Performance:
- Availability / reliability:
- Cost:
- Compliance / data residency:
- Team / timeline:

## Context (system boundary)
External actors, upstream/downstream systems, and third-party dependencies.

## Containers (runtime components)
List major components and responsibilities. Define ownership boundaries.

## Interfaces and contracts
- APIs (REST/GraphQL): endpoints, auth, pagination, idempotency
- Events/queues: topics, payload shape, ordering guarantees
- Data contracts between services

## Data model and ownership
Who owns which tables/collections? How do we handle migrations?

## Failure modes and mitigations
Time-outs, retries, rate limits, circuit breakers, dead-letter queues, backpressure.

## Scalability plan
What scales with what? What are the bottlenecks? What’s the next scaling step?

## Observability
Golden signals, logging strategy, tracing, dashboards, alert thresholds.

## Security and privacy
Threat model highlights, secrets handling, access control, audit requirements.

## Rollout and rollback
Deployment approach, feature flags, data backfills, safety checks.

## Open questions
Things that require stakeholder input or further discovery.

