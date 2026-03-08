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
  - Write
  - Edit
  - Bash
---

# Plan

Strategic planning that fits the problem. Simple features get concise plans. Complex work gets detailed plans with alternatives, risks, and phased implementation. Every plan explains WHY — not just WHAT.

## Common Rationalizations

| Shortcut | Why It Fails | The Cost |
|----------|-------------|----------|
| "Skip research — I already know the codebase" | You know YOUR mental model. The codebase may have changed, or patterns you haven't seen. | Plan conflicts with existing code → rework |
| "Skip decision rationale — the approach is obvious" | Obvious to you, now. Not to the person executing in 2 weeks, or to future-you debugging. | Decisions get questioned, re-litigated, or silently reversed |
| "Make every task detailed — more detail is better" | Over-specified plans are brittle. They break on first contact with reality. | Plan becomes a constraint instead of a guide |
| "Skip risk analysis — it's low risk" | The risks you don't name are the ones that surprise you | Unmitigated risk → emergency debugging |

## Workflow

### 1. Detect Context

**Entry:** User has a topic, brainstorm path, or feature description.
**Exit:** Context understood — brainstorm consumed (if exists), scope clear enough to research.

**If the user provided a brainstorm path or topic:**
- Read the brainstorm document
- Extract key decisions, chosen approach, open questions
- Announce: "Using brainstorm: [filename]. Extracting decisions."

**If the user provided a topic but no brainstorm:**
- Check `docs/brainstorms/` for a recent match (last 14 days, semantic match on filename/frontmatter)
- If found, read it and use as context
- If multiple candidates, ask which one

**If no brainstorm and no clear topic:**
- Ask 2-3 clarifying questions. Not a dialogue marathon — just enough to understand scope, purpose, and constraints.
- Focus on: What problem does this solve? What's the desired outcome? Any constraints?

### 2. Research (One Focused Pass)

**Entry:** Context detected. Scope understood.
**Exit:** Codebase patterns known, past solutions surfaced, constraints identified.

Launch **one subagent** to gather context. Not four parallel agents — one pass that reads what matters.

The subagent should:
1. Read the project's `CLAUDE.md` for conventions and patterns
2. Scan files relevant to the feature (grep for related code, read key files)
3. Check `docs/solutions/` for past solutions that match this problem
4. If a brainstorm exists, cross-reference its decisions

**Surface past solutions:** If `docs/solutions/` has relevant entries, announce them:
```
>> Known pattern: docs/solutions/auth/jwt-refresh-fix.md (high match)
```

**No external research by default.** Only if the topic is genuinely unfamiliar AND the user approves. Most features don't need web searches — they need understanding of what already exists.

### 3. Calibrate Detail Level

**Entry:** Research complete.
**Exit:** Detail level chosen and communicated to user.

Auto-calibrate based on complexity. Don't ask the user to pick a detail level — assess it.

```
CONCISE plan — when:
- Scope is clear and bounded
- One person, one day or less
- Low risk (no auth, scoring, data, money)
- Clear precedent in codebase

STANDARD plan — when:
- Multi-day work but clear approach
- Some risk or new patterns needed
- Decision rationale adds value

DETAILED plan — when:
- Multi-repo or multi-team
- Unclear approach, multiple valid options
- High risk (auth, scoring, data, money, migrations)
- Significant architectural decisions
```

**Tell the user what you chose and why:** "This is a standard plan — multi-day work with a few decisions to document. Let me know if you want more or less detail."

### 4. Write the Plan

**Entry:** Detail level set, research findings available.
**Exit:** Plan document written with tasks, rationale, and acceptance criteria.

**Output path:** `docs/plans/YYYY-MM-DD-{type}-{kebab-topic}-plan.md`

**Types:** `feat`, `fix`, `refactor`, `chore`, `docs`

**YAML frontmatter:**
```yaml
---
title: "{type}: {description}"
type: {feat|fix|refactor|chore|docs}
status: active
date: YYYY-MM-DD
brainstorm: {path if exists}
repo: {GitHub URL if cross-repo}
repo_path: {relative path if cross-repo}
---
```

**Plan structure — all plans include:**

1. **Title and one-line summary**
2. **Problem Statement** — What's wrong or missing? Why does this matter?
3. **Proposed Solution** — High-level approach
4. **Implementation Tasks** — Checkboxes with dependency ordering. These become the tracker for `/work`.
5. **Acceptance Criteria** — How do we know it's done?

**Standard and detailed plans also include:**

6. **Decision Rationale** — Why this approach? What alternatives were considered? What are the tradeoffs?
   - This is the core of strategic planning. A plan without "why" is a todo list.
7. **Risk Analysis** — What could go wrong? How do we mitigate it?

**Detailed plans also include:**

8. **Phased Implementation** — Break into phases with exit criteria per phase
9. **References** — Links to brainstorm, relevant code, past solutions, external docs

### 5. Offer Next Steps

**Entry:** Plan written and saved.
**Exit:** User informed of next steps.

After writing the plan:

```
Plan ready at docs/plans/YYYY-MM-DD-{type}-{topic}-plan.md

Options:
- Review it and refine → I'll adjust based on your feedback
- /review → structured evaluation before starting
- /work → start implementing
```

## What Makes This Superpowered

This isn't a generic plan template. It models the Super Intelligence sub-competencies:

- **Task Decomposition (2.3):** Tasks are broken down with dependency ordering, not dumped as a flat list. The 90/10 split identifies what delivers most value first.
- **Prompt Mastery (2.2):** The plan IS a well-structured prompt for `/work`. Clear enough that execution requires no guessing.
- **Strategic AI Dialogue (2.4):** Decision rationale captures the reasoning process — not just the conclusion, but why alternatives were rejected.
- **Critical Trust (2.1):** Risks are flagged honestly. If something is uncertain, the plan says so instead of projecting false confidence.

## Validate

Before delivering the plan, verify:

- [ ] Tasks are dependency-ordered — not a flat, unordered list
- [ ] Acceptance criteria are measurable — "users can do X" not "the system is good"
- [ ] Decision rationale explains WHY, not just WHAT (for standard+ plans)
- [ ] Someone new could start `/work` from this plan without asking clarifying questions
- [ ] Plan confidence: **high** if codebase patterns exist, **medium** if new territory, **low** if unclear requirements — stated explicitly

## Confidence Calibration

State plan confidence explicitly in the plan document:
- **High confidence:** Clear requirements + existing codebase patterns to follow + bounded scope
- **Medium confidence:** Requirements understood but approach is new territory or involves tradeoffs
- **Low confidence:** Unclear requirements, ambiguous scope, or significant unknowns — flag these and suggest `/brainstorm` first

## Anti-patterns

- **Planning to plan.** Don't over-research. One focused pass, then write. The plan can be refined.
- **Template over substance.** Skip sections that add no value. A concise plan without risk analysis is fine if the risk is genuinely low.
- **Task soup.** Tasks should be ordered and sized. "Implement the feature" is not a task. "Add the migration for X, then update model Y" is.
- **Planning without context.** Always read the codebase first. Plans that ignore existing patterns waste time.

## Knowledge References

- `../knowledge/decision-frameworks.md` — How to evaluate tradeoffs and decide fast vs. slow
- `../knowledge/strategic-decomposition.md` — How to break work into dependency-ordered steps
