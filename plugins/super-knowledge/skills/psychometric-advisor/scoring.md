# Scoring Methods

Practical reference for developers implementing psychometric scoring. Covers score types, transformations, composites, forced-choice scoring, and interpretation frameworks.

## Classical Scoring Formulas

The simplest scoring approaches aggregate item responses into scale scores [Nunnally1978] `[academic]`.

| Formula | Definition | When to use |
|---------|-----------|-------------|
| **Sum score** | X = sum of item responses | Default for Likert scales; preserves variance |
| **Mean score** | X = sum / k (k = item count) | Comparing scales with different item counts |
| **Proportion correct** | P = correct / total | Ability tests, knowledge assessments |

`[consensus]` Sum and mean scores are interchangeable for single-scale analysis. Mean scores are preferred when comparing across scales of different lengths.

**Developer note:** Store raw sum scores. Derive mean scores and proportions at display time to preserve precision and allow re-scoring.

## Normative Scoring

Normative scoring locates an individual relative to a reference group (norm sample). All normative transformations require a representative norm sample with known mean and SD [Nunnally1978] `[academic]` [AERA2014] `[standards]`.

### Standard Score Types

| Score | Formula | M | SD | Range (practical) | Use case |
|-------|---------|---|----|-------------------|----------|
| **z-score** | z = (X - M) / SD | 0 | 1 | -3 to +3 | Statistical analysis, intermediate calculations |
| **T-score** | T = 50 + 10z | 50 | 10 | 20-80 | Profile reporting; avoids negatives and decimals |
| **Percentile** | Area under normal curve below z | 50th | -- | 1-99 | Intuitive for non-technical audiences |
| **Stanine** | 9 bands on normal curve | 5 | ~2 | 1-9 | Coarse classification; reduces over-interpretation |

`[strong]` T-scores (M=50, SD=10) are the most widely used standard score in personality and competency assessment -- no negatives, integer-friendly, clean percentile mapping.

**Stanine distribution:** 4%-7%-12%-17%-20%-17%-12%-7%-4% across stanines 1-9.

**Percentile pitfall:** Percentiles are nonlinear. Never average percentiles directly -- convert to z-scores first, average, convert back [Nunnally1978] `[academic]`.

## Ipsative Scoring

Ipsative scores express the relative strength of traits within a single person. The term was coined by Cattell (1944), from Latin *ipse* ("himself") [Cattell1944] `[academic]`.

In forced-choice instruments, choosing one trait reduces scores on competing traits. Each person's scale scores sum to the same constant.

### Fundamental Limitations

`[strong]` Hicks (1970) demonstrated that purely ipsative scores have severe psychometric constraints [Hicks1970] `[academic]`:

- **No between-person comparison.** Scores are relative to each person's own profile, not comparable across individuals.
- **Zero-sum covariance.** Scale intercorrelations are artifactually negative, making factor analysis invalid.
- **Zero-sum validity.** Validity coefficients across scales sum to zero for any criterion -- high validity on one scale suppresses others.

Ipsative scores are valid for within-person profiling (coaching, self-awareness) but not for selection, ranking, or any between-person decision [Hicks1970] `[academic]`.

## Score Transformations

**Linear:** `Y = a + bX`. Preserves distribution shape; changes scale only. Raw-to-T-score is linear if raw scores are already normal.

**Normalized (area):** Maps raw scores to percentile ranks, then converts via inverse normal CDF: `z = Phi_inverse(percentile/100)`, then `T = 50 + 10z`. Forces non-normal data into normal shape.

`[moderate]` Use normalized transformations only when the construct is theoretically expected to be normal and observed non-normality is due to sampling, not genuine population skew. Normalizing a legitimately skewed distribution distorts the construct [Nunnally1978] `[academic]`.

## Floor and Ceiling Effects

### Detection

Floor effects occur when scores cluster at the minimum; ceiling effects when scores cluster at the maximum. Standard detection thresholds [consensus]:

