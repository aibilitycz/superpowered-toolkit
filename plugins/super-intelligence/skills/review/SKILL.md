---
name: review
description: >
  Focused review of code, documents, or architecture — one deep pass with evidence-based
  findings and clear verdict. Auto-detects what you're reviewing: branch diff, PR, file path,
  plan, brainstorm, or spec. One reviewer that reads carefully beats nine that skim.
  Triggers: review, code review, review PR, review diff, review plan, review brainstorm,
  review spec, review document, evaluate, check.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Bash
---

# Review

One focused review. Not nine shallow passes — one deep one that reads carefully, evaluates with evidence, and gives a clear verdict. Works on code, documents, and architecture.

## Common Rationalizations

| Shortcut | Why It Fails | The Cost |
|----------|-------------|----------|
| "Skim the diff — I'll catch the important stuff" | The one line you skip is the one that matters. Dangerous bugs look correct. | Bug in production that a careful read would have caught |
| "No security concerns here" | Auth checks, input validation, and secrets leak through seemingly innocent code | Vulnerability shipped because nobody looked |
| "The tests pass, so the logic is correct" | Tests verify what the author THOUGHT the code does, not edge cases they missed | False confidence → undetected regression |
| "Just style nits — not worth mentioning" | Mixing style nits with real findings buries critical issues | Author reads 10 nits, misses the 1 security bug |

## Workflow

**Quick routing:** What kind of review is this?

| What You're Given | Review Type | Action |
|-------------------|------------|--------|
| Branch diff, PR, or code files | **Code review** | Launch strategic-reviewer agent |
| `.md` file in `docs/plans/` or `docs/brainstorms/` | **Document review** | Read and evaluate against document criteria |
| Directory path | **Architecture review** | Analyze patterns, conventions, dependencies |
| Unclear | Ask once: "Reviewing code or the document itself?" | |

### 1. Detect Review Type

**Entry:** User invoked `/review` with input (or no input = current branch diff).
**Exit:** Review type determined — code, document, or architecture.

Auto-detect what's being reviewed based on the input:

| Input | Review Type | Approach |
|-------|------------|----------|
| No arguments | **Code** — current branch diff | `git diff $(git merge-base HEAD main)..HEAD` |
| File path to `.md` in `docs/plans/`, `docs/brainstorms/` | **Document** — plan or brainstorm | Read and evaluate against document criteria |
| File path to code files | **Code** — specific files | Read and review those files |
| PR URL or number | **Code** — PR diff | `gh pr diff <number>` |
| Directory path | **Architecture** — structural review | Analyze patterns, conventions, dependencies |

**If ambiguous:** Ask once. "Reviewing code changes or the document itself?"

### 2. Gather Context

**Entry:** Review type known.
**Exit:** Conventions loaded, risk areas identified, related plan/brainstorm read.

Before reviewing, understand what "correct" looks like:

1. **Read the project's CLAUDE.md** for conventions and patterns
2. **Check what the change touches.** Auth, scoring, data, migrations, money → extra scrutiny
3. **Read the related plan or brainstorm** if referenced in commits or PR description
4. **Check for test files** in the diff. Note what's tested and what's not.

### 3. Review

**Entry:** Context gathered, diff/document available.
**Exit:** Findings documented with evidence and severity.

#### Code Review

Launch the **strategic-reviewer** agent with:
- The full diff (or file contents)
- Project conventions from CLAUDE.md
- Any plan/brainstorm context
- What areas the change touches (for priority calibration)

The agent does one focused review pass. No parallel swarm. One reviewer that does the job well.

**If the diff is large (>500 lines):** Focus on the most impactful files first. Read all of them, but prioritize findings from core logic over boilerplate, tests, or generated code.

#### Document Review

Read the full document. Don't skim — read it once, thoroughly. Evaluate against these criteria:

**Does it explain WHY?**
- Is there decision rationale? Not just "we'll use X" but "we'll use X because Y, and we considered Z."
- Are there decisions made without explanation? Flag each one.

**Are risks identified?**
- Does it acknowledge what could go wrong? Are mitigations proposed?
- Are there risks the author missed? (Security, performance, backward compatibility, data migration, cross-team dependencies)

**Is the scope clear?**
- Can you tell exactly what's in scope and what's not?
- Is there an explicit "out of scope" or "deferred" section?

**Are acceptance criteria measurable?**
- Can you determine from the criteria alone whether the feature is complete?
- Are criteria testable? "Users can do X" is testable. "The system is fast" is not.

**Are there unresolved blockers?**
- Open questions that should be answered before work begins?
- TBD or TODO items that would block implementation?

**Is it actionable?**
- Could someone start `/work` from this document right now?
- Are dependencies between tasks clear?

### 4. Present Findings

**Entry:** Review complete with findings.
**Exit:** Findings presented in structured format with clear verdict.

**For code reviews:**

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

**Confidence requirement:** Every finding needs [evidence] + [failure scenario]. No evidence = no finding. "This looks off" is not a finding. "This will fail when X because Y" is.

**For document reviews:**

```markdown
## Document Review: [filename]

### Strengths
- [What's well done — be specific, not generic praise]

### Gaps
- [GAP-1] [What's missing or unclear] — Why this matters for implementation.

### Suggestions
- [SUG-1] [Specific improvement] — How this makes the document more actionable.

### Verdict: READY / NEEDS REFINEMENT

[1-2 sentence summary. If NEEDS REFINEMENT, name the top 1-3 things to fix before starting work.]
```

**If no issues found:** Say so clearly. Don't invent problems.

### 5. Bridge to Knowledge Compounding

If the review uncovered a non-obvious pattern, gotcha, or insight worth preserving:

```
>> This review found [insight]. Worth documenting for the team? /compound
```

Only suggest when genuinely useful. Most reviews don't produce novel insights — that's fine.

## What Makes This Superpowered

- **Critical Trust (2.1):** The reviewer flags uncertainty. "I'm not sure about X — verify with Y" instead of faking confidence.
- **One deep review > nine shallow ones.** One agent reading carefully produces signal. Nine agents skimming produce noise.
- **Universal scope.** Code, documents, architecture — one skill, one deep pass. The detective doesn't care whether the evidence is code or prose.
- **Knowledge compounding bridge.** Reviews aren't just quality gates — they're learning opportunities.

## Validate

**After code review, verify:**
- [ ] Did I check correctness? (logic errors, edge cases, broken invariants)
- [ ] Did I check security? (auth, input validation, secrets, OWASP basics)
- [ ] Did I check conventions? (project patterns, naming, structure)
- [ ] Did I check simplicity? (YAGNI, unnecessary abstractions)
- [ ] Did I check test coverage? (critical paths tested, not just happy path)

**After document review, verify:**
- [ ] Did I check WHY? (decision rationale, not just what)
- [ ] Did I check risks? (what could go wrong, mitigations)
- [ ] Did I check scope? (clear in/out of scope)
- [ ] Did I check criteria? (measurable, testable acceptance criteria)
- [ ] Did I check actionability? (can `/work` start from this?)

## When NOT to Use /review

- **Trivial changes.** Typo fixes, config updates, formatting. Just commit.
- **Generated code.** Review the input, not the output. Migrations, lockfiles, etc.
- **You just want a linter.** Run the linter instead. `/review` is for semantic review.

## Knowledge References

- `../knowledge/critical-evaluation.md` — How to evaluate with evidence and flag uncertainty
- `../agents/strategic-reviewer.md` — The agent that does the actual code review
