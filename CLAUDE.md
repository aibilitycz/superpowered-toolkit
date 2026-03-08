# Superpowered Toolkit

Plugin marketplace for the Superpowered Professional methodology. Every plugin here is derived from and anchored to the SP methodology's 5 Superpowers, 20 sub-competencies, and assessment framework.

## Architecture

```
superpowered-toolkit/
├── METHODOLOGY.md              # Meta-framework: layers, anchors, quality gates
├── .claude-plugin/
│   └── marketplace.json        # Plugin registry for Claude Code
├── plugins/
│   ├── psychometric-ai-toolkit/  # MEASURE layer — assessment science
│   └── [future plugins]
└── CONTRIBUTING.md             # Quality gates for contributions
```

**Read `METHODOLOGY.md` first** — it defines the four capability layers (MEASURE, DEVELOP, BUILD, GOVERN), the methodology anchor rule, and plugin quality standards.

## Key Rules

1. **Every plugin has a methodology anchor.** No anchor = doesn't belong here. See METHODOLOGY.md.
2. **Evidence-grounded.** All claims cite sources tagged `[academic]`, `[standards]`, or `[practitioner]`.
3. **Evidence strength on recommendations.** `[strong]`, `[moderate]`, `[emerging]`, `[consensus]`.
4. **SP-specific overrides generic.** When SP methodology conflicts with a plugin's generic recommendation, SP wins for Aimee implementations. Generic applies elsewhere.
5. **Fairness is non-negotiable.** Any plugin touching scoring, items, or decisions must address DIF/fairness.

## Plugins

| Plugin | Layer | Version | What It Does |
|--------|-------|---------|-------------|
| [psychometric-ai-toolkit](plugins/psychometric-ai-toolkit/) | MEASURE | 0.2.0 | 9 domain knowledge files, 3 skills, 2 agents for psychometric assessment science |

## Install

```bash
# Add marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install a plugin
/plugin install psychometric-ai-toolkit@superpowered-toolkit
```

## SP Methodology Reference

The source of truth is the [superpowered-professional](https://github.com/aibilitycz/superpowered-professional) repo:

- **5 Superpowers:** Perception, Intelligence, Knowledge, Creation, Integration
- **20 Sub-competencies:** 4 per superpower (1 mindset, 1 skill, 2 additional)
- **Score Components:** Mindset 35%, Skills 30%, Domain 25%, Technical 10%
- **Assessment Layers:** L1 (structured, deterministic) + L2 (behavioral, LLM-scored)
- **6 Archetypes:** Derived from top 2 superpowers
