# Superpowered Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin_Marketplace-6366f1)](https://claude.com/claude-code)

5 AI-powered plugins for Claude Code — one per Superpowered Professional dimension. Replace generic development workflows with methodology-grounded alternatives.

```
/brainstorm → /plan → /work → /review → /compound
 Perception   Intelligence   Creation   Intelligence   Knowledge
```

## Install

```bash
# Add the marketplace (once)
/plugin marketplace add aibilitycz/superpowered-toolkit

# Install individual plugins
/plugin install super-perception@superpowered-toolkit
/plugin install super-intelligence@superpowered-toolkit
/plugin install super-knowledge@superpowered-toolkit
/plugin install super-creation@superpowered-toolkit
/plugin install super-integration@superpowered-toolkit
```

Install what you need. Each plugin works independently — `super-integration` ties them together but isn't required.

## Plugins

### [super-perception](plugins/super-perception/) — Discovery

**Skill:** `/brainstorm` — Reframe problems, explore approaches, surface past work before building.

**Agent:** researcher — Scans codebase, docs, past brainstorms, and solutions to gather context.

### [super-intelligence](plugins/super-intelligence/) — Strategic Thinking

**Skills:**
- `/plan` — Auto-calibrated planning (concise/standard/detailed based on scope)
- `/review` — Focused code, document, or architecture review with evidence-based findings
- `/think` — Expert panel simulation, devil's advocate, tradeoff analysis
- `/investigate` — Detective-style root cause analysis (Sherlock/Poirot/Columbo lenses)

**Agents:** strategic-reviewer, investigator, python-reviewer, typescript-reviewer, security-reviewer, infra-reviewer, performance-reviewer

**Knowledge:** decision frameworks, critical evaluation, strategic decomposition, infrastructure ops, security review, Python/FastAPI patterns, TypeScript/Next.js patterns, observability

### [super-knowledge](plugins/super-knowledge/) — Knowledge & Measurement

**Skills:**
- `/compound` — Capture solutions, context docs, learnings, and principles
- `/psychometric-advisor` — Expert guidance across 9 domains (IRT, reliability, validity, item design, scoring, AI assessment, statistics, I/O psychology, ethics)
- `/item-designer` — 5-step guided workflow for assessment items
- `/scoring-reviewer` — Validate scoring changes against psychometric standards

**Agents:** knowledge-architect, psychometry-expert, assessment-auditor, skill-reviewer

**Knowledge:** context engineering, compounding patterns, 68+ peer-reviewed psychometric citations

### [super-creation](plugins/super-creation/) — Execution

**Skill:** `/work` — Execute a plan from start to ship. Read tasks, implement, test, commit, quality checks, push.

**Knowledge:** the 90/10 craft (AI does 90%, you craft the 10% that matters), CI/CD patterns

### [super-integration](plugins/super-integration/) — Orchestration

**Skill:** `/orchestrate` — Detects where you are in the workflow, suggests the next phase, maintains flow between plugins.

**Knowledge:** workflow patterns (full loop, partial flows, transitions)

## Not Every Task Needs the Full Loop

| Task | Flow |
|------|------|
| Quick bug fix | `/investigate` → `/work` |
| New feature | `/brainstorm` → `/plan` → `/work` → `/review` |
| Hard decision | `/think` |
| Code review | `/review` |
| Document a fix | `/compound` |
| Not sure where to start | `/orchestrate` |

## Quality Standards

All plugins follow shared conventions ([CONVENTIONS.md](CONVENTIONS.md)):

- **Methodology anchor** — every plugin connects to SP superpowers and sub-competencies
- **Evidence-grounded** — claims cite sources with `[academic]`, `[standards]`, `[practitioner]` tags
- **Rationalizations tables** — common shortcuts documented with costs, so Claude avoids them
- **Entry/exit criteria** — every workflow phase has explicit gates
- **Confidence calibration** — skills declare when they're uncertain

See [METHODOLOGY.md](METHODOLOGY.md) for the meta-framework and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Disclaimer

These tools provide guidance based on published research, not certification. For high-stakes assessment decisions (hiring, certification, clinical diagnosis), verify recommendations with a qualified professional.

## License

MIT
