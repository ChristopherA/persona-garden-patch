---
created: 2026-03-26
author: Christopher Allen
brief_summary: "Classifies estate agents into four functional types: stewards (estate-level strategic and tactical coordination), orchestrators (coordinate workers within a precinct), workers (execute bounded commissions), and boundary guardians (enforce constraints across precincts). The taxonomy emerged from practice — initially three types, extended to four when strategic coordination proved functionally distinct from boundary enforcement."
tagline: "Stewards direct, orchestrators coordinate, workers execute, boundary guardians constrain — four types from practice"
grafted: 2026-04-01
---

- is_a::[Decision Form](../forms/Decision%20Form.html)
- has_status::[Growing Stage](../forms/Growing%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)

# Functional Types in Agent Taxonomy

## Context

The estate accumulated 10+ agent roles over several weeks of development. Initially described informally — "the orchestrator manages the garden," "the reader assesses citations" — the relationships between agents were implicit. Some coordinated others; some worked alone on bounded tasks; some enforced rules across the whole estate. Without a taxonomy, new agent proposals lacked a framework for evaluating whether they filled a real gap or duplicated an existing function.

The taxonomy emerged from observing what each agent actually does, not from top-down design. Three types were initially identified (orchestrator, worker, boundary guardian). The strategic coordinator was classified as a boundary guardian alongside the constraint enforcer, but this proved inaccurate — one sets architectural direction and coordinates orchestrators, while the other enforces constraints. These are different functions. The introduction of a tactical coordinator spanning precincts confirmed that estate-level coordination was a distinct type, not a variant of boundary enforcement. The fourth type — steward — was added to reflect this.

## Decision

Classify all estate agents into four functional types:

| Type | Role | Examples |
|------|------|---------|
| **Steward** | Estate-level strategic and tactical coordination spanning precincts | Strategic director ([Seneschal Persona](../personas/Seneschal%20Persona.html)), tactical coordinator |
| **Orchestrator** | Coordinates workers within a precinct | [Chancellor Persona](../personas/Chancellor%20Persona.html) (Household), [Groundskeeper Persona](../personas/Groundskeeper%20Persona.html) (Garden) |
| **Worker** | Executes commissions in bounded scope | [Gardener](../personas/Gardener%20Persona.html), [Cultivator](../personas/Cultivator%20Persona.html), [Forager](../personas/Forager%20Persona.html), [Pruner](../personas/Pruner%20Persona.html) |
| **Boundary guardian** | Enforces constraints across precincts | [Chatelaine Persona](../personas/Chatelaine%20Persona.html) (privacy/secrets) |

Stewards span precincts without managing one. They set direction or translate direction into tactical execution across precincts. Orchestrators deploy workers via commissions within their precinct. Workers report back; orchestrators decide what to act on. Boundary guardians enforce cross-precinct constraints without managing content or coordinating workers.

## Consequences

- Every new agent proposal must identify its functional type
- Stewards use high-capability models (strategic judgment); orchestrators use high-capability models (coordination judgment); workers use efficient models by default (execution-focused), high-capability when the task requires depth
- Workers do not write to queues or briefs directly — they report to their orchestrator
- The estate charter documents the taxonomy as the authoritative reference
- Stewards and orchestrators each own a maintenance workstream as their routing sink

## Alternatives Considered

- **Two types (orchestrator + worker)** — the initial model before the boundary guardian was separated from the household orchestrator. Rejected because constraint enforcement is functionally distinct from both coordination and execution
- **Three types (orchestrator + worker + boundary guardian)** — the strategic coordinator was classified as a boundary guardian. Rejected because strategic coordination (setting direction, resolving disputes) is functionally distinct from constraint enforcement (preventing violations). The misclassification persisted across multiple sessions because both types span precincts — but spanning precincts is a shared trait, not a shared function
- **Flat list (no types)** — rejected because it provides no framework for evaluating new agent proposals or understanding agent relationships
- **Hierarchical model (strategic coordinator at top, then orchestrators, then workers)** — considered but the boundary guardian doesn't fit a hierarchy. The constraint enforcer is a peer to the strategic coordinator, not subordinate

## Relations

- depends_on::[[Boundary Guardian as Distinct Agent Type]]↑
  - The third type exists because boundary enforcement was separated from orchestration.

- relates_to::[[Precinct as Organizational Unit]]↑
  - Orchestrators map to precincts; stewards and boundary guardians span them.

- relates_to::[Knowledge Estate as Peer Commons Architecture](../decisions/Knowledge%20Estate%20as%20Peer%20Commons%20Architecture.html)
  - The four types map to the estate's sovereignty-as-membrane model: stewards maintain the whole membrane, orchestrators manage sections of it, workers do bounded work within sections, boundary guardians prevent leaks.
