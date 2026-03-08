---
name: orchestrate
description: >
  Cross-plugin workflow conductor. Detects where you are in the workflow, suggests the next
  phase, and maintains artifact flow between plugins. Triggers: orchestrate, workflow, what's next,
  full flow, brainstorm to ship, lifecycle, conduct.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
---

# Orchestrate

The conductor. Detects where you are in the superpowered workflow, suggests the next phase, and ensures artifacts flow between plugins. This skill doesn't do the work — it routes to the right superpower.

## The Full Loop

```
/brainstorm (Super Perception)
    ↓ writes: docs/brainstorms/YYYY-MM-DD-{topic}-brainstorm.md
/plan (Super Intelligence)
    ↓ reads brainstorm, writes: docs/plans/YYYY-MM-DD-{topic}-plan.md
/work (Super Creation)
    ↓ reads plan, executes tasks, commits incrementally, ships (quality checks + push)
/review (Super Intelligence)
    ↓ reads changes, produces evidence-based review
/compound (Super Knowledge)
    ↓ captures solution: docs/solutions/{domain}/{topic}.md
```

Not every task needs the full loop. Small fixes skip brainstorm and plan. Medium tasks skip brainstorm. Only significant features run the complete cycle.

## Workflow

**Keyword routing — what the user says → what to suggest:**

| User Says | Suggest |
|-----------|---------|
| "I have an idea" / "what should we build" / "explore" | `/brainstorm` |
| "plan this" / "how should we build" / "break this down" | `/plan` |
| "let's build" / "start working" / "execute" / "implement" | `/work {plan-path}` |
| "review this" / "check the code" / "is this ready" | `/review` |
| "document this" / "save this fix" / "capture" | `/compound` |
| "what's next" / "where are we" / "status" | Run the detect → assess flow below |

### 1. Detect Current State

**Entry:** User invoked `/orchestrate` or asked "what's next?"
**Exit:** Workflow artifacts scanned — brainstorms, plans, branches, solutions cataloged.

Scan the project for workflow artifacts:

```bash
# Recent brainstorms (last 14 days)
ls -la docs/brainstorms/*.md 2>/dev/null | tail -5

# Active plans
grep -rl "status: active" docs/plans/*.md 2>/dev/null

# Current branch and uncommitted changes
git status --short
git log --oneline -5

# Recent solutions
ls -la docs/solutions/**/*.md 2>/dev/null | tail -5
```

### 2. Assess Phase

**Entry:** Artifacts scanned.
**Exit:** Current phase identified with confidence.

Based on what exists, determine where the user is:

| Signals | Phase | Suggest |
|---------|-------|---------|
| No brainstorm, no plan, vague idea | **Discovery** | `/brainstorm` — explore the problem first |
| Recent brainstorm, no plan | **Planning** | `/plan {brainstorm-path}` — turn decisions into a plan |
| Active plan with unchecked tasks | **Execution** | `/work {plan-path}` — start building |
| Active plan, all tasks checked | **Review** | `/review` — check the code before shipping |
| Review complete, tests passing | **Finalize** | `/work` — finalize and push (shipping is step 7 of /work) |
| Just shipped or fixed something non-trivial | **Compounding** | `/compound` — capture the solution |
| Everything current is shipped | **Done** | No action needed. Start a new cycle when ready. |

### 3. Present Status and Recommendation

**Entry:** Phase assessed.
**Exit:** Status and recommendation presented to user.

```markdown
## Workflow Status

**Current phase:** {phase}
**Active artifacts:**
- Brainstorm: {path or "none"}
- Plan: {path or "none"}
- Branch: {branch name}
- Uncommitted changes: {yes/no}

**Recommended next step:** {command with path}
**Why:** {one sentence reasoning}

**Alternative:** {if there's a reasonable alternative}
```

### 4. Route to the Right Superpower

**Entry:** User chose a next step.
**Exit:** User guided to the correct skill with the right arguments.

After the user chooses:
- Guide them to invoke the right skill
- Provide the correct argument (e.g., the brainstorm path for `/plan`)
- Note any context the next skill should know

## Partial Flows

Not everything needs the full loop:

| Task Size | Recommended Flow |
|-----------|-----------------|
| **Trivial** (typo, config) | Just fix it. No workflow needed. |
| **Small** (< 1 hour, clear scope) | `/work` → commit. Skip brainstorm, plan, and review. |
| **Medium** (1-3 days, clear approach) | `/plan` → `/work` → `/review` |
| **Large** (multi-day, unclear approach) | Full loop: `/brainstorm` → `/plan` → `/work` → `/review` → `/compound` |
| **Exploration** (no clear goal yet) | `/brainstorm` only. Decide next steps after. |

## Cross-Plugin Conventions

How plugins find each other's artifacts:

| Artifact | Location | Frontmatter |
|----------|----------|-------------|
| Brainstorm | `docs/brainstorms/YYYY-MM-DD-{topic}-brainstorm.md` | `type: brainstorm`, `related:` |
| Plan | `docs/plans/YYYY-MM-DD-{type}-{topic}-plan.md` | `type: {feat\|fix\|...}`, `status: active`, `brainstorm:` |
| Solution | `docs/solutions/{domain}/{topic}.md` | `domain:`, `symptoms:`, `root_cause:` |

**The `related:` field** in frontmatter is how artifacts link across phases. A plan's `brainstorm:` field points to its brainstorm. A solution's `related:` field points to the plan that generated it.

## What Makes This Superpowered

- **Workflow Orchestration (5.2):** This IS workflow orchestration — routing work through the right tools at the right time.
- **Augmentation Vision (5.1):** The status view shows how human + AI collaboration works across the full lifecycle.
- **Process Decomposition (5.3):** Breaking complex projects into plugin-appropriate phases.
- **The compound effect:** When the full loop completes, the knowledge captured makes the next loop faster. Orchestrate makes this visible.

## Anti-patterns

- **Orchestrating trivial tasks.** Don't run the full loop for a typo fix. Use judgment.
- **Auto-advancing.** Never auto-advance between phases. The human decides when to move forward.
- **Forcing the full loop.** Partial flows are fine. Not every task needs brainstorming.
- **Orchestrating without other plugins.** This skill needs the other superpowers installed. Without them, it's just suggestions.
