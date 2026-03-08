---
name: plan
description: >
  Strategic planning with auto-calibrated detail, decision rationale, and dependency ordering.
  Use when starting a new feature, bug fix, refactor, or any non-trivial work. Produces a
  plan document with tasks, reasoning, and acceptance criteria. Triggers: plan, planning,
  create plan, implementation plan, feature plan, work plan.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - AskUserQuestion
  - Write
  - Edit
---

# Plan

Strategic planning that fits the problem. Answers **HOW** to build what was decided in `/brainstorm` (or from scratch for clear requirements).

## Boundaries

**This skill MAY:** research (read-only), analyze codebase patterns, write the plan document.
**This skill MAY NOT:** edit code, create files beyond the plan document, run tests, deploy, implement anything.

**NEVER write code during this skill. Research and plan only.**

## Common Rationalizations

| Shortcut | Why It Fails | The Cost |
|----------|-------------|----------|
| "Skip research — I already know the codebase" | You know YOUR mental model. The codebase may have changed. | Plan conflicts with existing code → rework |
| "Skip decision rationale — the approach is obvious" | Obvious to you, now. Not to the person executing in 2 weeks. | Decisions get questioned, re-litigated, or silently reversed |
| "Make every task detailed — more detail is better" | Over-specified plans are brittle. They break on first contact with reality. | Plan becomes a constraint instead of a guide |
| "Skip risk analysis — it's low risk" | The risks you don't name are the ones that surprise you. | Unmitigated risk → emergency debugging |

---

## Phase 0: Detect Context

**Entry:** User has a topic, brainstorm path, or feature description.

**If the user provided a brainstorm path:**
1. Read the brainstorm document
2. Extract key decisions, chosen approach, open questions
3. Announce: "Using brainstorm: [filename]. Extracting decisions."
4. **Skip Phase 1** — the brainstorm already answered WHAT to build

**If the user provided a topic but no brainstorm:**
- Check `docs/brainstorms/` (or project override path) for a recent match (last 14 days, semantic match on filename/frontmatter)
- **If one found:** Read it and announce. Skip Phase 1.
- **If multiple found:** Use **AskUserQuestion** to ask which brainstorm to use, or whether to proceed without one.
- **If none found:** Continue to Phase 1.

**Exit:** Context understood — brainstorm consumed (if exists), scope clear enough to research.

---

## Phase 1: Refine the Idea (Only if No Brainstorm)

**Entry:** No brainstorm exists. User provided a topic or description.

Use **AskUserQuestion** to ask clarifying questions — one at a time, not a questionnaire:
- What problem does this solve?
- What's the desired outcome?
- Any constraints? (time, tech, dependencies)

Prefer multiple-choice questions when natural options exist. Continue until the scope is clear OR user says "proceed."

**Exit:** Scope understood well enough to research.

---

## Phase 2: Research

**Entry:** Context detected (Phase 0) or idea refined (Phase 1).

Launch research **in parallel**:

- Task researcher("Find existing patterns related to: <feature description>. Search project CLAUDE.md for conventions, codebase for similar implementations, docs/solutions/ for past fixes, and docs/plans/ for related work.")

**Surface past solutions:**
```
>> Known pattern: docs/solutions/auth/jwt-refresh-fix.md (high match)
>> Existing code: services/scoring-engine/composite.py (similar pattern)
```

**Research decision for external sources:**

- **High-risk topics (security, payments, data privacy, migrations):** Always research externally. The cost of missing something is too high.
- **Strong local context (codebase has patterns, CLAUDE.md has guidance):** Skip external research.
- **Uncertain or unfamiliar territory:** Research externally.

**If external research is needed:**
Announce the decision and proceed: "This involves payment processing — researching current best practices before planning."

**Exit:** Codebase patterns known, past solutions surfaced, constraints identified.

---

## Phase 3: Calibrate Detail Level

**Entry:** Research complete.

Auto-calibrate based on complexity. Don't ask the user — assess it, then tell them.

