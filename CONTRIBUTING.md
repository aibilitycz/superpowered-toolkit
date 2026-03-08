# Contributing

Contributions to the Psychometric AI Toolkit are welcome. This document defines quality gates for knowledge contributions.

## What We Accept

- **Domain file improvements** — corrections, additional citations, refined decision trees
- **New anti-patterns** — with specific examples and psychometric justification
- **Citation updates** — newer studies that supersede or extend existing references
- **Bug fixes** — routing errors, typos, broken cross-references

## Quality Gates

Every knowledge contribution must meet these standards before merging.

### Domain Files (`skills/psychometric-advisor/*.md`)

| Requirement | Minimum |
|-------------|---------|
| Citations per file | 5 peer-reviewed sources (academic or standards body) |
| Decision trees | At least 1 per domain |
| Anti-patterns | 2-3 with concrete examples |
| Word count | 800-1500 words |
| Evidence markers | Every recommendation tagged: `[strong]`, `[moderate]`, `[emerging]`, or `[consensus]` |
| Source tags | Every citation tagged: `[academic]`, `[standards]`, or `[practitioner]` |

### Citation Standards

- **Prefer peer-reviewed sources** over practitioner blogs or grey literature
- **Include full reference** in the domain file's References section: `[AuthorYear]` Author(s). (Year). *Title*. Journal/Publisher. `[source-type]`
- **Add to `references.md`** — the master bibliography must stay in sync
- **Mark evidence strength honestly** — don't upgrade `[emerging]` to `[strong]` without meta-analytic support

### What Counts as Each Source Type

| Tag | Definition | Example |
|-----|-----------|---------|
| `[academic]` | Peer-reviewed journal, published book, conference proceedings | Embretson & Reise (2000) |
| `[standards]` | Professional standards body publication | AERA/APA/NCME Standards (2014) |
| `[practitioner]` | Industry blog, technical report, white paper | Aggregate practitioner reports |

### Skills and Agents

- Follow existing format exactly (frontmatter, sections, output templates)
- Workflow skills must reference specific domain files in Prerequisites
- Agents must specify model requirement and scope boundaries

## Process

1. Fork the repo
2. Create a branch (`fix/reliability-citation-update`)
3. Make changes following quality gates above
4. Submit a PR with:
   - What changed and why
   - Which domain files affected
   - Any new citations added (with full references)

## What We Don't Accept

- **Uncited claims** — every factual statement needs a source
- **Marketing language** — this is a technical reference, not a sales pitch
- **Proprietary methods** — only publicly available, verifiable approaches
- **AI-generated content without review** — LLMs can draft, but a human must verify citations exist and claims are accurate

## Updating Domain Files

When updating a domain file:

1. Check that existing citations still support the claims
2. Add new citations to both the domain file's References section AND `references.md`
3. Update any decision trees affected by new evidence
4. Verify word count stays within 800-1500 range
5. Run through the quality gates checklist above

## Questions

Open an issue on GitHub for questions about contribution standards.
