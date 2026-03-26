---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Reference form type: a comprehensive briefing synthesizing multiple sources and forms into a coherent domain picture. May contain model-like tables, principle-like recommendations, and gloss-like interpretations. Source docs in Research/ carry this type."
tagline: "What do I need to know about this domain to act effectively? — the structural contract for reference forms"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Reference Form

**Core question**: "What do I need to know about this domain to act effectively?"

A comprehensive briefing synthesizing multiple sources and forms into a coherent domain picture. May contain model-like tables, principle-like recommendations, and gloss-like interpretations. Evolving; updated as the domain changes.

References are containers — they hold content that spans multiple form types. Their value is as stable briefings: comprehensive, updated as the domain changes, but not structured for extraction.

Distinguished from Research Form: a reference synthesizes what's known for lookup; a research form investigates a question and depletes as findings extract into standalone nodes. If a document has an extraction manifest and form-typed sections, it's a Research Form. If it's a comprehensive briefing you look things up in, it's a Reference.

## Structural Contract

A reference form has flexible structure but typically includes:

- **Overview** — What domain this reference covers and why it matters.
- **Content sections** — Organized by topic, not by form type. May contain model-like tables, principle-like constraints, pattern-like solutions, and gloss-like interpretations.
- **Sources** — Materials synthesized into this reference.
- **Relations** — Connections to garden nodes extracted from this reference and to related domains.

References do not have a rigid section order like decisions or patterns. Their value is comprehensiveness, not structural consistency.

Naming heuristic: descriptive scope. Name what's covered, not what's concluded. "Structural Elements Within Forms" not "Why Some Knowledge Types Aren't Forms."

## Typical Predicates

- `is_a::[\[\[Reference Form\]\]](Reference%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Growing Stage\]\]](Growing%20Stage.html)`
- `in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`
- `source_of::[[Related Form]]↑` — when a reference informs other nodes (less common than in Research Form)

## Current Usage

Some source documents in `Research/deep-context-architecture/` carry `is_a::[\[\[Reference Form\]\]](Reference%20Form.html)`. Documents with extraction manifests and form-typed sections should be reclassified as `is_a::[\[\[Research Form\]\]](Research%20Form.html)`. Static briefing documents (naming conventions, product requirements) remain as References.

## Category

Structural form — captures *how things relate* and *what we understand*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 62-63.

## Relations

- relates_to::[\[\[Gloss Form\]\]](Gloss%20Form.html) — references contain gloss-like interpretations that can be extracted
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — references contain model-like tables that can be extracted
- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — references contain decisions that can be extracted
- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — references contain pattern-like solutions that can be extracted
- relates_to::[\[\[Research Form\]\]](Research%20Form.html) — research investigates and extracts; references brief and synthesize
