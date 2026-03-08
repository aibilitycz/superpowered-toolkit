---
name: compound
description: >
  Capture a recently solved problem as a searchable solution document. Use after fixing
  non-trivial bugs, resolving tricky issues, or discovering gotchas worth preserving.
  Triggers: compound, document solution, capture fix, save solution, knowledge compound,
  document this, save this fix.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Write
  - Edit
  - Bash
---

# Compound

Capture a recently solved problem while context is fresh. The solution goes into `docs/solutions/` with searchable frontmatter so next time someone hits the same issue, the answer is already there.

**Why "compound"?** Each documented solution compounds your team's knowledge. The first time you solve a problem takes research. Document it, and the next occurrence takes minutes. Knowledge compounds.

## Workflow

### 1. Detect the Problem

**If invoked with context** (e.g., after a fix in the current session):
- Scan the recent conversation for: what broke, what was investigated, what fixed it
- Identify: component, symptoms, root cause, fix

**If invoked with an argument** (e.g., `/compound auth token refresh`):
- Use the argument as a hint for what to document
- Ask clarifying questions if the problem/fix isn't clear from context

**If invoked with no context:**
- Ask: "What problem did you just solve? Brief description is fine — I'll help structure it."

### 2. Research Duplicates

Before writing, check if this solution already exists:

```
Search docs/solutions/ for:
- Similar symptoms or component names
- Same error messages
- Same root cause category
```

**If a related solution exists:**
- Announce: "Found related: `docs/solutions/{path}`. Update the existing doc or create a new one?"
- If updating, edit the existing file to add the new context

### 3. Extract Solution

From the conversation or user input, extract:

1. **Problem** — What happened? What were the symptoms?
2. **Root cause** — Why did it happen? What was actually wrong?
3. **Fix** — What resolved it? Include the specific change.
4. **Prevention** — How to avoid this in the future? Tests, checks, patterns.

### 4. Write Solution Document

**Output path:** `docs/solutions/{domain}/{kebab-topic}.md`

**Domains:** Choose the most specific: `auth`, `database`, `scoring`, `frontend`, `backend`, `infrastructure`, `deployment`, `testing`, `integration`, or create a new one if needed.

**YAML frontmatter:**
```yaml
---
title: "{Brief description of the problem and fix}"
date: YYYY-MM-DD
domain: {domain}
component: {specific component or service}
symptoms:
  - "symptom 1"
  - "symptom 2"
root_cause: "{one-line root cause}"
severity: {low|medium|high|critical}
related: []
---
```

**Document structure:**
```markdown
# {Title}

## Problem
{What happened. Symptoms. How it manifested.}

## Root Cause
{Why it happened. The actual underlying issue.}

## Fix
{What resolved it. Specific code changes, config changes, or commands.}

```{language}
// The specific fix — code diff, config change, command
```

## Prevention
{How to avoid this in the future. Tests to add, patterns to follow, checks to implement.}

## Related
- {Links to related solutions, ADRs, or documentation}
```

### 5. Confirm

After writing:
```
Solution captured at docs/solutions/{domain}/{topic}.md
Searchable by: {list of frontmatter symptoms and keywords}
```

## What Makes This Superpowered

- **Knowledge Compounding (3.4):** Every solution captured makes the next occurrence faster. The library grows with use.
- **Iterative Learning (3.1):** You learned something by doing — now it's preserved for next time.
- **Knowledge Architecture (3.2):** Solutions are structured with frontmatter for machine retrieval. Not a blog post — a searchable knowledge base.
- **Cross-plugin bridge:** Other plugins surface these solutions automatically. `/plan` checks `docs/solutions/` before planning. `/review` suggests `/compound` when it finds insights.

## Anti-patterns

- **Documenting the obvious.** "I fixed a typo" doesn't need a solution doc. Save this for non-trivial problems.
- **Writing a novel.** Keep it concise. Problem → root cause → fix → prevention. Not a blog post.
- **Skipping the frontmatter.** The frontmatter IS the search index. Without symptoms and root_cause, the doc is hard to find later.
- **Never searching first.** Always check `docs/solutions/` before creating a new doc. Duplicates dilute the library.
