---
name: feature-design-assistant
description: Turn ideas into fully formed designs and specs through natural collaborative dialogue. Use when planning new features, designing architecture, or making significant changes to the codebase.
---

# Feature Design Assistant

Turn ideas into implementable specs with clear scope, risks, and acceptance criteria.

## Workflow
1) **Context**: skim the repo for patterns, modules, and recent changes.
2) **Discovery**: ask up to 4 questions per round.
3) **Design**: propose a solution with trade-offs.
4) **Spec**: write a short design doc with sections below.

## Discovery Questions (examples)
- Goal and primary users?
- Scope and timeline constraints?
- Which layers are touched (data, API, UI, infra)?
- Quality bar (performance, security, reliability)?
- Non-goals / out-of-scope?

## Design Doc Template
- **Problem**
- **Goals / Non-goals**
- **Proposed solution** (components, data flow)
- **Alternatives** (and why rejected)
- **Risks / Open questions**
- **Testing / rollout plan**
- **Acceptance criteria**

## Guardrails
- Keep scope tight; call out what is explicitly excluded.
- Prefer existing patterns unless the user asks to change architecture.
- If the change is large, propose a phased rollout.

## References
- Extended examples: `references/examples.md`

