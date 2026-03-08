# AI-Based Assessment

Using LLMs to score open-ended assessment responses. This is a nascent field --- most evidence is emerging or moderate. Be skeptical of strong claims and validate empirically in your own context.

---

## LLM-as-Judge Paradigm

Replace or supplement human raters with LLM calls that evaluate responses against a scoring rubric. Zheng et al. showed strong LLM judges achieve >80% agreement with human preferences, matching inter-human agreement [Zheng2023]. `[moderate]`

This does NOT mean LLMs are interchangeable with trained human raters. MT-Bench evaluates general quality preferences, not construct-aligned behavioral scoring. Transfer to structured assessment requires rubric grounding, calibration, and agreement measurement specific to your construct.

**Works well:** Behavioral descriptions, situational responses, written reflections scored against well-defined rubrics with distinct levels.

**Struggles:** Highly nuanced constructs, culture-specific behavioral norms, deep domain expertise, ambiguous rubric levels.

---

## Calibration Methods

### Few-Shot Exemplars

Provide 2-5 scored examples per rubric level. Few-shot outperforms zero-shot by ~12.6% accuracy in science assessment scoring [Lee2024]. `[moderate]` Include one clear example per level, choose consensus cases, and add one borderline case with explicit reasoning.

### Rubric-Grounded Prompting

Embed the full rubric with behavioral anchors in the prompt. Prometheus shows rubric-grounded evaluation achieves Pearson r = 0.897 with human evaluators [Kim2024]. `[moderate]`

### Calibration Sets

Reserve 50-100 human-scored responses. Score them with your LLM pipeline, compute agreement (QWK, ICC), and iterate on prompts/exemplars until agreement meets your target. Analogous to rater certification in traditional assessment.

---

## Ensemble Scoring

A single LLM call is noisy. Even at temperature 0, outputs are not perfectly deterministic. `[emerging]`

| Method | How | When to Use |
|--------|-----|-------------|
| **Modal score** | N passes (3-5), take mode | Categorical rubric levels |
| **Mean score** | Average N passes | Continuous scales |
| **Multi-model panel** | 2-3 different models, aggregate | High-stakes, bias reduction |
| **Weighted voting** | Weight by calibration-set agreement | Known performance differences |

**Rules of thumb:** Minimum 3 passes for consequential decisions. 5 passes for high-stakes. Temperature 0 always. Ensemble does NOT fix systematic bias --- if the rubric is misinterpreted, all passes err the same way. High within-ensemble variance signals ambiguous rubric levels.

---

## Hybrid Scoring Pipelines (L1 + L2)

Combine structured items (L1) with LLM-scored behavioral observation (L2).

- **L1**: Forced-choice, Likert, SJT with keyed responses. Deterministic scoring. High reliability, low cost.
- **L2**: Free-text behavioral prompts. LLM-scored against rubrics. Richer signal, higher cost, requires calibration.

```
Response --> L1 items --> deterministic scoring --> L1 scores --+
         |                                                      |
         +-> L2 items --> prompt + rubric + exemplars            +--> Composite
                          --> N parallel LLM calls (ensemble)   |
                          --> aggregation --> L2 scores ---------+
```

Weight allocation should be empirically derived from validity evidence. Start L1-dominant (e.g., 70/30) and adjust based on incremental validity of L2 for predicting your criterion. `[emerging]`

---

## Inter-Rater Agreement with AI Scorers

Treat the LLM as another rater. Apply standard metrics:

| Metric | Use Case | Acceptable Threshold |
|--------|----------|---------------------|
| **QWK** | Ordinal rubric scales | >= 0.60 moderate, >= 0.80 strong |
| **ICC (two-way mixed)** | Continuous scores | >= 0.75 good, >= 0.90 excellent |
| **Adjacent agreement %** | Off-by-one tolerance | >= 85% |

Tang et al. found GPT-4 achieved QWK = 0.57 vs. human-human QWK = 0.66 on analytic rubrics [Tang2024]. The gap is meaningful --- LLMs approach but do not yet match trained human raters. `[moderate]`

**Critical distinction:** LLM self-consistency (ICC = 0.97 across repeated runs) measures test-retest consistency of the model, NOT agreement with a construct-valid human standard.

---

## Rubric Design for LLM Scoring

1. **Behavioral anchors, not trait labels.** "Describes specific actions and outcomes" not "Shows strategic thinking."
2. **Distinct, non-overlapping levels.** If humans cannot distinguish levels 2 and 3, the LLM will not either.
3. **3-5 levels maximum.** Finer gradations reduce reliability without proportional gain.
4. **Explicit boundary conditions.** State what moves a response from level N to N+1.
5. **Negative anchors.** Define what each level is NOT.

```
Dimension: [construct name]
Definition: [1-2 sentence behavioral definition]

Score 1 - [label]: [description]. Indicators: [list]. NOT this level if: [condition]
Score 2 - [label]: [description]. Indicators: [list]. NOT this level if: [condition]
...
Score 5 - [label]: [description]. Indicators: [list].
```

---

## Prompt Engineering for Assessment

**Structured output:** Always request JSON for reliable parsing: `{"score": <1-5>, "reasoning": "...", "evidence": "..."}`

**Chain-of-thought scoring:** Require reasoning before scoring. CoT increases zero-shot accuracy by 13.4% [Lee2024]. `[moderate]` Pattern: (1) restate rubric criteria, (2) identify evidence in response, (3) compare against each level, (4) assign score with justification.

