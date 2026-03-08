# The 90/10 Craft

AI does 90% of the heavy lifting. You craft the 10% that makes it excellent. This isn't about laziness — it's about focusing your expertise where it matters most.

---

## The Principle

When building software with AI, the work splits naturally:

**The 90% (AI handles):**
- Writing boilerplate code
- Implementing known patterns
- Generating test scaffolding
- Producing documentation drafts
- Creating initial implementations of well-understood features

**The 10% (you craft):**
- Architecture decisions — which patterns to use, how services connect
- Edge case identification — what the AI didn't think of
- Naming — good names communicate intent, bad names create confusion
- Test design — what to test, what the important paths are
- Code review — verifying the AI got it right, catching logic errors
- Integration design — how this piece fits the larger system

The 10% is where your expertise, judgment, and understanding of the business context matter. It's the difference between code that works and code that's right.

---

## How to Focus on the 10%

### Before AI Writes Code

Your highest-leverage moment is before the AI starts writing. The context you provide determines the quality of the 90%.

**Invest time in:**
- Clear task descriptions — "Add a payment endpoint that validates Apple Pay tokens, charges via Stripe, and updates the order status" beats "implement payments"
- Pattern references — "Follow the pattern in `services/auth/handler.ts`" prevents the AI from inventing a new pattern
- Constraint specification — "Must use the existing `AppError` class for error handling" prevents convention violations

**The paradox:** Spending 5 minutes on context saves 30 minutes fixing AI output. The 10% starts before the 90%.

### While AI Writes Code

Monitor, don't micromanage. Let the AI complete a logical unit, then review.

**Watch for:**
- Pattern violations — is it matching the codebase conventions?
- Missing edge cases — what happens with null input, empty arrays, concurrent requests?
- Naming quality — are names descriptive and consistent?
- Over-engineering — is the AI adding abstractions nobody asked for?

### After AI Writes Code

This is where the craft happens. The AI produced something functional. Your job is to make it right.

**Your review checklist:**
1. **Does it match existing patterns?** The AI might have invented a new pattern. Redirect to the existing one.
2. **Are the names good?** AI-generated names are often verbose or generic. Rename for clarity.
3. **Are edge cases handled?** Add the cases the AI missed.
4. **Is it simple enough?** Remove unnecessary abstractions, unused parameters, premature generalizations.
5. **Are the tests testing the right things?** AI tests often test implementation details instead of behavior. Fix the test design.

---

## The Craft of Naming

Names are the most common 10% item. AI produces functional names. You produce meaningful ones.

| AI Name | Crafted Name | Why |
|---------|-------------|-----|
| `processUserPaymentTransaction` | `chargeOrder` | Concise, matches domain language |
| `handleError` | `mapToApiError` | Describes what it actually does |
| `getData` | `fetchActiveAssessments` | Specific about what data and from where |
| `utils/helpers.ts` | `lib/scoring.ts` | Domain-specific, not a junk drawer |

**Rule:** If you have to read the implementation to understand what a function does, the name is wrong.

---

## The Craft of Test Design

AI writes tests that cover lines. You design tests that cover behavior.

**AI's default test:**
```
test("createUser returns user") — tests that the function runs without crashing
```

**Crafted test:**
```
test("createUser with valid input returns user with hashed password")
test("createUser with duplicate email returns EmailAlreadyExistsError")
test("createUser with empty password returns ValidationError")
```

The crafted tests describe behavior. Each test name is a specification. The test suite becomes documentation.

**What to focus on:**
- Happy path + the 2-3 most likely failure modes
- Boundary cases (empty input, max length, zero, negative)
- Integration points (what happens when the database is down, when the API returns 500)
- Business rules (the logic that's specific to your domain)

---

## When the 90/10 Split Shifts

Not all tasks are 90/10. Some tasks need more human involvement:

| Task | AI % | Human % | Why |
|------|------|---------|-----|
| Boilerplate CRUD | 95% | 5% | Well-understood pattern |
| New API endpoint | 85% | 15% | Need to design the contract |
| Complex business logic | 70% | 30% | Domain knowledge is critical |
| Security-sensitive code | 60% | 40% | Verification is more important |
| Architecture decisions | 20% | 80% | AI can propose, human must decide |
| Debugging production issues | 50% | 50% | AI helps investigate, human connects the dots |

**Recognize the shift.** When a task needs more human attention, slow down. Don't treat a security feature like boilerplate CRUD.

---

## Anti-patterns

- **The 100/0 split.** Accepting all AI output without review. The 10% exists because AI makes mistakes that matter. Always review.
- **The 0/100 split.** Writing everything by hand. If AI can produce a correct implementation of a known pattern, let it. Your time is better spent on the 10%.
- **Polishing the 90%.** Spending time reformatting AI-generated code that's correct and follows conventions. If it works and matches patterns, move on.
- **Neglecting the 10%.** Skipping test design, accepting bad names, ignoring edge cases. The 10% is where quality lives.
- **One-shot prompting.** Giving AI a vague instruction and hoping for the best. Invest in context — it's the highest-ROI activity.
