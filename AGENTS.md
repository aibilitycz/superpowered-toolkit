# Agents

12 specialized agents across 3 plugins. Agents run as subprocesses — they handle research, review, and analysis without polluting your main context window.

## Quick Reference

| Agent | Plugin | Purpose | Tools |
|-------|--------|---------|-------|
| researcher | super-perception | Codebase, docs, and solution scanning for discovery | Read, Grep, Glob |
| strategic-reviewer | super-intelligence | Focused code review with Critical Trust | Read, Grep, Glob |
| investigator | super-intelligence | Evidence-trail detective for root causes and bugs | Read, Grep, Glob |
| python-reviewer | super-intelligence | Python type safety, async, Pydantic, FastAPI patterns | Read, Grep, Glob |
| typescript-reviewer | super-intelligence | TypeScript narrowing, hooks, RTK Query, Drizzle patterns | Read, Grep, Glob |
| security-reviewer | super-intelligence | OWASP Top 10, auth, secrets, input validation, threat modeling | Read, Grep, Glob |
| infra-reviewer | super-intelligence | Terraform/OpenTofu, Helm, K8s, Dockerfiles, CI/CD | Read, Grep, Glob, Bash |
| performance-reviewer | super-intelligence | N+1 queries, complexity, memory, scaling, SLO compliance | Read, Grep, Glob |
| knowledge-architect | super-knowledge | Build and maintain structured knowledge docs (CLAUDE.md, guides) | Read, Grep, Glob |
| psychometry-expert | super-knowledge | Deep cross-domain psychometric analysis (3+ domains) | Read, Grep, Glob |
| assessment-auditor | super-knowledge | Autonomous instrument review (items, scoring, rubrics) | Read, Grep, Glob |
| skill-reviewer | super-knowledge | Grade skills/agents A-F against quality bar and CONVENTIONS.md | Read, Grep, Glob |

## By Plugin

### super-perception (1 agent)

**researcher** — Scans codebase, docs, past brainstorms, and solutions to surface context for brainstorming and discovery. Used internally by `/brainstorm` during Phase 2.

### super-intelligence (7 agents)

**strategic-reviewer** — One deep review instead of nine shallow ones. Analyzes quality, correctness, and convention adherence with Critical Trust.

**investigator** — Follows evidence trails using three lenses: Sherlock (deduction), Poirot (psychology/intent), Columbo (what's missing). Works on code, performance, architecture, data, and systems.

**python-reviewer** — Python-specialized review focusing on type safety, async correctness, Pydantic validation, SQLAlchemy session handling, and FastAPI patterns.

**typescript-reviewer** — TypeScript-specialized review focusing on type narrowing, hook dependencies, RTK Query cache invalidation, Effect-TS layers, and Drizzle patterns.

**security-reviewer** — Deep security review with OWASP Top 10, auth patterns, secret management, input validation, and adversarial threat modeling.

**infra-reviewer** — Infrastructure code review for Terraform/OpenTofu, Helm charts, Kubernetes manifests, Dockerfiles, and CI/CD pipelines. The only agent with Bash access for validation commands.

**performance-reviewer** — Performance-focused review analyzing N+1 queries, algorithmic complexity, memory usage, scaling projections, and SLO compliance.

### super-knowledge (4 agents)

**knowledge-architect** — Builds and maintains structured knowledge docs — CLAUDE.md files, knowledge bases, onboarding guides. Optimizes context that AI will consume repeatedly.

**psychometry-expert** — Deep multi-step psychometric analysis for questions spanning 3+ domains. Cross-domain reasoning, tradeoff evaluation, methodology decisions. Redirected to from `/psychometric-advisor` when a question is too broad.

**assessment-auditor** — Autonomous quality review of assessment instruments — item definitions, scoring config, rubric files (YAML/JSON/CSV). Produces structured report with severity-rated findings. Redirected to from `/psychometric-advisor` for audit requests.

**skill-reviewer** — Reviews SKILL.md and agent .md files against the toolkit's quality bar. Grades A-F based on methodology anchoring, safety mechanisms, and CONVENTIONS.md compliance.

### super-creation & super-integration

No agents. These plugins focus on execution (`/work`, `/audio`) and orchestration (`/orchestrate`) respectively.

## Usage

Agents are invoked automatically by skills or explicitly via the `Agent` tool:

```
# Automatic — /review uses strategic-reviewer internally
/review path/to/file.py

# Explicit — invoke an agent directly
Agent(subagent_type="python-reviewer", prompt="Review services/scoring-engine/")
Agent(subagent_type="investigator", prompt="Why is the scheduler skipping runs?")
```

All agents are read-only (except infra-reviewer which can run validation commands). They never modify code.
