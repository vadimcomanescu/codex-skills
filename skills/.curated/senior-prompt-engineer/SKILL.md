---
name: senior-prompt-engineer
description: Prompt engineering workflow for building reliable assistants and agents: task decomposition, instruction hierarchy, tool-use patterns, safety constraints, and evaluation design. Use when writing or refactoring system prompts, creating structured prompts, building prompt test suites, or debugging regressions in LLM behavior.
---

# Senior Prompt Engineer

Treat prompts like products: versioned, tested, and measurable.

## Quick Start
1) Define the job: inputs, outputs, and the “definition of done”.
2) Write the smallest prompt that:
   - states constraints clearly
   - defines output format
   - includes edge-case handling
3) Add examples only when needed (few-shot is expensive).
4) Create an eval set: representative cases + adversarial cases.
5) Iterate with diffs: change one thing, measure impact.

## Optional tool: scaffold a prompt + eval harness
```bash
python ~/.codex/skills/senior-prompt-engineer/scripts/scaffold_prompt_eval.py . --out evals/prompt_eval
```

## References
- Prompt review checklist: `references/prompt-review.md`

