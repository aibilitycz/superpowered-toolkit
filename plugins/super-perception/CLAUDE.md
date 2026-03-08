# Super Perception

Seeing where AI creates value — and the curiosity to look for it everywhere. This plugin embodies SP Superpower 1 — discovery, brainstorming, and problem reframing before committing to a solution.

## Methodology Anchor

- **Superpower:** Super Perception (SP Superpower 1)
- **Sub-competencies activated:**
  - **1.1 AI Curiosity** — Brainstorm encourages exploring multiple approaches before committing
  - **1.2 Opportunity Recognition** — Research surfaces related patterns, past solutions, prior art
  - **1.3 AI-Augmented Discovery** — Multi-source synthesis (codebase, docs, past brainstorms) creates new insights
  - **1.4 Problem Reframing** — Brainstorm explicitly asks "what problem are we actually solving?"
- **How it activates them:** `/brainstorm` doesn't jump to solutions — it questions the problem first. The researcher agent digs across sources to surface what you'd miss on your own. Using these tools builds the habit of looking before leaping.
- **Why this belongs:** Building the wrong thing fast is worse than building nothing. This plugin ensures you're solving the right problem before committing resources.

See `../../METHODOLOGY.md` for the four capability layers and methodology anchor rule.

## Core Principles

1. **Question the problem before solving it.** The biggest waste isn't slow execution — it's executing on the wrong thing.
2. **Explore before committing.** Consider 2-3 approaches, not just the first one that comes to mind.
3. **Surface what exists.** Check past brainstorms, solutions, and codebase patterns before assuming you're starting fresh.
4. **Make decisions explicit.** The brainstorm output captures what was decided and why — this feeds directly into `/plan`.
5. **Know when to stop.** Brainstorming has diminishing returns. When the approach is clear, move to planning.

## Decision Trees

### Do I Need to /brainstorm?

```
Is the problem clear and the approach obvious?
├─ Yes → Is it a pattern you've done before?
│  ├─ Yes → Skip brainstorm, go to /plan
│  └─ No → Quick brainstorm (15 min) to validate the approach
├─ No → Is there significant ambiguity or risk?
│  ├─ Yes → Full brainstorm — explore approaches, resolve questions
│  └─ No → Quick brainstorm — clarify the problem, pick an approach
└─ Not sure → Start a brainstorm — it'll become clear quickly
```

### When to Stop Brainstorming

```
Has the brainstorm answered these?
├─ What problem are we solving? → Yes/No
├─ What approach are we taking? → Yes/No
├─ What alternatives did we consider? → Yes/No
├─ What's explicitly out of scope? → Yes/No
└─ All yes → Stop brainstorming, move to /plan
   Any no → Keep exploring that question
```

## Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| [Brainstorm](skills/brainstorm/SKILL.md) | `/brainstorm` | Collaborative discovery — explore the problem, evaluate approaches, make decisions |

## Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| [Researcher](agents/researcher.md) | sonnet | Deep research across codebase, docs, and past brainstorms |

## Knowledge

| File | Topic |
|------|-------|
| [Discovery Patterns](knowledge/discovery-patterns.md) | How superpowered professionals discover — problem reframing, lateral thinking, exploration techniques |

## Disclaimer

This plugin provides structured brainstorming and discovery workflows. It surfaces options and tradeoffs but does not make decisions for you. Use the output as input to planning and decision-making, not as a final answer.
