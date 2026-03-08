# Discovery Patterns

How superpowered professionals discover — the patterns that separate good problem-solving from great problem-solving. Discovery isn't about finding answers. It's about finding the right questions.

---

## Problem Reframing

The highest-leverage discovery technique. Before solving, ask: "Is this the right problem?"

### The Reframing Test

When someone says "we need to build X," pause and ask:

1. **What problem does X solve?** Get the problem behind the solution.
2. **Who has this problem?** Real users, or assumed users?
3. **How are they solving it today?** The current workaround reveals the real need.
4. **What does success look like?** Not features — outcomes. What's true when this is done?

**Example:**
- **Request:** "We need a notification preferences page"
- **Reframe:** "Users are getting notifications they don't want. The problem is unwanted noise, not missing preferences. Maybe the solution is better default notifications, not more settings."

The reframe might lead to the same solution. Or it might lead to a simpler one. Either way, you understand the problem better.

### When to Reframe

- Always reframe at the start of a brainstorm. It takes 2 minutes and occasionally saves weeks.
- Especially reframe when the request is a solution ("build X") rather than a problem ("users can't do Y").
- Don't reframe simple, well-understood tasks. A bug fix doesn't need philosophical questioning.

---

## Lateral Exploration

Looking at a problem from unexpected angles. Most people explore vertically (deeper into the same approach). Superpowered professionals explore laterally (across approaches).

### The Three-Approach Rule

Before committing to an approach, generate at least three options:

1. **The obvious approach.** The first thing that comes to mind. Usually fine.
2. **The simple approach.** What's the minimum that would work? Often simpler than the obvious one.
3. **The surprising approach.** What if we did it completely differently? Challenge the assumptions.

**Example:**
- **Problem:** Users need real-time notifications
- **Obvious:** WebSocket server + notification service
- **Simple:** Email notifications (async, no new infrastructure)
- **Surprising:** SSE from existing API (no new service, one-way is sufficient)

The simple or surprising approach is often better than the obvious one. You don't know until you look.

### Constraint Flipping

Take a constraint and flip it. Ask "what if this constraint didn't exist?"

- "We need to support 10,000 concurrent users" → "What if we only needed to support 100?"
- "This has to be real-time" → "What if 5-minute delay was acceptable?"
- "We can't change the database schema" → "What if we could?"

The flipped constraint often reveals simpler solutions. Sometimes the constraint is real and you flip it back. Sometimes you discover it wasn't actually a hard constraint.

---

## Prior Art Research

Don't start from scratch. Most problems have been solved before — in your codebase, in your team's history, or in the wider ecosystem.

### Internal Prior Art

Your most valuable source. Solutions from your own codebase fit your conventions, architecture, and constraints.

**Where to look:**
- `docs/solutions/` — past problem/solution pairs
- `docs/brainstorms/` — past explorations of similar topics
- Codebase — grep for similar features, services, patterns
- ADRs — past architectural decisions that affect this area

### Team Prior Art

What has the team learned? Solutions in people's heads are useless if not captured.

**Surface it:**
- "Has anyone built something similar?" — Ask the team.
- Check git history for related changes — who touched this area last?
- Read past PR descriptions for context on why things were built a certain way.

### External Prior Art

How does the wider ecosystem solve this?

**When to look externally:**
- The problem is genuinely novel for your team
- You need to evaluate technology choices
- Best practices exist but aren't captured internally

**When NOT to look externally:**
- You have a working internal pattern (match it, don't replace it)
- The problem is well-understood and the approach is clear
- External research would delay more than it helps

---

## Signal Detection

Noticing what others miss. Not a mystical ability — a set of deliberate practices.

### Ask Why Three Times

When you encounter a decision, bug, or pattern, ask "why" three times to get past the surface:

1. "Why do we batch notifications?" → "Because individual sends are slow."
2. "Why are individual sends slow?" → "Because each send hits a rate-limited API."
3. "Why do we hit a rate-limited API?" → "Because we're using the legacy notification provider."

The third "why" often reveals the real problem — not what you'd fix by looking at the surface.

### Anomaly Awareness

Pay attention to things that seem off:
- Code that's more complex than expected — why?
- A workaround in production code — what caused it?
- A test that's been disabled — what broke?
- A TODO comment from 6 months ago — is it still relevant?

Anomalies are signals. They point to problems worth investigating or decisions worth understanding.

### The "What Could Go Wrong" Scan

Before committing to an approach, spend 5 minutes listing what could go wrong. Not exhaustive risk analysis — just the obvious failure modes.

This isn't pessimism. It's the part of discovery that prevents expensive surprises during implementation.

---

## Anti-patterns

- **Jumping to solutions.** "Let's use X" before understanding the problem. Solutions without problem understanding are guesses.
- **Analysis paralysis.** Researching forever instead of deciding. Set a timebox. When it expires, decide with what you know.
- **Ignoring prior art.** Building from scratch when a working pattern exists. Check before inventing.
- **Only vertical exploration.** Going deeper into the first approach without considering alternatives. The Three-Approach Rule prevents this.
- **Discovery without output.** Exploring without writing anything down. A brainstorm that isn't documented is a conversation that's forgotten.
