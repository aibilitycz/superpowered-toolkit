# Statistical Methods for Psychometrics

Core statistical techniques for building, validating, and evaluating psychometric instruments. Practical reference for developers implementing assessments.

---

## Exploratory Factor Analysis (EFA)

EFA discovers latent factor structure when dimensionality is unknown. Use during instrument development [consensus].

**Extraction**: Use Maximum Likelihood (ML) for normal data (produces fit statistics) or Principal Axis Factoring (PAF) for non-normal data. Avoid PCA for construct identification -- it conflates common and unique variance [CostelloOsborne2005] [strong].

**Rotation**: Default to oblique (direct oblimin, promax). Psychological factors are almost always correlated, and oblique rotation recovers the orthogonal solution if factors happen to be uncorrelated [CostelloOsborne2005] [strong]. Use orthogonal (varimax) only when theory requires uncorrelated factors [Kline2015].

**Factor retention** is the most consequential EFA decision. Triangulate multiple methods [CostelloOsborne2005]:

| Method | Description | Quality |
|--------|------------|---------|
| **Parallel Analysis** [Horn1965] | Compares observed eigenvalues to eigenvalues from random data of the same dimensions. Retain factors whose observed eigenvalue exceeds the random 95th percentile. | Best-performing method in simulation studies [strong] |
| **Velicer's MAP** [Velicer1976] | Computes average squared partial correlation after removing each successive component. Retain factors up to the minimum average partial. | Strong second method; complements parallel analysis [strong] |
| **Scree plot** | Visual inspection of eigenvalue plot for the "elbow." | Subjective; use as confirmatory check, never as sole criterion [moderate] |
| **Kaiser criterion** (eigenvalue > 1) | Retain all factors with eigenvalue above 1.0. | Consistently over-extracts factors. Do not use as primary method [strong] |

---

## Confirmatory Factor Analysis (CFA)

CFA tests whether a hypothesized factor structure fits observed data. It is a special case of SEM restricted to measurement models [Brown2015].

**Three requirements**: (1) **Specification** -- define the model a priori from theory or prior EFA [Brown2015] [consensus]. (2) **Identification** -- each factor needs 3+ indicators (4+ preferred) [Kline2015]. (3) **Estimation** -- ML for continuous normal data; WLSMV for ordinal items (Likert < 5 categories) [Brown2015] [strong].

**EFA vs CFA**: EFA asks "what is the structure?" (exploratory). CFA asks "does this structure fit?" (confirmatory). Never run CFA on the same data used for EFA -- always use a hold-out sample [Brown2015] [consensus].

---

## Structural Equation Modeling (SEM)

SEM combines measurement models (CFA) with structural models (path/regression among latent variables), accounting for measurement error [Kline2015].

**Components**: Measurement model (CFA linking indicators to latent variables) + structural model (regression paths among latent variables). For mediation (A -> M -> B), test indirect effects with bootstrapped CIs, not the Sobel test [Kline2015] [strong].

**Two-step approach**: First establish adequate CFA fit, then add structural paths. This prevents confounding poor measurement with poor theory [strong].

---

## Bifactor Models

A bifactor model specifies one **general factor** (all items load on it) plus multiple **specific (group) factors** (subsets of items). Factors are orthogonal by specification [Reise2012].

**When to use**: Testing if a construct is "unidimensional enough" for a total score; evaluating whether subscales add value beyond the total; instruments with a dominant general factor plus domain facets [Reise2012].

### Key Indices

| Index | Interpretation | Threshold |
|-------|---------------|-----------|
| **ECV** (Explained Common Variance) | Proportion of common variance due to the general factor | > 0.70 suggests essentially unidimensional [moderate] |
| **Omega-H** (Omega Hierarchical) | Reliability of total score attributable to general factor | > 0.75 supports total score interpretation [Rodriguez2016] |
| **Omega-HS** (Omega Hierarchical Subscale) | Reliability of subscale after removing general factor | Low values mean subscale scores add little beyond total |

---

## Model Fit Indices

No single fit index is sufficient. Report multiple indices from different families [HuBentler1999] [consensus].

| Index | Acceptable | Good | Measures |
|-------|-----------|------|----------|
| **RMSEA** | < 0.08 | < 0.06 | Parsimony-adjusted badness of fit [HuBentler1999] |
| **CFI** | > 0.90 | > 0.95 | Incremental fit vs null model [HuBentler1999] |
| **TLI** (NNFI) | > 0.90 | > 0.95 | Like CFI, penalizes complexity [HuBentler1999] |
| **SRMR** | - | < 0.08 | Average standardized residual [HuBentler1999] |
| **Chi-square** | p > 0.05 | - | Exact-fit test; report but do not rely on |

**Two-index strategy**: Always pair SRMR with CFI, TLI, or RMSEA. Report RMSEA with 90% CI [HuBentler1999] [strong].

---

## Sample Size Requirements

| Analysis | Minimum | Recommended | Source |
|----------|---------|-------------|--------|
| **EFA** | N:p ratio 5:1 | N:p ratio 10:1 or N >= 300 | [CostelloOsborne2005] [moderate] |
| **CFA** | N >= 200 | N:q ratio 10:1 (q = free params) | [Kline2015] [moderate] |
| **SEM** | N:q ratio 10:1 | N:q ratio 20:1 | [Kline2015] [strong] |
| **IRT (2PL)** | N >= 250 | N >= 500 | [Embretson2000] [moderate] |

