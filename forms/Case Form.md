---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Case form type: a specific narrative with outcome recording what was attempted, what resulted, and what was learned. Immutable — history doesn't change, though interpretation may."
tagline: "What happened when this was tried? — the structural contract for case forms"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Case Form

**Core question**: "What happened when this was tried?"

A specific narrative with outcome. Not generalized (that's a pattern), not interpretive (that's a gloss). Records what was attempted, what resulted, and what was learned. Immutable; history doesn't change, though interpretation of it may.

## Structural Contract

Every case form requires these sections in order:

- **Situation** — What was the context? What conditions existed?
- **Action** — What was attempted? Who did what?
- **Outcome** — What resulted? Include both expected and unexpected consequences.
- **Lessons** — What was learned from this experience?
- **Sources** — Primary accounts, documentation, or records of the event.
- **Relations** — Connections to patterns validated or invalidated, principles tested, decisions that followed.

Naming heuristic: describe what was attempted and the context. Action + scope. "Hybrid Bootstrapping for Garden Migration" not "The Bootstrap Case."

## Typical Predicates

- `is_a::[\[\[Case Form\]\]](Case%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)`
- `in_domain::[[Domain Name]]↑`
- `validates::[\[\[Pattern Form\]\]](Pattern%20Form.html)` — patterns this case confirms
- `invalidates::[\[\[Pattern Form\]\]](Pattern%20Form.html)` — patterns this case disproves
- `prompted::[\[\[Decision Form\]\]](Decision%20Form.html)` — decisions that followed from this case

## Exemplars

- [[Hybrid Bootstrapping for Garden Migration]]↑ — scripted tag-to-predicate conversion of 913 files, then hand-authored extraction to garden forms
- [[Architecture Document Extraction to Garden Forms]]↑ — decomposing a 450-line architecture document into 80+ typed garden nodes across 12 sessions

## Category

Action form — captures *what to do* and *what happened*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 85-88.

## Relations

- relates_to::[\[\[Pattern Form\]\]](Pattern%20Form.html) — cases validate or invalidate patterns
- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — cases prompt decisions; decisions record forward-looking choices
- relates_to::[\[\[Gloss Form\]\]](Gloss%20Form.html) — interpretation of cases may become glosses
