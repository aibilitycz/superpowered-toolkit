# Super Creation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-6366f1)](https://claude.com/claude-code)
[![Skills](https://img.shields.io/badge/Skills-2-green)]()
[![Agents](https://img.shields.io/badge/Agents-1-green)]()

A Claude Code plugin for executing plans, shipping features, and building at speed — AI does 90%, you craft the 10% that matters.

2 skills. 1 agent. Ship complete features, not perpetual WIPs.

## What It Does

- **`/work`** — Execute a plan. Read the tasks, implement them in dependency order, test continuously, commit incrementally. Uses the plan's checkboxes as the tracker — tick them off as you go.
- **`/ship`** — Finalize a feature. Run quality checks, generate release notes, push. The shipping checklist that ensures nothing gets forgotten.

## Install

Part of the [Superpowered Toolkit](https://github.com/aibilitycz/superpowered-toolkit) marketplace.

```bash
# Add the marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install this plugin
/plugin install super-creation@superpowered-toolkit
```

## Skills & Agents

| Component | Type | Purpose |
|-----------|------|---------|
| `work` | Skill | Execute plans with continuous testing and incremental commits |
| `ship` | Skill | Finalize features with quality checks and release notes |
| `builder` | Agent | Focused execution — implements tasks following existing patterns |

## Methodology Anchor

- **Superpower:** Super Creation (SP Superpower 4)
- **Sub-competencies activated:** Creative Courage (4.1), The 90/10 Craft (4.2), Building (4.3), Multi-Format Production (4.4)
- **How it activates them:** By rewarding shipping over perfecting. `/work` executes with continuous checkpoints. `/ship` generates multi-audience release notes. The workflow builds the muscle of finishing.
- **Why this belongs:** Ideas without execution are worthless. This plugin turns plans into shipped software.

See [METHODOLOGY.md](../../METHODOLOGY.md) for the full meta-framework.

## Disclaimer

This plugin provides structured execution workflows. It does not replace code review, testing, or human judgment about what to ship. Always verify AI-generated code before deploying to production.

## License

MIT
