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

## Skill Design Patterns

Skills are executable specifications — not guidance documents. They tell Claude exactly what to do, when to ask, when to branch, and when to stop.

### Size and Structure

- **SKILL.md target: under 500 lines.** If longer, extract detail into `references/` or `workflows/` subdirectories.
- **One level deep only.** Files linked from SKILL.md do NOT chain to other files. Prevents reference degradation.
- **Progressive disclosure:** SKILL.md has the routing and phases. Reference files have the domain knowledge.

```
skills/<skill-name>/
├── SKILL.md              # Phases, routing, boundaries (under 500 lines)
├── references/           # Optional: domain knowledge, checklists
│   └── <topic>.md
└── workflows/            # Optional: detailed step-by-step for complex routes
    └── <route>.md
```

### Skill Boundaries

Every skill declares what it MAY and MAY NOT do. This is non-negotiable.

```markdown
## Boundaries

**This skill MAY:** research, discuss, write the brainstorm document
**This skill MAY NOT:** edit code, create files beyond the output artifact, run tests, deploy
```

For read-only skills, enforce with the `allowed-tools` frontmatter — don't list `Write`, `Edit`, or `Bash` if the skill shouldn't use them.

Hard boundary enforcement uses ALL CAPS prohibition:

```markdown
**NEVER write code during this skill. This is a discussion, not implementation.**
```

### Numbered Phases with Entry/Exit Criteria

Every phase has explicit gates. Unnumbered prose produces unreliable execution.

```markdown
### Phase 2: Research

**Entry:** Problem statement is clear (Phase 1 complete).

1. Launch researcher agent...
2. Surface findings...

**Exit:** Findings presented. User has seen what exists before exploring approaches.
```

### Claude Code Interaction Tools

Skills can use these Claude Code tools for rich user interaction:

| Tool | Purpose | Use When |
|------|---------|----------|
| **AskUserQuestion** | Structured choices with UI cards | Decision points, routing, comparisons |
| **TaskCreate/TaskUpdate** | Progress tracking with spinner, dependencies | `/work` — trackable task execution |
| **EnterPlanMode/ExitPlanMode** | Formal plan → approve → implement flow | When plan needs explicit user sign-off |

### AskUserQuestion (Structured)

Use at every decision point. This is a **structured JSON tool**, not prose — Claude Code renders it as interactive UI cards.

**API constraints:**
- 1-4 questions per call
- 2-4 options per question (an "Other" option is added automatically)
- `header`: max 12 characters (displayed as chip/tag)
- `label`: 1-5 words per option
- `description`: explains tradeoffs or what happens if chosen
- `preview`: optional — renders side-by-side comparison (code, mockups, diagrams)
- `multiSelect`: true when multiple answers are valid

**Single choice (routing):**
```markdown
Use **AskUserQuestion** with:
- question: "Brainstorm captured. What would you like to do next?"
- header: "Next step"
- options:
  1. label: "Proceed to plan", description: "Run /plan using this brainstorm as input"
  2. label: "Keep exploring", description: "More questions before committing to an approach"
  3. label: "Done for now", description: "Return later — path saved for /plan"
- multiSelect: false
```

**Multiple choice (priorities):**
```markdown
Use **AskUserQuestion** with:
- question: "Which areas should the plan cover?"
- header: "Scope"
- options:
  1. label: "Backend API", description: "New endpoints, data models, validation"
  2. label: "Frontend UI", description: "Components, state, user flows"
  3. label: "Infrastructure", description: "Deployment, config, monitoring"
  4. label: "Testing", description: "Unit, integration, E2E test plan"
- multiSelect: true
```

**With previews (comparing approaches):**
```markdown
Use **AskUserQuestion** with previews for side-by-side comparison:
- question: "Which approach do you prefer?"
- header: "Approach"
- options:
  1. label: "WebSockets", description: "Real-time bidirectional", preview: "Client ←→ Server\nPersistent connection\nLow latency\nMore complex"
  2. label: "SSE", description: "Server push only", preview: "Client ← Server\nHTTP-based\nSimpler\nOne-way only"
- multiSelect: false
```

**Recommended option:** Add "(Recommended)" to the label of the preferred option and list it first.

**Routing after selection:**
```markdown
**If user selects "Keep exploring":** Return to Phase 2 and continue.

**If user selects "Proceed to plan":** Suggest `/plan {path}`.
```

### Task Progress: TaskCreate/TaskUpdate

For `/work` and other execution skills, use TaskCreate to show progress with spinner UI:

```markdown
Use **TaskCreate** for each plan task:
- subject: "Add user authentication middleware"
- description: "Create Express middleware that validates JWT tokens..."
- activeForm: "Adding auth middleware"

When starting work: **TaskUpdate** status to "in_progress" (shows spinner).
When done: **TaskUpdate** status to "completed".
```