**Rubric embedding:** Include the complete rubric in every call. Never rely on the LLM's implicit knowledge of quality.

---

## Quality Assurance

### Monitoring Scorer Drift

LLM behavior changes with model updates. Without monitoring, error rates can increase 35% over 6 months [Practitioner2025]. `[emerging]`

1. Maintain 50-100 human-scored calibration responses as a fixed benchmark
2. Re-score calibration set weekly or after any model/prompt change
3. Alert if QWK drops >0.05 from baseline or mean score shifts >0.3 SD
4. Quarterly: have humans re-score a subset to validate the calibration set itself

**Log every scoring call:** prompt hash, model version, temperature, raw output, parsed score, response ID.

---

## Bias and Fairness

LLMs can infer demographics from writing style and introduce bias. Scoring errors for non-native speakers increase when the LLM correctly identifies them as non-native [Dong2025]. `[emerging]`

**Known bias vectors:** language variety (L2 underscoring), verbosity bias (longer = higher), position bias in pairwise comparisons, self-enhancement [Zheng2023].

**Mitigation:** (1) DIF analysis across demographic groups, (2) strip identifiers before scoring, (3) instruct LLM to evaluate only construct-relevant behaviors, (4) adversarial testing with equivalent content in different language varieties, (5) human audit samples per demographic group.

---

## Decision Tree: Should I Use AI Scoring?

```
Is the response open-ended (free text, behavioral description)?
|
+-- No --> Use deterministic scoring
|
+-- Yes
    |
    What are the stakes?
    |
    +-- Low (research, development)
    |   |
    |   Rubric with behavioral anchors available?
    |   +-- No --> Write the rubric first (see Rubric Design)
    |   +-- Yes --> AI scoring appropriate
    |              3-pass ensemble, QWK >= 0.60, monthly calibration
    |
    +-- Moderate (screening, formative)
    |   |
    |   Rubric available AND >= 50 human-scored calibration responses?
    |   +-- No --> Collect calibration data first
    |   +-- Yes --> AI scoring with safeguards
    |              5-pass ensemble, QWK >= 0.70
    |              Human review of borderline cases, weekly calibration, DIF
    |
    +-- High (selection, certification)
        |
        >= 200 human-scored responses with established inter-rater reliability?
        +-- No --> Do not use AI as sole scorer
        +-- Yes
            |
            LLM-human QWK matches human-human QWK (within 0.05)?
            +-- No --> Do not use AI as sole scorer
            +-- Yes --> AI acceptable as ONE input in hybrid pipeline
                        5-pass multi-model ensemble
                        Human second-scoring of all consequential decisions
                        Continuous drift detection, quarterly DIF audit
```

---

## Anti-Patterns

**1. Single LLM call without calibration for high-stakes scoring.** A single uncalibrated call has unknown reliability and unknown bias --- psychometrically indefensible for consequential decisions. Always calibrate against human-scored data and use ensemble scoring. Budget for the 3-5x cost multiplier.

**2. Not measuring LLM-human inter-rater agreement.** Teams deploy LLM scoring assuming it works because outputs "look reasonable." Without QWK or ICC against human standards, there is no evidence the LLM measures the intended construct. Treat deployment like rater certification: compute agreement, set thresholds, monitor continuously.

**3. Treating LLM confidence as psychometric reliability.** Log-probabilities and self-reported confidence ("I am 90% sure this is a 4") reflect token prediction probability, not measurement precision. A model can be highly confident while systematically wrong. Reliability must be computed from score data using ICC, alpha, or omega. LLM confidence is useful for routing borderline cases to human review --- nothing more.

---

## Evidence Gaps

- **Long-term drift**: Few systems have published longitudinal LLM scorer stability data `[emerging]`
- **Construct validity**: Most studies use agreement metrics, not convergent/discriminant validity `[emerging]`
- **Cross-cultural fairness**: Nearly all research uses English from Western contexts `[emerging]`
- **Optimal ensemble size**: 3-5 passes is practitioner consensus, not empirically optimized `[emerging]`
- **Hybrid weighting**: No published studies compare L1+L2 weighting strategies `[emerging]`

The AERA/APA/NCME Joint Committee announced a Standards revision in 2024 addressing AI in testing, but no updated guidance is published yet [AERA2024]. `[emerging]`

---

## References

- `[Zheng2023]` Zheng, L. et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS 36*. `[academic]`
- `[Kim2024]` Kim, S. et al. (2024). Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models. *ICLR 2024*. `[academic]`
- `[Lee2024]` Lee, G., Latif, E., Wu, X., Liu, N., & Zhai, X. (2024). Applying large language models and chain-of-thought for automatic scoring. *Computers and Education: AI, 6*, 100213. `[academic]`
- `[Tang2024]` Tang, X., Chen, H., Lin, D., & Li, K. (2024). Harnessing LLMs for multi-dimensional writing assessment. *Heliyon, 10*(14), e34262. `[academic]`
- `[Dong2025]` Dong, Y., Li, Y., & Zhai, X. (2025). Does the Prompt-based LLM Recognize Students' Demographics and Introduce Bias in Essay Scoring? *arXiv:2504.21330*. `[academic]`
- `[AERA2014]` AERA, APA, & NCME. (2014). *Standards for Educational and Psychological Testing*. `[standards]`
- `[AERA2024]` AERA, APA, & NCME Joint Committee. (2024). Standards Revision Committee announcement. `[standards]`
- `[Practitioner2025]` Aggregate practitioner reports on LLM monitoring in production assessment systems (2024-2025). `[practitioner]`
