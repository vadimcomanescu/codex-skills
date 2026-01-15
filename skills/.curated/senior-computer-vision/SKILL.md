---
name: senior-computer-vision
description: Computer vision engineering workflow for dataset design, model selection (detection/segmentation/classification), evaluation, inference optimization, and deployment. Use when planning or reviewing CV systems, auditing datasets, defining metrics/splits, or diagnosing model/inference issues.
---

# Senior Computer Vision

Build CV systems that generalize, are measurable, and are deployable.

## Quick Start
1) Specify the task precisely: classification vs detection vs segmentation; latency and target hardware.
2) Dataset first: define label taxonomy, edge cases, split strategy, and evaluation metrics.
3) Train with discipline: baselines, ablations, and error analysis (not just “more epochs”).
4) Deploy with realism: preprocessing parity, batching, quantization/trt where needed, monitoring.

## Optional tool: dataset inventory (no ML deps)
For a directory like `data/train/<class>/...` or any image folder:
```bash
python ~/.codex/skills/senior-computer-vision/scripts/dataset_inventory.py data/ --out /tmp/dataset_report.json
```

## References
- Metrics and splits: `references/metrics-and-splits.md`

