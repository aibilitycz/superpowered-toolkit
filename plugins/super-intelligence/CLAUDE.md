# Super Intelligence

Better thinking and smarter decisions through symbiosis with AI. This plugin embodies SP Superpower 2 — strategic planning, critical evaluation, and deliberate decision-making.

## Methodology Anchor

- **Superpower:** Super Intelligence (SP Superpower 2)
- **Sub-competencies activated:**
  - **2.1 Critical Trust** — Review evaluates with evidence, flags uncertainty, never fakes confidence
  - **2.2 Prompt Mastery** — Plan produces precise specifications that serve as well-structured prompts for execution
  - **2.3 Task Decomposition** — Plan breaks complex work into dependency-ordered, right-sized steps
  - **2.4 Strategic AI Dialogue** — Plan and review use multi-step reasoning, not one-shot analysis
- **How it activates them:** Not by explaining — by modeling. The way `/plan` decomposes work IS Task Decomposition. The way `/review` flags uncertainty IS Critical Trust. Using the tools builds the skill.
- **Why this belongs:** You cannot be superpowered without thinking well. This plugin is the foundation for every other workflow.

See `../../METHODOLOGY.md` for the four capability layers and methodology anchor rule.

## Core Principles

1. **Think before doing.** Planning is not overhead — it's the highest-leverage activity. A 30-minute plan saves days of wrong-direction work.
2. **One deep pass > many shallow ones.** One reviewer that reads carefully beats nine that skim. Quality of attention matters more than quantity of agents.
3. **Decisions need reasons.** "What" without "why" is a todo list, not a plan. Every decision should capture the reasoning, not just the conclusion.
4. **Uncertainty is signal.** Saying "I don't know" is more valuable than guessing. Flag what's uncertain and what would resolve it.
5. **Simple until proven otherwise.** Start with the simplest approach. Add complexity only when you have evidence it's needed.

## Interaction Principles

- **Challenge with evidence.** Use CoVe and past-decision referencing, not persona prompts. See `knowledge/socratic-patterns.md`.
- **Adapt autonomy to context.** Confidence-gated escalation: >85% act, 50-70% ask, <50% escalate. See `../super-integration/knowledge/autonomy-modes.md`.
- **Consult memory.** Search past plans, reviews, and solutions before starting. See `../super-knowledge/knowledge/active-memory-integration.md`.

## Decision Trees

### How Much Detail in a Plan?

```
Is the scope clear and bounded?
├─ Yes → Can one person build it in a day?
│  ├─ Yes → CONCISE plan (problem, approach, tasks, acceptance criteria)
│  └─ No → Is it multi-repo or multi-team?
│     ├─ Yes → DETAILED plan (+ alternatives, risks, phased implementation)
│     └─ No → STANDARD plan (+ decision rationale, key risks)
└─ No → Ask 2-3 clarifying questions first, then re-evaluate
```

### When to Review Code

```
Did you change code?
├─ Yes → Is it a trivial change (typo, config, formatting)?
│  ├─ Yes → Skip review
│  └─ No → Does it touch auth, scoring, data, or money?
│     ├─ Yes → Full /review (mandatory)
│     └─ No → Quick self-check, /review if unsure
└─ No → No review needed
```

### When to Review a Document

```
Is this document going to drive implementation?
├─ Yes → /review the document before starting work
│  └─ Are there open questions or unclear scope?
│     ├─ Yes → Resolve before proceeding
│     └─ No → Ready for /work
└─ No → Read it, but formal review is optional
```

### When to /think

```
Is this a hard decision with multiple valid options?
├─ Yes → Are the stakes high (hard to reverse, expensive if wrong)?
│  ├─ Yes → /think — full analysis
│  └─ No → Quick mental evaluation, then decide
└─ No → Just decide and move
```

## Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| [Plan](skills/plan/SKILL.md) | `/plan` | Strategic planning with auto-calibrated detail, decision rationale, dependency ordering |
| [Review](skills/review/SKILL.md) | `/review` | Focused review of code, documents, or architecture — auto-detects scope, one deep pass |
| [Think](skills/think/SKILL.md) | `/think` | Deep reasoning — expert panels, devil's advocate, what-if scenarios, tradeoff analysis |
| [Investigate](skills/investigate/SKILL.md) | `/investigate` | Detective-style investigation — follows evidence trails with Sherlock/Poirot/Columbo lenses |

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| [Strategic Reviewer](agents/strategic-reviewer.md) | sonnet | Focused code review with Critical Trust — reads deeply, evaluates with evidence, flags uncertainty |
| [Investigator](agents/investigator.md) | sonnet | Detective agent — follows evidence trails across code, performance, architecture, data, systems |
| [Python Reviewer](agents/python-reviewer.md) | sonnet | Python-specialized review — async, Pydantic, SQLAlchemy, FastAPI patterns |
| [TypeScript Reviewer](agents/typescript-reviewer.md) | sonnet | TypeScript-specialized review — types, hooks, RTK Query, Next.js, Effect-TS |
| [Security Reviewer](agents/security-reviewer.md) | sonnet | Deep security review — OWASP, auth, secrets, adversarial threat modeling |
| [Infra Reviewer](agents/infra-reviewer.md) | sonnet | Infrastructure review — Terraform, Helm, K8s, Docker, CI/CD |
| [Performance Reviewer](agents/performance-reviewer.md) | sonnet | Performance review — N+1 queries, complexity, memory, scaling |

## Knowledge

| File | Topic |
|------|-------|
| [Decision Frameworks](knowledge/decision-frameworks.md) | How superpowered professionals make decisions — stakes matrix, tradeoff evaluation, when to ask for help |
| [Critical Evaluation](knowledge/critical-evaluation.md) | Evidence-based evaluation, uncertainty as information, priority triage |
| [Strategic Decomposition](knowledge/strategic-decomposition.md) | Breaking complex work into steps — top-down decomposition, dependency ordering, the 90/10 split |
| [Infrastructure Ops](knowledge/infrastructure-ops.md) | Terraform/Helm/K8s validation pipelines, debugging patterns, Dockerfile best practices |
| [Security Review](knowledge/security-review.md) | OWASP Top 10, auth patterns, secret management, input validation, adversarial modeling |
| [Python & FastAPI](knowledge/python-fastapi-patterns.md) | FastAPI, Pydantic, SQLAlchemy async, type hints, async/await correctness |
| [TypeScript & Next.js](knowledge/typescript-nextjs-patterns.md) | Next.js 15, React 19, RTK Query, Effect-TS, Drizzle ORM, strict TypeScript |
| [Observability](knowledge/observability.md) | PromQL, LogQL, Grafana dashboards, alerting rules, SLO/SLI patterns |
| [Socratic Patterns](knowledge/socratic-patterns.md) | Evidence-based challenging — CoVe technique, question templates, calibration |

## Disclaimer

This plugin provides structured workflows for planning, review, and evaluation. It improves the quality of AI-assisted thinking but does not replace domain expertise or professional judgment. Critical decisions should involve qualified humans.
