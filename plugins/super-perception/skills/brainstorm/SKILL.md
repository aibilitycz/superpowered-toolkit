---
name: brainstorm
description: >
  Collaborative discovery before planning. Explore the problem space, evaluate approaches,
  surface past work, and produce a structured brainstorm document. Triggers: brainstorm,
  explore, discovery, ideate, think through, what should we build, explore approaches.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Agent
  - Write
  - Edit
  - Bash
---

# Brainstorm

Collaborative discovery before planning. Brainstorming answers **WHAT** to build and **WHY** — it precedes `/plan`, which answers **HOW**.

## Workflow

### 1. Assess Whether Brainstorming Is Needed

Not everything needs a brainstorm.

**Skip brainstorming if:**
- Requirements are already clear and specific
- The approach is obvious (well-known pattern, done before)
- It's a small bug fix or routine task

**Suggest skipping:** "Your requirements are clear enough to proceed directly to `/plan`. Want to brainstorm anyway, or go straight to planning?"

**Brainstorm when:**
- The problem is ambiguous or has multiple valid approaches
- It's a significant feature with architectural implications
- The user isn't sure what they want yet
- There's real risk of building the wrong thing

### 2. Reframe the Problem

This is the critical step that makes brainstorming superpowered. Before exploring solutions, question the problem.

**Ask:**
- "What problem are we actually solving?" — Strip away assumptions. Get to the root need.
- "Who has this problem and when?" — Context changes solutions. A problem for 10 users is different from 10,000.
- "What does success look like?" — Not features, outcomes. What's true when this is done?

**Don't skip this.** The biggest waste in software isn't slow execution — it's building the wrong thing. 5 minutes of reframing saves days of rework.

### 3. Research What Exists

Launch the **researcher** agent to scan:
1. `docs/brainstorms/` — past brainstorms on similar topics
2. `docs/solutions/` — past solutions that might be relevant
3. Codebase — existing patterns, similar features, related code
4. `docs/plans/` — any plans that touch this area

**Surface findings:**
```
>> Related brainstorm: docs/brainstorms/2026-02-15-notifications-brainstorm.md
>> Existing pattern: services/email-notifier/ (notification handling)
>> Past solution: docs/solutions/infrastructure/sse-auth-token-refresh.md
```

### 4. Explore Approaches

Through collaborative dialogue, explore 2-3 approaches. For each:
- **What it optimizes for** (speed, flexibility, simplicity, etc.)
- **What it costs** (complexity, maintenance, time, risk)
- **Who's done this before** (prior art in the codebase or industry)

**Question techniques:**
- Ask one question at a time — not a questionnaire
- Prefer multiple choice when natural options exist
- Start broad (purpose, users), narrow to specifics (constraints, edge cases)
- Validate assumptions explicitly: "I'm assuming X — correct?"

**Exit when:**
- The approach is clear and the user says "proceed"
- You've explored enough to make an informed decision
- The user signals they've decided

### 5. Make Decisions Explicit

For each decision made during brainstorming, capture:
- **What was decided** — the choice
- **Why** — the reasoning
- **What was rejected** — alternatives considered

Also capture:
- **Open questions** — things that need to be resolved during planning or implementation
- **Out of scope** — things explicitly excluded

### 6. Write Brainstorm Document

**Output path:** `docs/brainstorms/YYYY-MM-DD-{kebab-topic}-brainstorm.md`

**YAML frontmatter:**
```yaml
---
title: "{Topic}"
type: brainstorm
date: YYYY-MM-DD
participants: [{who was involved}]
related:
  - {links to related brainstorms, plans, solutions}
---
```

**Document structure:**
```markdown
# {Topic}

## Problem Statement
{The actual problem, reframed if needed}

## What We're Building
{High-level description of the approach}

## Why This Approach
{Decision rationale}

## Key Design Decisions
### Q1: {Decision} — RESOLVED
**Decision:** {What was decided}
**Rationale:** {Why}
**Alternatives:** {What else was considered}

## Resolved Questions
{Questions that were answered during brainstorming}

## Open Questions
{Questions that need to be answered during planning/implementation}

## Next Steps
1. /plan — create implementation plan from these decisions
```

### 7. Offer Next Steps

```
Brainstorm captured at docs/brainstorms/YYYY-MM-DD-{topic}-brainstorm.md

Next: /plan to turn these decisions into an implementation plan.
```

## What Makes This Superpowered

- **Problem Reframing (1.4):** The brainstorm questions the problem before solving it. "What are we actually solving?" is the highest-leverage question.
- **Opportunity Recognition (1.2):** The researcher agent surfaces past work, patterns, and prior art. You see what's already there before building something new.
- **AI-Augmented Discovery (1.3):** Multi-source research synthesized into insights. The agent connects dots across brainstorms, solutions, and code.
- **AI Curiosity (1.1):** Exploring multiple approaches before committing. The brainstorm rewards looking around, not jumping to the first idea.

## Anti-patterns

- **Brainstorming alone.** A brainstorm is collaborative. Ask questions, challenge assumptions, explore together.
- **Jumping to solutions.** "Let's use WebSockets" is a solution, not a brainstorm. Start with the problem.
- **Endless exploration.** Brainstorming has diminishing returns. When the approach is clear, stop. Move to `/plan`.
- **Not writing it down.** A brainstorm that isn't documented is a conversation that's forgotten. Write the doc.
- **Brainstorming trivial things.** Small tasks don't need brainstorms. Use judgment.
