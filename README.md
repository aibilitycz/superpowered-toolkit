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

**Skill:** `/brainstorm` — Reframe problems, explore approaches, surface past work before building. Uses Socratic verification (CoVe) to challenge assumptions before accepting problem framing.

**Agent:** researcher — Scans codebase, docs, past brainstorms, and solutions to gather context.

**Knowledge:** discovery patterns

### [super-intelligence](plugins/super-intelligence/) — Strategic Thinking

**Skills:**
- `/plan` — Auto-calibrated planning (concise/standard/detailed based on scope). Surfaces past plans and adapts autonomy level to context.
- `/review` — Focused code, document, or architecture review with evidence-grounded challenge (CoVe verification on each finding)
- `/think` — Expert panel simulation, devil's advocate, adversarial verification with provisional confidence
- `/investigate` — Detective-style root cause analysis (Sherlock/Poirot/Columbo lenses). Consults past solutions before investigating.

**Agents:** strategic-reviewer, investigator, python-reviewer, typescript-reviewer, security-reviewer, infra-reviewer, performance-reviewer

**Knowledge:** decision frameworks, critical evaluation, strategic decomposition, socratic patterns, infrastructure ops, security review, Python/FastAPI patterns, TypeScript/Next.js patterns, observability

### [super-knowledge](plugins/super-knowledge/) — Knowledge & Measurement

**Skills:**
- `/compound` — Capture solutions, context docs, learnings, and principles. Intelligent dedup — checks for existing solutions before creating new ones.
- `/psychometric-advisor` — Expert guidance across 9 domains (IRT, reliability, validity, item design, scoring, AI assessment, statistics, I/O psychology, ethics)
- `/item-designer` — 5-step guided workflow for assessment items. Challenges format selection with psychometric tradeoffs.
- `/scoring-reviewer` — Validate scoring changes against psychometric standards. Technical checks run autonomously; fairness checks always escalate.

**Agents:** knowledge-architect, psychometry-expert, assessment-auditor, skill-reviewer

**Knowledge:** context engineering, compounding patterns, active memory integration, 68+ peer-reviewed psychometric citations

### [super-creation](plugins/super-creation/) — Execution

**Skills:**
- `/work` — Execute a plan from start to ship. Read tasks, implement, test, commit, quality checks, push. Defaults to autonomous mode when a plan file is provided.
- `/audio` — Generate audio content — text-to-speech, podcasts, voice cloning, sound effects, dubbing, and audio isolation (ElevenLabs).

**Knowledge:** the 90/10 craft (AI does 90%, you craft the 10% that matters), CI/CD patterns

### [super-integration](plugins/super-integration/) — Orchestration

**Skill:** `/orchestrate` — Detects where you are in the workflow, suggests the next phase, maintains flow between plugins. Memory-informed routing — surfaces existing brainstorms and plans.

**Knowledge:** workflow patterns (full loop, partial flows, transitions), autonomy modes (confidence-gated escalation)

## Not Every Task Needs the Full Loop

| Task | Flow |
|------|------|
| Quick bug fix | `/investigate` → `/work` |
| New feature | `/brainstorm` → `/plan` → `/work` → `/review` |
| Hard decision | `/think` |
| Code review | `/review` |
| Document a fix | `/compound` |
| Assessment question | `/psychometric-advisor` or `/item-designer` |
| Generate audio | `/audio` |
| Not sure where to start | `/orchestrate` |

## What Makes This Different

Skills aren't just prompts — they're structured workflows with:

- **Socratic challenge** — skills question assumptions using Chain-of-Verification (CoVe), not personality-based pushback
- **Adaptive autonomy** — skills detect interactive vs autonomous context and adjust (>85% confidence = act, <50% = escalate)
- **Active memory** — skills surface relevant past brainstorms, plans, and solutions at startup (max 3 artifacts, no context bloat)
- **Methodology anchor** — every plugin connects to SP superpowers and sub-competencies
- **Evidence-grounded** — claims cite sources with `[academic]`, `[standards]`, `[practitioner]` tags
- **Rationalizations tables** — common shortcuts documented with costs, so Claude avoids them
- **Entry/exit criteria** — every workflow phase has explicit gates
- **Confidence calibration** — skills declare when they're uncertain

See [METHODOLOGY.md](METHODOLOGY.md) for the meta-framework, [AGENTS.md](AGENTS.md) for the agent registry, and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Compatibility

**Claude Code** — full support. Plugins install via the marketplace and load automatically.

**Cursor / Windsurf / other AI editors** — not directly compatible. These tools use different configuration formats (`.cursorrules`, etc.). The knowledge files are plain markdown and can be referenced manually, but the structured skill workflows (phases, tool permissions, entry/exit criteria) are Claude Code-specific.

## Disclaimer

These tools provide guidance based on published research, not certification. For high-stakes assessment decisions (hiring, certification, clinical diagnosis), verify recommendations with a qualified professional.

## License

MIT
