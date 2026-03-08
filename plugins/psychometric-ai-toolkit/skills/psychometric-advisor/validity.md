# Validity

Validity answers: "Are the decisions we make from scores justified?" Critically, validity is not a property of the test itself — it is a property of the **interpretations and uses** of test scores [Messick1995] [academic]. A test produces scores that are valid *for a specific purpose, in a specific population, under specific conditions*.

## Messick's Unified Validity Framework

Messick [Messick1995] [academic] argued the traditional split into independent "types" (content, criterion, construct) is fragmented. His unified framework treats **construct validity as the integrating force** — all evidence contributes to a single evaluation of whether score interpretations are defensible. Six aspects:

| Aspect | Question It Answers |
|--------|-------------------|
| **Content** | Do items representatively sample the domain? |
| **Substantive** | Are response processes consistent with the construct? |
| **Structural** | Does the internal structure match the theoretical model? |
| **Generalizability** | Do scores generalize across contexts, groups, and tasks? |
| **External** | Do scores relate to external criteria as theory predicts? |
| **Consequential** | Are there unintended consequences of score use? |

`[strong]` `[consensus]` — This framework is the dominant paradigm in modern psychometrics and is adopted by the AERA/APA/NCME Standards [AERA2014] [standards].

### Kane's Argument-Based Approach

Kane [Kane2013] [academic] operationalized Messick's ideas into a practical methodology. Instead of asking "is this test valid?", Kane asks: "what is the argument for using these scores this way?" His interpretation/use argument (IUA) chains four inferences — **Scoring** (observation to score), **Generalization** (score to universe score), **Extrapolation** (to target domain), **Implication** (to decision) — each requiring its own evidence. `[strong]`

## Content Validity

Content validity asks: does the assessment adequately sample the domain it claims to cover? This is established through **expert judgment**, not statistical analysis.

### Subject Matter Expert (SME) Panels

A panel of 5-10 domain experts independently rates each item on relevance, representativeness, and clarity. The standard quantitative index is **Lawshe's Content Validity Ratio** [Lawshe1975] [academic]:

```
CVR = (ne - N/2) / (N/2)

where:
  ne = number of experts rating the item "essential"
  N  = total number of experts on the panel
```

CVR ranges from -1 to +1. A positive value means more than half the experts rated the item essential. Critical values depend on panel size (e.g., CVR >= 0.75 for a 7-member panel at p < .05). Wilson, Pan, and Schumsky [Wilson2012] [academic] published corrected critical values addressing errors in Lawshe's original table.

## Criterion Validity

Criterion validity evaluates whether scores predict or correlate with an external outcome.

| Type | Design | Example |
|------|--------|---------|
| **Predictive** | Test now, measure criterion later | Selection test vs. job performance at 6 months |
| **Concurrent** | Test and criterion measured simultaneously | New scale vs. established measure |

**Metrics**: Pearson's *r* (continuous), AUC/ROC (binary). Benchmarks `[moderate]`: *r* >= .30 meaningful, *r* >= .40 strong for selection. Always report confidence intervals. Correct for restriction of range in pre-selected samples [AERA2014] [standards].

## Construct Validity

Construct validity is the overarching question: does the test measure the theoretical construct it claims to measure? Two classical methods come from Campbell and Fiske [CampbellFiske1959] [academic]:

### Convergent Validity

The test should correlate **positively and substantially** with other measures of the same construct, especially when measured by different methods. Example: a new conscientiousness scale should correlate *r* >= .50 with an established conscientiousness inventory.

### Discriminant Validity

The test should **not** correlate strongly with measures of theoretically distinct constructs. Example: a conscientiousness scale should correlate more weakly with extraversion measures than with other conscientiousness measures.

### Multitrait-Multimethod Matrix (MTMM)

Campbell and Fiske [CampbellFiske1959] [academic] introduced the MTMM matrix: cross multiple traits with multiple methods, then check that same-trait/different-method correlations (convergent) exceed different-trait/same-method correlations (discriminant). Modern practice often uses CFA to model MTMM data, handling method variance more rigorously. `[strong]`

## Face Validity

Face validity is whether the test **looks like** it measures what it claims, from the perspective of test-takers or stakeholders. It is not validity evidence in the psychometric sense — it is a perception.

Face validity matters for practical reasons: tests that appear irrelevant reduce motivation, increase complaints, and may face legal challenges in employment settings. But face validity alone proves nothing about whether the test actually works.

`[consensus]` — AERA/APA/NCME Standards [AERA2014] explicitly exclude face validity from the evidential basis of validity.

## Differential Item Functioning (DIF)

DIF analysis detects whether individual items behave differently across demographic groups (gender, ethnicity, language) after controlling for the trait being measured [HollandWainer1993] [academic]. An item shows DIF when equally-able members of different groups have different probabilities of answering correctly (or endorsing).

**Types**: Uniform DIF (one group consistently advantaged) vs. non-uniform DIF (advantage reverses across ability levels).

**Methods**: Mantel-Haenszel (uniform, large samples), logistic regression (both types), IRT-based (Lord's chi-square, Raju's area). ETS effect size classification for MH: A = negligible (|delta| < 1.0), B = moderate (1.0-1.5), C = large (>= 1.5, flag for review).

