---
created: 2026-04-02
author: Christopher Allen
brief_summary: "Horton's architectural pattern — adding accountability to capability systems by interposition rather than modification — generalizes beyond security. Any system that delegates authority can add coordination, accountability, or translation as a transparent layer without requiring either side to change. This pattern directly addresses the cross-garden interoperability question: sovereign knowledge systems can coordinate through interposed layers (citations, glosses, vocabulary bridges) without either adopting the other's model."
tagline: "Add coordination between sovereign systems without modifying either side"
---

- is_a::[[Gloss Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Deep Context Architecture]]

# Accountability as a Layer Not a Replacement

Miller, Donnelley, and Karp's [[Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems|Horton protocol]] demonstrates a pattern that generalizes well beyond security: when two systems need to coordinate, you can add the coordination as a transparent layer between them rather than modifying either system to accommodate the other.

In Horton's case, the problem was accountability in capability systems. Capabilities provide proactive safety (least authority, no ambient permissions) but not reactive accountability (who did what). ACL systems provide accountability but sacrifice safety. Rather than choosing one or replacing either, Horton interposes a tracking layer that adds accountability without touching the capability substrate. Neither side changes. The new property emerges from the layer between them.

## The Pattern Beyond Security

This interposition pattern maps directly to the cross-garden coordination problem this group faces. Victoria's Uni-Versum has its own vocabulary (nos, agens, fidelis-est, autonomia). Christopher's estate has its own (garden, precinct, persona, commission). Peter and Victoria's Reflection Personas use a third (analytical lenses grounded in intellectual frameworks). These aren't competing — they're sovereign systems with different architectures serving different purposes.

The [[Vocabulary Collision Navigation]] pattern already describes how the group handles naming overlaps: glosses that translate between systems, citations that formally read one system's work through another's lens, cross-references that bridge without merging. These are interposition layers — they sit between sovereign knowledge systems and provide mutual intelligibility without requiring either side to adopt the other's vocabulary.

Horton adds something the group hasn't named yet: the coupling of authority with accountability at the interposition layer. When one garden cites another's work, the citation carries both the reference (the authority to use the idea) and the attribution (the accountability for how it's used). The garden's citation form — with its analysis and insights sub-files — is structurally similar to Horton's proxy/stub pairs: it wraps the source work in a structure that tracks how the receiving system interprets and applies it, without modifying the original.

## What This Means for the Commons Question

The group's emerging norms — share seeds freely, credit sources through citation, don't force vocabulary convergence — are lightweight interposition layers. They coordinate sovereign systems without requiring structural change to any of them. Horton's insight suggests these layers can be formalized incrementally: add accountability tracking where it's needed (certain delegation paths, certain cross-garden exchanges) without imposing it everywhere.

The question for the group: what does the next interposition layer look like? Citations and glosses handle vocabulary. What handles trust — the progressive confidence that builds through repeated cross-garden exchanges?

## Relations

- relates_to::[[Vocabulary Collision Navigation]]
  - Vocabulary navigation is an interposition layer for naming collisions; Horton shows the same pattern for authority and accountability
- relates_to::[[Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems]]
  - The source of the interposition-over-modification pattern, applied here beyond its original security context
- relates_to::[[Sovereignty Is Selective Permeability Not Absolute Control]]
  - The membrane model: selective permeability IS interposition — the membrane is the layer between sovereign interior and external world