```
CONCISE — when:
- Scope is clear and bounded
- One person, one day or less
- Low risk (no auth, scoring, data, money)
- Clear precedent in codebase

STANDARD — when:
- Multi-day work but clear approach
- Some risk or new patterns needed
- Decision rationale adds value

DETAILED — when:
- Multi-repo or multi-team
- Unclear approach, multiple valid options
- High risk (auth, scoring, data, money, migrations)
- Significant architectural decisions
```

Tell the user: "This is a [level] plan — [reason]. Let me know if you want more or less detail."

**Exit:** Detail level chosen and communicated.

---

## Phase 4: Write the Plan

**Entry:** Detail level set, research findings available.

Check the project's `CLAUDE.md` for a "Toolkit Output Paths" table. Use those paths if present, otherwise use defaults.

**Output path:** `{plans_path}/YYYY-MM-DD-{type}-{kebab-topic}-plan.md`
(Default `plans_path`: `docs/plans/`)

**Types:** `feat`, `fix`, `refactor`, `chore`, `docs`

**YAML frontmatter:**
```yaml
---
title: "{type}: {description}"
type: plan
date: YYYY-MM-DD
status: approved
brainstorm: {path if exists}
confidence: high | medium | low
---
```

**All plans include:**
1. **Title and one-line summary**
2. **Problem Statement** — What's wrong or missing? Why does this matter?
3. **Proposed Solution** — High-level approach
4. **Implementation Tasks** — Checkboxes with dependency ordering. These become the tracker for `/work`.
5. **Acceptance Criteria** — How do we know it's done? Measurable, testable.

**Standard and detailed plans also include:**
6. **Decision Rationale** — Why this approach? Alternatives considered? Tradeoffs?
7. **Risk Analysis** — What could go wrong? How do we mitigate it?

**Detailed plans also include:**
8. **Phased Implementation** — Phases with exit criteria per phase
9. **References** — Links to brainstorm, relevant code, past solutions

**Confidence calibration (stated in frontmatter and body):**
- **High:** Clear requirements + existing codebase patterns + bounded scope
- **Medium:** Requirements understood but approach is new territory
- **Low:** Unclear requirements, ambiguous scope, significant unknowns — flag these and suggest `/brainstorm` first

**Exit:** Plan document written.

---

## Phase 5: Handoff

**Entry:** Plan written and saved.

Use **AskUserQuestion** to present options:

**Question:** "Plan ready at `{path}`. What would you like to do next?"

**Options:**
1. **Review and refine** — I'll adjust based on your feedback
2. **Start implementation** — Run `/work` with this plan
3. **Get a second opinion** — Run `/review` on the plan document
4. **Done for now** — Return later

**If user selects "Review and refine":** Accept feedback, update the plan, then present these options again.

**If user selects "Start implementation":** Suggest running `/work {plan-path}`.

**If user selects "Get a second opinion":** Suggest running `/review {plan-path}`.

**If user selects "Done for now":** Confirm the path and remind: "To start later: `/work {plan-path}`"

---

## Validate

Before delivering the plan, verify:

- [ ] Tasks are dependency-ordered — not a flat, unordered list
- [ ] Acceptance criteria are measurable — "users can do X" not "the system is good"
- [ ] Decision rationale explains WHY, not just WHAT (for standard+ plans)
- [ ] Someone new could start `/work` from this plan without clarifying questions
- [ ] Confidence level is stated and honest
- [ ] No code was written — only the plan document was created

## What Makes This Superpowered

- **Task Decomposition (2.3):** Tasks broken down with dependency ordering, not dumped as a flat list.
- **Prompt Mastery (2.2):** The plan IS a well-structured prompt for `/work`. Clear enough that execution requires no guessing.
- **Strategic AI Dialogue (2.4):** Decision rationale captures reasoning — not just conclusions, but why alternatives were rejected.
- **Critical Trust (2.1):** Risks flagged honestly. If uncertain, the plan says so.

## Knowledge References

- `../knowledge/decision-frameworks.md` — How to evaluate tradeoffs
- `../knowledge/strategic-decomposition.md` — How to break work into dependency-ordered steps
