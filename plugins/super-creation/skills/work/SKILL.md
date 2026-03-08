---
name: work
description: >
  Execute a plan — read tasks, implement in dependency order, test continuously, commit
  incrementally. Uses the plan's own checkboxes as the tracker. Triggers: work, execute plan,
  implement, start work, build, implement plan.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Write
  - Edit
  - Bash
---

# Work

Execute a plan. Read the tasks, implement them in dependency order, test after every change, commit incrementally. The plan's checkboxes are the tracker — tick them off as you go. No separate todo system.

## Workflow

### 1. Read and Understand the Plan

**If invoked with a plan path** (e.g., `/work docs/plans/2026-03-08-feat-notifications-plan.md`):
- Read the plan completely
- Identify: tasks (checkboxes), dependencies between tasks, acceptance criteria

**If invoked without a path:**
- Check `docs/plans/` for the most recent active plan (status: active in frontmatter)
- If found, confirm: "Found plan: [title]. Start working on this?"
- If not found, ask: "Which plan should I execute? Provide a path or describe what to build."

**If anything is unclear:**
- Ask clarifying questions now — better to ask than build the wrong thing
- Focus on: ambiguous requirements, unclear dependencies, missing acceptance criteria

### 2. Set Up Environment

Check the current branch and confirm approach:
```bash
git branch --show-current
git status
```

Follow the project's branching conventions (check CLAUDE.md). Pull latest changes before starting.

### 3. Execute Tasks

For each task in dependency order:

```
while (unchecked tasks remain):
  1. Read the task and any referenced files
  2. Look for similar patterns in the codebase (grep, glob)
  3. Implement following existing conventions
  4. Run relevant tests
  5. If tests pass → check off the task in the plan ([ ] → [x])
  6. Evaluate: commit now or continue to the next task?
```

**Commit heuristic:** Commit when you've completed a logical unit — a model, a service, a component, a migration. Don't commit partial units or WIP state. If the commit message would be "WIP", keep working.

**When tests fail:** Fix immediately. Don't move to the next task with broken tests. If a test failure reveals a plan problem, update the plan.

### 4. Follow Existing Patterns

This is the most important rule of execution:

1. **Read the codebase first.** Before writing new code, find similar patterns.
2. **Match conventions exactly.** Naming, structure, error handling, test patterns.
3. **Reuse existing components.** Don't build what already exists.
4. **Check CLAUDE.md.** The project's conventions are documented there.

The fastest way to introduce bugs is to ignore existing patterns. The fastest way to ship clean code is to follow them.

### 5. Incremental Commits

After completing each logical unit:

```bash
# Stage only the files for this unit
git add <specific files>

# Commit with a descriptive message
git commit -m "feat(scope): description of this complete unit"
```

**Stage specific files — never `git add .`** You might have files from other work in progress.

### 6. Complete and Report

When all checkboxes are checked:

```
All tasks complete. Summary:
- [x] Task 1 — what was done
- [x] Task 2 — what was done
- [x] Task N — what was done

Acceptance criteria status:
- [x] Criterion 1 — verified by test/manual check
- [ ] Criterion 2 — needs verification (explain)

Next: /review to check the code, or /ship if ready.
```

## What Makes This Superpowered

- **Building (4.3):** Execute plans, write code, run tests. The core loop of creation.
- **The 90/10 Craft (4.2):** AI generates the code. Your job is matching patterns, catching edge cases, verifying correctness — the 10% that matters.
- **Creative Courage (4.1):** Ship incrementally. Each commit is a working checkpoint. Don't wait for perfection.
- **No overhead:** Plan checkboxes are the tracker. No separate todo system, no task management ceremony.

## Anti-patterns

- **Starting without reading the plan.** The plan has context, references, and decisions. Read it.
- **Ignoring existing patterns.** The codebase has conventions. Follow them. Don't invent new patterns.
- **Testing at the end.** Test after every change. Continuous testing prevents big surprises.
- **Giant commits.** One commit per logical unit. Small, focused commits are easier to review and revert.
- **80% done syndrome.** Finish the feature. Check every box. Incomplete work is worse than no work.
