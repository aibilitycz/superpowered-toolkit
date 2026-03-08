# Assessment Ethics & Standards

Ethical and legal requirements for building, deploying, and maintaining assessments. Covers professional standards, fairness, privacy, AI obligations, and cross-cultural adaptation.

## Professional Testing Standards

### APA/AERA/NCME Standards (2014) [standards]

The *Standards* [AERA2014] are the primary authority for assessment quality. The 2014 edition elevated fairness to a foundational concern alongside validity and reliability:

- **Validity evidence is mandatory** -- document content, response process, internal structure, relations to other variables, and consequences of testing (Standard 1.0) `[consensus]`
- **Fairness throughout the lifecycle** -- all steps (design, validation, administration, scoring) must minimize construct-irrelevant variance for all examinees (Chapter 3) `[consensus]`
- **Documentation obligations** -- provide a technical manual covering reliability, validity, norming, scoring, and intended uses (Standard 7.4) `[consensus]`
- **Score interpretation boundaries** -- state what scores mean, what they do not mean, and generalizability limits (Standard 1.1-1.8) `[strong]`
- **Test user qualifications** -- specify required competence for administration, scoring, and interpretation (Standard 9.1) `[consensus]`

### ITC Guidelines for Test Use (2013) [standards]

The ITC Guidelines [ITC2013] define test user responsibilities internationally:

- **Evaluate suitability** -- confirm testing is appropriate for the stated goal before administration `[consensus]`
- **Competence requirement** -- test users must understand psychometric principles, the specific test, and the target population `[consensus]`
- **Rights of test-takers** -- informed consent, feedback on results, protection from score misuse `[strong]`
- **Score fairness** -- verify that use and interpretation are fair across demographic groups `[consensus]`

## Fairness in Testing

### Bias Detection and Adverse Impact

**Differential Item Functioning (DIF):** Items must be analyzed for DIF -- statistical differences in item performance between groups after controlling for ability. DIF detection is a validity requirement, not optional [AERA2014, Standard 3.6]. `[consensus]`

**Adverse Impact and the 4/5ths Rule:** The EEOC Uniform Guidelines [EEOC1978] define adverse impact: a selection rate for any group below 80% of the highest group's rate is prima facie evidence of adverse impact. `[consensus]`

Caveats:
- The 4/5ths rule is a screening heuristic, not a safe harbor -- passing does not guarantee compliance
- Smaller differences may constitute adverse impact when statistically significant
- When adverse impact is found, validate against job-relevant criteria
- Supplement with significance tests (Fisher exact, chi-square) for small samples `[strong]`

Run adverse impact analyses before deployment, after norming, and at regular post-deployment intervals.

### Accommodations and Accessibility

Assessments must be accessible to individuals with disabilities [AERA2014, Ch. 3]. `[consensus]`

- **Reasonable adjustments** -- extended time, alternative formats, modified response modes
- **Construct preservation** -- accommodations must not alter the construct measured
- **Universal design** -- reduce the need for accommodations (clear fonts, sufficient contrast, simple navigation)
- **Flagging** -- current best practice trends toward non-flagging when equivalence is demonstrated `[moderate]`

## Informed Consent

Minimum disclosure requirements [AERA2014, Standard 8.4; ITC2013; GDPR Art. 13-14]:

| Must Disclose | Example |
|---|---|
| Purpose of assessment | "Measures problem-solving style for hiring decisions" |
| What is measured | Constructs (cognitive ability, personality traits) |
| How scores are used | Selection, development, placement |
| Who accesses results | HR, hiring manager, third-party vendor |
| Data retention period | "Stored 12 months, then deleted" |
| Right to withdraw | Voluntary participation; consequences of withdrawal |
| AI involvement | Whether AI/algorithms contribute to scoring |
| Right to feedback | How and when results are available |

## Data Privacy (GDPR)

Assessment data is personal data under GDPR. Personality and cognitive results may constitute profiling data.

**Article 22 -- Automated Decision-Making:** Individuals have the right not to be subject to decisions based solely on automated processing producing legal or significant effects. Assessment-based hiring with automated scoring likely triggers Art. 22. Safeguards required: human intervention, right to express a view, right to contest. `[strong]`

**Right to Explanation (Art. 13-15, Recital 71):** Data subjects must receive "meaningful information about the logic involved" -- explain scoring methodology comprehensibly, not just "you scored 45/100." `[strong]`

**DPIA:** Required before deploying automated assessment systems producing legal or significant effects (Art. 35). `[consensus]`

**Retention:** Define proportional retention periods. Implement automated deletion. Honor right to erasure (Art. 17).

## AI Ethics in Assessment

### Transparency of AI Scoring

When AI (including LLMs) contributes to scoring, additional obligations apply [AERA2014; EUAI2024; GDPR Art. 22]. `[emerging]`

Disclose: that AI is involved (to test-takers and purchasers), the AI's role (sole scorer, co-rater, quality layer), validation evidence, and known limitations.

**Right to human review:** For high-stakes decisions, provide human review of AI scores on request. Legally required under GDPR Art. 22 and the EU AI Act for high-risk systems. `[strong]`

### EU AI Act (2024) [standards]

The EU AI Act [EUAI2024] classifies AI in employment and education as **high-risk** (Annex III):

- **Category 3 -- Education:** AI evaluating learning outcomes, assessing education level, monitoring behavior during tests
- **Category 4 -- Employment:** AI for recruitment, performance evaluation, task allocation

