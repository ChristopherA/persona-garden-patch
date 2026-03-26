---
created: 2026-03-26
author: Christopher Allen
status: accepted
brief_summary: "Persona nodes in the garden are the design authority for agent behavior. Agent configuration files (Claude Code .md files, AGENTS.md entries, future SOUL.md renditions) are downstream artifacts that implement what the persona specifies. The persona carries design rationale, declared blind spots, behavioral scope, and typed relationships to peer personas. The agent file is a platform-specific rendition — it consumes the persona's decisions but does not originate them."
tagline: "The persona is the knowledge artifact; the agent file is its rendition."
---

- is_a::[Decision Form](../forms/Decision%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Agentic Architecture](../domains/Agentic%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Persona Nodes as Design Authority for Agent Configuration

## Context

Agent systems need personas. Most approaches treat them as configuration: a system prompt, a YAML file, a role string. The persona is consumed by the runtime and invisible to everyone else. In the garden's multi-agent architecture, eight personas (Seneschal, Groundskeeper, Chancellor, Chatelaine, Gardener, Cultivator, Forager, Pruner) each have both a garden persona node and a Claude Code agent file.

The question: which is authoritative? When the persona node says one thing and the agent file says another, which wins? Where do design decisions originate — in the garden or in the configuration?

Peter Kaminski's work with 27 reflection personas for his course — and Victoria Gracia's compound personas with full cultural context documents — demonstrated that shallow configuration misses the depth that makes personas useful. A single-page prompt is a shallow persona; a compound knowledge node with design rationale, blind spots, and typed relationships is a deep one.

## Decision

**Persona nodes are the design authority.** Agent configuration files are downstream renditions.

The persona node carries:
- **Behavioral scope** — what the agent does and does not do
- **Declared blind spots** — what the agent cannot see about itself
- **Operational architecture** — how the agent coordinates with peers
- **Design rationale** — why these choices were made
- **Typed relationships** — `constrains::`, `composes_with::`, `extends::` edges to peer personas and to the models, patterns, and inquiries that inform the design

The agent file consumes these decisions and renders them into a platform-specific format (Claude Code system prompt, future SOUL.md, future AGENTS.md entry). The agent file does not originate design decisions — it implements them.

This distinction matters because it makes persona design:
- **Auditable** — the persona node participates in the knowledge graph, where its relationships are visible and traversable
- **Composable** — personas relate to each other through typed predicates, not through implicit conventions in configuration files
- **Evolvable** — changes to persona design go through the same status lifecycle (Seed → Growing → Evergreen) as any other knowledge node
- **Portable** — the same persona node can render into multiple platform formats via `renders_as::` predicates

## Consequences

- Agent files should be regenerable from persona nodes. If an agent file contains behavioral decisions not present in the persona node, those decisions should be upstreamed to the persona.
- The `renders_as::` predicate (proposed in [Does the Garden Persona Architecture Need a Portability Layer](../inquiries/Does%20the%20Garden%20Persona%20Architecture%20Need%20a%20Portability%20Layer.html)) would formalize the relationship between persona nodes and their platform-specific renditions.
- Compound persona nodes (folder-based, with supporting documents in Renditions/) become the natural structure for deep personas — the pattern Victoria Gracia independently discovered.

**Further investigation needed**: This decision is validated within a single-platform context (Claude Code). The sync mechanism between persona nodes and agent files — how changes propagate, whether rendition generation should be automated, how drift is detected — remains an open question that cannot be fully explored until the architecture moves beyond Claude Code to multiple agent frameworks. See [\[\[How Should Persona Node Changes Sync to Agent Configuration Files\]\]](../inquiries/How%20Should%20Persona%20Node%20Changes%20Sync%20to%20Agent%20Configuration%20Files.html).

## Alternatives Considered

**Agent file as source of truth**: Treat the `.md` agent file as authoritative and the persona node as documentation. Rejected because configuration files lack typed relationships, design rationale, and lifecycle management. The agent file would be an island — connected to nothing, explaining nothing.

**Bidirectional sync**: Both persona node and agent file are authoritative; changes in either propagate to the other. Rejected because bidirectional sync creates merge conflicts and ambiguity about which version is canonical. One source of truth is simpler.

**No formal relationship**: Let persona nodes and agent files drift independently. Rejected because drift means the agent's actual behavior diverges from its documented design — exactly the opacity problem that motivated treating personas as knowledge artifacts.

## Sources

- Dialogue between Christopher Allen and Peter Kaminski (March 2026) on reflection personas and compound documents
- Garden estate architecture: eight operational personas with corresponding Claude Code agent files
- Victoria Gracia's compound persona work with Toki Pona cultural context

## Relations

- relates_to::[[Augmentation Over Autonomy in Agent Architecture]]↑
  - The persona-as-authority decision reinforces augmentation: the user designs personas as knowledge artifacts, agents implement them.

- relates_to::[Does the Garden Persona Architecture Need a Portability Layer](../inquiries/Does%20the%20Garden%20Persona%20Architecture%20Need%20a%20Portability%20Layer.html)
  - The portability inquiry asks how persona nodes render into multiple frameworks — this decision establishes that rendering is always downstream from the persona node.

- relates_to::[[Boundary Guardian as Distinct Agent Type]]↑
  - The Chatelaine persona exemplifies why persona nodes need more than configuration: the boundary guardian role requires declared blind spots and explicit authority limits that a system prompt alone cannot carry.
