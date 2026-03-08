# I/O Psychology

Applied I/O psychology knowledge for assessment development: job analysis, competency modeling, selection methods, and adverse impact monitoring.

## Competency Modeling

A competency model defines the KSAOs (knowledge, skills, abilities, other characteristics) required for effective performance in a role.

**Core components:**

- **Behavioral indicators** — Observable actions that demonstrate a competency at a given level. Must be specific enough to rate ("Identifies stakeholder concerns before proposing solutions") not vague ("Good communicator"). [Campion2011] [strong]
- **Proficiency levels** — Typically 3-5 ordered tiers (e.g., Foundational, Proficient, Advanced, Expert). Each level has distinct behavioral indicators. Avoid more than 5 levels; raters cannot reliably distinguish finer gradations. [Campion2011] [moderate]
- **Competency frameworks** — Structured collections of 8-12 competencies organized by domain (cognitive, interpersonal, leadership). Fewer than 6 creates construct deficiency; more than 15 creates rater fatigue and overlap. [Campion2011] [strong]

**Key best practices** from [Campion2011]: Ground competencies in organizational strategy. Start with job analysis. Use multiple data sources (SMEs, incumbents, supervisors). Define behavioral indicators at each proficiency level. Validate against performance criteria.

## Job Analysis Methods

Job analysis is the foundation. Every defensible assessment traces back to it. [SackettLievens2008] [consensus]

| Method | When to Use | Limitations |
|--------|-------------|-------------|
| **Critical incidents** — SMEs describe effective/ineffective behavior episodes | Identifying behavioral indicators for competency models | Time-intensive; memorable-event bias |
| **Task analysis** — Systematic listing of tasks by frequency, importance, difficulty | Job descriptions; content validation | Misses emergent/contextual behaviors |
| **SME panels** — 6-12 experts rate KSAOs for relevance | Linking competencies to job requirements; legal defensibility | Composition bias; groupthink |
| **O\*NET** — US DoL occupational database with standardized descriptors | Initial scoping; cross-job comparisons; limited SME access | US-centric; may lag role evolution |

**Implementation rule:** Use at least two methods. Task analysis plus SME panels is the minimum defensible combination for selection assessments. [SackettLievens2008] [strong]

## Faking Resistance in Personnel Selection

Self-report personality measures are vulnerable to response distortion in high-stakes contexts. Candidates can and do elevate scores by 0.3-0.5 SD on socially desirable traits. [Morgeson2007] [strong]

**Countermeasures (ranked by evidence):**

1. **Forced-choice (MFC)** — Pair equally desirable statements; Thurstonian IRT recovers normative scores. Only format with strong faking resistance evidence. [strong]
2. **Social desirability scales** — Embedded scales (e.g., Paulhus BIDR) flag impression management. Useful as validity check but insufficient alone; score adjustments can introduce more error. [moderate]
3. **Warning statements** — Small effect (d ~ 0.1-0.2). Low cost, not sufficient alone. [moderate]
4. **Supervised retesting** — Re-administer to flagged candidates. Expensive but effective. [moderate]

For high-stakes selection use forced-choice; for development (low stakes) Likert is acceptable. [TettChristiansen2007] [strong]

## Adverse Impact

The 4/5ths (80%) rule: if the selection rate for a protected group is less than 80% of the rate for the highest-scoring group, adverse impact is indicated. [EEOC1978] [standards]

- **Cognitive ability tests** produce the largest group differences (d ~ 1.0 in US samples). High validity, high adverse impact. [SackettLievens2008] [strong]
- **Personality tests** produce small group differences (d < 0.15). Lower impact, lower validity. [Ones2007] [strong]
- **Structured interviews** offer a favorable validity-to-impact ratio. [SackettLievens2008] [moderate]
- **Forced-choice personality** may further reduce group differences vs. Likert. [emerging]

**Reducing adverse impact:** (1) Composite predictors (cognitive + personality + interview) rather than cognitive alone; (2) band-based scoring (scores within SEM treated as equivalent); (3) Pareto-optimal weighting to balance validity and group differences; (4) SJTs as cognitive ability supplements.

**Validity-diversity tradeoff:** Methods maximizing criterion validity (cognitive ability) tend to maximize adverse impact. The goal is the Pareto frontier — acceptable validity with minimal group differences. [SackettLievens2008] [strong]

## Performance Prediction

Criterion validity coefficients (corrected for range restriction and criterion unreliability):

| Predictor | Validity (r) | Adverse Impact | Evidence |
|-----------|-------------|----------------|----------|
| Cognitive ability (GMA) | .45-.65 | High | Strongest single predictor [SackettLievens2008] [strong] |
| Structured interviews | .40-.55 | Low-Moderate | Behavioral/situational Qs with anchored rubrics [strong] |
| Conscientiousness | .20-.25 | Very Low | Best Big Five predictor across jobs [Ones2007] [strong] |
| Assessment centers | .35-.45 | Moderate | Multiple exercises, trained assessors [strong] |
| Job knowledge tests | .45-.55 | Moderate-High | Best for experienced hires [moderate] |
| Unstructured interviews | .15-.25 | Variable | Not recommended; low reliability [strong] |

Personality adds 5-10% incremental variance beyond cognitive ability. Small per-decision, meaningful at scale. [Ones2007] [strong]

## 360-Degree Feedback

Multi-source assessment collects ratings from self, supervisor, peers, and direct reports.

