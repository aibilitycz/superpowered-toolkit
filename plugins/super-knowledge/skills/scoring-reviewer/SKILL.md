---
name: scoring-reviewer
description: >
  Validates scoring changes against psychometric standards. Use when the user modifies
  scoring weights, formulas, thresholds, bands, normative references, or composite scoring.
  Triggers: scoring change, weight change, formula change, scoring review, validate scoring,
  threshold change, band change, composite score, normative reference.
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Scoring Reviewer

Validates proposed scoring changes against psychometric standards. Catches changes that would compromise measurement validity, reliability, or fairness.

## Prerequisites

Before reviewing, read these domain files for reference:
- `skills/psychometric-advisor/scoring.md` — scoring methods and principles
- `skills/psychometric-advisor/reliability.md` — reliability implications of scoring changes
- `skills/psychometric-advisor/validity.md` — validity implications, DIF considerations

## Input

The user provides one of:
- Natural language description of the scoring change
- Code diff showing scoring formula modifications
- Before/after scoring configuration (YAML, JSON, or code)

## Validation Checklist

Apply each check. Mark PASS, FAIL, or N/A with specific reasoning.

### 1. Composite Reliability
- [ ] Composite reliability remains ≥ threshold for assessment stakes (0.70 / 0.80 / 0.90)
- [ ] If reliability drops, is the tradeoff justified and documented?
- [ ] Are subscale reliabilities sufficient for any subscale-level decisions?

### 2. Weight Justification
- [ ] Weights are empirically derived (factor loadings, regression) OR theoretically justified (documented rationale)
- [ ] Arbitrary weights are flagged: "I felt like dimension X should be 40%" is not justification
- [ ] Weight rationale is documented somewhere reviewable

### 3. Weight Arithmetic
- [ ] Proportional weights sum to 1.0 (or intended total)
- [ ] Additive weights produce expected score range
- [ ] No rounding errors accumulate across dimensions

### 4. Dimension Dominance
- [ ] No single dimension contributes >50% of composite without explicit justification
- [ ] If dominant dimension is intentional, justification references validity evidence
- [ ] Dimension contribution is proportional to its importance for the criterion

### 5. Normative Reference
- [ ] Norm sample is representative of target population
- [ ] Norm recency is appropriate (norms <10 years old for personality, <5 for rapidly changing domains)
- [ ] Normative and ipsative scores are not mixed without clear labeling

### 6. Score Boundaries
- [ ] Floor and ceiling are psychometrically motivated (not arbitrary round numbers)
- [ ] Score distribution has adequate variance (no bunching at extremes)
- [ ] Boundary cases are tested (what happens at min/max?)

### 7. Ipsative vs. Normative
- [ ] Ipsative scores (within-person ranking) are not interpreted as normative (between-person comparison)
- [ ] If both score types exist, they are clearly distinguished in output
- [ ] Ipsative profiles are not correlated or factor-analyzed (violates independence assumption)

### 8. Construct-Irrelevant Variance
- [ ] Change does not introduce systematic variance unrelated to the measured construct
- [ ] Method effects are controlled (e.g., acquiescence bias in all-positive Likert)
- [ ] Response format artifacts don't contaminate scores

### 9. DIF / Fairness Impact
- [ ] Does this change affect subgroups differently? (age, gender, culture, language)
- [ ] If DIF analysis exists, do results still hold under the new scoring?
- [ ] Adverse impact ratios remain within acceptable bounds (4/5ths rule as baseline)

### 10. Backward Compatibility
- [ ] Can existing scores be interpreted under the new model?
- [ ] If not, is there a migration/recalculation plan?
- [ ] Are score history and trends preserved or explicitly broken?

## Escalation Judgment

Not all checks require the same level of human oversight:

- **Checks 1-7 (technical):** Can pass/fail autonomously. Clear criteria, objective thresholds.
- **Checks 8-10 (judgment: fairness, norming, stakeholder impact):** Always flag for human review, even in autonomous mode. These involve value judgments that require domain expertise.
- **Contradiction detection:** If a scoring change contradicts a past decision documented in `docs/solutions/`, surface it explicitly: "This conflicts with [prior solution]. Has the context changed?"

## Output Format

```markdown
## Scoring Review

### Change Summary
[1-2 sentence description of what changed]

### Checklist Results
| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | Composite reliability | PASS/FAIL/N/A | [reasoning] |
| 2 | Weight justification | PASS/FAIL/N/A | [reasoning] |
| ... | ... | ... | ... |

### Critical Issues
[Issues that must be resolved before shipping]

### Warnings
[Issues that should be addressed but don't block shipping]

### Verdict
**APPROVE** / **APPROVE WITH CONDITIONS** / **REJECT**

[1-2 sentence summary with the key reason]
```

## Anti-patterns

- **"The business wants 40/30/30 weights"** — Business preference is not psychometric justification. Push back with evidence.
- **"We've always used these weights"** — Historical inertia is not validation. Ask when they were last reviewed.
- **"Alpha is 0.68, close enough"** — Below threshold is below threshold. Either fix it or lower the stakes.
- **Changing weights without re-checking DIF** — Weight changes can introduce differential impact even when items are fair.
