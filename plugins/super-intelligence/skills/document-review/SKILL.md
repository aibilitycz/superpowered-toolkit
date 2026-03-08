---
name: document-review
description: >
  Structured evaluation of brainstorms, plans, and specs against Critical Trust criteria.
  Use when reviewing a document before starting work, after writing a plan, or when
  evaluating a spec for completeness. Triggers: document review, review document, review plan,
  review brainstorm, review spec, evaluate document, check plan.
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Document Review

Evaluate brainstorms, plans, and specs before they drive implementation. Catches missing reasoning, unidentified risks, and scope gaps — the things that cause rework when discovered mid-build.

## Workflow

### 1. Read the Document

Read the full document. Don't skim — read it once, thoroughly.

### 2. Evaluate Against Criteria

Apply each criterion. Not as a checkbox pass — think about each one in the context of THIS document and what it's trying to achieve.

#### Does it explain WHY?

- Is there a decision rationale? Not just "we'll use X" but "we'll use X because Y, and we considered Z."
- If the document describes a technical approach, can you understand the reasoning? Could someone new to the project follow the logic?
- Are there decisions made without explanation? Flag each one.

#### Are risks identified?

- Does the document acknowledge what could go wrong?
- Are mitigations proposed for the significant risks?
- Are there risks the author seems to have missed? (Security, performance, backward compatibility, data migration, cross-team dependencies)

#### Is the scope clear?

- Can you tell exactly what's in scope and what's not?
- Are there ambiguous areas where someone might reasonably assume something is included but it's not mentioned?
- Is there an explicit "out of scope" or "deferred" section?

#### Are acceptance criteria measurable?

- Can you determine, from the criteria alone, whether the feature is complete?
- Are criteria testable? "Users can do X" is testable. "The system is fast" is not.
- Are there important behaviors not covered by any acceptance criterion?

#### Are there unresolved open questions?

- Are there open questions that should be answered before work begins?
- Are there assumptions stated without verification?
- Are there "TBD" or "TODO" items that would block implementation?

#### Is it actionable?

- Could someone start `/work` from this document right now?
- Are tasks specific enough to implement without guessing?
- Are dependencies between tasks clear?

### 3. Present Findings

```markdown
## Document Review: [filename]

### Strengths
- [What's well done — be specific, not generic praise]

### Gaps
- [GAP-1] [What's missing or unclear] — Why this matters for implementation.
- [GAP-2] ...

### Suggestions
- [SUG-1] [Specific improvement] — How this makes the document more actionable.
- [SUG-2] ...

### Verdict: READY / NEEDS REFINEMENT

[1-2 sentence summary. If NEEDS REFINEMENT, name the top 1-3 things to fix before starting work.]
```

**Verdict guide:**
- **READY:** The document has clear scope, decision rationale, identified risks, and actionable tasks. Minor suggestions can be addressed during implementation.
- **NEEDS REFINEMENT:** There are gaps that would cause confusion or rework if not addressed first. Specify what needs to change.

## What This Is Not

- **Not an editor.** Don't fix grammar, style, or formatting. Focus on content.
- **Not a blocker factory.** The goal is to make documents more actionable, not to create busywork. If a document is 90% ready and the gaps are minor, verdict is READY with suggestions.
- **Not a template check.** Don't evaluate whether the document follows a specific template. Evaluate whether it contains the thinking needed to drive good implementation.

## What Makes This Superpowered

- **Critical Trust (2.1):** Evaluates with evidence. "This section is unclear" always comes with WHY and what would make it clear.
- **Strategic AI Dialogue (2.4):** The review isn't a checklist — it's a thoughtful evaluation of whether the document models good reasoning.
- **Practical focus:** Every finding points toward action. Not "this is incomplete" but "this is incomplete — add X to unblock Y."
