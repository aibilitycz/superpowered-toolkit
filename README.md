# Superpowered Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin_Marketplace-6366f1)](https://claude.com/claude-code)

AI-powered assessment expertise for Claude Code, Cursor, and beyond. Skills, agents, and knowledge grounded in peer-reviewed research.

## Install

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install a plugin
/plugin install psychometric-ai-toolkit@superpowered-toolkit
```

### Cursor

Cursor support is planned. Skills use the same SKILL.md format and work in both environments.

## Plugins

### [psychometric-ai-toolkit](plugins/psychometric-ai-toolkit/)

Expert-level psychometric guidance for building AI-powered assessments.

- **9 knowledge domains** — IRT, reliability, validity, item design, scoring, AI assessment, statistics, I/O psychology, ethics
- **3 skills** — psychometric-advisor (router + 9 domain files), item-designer (5-step workflow), scoring-reviewer (10-point checklist)
- **2 agents** — psychometry-expert (cross-domain analysis), assessment-auditor (instrument review)
- **68+ citations** — all grounded in peer-reviewed research with evidence strength markers

Two modes: **Reference** ("What is...") for neutral explanations, **Advisory** ("Should I...") for opinionated recommendations.

## Disclaimer

These tools provide guidance based on published research, not certification. For high-stakes assessment decisions (hiring, certification, clinical diagnosis), verify recommendations with a qualified professional.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for quality gates and contribution guidelines.

## License

MIT
