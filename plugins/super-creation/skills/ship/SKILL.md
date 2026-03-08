---
name: ship
description: >
  Finalize a feature — run quality checks, generate release notes, create PR or push.
  Use when work is complete and you're ready to ship. Triggers: ship, finalize, release,
  push, create PR, ship it, ready to ship, done building.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Write
  - Edit
  - Bash
---

# Ship

Finalize a feature and ship it. Run the quality checklist, generate release notes, and push. This is the last step before code goes live.

## Workflow

### 1. Verify Completeness

Check that work is actually done:

```
- Read the plan → are all checkboxes checked?
- Are all acceptance criteria met?
- Is there any uncommitted work? (git status)
```

**If incomplete:** List what's remaining. Ask whether to finish or ship as-is.

### 2. Quality Checks

Run in order. Fix issues before proceeding to the next check.

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

### 3. Generate Release Notes

Produce release notes for **three audiences** from the same changes:

**Customer-facing** (for changelog, release page):
```markdown
### What's New
- {Feature in user terms — what they can do now that they couldn't before}

### Fixes
- {Bug fix in user terms — what works better now}
```

**Engineering** (for team, PR description):
```markdown
### Changes
- {Technical description — what changed, which services, why}

### Testing
- {What was tested, how, coverage}
```

**Business** (for stakeholders, status updates):
```markdown
### Impact
- {Business value — what this enables, metrics affected}
```

### 4. Create Commit and Push

```bash
# Stage all remaining changes
git add <specific files>

# Final commit
git commit -m "feat(scope): ship {feature description}

Co-Authored-By: Claude <noreply@anthropic.com>"

# Push
git push origin <branch>
```

**If creating a PR:**
```bash
gh pr create --title "{short title}" --body "{release notes + testing summary}"
```

### 5. Update Plan Status

If the plan has frontmatter with `status: active`, update to `status: complete`.

### 6. Suggest Next Steps

```
Shipped. All systems go.

Suggested:
- /compound — if this fix has insights worth preserving
- /review — if code hasn't been reviewed yet
- Monitor deployment — check logs, metrics, error rates
```

## What Makes This Superpowered

- **Creative Courage (4.1):** The act of shipping. Done is better than perfect.
- **Multi-Format Production (4.4):** Three-audience release notes from a single set of changes. Customer, engineering, and business — all from the same work.
- **The closing loop:** Ship connects back to `/compound` (capture what you learned) and forward to monitoring (verify it works). It's not the end — it's a transition.

## Anti-patterns

- **Shipping without tests passing.** Tests are the minimum quality bar. No exceptions.
- **Skipping linting.** Linting catches things humans miss. Run it.
- **Shipping incomplete work.** If the plan has unchecked boxes, either finish or explicitly defer them.
- **Forgetting release notes.** Every ship should have notes — even internal ones. Future you will thank present you.
