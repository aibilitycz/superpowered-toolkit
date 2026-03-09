# Autonomy Modes

How skills decide when to act independently and when to involve the human. Not a binary switch — a confidence-gated spectrum. The goal: skills that proceed smoothly when context is clear, and escalate precisely when it matters.

---

## Mode Detection

Skills don't ask "am I in autonomous mode?" — they assess the context and calibrate.

### Detection Heuristics

| Signal | Suggests | Weight | Example |
|--------|----------|--------|---------|
| Plan file provided as input | Autonomous | High | `/work docs/plans/2026-03-09-feat-x-plan.md` |
| Running inside a workflow chain | Autonomous | High | `/plan` after `/brainstorm` produced a doc |
| User says "just do it" / "run it" / "go ahead" | Autonomous | High | Explicit instruction to proceed |
| Detailed prompt with specifics (>200 words) | Autonomous | Medium | Full context provided upfront |
| Prior brainstorm/plan exists for this topic | Autonomous | Medium | Decisions already made |
| Problem is ambiguous or has multiple valid approaches | Interactive | High | No clear winner among options |
| High-stakes domain (auth, scoring, data, money) | Interactive | High | Consequences of wrong decision are severe |
| No prior context exists for this topic | Interactive | High | Starting cold |
| User asks a question (not gives an instruction) | Interactive | Medium | "Should we..." vs "Do this" |

**Default when signals conflict:** Interactive. The cost of asking one extra question is low; the cost of a wrong autonomous decision can be high.

---

## Confidence-Gated Escalation

Every decision point has a confidence level. Use it to gate behavior:

```
> 85% confidence  → Execute. Log the decision briefly.
                    "Chose X because Y."

70-85% confidence → Execute. Flag for awareness.
                    "Note: I chose X over Y because Z. Worth a quick check."

50-70% confidence → Pause. Present options.
                    "I'm leaning toward X but Y is also viable. Key tradeoff: ..."

< 50% confidence  → Escalate. Ask directly.
                    "I don't have enough context to decide this. Specifically, I need..."
```

### What Makes Confidence High vs Low

| Raises Confidence | Lowers Confidence |
|-------------------|-------------------|
| Clear precedent in codebase (pattern exists) | No existing pattern to follow |
| Decision was made in a prior brainstorm/plan | Contradicts a prior decision |
| One approach is clearly better on all dimensions | Tradeoff between equally valid approaches |
| Low stakes (easily reversible) | High stakes (auth, data, scoring, money) |
| Strong evidence from docs, tests, or prior art | Uncertainty about requirements or constraints |

---

## Behavior by Mode

| Aspect | Interactive Mode | Autonomous Mode |
|--------|-----------------|-----------------|
| Questions | Socratic dialogue, one at a time | Decide using heuristics, log reasoning |
| Pushback | Active — challenge assumptions, use CoVe | Only on clear anti-patterns or contradictions |
| Progress updates | Conversational, check for alignment | Structured status at milestones |
| Decisions | Collaborate: present options, seek input | Decide: choose and document rationale |
| Escalation | Ask when genuinely uncertain | Only when confidence < 70% |
| Output style | Dialogue + final artifact | Artifact with appended decision log |

---

## Safety Rails

These override confidence gates — always escalate regardless of confidence:

### Always-Escalate Domains

- **Authentication/authorization** changes
- **Scoring formulas or weights** (psychometric validity at stake)
- **Data deletion or migration** (irreversible)
- **Financial/billing logic** (money)
- **User-facing copy** that changes meaning (not typos)
- **Security configuration** (CORS, CSP, secrets)

### The 3-Decision Gate

If autonomous mode produces 3+ significant decisions without human check-in, insert a brief summary:

```
Autonomous progress check:
1. [Decision 1] — chose X because Y
2. [Decision 2] — chose A because B
3. [Decision 3] — chose M because N

Continuing unless you want to adjust.
```

This prevents drift without constant interruption.

### Never-Skip Rules

Autonomous mode never skips:
- Quality checks (tests, linting)
- Security-sensitive validation
- Plan task completion tracking
- Commit discipline (one logical unit per commit)

---

## Decision Log Format

When running autonomously, append a decision log to the output so the human can review after the fact:

```markdown
## Autonomous Decisions

| # | Decision | Confidence | Rationale |
|---|----------|-----------|-----------|
| 1 | Used SSE over WebSocket | 90% | Existing pattern in 3 services, lower complexity |
| 2 | Added retry with backoff | 85% | Standard resilience pattern, no downside |
| 3 | Skipped feature flag | 75% | Small blast radius, easy rollback via revert |
```

This format lets the human scan decisions quickly and flag anything worth revisiting.

---

## Skill-Specific Application

Different skills have different autonomy profiles:

| Skill | Default Mode | Why |
|-------|-------------|-----|
| `/work` | Autonomous (when plan exists) | Plans are pre-approved decisions — execute, don't re-litigate |
| `/brainstorm` | Interactive | Discovery requires dialogue — autonomous brainstorming is just guessing |
| `/plan` | Autonomous if brainstorm exists, interactive if not | Brainstorm provides the decisions; without it, need to discover |
| `/review` | Autonomous | Reviews should be thorough regardless — present findings at the end |
| `/think` | Interactive | Deep reasoning benefits from human input at decision points |
| `/investigate` | Autonomous | Follow evidence chains without interruption — present the case at the end |
| `/compound` | Autonomous | Capture decisions are low-risk — document now, prune later |
| `/orchestrate` | Interactive | Routing decisions benefit from human intent confirmation |

---

## Anti-patterns

- **Binary autonomy.** "Full auto" or "ask everything" — both miss the point. Confidence-gated is the right granularity.
- **Asking permission for obvious actions.** "Should I read the file you just told me to review?" — friction without value.
- **Silent autonomy.** Making decisions without logging them. The human can't review what they can't see.
- **Overriding safety rails.** "I'm confident enough to skip the auth review" — no. Safety rails are not confidence-dependent.
- **Mode announcement.** Don't say "I'm now switching to autonomous mode." Just act appropriately. The user sees the behavior, not the mode label.
