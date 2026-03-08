# Super Integration

Designing AI systems and workflows where AI and humans work together. This plugin embodies SP Superpower 5 — workflow orchestration, cross-plugin coordination, and the full brainstorm-to-compound lifecycle.

## Methodology Anchor

- **Superpower:** Super Integration (SP Superpower 5)
- **Sub-competencies activated:**
  - **5.1 Augmentation Vision** — Orchestrate shows how human + AI collaboration works across the full workflow
  - **5.2 Workflow Orchestration** — Conducts the cross-plugin flow: brainstorm → plan → work → review → compound
  - **5.3 Process Decomposition** — Breaks complex projects into plugin-appropriate phases
  - **5.4 Collaboration Design** — Cross-plugin conventions enable team collaboration on shared artifacts
- **How it activates them:** `/orchestrate` isn't another planning tool — it's the conductor that routes work through the right superpowers at the right time. Using it builds the skill of seeing workflows as systems, not sequences of tasks.
- **Why this belongs:** Individual superpowers are powerful. Combined superpowers are transformative. This plugin makes the whole greater than the sum.

See `../../METHODOLOGY.md` for the four capability layers and methodology anchor rule.

## Core Principles

1. **The right tool at the right time.** Each phase of work has a superpower that fits. Orchestrate routes to the right one.
2. **Artifacts flow forward.** A brainstorm feeds into a plan. A plan feeds into work. A review feeds into compound. Nothing is lost between phases.
3. **Conventions enable flow.** Shared file naming, frontmatter, and directory structure mean plugins can find each other's outputs without configuration.
4. **Humans decide transitions.** Orchestrate suggests the next phase but never auto-advances. The human decides when to move forward.
5. **The full loop compounds.** When the loop completes (brainstorm → compound), the knowledge captured makes the next loop faster and better.

## Decision Trees

### Which Superpower Next?

```
Where are you in the workflow?
├─ Starting fresh, unclear what to build → /brainstorm (Super Perception)
├─ Know what to build, need a plan → /plan (Super Intelligence)
├─ Have a plan, ready to execute → /work (Super Creation)
├─ Code written, need review → /review (Super Intelligence)
├─ Review done, ready to ship → /work handles shipping too (Super Creation)
├─ Just solved a hard problem → /compound (Super Knowledge)
├─ Need to evaluate a document → /review auto-detects documents (Super Intelligence)
├─ Hard decision with multiple options → /think (Super Intelligence)
├─ Something is broken, need root cause → /investigate (Super Intelligence)
└─ Not sure → /orchestrate (this plugin) — it'll figure it out
```

### Full Flow or Partial?

```
Is this a significant feature (multi-day, multi-repo)?
├─ Yes → Full flow: brainstorm → plan → work → review → ship → compound
│  └─ /orchestrate will guide you through each phase
├─ No → Is it a bug fix or small task?
│  ├─ Yes → Partial flow: /work → /review (skip brainstorm and plan)
│  └─ No → Medium task: /plan → /work → /review
└─ Just exploring → /brainstorm only — decide next step after
```

## Skills

| Skill | Command | Purpose |
|-------|---------|---------|
| [Orchestrate](skills/orchestrate/SKILL.md) | `/orchestrate` | Conduct the full cross-plugin workflow — detect current phase, suggest next steps, maintain flow |

## Knowledge

| File | Topic |
|------|-------|
| [Workflow Patterns](knowledge/workflow-patterns.md) | How superpowered workflows connect — the full loop, partial flows, transitions |

## Disclaimer

This plugin orchestrates workflows across other superpower plugins. It requires the other plugins to be installed for full functionality. It provides workflow guidance but does not make decisions about when to transition between phases — that's your call.
