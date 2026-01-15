# API Guidelines (practical defaults)

## REST basics
- Use nouns for resources: `/users`, `/orders/{id}`
- Use HTTP status codes correctly (4xx for client errors, 5xx for server errors)
- Return structured error bodies with stable error codes

## Idempotency and retries
- For create/mutate operations that may be retried: support idempotency keys.
- Ensure handlers are safe on replays (avoid double charges / double writes).

## Pagination
- Prefer cursor pagination for large datasets.
- Always define ordering guarantees.

## Auth and authorization
- Authenticate requests; authorize per resource (server-side).
- Separate “who are you” from “what can you do”.

## Observability
- Add correlation IDs and structured logs for critical paths.
- Emit metrics for latency, error rate, and saturation.

