---
created: 2026-03-23
author: Christopher Allen
status: accepted
brief_summary: "The commission architecture is augmentation, facilitation, and amplification — not autonomous operation. Orchestrator personas must escalate to the user before merging deliverables containing judgments about intellectual content, skill behavior changes, priority signals, cross-project architectural decisions, or authorial voice. Process and plumbing fixes are autonomous. The test: does this contain judgments about the user's work, priorities, or intellectual stance?"
tagline: "Augmentation, facilitation, amplification — not autonomy. The user's judgment is not delegable."
grafted: 2026-04-01
---

- is_a::[Decision Form](../forms/Decision%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Augmentation Over Autonomy in Agent Architecture

## Context

During the first commission cycle between an orchestrator and worker agent, the orchestrator merged a worker's report that contained qualitative judgments about the user's intellectual work — what citations "captured well" versus "missed" — without presenting those judgments for review. The commission architecture had no explicit boundary between autonomous process work and work requiring user judgment.

This exposed a gap: without an escalation protocol, an orchestrator persona substitutes its judgment for the user's on matters that belong to the user. The gap is architectural, not preferential — it defines the authority boundary in the [principal-agent relationship](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html).

## Decision

The commission architecture operates as **augmentation, facilitation, and amplification** — not autonomous operation.

Orchestrator personas must escalate to the user (via AskUserQuestion) before merging any deliverable that contains:
- Judgments about the user's intellectual content
- Skill behavior changes
- New ghost links (which signal garden priorities)
- Cross-project architectural decisions
- Anything touching authorial voice or editorial stance

Process and plumbing fixes (formatting, structural consistency, predicate corrections) are autonomous.

**The test**: "Does this contain judgments about the user's work, priorities, or intellectual stance?" If yes, escalate. If no, proceed.

## Consequences

**Positive**:
- User retains authority over intellectual and editorial decisions
- Orchestrator can still move quickly on process work
- Clear test for when to escalate vs proceed

**Negative**:
- Slows commission throughput for content-heavy deliverables
- Orchestrator must read deliverables before approving commits (not just approve permission prompts)

## Open Questions

- Where is the line between agent capabilities and skill capabilities? Agents should complement skills, not substitute for them. Agentic best practices research needed to understand where different kinds of automation belong.
- Does the escalation protocol change as the garden matures and the user has more confidence in the system's judgments?
- Should different persona tiers have different escalation thresholds?

## Sources

- Commission cycle observation — orchestrator merged report with unreviewed intellectual judgments
- [Principal Authority as Agency Law for Digital Identity](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html) — authority model
- [[Human Authority Over Augmentation Systems]]↑ — principle this decision implements
- [Groundskeeper Persona](../personas/Groundskeeper%20Persona.html) — persona that required the escalation protocol

## Relations

- implements::[[Human Authority Over Augmentation Systems]]↑
- relates_to::[Principal Authority as Agency Law for Digital Identity](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)
- relates_to::[Groundskeeper Persona](../personas/Groundskeeper%20Persona.html)
- relates_to::[[Commission as Bounded Work Assignment]]↑
