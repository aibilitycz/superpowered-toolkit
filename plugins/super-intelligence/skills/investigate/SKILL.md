---
name: investigate
description: >
  Detective-style investigation that follows evidence trails to find root causes, bugs,
  inconsistencies, and hidden problems. Works on code, performance, architecture, data,
  and systems. Three investigative lenses: Sherlock (deduction), Poirot (psychology/intent),
  Columbo (what's missing). Triggers: investigate, debug, detective, find bug, root cause,
  what's wrong, diagnose, trace, why is this broken, what happened.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Bash
---

# Investigate

Detective-style investigation. Not a checklist runner, not a linter — a detective that follows evidence trails, notices what's missing, and connects things others overlook.

## The Three Minds

Three investigative lenses. Not roleplay — reasoning frameworks that each unlock a different class of problems:

**Sherlock Holmes** — Deductive elimination. Deduce what MUST be true for something to work correctly, then verify each premise. "When you have eliminated the impossible, whatever remains, however improbable, must be the truth." Catches structural problems: logic errors, broken invariants, impossible states, type mismatches.

**Hercule Poirot** — Psychological method. Study the author's intent and mental model. "It is the brain, the little grey cells, on which one must rely." Sees the gap between what someone THOUGHT the system does and what it ACTUALLY does. Misunderstood APIs, wrong assumptions, subtle misreads.

**Columbo** — Persistent nagging. Something doesn't sit right. "Just one more thing..." Catches what's MISSING — the error handler that should be there, the edge case nobody considered, the test that doesn't exist, the cleanup that never happens.

All three work the same case. Each sees what the others miss.

## Polarities

`/investigate` adapts to what you're investigating:

| Polarity | Focus | Example Trigger |
|----------|-------|----------------|
| **Code** | Bugs, logic errors, type mismatches, broken flows | `/investigate` on a diff or file path |
| **Performance** | Slow queries, memory leaks, bottlenecks, scaling issues | "Why is this slow?" |
| **Architecture** | Pattern violations, coupling, dependency issues, design drift | "Is this the right structure?" |
| **Data** | Integrity issues, schema problems, migration risks, inconsistencies | "The data doesn't look right" |
| **System** | Infrastructure, networking, deployment, runtime failures | "Something is broken in production" |

**Auto-detected from context.** If you provide a diff, it's a code investigation. If you describe a performance problem, it's performance. You can also specify: `/investigate performance why is the scoring endpoint slow?`

## Method

### Phase 1: Survey the Scene (Poirot)

*"I do not leap to the conclusions. First, I observe."*

Understand the full picture before analyzing:
- What is happening? What SHOULD be happening?
- What is the author's/system's mental model? What do they believe about the system?
- What assumptions are being made — are they warranted?
- Does the evidence tell a coherent story, or are there contradictions?

### Phase 2: Examine the Evidence (Holmes)

*"It is a capital mistake to theorize before one has data."*

Apply deductive reasoning:
- What MUST be true for this to work correctly? List the premises.
- What patterns do you observe? What's consistent? What breaks pattern?
- Are the components telling a coherent story?

**Follow the trail.** When something catches your eye, trace it:
- Where does this data come from? Where does it go?
- What calls this? What does this call?
- Are the types/contracts flowing correctly through the chain?

Eliminate the impossible: if a value can be null here and there's no null check, that's not suspicion — it's a deduction.

### Phase 3: Interview the Witnesses (Poirot)

*"Every witness tells you something — even when they lie."*

Study the surrounding context:
- Do the tests actually test what this does, or what the author WISHES it does?
- Do the types/schemas tell the same story as the implementation?
- Does the API contract match what callers expect?
- Is there a mismatch between how existing code uses an interface and how new code provides it?

### Phase 4: Just One More Thing (Columbo)

*"Oh, I'm sorry to bother you again, but there's just one more thing that's been nagging at me..."*

The most important phase. Look for what's MISSING:
- Error cases not handled
- Tests that should exist but don't
- Null/undefined checks absent
- Race conditions in async code
- Cleanup that never happens (listeners, timers, subscriptions, connections)
- Boundary conditions ignored (zero, empty, maximum)
- Logging/monitoring for operations that can fail silently
- Rollback paths for irreversible operations

Keep nagging. The thing that seems like a minor detail is often the whole case.

### Phase 5: Connect the Evidence (Holmes)

*"The game is afoot."*

Synthesize. The problems that matter most hide at intersections:
- A type says one thing, the runtime does another
- A function is async but its caller doesn't await
- A database column is NOT NULL but the API doesn't validate
- A feature flag check exists in one layer but not another
- An error is caught but the operation continues as if it succeeded

Each finding must survive the Holmes test: given the evidence, is there any other explanation?

## Rules of Investigation

1. **Never accuse without evidence.** Every finding cites specific location and explains WHY with a concrete scenario.
2. **Distinguish certainty.** Three levels only:
   - **Conclusive** — This WILL cause a problem. Here's the proof.
   - **Suspicious** — This looks wrong. Here's what could go wrong.
   - **Warrants investigation** — Can't prove it from here, but someone should check.
3. **Follow trails, don't scan categories.** If examining a query leads to a missing index, follow that.
4. **The most dangerous bugs look correct.** Focus on what LOOKS right but isn't.
5. **Assumptions are suspects.** When someone assumed something is always true, check if it is.

## What You Ignore

- Style nitpicks — that's what linters are for
- Suggestions that aren't problems — unless the current state has a defect
- Hypothetical future problems — only real, present danger

## Case Report

```markdown
## Case: [Brief title of what was investigated]

### Scene Assessment
[2-3 sentences: what's happening, the mental model, initial impression]

### Findings

#### [CONCLUSIVE] Finding title
**Evidence:** [location] — [quote the relevant evidence]
**Deduction:** [Why this is definitely a problem, with concrete failure scenario]
**Impact:** [What happens when this fails]

#### [SUSPICIOUS] Finding title
**Evidence:** [location] — [quote the relevant evidence]
**Deduction:** [Why this looks wrong, what could go wrong]
**Recommendation:** [What to verify or fix]

#### [INVESTIGATE] Finding title
**Evidence:** [location] — [quote the relevant evidence]
**Concern:** [What might be wrong but can't be proven from here]
**Question:** [What should be verified]

### Just One More Thing...
[Columbo's parting observations — what SHOULD be here but isn't.
Missing tests, absent error handling, unguarded edge cases.
Each with a concrete scenario of what goes wrong.]

### Case Summary
**Verdict:** CLEAN / MINOR CONCERNS / BUGS FOUND / CRITICAL ISSUES
**Confidence:** [How thoroughly you were able to investigate given the scope]
[1-2 sentence overall assessment]
```

## Adapting to Scope

- **Small scope (< 50 lines, single component):** Go deep. Trace every flow. Read all callers.
- **Medium scope (50-300 lines, few components):** Focus on the riskiest areas. Follow 2-3 trails.
- **Large scope (300+ lines, system-wide):** Prioritize new logic, state changes, and boundaries. Flag areas that deserve deeper investigation.

## What Makes This Superpowered

- **Critical Trust (2.1):** Calibrated certainty. Three levels of confidence, never faking it.
- **Task Decomposition (2.3):** Complex investigations broken into phased methodology.
- **Strategic AI Dialogue (2.4):** The detective asks the questions others forgot. It's the thinking partner that pushes back.
- **Universal.** Code, performance, architecture, data, systems — same methodology, different evidence.

## Knowledge References

- `../knowledge/critical-evaluation.md` — Evidence types, uncertainty flagging
- `../knowledge/decision-frameworks.md` — Stakes matrix for prioritizing investigation depth
- `../agents/investigator.md` — The agent that runs investigations autonomously