- **Rater groups:** Minimum 3 peers and 3 direct reports for adequate reliability. [consensus]
- **Rater agreement:** Within-source reliability is .50-.60 (peers), .35-.45 (subordinates). Cross-source correlations are lower (.20-.35) — expected, since different raters observe different behaviors. [moderate]
- **Self-other discrepancy:** Self-ratings average 0.5-0.8 SD higher than other-ratings. The gap is largest for poor performers and is itself a useful development signal. [strong]
- **Purpose:** 360 is a development tool, not a selection tool. Using it for pay/promotion distorts rater honesty. [consensus]

## Assessment Centers

Assessment centers use multiple simulation exercises (in-basket, role-play, group discussion, presentation) evaluated by trained assessors against predefined competency dimensions.

**Design:** Minimum 3 exercises; each competency in 2+ exercises; assessor ratio 1:2 max; ORCE training (Observe, Record, Classify, Evaluate).

**MTMM concern:** Ratings correlate more across competencies within exercises (method effects) than across exercises for the same competency (trait effects). Mitigate with BARS, separating observation from evaluation, or exercise-based scoring. [SackettLievens2008] [strong]

## Workplace Personality Assessment

**Big Five in selection:** Conscientiousness is valid across most jobs (task performance, training) [Ones2007] [strong]. Emotional Stability predicts CWB and stress tolerance [moderate]. Agreeableness and Extraversion are valid for interpersonal and social/leadership roles respectively [moderate]. Openness is a weak general predictor [moderate].

**Bandwidth-fidelity dilemma** [TettChristiansen2007]: Broad traits (Big Five) predict broad criteria but miss specific behaviors. Narrow facets (e.g., Achievement Striving) predict specific criteria better but risk capitalizing on chance. Match predictor bandwidth to criterion bandwidth.

**Trait activation theory** [TettChristiansen2007]: Traits predict performance only when the situation activates them. Extraversion predicts sales performance but not isolated analytical roles. Always link personality constructs to job-relevant situational demands via job analysis.

## Decision Tree: Which Assessment Method?

```
What is the primary HR purpose?
|
+-- SELECTION (hiring / promotion)
|   |
|   +-- Is cognitive ability critical to the role?
|   |   |
|   |   +-- YES --> Cognitive test + structured interview
|   |   |           + personality (forced-choice) as supplement
|   |   |           Monitor adverse impact [strong]
|   |   |
|   |   +-- NO  --> Structured interview + forced-choice personality
|   |               + SJT or work sample [strong]
|   |
|   +-- Is the role leadership / senior?
|       |
|       +-- YES --> Assessment center (3+ exercises)
|       |           + structured interview + personality [strong]
|       |
|       +-- NO  --> See cognitive ability branch above
|
+-- DEVELOPMENT (coaching / growth)
|   |
|   +-- 360-degree feedback (multi-source)
|   |   + Likert personality (faking less relevant)
|   |   + Developmental assessment center (feedback-focused)
|   |   Do NOT use results for pay/promotion [consensus]
|
+-- SUCCESSION PLANNING
    |
    +-- Assessment center (high-fidelity simulations)
    |   + Cognitive ability screen
    |   + 360-degree feedback (from current role)
    |   + Personality profile (bandwidth matched to target role)
    |   Weight potential indicators over current performance [moderate]
```

## Anti-Patterns

### 1. Self-report personality for high-stakes selection without faking controls

Deploying Likert-based Big Five for hiring without forced-choice, SD checks, or warnings. Candidates inflate scores 0.3-0.5 SD, changing rank-ordering and penalizing honest respondents. **Fix:** Use MFC with Thurstonian IRT scoring for selection; reserve Likert for development. [Morgeson2007] [strong]

### 2. Ignoring adverse impact until post-deployment

Checking group differences only after legal challenge. Retrofitting (changing cutoffs, reweighting, replacing predictors) is more expensive and legally risky than proactive design. **Fix:** Run adverse impact simulations during design using pilot data. Document as part of the validation report. [SackettLievens2008] [consensus]

### 3. Building competency models without job analysis

Defining competencies from executive intuition or copying another organization's model. Without job analysis, models lack content validity and legal defensibility. **Fix:** Start with task analysis + SME panels. Map each competency to job requirements. Validate against performance criteria. [Campion2011] [strong]

## References

- `[Campion2011]` Campion, M. A., Fink, A. A., Ruggeberg, B. J., Carr, L., Phillips, G. M., & Odman, R. B. (2011). Doing competencies well: Best practices in competency modeling. *Personnel Psychology, 64*(1), 225-262. `[academic]`
- `[EEOC1978]` Equal Employment Opportunity Commission. (1978). Uniform Guidelines on Employee Selection Procedures. *Federal Register, 43*, 38290-38315. `[standards]`
- `[Morgeson2007]` Morgeson, F. P., Campion, M. A., Dipboye, R. L., Hollenbeck, J. R., Murphy, K., & Schmitt, N. (2007). Reconsidering the use of personality tests in personnel selection contexts. *Personnel Psychology, 60*(3), 683-729. `[academic]`
- `[Ones2007]` Ones, D. S., Dilchert, S., Viswesvaran, C., & Judge, T. A. (2007). In support of personality assessment in organizational settings. *Personnel Psychology, 60*(4), 995-1027. `[academic]`
- `[SackettLievens2008]` Sackett, P. R., & Lievens, F. (2008). Personnel selection. *Annual Review of Psychology, 59*, 419-450. `[academic]`
- `[TettChristiansen2007]` Tett, R. P., & Christiansen, N. D. (2007). Personality tests at the crossroads: A response to Morgeson, Campion, Dipboye, Hollenbeck, Murphy, and Schmitt (2007). *Personnel Psychology, 60*(4), 967-993. `[academic]`
- `[SIOP2018]` Society for Industrial and Organizational Psychology. (2018). *Principles for the Validation and Use of Personnel Selection Procedures* (5th ed.). `[standards]`
