# Prompt Review Checklist

## Instruction clarity
- Does it define the task and expected output format?
- Are constraints explicit and prioritized?
- Are tool-use rules unambiguous (when to call tools, what to do with failures)?

## Robustness
- How should the model behave on missing/invalid inputs?
- Are there adversarial examples (prompt injection, irrelevant context, contradictory requests)?

## Evaluation
- Is there a stable test set?
- Are we measuring what matters (accuracy, safety, latency, cost)?

## Maintainability
- Is the prompt modular (sections) and easy to diff?
- Are examples minimal and representative?

