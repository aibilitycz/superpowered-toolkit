# Reliability

How consistently an instrument measures what it claims to measure. Necessary but not sufficient for validity — a ruler that always reads 2cm too long is reliable but not valid. See `validity.md` for the validity argument; see `statistics.md` for computation details.

---

## Internal Consistency

Measures whether items within a scale are measuring the same construct.

### Cronbach's Alpha

The most widely reported coefficient. Estimates proportion of total score variance attributable to the true score. [consensus]

- **Formula basis:** Average inter-item correlation scaled by number of items
- **Range:** 0 to 1 (negative values indicate a problem, not low reliability)
- **Assumption:** Tau-equivalence (equal true-score loadings) — rarely true in practice [McNeish2018] [academic]

**When alpha misleads:**
- Multidimensional scales: under- or overestimates depending on structure [Sijtsma2009] [academic]
- Unequal loadings: underestimates reliability [Revelle2009] [academic]
- Adding redundant items inflates alpha without improving measurement [strong]
- Short scales (< 5 items): mechanically deflated by item count [Sijtsma2009] [academic]

### McDonald's Omega

Recommended when tau-equivalence is violated — which is most instruments. [strong]

- **Omega total (omega_t):** Variance due to all common factors. Use for total-score reliability. [Revelle2009] [academic]
- **Omega hierarchical (omega_h):** Variance due to the general factor only. Use with bifactor/hierarchical models to see how much of the total score reflects the intended construct vs. group-factor noise. [Revelle2009] [academic]

**Rule of thumb:** If omega_t and alpha are within 0.02, either is fine. If they diverge, alpha is distorted — report omega. [McNeish2018] [academic]

### Composite Reliability (CR)

For multi-scale instruments with composite scores from subscales:

- **CR = (sum of loadings)^2 / [(sum of loadings)^2 + sum of error variances]** (from CFA)
- Does not assume tau-equivalence. Threshold: CR >= 0.70. [NunnallyBernstein1994] [academic] [moderate]

---

## Test-Retest Reliability

Stability over time: administer the same instrument to the same people twice, correlate scores.

| Construct Type | Interval | Rationale |
|----------------|----------|-----------|
| Stable traits (personality, ability) | 2-4 weeks | Prevents memory effects; true change unlikely [NunnallyBernstein1994] [academic] |
| States or moods | Hours to days | Construct genuinely changes; long gaps confound stability with change |
| Attitudes | 1-2 weeks | Moderate temporal stability expected |
| Skills under development | Varies | Low retest may reflect learning, not poor reliability |

**Watch out:** Low test-retest can mean poor reliability OR genuine construct change. The coefficient alone cannot distinguish them. [consensus]

---

## Inter-Rater Reliability

Critical for assessments involving human or AI judgment.

### ICC (Intraclass Correlation)

Standard metric for continuous ratings. Choosing the wrong form produces misleading results. [Shrout1979] [academic]

| ICC Form | Use When |
|----------|----------|
| ICC(1,1) | Each subject rated by different random raters |
| ICC(2,1) | Random raters, you need absolute score agreement |
| ICC(3,1) | Fixed raters, you need rank-order consistency |
| ICC(2,k) / ICC(3,k) | Same as above but for averaged ratings across k raters |

**AI scoring:** ICC(3,1) for consistency with human raters; ICC(2,1) when AI must be interchangeable with humans. [strong]

### Cohen's Kappa

For categorical ratings. Corrects for chance agreement (unlike raw percent agreement). [consensus]

- **Weighted kappa (quadratic):** For ordered categories. Numerically equivalent to ICC. [strong]
- **Benchmarks:** < 0.40 poor, 0.40-0.60 moderate, 0.60-0.80 substantial, > 0.80 excellent [Landis1977] [academic]

---

## Split-Half Reliability

Divide the test into two halves, correlate the half-scores. Fast but crude — rarely the primary reliability method today.

- **Spearman-Brown correction:** Adjusts the half-test correlation to estimate full-test reliability: `r_full = 2 * r_half / (1 + r_half)`
- **Splitting method matters:** Odd-even splitting is conventional, but random splits vary. Coefficient alpha is actually the mean of all possible split-half coefficients. [NunnallyBernstein1994] [academic]
- **Use case today:** Quick sanity check during development, or when only a single administration is available and item-level data is not accessible.

---

## Standard Error of Measurement (SEM)

Translates reliability into a concrete error band: `SEM = SD * sqrt(1 - r)`. A 95% CI around an observed score is approximately `score +/- 1.96 * SEM`. [consensus]

