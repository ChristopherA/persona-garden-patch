---
created: 2026-03-23
author: Christopher Allen
status: accepted
brief_summary: "The knowledge estate persona hierarchy uses a medieval estate metaphor with three tiers: Seneschal (estate-level strategic oversight), Groundskeeper and Chancellor (precinct-level orchestrators), Gardener and Scribe (precinct-level workers). The metaphor includes the medieval commons — shared ground not owned or controlled in a traditional sense — following Ostrom's commons governance principles. Everyone using this system is a peer with their own household, estate, and commons; the hierarchy describes functional roles within one person's estate, not authority over others."
tagline: "Everyone has their own household, estate, and commons — functional hierarchy within, peer relationship without"
---

- is_a::[[Decision Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Deep Context Architecture]]
- in_precinct::[[Garden Precinct]]

# Knowledge Estate as Peer Commons Architecture

## Context

The knowledge management system needed a coherent metaphor for AI persona coordination across two precincts (Garden and Household). The Groundskeeper/Gardener pair emerged first for the Garden Precinct. When architectural decisions began spanning both precincts, a higher-level coordinator was needed, and a parallel pair for the Household Precinct.

The medieval estate provides the metaphor: a household with grounds (garden), interior rooms (vault), and a steward overseeing both. But the metaphor carries a risk: one interpretation is that people using this system set themselves up as lords over others.

## Decision

### Three-tier persona hierarchy

| Tier | Role | Precinct | Function |
|------|------|----------|----------|
| Estate | [[Seneschal Persona\|Seneschal]] | Cross-precinct | Strategic oversight, boundary resolution, direction-setting |
| Precinct orchestrator | [[Groundskeeper Persona\|Groundskeeper]] | Garden | Coordinates Gardeners, manages commissions, maintains garden coherence |
| Precinct orchestrator | [[Chancellor Persona\|Chancellor]] | Vault | Organizes notes, maintains structure, ensures internal order |
| Precinct worker | [[Gardener Persona\|Gardener]] | Garden | Executes commissions in worktrees, creates/refines garden nodes |
| Precinct worker | Scribe (candidate) | Vault | Note creation, meeting capture, daily journal entries |

The Groundskeeper and Chancellor are **peers** — neither reports to the other. The Seneschal resolves boundary disputes and sets direction affecting both.

### The commons is part of the estate

The medieval estate metaphor explicitly includes the **commons** — shared ground at the edges of the estate, not owned or controlled in a traditional property sense. This follows Elinor Ostrom's principles of commons governance: shared resources managed by community rules rather than individual ownership.

In the knowledge estate:
- The **garden** is [[Synpraxis]] — collaborative knowledge that informs work with others. It faces outward toward the commons.
- The **household** is [[Praxis as Purposeful Personal Action|praxis]] — personal work. It faces inward.
- The **commons** is where gardens from different estates overlap and interact — collaborative projects, shared references, co-authored works.

### Design heritage: Self-Sovereign Identity

The estate architecture draws its design heritage from [[Allen (2016) The Path to Self-Sovereign Identity|Self-Sovereign Identity]] principles — particularly the recognition that sovereignty is a membrane, not a wall. The "self-sovereign estate" name encodes this: each person's estate is self-sovereign in the same sense that self-sovereign identity is self-sovereign. Authority flows from the person, is explicit and bounded, and follows the [[Allen (2023) Least and Necessary Design Patterns|least authority principle]] — each agent receives only the authority it needs. The delegated authority spectrum (steward → orchestrator → worker) implements this: every commission is traceable to the principal's authorization.

### Peers, not lords

Everyone using this system has their own household, estate, and commons. The persona hierarchy describes **functional roles within one person's estate**, not authority of one person over another. The Seneschal/Groundskeeper/Chancellor are AI personas serving one human principal — not a governance structure over other humans.

This distinction matters because the system is designed for [[Synpraxis|synpraxis]] — collaborative knowledge. When two people's gardens interact through the commons, they meet as peers. The estate metaphor governs the internal organization of each person's knowledge, not the relationship between people.

## Consequences

**Positive**:
- Clear separation of concerns across precincts
- Natural extension path for new precincts and worker types
- Commons framing prevents the "lord over others" misinterpretation
- Peer relationship between precinct orchestrators prevents hierarchy creep

