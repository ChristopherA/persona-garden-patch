---
created: 2026-03-09
author: Christopher Allen
brief_summary: "Defines the Research form type: a living investigation that grows through active research, contains form-typed sections with their own predicates, and depletes as findings extract into standalone garden nodes. Distinguished from Reference (static briefing) by its depletion lifecycle and from Inquiry (poses questions) by containing evidence and analysis."
tagline: "What have I investigated about this question, and what did I find? — the structural contract for research forms"
formatted: "2026-03-14"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Research Form

**Core question**: "What have I investigated about this question, and what did I find?"

A living investigation that grows through active research. Contains form-typed sections — each section carries its own `is_a::` predicate identifying what kind of garden node it would become when extracted. The research form depletes over time: as findings extract into standalone garden nodes, the research note's value migrates outward. A fully extracted research note has done its job.

Distinguished from two related forms:

- **Reference Form** — a static briefing for lookup. References synthesize; research investigates. A reference answers "what do I need to know?" A research form answers "what did I find out?"
- **Inquiry Form** — poses questions and directs investigation. An inquiry drives a research form; the research form contains the evidence and analysis the inquiry called for.

The typical lifecycle: an Inquiry poses a question → a Research form investigates it → form-typed sections extract into standalone Models, Patterns, Glosses, Decisions → the Research form depletes, leaving provenance links.

## Structural Contract

A research form requires these sections in order:

1. **Overview** — What prompted this investigation, what question is being explored, and a provisional orientation. The overview frames but does not argue. "The answer appears to be X rather than Y" invites revision; a thesis resists it. State enough for the reader to follow the investigation without committing to a conclusion the findings haven't yet earned.

2. **Form-typed sections** — Each finding organized as a named section with its own `is_a::` predicate and structural contract. Sections use `### Form-Type: Descriptive Title` headings. Each section is independently extractable. Per-section `#### Sources` track evidence for that finding.

3. **Research Gaps** — Unanswered questions, areas needing further investigation. Well-defined gaps may become Inquiry forms.

4. **Sources** — Aggregated sources from all sections.

5. **Relations** — Note-level typed predicates connecting to other vault and garden nodes.

6. **Extracted Garden Nodes** — Extraction manifest using `source_of::` predicates. Lists all form-typed sections as extraction targets, tracking which have been extracted and which remain embedded.

Form-typed sections follow their target form type's structural contract. A section marked `is_a::[\[\[Pattern Form\]\]](Pattern%20Form.html)` should have Context, Forces, Solution, Consequences. A section marked `is_a::[\[\[Model Form\]\]](Model%20Form.html)` should have elements and relationships.

### Why Not Thesis-Driven

Academic papers argue a position: thesis → evidence → conclusion. Research forms investigate a question and produce garden nodes. The distinction matters:

- **A thesis biases toward confirmation.** Starting with a claim to defend shapes which findings get typed and which get overlooked. The garden's extraction model works better when findings are typed during synthesis, not filtered through a predetermined argument.
- **The "conclusion" is the extraction manifest.** Findings distribute across form-typed sections that become standalone nodes. There is no concluding section because the value migrates outward — the research form's job is to produce nodes, not to persuade.
- **Provisional framing replaces thesis.** The overview states a provisional read that may be revised as form-typed sections develop. This is closer to a working hypothesis than a thesis — it orients without constraining.

A research form that hardens into arguing a single position has probably found a Decision or Conviction, not more research to do.

### Naming Heuristic

Topic of investigation + architectural or domain framing. "Research Graphs and Precinct Architecture" not "Notes on Cornelius Article."

## Depletion Lifecycle

Research forms have a lifecycle distinct from other garden forms:

1. **Active** — Growing through investigation. New form-typed sections added as findings emerge. `has_status::[\[\[Growing Stage\]\]](Growing%20Stage.html)`.
2. **Extracting** — Findings stable enough to become standalone nodes. Individual sections extract via the `source_of::` / `extracted_from::` provenance pair. The extraction manifest tracks progress.
3. **Depleted** — Most or all form-typed sections have been extracted. The research note retains value as a provenance anchor (where did these nodes come from?) but no longer contains unique content. `has_status::[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)` — the note is complete, not abandoned.

A research form that never depletes may actually be a Reference — a static briefing that doesn't produce standalone nodes.

## Typical Predicates

- `is_a::[\[\[Research Form\]\]](Research%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)`, `[\[\[Growing Stage\]\]](Growing%20Stage.html)`, or `[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)`
- `in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`
- `source_of::[[Extracted Form]]↑` — tracks what was extracted from this research
- `extends::[\[\[Inquiry Form\]\]](Inquiry%20Form.html)` — the inquiry that drove this investigation
- `relates_to::[\[\[Citation Form\]\]](Citation%20Form.html)` — sources consulted during research

## Category

Generative form — research produces other garden nodes. Paired with Inquiry Form: inquiries pose questions, research forms investigate them.

## Location

Research Form nodes live in `Garden/research/`, parallel to other form-type subfolders.

### Operational Use Outside the Garden

The Research Form structure works for operational research placed in `Research/` rather than `Garden/research/`. In this mode, form-typed sections with `is_a::` predicates serve as structural labels organizing findings by knowledge type — but the sections are not extraction targets. The extraction manifest describes the document's structure without implying future garden node creation.

This dual mode reflects the form's portability: the structural contract (overview, form-typed sections, research gaps, sources, relations) organizes any investigation, whether it feeds the garden graph or serves a handoff.

## Exemplars

- [[Research Graphs and Precinct Architecture]]↑ — investigates whether research needs its own precinct, with 7 form-typed sections (garden use, extracting)
- [[Remote Session Multiplexing for macOS and iTerm2]]↑ — evaluates session persistence tools for handoff response, with 9 form-typed sections (operational use in Research/, non-extracting)

## Relations

- relates_to::[\[\[Inquiry Form\]\]](Inquiry%20Form.html)
  - Inquiries drive research; research answers inquiries. An inquiry may spawn multiple research forms.

- relates_to::[\[\[Reference Form\]\]](Reference%20Form.html)
  - References are static briefings; research forms are living investigations. Research may produce a Reference as a stable output.

- relates_to::[\[\[Citation Form\]\]](Citation%20Form.html)
  - Citations are evidence consumed by research. The research form's provenance chains connect through citations.

- relates_to::[[Extraction Model for Garden Migration]]↑
  - Research forms are primary extraction targets — the extraction model governs how form-typed sections become standalone nodes.

- relates_to::[\[\[Opus Form\]\]](Opus%20Form.html) — research findings may feed insights presented in opuses