| Severity | % at extreme | Action |
|----------|-------------|--------|
| Negligible | < 5% | No action needed |
| Minor | 5-10% | Monitor; note in documentation |
| Moderate | 10-15% | Investigate; consider additional items |
| Severe | > 15% | Redesign required; scores unreliable at extremes |

### Psychometric Consequences

- **Attenuated reliability:** Restricted variance reduces internal consistency estimates.
- **Attenuated validity:** Correlations with criteria are artificially weakened (restriction of range).
- **Insensitivity to change:** Cannot detect improvement (ceiling) or decline (floor) over time.

**Developer check:** After each data collection, compute `% at min` and `% at max`. Flag if either exceeds 15%.

## Composite Scoring

Composites combine multiple scale scores into a single score. The central question is how to weight component scales [Nunnally1978] `[academic]`.

### Weighting Methods

| Method | How weights are set | When to use |
|--------|-------------------|-------------|
| **Equal (unit)** | All scales weighted 1.0 | Default when no empirical basis exists; robust and transparent |
| **Theoretical** | Weights from substantive theory or job analysis | When construct importance hierarchy is well-established |
| **Empirical** | Weights from regression on a criterion | When criterion data is available and sample is large (N > 200) |

`[strong]` Equal weights are surprisingly robust -- unit-weighted composites perform comparably to optimally-weighted composites in cross-validation, because regression weights capitalize on sampling error [Bobko2007] `[academic]`.

### Composite Formula

```
Composite = w1*S1 + w2*S2 + ... + wk*Sk    (proportional weights sum to 1.0)
```

**Dominance check:** Flag if any single dimension contributes >50% of composite variance -- this signals construct underrepresentation.

## Band-Based Classification

Score bands group continuous scores into interpretive categories, acknowledging measurement error.

Bands should reflect the Standard Error of Measurement (SEM): boundary = cutoff +/- 1 SEM (68% CI) or +/- 1.96 SEM (95% CI).

`[moderate]` Overlapping bands (adjacent categories share an uncertainty zone) are psychometrically honest and reduce misclassification. Scores in the overlap zone should be reported as "borderline" rather than forced into a category [Cascio1991] `[academic]`.

## Scoring Forced-Choice (MFC) Instruments

### Classical Paired Comparison

Assigns +1 to chosen trait, 0 to unchosen. Produces fully ipsative scores. All Hicks (1970) limitations apply [Hicks1970] `[academic]`.

### Thurstonian IRT (TIRT) Scoring

`[strong]` Brown & Maydeu-Olivares (2011) introduced the TIRT model, which recovers normative (non-ipsative) trait estimates from forced-choice data by modeling the comparative judgment process [BrownMaydeu2011] `[academic]`.

TIRT models each pairwise comparison as a difference between two latent utilities, estimates person-level theta values per dimension, and produces scores free from the zero-sum constraint -- enabling valid between-person comparison.

`[moderate]` Wang et al. (2017) showed that TIRT-based theta estimates recover the latent trait structure more accurately than classical ipsative scoring, particularly for instruments with 3+ dimensions [Wang2017] `[academic]`.

**Developer rule:** Forced-choice + between-person comparison = must use IRT-based scoring. Classical scoring produces ipsative data invalid for ranking.

## Score Interpretation Frameworks

| Framework | Question answered | Score types | Requirements |
|-----------|------------------|-------------|--------------|
| **Norm-referenced** | "How does this person compare to others?" | T-score, percentile, stanine | Representative norm sample; refresh every 5-10 years |
| **Criterion-referenced** | "Does this person meet the standard?" | Pass/fail, band classification | Empirically established cutoffs; documented standard-setting method (e.g., Angoff) |

Both defined in [AERA2014] `[standards]`. Many assessments combine both: norm-referenced profiles with criterion-referenced pass/fail cutoffs.

