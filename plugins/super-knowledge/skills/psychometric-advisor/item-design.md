# Item Design

Principles, formats, and anti-patterns for writing psychometrically sound assessment items. Primary reference for the `item-designer` skill and domain 4 of `psychometric-advisor`.

---

## Item Formats

### Multi-dimensional Forced Choice (MFC)

MFC presents a block of statements and forces a ranking or selection (most/least like me). Each statement targets a different dimension, so faking one dimension distorts another. [strong]

**Block construction:**
- Blocks contain 2-5 statements; triplets are the most common TIRT-compatible format [Brown2011] [academic].
- Each statement in a block must measure a **different** dimension. Never place two items from the same dimension in one block.
- Every dimension must appear across multiple blocks (minimum 3) for estimation precision [Stark2005] [academic].
- Match statement length and complexity within blocks to prevent position bias.

**Social desirability matching:**
- All statements within a block must be matched on social desirability [Stark2005] [academic]. This is the single most important rule of MFC design.
- Pre-rate desirability with an independent sample or use published norms. Do not rely on author judgment. [moderate]
- Desirability mismatch turns forced-choice into transparent choice, eliminating faking resistance.

**TIRT scoring compatibility:**
- Thurstonian IRT models rankings as pairwise comparisons [Brown2011] [academic].
- Each dimension pair must appear together in at least 1-2 blocks. Use a balanced incomplete block design.
- Binary outcomes (most/least) yield one comparison per pair; full rankings yield C(n,2) per block.
- Plan the design matrix (which dimensions co-occur) before writing items.

### Likert Scales

Graded agreement or frequency scales. Well-understood but vulnerable to response styles. [consensus]

**Optimal number of points:**
- **5 points** -- sufficient for most personality and attitude measures, lower cognitive load [Krosnick1999] [academic]. Preferred for lower literacy populations or mobile-first delivery.
- **7 points** -- finer discrimination, slightly higher reliability. Gain beyond 7 is negligible [Krosnick1999] [academic]. [moderate]
- **Even-numbered** (4/6) -- removes midpoint, forcing directional response. Use only when neutral is meaningless.
- Default to 5 unless requirements demand 7. Never exceed 7 for self-report personality.

**Anchor wording:**
- Fully labeled scales (every point) improve reliability and cross-cultural comparability [Krosnick1999] [academic].
- Behavioral frequency anchors (Never / Rarely / Sometimes / Often / Always) for behavioral items.
- Agreement anchors (Strongly Disagree to Strongly Agree) for attitudes and beliefs.
- Do not mix anchor types within the same instrument.

**Reverse scoring:**
- Include at least 20% reverse-scored items to detect acquiescence bias [Paulhus1991] [academic].
- Write **conceptual opposites**, not grammatical negations. "I avoid social gatherings" beats "I do not enjoy parties." [moderate]

### Situational Judgment Tests (SJT)

Realistic scenarios where respondents evaluate response options, capturing contextualized judgment. [strong]

**Scenario design:**
- Base on **critical incidents** from job analysis or SME panels [Weekley2006] [academic].
- 3-5 sentences with role-relevant constraints (time pressure, competing priorities).
- Avoid overly role-specific scenarios that exclude respondents outside that exact context.

**Response format:**
- **Most/least effective** -- best balance of information, faking resistance, and respondent experience [Weekley2006] [academic].
- **Rank order** -- more information per item but higher cognitive load.
- **Rate each** -- allows normative scoring but loses forced trade-off.

**Scoring methods:**
- **Expert consensus** -- most common and defensible [Weekley2006] [academic]. [consensus]
- **Empirical keying** -- maximizes prediction, risks capitalization on chance.
- **Theory-based** -- transparent, may miss empirical patterns.

---

## Item Writing Principles

Apply across all formats. [consensus]

**Behavioral specificity:** Describe observable behaviors, not internal states. "I create written plans before starting projects" beats "I am organized" [HaladynaRodriguez2013] [academic]. Use active voice, concrete verbs (ask, delegate, review), and specify context.

**Single construct per item:** "I communicate clearly and manage my time well" conflates two constructs. Test: can a respondent agree with one half and disagree with the other? If yes, split.

**Reading level:** Target Flesch-Kincaid grade 6-8 for general populations, 10-12 for professional contexts [HaladynaRodriguez2013] [academic]. Keep items under 20 words. Avoid jargon and culturally-specific references.

**Stem construction:** Lead with context, end with behavior: "When working on a team project, I typically..." Avoid leading language and absolutes (always, never).

---

## Social Desirability and Faking Resistance

Social desirability (SD) inflates scores on positive traits and deflates negative ones when uncontrolled [Paulhus1991] [academic].

**Matched-desirability blocks (MFC):** Pre-test statements on a 1-7 desirability scale with an independent sample. Group statements within 0.5 SD of each other [Stark2005] [academic]. This is the primary defense against faking.

**Balanced keying (Likert):** Mix positive and negative items (60/40 or 50/50 split) to control acquiescence bias [Paulhus1991] [academic].

**SD scales:** Dedicated scales (e.g., Paulhus BIDR) allow post-hoc detection, but statistical SD correction is controversial -- it can remove valid trait variance [Ones1996] [academic]. [moderate] Prefer designing faking resistance into the format over detecting and correcting it.

