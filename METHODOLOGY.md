# Superpowered Toolkit Methodology

This document defines how every plugin in the Superpowered Toolkit connects to the Superpowered Professional (SP) methodology. It is the meta-framework that governs what belongs here and how plugins relate to each other.

---

## The SP Methodology (Source of Truth)

The Superpowered Professional methodology measures AI readiness across:

- **5 Superpowers** — Perception, Intelligence, Knowledge, Creation, Integration
- **20 Sub-competencies** — 4 per superpower (1 mindset, 1 skill, 2 additional)
- **4 Score Components** — Mindset (35%), Skills (30%), Domain (25%), Technical (10%)
- **6 Archetypes** — Derived from top 2 superpowers
- **2 Assessment Layers** — L1 (structured items, deterministic scoring) + L2 (behavioral observation, LLM-scored)

Full methodology: [superpowered-professional/methodology/](https://github.com/aibilitycz/superpowered-professional/tree/main/methodology)

---

## The Four Capability Layers

Every plugin serves one of four layers. A plugin may serve multiple layers but must have a primary.

| Layer | Question It Answers | Scope |
|-------|-------------------|-------|
| **MEASURE** | How do we assess the superpowers? | Psychometrics, IRT, scoring, calibration, item analysis |
| **DEVELOP** | How do we grow the superpowers? | Coaching paths, learning recommendations, gap analysis |
| **BUILD** | How do we build systems that deliver? | Assessment engines, item banks, config patterns, pipelines |
| **GOVERN** | How do we do it responsibly? | Ethics, fairness, compliance, methodology decisions |

```
               ┌─────────────┐
               │   GOVERN    │  Ethics, fairness, methodology rules
               └──────┬──────┘
                      │
    ┌─────────┬───────┴───────┬─────────┐
    │         │               │         │
┌───┴───┐ ┌──┴────┐   ┌──────┴──┐ ┌────┴────┐
│MEASURE│ │DEVELOP│   │  BUILD  │ │ (future)│
│       │ │       │   │         │ │         │
└───┬───┘ └───┬───┘   └────┬────┘ └─────────┘
    │         │            │
    └─────────┴────────────┘
              │
    ┌─────────┴──────────┐
    │  SP Methodology    │
    │  5 Superpowers     │
    │  20 Sub-competencies│
    └────────────────────┘
```

---

## The Methodology Anchor Rule

**Every plugin must have a Methodology Anchor** — a direct line to one or more superpowers, sub-competencies, or methodology components.

A plugin without a methodology anchor does not belong in this toolkit.

### How to Define an Anchor

Each plugin's `plugin.json` or `README.md` must declare:

```markdown
## Methodology Anchor

- **Layer:** MEASURE
- **Superpowers served:** All 5 (measurement science is cross-cutting)
- **Methodology components:** L1 scoring, L2 scoring, item calibration, reliability, validity
- **Why this belongs:** You cannot assess the 5 superpowers without psychometrically sound measurement.
```

### Anchor Examples

| Plugin | Primary Layer | Anchor | Rationale |
|--------|--------------|--------|-----------|
| `super-perception` | BUILD | Superpower 1: AI Curiosity, Opportunity Recognition, Discovery, Problem Reframing | Discovery and brainstorming before building |
| `super-intelligence` | BUILD | Superpower 2: Critical Trust, Prompt Mastery, Task Decomposition, Strategic AI Dialogue | Strategic thinking is the foundation for every workflow |
| `super-knowledge` | MEASURE + BUILD | Superpower 3: Iterative Learning, Knowledge Architecture, Context Engineering, Knowledge Compounding | Knowledge capture, context engineering, psychometric expertise |
| `super-creation` | BUILD | Superpower 4: Creative Courage, The 90/10 Craft, Building, Multi-Format Production | Execution and shipping |
| `super-integration` | BUILD | Superpower 5: Augmentation Vision, Workflow Orchestration, Process Decomposition, Collaboration Design | Cross-plugin workflow orchestration |
| `sp-methodology` (planned) | GOVERN | Score components, archetypes, P1-P8 decisions | Defines the rules that plugins implement |
| `assessment-builder` (future) | BUILD | L1+L2 pipeline, item bank | Implements the assessment flow from 08-assessment-design |
| `coaching-advisor` (future) | DEVELOP | 20 sub-competencies | Maps gaps to growth paths per sub-competency |
| `calibration-ops` (future) | MEASURE | Item parameters, DIF, drift | Monitors measurement quality in production |

---

## Plugin Quality Standards

### Universal (All Plugins)

1. **Methodology anchor declared** in README
2. **Evidence-grounded** — claims cite sources with type tags: `[academic]`, `[standards]`, `[practitioner]`
3. **Evidence strength marked** on recommendations: `[strong]`, `[moderate]`, `[emerging]`, `[consensus]`
4. **Fairness considered** — every plugin that touches scoring, items, or decisions must address DIF/fairness
5. **Disclaimer present** — no plugin replaces qualified professional judgment for high-stakes decisions

### Per Layer

| Layer | Additional Requirements |
|-------|----------------------|
| MEASURE | Min 5 citations per domain file. Decision trees for method selection. Anti-patterns documented. |
| DEVELOP | Growth recommendations linked to specific sub-competencies. Behavioral level indicators referenced. |
| BUILD | Config patterns match production assessment architecture. Code examples use real schemas. |
| GOVERN | References SP methodology docs directly. Conflict resolution rules documented (SP-specific overrides generic). |

---

## Conflict Resolution

When a plugin's generic recommendation conflicts with an SP-specific decision:

1. **SP methodology wins** for Aimee/SP implementations — the methodology was designed for this context
2. **Generic recommendation applies** for non-SP use cases — other teams using the toolkit are not bound by SP decisions
3. **Document the divergence** — note where SP chose differently and why

Example: The psychometric toolkit recommends equal weights as the default composite method. SP uses 35/30/25/10 weights with documented justification (mindset predicts growth better than current knowledge). Both are valid — the SP weights are theoretically justified per the methodology, not arbitrary.

---

## Creating a New Plugin

1. **Start with the methodology.** Which superpowers does this serve? Which layer?
2. **Check for overlap.** Does an existing plugin already cover this? Extend it instead.
3. **Define the anchor.** Write the methodology anchor section before writing any content.
4. **Follow the structure:**
   ```
   plugins/your-plugin/
   ├── .claude-plugin/
   │   └── plugin.json       # name, version, description, keywords
   ├── CLAUDE.md              # Core principles, quick decision trees
   ├── README.md              # What, why, install, methodology anchor
   ├── skills/                # SKILL.md files (Claude Code auto-discovers)
   ├── agents/                # Agent .md files (Claude Code auto-discovers)
   └── examples/              # Usage walkthroughs
   ```
5. **Meet quality gates** from CONTRIBUTING.md before merging.
6. **Register in marketplace.json** with version and description.

---

## Roadmap

| Phase | Plugin | Layer | Status |
|-------|--------|-------|--------|
| v0.2 | `psychometric-ai-toolkit` | MEASURE | Absorbed into `super-knowledge` |
| v0.3 | 5 superpower plugins | BUILD | Shipped — perception, intelligence, knowledge, creation, integration |
| v0.4 | `sp-methodology` | GOVERN | Planned — move from aimee-product |
| v0.5 | Cursor converter | — | Planned — multi-environment support |
| v1.0 | Official Anthropic marketplace submission | — | After v0.3 |
| Future | `assessment-builder` | BUILD | Assessment config patterns |
| Future | `coaching-advisor` | DEVELOP | Growth paths per sub-competency |
| Future | `calibration-ops` | MEASURE | Production monitoring |
