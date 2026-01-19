---
name: senior-architect
description: "Senior software architecture workflows and tooling for system design, scalability and reliability planning, API/data modeling, trade-off analysis, ADR writing, and producing clear architecture diagrams (Mermaid). Use when you need to define or revise architecture for a feature/system, choose technologies, document decisions, or review an existing codebase’s architecture."
---

# Senior Architect

Design and document architectures that are clear, defensible, and shippable.

## Quick Start
1) Clarify constraints:
   - Primary user journey + success metrics
   - Non-functional requirements (latency, throughput, availability, cost, compliance)
   - Team constraints (skills, timelines, operational maturity)
2) Produce outputs (in this order):
   - **Context**: system boundary + external dependencies
   - **Containers**: major runtime components and responsibilities
   - **Interfaces**: APIs/events/contracts + data ownership
   - **Risks**: failure modes + mitigations + open questions
   - **Decisions**: ADRs with explicit trade-offs

## Use the bundled tools (optional, but recommended)

From your project root, run the scripts from the installed skill directory (default install location: `~/.codex/skills/senior-architect/`).

Bootstrap a documentation skeleton (ADR + architecture doc templates):
```bash
python ~/.codex/skills/senior-architect/scripts/project_architect.py . --out docs/architecture
```

Summarize dependencies and detected stack signals (Node/Python/Go/Rust, Next.js, Postgres, etc.):
```bash
python ~/.codex/skills/senior-architect/scripts/dependency_analyzer.py . --json --output /tmp/deps.json
```

Generate a starter Mermaid diagram based on detected components:
```bash
python ~/.codex/skills/senior-architect/scripts/architecture_diagram_generator.py . --out docs/architecture/diagram.mmd
```

## References (load only when needed)
- Architecture patterns and when to use them: `references/architecture-patterns.md`
- End-to-end system design workflow + checklists: `references/system-design-workflow.md`
- Tech decision matrixes (DB, APIs, queues, caching, observability): `references/tech-decision-guide.md`

## Deliverables (what “done” looks like)
- `docs/architecture/ARCHITECTURE.md` with clear boundaries, contracts, data ownership, and scaling assumptions
- At least one ADR under `docs/architecture/adr/` for the most consequential decision
- A Mermaid diagram (`.mmd`) that matches the written architecture
