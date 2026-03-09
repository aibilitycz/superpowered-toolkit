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
  - AskUserQuestion
  - Bash
---

# Orchestrate

The conductor. Detects where you are in the superpowered workflow, suggests the next phase, ensures artifacts flow between plugins. This skill doesn't do the work — it routes to the right superpower.

## Boundaries

**This skill MAY:** scan for artifacts (read-only), present status, suggest next steps, route to other skills.
**This skill MAY NOT:** edit code, write documents, execute plans, perform reviews. Routing only.

**This skill routes. Other skills do.**

## The Full Loop

```
/brainstorm (Perception)
    ↓ writes: docs/brainstorms/YYYY-MM-DD-{topic}-brainstorm.md
/plan (Intelligence)
    ↓ reads brainstorm, writes: docs/plans/YYYY-MM-DD-{topic}-plan.md
/work (Creation)
    ↓ reads plan, executes tasks, commits, ships
/review (Intelligence)
    ↓ reads changes, produces findings
/compound (Knowledge)
    ↓ captures: docs/solutions/{domain}/{topic}.md
```

Not every task needs the full loop. Match flow to task size.

---

## Phase 0: Keyword Routing

**Entry:** User invoked `/orchestrate` or used a keyword.

**If the user's intent is clear, route immediately:**

| User Says | Route To |
|-----------|----------|
| "I have an idea" / "what should we build" / "explore" | `/brainstorm` |
| "plan this" / "how should we build" / "break this down" | `/plan` |
| "let's build" / "start working" / "execute" / "implement" | `/work {plan-path}` |
| "review this" / "check the code" / "is this ready" | `/review` |
| "document this" / "save this fix" / "capture" | `/compound` |
| "what's next" / "where are we" / "status" | Continue to Phase 1 |

**If intent matches a route:** Suggest the skill directly. Don't scan artifacts first.

**Exit:** Either routed to a skill, or continuing to artifact scan.

---

## Phase 1: Detect Current State

**Entry:** User asked "what's next?" or intent is unclear.

Scan for workflow artifacts:

```bash
# Recent brainstorms (last 14 days)
ls -la docs/brainstorms/*.md 2>/dev/null | tail -5

# Active plans
grep -rl "status: approved\|status: in_progress" docs/plans/*.md 2>/dev/null

# Current branch and changes
git status --short
git log --oneline -5

# Recent solutions
ls -la docs/solutions/**/*.md 2>/dev/null | tail -5
```

Check the project's `CLAUDE.md` for a "Toolkit Output Paths" table and use override paths if present.

### Memory-Informed Routing

When artifacts are found, surface them with direct paths so the user can jump straight in:
- If a brainstorm exists but no plan: `>> Ready for planning: /plan docs/brainstorms/YYYY-MM-DD-topic-brainstorm.md`
- If a plan exists but work hasn't started: `>> Ready for execution: /work docs/plans/YYYY-MM-DD-type-topic-plan.md`
- If recent solutions exist for the topic: `>> Related prior art: docs/solutions/{domain}/{topic}.md`

This reduces friction — the user sees the exact command to run, not just a phase suggestion.

See `../knowledge/autonomy-modes.md` for routing confidence patterns.

**Exit:** Artifacts cataloged.

---

## Phase 2: Assess Phase

**Entry:** Artifacts scanned.

| Signals | Phase | Suggest |
|---------|-------|---------|
| No brainstorm, no plan, vague idea | **Discovery** | `/brainstorm` |
| Recent brainstorm, no plan | **Planning** | `/plan {brainstorm-path}` |
| Active plan with unchecked tasks | **Execution** | `/work {plan-path}` |
| Active plan, all tasks checked | **Review** | `/review` |
| Review complete, tests passing | **Ship** | Push and finalize |
| Just shipped or fixed something non-trivial | **Compounding** | `/compound` |
| Everything shipped | **Done** | No action needed |

**Exit:** Phase identified.

---

## Phase 3: Present Status

**Entry:** Phase assessed.

```markdown
## Workflow Status

**Current phase:** {phase}
**Active artifacts:**
- Brainstorm: {path or "none"}
- Plan: {path or "none"}
- Branch: {branch name}
- Uncommitted changes: {yes/no}

**Recommended next step:** {command with path}
**Why:** {one sentence}
```

Use **AskUserQuestion** with:
- question: "Here's where things stand. What would you like to do?"
- header: "Next step"
- options:
  1. label: "{Recommended action} (Recommended)", description: "{why this is the logical next step}"
  2. label: "Something else", description: "Tell me what you'd like to do instead"
  3. label: "Start fresh", description: "Begin a new workflow cycle"
- multiSelect: false

**If user selects the recommendation:** Guide them to invoke the right skill with the right arguments.

**If user selects "Something else":** Use **AskUserQuestion** (header: "Action", question: "What would you like to do?") with the common skill options as choices, then route.

**Exit:** User routed to the right skill.

---

## Partial Flows

| Task Size | Recommended Flow |
|-----------|-----------------|
| **Trivial** (typo, config) | Just fix it. No workflow needed. |
| **Small** (< 1 hour, clear scope) | `/work` → commit |
| **Medium** (1-3 days, clear approach) | `/plan` → `/work` → `/review` |
| **Large** (multi-day, unclear approach) | `/brainstorm` → `/plan` → `/work` → `/review` → `/compound` |
| **Exploration** (no clear goal) | `/brainstorm` only |

## Cross-Plugin Artifact Conventions

How plugins find each other's artifacts:

| Artifact | Default Location | Key Frontmatter |
|----------|-----------------|-----------------|
| Brainstorm | `docs/brainstorms/YYYY-MM-DD-{topic}-brainstorm.md` | `type: brainstorm` |
| Plan | `docs/plans/YYYY-MM-DD-{type}-{topic}-plan.md` | `type: plan`, `status:`, `brainstorm:` |
| Solution | `docs/solutions/{domain}/{topic}.md` | `type: solution`, `domain:`, `symptoms:` |

The `related:` field links artifacts across phases. A plan's `brainstorm:` points to its brainstorm. A solution's `related:` points to the plan.

Projects can override these paths — see CONVENTIONS.md "Output Artifacts" section.

## What Makes This Superpowered

- **Workflow Orchestration (5.2):** Routing work through the right tools at the right time.
- **Augmentation Vision (5.1):** Status view shows human + AI collaboration across the lifecycle.
- **Process Decomposition (5.3):** Breaking projects into plugin-appropriate phases.
- **The compound effect:** When the full loop completes, knowledge captured makes the next loop faster.

## Anti-patterns

- **Orchestrating trivial tasks.** Don't run the full loop for a typo.
- **Auto-advancing.** Never auto-advance between phases. The human decides.
- **Forcing the full loop.** Partial flows are fine.