N:p = participants per item (EFA). N:q = participants per estimated parameter (CFA/SEM). A 20-item, 5-factor CFA easily has 50+ free parameters, requiring N >= 500. For high-stakes decisions, use Monte Carlo power simulation (Mplus, simsem in R) rather than rules of thumb [strong].

---

## Effect Sizes

| Measure | Small | Medium | Large | Use Case |
|---------|-------|--------|-------|----------|
| **Cohen's d** | 0.20 | 0.50 | 0.80 | Mean differences between groups |
| **Eta-squared** | 0.01 | 0.06 | 0.14 | Variance explained (ANOVA) |
| **Omega-squared** | 0.01 | 0.06 | 0.14 | Less biased eta-squared alternative; preferred [strong] |
| **r** (correlation) | 0.10 | 0.30 | 0.50 | Bivariate association |

Always report effect sizes alongside p-values. Statistical significance with large N tells you nothing about practical importance [Cohen1988] [consensus].

---

## Correlation in Psychometric Context

**Attenuation correction**: Observed correlations are weakened by measurement error. Correct with `r_corrected = r_observed / sqrt(rxx * ryy)`. Report both observed and corrected values [Nunnally1994] [strong].

**Restriction of range**: When sampling only high (or low) scorers, correlations with other variables are artificially reduced. Apply Thorndike's Case 2/3 corrections when generalizing from selected to full populations [strong].

---

## Decision Tree: Which Analysis Should I Run?

```
What is your research question?
|
+-- "What is the factor structure?"
|   +-- No prior theory       --> EFA (ML, oblique, parallel analysis)
|   +-- Have a hypothesis      --> CFA (on independent sample)
|
+-- "Does my structure fit?"   --> CFA
|   +-- + relationships?       --> Full SEM
|
+-- "Unidimensional enough     --> Bifactor model
|    for a total score?"           (check ECV, omega-H, omega-HS)
|
+-- "Do groups differ on       --> Multi-group CFA (measurement invariance)
|    a latent construct?"          then multi-group SEM
|
+-- "Relationship between      --> SEM (if measured with error)
     two constructs?"              Correlation + attenuation correction (if simple)
```

---

## Anti-Patterns

### 1. Using EFA When CFA Is Needed (or Vice Versa)

Running EFA on data where you have a hypothesized structure, or running CFA as an "exploratory" tool by chasing modification indices. CFA re-specified iteratively is a poorly controlled EFA [Brown2015]. **Rule**: If you have a structure, test with CFA on held-out data. If CFA fails, revise theory, not the model. [consensus]

### 2. Reporting Only Chi-Square for Model Fit

Rejecting a model because chi-square is significant. Chi-square is a function of sample size: N > 200 rejects trivially misspecified models; N < 100 passes badly misspecified ones [HuBentler1999] [Kline2015]. **Rule**: Report chi-square for transparency but evaluate fit using RMSEA, CFI, TLI, and SRMR together. [consensus]

### 3. Running CFA With Inadequate Sample Size

Fitting a 30-item, 5-factor CFA with N=50 (N:q below 1:1; minimum is 10:1). Parameter estimates are unstable, standard errors unreliable, fit indices biased upward [Kline2015]. **Rule**: Calculate free parameters before collecting data. If N:q < 10:1, increase N or reduce model complexity. [strong]

---

## References

- [Brown2015] Brown, T. A. (2015). *Confirmatory Factor Analysis for Applied Research* (2nd ed.). Guilford Press. [academic]
- [Cohen1988] Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum. [academic]
- [CostelloOsborne2005] Costello, A. B., & Osborne, J. W. (2005). Best practices in exploratory factor analysis: Four recommendations for getting the most from your analysis. *Practical Assessment, Research, and Evaluation, 10*(7), 1-9. [academic]
- [Embretson2000] Embretson, S. E., & Reise, S. P. (2000). *Item Response Theory for Psychologists*. Lawrence Erlbaum. [academic]
- [Horn1965] Horn, J. L. (1965). A rationale and test for the number of factors in factor analysis. *Psychometrika, 30*(2), 179-185. [academic]
- [HuBentler1999] Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling, 6*(1), 1-55. [academic]
- [Kline2015] Kline, R. B. (2015). *Principles and Practice of Structural Equation Modeling* (4th ed.). Guilford Press. [academic]
- [Nunnally1994] Nunnally, J. C., & Bernstein, I. H. (1994). *Psychometric Theory* (3rd ed.). McGraw-Hill. [academic]
- [Reise2012] Reise, S. P. (2012). The rediscovery of bifactor measurement models. *Multivariate Behavioral Research, 47*(5), 667-696. [academic]
- [Rodriguez2016] Rodriguez, A., Reise, S. P., & Haviland, M. G. (2016). Evaluating bifactor models: Calculating and interpreting statistical indices. *Psychological Methods, 21*(2), 137-150. [academic]
- [Velicer1976] Velicer, W. F. (1976). Determining the number of components from the matrix of partial correlations. *Psychometrika, 41*(3), 321-327. [academic]
