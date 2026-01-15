# Metrics and Splits (practical)

## Choose metrics that match deployment
- **Classification**: accuracy is rarely enough; track per-class precision/recall, macro-F1, calibration.
- **Detection**: mAP is useful; also track per-class recall at relevant IoU thresholds.
- **Segmentation**: mIoU + boundary quality (for fine edges).

## Splits
- Avoid leakage: split by *subject*, *scene*, *video*, or *capture session* when relevant.
- Keep a “hard” set: rare lighting, occlusions, motion blur, extreme scales.
- Track distribution drift between train/val/test.

## Error analysis
- Make a small taxonomy of failures (lighting, occlusion, class confusion, tiny objects).
- Prioritize data fixes and label fixes before complex model changes.

