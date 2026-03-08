# Workflow Patterns

How superpowered workflows connect — the full loop, partial flows, and the transitions between phases. Not project management methodology. Practical patterns for how work actually flows when you're building with AI.

---

## The Full Loop

The complete superpowered workflow:

```
Perceive → Think → Build → Evaluate → Preserve
   |          |        |         |          |
/brainstorm  /plan   /work    /review    /compound
   |          |        |         |          |
discover    decide   execute   verify     capture
```

Each phase maps to a superpower. Each produces an artifact that feeds the next:

| Phase | Superpower | Input | Output |
|-------|-----------|-------|--------|
| Perceive | Super Perception | Vague idea or problem | Brainstorm doc with decisions |
| Think | Super Intelligence | Brainstorm or clear requirements | Plan with tasks and rationale |
| Build | Super Creation | Plan with checkboxes | Working code, tests, commits |
| Evaluate | Super Intelligence | Code changes or diff | Review with findings and verdict |
| Ship | Super Creation | Reviewed code | Released feature, release notes |
| Preserve | Super Knowledge | Solved problem or insight | Solution doc in searchable library |

The loop is self-reinforcing: preserved knowledge makes the next perceive and think phases faster.

---

## Partial Flows

Not every task needs the full loop. The right flow depends on the task's size and clarity.

### No Flow (Just Do It)

For trivial tasks: typo fixes, config changes, formatting.

Just make the change, commit, push. No brainstorm, no plan, no review ceremony. If the change takes less than 15 minutes and the risk is near zero, workflow overhead is waste.

### Short Flow (Plan → Build)

For small, clear tasks: bug fixes with known cause, small features with obvious approach.

```
/plan (or just mental planning) → /work → commit
```

Skip brainstorm (you know what to build), skip formal review (the change is small). Run tests, commit, move on.

### Medium Flow (Plan → Build → Review)

For medium tasks: multi-hour features, changes that touch important logic.

```
/plan → /work → /review → /ship
```

Skip brainstorm (requirements are clear), but get a review (the change is significant enough to warrant one). Ship when the review passes.

### Full Flow (Perceive → Build → Preserve)

For significant work: multi-day features, unclear requirements, high-risk changes.

```
/brainstorm → /plan → /work → /review → /ship → /compound
```

The full loop. Every phase adds value because the work is complex enough to benefit from structured discovery, planning, and knowledge capture.

---

## Transition Patterns

### Brainstorm → Plan

The brainstorm document is the plan's primary input. The transition should be seamless:

- `/plan docs/brainstorms/YYYY-MM-DD-topic-brainstorm.md` reads the brainstorm
- Decisions from the brainstorm become the plan's rationale
- Open questions from the brainstorm become items to resolve in the plan
- The plan's frontmatter links back to the brainstorm via `brainstorm:` field

### Plan → Work

The plan's checkboxes become the work tracker:

- `/work docs/plans/YYYY-MM-DD-type-topic-plan.md` reads the plan
- Tasks are executed in the order specified (dependency-aware)
- Each checkbox gets checked as the task completes
- The plan is the living document — updated as work progresses

### Work → Review

The transition is natural — you've written code, now get it reviewed:

- `/review` with no arguments reviews the current branch diff
- The review can reference the plan for intent context
- Critical issues block shipping; suggestions are author's choice

### Review → Ship

If the review passes:

- `/ship` runs quality checks and generates release notes
- Plan status updates from `active` to `complete`
- Release notes cover three audiences (customer, engineering, business)

### Ship → Compound

After shipping, capture what you learned:

- `/compound` if the work involved non-obvious problems or insights
- The solution doc links back to the plan via `related:` field
- Future brainstorms and plans will surface this solution automatically

---

## Flow Selection Heuristics

How to choose the right flow without overthinking it:

**Start with the minimum viable flow.** You can always add phases:
- Start with "just do it" → if it gets complex, add a plan
- Start with a plan → if requirements are unclear, add a brainstorm
- Start without review → if the change grows, add a review

**Match the flow to the risk, not the size:**
- A 2-line change to the auth system needs a review
- A 200-line change to a README doesn't
- Risk = consequence of getting it wrong, not amount of code

---

## Artifact Conventions

How plugins find each other's outputs:

| Artifact | Location | Key Frontmatter |
|----------|----------|----------------|
| Brainstorm | `docs/brainstorms/YYYY-MM-DD-{topic}-brainstorm.md` | `type: brainstorm`, `related:` |
| Plan | `docs/plans/YYYY-MM-DD-{type}-{topic}-plan.md` | `status: active\|complete`, `brainstorm:` |
| Solution | `docs/solutions/{domain}/{topic}.md` | `domain:`, `symptoms:`, `root_cause:` |

The `related:` field in frontmatter creates the graph between artifacts. A plan links to its brainstorm. A solution links to its plan. This graph is how knowledge compounds — each new artifact connects to the ones that came before.

---

## Anti-patterns

- **Full loop for everything.** Running all 6 phases for a typo fix. Match the flow to the task.
- **Skipping review on risky changes.** Size doesn't determine risk. Auth changes, data migrations, and scoring formula updates always need review.
- **Not compounding.** Finishing work without capturing what you learned. The compound phase is what makes the next loop faster.
- **Linear thinking.** Assuming you must go in order. Sometimes you discover during /work that you need to go back to /plan. That's fine — loops, not lines.
- **Automating transitions.** Trying to auto-advance between phases. Humans decide transitions. The conductor suggests, never decides.