- Scores differing by less than 1 SEM should not be treated as meaningfully different [strong]
- Use SEM to set minimum detectable difference thresholds in scoring logic
- In IRT systems, SEM varies along the trait continuum (conditional SEM) — report it per person, not just per test [Embretson2000] [academic]

---

## Reliability Thresholds by Stakes

Floors, not targets. [NunnallyBernstein1994] [academic] [strong]

| Stakes | Minimum | Examples |
|--------|---------|----------|
| **High** | >= 0.90 | Hiring, certification, clinical diagnosis |
| **Moderate** | >= 0.80 | Development feedback, screening, team placement |
| **Low** | >= 0.70 | Research, exploration, formative feedback |

A reliability of 0.70 means 30% of score variance is error. [consensus]

---

## Decision Tree: Which Reliability Coefficient to Report

```
What type of assessment?
│
├─ Single administration, item-level data available
│  ├─ Scale is unidimensional (confirmed by CFA)?
│  │  ├─ Factor loadings roughly equal? → Cronbach's alpha is adequate
│  │  └─ Loadings vary substantially? → Report McDonald's omega_t
│  ├─ Scale has subscales or group factors?
│  │  └─ Report omega_h (general factor) + omega_t (total)
│  │     + subscale-level omega or alpha
│  └─ Composite of multiple scales?
│     └─ Report composite reliability (CR) from CFA
│
├─ Two administrations, same instrument
│  └─ Report test-retest correlation
│     + internal consistency from each administration
│
├─ Ratings by human judges or AI scorers
│  ├─ Continuous scores? → ICC (choose form per Shrout & Fleiss table above)
│  ├─ Ordered categories? → Weighted kappa or ICC
│  └─ Nominal categories? → Cohen's kappa
│
└─ Split-half (only if item-level data unavailable)
   └─ Report Spearman-Brown corrected split-half coefficient
```

**General rule:** Report at least two types of reliability evidence when possible (e.g., internal consistency + test-retest). A single coefficient tells an incomplete story. [AERA2014] [standards]

---

## Anti-Patterns

### 1. "Alpha is 0.68, close enough"

Below threshold is below threshold. 0.68 for moderate stakes = 32% error variance. Fix it: add items, remove poor ones (check item-total correlations), investigate dimensionality. If 0.68 is the ceiling after refinement, lower the stakes of the decisions it informs. [strong]

### 2. Reporting only alpha when omega is more appropriate

If your CFA shows unequal loadings, alpha misrepresents reliability. McNeish (2018) showed tau-equivalence is violated in the vast majority of instruments. Default to omega. The difference can exceed 0.05. [McNeish2018] [academic] [strong]

### 3. Confusing reliability with validity

A perfectly reliable instrument can be perfectly useless. Reliability = consistency; validity = measuring the right thing. Never claim an assessment "works" on reliability alone. See `validity.md`. [Messick1995] [academic] [consensus]

---

## Implementation Notes

- **Compute both alpha and omega** by default. Flag divergence > 0.02.
- **Store item-level responses** — you cannot compute internal consistency post hoc without them.
- **AI scoring:** Compute inter-rater reliability (AI vs. human panel) before deployment. Track longitudinally — model drift degrades reliability.
- **Surface SEM in score reports.** Confidence bands prevent over-interpretation of small differences.

---

## References

- [Revelle2009] Revelle, W., & Zinbarg, R. E. (2009). Coefficients alpha, beta, omega, and the glb: Comments on Sijtsma. *Psychometrika, 74*(1), 145-154. [academic]
- [NunnallyBernstein1994] Nunnally, J. C., & Bernstein, I. H. (1994). *Psychometric Theory* (3rd ed.). McGraw-Hill. [academic]
- [Shrout1979] Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin, 86*(2), 420-428. [academic]
- [McNeish2018] McNeish, D. (2018). Thanks coefficient alpha, we'll take it from here. *Psychological Methods, 23*(3), 412-433. [academic]
- [Sijtsma2009] Sijtsma, K. (2009). On the use, the misuse, and the very limited usefulness of Cronbach's alpha. *Psychometrika, 74*(1), 107-120. [academic]
- [AERA2014] American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for Educational and Psychological Testing*. AERA. [standards]
- [Messick1995] Messick, S. (1995). Validity of psychological assessment: Validation of inferences from persons' responses and performances as scientific inquiry into score meaning. *American Psychologist, 50*(9), 741-749. [academic]
- [Embretson2000] Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum Associates. [academic]
- [Landis1977] Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159-174. [academic]
