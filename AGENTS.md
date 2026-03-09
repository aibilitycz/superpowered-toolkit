# Superpowered Toolkit

Plugin marketplace for Claude Code. 5 plugins — one per Superpowered Professional dimension — that replace generic AI workflows with methodology-grounded alternatives.

## Project Structure

```
superpowered-toolkit/
├── METHODOLOGY.md              # Meta-framework: layers, anchors, quality gates
├── CONVENTIONS.md              # Shared file naming, frontmatter, structure rules
├── CONTRIBUTING.md             # Quality gates for contributions
├── .claude-plugin/
│   └── marketplace.json        # Plugin registry for Claude Code marketplace
└── plugins/
    ├── super-perception/       # Discovery, brainstorming (/brainstorm)
    ├── super-intelligence/     # Planning, review, reasoning (/plan, /review, /think, /investigate)
    ├── super-knowledge/        # Knowledge capture, psychometrics (/compound, /psychometric-advisor, /item-designer, /scoring-reviewer)
    ├── super-creation/         # Execution, audio (/work, /audio)
    └── super-integration/      # Workflow orchestration (/orchestrate)
```

Each plugin follows the same layout:

```
plugins/<plugin-name>/
├── .claude-plugin/plugin.json   # Name, version, description, keywords
├── CLAUDE.md                    # Core principles, decision trees
├── skills/<name>/SKILL.md       # Executable workflow (one per skill)
├── agents/<name>.md             # Specialized subagents (read-only)
└── knowledge/<topic>.md         # Reference material loaded on demand
```

## Commands

| Command | Plugin | What It Does |
|---------|--------|-------------|
| `/brainstorm` | super-perception | Collaborative discovery — reframe problems, explore approaches, surface past work |
| `/plan` | super-intelligence | Auto-calibrated planning with dependency ordering and decision rationale |
| `/review` | super-intelligence | Focused code/document/architecture review with evidence-based findings |
| `/think` | super-intelligence | Deep reasoning — expert panels, devil's advocate, tradeoff analysis |
| `/investigate` | super-intelligence | Detective-style root cause analysis |
| `/compound` | super-knowledge | Capture solutions, context docs, and learnings for future reuse |
| `/psychometric-advisor` | super-knowledge | Expert guidance: IRT, reliability, validity, scoring, AI assessment (9 domains) |
| `/item-designer` | super-knowledge | Guided 5-step workflow for assessment item design |
| `/scoring-reviewer` | super-knowledge | Validate scoring changes against psychometric standards |
| `/work` | super-creation | Execute a plan from start to ship (tasks, tests, commits, quality checks) |
| `/audio` | super-creation | Generate audio — TTS, podcasts, voice cloning, sound effects |
| `/orchestrate` | super-integration | Detect workflow state and suggest next phase |

## Code Style and Conventions

- **Language:** Markdown with YAML frontmatter
- **File naming:** `kebab-case.md` everywhere
- **Output artifacts:** `YYYY-MM-DD-{kebab-topic}-{type}.md`
- **Evidence markers:** `[strong]`, `[moderate]`, `[emerging]`, `[consensus]` on recommendations
- **Source tags:** `[academic]`, `[standards]`, `[practitioner]` on citations
- **Knowledge files:** 800-1200 words, accessible voice, open with what/why then how then pitfalls
- **Skills:** Under 500 lines. Numbered phases with entry/exit criteria. Boundaries (MAY/MAY NOT) required.
- **Agents:** Read-only by default. Specify model and tool permissions in frontmatter.

See `CONVENTIONS.md` for the full specification.

## Key Design Principles

1. **Methodology anchor required.** Every plugin maps to SP superpowers and sub-competencies. No anchor = doesn't belong here.
2. **Evidence-grounded.** Factual claims cite sources. Psychometric content requires 5+ peer-reviewed citations per domain.
3. **Socratic challenge.** Skills question assumptions using Chain-of-Verification (CoVe), not personality-based pushback.
4. **Adaptive autonomy.** Skills detect interactive vs autonomous context. High confidence (>85%) = act. Low confidence (<50%) = escalate.
5. **Active memory.** Skills surface relevant past brainstorms, plans, and solutions at startup (max 3 artifacts).
6. **Fairness is non-negotiable.** Any plugin touching scoring, items, or decisions must address DIF/fairness.

## Testing and Validation

No automated test suite — plugins are markdown-based knowledge and workflow definitions. Quality is validated by:

- **Skill reviewer agent** (`super-knowledge`) — grades skills A-F against CONVENTIONS.md
- **Line count checks** — skills under 500 lines, CLAUDE.md under 120 lines, knowledge files 800-1200 words
- **Cross-reference validation** — all relative paths resolve to existing files
- **Manual testing** — run each skill against real scenarios and verify phase transitions, output format, and boundary adherence

## Git Workflow

- **Trunk-based development** — commit directly to `main`
- **Versioning:** SemVer in each plugin's `plugin.json`
- **Commit format:** `type: description` (feat, fix, docs, chore, refactor)

## Boundaries

- **Do** edit markdown files, update knowledge, improve skill workflows, add agents
- **Do not** add non-markdown code, build systems, or runtime dependencies — this is a pure knowledge/workflow toolkit
- **Do not** include proprietary methods or uncited claims
- **Do not** reference internal project paths — this is a public repository