`[strong]` — DIF analysis is required by AERA/APA/NCME Standards for any assessment used across demographic groups.

## Measurement Invariance

Measurement invariance tests whether the entire measurement model functions equivalently across groups, using multi-group CFA in a sequential hierarchy [Vandenberg2000] [academic]:

| Level | Constrained | Required For |
|-------|------------|-------------|
| **Configural** | Same model structure | Any cross-group comparison |
| **Metric** | + factor loadings | Comparing correlations across groups |
| **Scalar** | + intercepts | Comparing group means |
| **Strict** | + residuals | Comparing observed scores directly |

Evaluate via delta-CFI (<= .01 suggests invariance holds) rather than chi-square, which is overpowered in large samples [Cheung2002] [academic]. Scalar invariance is the minimum for comparing means across groups. `[strong]`

## Decision Tree: What Validity Evidence Do I Need?

```
PURPOSE?
|
+-- SELECTION (hiring, admissions, certification)
|   +-- High-stakes? --> Content(CVR) + Criterion(predictive) + Construct
|   |                     + DIF + Invariance(scalar) + Adverse impact
|   +-- Low-stakes?  --> Content(SME) + Criterion(concurrent) + DIF
|
+-- DEVELOPMENT (coaching, feedback)
|   +-- Content(SME) + Construct(convergent) + Face(for buy-in)
|       + DIF if diverse population
|
+-- DIAGNOSIS (clinical, classification)
|   +-- Content + Criterion(vs gold standard) + Construct
|       + Classification accuracy(sens/spec) + DIF + Invariance
|
+-- RESEARCH (construct measurement)
    +-- Construct(CFA) + Invariance(if comparing groups) + Content
```

## Validation Study Design

Validation is not a one-time event — it is an ongoing program of evidence accumulation.

### Minimum Viable Validation

1. **Define the IUA** (Kane): what claims are you making about scores?
2. **Content evidence**: SME panel (min 5 experts), CVR, blueprint alignment
3. **Internal structure**: CFA confirming factor structure, reliability
4. **Convergent/discriminant**: correlations with established measures (N >= 200)
5. **DIF analysis**: gender and primary demographic groups (N >= 100 per group)
6. **Criterion evidence** (if selection): predictive or concurrent study

### Sample Sizes

CFA: min 200, recommended 300-500. Criterion: min 100, recommended 200+. DIF: min 100 per group. Measurement invariance: min 200 per group.

### Re-Validation Triggers

Population changes, item modifications, scoring model changes, 3-5 years elapsed, adverse impact signals in operational data.

## Anti-Patterns

### 1. "Face Validity Is Enough"

Face validity is perception, not evidence. Unstructured interviews have high face validity but low predictive validity. Cognitive ability tests seem irrelevant but predict strongly. Always collect actual validity evidence beyond appearance. `[consensus]`

### 2. Skipping DIF Analysis in Diverse Populations

No DIF analysis means no evidence of item fairness. Biased items produce score differences that reflect item properties, not true trait differences — leading to discriminatory decisions. Not optional for any assessment with legal exposure [HollandWainer1993] [academic]. `[strong]`

### 3. Validate Once and Never Re-Validate

Validity evidence has a shelf life. Populations change, items become dated, scoring models drift. The Standards [AERA2014] require evidence for each major interpretation and population. Build re-validation into the assessment lifecycle as a scheduled activity, not an afterthought.

## References

- `[Messick1995]` Messick, S. (1995). Validity of psychological assessment: Validation of inferences from persons' responses and performances as scientific inquiry into score meaning. *American Psychologist*, 50(9), 741-749. `[academic]`
- `[AERA2014]` American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). *Standards for Educational and Psychological Testing*. AERA. `[standards]`
- `[Kane2013]` Kane, M. T. (2013). Validating the interpretations and uses of test scores. *Journal of Educational Measurement*, 50(1), 1-73. `[academic]`
- `[CampbellFiske1959]` Campbell, D. T., & Fiske, D. W. (1959). Convergent and discriminant validation by the multitrait-multimethod matrix. *Psychological Bulletin*, 56(2), 81-105. `[academic]`
- `[HollandWainer1993]` Holland, P. W., & Wainer, H. (Eds.). (1993). *Differential Item Functioning*. Lawrence Erlbaum Associates. `[academic]`
- `[Lawshe1975]` Lawshe, C. H. (1975). A quantitative approach to content validity. *Personnel Psychology*, 28(4), 563-575. `[academic]`
- `[Wilson2012]` Wilson, F. R., Pan, W., & Schumsky, D. A. (2012). Recalculation of the critical values for Lawshe's content validity ratio. *Measurement and Evaluation in Counseling and Development*, 45(3), 197-210. `[academic]`
- `[Vandenberg2000]` Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature: Suggestions, practices, and recommendations for organizational research. *Organizational Research Methods*, 3(1), 4-70. `[academic]`
- `[Cheung2002]` Cheung, G. W., & Rensvold, R. B. (2002). Evaluating goodness-of-fit indexes for testing measurement invariance. *Structural Equation Modeling*, 9(2), 233-255. `[academic]`
