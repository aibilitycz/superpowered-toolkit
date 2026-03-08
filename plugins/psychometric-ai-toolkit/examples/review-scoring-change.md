# Example: Review a Scoring Change

## Scenario

You've changed the composite scoring weights for a leadership assessment from equal weights (25% each across 4 dimensions) to differentiated weights (40% Strategic Thinking, 25% People Leadership, 20% Execution, 15% Communication).

## How to Use

Ask Claude:

> "I changed our leadership assessment weights from equal (25% each) to 40/25/20/15 across Strategic Thinking, People Leadership, Execution, and Communication. Is this psychometrically valid?"

## What Happens

1. Claude activates the `scoring-reviewer` skill
2. Runs through the 10-point validation checklist
3. Flags key questions:
   - Is the 40% weight for Strategic Thinking empirically justified?
   - Does this change affect DIF results?
   - Are existing scores still interpretable?
4. Produces a PASS/FAIL verdict with specific reasoning

## Expected Output

The scoring-reviewer will likely flag:
- **Weight justification** — needs evidence (regression weights, SME panel, or criterion validity data)
- **Dimension dominance** — Strategic Thinking at 40% needs explicit justification
- **Backward compatibility** — existing scores not comparable under new weights
- **DIF check** — weight change may alter subgroup impact patterns
