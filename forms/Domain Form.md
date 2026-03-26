---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Domain form type: a navigational and structural index for a shared language community — its scope, vocabulary, key nodes, open questions, and connections to other domains. A gardener's workbench for working within a knowledge area. 3 nodes in Garden/domains/."
tagline: "What shared language community does this cluster of forms belong to? — the structural contract for domain forms"
---

- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)
- in_precinct::[\[\[Household Precinct\]\]](../glosses/Household%20Precinct.html)

# Domain Form

**Core question**: "What shared language community does this cluster of forms belong to?"

A navigational and structural index for a **shared language community** — a bounded context where specific terms carry compressed meaning among practitioners. Distinguished from a reference (which briefs on a domain) by being an active map: it tracks which principles, patterns, cases, and citations exist within the domain, what's seed versus evergreen, and where the gaps are.

A domain in this garden is NOT a disciplinary classification or library science "knowledge domain." It is a shared language context — the place where "form," "predicate," and "seed stage" (Deep Context Architecture), or "principal authority" and "LESS Identity" (Self-Sovereign Identity) mean specific things without explanation. See [[Domains as Shared Language Communities]]↑ for the architectural decision and rationale.

Domains cut across form types. A domain page is a gardener's workbench: "I want to work on digital identity today" starts at the domain page. It is also a **vocabulary index** — the entry point for newcomers learning the shared language of that community (per L47).

## Structural Contract

A domain form requires:

- **Scope statement** — What this domain covers and doesn't cover.
- **Key nodes index** — Nodes organized by theme or form type. Tracks what exists and at what stage.
- **Open questions** — What's unresolved or under-explored within this domain.
- **Sources** — Key references and citations grounding this domain.
- **Relations** — Typed links to related domains and to the nodes this domain indexes.

Domain pages serve as vocabulary indexes for newcomers — entry points explaining the shared language of a knowledge area (per L47).

Naming heuristic: knowledge area proper name, concise. One to three words that name the field. "Deep Context Architecture" not "Deep Context Architecture Domain."

## Typical Predicates

- `is_a::[\[\[Domain Form\]\]](Domain%20Form.html)`
- `has_status::[\[\[Growing Stage\]\]](Growing%20Stage.html)`
- `indexes::[[Garden Node]]↑` — nodes belonging to this domain
- `relates_to::[[Other Domain]]↑` — related knowledge areas

## Exemplars

- [\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html) — the self-referential domain: 79 nodes defining the architecture that defines the garden
- [[Self-Sovereign Identity]]↑ — first non-Deep Context Architecture domain, 4 nodes on the principal authority framework from agency law
- [[Synpraxis]]↑ — how independent agents achieve outcomes together across varying degrees of integration

## Category

Structural form — captures *how things relate* and *what we understand*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 71-76.

## Relations

- relates_to::[\[\[Reference Form\]\]](Reference%20Form.html) — references brief on domains; domain pages actively index them
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — models describe structural relationships within a domain
- relates_to::[\[\[Inquiry Form\]\]](Inquiry%20Form.html) — domain pages track open questions that inquiry nodes investigate
- relates_to::[\[\[Opus Form\]\]](Opus%20Form.html) — domains index opuses alongside other form types via in_domain:: predicates
