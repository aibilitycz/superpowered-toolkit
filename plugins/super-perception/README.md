# Super Perception

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-6366f1)](https://claude.com/claude-code)
[![Skills](https://img.shields.io/badge/Skills-1-green)]()
[![Agents](https://img.shields.io/badge/Agents-1-green)]()

A Claude Code plugin for discovery, brainstorming, and problem reframing — see what others miss before building.

1 skill. 1 agent. Look before you leap.

## What It Does

- **`/brainstorm`** — Collaborative discovery before planning. Explores the problem space, evaluates approaches, surfaces past work, and produces a structured brainstorm document that feeds directly into `/plan`. Explicitly questions the framing — "are we solving the right problem?"

## Install

Part of the [Superpowered Toolkit](https://github.com/aibilitycz/superpowered-toolkit) marketplace.

```bash
# Add the marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install this plugin
/plugin install super-perception@superpowered-toolkit
```

## Skills & Agents

| Component | Type | Purpose |
|-----------|------|---------|
| `brainstorm` | Skill | Collaborative discovery — explore the problem, evaluate approaches, make decisions |
| `researcher` | Agent | Deep research across codebase, docs, and past brainstorms |

## Methodology Anchor

- **Superpower:** Super Perception (SP Superpower 1)
- **Sub-competencies activated:** AI Curiosity (1.1), Opportunity Recognition (1.2), AI-Augmented Discovery (1.3), Problem Reframing (1.4)
- **How it activates them:** By questioning before building. `/brainstorm` doesn't jump to solutions — it explores the problem first. The researcher agent surfaces what you'd miss on your own.
- **Why this belongs:** Building the wrong thing fast is worse than building nothing. This plugin ensures you're solving the right problem.

See [METHODOLOGY.md](../../METHODOLOGY.md) for the full meta-framework.

## Disclaimer

This plugin provides structured brainstorming and discovery workflows. It surfaces options and tradeoffs but does not make decisions for you.

## License

MIT
