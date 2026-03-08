---
name: compound
description: >
  Capture knowledge — solutions, context docs, learnings, and principles. Use after fixing
  non-trivial bugs, creating context for AI, or discovering patterns worth preserving.
  Triggers: compound, document solution, capture fix, save solution, knowledge compound,
  document this, save this fix, context, create context, update context, build context,
  learn, save learning, remember this.
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

Capture knowledge while context is fresh. Solutions, context docs, learnings — whatever you just discovered, structure it so it's findable and useful next time.

**Why "compound"?** Each piece of captured knowledge compounds your team's effectiveness. The first time you solve a problem takes research. Document it, and the next occurrence takes minutes. Knowledge compounds.

## Common Rationalizations

| Shortcut | Why It Fails | The Cost |
|----------|-------------|----------|
| "Skip duplicate check — I'll just write a new doc" | Parallel docs drift. Two docs about the same thing eventually contradict each other. | Knowledge drift → wrong fix applied next time |
| "Skip frontmatter — it's just metadata" | Frontmatter IS the search index. Without it, the solution is unfindable. | Knowledge captured but never surfaced → wasted effort |
| "Good enough — I'll refine later" | You won't. Context is freshest NOW. Later, you'll forget the nuance. | Incomplete doc → next person can't reproduce the fix |
| "Too trivial to document" | The "trivial" fix that took you 30 minutes will take someone else 30 minutes too | Repeated debugging of known problems |

## Workflow

### 1. Detect What to Capture

Auto-detect the capture type based on context:

| Context | Capture Type | Output |
|---------|-------------|--------|
| Just fixed a bug, resolved an error | **Solution** | `docs/solutions/{domain}/{topic}.md` |
| Need to create/update AI context | **Context doc** | `CLAUDE.md`, `knowledge/{topic}.md`, or `docs/` |
| Discovered a pattern, preference, or principle | **Learning** | `CLAUDE.md` or memory files |

**If invoked after a fix:** Scan conversation for what broke, what was investigated, what fixed it.
**If invoked with a topic** (e.g., `/compound auth token refresh`): Use as a hint, ask if unclear.
**If invoked with no context:** Ask: "What knowledge do you want to capture? A solution, context doc, or learning?"

### 2. Check for Duplicates

Before writing, check if this knowledge already exists:

```
Search docs/solutions/, CLAUDE.md, knowledge/ for:
- Similar symptoms or component names
- Same error messages or topic
- Same root cause or pattern
```

**If related content exists:** "Found related: `{path}`. Update the existing doc or create new?" Principle: **update > create.** Don't create parallel docs that drift.

### 3. Capture

#### Solution Capture

Extract from conversation or user input:

1. **Problem** — What happened? Symptoms?
2. **Root cause** — Why did it happen?
3. **Fix** — What resolved it? Include the specific change.
4. **Prevention** — How to avoid this in the future?

**Output path:** `docs/solutions/{domain}/{kebab-topic}.md`

**Domains:** `auth`, `database`, `scoring`, `frontend`, `backend`, `infrastructure`, `deployment`, `testing`, `integration`, or create a new one if needed.

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

## Prevention
{How to avoid this in the future. Tests, patterns, checks.}

## Related
- {Links to related solutions, ADRs, or documentation}
```

#### Context Doc Capture

Determine the right location:

| Type | When to Use | Where It Goes |
|------|------------|--------------|
| **Project CLAUDE.md** | Core conventions, rules for every session | Root `CLAUDE.md` |
| **Knowledge file** | Domain reference loaded on demand by skills/agents | `knowledge/{topic}.md` |
| **Onboarding doc** | Setup instructions, architecture overview | `docs/developers/` |
| **Decision record** | Why a specific technical decision was made | `architecture/decisions/` |

**For CLAUDE.md:** Keep it concise — loaded every session. Tables for quick reference, decision trees for conditional logic. Link to details rather than inlining.

**For knowledge files:** 800-1200 words. Accessible voice. Structure: what and why → how → pitfalls/anti-patterns. Cross-reference related knowledge files.

**For any context doc:** Open with purpose. Be specific. Include examples. Date it.

#### Learning Capture

For patterns, preferences, or principles:

- **If project-specific:** Add to project CLAUDE.md or memory files
- **If toolkit-wide:** Add to the relevant plugin's knowledge/ directory
- Keep it concise — one pattern per entry

### 4. Verify and Confirm

After writing:
```
Knowledge captured at {path}
Searchable by: {list of frontmatter keywords or section}
```

- If it's a knowledge file, verify the skill that references it can find it
- If it's CLAUDE.md, verify it doesn't duplicate existing entries
- If it's a solution doc, verify frontmatter has searchable symptoms

## What Makes This Superpowered

- **Knowledge Compounding (3.4):** Every solution captured makes the next occurrence faster. The library grows with use.
- **Context Engineering (3.3):** Preparing the right context for AI consumption — structured, typed, discoverable.
- **Knowledge Architecture (3.2):** Solutions with frontmatter for machine retrieval. Context docs organized by type and purpose. Not random docs — structured knowledge.
- **Cross-plugin bridge:** Other plugins surface this knowledge. `/plan` checks `docs/solutions/` before planning. `/review` suggests `/compound` when it finds insights.

## Validate

Before delivering the captured knowledge, verify:

- [ ] **Findable:** Search for the symptoms — does this doc surface? Are frontmatter keywords what someone would actually search for?
- [ ] **Reproducible:** Could someone reproduce the problem from the symptoms description alone?
- [ ] **Verified:** Root cause is confirmed (not just a theory). Fix was tested (not just proposed).
- [ ] **No duplicates:** Searched `docs/solutions/`, `CLAUDE.md`, `knowledge/` — this is genuinely new
- [ ] **Correctly typed:** Solution doc vs. context doc vs. learning — each has different structure and location

**If any element is missing, note it:** "Root cause is suspected but not confirmed — needs verification" is better than leaving it out silently.

## Anti-patterns

- **Documenting the obvious.** "I fixed a typo" doesn't need a solution doc.
- **Writing a novel.** Keep it concise. Problem → root cause → fix → prevention.
- **Skipping the frontmatter.** The frontmatter IS the search index.
- **Never searching first.** Always check existing docs. Duplicates dilute the library.
- **Context dumps.** Don't paste everything into CLAUDE.md. Keep it focused — link to details.
- **Stale context.** Date your docs. Review periodically.
