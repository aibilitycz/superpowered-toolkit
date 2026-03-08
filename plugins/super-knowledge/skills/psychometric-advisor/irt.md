# Item Response Theory (IRT)

Practical reference for developers building assessment systems. Covers model selection, parameter interpretation, fit assessment, and common mistakes.

---

## Classical Test Theory (CTT): The Baseline

CTT decomposes an observed score into true score plus error: **X = T + E** [Lord1968]. Three limitations motivate moving to IRT:

- **Sample-dependent item statistics.** Difficulty values change with the sample tested [Embretson2000].
- **Test-dependent person scores.** Scores depend on which items were administered, complicating cross-form comparisons [Hambleton1991].
- **Constant measurement error.** CTT assumes equal SEM across the entire score range; in practice, precision varies by trait level [deAyala2009].

IRT addresses all three: item parameters are invariant across samples, person parameters are invariant across items, and measurement precision varies along the trait continuum. `[strong]` `[consensus]`

---

## IRT Models

### Rasch / One-Parameter Logistic (1PL)

Single item parameter — **difficulty (b)**. P(correct) = exp(theta - b) / [1 + exp(theta - b)].

**Key assumption:** All items discriminate equally. Rasch practitioners treat this as prescriptive — items that don't fit are removed, not modeled with extra parameters [Rasch1960].

**When to use:** Small samples (N >= 100), educational assessments with controlled item quality, when specific objectivity is prioritized. `[strong]`

### Two-Parameter Logistic (2PL)

Adds **discrimination (a)**: P(correct) = exp[a(theta - b)] / {1 + exp[a(theta - b)]}.

- **a (discrimination):** ICC slope at inflection. Typical range: 0.5-2.5. Below 0.5 = weak item [Baker2004].
- **b (difficulty):** Theta where P = 0.50. Range: -3 to +3 logits [Embretson2000].

**When to use:** N >= 250, items varying in discriminating power, most personality/attitude assessments with binary scoring. `[strong]`

### Three-Parameter Logistic (3PL)

Adds **guessing (c)** — lower asymptote: P = c + (1-c) * 2PL formula.

- **c (pseudo-guessing):** P(correct) as theta approaches negative infinity. Theoretical chance for 4-option MC = 0.25, but estimated values often differ [deAyala2009].

**When to use:** N >= 500 (preferably 1000+), multiple-choice knowledge/ability tests. Avoid for personality items where guessing is meaningless. `[strong]`

### Graded Response Model (GRM)

For ordered polytomous items (Likert scales, partial credit) [Samejima1969]. Extends 2PL to m+1 ordered categories.

**Parameters:** One **a** (discrimination) per item. **m thresholds (b_k)** per item — the theta where cumulative P(X >= k) = 0.50. Must be ordered: b_1 < b_2 < ... < b_m.

**Mechanics:** Models cumulative probabilities, then derives category probabilities by subtraction: P(X=k) = P*(X >= k) - P*(X >= k+1).

**When to use:** Likert-type items, any ordered response categories, N >= 250. `[strong]`

### Thurstonian IRT (TIRT)

For forced-choice / MFC questionnaires [Brown2011]. Models the comparison process when respondents rank or choose between statements within a block.

**How it works:** Each statement has a latent utility on its trait dimension. Respondents choose the statement with higher perceived utility. Parameters: **trait loadings (lambda)**, **threshold (tau)** for statement attractiveness, and **uniquenesses**.

TIRT produces normative (non-ipsative) scores from forced-choice data, solving the problem that classical ipsative scoring distorts inter-trait correlations and criterion validity [Brown2012].

**When to use:** MFC personality assessments, faking-resistant selection contexts, blocks of 2+ statements on different dimensions. N >= 300. `[moderate]`

---

## Item Parameter Quick Reference

| Parameter | Symbol | Model(s) | Interpretation | Typical Range |
|-----------|--------|----------|----------------|---------------|
| Difficulty | b | All | Trait level for P = 0.50 | -3 to +3 logits |
| Discrimination | a | 2PL, 3PL, GRM | Slope at inflection; higher = sharper | 0.5 - 2.5 |
| Guessing | c | 3PL | Lower asymptote; chance of correct when theta is very low | 0.0 - 0.35 |
| Threshold | b_k | GRM | Boundary between adjacent categories | Ordered within item |
| Trait loading | lambda | TIRT | Statement-trait relationship strength | 0.3 - 0.9 (standardized) |

---

## Model Selection Decision Tree

```
What is the item response format?
│
├─ Binary (correct/incorrect, yes/no)
│  ├─ Guessing plausible? (MC knowledge test)
│  │  ├─ Yes + N >= 500 ──► 3PL
│  │  └─ Yes + N < 500  ──► 2PL with fixed c
│  └─ No guessing ──► Items vary in discrimination?
│     ├─ Yes / unknown ──► 2PL  [default]
│     └─ No / want specific objectivity ──► Rasch (1PL)
│
├─ Ordered categories (Likert, partial credit)
│  ├─ N >= 250 ──► GRM  [default for polytomous]
│  └─ N < 250  ──► CTT or partial credit model
│
├─ Forced-choice blocks (MFC)
│  ├─ Need normative scores ──► TIRT
│  └─ Ipsative OK ──► classical scoring (note validity limits)
│
├─ Multidimensional ──► MIRT (beyond this guide)
└─ Nominal categories ──► NRM (rarely needed)
```

---

## Model Fit Assessment

**Item fit:** Use **S-X2** [Orlando2000] — less sample-size sensitive than traditional chi-square. Items with p < .01 (after correction) warrant review. RMSEA per item: < 0.05 good, 0.05-0.08 acceptable, > 0.10 poor. `[strong]`

