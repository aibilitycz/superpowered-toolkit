---
name: think
description: >
  Deep reasoning for complex decisions — expert panel simulation, devil's advocate,
  what-if scenarios, and structured tradeoff analysis. Use when a decision has high stakes,
  multiple valid approaches, or you need to stress-test your thinking. Triggers: think,
  think through, analyze, expert panel, devil's advocate, what if, tradeoff, decision,
  weigh options, stress test, second opinion.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Bash
---

# Think

Deep reasoning for decisions that matter. Not for every question — for the ones where getting it wrong is expensive. Expert perspectives, devil's advocate, what-if scenarios, and structured tradeoff analysis.

## When to Use /think

- **High-stakes decisions** — architecture choices, scoring formula changes, security design
- **Multiple valid approaches** — you need to weigh tradeoffs, not just pick one
- **Stress-testing** — you have a plan and want to find the holes before building
- **Stuck** — you've been going in circles and need a structured way out

**When NOT to use /think:** For decisions that are easily reversible, low-stakes, or have obvious answers. Just decide and move.

## Workflow

### 1. Frame the Question

**If invoked with a question** (e.g., `/think should we use WebSockets or SSE for real-time updates?`):
- Use the question as the starting point
- Gather relevant context: what does the codebase currently do? What are the constraints?

**If invoked without a question:**
- Ask: "What decision or problem do you want to think through?"

**If invoked with `ultrathink`** (e.g., `/think ultrathink`):
- Enable extended thinking mode — deeper analysis, more perspectives, longer chains of reasoning

### 2. Choose the Mode

| Mode | When | What It Does |
|------|------|-------------|
| **Expert Panel** | Multiple domains intersect | Simulate 3-5 relevant expert perspectives |
| **Devil's Advocate** | You have a preferred option | Systematically attack it. Find every reason it fails. |
| **What-If Analysis** | Uncertain about consequences | Trace each option forward through concrete scenarios |
| **Tradeoff Matrix** | Comparing options across criteria | Structured comparison with weighted criteria |

**If mode isn't obvious from the question, default to Expert Panel** — it's the most versatile.

### 3. Think

#### Expert Panel

Identify 3-5 relevant expert perspectives based on the question. Not generic experts — specific perspectives that illuminate different facets of THIS decision.

For each expert:
```
### [Expert perspective name]

**Lens:** What this perspective focuses on
**Assessment:** What they see in this situation
**Recommendation:** What they'd do and why
**Concern:** What worries them about other approaches
```

Then synthesize:
```
### Synthesis
Where experts agree: [consensus]
Where they disagree: [tensions]
The key tradeoff: [the core tension to resolve]
```

#### Devil's Advocate

Take the proposed approach and systematically attack it:

1. **Steel man it first** — state the strongest version of why this approach makes sense
2. **Attack the assumptions** — what must be true for this to work? Is each assumption actually true?
3. **Find the failure modes** — how does this break? Under what conditions?
4. **Identify the hidden costs** — what does this approach make harder in the future?
5. **Propose the counter-argument** — what's the strongest alternative?

#### What-If Analysis

For each option, trace forward through concrete scenarios:

```
### Option A: [name]

**If it goes well:** [best realistic outcome, with specifics]
**If it goes okay:** [likely outcome, with specifics]
**If it goes badly:** [worst realistic outcome, with specifics]
**Reversibility:** [how hard is it to undo this decision?]
**What you learn:** [what does this choice teach you, even if it fails?]
```

#### Tradeoff Matrix

Define criteria, weight them, score each option:

```
| Criterion (weight) | Option A | Option B | Option C |
|---------------------|----------|----------|----------|
| Speed to ship (30%) | 8/10     | 5/10     | 7/10     |
| Maintainability (25%)| 6/10    | 9/10     | 7/10     |
| Risk (25%)          | 7/10     | 8/10     | 5/10     |
| Team capability (20%)| 9/10    | 6/10     | 7/10     |
| **Weighted total**  | **7.4**  | **7.0**  | **6.5**  |
```

### 4. Conclude

Every `/think` session ends with a clear recommendation:

```
## Recommendation

**Do:** [specific recommendation]
**Because:** [1-2 sentence reasoning]
**Risk:** [the main risk of this choice and how to mitigate it]
**Confidence:** [low/medium/high] — [why]
```

If there's no clear winner, say so. "Both A and B are defensible. Here's the tiebreaker question: [the one thing that determines which is better]."

## What Makes This Superpowered

- **Critical Trust (2.1):** You don't trust your first instinct on hard decisions. You stress-test it.
- **Strategic AI Dialogue (2.4):** This IS strategic AI dialogue — using AI as a thinking partner, not just an executor.
- **Task Decomposition (2.3):** Complex decisions get decomposed into evaluable components.
- **The thinking that prevents rework.** 30 minutes of `/think` before a week of `/work` often saves the week.

## Knowledge References

- `../knowledge/decision-frameworks.md` — Stakes matrix, when to decide fast vs. slow
- `../knowledge/critical-evaluation.md` — Evidence types, uncertainty flagging
- `../knowledge/strategic-decomposition.md` — Breaking complex problems into evaluable parts
