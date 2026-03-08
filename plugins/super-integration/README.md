# Super Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-6366f1)](https://claude.com/claude-code)
[![Skills](https://img.shields.io/badge/Skills-1-green)]()

A Claude Code plugin for cross-plugin workflow orchestration — the conductor that routes work through the right superpowers at the right time.

1 skill. The whole is greater than the sum.

## What It Does

- **`/orchestrate`** — Conduct the full cross-plugin workflow. Detects where you are (brainstorming? planning? coding? reviewing?), suggests the next phase, and maintains artifact flow between plugins. The lifecycle: brainstorm → plan → work → review → ship → compound.

## Install

Part of the [Superpowered Toolkit](https://github.com/aibilitycz/superpowered-toolkit) marketplace.

```bash
# Add the marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install this plugin
/plugin install super-integration@superpowered-toolkit
```

**Note:** For full functionality, install the other superpower plugins too. Super Integration orchestrates the flow between them.

## Skills & Agents

| Component | Type | Purpose |
|-----------|------|---------|
| `orchestrate` | Skill | Cross-plugin workflow conductor — detect phase, suggest next steps, maintain flow |

## The Full Loop

```
/brainstorm (Super Perception)
    ↓ writes brainstorm doc
/plan (Super Intelligence)
    ↓ reads brainstorm, writes plan
/work (Super Creation)
    ↓ reads plan, executes, commits
/review (Super Intelligence)
    ↓ reads changes, produces review
/compound (Super Knowledge)
    ↓ captures solution for future use
```

## Methodology Anchor

- **Superpower:** Super Integration (SP Superpower 5)
- **Sub-competencies activated:** Augmentation Vision (5.1), Workflow Orchestration (5.2), Process Decomposition (5.3), Collaboration Design (5.4)
- **How it activates them:** By making the connections visible. `/orchestrate` shows how each superpower feeds the next — that systems-level view IS augmentation vision.
- **Why this belongs:** Individual superpowers are powerful. Combined superpowers are transformative.

See [METHODOLOGY.md](../../METHODOLOGY.md) for the full meta-framework.

## Disclaimer

This plugin orchestrates workflows across other superpower plugins. It requires other superpower plugins for full functionality. It provides guidance but does not auto-advance between phases — transitions are your decision.

## License

MIT
