# Example: Validate an LLM Scorer

## Scenario

You built an LLM-based scorer for open-ended behavioral responses (e.g., "Describe a time you handled a conflict"). The LLM scores on a 1-5 rubric but inter-rater agreement with human experts is only Cohen's kappa = 0.42.

## How to Use

Ask Claude:

> "My LLM scorer for behavioral responses has Cohen's kappa of 0.42 against human raters. Is this acceptable? How do I improve it?"

## What Happens

1. Claude activates the `psychometric-advisor` skill
2. Routes to `ai-assessment.md` (primary) and `reliability.md` (secondary)
3. Provides advisory-mode response:
   - Kappa 0.42 = "moderate" agreement (Landis & Koch) — below acceptable for most assessment uses
   - Threshold depends on stakes: ≥0.60 for screening, ≥0.80 for high-stakes
   - Improvement strategies: rubric refinement, calibration examples, ensemble scoring, anchor training

## Expected Advice

- **Root cause analysis:** Is the disagreement systematic (LLM always rates higher) or random?
- **Rubric clarity:** Are rubric levels behaviorally anchored with distinct examples?
- **Calibration:** Add calibration examples (scored responses with expert rationale) to the prompt
- **Ensemble:** Use multiple LLM passes and aggregate (reduces random error)
- **Hybrid approach:** Use LLM for screening (L1), human review for borderline cases (L2)
- **Evidence strength:** Mark specific recommendations as [emerging] since LLM-as-judge is a nascent field
