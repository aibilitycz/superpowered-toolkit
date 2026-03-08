# Super Knowledge

Learn by doing and make everything reusable. Infinite memory. This plugin embodies SP Superpower 3 — knowledge architecture, context engineering, and knowledge compounding. It also houses expert domain knowledge, starting with psychometric measurement science.

## Methodology Anchor

- **Superpower:** Super Knowledge (SP Superpower 3)
- **Sub-competencies activated:**
  - **3.1 Iterative Learning** — Compound captures solutions from practice, not theory. Learn by doing.
  - **3.2 Knowledge Architecture** — Context skill builds structured, discoverable knowledge. Only Handle It Once.
  - **3.3 Context Engineering** — Context docs are typed, versioned, cross-referenced — the right context for AI.
  - **3.4 Knowledge Compounding** — Every solved problem feeds the solution library. Knowledge grows with use.
- **How it activates them:** `/compound` captures solutions, builds context docs, and preserves learnings — one skill for all knowledge capture. The psychometric domain module demonstrates what deep, organized expertise looks like. Using these tools builds the habit of preserving and structuring knowledge.
- **Why this belongs:** Knowledge that isn't captured is lost. This plugin makes knowledge capture automatic and knowledge retrieval effortless.

See `../../METHODOLOGY.md` for the four capability layers and methodology anchor rule.

## Core Principles

1. **Capture while fresh.** The best time to document a solution is right after you solve the problem. Context fades fast.
2. **Structure for retrieval.** Knowledge that can't be found is the same as knowledge that doesn't exist. Use frontmatter, categories, and cross-references.
3. **Only Handle It Once.** If you solve a problem, document it so nobody (including future you) solves it again.
4. **Context > syntax.** The right context makes AI dramatically more effective. Invest in context docs — they compound.
5. **Evidence-grounded.** For domain knowledge (psychometrics, measurement), claims cite sources. No black boxes.

## Decision Trees

### Should I /compound This?

```
Did you just solve a non-trivial problem?
├─ Yes → Did it take >15 minutes or require investigation?
│  ├─ Yes → /compound — worth capturing
│  └─ No → Was it a gotcha that would trip someone up?
│     ├─ Yes → /compound — save others the pain
│     └─ No → Skip — too simple to be worth documenting
└─ No → Skip — nothing to compound
```

### Should I /compound a Context Doc?

```
Is there knowledge that AI needs repeatedly?
├─ Yes → Is it already in CLAUDE.md or a knowledge file?
│  ├─ Yes → /compound to update the existing doc
│  └─ No → /compound to create a structured context doc
└─ No → Skip — don't create docs for one-off use
```

### Which Psychometric Skill?

```
What's the question about?
├─ Single domain (IRT, reliability, scoring, etc.) → psychometric-advisor
├─ Item writing or design → item-designer
├─ Scoring change validation → scoring-reviewer
├─ Complex cross-domain question (3+ domains) → psychometry-expert agent
└─ Full instrument audit → assessment-auditor agent
```

## Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| [Compound](skills/compound/SKILL.md) | `/compound` | Capture knowledge — solutions, context docs, learnings, and principles |
| [Psychometric Advisor](skills/psychometric-advisor/SKILL.md) | `/psychometric-advisor` | Expert psychometric guidance across 9 domains (IRT, reliability, validity, scoring, etc.) |
| [Item Designer](skills/item-designer/SKILL.md) | `/item-designer` | 5-step guided workflow for creating assessment items |
| [Scoring Reviewer](skills/scoring-reviewer/SKILL.md) | `/scoring-reviewer` | Validate scoring changes against psychometric standards |

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| [Knowledge Architect](agents/knowledge-architect.md) | sonnet | Context engineering — builds and maintains structured knowledge docs |
| [Psychometry Expert](agents/psychometry-expert.md) | sonnet | Deep cross-domain psychometric analysis (3+ domains) |
| [Assessment Auditor](agents/assessment-auditor.md) | sonnet | Autonomous instrument review with structured audit report |
| [Skill Reviewer](agents/skill-reviewer.md) | sonnet | Grade skills and agents A-F against the toolkit's quality bar |

## Knowledge

| File | Topic |
|------|-------|
| [Context Engineering](knowledge/context-engineering.md) | How to build structured context for AI — types, versioning, the right granularity |
| [Compounding Patterns](knowledge/compounding-patterns.md) | Knowledge compounding patterns — solution libraries, cross-references, retrieval |
| [Psychometric References](knowledge/psychometric-references.md) | Master bibliography for psychometric domain files |

## Psychometric Domain

This plugin includes a complete psychometric knowledge base — 9 domain files covering IRT, reliability, validity, item design, scoring, AI assessment, statistics, I/O psychology, and ethics. All grounded in peer-reviewed research with 68+ citations.

The psychometric domain is housed here because psychometrics is **organized, expert knowledge** — exactly what Super Knowledge is about. The domain-specific skills (psychometric-advisor, item-designer, scoring-reviewer) need direct access to the 9 knowledge files they reference.

## Disclaimer

This plugin provides structured workflows for knowledge management and expert psychometric guidance based on published research. For high-stakes assessment decisions (hiring, certification, clinical diagnosis), verify psychometric recommendations with a qualified psychometrician.