**Person fit:** **l_z** [Drasgow1985] — standardized log-likelihood of response pattern. Values z < -2 flag aberrant patterns (guessing, carelessness). Investigate before discarding.

**Model comparison:** **LRT** for nested models (1PL vs 2PL, 2PL vs 3PL) [deAyala2009]. **AIC/BIC** for non-nested; BIC preferred (stronger parsimony penalty) `[moderate]`. **M2** for limited-information fit; report with RMSEA_M2 [Maydeu-Olivares2013].

**Rule:** Use multiple indices together. No single statistic is decisive. `[consensus]`

---

## Anti-Patterns

### 1. Using 3PL on personality items

**Mistake:** Applying 3PL to personality questionnaires because "it's the most sophisticated model."

**Why it fails:** The c-parameter models guessing. Personality items have no correct answer and no guessing mechanism. The parameter becomes uninterpretable and destabilizes estimation [Embretson2000].

**Fix:** 2PL for binary personality items, GRM for Likert-type. Reserve 3PL for multiple-choice knowledge tests.

### 2. Running IRT calibration with insufficient sample size

**Mistake:** Calibrating 2PL or 3PL on N = 80 and treating parameters as stable.

**Why it fails:** Small samples produce discrimination estimates with large standard errors — items appear extreme due to noise, not real quality differences. The 3PL c-parameter is especially fragile below N = 500 [deAyala2009].

**Minimum sample sizes (rules of thumb):**

| Model | Minimum N | Recommended N |
|-------|-----------|---------------|
| Rasch / 1PL | 100 | 200+ |
| 2PL | 250 | 500+ |
| 3PL | 500 | 1000+ |
| GRM | 250 | 500+ |
| TIRT | 300 | 500+ |

`[moderate]` — exact thresholds depend on test length, parameter distributions, and estimation method.

**Fix:** Start with Rasch/1PL or CTT for pilot data. Graduate to more complex models as sample grows. Use simulation studies to verify your sample supports stable estimation before trusting parameters.

### 3. Ignoring unidimensionality and local independence assumptions

**Mistake:** Fitting a unidimensional IRT model to multidimensional items without checking assumptions.

**Why it fails:** Theta conflates distinct constructs. Discrimination is inflated for dominant-factor items and deflated for others. Local independence violations (testlets, shared stimuli) inflate reliability and distort standard errors [Embretson2000] [deAyala2009].

**Fix:** Run EFA/CFA before IRT calibration. Check eigenvalue ratio (>= 3:1 heuristic for dominant factor). Use bifactor models for testlets, MIRT for genuinely multidimensional data, or fit separate models per subscale.

---

## Recommendations Summary

- Default to **2PL** for binary items, **GRM** for Likert-type `[strong]` [Embretson2000] [deAyala2009]
- Use **TIRT** for forced-choice assessments needing normative scores `[moderate]` [Brown2011]
- Always check **unidimensionality** before fitting any IRT model `[consensus]`
- Report **multiple fit indices**; never rely on one statistic `[consensus]` [Maydeu-Olivares2013]
- Start simple (Rasch/CTT) with small samples; add complexity with data `[strong]` [deAyala2009]
- Prefer **BIC** over AIC for model comparison `[moderate]`

---

## References

- **[Rasch1960]** `[academic]` Rasch, G. (1960). *Probabilistic Models for Some Intelligence and Attainment Tests.* Copenhagen: Danish Institute for Educational Research.
- **[Lord1968]** `[academic]` Lord, F. M., & Novick, M. R. (1968). *Statistical Theories of Mental Test Scores.* Addison-Wesley.
- **[Samejima1969]** `[academic]` Samejima, F. (1969). Estimation of latent ability using a response pattern of graded scores. *Psychometrika Monograph Supplement, 34*(4, Pt. 2), 1-97.
- **[Hambleton1991]** `[academic]` Hambleton, R. K., Swaminathan, H., & Rogers, H. J. (1991). *Fundamentals of Item Response Theory.* Sage.
- **[Embretson2000]** `[academic]` Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists.* Lawrence Erlbaum.
- **[Baker2004]** `[academic]` Baker, F. B. (2004). *Item Response Theory: Parameter Estimation Techniques* (2nd ed.). Marcel Dekker.
- **[deAyala2009]** `[academic]` de Ayala, R. J. (2009). *The Theory and Practice of Item Response Theory.* Guilford Press.
- **[Brown2011]** `[academic]` Brown, A., & Maydeu-Olivares, A. (2011). Item response modeling of forced-choice questionnaires. *Educational and Psychological Measurement, 71*(3), 460-502.
- **[Brown2012]** `[academic]` Brown, A., & Maydeu-Olivares, A. (2012). Fitting a Thurstonian IRT model to forced-choice data using Mplus. *Behavior Research Methods, 44*(4), 1135-1147.
- **[Maydeu-Olivares2013]** `[academic]` Maydeu-Olivares, A. (2013). Goodness-of-fit assessment of item response theory models. *Measurement, 11*(3), 71-101.
- **[Orlando2000]** `[academic]` Orlando, M., & Thissen, D. (2000). Likelihood-based item-fit indices for dichotomous IRT models. *Applied Psychological Measurement, 24*(1), 50-64.
- **[Drasgow1985]** `[academic]` Drasgow, F., Levine, M. V., & Williams, E. A. (1985). Appropriateness measurement with polychotomous item response models. *British Journal of Mathematical and Statistical Psychology, 38*(1), 67-86.