**Forced-choice superiority:** MFC with matched desirability shows significantly higher faking resistance than Likert [Salgado2014] [academic]. [strong] Salgado & Tauriz (2014) meta-analysis (49 studies) found FC formats reduced faking-related score inflation by ~70% vs. single-stimulus Likert. Stark et al. (2005) showed MFC maintained rank-order validity (rho = .85) under instructed faking. Caveat: poorly matched MFC blocks are as fakeable as Likert. [moderate]

---

## Anchoring Effects

- Frequency anchors (Never to Always) reduce ambiguity for behavioral items [Krosnick1999] [academic]. Agreement anchors suit attitudes and evaluative judgments.
- Mismatch between item content and anchor type introduces construct-irrelevant variance.
- Decide anchor type before writing items to ensure content-format congruence.

---

## Distractor Analysis (MC Items)

For knowledge/ability items with one keyed answer and distractors. [consensus]

- Distractors chosen by <5% of respondents are non-functional -- remove or replace [HaladynaRodriguez2013] [academic].
- Three options with good distractors often outperform four with a dead distractor [HaladynaRodriguez2013] [academic]. [moderate]
- Distractors should represent common misconceptions, not absurd options.
- **Analysis:** compute selection proportions by score tertile. Correct answer should trend positive (low < mid < high). Distractors with positive trends indicate miskeying or ambiguity.

---

## Item Format Decision Tree

```
ITEM FORMAT SELECTION
=====================

What are you measuring?
|
+-- Personality / behavioral tendencies
|   |
|   +-- High stakes? (selection, promotion)
|   |   |
|   |   +-- YES --> Is faking a primary concern?
|   |   |   |
|   |   |   +-- YES --> MFC with matched desirability
|   |   |   |          (TIRT scoring, min 3 dimensions)
|   |   |   |
|   |   |   +-- NO  --> Likert (5-pt) + balanced keying
|   |   |              + SD detection scale
|   |   |
|   |   +-- NO (development, coaching)
|   |       |
|   |       +-- Likert (5-pt), frequency anchors
|   |           (reverse score >= 20% of items)
|   |
+-- Judgment / decision-making
|   |
|   +-- Context-dependent?
|   |   |
|   |   +-- YES --> SJT (most/least effective)
|   |   |          (expert consensus scoring)
|   |   |
|   |   +-- NO  --> MC with distractor analysis
|   |
+-- Knowledge / ability
|   |
|   +-- MC, 3-4 options per item
|      (all distractors functional, >5% selection)
|
+-- Attitudes / beliefs / values
    |
    +-- Likert (5 or 7-pt), agreement anchors
       (balanced keying, conceptual reverse items)
```

---

## Anti-patterns

### 1. Unmatched Social Desirability in MFC Blocks

**Mistake:** One statement is obviously more desirable ("I inspire others" vs. "I double-check spreadsheets"). Respondents pick the desirable option regardless of accuracy, turning MFC into a transparent SD measure [Stark2005] [academic].

**Fix:** Pre-rate all statements for desirability with an independent sample. Match within 0.5 SD before forming blocks.

### 2. All Positively-Keyed Likert Items (Acquiescence Bias)

**Mistake:** Every item keyed so "Strongly Agree" = more of the trait. Acquiescent responders score artificially high -- the score partly measures compliance, not the target construct [Paulhus1991] [academic].

**Fix:** Include 20-40% reverse-scored items as conceptual opposites ("I often leave tasks unfinished"), not grammatical negations ("I do not plan ahead").

### 3. SJT Options That Are Obviously Right or Wrong

**Mistake:** Including "Yell at the client" alongside "Calmly address the concern." Zero variance, zero information, damages perceived fairness [Weekley2006] [academic].

**Fix:** All options should be plausible responses a reasonable person might choose. The "best" option is best by degree, not by kind. Verify with SMEs.

---

## References

- `[Brown2011]` Brown, A., & Maydeu-Olivares, A. (2011). Item response modeling of forced-choice questionnaires. *Educational and Psychological Measurement, 71*(3), 460-502. `[academic]`
- `[HaladynaRodriguez2013]` Haladyna, T. M., & Rodriguez, M. C. (2013). *Developing and validating test items.* Routledge. `[academic]`
- `[Krosnick1999]` Krosnick, J. A. (1999). Survey research. *Annual Review of Psychology, 50*, 537-567. `[academic]`
- `[Ones1996]` Ones, D. S., Viswesvaran, C., & Reiss, A. D. (1996). Role of social desirability in personality testing for personnel selection. *Journal of Applied Psychology, 81*(6), 660-679. `[academic]`
- `[Paulhus1991]` Paulhus, D. L. (1991). Measurement and control of response bias. In J. P. Robinson et al. (Eds.), *Measures of personality and social psychological attitudes* (pp. 17-59). Academic Press. `[academic]`
- `[Salgado2014]` Salgado, J. F., & Tauriz, G. (2014). The Five-Factor Model, forced-choice personality inventories and performance: A comprehensive meta-analysis. *European Journal of Work and Organizational Psychology, 23*(1), 3-30. `[academic]`
- `[Stark2005]` Stark, S., Chernyshenko, O. S., & Drasgow, F. (2005). An IRT approach to constructing and scoring pairwise preference items involving stimuli on different dimensions. *Applied Psychological Measurement, 29*(3), 184-203. `[academic]`
- `[Weekley2006]` Weekley, J. A., & Ployhart, R. E. (2006). *Situational judgment tests: Theory, measurement, and application.* Erlbaum. `[academic]`
