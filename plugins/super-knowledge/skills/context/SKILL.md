---
name: context
description: >
  Build and maintain structured context documents for AI consumption. Use when you need
  to create or update CLAUDE.md files, knowledge docs, onboarding guides, or any structured
  context that AI will consume repeatedly. Triggers: context, create context, update context,
  build context, context doc, knowledge doc, CLAUDE.md.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Write
  - Edit
  - Bash
---

# Context

Build and maintain structured context documents. The right context makes AI dramatically more effective — this skill helps you create context docs that are typed, versioned, and organized for retrieval.

## Workflow

### 1. Understand the Need

**If invoked with a topic** (e.g., `/context authentication patterns`):
- Use the topic to scope what context doc to create or update
- Check if relevant context already exists (CLAUDE.md, knowledge files, docs/)

**If invoked without a topic:**
- Ask: "What knowledge does AI need to have for your project? Describe the topic or point me to the files."

### 2. Assess What Exists

Before creating anything, scan for existing context:

```
- Read project CLAUDE.md — what's already documented?
- Check knowledge/ directories — any overlap?
- Search docs/ for related documentation
- Check if this should be added to an existing doc rather than creating a new one
```

**Principle: update > create.** If existing context covers this topic, update it. Don't create parallel docs that drift.

### 3. Determine Context Type

| Type | When to Use | Where It Goes |
|------|------------|--------------|
| **Project CLAUDE.md** | Core conventions, patterns, and rules that apply to every session | Root `CLAUDE.md` |
| **Knowledge file** | Domain-specific reference that skills/agents load on demand | `knowledge/{topic}.md` |
| **Onboarding doc** | Setup instructions, architecture overview, getting started | `docs/developers/` |
| **Decision record** | Why a specific technical decision was made | `docs/decisions/` or `architecture/decisions/` |

### 4. Write the Context Doc

**For CLAUDE.md updates:**
- Keep it concise — CLAUDE.md is loaded every session, so every line costs attention
- Structure: what matters most first, details later
- Use tables for quick reference, decision trees for conditional logic
- Link to detailed docs rather than inlining everything

**For knowledge files:**
- 800-1200 words
- Accessible voice — written for practitioners, not academics
- Structure: what and why → how → pitfalls/anti-patterns
- Cross-reference related knowledge files

**For any context doc:**
- Open with purpose — why does this doc exist, when should you read it?
- Be specific — "use snake_case for database columns" not "follow naming conventions"
- Include examples — show, don't just tell
- Date it — context goes stale, dates help assess freshness

### 5. Verify Integration

After writing or updating:
- If it's a knowledge file, verify the skill that references it can find it
- If it's CLAUDE.md, verify it doesn't duplicate existing entries
- If it's a doc, verify it's linked from the relevant index or knowledge map

## What Makes This Superpowered

- **Context Engineering (3.3):** This IS context engineering — preparing the right context for AI consumption.
- **Knowledge Architecture (3.2):** Organized, typed, discoverable. Not random docs — structured knowledge.
- **Only Handle It Once (OHIO):** Write the context once, structured well. Every future session benefits.

## Anti-patterns

- **Context dumps.** Pasting everything into CLAUDE.md. Keep it focused — link to details.
- **Stale context.** Context that was true 6 months ago but isn't now. Date your docs. Review periodically.
- **Duplicate context.** Two docs saying the same thing — they'll drift. One source of truth.
- **Context without structure.** A wall of text is worse than no context. Use headings, tables, decision trees.
