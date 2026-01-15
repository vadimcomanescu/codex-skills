# Architecture Patterns (when to use what)

## Modular monolith (default)
**Use when:** one team, tight coupling, fast iteration, unclear boundaries.
**Benefits:** simplest deployment, easy local dev, shared types, fewer distributed failures.
**Watch-outs:** enforce module boundaries; don’t let “shared” become “global soup”.

## Microservices (only with strong justification)
**Use when:** clear bounded contexts, independent scaling/deploy needs, mature ops, multiple teams.
**Benefits:** independent deploy, fault isolation (sometimes), heterogeneous tech stacks.
**Watch-outs:** distributed tracing, versioned contracts, partial failures, platform costs.

## Event-driven / async workflows
**Use when:** long-running workflows, integration, decoupling producers/consumers, smoothing load.
**Benefits:** resiliency and elasticity, natural audit log, loose coupling.
**Watch-outs:** ordering, idempotency, retries, replay/backfill, eventual consistency.

## Hexagonal / ports-and-adapters
**Use when:** business logic should be isolated from frameworks (web/db/queue), long-lived domains.
**Benefits:** testability, framework swaps, clearer boundaries.
**Watch-outs:** over-abstraction for small apps; keep ports minimal and purposeful.

## CQRS (selectively)
**Use when:** read and write models diverge, high read scale, complex projections.
**Benefits:** performance and clarity for reads, tailored models.
**Watch-outs:** duplicated data, projection lag, operational complexity.

## Practical anti-patterns
- “Microservices because it’s cool”
- “Shared database across services”
- “No ownership of schemas/contracts”
- “Async without idempotency”