**Negative**:
- Medieval metaphor may be unfamiliar to some users
- Three tiers may be over-engineering for a single-user system
- The commons concept is aspirational — no multi-estate interaction exists yet

## The Impossibility Constraint

Allen's Impossibility Hypothesis predicts that no decentralized commons can simultaneously achieve robust coordination, liveness, fault tolerance, and sustained decentralization. The estate's commons architecture operates within this constraint rather than attempting to solve it. The emerging norms of the Thursday group — share freely, credit through citation, don't force convergence — are lightweight social coordination that absorbs the constraints the protocol cannot satisfy. This is exactly what the impossibility hypothesis predicts: working decentralized systems shift unmet constraints into social layers.

The Gordian Club System addresses one aspect of the commons question: creating relational spaces that belong to the relationship, not to either party. Clubs are autonomous cryptographic objects requiring no infrastructure — sovereignty belongs to the relationship. Victoria Gracia's "space for the other" (a workspace that holds both voices, where the structure reflects the connection rather than either individual's reasoning) maps directly onto what clubs provide. The Spectrum of Consent maps the governance trade-offs for how these shared spaces make decisions.

## Open Questions

- What is the Scribe's exact scope? Is it the vault equivalent of the Gardener, or does it have different boundaries?
- How does the commons manifest technically? Shared git repositories? Federated gardens? Published outputs? Gordian Clubs?
- Should the Seneschal have an operational agent file, or is the Seneschal role always played by the user with AI augmentation?
- Is `in_precinct::[[Garden Precinct]]` correct for the Seneschal, or does it need a new precinct designation?
- How do the emerging social norms (share freely, credit through citation, don't force convergence) relate to Ostrom's principles? Are they sufficient, or do they need formalization as the group grows?

## Sources

- Estate management metaphor discussion (Session 7, 2026-03-23)
- [[Persona Form]] structural contract
- Elinor Ostrom, *Governing the Commons* (1990) — commons governance principles
- Rebooting the Web of Trust community — 7 years of face-to-face collaborative knowledge production as commons exemplar

## Relations

- relates_to::[[Seneschal Persona]]
- relates_to::[[Groundskeeper Persona]]
- relates_to::[[Chancellor Persona]]
- relates_to::[[Gardener Persona]]
- relates_to::[[Synpraxis]]
- relates_to::[[Praxis as Purposeful Personal Action]]
- relates_to::[[Principal-Agent Relationship in Augmented Knowledge Work]]
- relates_to::[[Allen (2016) The Path to Self-Sovereign Identity]]
  - Design heritage: SSI principles of explicit authority, bounded delegation, and sovereignty-as-membrane ground this architecture.
- relates_to::[[Allen (2023) Least and Necessary Design Patterns]]
  - The delegated authority spectrum implements least authority (ceiling) and necessary authority (floor).

- extended_by::[[Household Precinct Over Vault Precinct]]
  - The Household Precinct rename resolved the vault-vault naming collision in this architecture.

- extended_by::[[Functional Types in Agent Taxonomy]]
  - Formalizes the persona hierarchy this decision introduced (orchestrators, workers, boundary guardians).

- extended_by::[[Boundary Guardian as Distinct Agent Type]]
  - Splits the Chatelaine role, adding a constraint-enforcement function not present in the original three-tier design.

- relates_to::[[Three-Layer Publication Membrane]]
  - The publication membrane governs what crosses from estate-private to commons-published — the mechanism for the commons interaction this decision envisions
- relates_to::[[Federated Agent Governance Across Sovereign Estates]]
  - The inquiry into how agents from different estates interact when the commons becomes active — governance for the aspirational multi-estate interaction
- relates_to::[[Vocabulary Collision Navigation]]
  - The commons preserves vocabulary diversity as a feature — each estate's naming tradition translates rather than merges
- relates_to::[[Scope-Encoded Naming as Authority Boundary]]
  - Scope-encoded names make the three-tier hierarchy visible in naming
- relates_to::[[Allen's Impossibility Hypothesis]]
  - The commons architecture operates within the impossibility constraints; social norms carry load the protocol cannot
- relates_to::[[Allen (2015) A Spectrum of Consent]]
  - Maps the governance trade-offs for how commons participants make collective decisions
- relates_to::[[Gracia (2026) Uni-Versum Personal Knowledge Architecture]]
  - Victoria's "space for the other" — relational workspaces belonging to the relationship — maps onto the commons layer
