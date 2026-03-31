---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Model form type: a structural representation showing elements, relationships, boundaries, and feedback loops. How things relate to each other. Evolving as understanding grows. Models are explanatory (how things work), distinct from patterns (what to do) and scenarios (what might happen)."
tagline: "How do these elements relate to each other? — the structural contract for model forms"
---

- is_a::[Form Type](Form%20Type.html)
- has_status::[Seed Stage](Seed%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Model Form

**Core question**: "How do these elements relate to each other?"

A structural representation — elements, relationships, boundaries, feedback loops. Models show how things relate, not what to do about them. Evolving; updated as understanding grows.

## Structural Contract

A model form requires:

- **Introductory framing** — What the model represents and why it matters. State the value proposition.
- **Structure** — The elements and their relationships. Often includes a mapping table showing correspondence between abstract concepts and concrete implementation.
- **Boundaries** — Where the model applies and where it breaks down.
- **Sources** — Origin material the model was derived from.
- **Relations** — Connections to principles it supports, patterns it contextualizes, and decisions it informs.

Naming heuristic: value proposition + structure metaphor. "Compound Node Anatomy" not "Compound Node Model."

## Typical Predicates

- `is_a::[Model Form](Model%20Form.html)`
- `has_status::[Seed Stage](Seed%20Stage.html)` or `[Growing Stage](Growing%20Stage.html)`
- `in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)`
- `depends_on::[[Foundational Concept]]↑` — prerequisites
- `implements::[Decision Form](Decision%20Form.html)` — operationalizes a decision
- `relates_to::[Principle Form](Principle%20Form.html)`, `[Boundary Form](Boundary%20Form.html)`, `[Pattern Form](Pattern%20Form.html)`

## Compound Collection Usage

A Model Form node can serve as the parent index of a compound folder containing other form-typed nodes. In this usage, the model describes the collection's organizing structure — categories, relationships between groups, and the collection's boundaries — while individual nodes within the folder carry their own form types (typically Pattern Form). Category and subcategory nodes within the collection are themselves Model Form nodes, creating a hierarchy of models indexing patterns.

This usage relies on two predicates: `in_collection::` binds individual nodes to their parent model, and `in_category::` binds nodes to their category model. Categories are flat nodes in the same compound folder, not filesystem subfolders.

See [[Model Form as Pattern Language Index]]↑ for the architectural decision and [[Patterns of Cooperative Play]]↑ for the first concrete instance (152 patterns across 10 categories, 177 files).

## Exemplars

- [[Compound Node Anatomy]]↑ — mapping table between abstract structure and vault implementation
- [[Principal-Agent Relationship in Augmented Knowledge Work]]↑ — multi-level model with conferral mechanisms
- [[Personal Knowledge Management Organizing Principle Spectrum]]↑ — comparative model positioning approaches along an axis
- [[Sycophantic Confidence Spiral]]↑ — feedback loop model with empirical measurements
- [[Vocabulary Lifecycle Through Tending]]↑ — cross-domain mechanism model with instance mapping table
- [[Patterns of Cooperative Play]]↑ — compound collection parent indexing 152 Pattern Form nodes via category Model Form nodes

## Category

Structural form — captures *how things relate* and *what we understand*.

## Sources

Definition from [Deep Context as an Architecture for Captured Reasoning](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 59-60.

## Relations

- relates_to::[Pattern Form](Pattern%20Form.html) — patterns operate within the structural context models describe
- relates_to::[Principle Form](Principle%20Form.html) — principles constrain models; models show where principles apply
- relates_to::[Gloss Form](Gloss%20Form.html) — glosses interpret concepts that models structure
- relates_to::[Boundary Form](Boundary%20Form.html) — boundaries define authority zones that models map
