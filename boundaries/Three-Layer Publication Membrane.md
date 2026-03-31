---
created: 2026-03-31
author: Christopher Allen
brief_summary: "Compound documents have three visibility layers, each controlled by a different membrane: git-secret (credentials and sensitive data, never committed), estate-private (operational memory and session learnings, git-tracked but behind the Private/ publication membrane), and patch-published (synpraxis content that crosses the garden patch boundary to collaborators). Maps to the sovereignty membrane hierarchy: body integrity, household, garden edge."
tagline: "Three visibility membranes — secrets never leave, operations stay private, synpraxis crosses to collaborators"
---

- is_a::[[Boundary Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Deep Context Architecture]]
- in_precinct::[[Garden Precinct]]

# Three-Layer Publication Membrane

## Authority Zones

| Layer | Visibility | Enforcement | Content | Membrane |
|-------|-----------|-------------|---------|----------|
| **git-secret** | Never committed | .gitignore + Chatelaine audit | Credentials, API keys, sensitive personal data | Body integrity — nothing crosses |
| **estate-private** | Git-tracked, not published | Private/ subfolder convention + publication scripts | Operational memory, session learnings, corrections history, internal analysis | Household — visible to all estate agents, invisible to collaborators |
| **patch-published** | Crosses garden patch boundary | Patch conventions + publishing pipeline | Synpraxis content — citations, models, patterns, insights for collaborative work | Garden edge — selectively permeable to specific audiences |

Each layer has different permeability rules. Layer 1 is opaque — nothing crosses under any circumstances. Layer 2 is selectively transparent within the estate but opaque outward. Layer 3 is selectively permeable — content is published to specific patches for specific collaborator audiences, not broadcast.

The Private/ subfolder is the structural implementation of layer 2. Any compound document can contain a Private/ subfolder holding estate-private analysis, process notes, or accumulated operational context that informs the published content but is not itself published.

## Agent Behavior at Boundaries

1. **Before committing**: Check whether content belongs at layer 1 (git-secret). The Chatelaine audits for credentials, API keys, and sensitive personal data. When uncertain, escalate — the cost of committing a secret is irreversible.
2. **Before publishing to a patch**: Check whether content is layer 2 (estate-private) or layer 3 (patch-published). Estate-private content lives in Private/ and stays behind the publication membrane. The publishing pipeline excludes Private/ by convention.
3. **When creating compound documents**: Structure content across layers at creation time. Analysis that informs the published node but reveals internal operational patterns (session-specific learnings, estate-internal corrections) belongs in Private/.

## Amendment

The three-layer structure is amendable by the principal (Christopher Allen) through the Seneschal's architectural authority. Changes to layer boundaries require explicit decision nodes — the membrane architecture is load-bearing for both privacy (layer 1), operational integrity (layer 2), and collaborative trust (layer 3).

Adding a fourth layer (e.g., a semi-public layer between estate-private and patch-published for trusted collaborators with deeper access) would require a Decision Form node documenting the context, choice, and consequences.

## Sources

- Seneschal Session 111 (2026-03-30) — three-layer model articulated during compound document architecture design
- [[Six Approaches to Persona Architecture — Synthesis]] — Axis 4 discusses publication as the mechanism for cross-system interoperability
- [[Sovereignty Is Selective Permeability Not Absolute Control]] — sovereignty-as-membrane model that this boundary implements

## Relations

- grounded_in::[[Sovereignty Is Selective Permeability Not Absolute Control]]
  - The three layers map to the sovereignty membrane hierarchy: body integrity (secrets), household (estate-private), garden edge (published)
- relates_to::[[Knowledge Estate as Peer Commons Architecture]]
  - The commons operates at layer 3 — patch-published content is the mechanism for peer interaction
- relates_to::[[Naming Carries Relational Weight]]
  - The layer names themselves carry architectural weight — "private" vs "secret" vs "published" encode different membrane permeabilities
- relates_to::[[Six Approaches to Persona Architecture — Synthesis]]
  - The synthesis's practical question ("how do we publish patches so we can cross-reference each other?") is a layer-3 question
- relates_to::[[Gracia (2026) Uni-Versum Personal Knowledge Architecture]]
  - Gracia's diploma concept governs inter-system trust at the layer-3 boundary