High-risk compliance: risk management (Art. 9), data governance (Art. 10), technical documentation (Art. 11), logging (Art. 12), transparency (Art. 13), human oversight (Art. 14), accuracy/robustness (Art. 15), conformity assessment (Art. 43). **Applicable August 2026.**

## Test Security

| Threat | Mitigation |
|---|---|
| Item exposure | Item banking with rotation; exposure monitoring; adaptive testing |
| Pre-knowledge | Large item pools; randomized selection; proctoring |
| Impersonation | Identity verification; proctoring; IP logging |
| Unauthorized aids | Calibrated time limits; secure browser; clipboard disabled |

ITC Guidelines on Computer-Based Testing [Bartram2001] require equivalence evidence for digital formats, authentication, encryption, and audit trails. `[strong]`

## Cultural Sensitivity

### ITC Guidelines for Translating and Adapting Tests (2017) [standards]

The ITC adaptation guidelines [ITC2017] provide 18 guidelines across six phases: `[consensus]`

1. **Pre-condition** -- evaluate construct equivalence across cultures before adapting
2. **Test Development** -- forward-backward translation with reconciliation; target-culture SMEs
3. **Confirmation** -- empirical equivalence evidence (measurement invariance, DIF, reliability)
4. **Administration** -- comparable conditions across sites
5. **Scoring/Interpretation** -- develop local norms; do not assume source norms transfer
6. **Documentation** -- record all adaptation decisions and limitations

Key principles: construct equivalence precedes translation; linguistic accuracy does not guarantee psychometric equivalence; bias operates at item, method, and construct levels [VanDeVijver2004]. `[strong]`

## Decision Tree: What Requirements Apply?

```
START: Assessment purpose?
|
+---> Employment selection / promotion
|     +-- US jurisdiction?
|     |   +- YES -> EEOC Guidelines [EEOC1978]: 4/5ths rule,
|     |   |         adverse impact analysis, criterion validity
|     |   +- NO  -> Check local employment law
|     |
|     +-- EU/EEA jurisdiction?
|     |   +- YES -> GDPR Art. 22 (automated decisions)
|     |   |         EU AI Act HIGH-RISK (Annex III, Cat. 4)
|     |   |         DPIA required; human review mandatory
|     |   +- NO  -> Check local data protection law
|     |
|     +-- AI in scoring?
|         +- YES -> Disclose to test-takers
|         |         Validate AI (inter-rater agreement)
|         |         Provide human review option
|         |         If EU: full AI Act compliance
|         +- NO  -> Standard psychometric validation
|
+---> Education (admissions, placement, grading)
|     +-- EU? -> HIGH-RISK (Annex III, Cat. 3)
|     |          Same GDPR/DPIA as employment
|     +-- AI?  -> Same AI branch as above
|
+---> Development / coaching (low-stakes)
|     +-- Informed consent still required
|     +-- GDPR still applies if EU
|     +-- EU AI Act: likely NOT high-risk (unless feeding
|         employment decisions)
|
+---> Research
      +-- IRB/ethics committee approval
      +-- Consent with right to withdraw
      +-- Data minimization and anonymization
      +-- Cannot repurpose other data without consent
```

**Always applicable:** AERA2014 Standards, ITC Test Use, informed consent, fairness analysis, ITC Adaptation if cross-cultural.

## Anti-Patterns

| Anti-Pattern | Why Harmful | Do Instead |
|---|---|---|
| **Deploying AI scoring without disclosure** | Violates GDPR transparency, EU AI Act Art. 13, professional ethics. Erodes trust. Invites enforcement. | Disclose AI in consent materials. Explain role and validation. Provide human review. |
| **Using assessment data beyond stated purpose** | Violates GDPR purpose limitation (Art. 5(1)(b)). May constitute unauthorized profiling. | Obtain separate consent per purpose. Implement technical controls against scope creep. |
| **Assuming one norm group fits all populations** | Produces systematically biased scores. Violates fairness [AERA2014 Ch. 3]. Causes adverse impact. | Test measurement invariance. Develop local norms or demonstrate equivalence. Run DIF. |

## References

| Key | Source | Type |
|---|---|---|
| [AERA2014] | AERA, APA, & NCME. (2014). *Standards for Educational and Psychological Testing*. AERA. | `[standards]` |
| [ITC2013] | International Test Commission. (2013). *ITC Guidelines on Test Use*. | `[standards]` |
| [ITC2017] | International Test Commission. (2017). *ITC Guidelines for Translating and Adapting Tests* (2nd ed.). | `[standards]` |
| [EEOC1978] | EEOC. (1978). *Uniform Guidelines on Employee Selection Procedures*. 29 CFR 1607. | `[standards]` |
| [EUAI2024] | EU. (2024). *Regulation 2024/1689 -- Artificial Intelligence Act*. OJ EU. | `[standards]` |
| [Bartram2001] | Bartram, D. (2001). ITC Guidelines on Computer-Based and Internet Delivered Testing. | `[practitioner]` |
| [VanDeVijver2004] | Van de Vijver, F. & Tanzer, N. (2004). Bias and equivalence in cross-cultural assessment. *Eur. Rev. Appl. Psychol., 54*(2), 119-135. | `[academic]` |
| [GDPR2016] | EU. (2016). *Regulation 2016/679 -- General Data Protection Regulation*. OJ EU. | `[standards]` |
