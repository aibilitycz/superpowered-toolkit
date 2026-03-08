# Superpowered Toolkit Conventions

Shared conventions for all plugins in the toolkit. Follow these when creating or updating any plugin.

---

## Directory Structure

Every plugin lives under `plugins/<plugin-name>/` and follows this layout:

```
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json           # Required: name, version, description, keywords
├── CLAUDE.md                 # Required: core principles, decision trees, methodology anchor
├── README.md                 # Required: install guide, what it does, methodology anchor, disclaimer
├── skills/
│   └── <skill-name>/
│       └── SKILL.md          # One SKILL.md per skill (Claude Code auto-discovers)
├── agents/
│   └── <agent-name>.md       # One .md per agent (Claude Code auto-discovers)
├── knowledge/
│   └── <topic>.md            # Reference material loaded by skills/agents
└── examples/
    └── <scenario>.md         # Usage walkthroughs demonstrating the plugin
```

**Optional directories:** Only create `knowledge/` and `examples/` if the plugin has content for them. Don't create empty directories.

---

## File Naming

| Type | Convention | Example |
|------|-----------|---------|
| Plugin directory | `kebab-case` | `super-intelligence` |
| Skill directory | `kebab-case`, matches the slash command | `plan/`, `document-review/` |
| Agent file | `kebab-case.md` | `strategic-reviewer.md` |
| Knowledge file | `kebab-case.md`, descriptive topic name | `decision-frameworks.md` |
| Example file | `kebab-case.md`, describes the scenario | `plan-complex-feature.md` |

---

## YAML Frontmatter

### Skills (`SKILL.md`)

```yaml
---
name: skill-name
description: >
  One-paragraph description. Include trigger keywords for Claude Code
  auto-discovery. Be specific about when this skill activates.
allowed-tools:
  - Read
  - Grep
  - Glob
---
```

**Required fields:** `name`, `description`, `allowed-tools`

### Agents (`<agent-name>.md`)

```yaml
---
name: agent-name
description: >
  One-paragraph description. Include when to use this agent and what
  it's good at.
model: sonnet
tools: Read, Grep, Glob
---
```

**Required fields:** `name`, `description`, `model`, `tools`

### plugin.json

```json
{
  "name": "plugin-name",
  "version": "0.1.0",
  "description": "One sentence. What it does, not how.",
  "author": {
    "name": "aibility",
    "url": "https://github.com/aibilitycz"
  },
  "homepage": "https://github.com/aibilitycz/superpowered-toolkit/tree/main/plugins/<name>",
  "repository": "https://github.com/aibilitycz/superpowered-toolkit",
  "license": "MIT",
  "keywords": ["relevant", "keywords"]
}
```

---

## Output Artifacts

Skills produce artifacts in the consuming project (the repo where the toolkit is installed). These are the **default paths and naming conventions**. Projects can override them in their `CLAUDE.md`.

### Default Paths

| Artifact | Default Path | Produced By |
|----------|-------------|-------------|
| Brainstorms | `docs/brainstorms/` | `/brainstorm` |
| Plans | `docs/plans/` | `/plan` |
| Solutions | `docs/solutions/` | `/compound` |
| Runbooks | `docs/operators/runbooks/` | `/work` (when creating ops docs) |
| ADRs | `architecture/decisions/` | `/plan`, `/think` |
| Handoffs | `docs/handoffs/` | `/orchestrate` |

### File Naming

All output artifacts follow the same pattern:

```
YYYY-MM-DD-{kebab-topic}-{type}.md
```

Examples:
- `2026-03-08-scoring-trust-audit-explainability-brainstorm.md`
- `2026-03-04-feat-l1-triplet-choice-assessment-plan.md`
- `2026-02-20-sse-auth-token-refresh.md` (solutions omit the `-solution` suffix)

### YAML Frontmatter (Output Artifacts)

Every artifact file must include frontmatter:

```yaml
---
title: "Human-readable title"
type: brainstorm | plan | solution | runbook | adr | handoff
date: YYYY-MM-DD
status: draft | approved | in_progress | complete | shipped  # plans only
participants: [who was involved]
related:
  - docs/brainstorms/YYYY-MM-DD-related-topic.md
  - https://github.com/org/repo/issues/123
---
```

**Required fields:** `title`, `type`, `date`
**Optional fields:** `status`, `participants`, `related`, `tags`

### Overriding Defaults

Projects override output paths in their `CLAUDE.md`:

```markdown
## Toolkit Output Paths

| Artifact | Path |
|----------|------|
| Brainstorms | `design/brainstorms/` |
| Plans | `design/plans/` |
| Solutions | `knowledge/solutions/` |
```

Skills check the project's `CLAUDE.md` for a "Toolkit Output Paths" table before using defaults. If the table exists, its paths take precedence.

---

## Cross-References

- **Between plugins:** Use relative paths from the plugin root: `../../METHODOLOGY.md`, `../psychometric-ai-toolkit/CLAUDE.md`
- **Within a plugin:** Use paths relative to the file: `../knowledge/decision-frameworks.md`, `skills/plan/SKILL.md`
- **To SP methodology:** Link to the GitHub repo: `https://github.com/aibilitycz/superpowered-professional/tree/main/methodology`

---

## Methodology Anchor

Every plugin must declare a methodology anchor in both `CLAUDE.md` and `README.md`:

```markdown
## Methodology Anchor

- **Superpower:** [Which superpower this plugin embodies]
- **Sub-competencies activated:** [List the specific sub-competencies]
- **How it activates them:** [Not by lecturing — by modeling the behavior]
- **Why this belongs:** [One sentence connecting plugin to methodology]
```

See `METHODOLOGY.md` for the anchor rule and capability layers.

---

## Knowledge Files

- **Word count:** 800-1200 words
- **Voice:** Accessible, not academic. Written for practitioners, not researchers.
- **Structure:** Open with what and why, then how, then pitfalls/anti-patterns
- **Evidence markers:** Use `[strong]`, `[moderate]`, `[emerging]`, `[consensus]` on recommendations where evidence base matters
- **Citations:** Required for factual claims in MEASURE-layer plugins. Recommended but not required for other layers.

---

## Quality Gates (All Plugins)

Before shipping any plugin:

1. Methodology anchor declared in CLAUDE.md and README.md
2. All skills have complete YAML frontmatter
3. All agents specify model and scope boundaries
4. README includes disclaimer appropriate to the plugin's domain
5. Plugin registered in root `marketplace.json`
6. No references to internal projects (public repo)
7. Works without configuration (out of the box)
