# Superpowered Toolkit

Plugin marketplace for the Superpowered Professional methodology. 5 superpower plugins — one per SP dimension — that replace generic workflows with superpowered alternatives.

## Architecture

```
superpowered-toolkit/
├── METHODOLOGY.md              # Meta-framework: layers, anchors, quality gates
├── CONVENTIONS.md              # Shared file naming, frontmatter, structure
├── .claude-plugin/
│   └── marketplace.json        # Plugin registry for Claude Code
├── plugins/
│   ├── super-perception/       # Superpower 1 — discovery, brainstorming
│   ├── super-intelligence/     # Superpower 2 — planning, review, evaluation
│   ├── super-knowledge/        # Superpower 3 — compounding, context, psychometrics
│   ├── super-creation/         # Superpower 4 — execution, shipping
│   └── super-integration/      # Superpower 5 — orchestration, workflow
└── CONTRIBUTING.md             # Quality gates for contributions
```

**Read `METHODOLOGY.md` first** — it defines the methodology anchor rule and plugin quality standards.
**Read `CONVENTIONS.md`** — shared conventions for file naming, frontmatter, and cross-references.

## Key Rules

1. **Every plugin has a methodology anchor.** No anchor = doesn't belong here. See METHODOLOGY.md.
2. **Evidence-grounded.** Claims cite sources where applicable (especially MEASURE-layer content).
3. **Evidence strength on recommendations.** `[strong]`, `[moderate]`, `[emerging]`, `[consensus]`.
4. **SP-specific overrides generic.** When SP methodology conflicts with a plugin's generic recommendation, SP wins for SP implementations. Generic applies elsewhere.
5. **Fairness is non-negotiable.** Any plugin touching scoring, items, or decisions must address DIF/fairness.

## Plugins

| Plugin | Superpower | Version | What It Does |
|--------|-----------|---------|-------------|
| [super-perception](plugins/super-perception/) | 1. Perception | 0.1.0 | `/brainstorm` — discovery, problem reframing, research |
| [super-intelligence](plugins/super-intelligence/) | 2. Intelligence | 0.1.0 | `/plan`, `/review`, `/document-review` — planning, code review, evaluation |
| [super-knowledge](plugins/super-knowledge/) | 3. Knowledge | 0.1.0 | `/compound`, `/context` + psychometric domain (9 domains, 5 skills, 3 agents) |
| [super-creation](plugins/super-creation/) | 4. Creation | 0.1.0 | `/work`, `/ship` — execution, quality checks, release notes |
| [super-integration](plugins/super-integration/) | 5. Integration | 0.1.0 | `/orchestrate` — cross-plugin workflow conductor |

## The Full Loop

```
/brainstorm (Perception) → /plan (Intelligence) → /work (Creation) → /review (Intelligence) → /ship (Creation) → /compound (Knowledge)
```

Not every task needs the full loop. Match the flow to the task size and risk.

## Install

```bash
# Add marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install individual plugins
/plugin install super-perception@superpowered-toolkit
/plugin install super-intelligence@superpowered-toolkit
/plugin install super-knowledge@superpowered-toolkit
/plugin install super-creation@superpowered-toolkit
/plugin install super-integration@superpowered-toolkit
```

## SP Methodology Reference

The source of truth is the [superpowered-professional](https://github.com/aibilitycz/superpowered-professional) repo:

- **5 Superpowers:** Perception, Intelligence, Knowledge, Creation, Integration
- **20 Sub-competencies:** 4 per superpower (1 mindset, 1 skill, 2 additional)
- **Score Components:** Mindset 35%, Skills 30%, Domain 25%, Technical 10%
- **Assessment Layers:** L1 (structured, deterministic) + L2 (behavioral, LLM-scored)
- **6 Archetypes:** Derived from top 2 superpowers
