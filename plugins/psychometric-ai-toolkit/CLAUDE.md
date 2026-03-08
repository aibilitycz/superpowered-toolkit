# Psychometric AI Toolkit

Expert-level psychometric knowledge for AI-assisted assessment development. All guidance grounded in peer-reviewed research.

## Methodology Anchor

- **Layer:** MEASURE (primary capability layer in the Superpowered Toolkit framework)
- **Superpowers served:** All 5 — Perception, Intelligence, Knowledge, Creation, Integration
- **Methodology components:** L1 scoring, L2 scoring, item calibration, reliability, validity, composite weights
- **Why this belongs:** You cannot assess the 5 superpowers without psychometrically sound measurement. Every dimension score, composite weight, and assessment decision depends on the science encoded here.

See `../../METHODOLOGY.md` for the four capability layers (MEASURE/DEVELOP/BUILD/GOVERN), methodology anchor rule, and conflict resolution.

**Overlay rule:** When SP methodology makes a specific decision (e.g., 35/30/25/10 composite weights), it overrides generic toolkit recommendations for Aimee/SP implementations. Generic advice applies for non-SP use cases.

## Core Principles

1. **Measurement before technology.** Psychometric validity comes first. AI is a delivery mechanism, not a substitute for sound measurement science.
2. **Evidence strength matters.** Mark every recommendation with its evidence base: `[strong]` (meta-analyses, replicated findings), `[moderate]` (single well-designed studies), `[emerging]` (practitioner experience, limited research), `[consensus]` (professional standards bodies).
3. **No black boxes.** Every score, weight, and threshold must be explainable. If you can't justify it psychometrically, don't use it.
4. **Fairness is non-negotiable.** DIF analysis, adverse impact checks, and cultural sensitivity review are requirements, not nice-to-haves.
5. **Context determines method.** There is no universally "best" IRT model, item format, or scoring method. The right choice depends on purpose, population, stakes, and constraints.

## Quick Decision Trees

### Which IRT Model?

```
Is your instrument unidimensional?
├─ Yes → Are items dichotomous (right/wrong)?
│  ├─ Yes → Are items equally discriminating?
│  │  ├─ Yes → Rasch / 1PL
│  │  └─ No → 2PL (add guessing parameter? → 3PL)
│  └─ No (polytomous) → Graded Response Model (GRM) or Partial Credit Model
└─ No (multidimensional) → MIRT or bifactor model
   └─ Forced-choice format? → Thurstonian IRT (TIRT)
```

### Which Item Format?

```
What is the assessment purpose?
├─ Personality / soft skills → Is faking a concern?
│  ├─ High stakes (selection) → MFC (forced-choice blocks)
│  └─ Low stakes (development) → Likert is acceptable
├─ Situational judgment → SJT with behavioral anchors
├─ Knowledge / ability → MC with distractor analysis
└─ Behavioral observation → AI-scored open-ended + rubric
```

### Reliability Acceptable?

```
What is the decision stakes?
├─ High stakes (hiring, certification) → α/ω ≥ 0.90
├─ Moderate stakes (development, screening) → α/ω ≥ 0.80
└─ Low stakes (research, exploration) → α/ω ≥ 0.70
```

## Disclaimer

This toolkit provides guidance based on published psychometric research, not certification. For high-stakes assessment decisions (hiring, certification, clinical diagnosis), verify recommendations with a qualified psychometrician. The toolkit authors are not liable for assessment decisions made using this guidance.
