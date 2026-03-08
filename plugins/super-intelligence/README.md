# Super Intelligence

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-6366f1)](https://claude.com/claude-code)
[![Skills](https://img.shields.io/badge/Skills-3-green)]()
[![Agents](https://img.shields.io/badge/Agents-1-green)]()

A Claude Code plugin for strategic planning, focused code review, and critical evaluation — grounded in the Super Intelligence superpower.

3 skills. 1 agent. 3 knowledge files. Better thinking, not more process.

## What It Does

Replaces bloated planning and review workflows with focused, superpowered alternatives:

- **`/plan`** — Strategic planning that auto-calibrates to your problem. Simple feature? Concise plan. Complex multi-repo work? Detailed plan with alternatives, risks, and phased implementation. Always includes decision rationale — WHY, not just WHAT.
- **`/review`** — One focused code review instead of nine shallow ones. Evidence-based findings, explicit uncertainty, clear verdict.
- **`/document-review`** — Evaluate brainstorms, plans, and specs before starting work. Checks for decision rationale, risk awareness, and actionability.

## Install

Part of the [Superpowered Toolkit](https://github.com/aibilitycz/superpowered-toolkit) marketplace.

```bash
# Add the marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install this plugin
/plugin install super-intelligence@superpowered-toolkit
```

## Skills & Agents

| Component | Type | Purpose |
|-----------|------|---------|
| `plan` | Skill | Strategic planning with auto-calibrated detail, dependency ordering, and past solution surfacing |
| `review` | Skill | Focused code review — one deep pass with severity-rated findings and verdict |
| `document-review` | Skill | Structured evaluation of brainstorms, plans, and specs against Critical Trust criteria |
| `strategic-reviewer` | Agent | The review engine — reads deeply, evaluates with evidence, flags uncertainty |

## Knowledge

| File | What It Covers |
|------|---------------|
| **Decision Frameworks** | Stakes matrix, tradeoff evaluation, the "good enough" threshold, when to ask for help |
| **Critical Evaluation** | Evidence-based evaluation, uncertainty as information, priority triage, intent over ideal |
| **Strategic Decomposition** | Top-down decomposition, dependency ordering, the 90/10 split, scope boundaries |

## Examples

See `examples/` for walkthroughs:

- **Plan a complex feature** — multi-repo feature with brainstorm context, detailed plan output
- **Review a scoring change** — focused review of a sensitive code change with evidence-based findings

## Methodology Anchor

- **Superpower:** Super Intelligence (SP Superpower 2)
- **Sub-competencies activated:** Critical Trust (2.1), Prompt Mastery (2.2), Task Decomposition (2.3), Strategic AI Dialogue (2.4)
- **How it activates them:** By modeling, not lecturing. The way `/plan` decomposes work IS Task Decomposition. The way `/review` flags uncertainty IS Critical Trust.
- **Why this belongs:** Strategic thinking is the foundation. You cannot be superpowered without thinking well.

See [METHODOLOGY.md](../../METHODOLOGY.md) for the full meta-framework.

## Disclaimer

This plugin provides structured workflows for planning, review, and evaluation. It improves the quality of AI-assisted thinking but does not replace domain expertise or professional judgment. Critical decisions should involve qualified humans.

## License

MIT
