# Example: Reviewing a Scoring Change

A walkthrough of `/review` on a sensitive code change — a scoring formula modification. Demonstrates the strategic-reviewer agent's evidence-based findings, uncertainty flagging, and Critical Trust.

---

## Scenario

A user invokes:

```
/review
```

The current branch has changes to the scoring engine: updated composite weights from equal (25/25/25/25) to research-based (35/30/25/10).

## What `/review` Does

### Step 1: Determine Scope

No arguments provided — review the current branch diff against main.

```bash
git diff $(git merge-base HEAD main)..HEAD
```

The diff spans 4 files:
- `services/scoring-engine/src/composite.py` — weight constants changed
- `services/scoring-engine/src/composite.py` — calculation function updated
- `services/scoring-engine/tests/test_composite.py` — test expectations updated
- `docs/decisions/ADR-015-composite-weights.md` — new ADR documenting the change

### Step 2: Understand Context

The review skill:
1. Reads the project's CLAUDE.md → finds: "Scoring changes require psychometric justification. Run /scoring-reviewer for weight changes."
2. Notes this touches **scoring** — high scrutiny area.
3. Reads the ADR referenced in the diff → understands the rationale: mindset predicts growth better than technical skill (SP methodology decision).

### Step 3: Review

The strategic-reviewer agent receives the diff and context. It reads the full diff, understands the intent (aligning weights with SP methodology), and evaluates.

### Step 4: Present Findings

```markdown
## Review: Composite scoring weight update (25/25/25/25 → 35/30/25/10)

### Critical Issues (must fix)

- **[CRIT-1]** `composite.py:47` — The old weights summed to 1.0 (0.25×4),
  but the new weights sum to 1.0 only if expressed as decimals (0.35+0.30+0.25+0.10).
  The code uses integer percentages (35+30+25+10=100) and divides by 100.
  This works, but the constant `WEIGHT_TOTAL = 4` on line 12 is now wrong —
  it should be `100` or removed. Currently unused, but if any code references
  it, the assertion `assert sum(weights) == WEIGHT_TOTAL` on line 52 will fail.

  **Fix:** Update `WEIGHT_TOTAL = 100` or remove the constant and assertion
  if they're dead code.

### Suggestions (consider)

- **[SUG-1]** `test_composite.py:23-45` — Tests were updated to match new
  weights, but there's no test for the boundary case where one dimension
  score is 0. With unequal weights, a 0 in the heavily-weighted dimension
  (mindset at 35%) has a much larger impact than before. Consider adding a
  test: `test_composite_with_zero_mindset_score`.

- **[SUG-2]** `composite.py:55` — The function `calculate_composite` takes
  individual scores but doesn't validate they're in the expected range (0-100).
  A negative score or >100 would produce unexpected results. This was
  true before the change too, but with unequal weights, out-of-range
  inputs are amplified. Consider adding input validation.

### Observations (FYI)

- **[OBS-1]** ADR-015 documents the rationale clearly — mindset predicts
  growth trajectory better than technical skill, based on SP methodology
  research. This aligns with the psychometric toolkit's recommendation
  that weight changes need theoretical justification.

- **[OBS-2]** I'm not confident about the psychometric validity of these
  specific weights. The ADR references the SP methodology but doesn't cite
  the empirical data. Consider running `/scoring-reviewer` for a psychometric
  validation of the 35/30/25/10 split — this is outside my scope.

### Verdict: APPROVE WITH NOTES

The weight update is correctly implemented and well-documented in ADR-015.
Fix the stale `WEIGHT_TOTAL` constant (CRIT-1) before merging.
The psychometric validity of the specific ratios is outside this review's
scope — suggest `/scoring-reviewer` for that.
```

### Step 5: Bridge to Knowledge Compounding

```
>> This review surfaced that weight constant assertions need updating
   when scoring formulas change. Worth documenting? /compound
```

## What This Demonstrates

- **Evidence-based findings:** Every critical issue and suggestion points to a specific file and line. "Line 12 has `WEIGHT_TOTAL = 4` which is now wrong" — not "the constants might be wrong."
- **Uncertainty flagging:** The reviewer explicitly says "I'm not confident about the psychometric validity" and suggests the right tool (`/scoring-reviewer`) instead of guessing. This IS Critical Trust in action.
- **Priority ordering:** The stale constant (CRIT-1) is the only blocker. Suggestions improve quality but don't block. Observations provide context.
- **Intent-aware review:** The reviewer read the ADR, understood the purpose (SP methodology alignment), and judged the code against that intent — not against abstract ideals about "what weights should be."
- **Scope awareness:** The reviewer knows its limits. Psychometric validity is not its domain. It flags this and redirects, rather than offering uninformed opinions.
- **Knowledge compounding bridge:** The insight about weight constants and assertions is worth preserving for future scoring changes.
