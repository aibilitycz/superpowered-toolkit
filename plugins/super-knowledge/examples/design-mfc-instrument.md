# Example: Design a Multi-dimensional Forced Choice (MFC) Instrument

## Scenario

You're building a 12-block MFC instrument to measure 4 leadership competencies for a development (not selection) context.

## How to Use

Ask Claude:

> "Help me design a 12-block MFC instrument measuring Strategic Thinking, People Leadership, Execution Excellence, and Communication. It's for leadership development, not hiring."

## What Happens

1. Claude activates the `item-designer` skill
2. Walks through 5 steps:
   - **Step 1:** Clarifies each competency's behavioral indicators
   - **Step 2:** Confirms MFC format (appropriate for personality/behavioral constructs)
   - **Step 3:** Drafts 12 blocks, each with 3-4 statements from different dimensions
   - **Step 4:** Checks social desirability matching, reading level, dimensional coverage
   - **Step 5:** Review summary with pass/fail per quality check

## Key Decisions the Skill Will Guide

- **Block size:** Pairs (2 statements) vs triplets (3) vs quads (4)
- **Social desirability matching:** Are all options within a block equally attractive?
- **Dimensional balance:** Each dimension appears in ≥3 blocks (minimum for reliability)
- **TIRT compatibility:** Block structure supports Thurstonian IRT scoring
- **Faking resistance:** In a development context, MFC is beneficial but not strictly required — skill will note this
