---
name: senior-data-scientist
description: Data science workflow for turning ambiguous questions into measurable metrics, experiments, and models. Use when framing hypotheses, selecting metrics, designing A/B tests, building predictive models, doing error analysis, or writing experiment/model reports with clear assumptions and caveats.
---

# Senior Data Scientist

Be rigorous about what you’re measuring and why.

## Quick Start
1) Translate the ask into a decision: “what will we do differently based on the result?”
2) Define metrics: primary metric, guardrails, and segmentation.
3) Choose method: analysis, A/B test, causal approach, or predictive model.
4) Validate: leakage checks, baseline, error analysis, and robustness.
5) Communicate: limitations, assumptions, and next steps.

## Optional tool: quick CSV profiling (no pandas)
```bash
python ~/.codex/skills/senior-data-scientist/scripts/csv_profile.py data.csv --max-rows 50000 --out /tmp/profile.json
```

## References
- Experiment report template: `references/experiment-report.md`

