---
name: item-designer
description: >
  Guided 5-step workflow for designing psychometrically sound assessment items.
  Use when the user wants to create new items, write assessment questions, design
  forced-choice blocks, build Likert scales, or create situational judgment scenarios.
  Triggers: write items, create items, design items, new assessment items, MFC blocks,
  Likert scale, SJT scenarios, item writing, assessment design.
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Item Designer

Guided workflow for creating psychometrically sound assessment items. Walks through 5 steps from construct definition to quality review.

## Prerequisites

Before starting, read these domain files for reference:
- `skills/psychometric-advisor/item-design.md` — item format principles and anti-patterns
- `skills/psychometric-advisor/io-psychology.md` — competency modeling context (if workplace assessment)

## Workflow

### Step 1: Construct Definition

Ask the user to define what they're measuring:

- **Dimension:** What broad trait or competency? (e.g., "Strategic Thinking")
- **Sub-competency:** What specific facet? (e.g., "Pattern Recognition in Ambiguous Data")
- **Behavioral indicators:** What does this look like in practice? (2-3 observable behaviors)
- **Target population:** Who takes this assessment? (role level, industry, language)
- **Stakes:** How will scores be used? (selection, development, research)

If the user is vague, push back: "I need specific behavioral indicators to write good items. 'Leadership' is too broad — which aspect of leadership?"

### Step 2: Format Selection

Use this decision tree based on Step 1 answers:

```
Is faking a concern? (high-stakes selection, promotion)
├─ Yes → Is the construct personality/behavioral?
│  ├─ Yes → MFC (forced-choice blocks)
│  │  └─ How many dimensions? ≥3 → TIRT-compatible MFC (pairs or triplets)
│  └─ No (knowledge/ability) → MC with distractor analysis
├─ No → Is the response continuous (degree of agreement)?
│  ├─ Yes → Likert scale (5 or 7 points)
│  └─ No → Is it about judgment in context?
│     ├─ Yes → SJT (situational judgment test)
│     └─ No → Consider AI-scored open-ended response
```

Present the recommendation with rationale. If the user disagrees, note the tradeoffs but follow their choice.

### Design Challenge

Before accepting the format choice, surface the key tradeoff for the user's context:
- "MFC resists faking but reduces reliability for small n. Is that acceptable for your population size?"
- "Likert is simpler to develop but vulnerable to response style bias. How high-stakes is this assessment?"
- Check past items in the project for format consistency — flag if the new item diverges from established patterns.
- In autonomous mode: make format selection using the decision tree above, log the rationale.

### Step 3: Item Drafting

Write items following format-specific principles:

**MFC (Forced-Choice) Items:**
- Frame as micro-scenarios: "When facing a tight deadline, I tend to..."
- Match social desirability within each block (all options equally attractive)
- Each option in a block measures a different dimension
- Use behavioral frequency language, not trait adjectives
- Minimum 3 blocks per dimension for reliability

**Likert Items:**
- Use behavioral frequency anchors (Never / Rarely / Sometimes / Often / Always)
- Or agreement anchors (Strongly Disagree → Strongly Agree) for attitude constructs
- Include reverse-scored items (≥20% of total)
- Avoid double-barreled items ("I am creative and innovative")
- Avoid absolutes ("I always..." / "I never...")

**SJT Items:**
- Present realistic workplace dilemmas with 4 response options
- Options should range from highly effective to counterproductive
- Avoid obviously correct or absurd options
- Base scenarios on critical incidents from job analysis

**AI-Scored Open-Ended:**
- Provide clear behavioral prompt ("Describe a time when...")
- Define rubric dimensions and anchor levels before writing prompts
- Ensure prompt elicits observable behaviors, not self-assessment

### Step 4: Quality Checks

Run each drafted item through this checklist:

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | Social desirability balance | Within MFC blocks: options equally attractive. Across Likert: mix of positive/negative keying |
| 2 | Reading level | Appropriate for target population (Flesch-Kincaid or similar) |
| 3 | No double-barreled items | Each item measures exactly one thing |
| 4 | No leading/loaded language | Neutral framing, no value judgments embedded |
| 5 | Behavioral anchors distinct | Each anchor level represents observably different behavior |
| 6 | Dimensional coverage | Item set covers all specified sub-competencies |
| 7 | Cultural sensitivity | No idioms, references, or scenarios that disadvantage specific groups |
| 8 | Construct alignment | Item content maps to stated behavioral indicators from Step 1 |

### Step 5: Review Summary

Present results as:

```markdown
## Item Design Review

### Items Created
- Format: [MFC / Likert / SJT / Open-ended]
- Count: [N items]
- Dimensions covered: [list]

### Quality Check Results
| Check | Status | Notes |
|-------|--------|-------|
| Social desirability | PASS/FAIL | [details] |
| Reading level | PASS/FAIL | [details] |
| ... | ... | ... |

### Items Needing Revision
- Item [ID]: [specific issue and suggested fix]

### Recommendations
- [Any structural suggestions for the item set as a whole]
```

## Anti-patterns

- **Don't write items without Step 1.** Skipping construct definition produces items that look good but don't measure anything specific.
- **Don't default to Likert.** It's the easy choice, not always the right one.
- **Don't ignore social desirability matching in MFC.** Unmatched blocks are trivially fakeable.
- **Don't write more items than needed.** More items ≠ better measurement if they're redundant.
