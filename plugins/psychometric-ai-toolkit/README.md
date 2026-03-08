# Psychometric AI Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-6366f1)](https://claude.com/claude-code)
[![Domains](https://img.shields.io/badge/Domains-9-green)]()
[![Citations](https://img.shields.io/badge/Citations-68+-orange)]()

A Claude Code plugin that provides expert-level psychometric, psychological, and statistical expertise for building AI-powered assessments.

9 knowledge domains. 3 skills. 2 agents. All grounded in peer-reviewed research.

## What It Does

Adds a psychometric expert to your Claude Code workflow:

- **Ask questions** about IRT models, reliability, validity, scoring, item design — get evidence-based answers with citations
- **Design items** with a guided 5-step workflow (construct → format → draft → check → review)
- **Validate scoring changes** against a 10-point psychometric checklist
- **Audit instruments** autonomously with severity-rated findings

Two modes:
- **Reference mode** ("What is...") — neutral explanations with all options
- **Advisory mode** ("Should I...") — opinionated recommendations with evidence strength

## Install

Part of the [Superpowered Toolkit](https://github.com/aibilitycz/superpowered-toolkit) marketplace.

```bash
# Add the marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install this plugin
/plugin install psychometric-ai-toolkit@superpowered-toolkit
```

## Domains

| Domain | What It Covers |
|--------|---------------|
| **IRT** | CTT, Rasch, 1PL–3PL, TIRT, GRM, model selection, item parameters |
| **Reliability** | Alpha, omega, test-retest, inter-rater, ICC, thresholds by stakes |
| **Validity** | Construct, criterion, content validity, DIF, fairness |
| **Item Design** | MFC, Likert, SJT, social desirability, faking resistance |
| **Scoring** | Normative, ipsative, composite, weights, floor/ceiling |
| **AI Assessment** | LLM-as-judge, calibration, ensemble scoring, hybrid L1+L2 |
| **Statistics** | Factor analysis, SEM, sample size, effect sizes, model fit |
| **I/O Psychology** | Competency modeling, job analysis, adverse impact, selection |
| **Ethics** | APA Standards, ITC Guidelines, fairness, AI ethics, consent |

## Skills & Agents

| Component | Type | Purpose |
|-----------|------|---------|
| `psychometric-advisor` | Skill | Routes queries to the right domain knowledge, detects reference vs advisory mode |
| `item-designer` | Skill | 5-step guided workflow for creating assessment items |
| `scoring-reviewer` | Skill | Validates scoring changes against 10-point psychometric checklist |
| `psychometry-expert` | Agent | Deep analysis for complex questions spanning 3+ domains |
| `assessment-auditor` | Agent | Autonomous instrument review with structured audit report |

## Examples

See `examples/` for walkthroughs:

- **Review a scoring change** — "I changed the weights, is this valid?"
- **Design an MFC instrument** — "Design a 12-block forced-choice instrument"
- **Validate an LLM scorer** — "My LLM scorer has low inter-rater agreement"

## Disclaimer

This toolkit provides guidance based on published psychometric research, not certification. For high-stakes assessment decisions (hiring, certification, clinical diagnosis), verify recommendations with a qualified psychometrician.

## License

MIT