## Decision Tree: Which Scoring Method?

```
ITEM FORMAT?
|
+-- Likert/rating -> Single scale? -> Sum/mean score
|                    Multiple?     -> Need overall? YES -> Composite
|                                                   NO  -> Independent scales
|                    Between-person? YES -> T-score/percentile
|                                    NO  -> Raw scores OK
|
+-- Forced-choice -> Between-person? YES -> TIRT theta [BrownMaydeu2011]
|                                     NO  -> Classical (ipsative) OK
|                    Dimensions: 2 -> TIRT optional | 3+ -> TIRT recommended
|
+-- Right/wrong   -> Simple: proportion correct
                     High-stakes/adaptive: IRT theta

COMPOSITE WEIGHTS?
|
+-- Criterion data + N>200? -> Empirical (cross-validate!)
+-- Theory/job analysis?    -> Theoretical (document rationale)
+-- Neither?                -> Equal weights (default; robust)

INTERPRETATION?
+-- "Compare to peers?"     -> Norm-referenced (T-score, percentile)
+-- "Meet a standard?"      -> Criterion-referenced (cutoff)
```

## Anti-Patterns

### 1. Treating Ipsative Scores as Normative `[strong]`

Developer ranks candidates by classical forced-choice scale scores or runs factor analysis on ipsative data. Both are invalid -- person totals are constant, correlations are artifactually negative, and spurious factors emerge [Hicks1970] `[academic]`. **Fix:** Use TIRT for between-person comparisons. If TIRT is infeasible, do not use forced-choice for selection.

### 2. Arbitrary Weights Without Justification `[moderate]`

"40% leadership, 35% communication, 25% analytical" with no empirical or theoretical basis. Arbitrary weights inject unvalidated assumptions and are indefensible in adverse impact challenges [Bobko2007] `[academic]`. **Fix:** Default to equal weights. Document any differential weighting rationale (job analysis, SME panel, regression). Cross-validate empirical weights.

### 3. Ignoring Floor/Ceiling Effects `[consensus]`

Deploying an assessment without checking score distributions. If 25% score at the maximum, the instrument cannot discriminate among high performers -- reliability and validity are attenuated. **Fix:** Check distributions after every collection. Flag >15% at either extreme. Extend item difficulty range or use adaptive testing.

## References

- `[Nunnally1978]` Nunnally, J. C. (1978). *Psychometric Theory* (2nd ed.). McGraw-Hill. `[academic]`
- `[Cattell1944]` Cattell, R. B. (1944). Psychological measurement: Normative, ipsative, interactive. *Psychological Review, 51*(5), 292-303. `[academic]`
- `[Hicks1970]` Hicks, L. E. (1970). Some properties of ipsative, normative, and forced-choice normative measures. *Psychological Bulletin, 74*(3), 167-184. `[academic]`
- `[BrownMaydeu2011]` Brown, A., & Maydeu-Olivares, A. (2011). Item response modeling of forced-choice questionnaires. *Educational and Psychological Measurement, 71*(3), 460-502. `[academic]`
- `[Wang2017]` Wang, W. C., Qiu, X. L., Chen, C. W., Ro, S., & Jin, K. Y. (2017). Item response theory models for ipsative tests with multidimensional pairwise comparison items. *Applied Psychological Measurement, 41*(8), 600-613. `[academic]`
- `[AERA2014]` American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for Educational and Psychological Testing*. AERA. `[standards]`
- `[Bobko2007]` Bobko, P., Roth, P. L., & Buster, M. A. (2007). The usefulness of unit weights in creating composite scores: A literature review, application to content validity, and meta-analysis. *Organizational Research Methods, 10*(4), 689-709. `[academic]`
- `[Cascio1991]` Cascio, W. F., Goldstein, I. L., Outtz, J., & Zedeck, S. (1991). Twenty-one issues and answers about banding. *Human Performance, 4*(1), 67-73. `[academic]`
