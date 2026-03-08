---
name: review
description: >
  Focused code review with one deep pass, evidence-based findings, and clear verdict.
  Use when reviewing branch diffs, specific files, or PR URLs. One reviewer that reads
  carefully beats nine that skim. Triggers: review, code review, review PR, review diff,
  review changes, check code.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Bash
---

# Review

One focused code review. Not nine shallow passes — one deep one that reads carefully, evaluates with evidence, and gives a clear verdict.

## Workflow

### 1. Determine Scope

**No arguments:** Review current branch diff against the default branch.
```bash
git diff $(git merge-base HEAD main)..HEAD
```

**File path argument:** Review those specific files.
```bash
# Read the specified files
```

**PR URL argument:** Fetch the PR diff.
```bash
gh pr diff <number>
```

**If the diff is large (>500 lines):** Focus on the most impactful files first. Read all of them, but prioritize findings from core logic over boilerplate, tests, or generated code.

### 2. Understand Context

Before reviewing, gather context:

1. **Read the project's CLAUDE.md** for conventions and patterns. This tells you what "correct" looks like for this project.
2. **Check what the change touches.** Does it touch auth, scoring, data, migrations, money? These areas get extra scrutiny.
3. **Read the related plan or brainstorm** if one is referenced in recent commits or the PR description. Judge the code against its purpose.
4. **Check for test files** in the diff. Note what's tested and what's not.

### 3. Review

Launch the **strategic-reviewer** agent with:
- The full diff (or file contents)
- Project conventions from CLAUDE.md
- Any plan/brainstorm context
- What areas the change touches (for priority calibration)

The agent does one focused review pass. No parallel swarm, no multiple passes. One reviewer that does the job well.

### 4. Present Findings

Present the agent's findings in conversation. Not in todo files, not in separate documents — right here in the chat.

```markdown
## Review: [scope summary]

### Critical Issues (must fix)
- **[CRIT-1]** [file:line] — Description. Why this matters. Fix suggestion.

### Suggestions (consider)
- **[SUG-1]** [file:line] — Description. Tradeoff if ignored.

### Observations (FYI)
- **[OBS-1]** Description.

### Verdict: APPROVE / APPROVE WITH NOTES / REQUEST CHANGES
```

**If no issues found:** Say so clearly. "No critical issues or suggestions. Code is clean, follows conventions, and does what the plan says. APPROVE."

**If verdict is REQUEST CHANGES:** Name the specific critical issues. Don't leave it vague.

### 5. Bridge to Knowledge Compounding

If the review uncovered a non-obvious pattern, gotcha, or insight worth preserving:

```
>> This review found [insight]. Worth documenting for the team? /compound
```

Only suggest this when genuinely useful. Most reviews don't produce novel insights — that's fine.

## What Makes This Superpowered

- **Critical Trust (2.1):** The reviewer flags uncertainty. "I'm not sure about X — verify with Y" instead of faking confidence. This models calibrated trust.
- **One deep review > nine shallow ones.** The strategic-reviewer agent reads the full diff, understands intent, and prioritizes findings. Nine agents skimming produce noise. One agent reading carefully produces signal.
- **Knowledge compounding bridge.** When a review uncovers something worth preserving, it suggests capturing it. Reviews aren't just quality gates — they're learning opportunities.
- **No configuration needed.** No settings file, no agent selection, no "which reviewers do you want?" One reviewer, works out of the box.

## When NOT to Use /review

- **Trivial changes.** Typo fixes, config updates, formatting. Just commit.
- **Generated code.** If a tool generated it (migrations, lockfiles), review the input, not the output.
- **You just want a linter.** Run the linter instead. `/review` is for semantic review, not style enforcement.

## Knowledge References

- `../knowledge/critical-evaluation.md` — How to evaluate with evidence and flag uncertainty
- `../agents/strategic-reviewer.md` — The agent that does the actual review
