---
name: work
description: >
  Execute a plan from start to ship — read tasks, implement in dependency order, test
  continuously, commit incrementally, run quality checks, and push. The plan's checkboxes
  are the tracker. Triggers: work, execute plan, implement, start work, build, ship, finalize,
  release, push, ready to ship, done building.
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

Execute a plan and ship it. Read the tasks, implement them in dependency order, test after every change, commit incrementally, run quality checks, and push. The plan's checkboxes are the tracker — tick them off as you go. No separate todo system.

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

### 6. Quality Checks (Before Shipping)

When all tasks are complete, run quality checks before pushing:

**Tests:**
```bash
# Run the project's test suite (check CLAUDE.md for the specific command)
# All tests must pass
```

**Linting:**
```bash
# Run the project's linter (check CLAUDE.md for the specific command)
# Fix any violations
```

**Convention check:**
- Does the code follow the project's patterns? (Quick scan of key files)
- Are there any files that shouldn't be committed? (.env, credentials, large binaries)

### 7. Ship

**Final commit and push:**
```bash
git add <specific files>
git commit -m "feat(scope): description

Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin <branch>
```

**If creating a PR** (when project uses branches):
```bash
gh pr create --title "{short title}" --body "{summary + testing notes}"
```

**Generate release notes** for three audiences:

| Audience | Focus |
|----------|-------|
| **Customer** | What they can do now that they couldn't before |
| **Engineering** | What changed, which services, why, test coverage |
| **Business** | Business value, metrics affected |

**Update plan status:** If the plan has `status: active` in frontmatter, update to `status: complete`.

### 8. Complete and Report

```
All tasks complete. Shipped.

Summary:
- [x] Task 1 — what was done
- [x] Task N — what was done

Acceptance criteria: all met / [list any that need verification]

Suggested next:
- /compound — if this work has insights worth preserving
- /review — if code hasn't been reviewed yet
- Monitor deployment — check logs, metrics, error rates
```

## What Makes This Superpowered

- **Building (4.3):** Execute plans, write code, run tests. The core loop of creation.
- **The 90/10 Craft (4.2):** AI generates the code. Your job is matching patterns, catching edge cases, verifying correctness — the 10% that matters.
- **Creative Courage (4.1):** Ship incrementally. Each commit is a working checkpoint. Done is better than perfect.
- **Multi-Format Production (4.4):** Three-audience release notes from a single set of changes.
- **No overhead:** Plan checkboxes are the tracker. One skill from start to shipped.

## Anti-patterns

- **Starting without reading the plan.** The plan has context, references, and decisions. Read it.
- **Ignoring existing patterns.** The codebase has conventions. Follow them.
- **Testing at the end.** Test after every change. Continuous testing prevents big surprises.
- **Giant commits.** One commit per logical unit. Small, focused commits are easier to review and revert.
- **80% done syndrome.** Finish the feature. Check every box. Incomplete work is worse than no work.
- **Shipping without tests passing.** Tests are the minimum quality bar. No exceptions.
- **Forgetting release notes.** Every ship should have notes — even internal ones. Future you will thank present you.
