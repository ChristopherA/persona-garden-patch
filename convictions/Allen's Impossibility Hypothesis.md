---
created: 2026-03-31
author: Christopher Allen
brief_summary: "The hypothesis that no decentralized system can simultaneously achieve robust coordination, liveness, strong fault tolerance, and sustained decentralization without relying on hidden assumptions or external coordination. Decentralization is unstable without implicit structure, and that structure is where the hidden assumptions live. Analogous to Arrow's Impossibility Theorem for voting and the FLP Impossibility Result for distributed consensus."
tagline: "Decentralization is unstable without implicit structure — and that structure is where the hidden assumptions live"
---

- is_a::[[Conviction Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Self-Sovereign Identity]]
- in_precinct::[[Garden Precinct]]

# Allen's Impossibility Hypothesis

## The Conviction

No decentralized system can simultaneously achieve robust coordination, liveness, strong fault tolerance, and sustained decentralization without relying on hidden assumptions or external coordination. Decentralization is not just hard to design — it is unstable without implicit structure, and that structure is where the hidden assumptions live.

This parallels two established impossibility results. Arrow's Impossibility Theorem demonstrates that no ranked voting system can satisfy a small set of reasonable fairness criteria simultaneously — every system sacrifices at least one. The Fischer-Lynch-Paterson (FLP) Impossibility Result proves that no deterministic protocol can guarantee consensus in an asynchronous distributed system where even one process may fail. Both show that fundamental requirements inevitably conflict. Any working system resolves this by shifting unmet constraints into implicit assumptions or social layers.

The same holds for decentralized governance broadly. Anyone who claims to have the "right" answer to collaborative governance is probably wrong — not because governance is unsolved, but because the constraints are genuinely incompatible. Every working decentralized system contains hidden trade-offs: assumptions about participant behavior, informal coordination mechanisms, social norms that carry load the protocol cannot.

## Grounding

This conviction emerges from three decades of building decentralized systems and watching them encounter the impossibility boundary:

- **Self-sovereign identity** codified ten principles (2016) that any identity system should satisfy. In practice, no system achieves all ten simultaneously. Systems that maximize portability sacrifice persistence guarantees. Systems that maximize minimization limit interoperability. The principles remain correct as aspirations; the impossibility is that achieving all simultaneously requires assumptions about the operating environment that are themselves centralizing.

- **Blockchain consensus** demonstrates the impossibility operationally. Bitcoin achieves coordination and fault tolerance but sacrifices liveness (confirmation takes minutes to hours) and sustained decentralization (mining pools reconcentrate). Ethereum achieves faster liveness but shifts trust assumptions to validators. Every protocol navigates the same impossibility surface.

- **Commons governance** (Ostrom's work) identifies conditions for successful commons management, but every successful commons she studied had implicit coordination mechanisms — cultural norms, community monitoring, graduated sanctions — that are themselves forms of external coordination. The commons works because the social layer absorbs the constraints the protocol cannot satisfy.

- **The Spectrum of Consent** maps how governance systems from unanimity through advisory to autocratic each resolve the impossibility by choosing which requirements to sacrifice. Unanimity sacrifices liveness (any participant can block). Majority rule sacrifices fault tolerance against coordinated minorities. Autocratic systems sacrifice decentralization entirely. The spectrum is a map of the impossibility surface.

## Implications

- **For governance design**: Stop seeking the right governance model. Instead, identify which constraints the system will sacrifice and make those trade-offs explicit. Hidden assumptions are more dangerous than acknowledged limitations.

- **For the commons question**: The Thursday group's emerging norms — share freely, credit through citation, don't force convergence — are more realistic than designed governance because they operate as lightweight social coordination (exactly the kind of implicit structure the hypothesis predicts). The question is whether to formalize those norms (risking brittleness) or let them remain implicit (risking drift).

- **For inter-estate collaboration**: When sovereign estates interact, every protocol for exchange encodes assumptions about trust, availability, and cooperation that may not hold across all participants. Gordian Envelope addresses part of this (cryptographic provenance survives context changes), but the social layer — who shares what, when, and why — carries the governance load.

- **For the estate architecture itself**: The persona hierarchy works because the social layer (user as principal, authorizing commissions, reviewing outputs) absorbs the coordination constraints that no protocol among agents could handle autonomously. Removing the human from the loop doesn't just lose judgment — it removes the hidden coordination mechanism.

## Sources

- Allen, C. (2016). "The Path to Self-Sovereign Identity" — 10 principles as impossibility surface map
- Allen, C. (2015). "A Spectrum of Consent" — governance models as impossibility trade-offs
- Arrow, K. (1951). *Social Choice and Individual Values* — impossibility theorem for voting systems
- Fischer, M., Lynch, N., & Paterson, M. (1985). "Impossibility of Distributed Consensus with One Faulty Process" — FLP impossibility result
- Ostrom, E. (1990). *Governing the Commons* — successful commons require implicit coordination
- Allen, C. (2026). Reply to Victoria's Musings — first explicit articulation of the hypothesis

## Relations

- grounds::[[Sovereignty Is Selective Permeability Not Absolute Control]] — the membrane is one response to the impossibility: if you cannot achieve everything simultaneously, control what crosses your boundary
- relates_to::[[Knowledge Estate as Peer Commons Architecture]] — the commons architecture operates within the impossibility constraints; social norms carry load the protocol cannot
- relates_to::[[Federated Agent Governance Across Sovereign Estates]] — inter-estate governance faces the impossibility directly: coordination, fault tolerance, and decentralization cannot all be maximized
- relates_to::[[Allen (2015) A Spectrum of Consent]] — maps the trade-off surface across governance models
