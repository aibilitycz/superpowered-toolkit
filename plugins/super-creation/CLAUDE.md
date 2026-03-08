# Super Creation

Creating, building, and shipping at speed. AI does 90%, you craft the 10% that matters. This plugin embodies SP Superpower 4 — execution with creative courage, focused craft, and a bias toward shipping.

## Methodology Anchor

- **Superpower:** Super Creation (SP Superpower 4)
- **Sub-competencies activated:**
  - **4.1 Creative Courage** — Ship incrementally. Don't wait for perfect — ship good and iterate.
  - **4.2 The 90/10 Craft** — Focus on the 10% that matters. AI handles the volume, you handle the quality.
  - **4.3 Building** — Execute plans, write code, run tests, commit working software.
  - **4.4 Multi-Format Production** — Ship skill handles release notes, changelogs, and documentation in one pass.
- **How it activates them:** `/work` executes plans from start to ship — continuous testing, incremental commits, quality checks, release notes. One skill, full lifecycle. The workflow rewards finishing, not perfecting.
- **Why this belongs:** Ideas without execution are worthless. This plugin turns plans into shipped software.

See `../../METHODOLOGY.md` for the four capability layers and methodology anchor rule.

## Core Principles

1. **Ship > perfect.** A finished feature that ships beats a perfect feature that doesn't. Iterate after shipping.
2. **The 90/10 rule.** AI generates 90% of the code. Your job is the 10% that makes it right — architecture decisions, edge cases, naming, test design.
3. **Test as you go.** Run tests after every change, not at the end. Continuous testing prevents big surprises.
4. **Follow existing patterns.** Don't reinvent. Read the codebase, match what exists. Consistency beats cleverness.
5. **Small commits, frequent pushes.** Each commit is a complete, working unit. Don't batch up large changes.

## Decision Trees

### Is This Task Ready for /work?

```
Do you have a plan with checkboxes?
├─ Yes → Are the tasks specific enough to implement without guessing?
│  ├─ Yes → Start /work
│  └─ No → Clarify the plan first (/plan or /document-review)
├─ No → Is it a small, clear task (< 1 hour)?
│  ├─ Yes → Just do it — no plan needed
│  └─ No → Write a plan first (/plan)
└─ Not sure → /plan — planning is never wasted for non-trivial work
```

### When to Commit

```
Did you just complete a logical unit?
├─ Yes → Do tests pass?
│  ├─ Yes → Commit with a descriptive message
│  └─ No → Fix the tests first, then commit
└─ No → Keep working — don't commit partial units
   └─ Exception: about to attempt something risky?
      └─ Yes → Commit current state as a checkpoint
```

## Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| [Work](skills/work/SKILL.md) | `/work` | Execute a plan from start to ship — implement, test, commit, quality checks, release notes, push |

## Knowledge

| File | Topic |
|------|-------|
| [The 90/10 Craft](knowledge/ninety-ten-craft.md) | How to focus on the 10% that matters — what AI handles, what you craft |

## Disclaimer

This plugin provides structured execution workflows. It does not replace code review, testing, or human judgment about what to ship. Always verify AI-generated code before deploying to production.