Tasks support dependencies (`addBlockedBy`, `addBlocks`) for ordered execution.

### Subagent Dispatch: Task()

Use explicit `Task()` syntax for subagent calls. Never describe agents vaguely — invoke them.

**Single agent:**
```markdown
Task researcher("Find existing patterns related to: <topic>.
Search docs/brainstorms/, docs/solutions/, and codebase.")
```

**Parallel agents:**
```markdown
Run these agents **in parallel**:

- Task researcher(feature_description)
- Task learnings-researcher(feature_description)
```

**Conditional agents:**
```markdown
**If the topic involves security, payments, or data privacy:**

- Task security-reviewer(context)
- Task best-practices-researcher(topic + "security")
```

### Wait Gates

When phases depend on subagent results, enforce synchronization:

```markdown
**WAIT for all Phase 1 agents to complete before proceeding.**

Collect results, then continue to Phase 2.
```

### Inter-Skill Loading

Skills can invoke other skills at transition points:

```markdown
Load the `document-review` skill and apply it to the brainstorm document.
```

Or route to a slash command:

```markdown
**If user selects "Start implementation":** Run `/work` with the plan path.
```

### Conditional Branching

Use explicit IF/THEN blocks — not prose that implies conditions.

**Content-based routing:**
```markdown
**If a relevant brainstorm exists:**
1. Read it
2. Extract decisions and open questions
3. Skip idea refinement — the brainstorm already answered WHAT

**If no brainstorm found:**
Run idea refinement (Phase 1.2).
```

**Detection-based routing:**
```markdown
**If PR contains database migrations or schema changes:**
- Task schema-drift-detector(PR content)
- Task data-migration-expert(PR content)
```

### Rationalizations Table

Every skill includes a table of shortcuts Claude might take and why they fail:

```markdown
## Common Rationalizations

| Shortcut | Why It Fails | The Cost |
|----------|-------------|----------|
| "Skip research — I know this" | Reinventing what exists | Wasted effort + inconsistency |
| "Keep exploring forever" | Diminishing returns after 2-3 options | Analysis paralysis |
```

For audit/review skills, this is mandatory. For creative skills, recommended.

### Degree of Freedom Calibration

Not every step needs equal prescription. Match freedom to task fragility:

| Fragility | Freedom | Skill Behavior |
|-----------|---------|----------------|
| **High** (scoring, security, destructive) | Low | "Run exactly this. No variations." |
| **Medium** (planning, configuration) | Medium | "Use this structure, customize content." |
| **Low** (brainstorming, exploration) | High | "Explore freely within these boundaries." |

A single skill can mix freedoms. Brainstorming has high freedom in exploration (Phase 2) but low freedom in document structure (Phase 4).

### Validate Checklist

Every skill ends with a verification step before delivering output:

```markdown
## Validate

Before delivering, verify:

- [ ] Problem was reframed, not accepted at face value
- [ ] At least 2 approaches explored with tradeoffs
- [ ] Every decision has rationale and rejected alternatives
- [ ] Open questions listed — nothing swept under the rug
```

### Workflow Patterns

Choose ONE structural pattern based on the skill's decision structure:

| Pattern | When to Use | Example |
|---------|------------|---------|
| **Linear progression** | Single path, no branching | `/compound` — always 1→2→3→done |
| **Routing** | Multiple independent workflows from shared intake | `/review` — routes to code vs document vs architecture |
| **Sequential pipeline** | Steps where output N feeds step N+1 | `/work` — research → implement → test → ship |
| **Safety gate** | Destructive or irreversible actions | Deployment skills — analyze fully BEFORE acting |
| **Dialogue loop** | Collaborative exploration with user | `/brainstorm` — ask → explore → ask → converge |

### Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| Vague phase descriptions ("research the topic") | Specific actions ("Launch researcher agent with these search paths") |
| Missing boundaries ("help the user") | Explicit MAY/MAY NOT declarations |
| Linear flow where branching is needed | Add AskUserQuestion at decision points |
| Monolithic SKILL.md (800+ lines) | Extract to references/ and workflows/ |
| Tools listed but not needed | Principle of least privilege — only list tools actually used |
| Phases without entry/exit criteria | Add **Entry:** and **Exit:** to every phase |
| Describing agents vaguely ("run a research agent") | Explicit `Task agent-name(params)` syntax |
| Skipping validation | Always end with Validate checklist |

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
8. Skills follow design patterns above (boundaries, phases, AskUserQuestion, Task() syntax)
9. Skills under 500 lines (detail extracted to references/workflows if needed)
