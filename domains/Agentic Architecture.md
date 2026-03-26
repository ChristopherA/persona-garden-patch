---
created: 2026-03-24
author: Christopher Allen
brief_summary: "Domain index for Agentic Architecture — patterns for AI agent systems operating as augmentations within human workflows. Covers configuration lifecycle (shearing layers, config-state separation), multi-agent coordination (commission architecture, persona design), tool orchestration, and naming discipline for pattern languages. This domain is about system architecture, not AI/ML capabilities."
tagline: "How to architect the scaffold that lets agents augment human work without replacing human judgment"
---

- is_a::[\[\[Domain Form\]\]](../forms/Domain%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Agentic Architecture

Agentic Architecture covers the design of systems where AI agents operate as augmentations within human workflows — configuration lifecycle, multi-agent coordination, persona design, and tool orchestration. The unifying question: how do you build a system scaffold that lets agents do more without eroding human authority?

This domain is distinct from AI/ML generally. It is not concerned with training, inference, or model capabilities. It is concerned with the structural decisions that determine how agents behave in a specific human context — how they receive instructions, maintain state, coordinate with other agents, and know when to escalate.

## Scope

**Covers**: Agent configuration lifecycle (how rules, skills, and state are stored and protected), multi-agent coordination patterns (Groundskeeper-Gardener commission architecture, persona differentiation), tool orchestration, the boundary between task instruction and role specialization, and naming discipline for agentic pattern languages.

**Does not cover**: AI/ML model design, training, or inference. Foundation model capabilities and limitations. General software architecture patterns not specific to agentic contexts. The [\[\[Deep Context Architecture\]\]](Deep%20Context%20Architecture.html) domain covers the garden's own knowledge architecture; Agentic Architecture covers the agent system architecture that operates within it.

## Key Forms

### Configuration Lifecycle

How agent configuration and state are stored, protected, and separated:

- [[Shearing Layers for Agent Configuration]]↑ — pattern: separate content, configuration, and state into storage locations with protection policies matching their write frequency
- [[Config-State Conflation]]↑ — anti-pattern: storing agent state alongside configuration forces a single protection policy onto incompatible lifecycle categories; the specific failure is the Claude Code v2.1.78+ protected-directory gate on `.claude/`
- [[Pace Layers for Knowledge and Agent Systems]]↑ — model: Brand's pace layering mapped to agent platform components — prompts change per-session, skills per-sprint, APIs per-quarter, compliance rules per-year

### Multi-Agent Coordination

How agents with different roles work together:

- [[Three Functional Types in Agent Taxonomy]]↑ — decision: orchestrators coordinate within precincts, workers execute bounded commissions, boundary guardians enforce constraints across precincts
- [[Boundary Guardian as Distinct Agent Type]]↑ — decision: separating constraint enforcement from orchestration (Chatelaine split into Chancellor + Chatelaine)
- [[Task Instruction and Role Specialization as Agent Configuration Layers]]↑ — model: AGENTS.md (task instruction, tool-agnostic) and persona files (role specialization, platform-specific) are complementary layers, not competing approaches
- [[Augmentation Over Autonomy in Agent Architecture]]↑ — decision: commission architecture operates as augmentation and facilitation; escalation protocol for intellectual judgments
- [[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑ — inquiry: what behavioral dimensions persona files should cover (open)
- [[Naming Distinctiveness in Agent and Garden Architecture]]↑ — inquiry: whether agent archetype overlap and garden naming conventions produce enough differentiation (open)
- [[Structured Disagreement Through Persona Review]]↑ — pattern: multiple persona perspectives on a proposal surface disagreements that single-agent review misses

### Naming Discipline

How to name patterns, principles, and concepts in an agentic pattern language:

- [[Vocabulary Search Before Naming]]↑ — principle: search existing vocabulary before proposing a name; adopt established terms when they fit; verify no collision with terms of art
- [[Propose Multi-Word Terms from the Start]]↑ — principle: name with at least two words immediately; retrofitting a qualifier later cascades through every node that linked the bare word

### Boundaries

Where agent authority begins and ends:

- [[Delegated Decision Authority Spectrum]]↑ — boundary: where agent authority begins and ends in the principal-agent relationship
- [[Automated Gardening Trust Problem]]↑ — inquiry: can agents garden their own instructions, or does self-modification require human oversight? (open)

## Candidate Forms

Patterns and concepts identified but not yet extracted:

### Patterns

- Commission as Bounded Work Assignment — what makes a commission distinct from a general task: bounded scope, defined deliverables, explicit out-of-bounds, close-out protocol
- Session Worktree Isolation — isolating commission work in a git worktree prevents cross-commission interference and makes clean merges possible
- Ghost Link as Garden Gap Signal — unresolved wikilinks in commission deliverables signal garden planning needs, not lint errors

### Models

- Commission Lifecycle — phases from intake through close-out: commission specification → worktree setup → execution → deep learning → session capture → merge
- Orchestrator-Executor Trust Model — what the Groundskeeper delegates to Gardeners and what it retains; the criteria for autonomy vs. escalation

### Inquiries

- Group Deliberation Mechanism — practical mechanism when an agent hits a group-deliberative boundary [[Group Deliberation Mechanism]]↑
- Agentic Pattern Language Completeness — how many named patterns constitute a sufficient pattern language for agent system design?

## Open Questions

- How should Agentic Architecture relate to [\[\[Deep Context Architecture\]\]](Deep%20Context%20Architecture.html) as a sub-domain? Many patterns here are instantiations of deeper Deep Context Architecture principles in an agentic context.
- Should the commission architecture have its own domain page, or does it live as a subdomain of Agentic Architecture?
- What's the right granularity for persona differentiation? The Groundskeeper-Gardener-Chancellor-Seneschal pattern emerged empirically; it hasn't been validated against alternative role structures.

## Sources

- [[Augmentation Over Autonomy in Agent Architecture]]↑ — founding decision for the commission architecture
- [[systematicls (2026) World-Class Agentic Engineering]]↑ — practitioner guide; independent validation of context management and rule/skill lifecycle
- [[Rajasekaran (2025) Effective Context Engineering for AI Agents]]↑ — Anthropic's engineering guide on attention budgets and sub-agent isolation
- Deep Context Garden commission sessions (2026-03) — empirical source for the shearing layers and config-state conflation patterns

## Relations

- relates_to::[\[\[Deep Context Architecture\]\]](Deep%20Context%20Architecture.html)
  - Deep Context Architecture defines the knowledge architecture the garden implements; Agentic Architecture defines the agent system that operates within it. Many patterns in this domain are agentic instantiations of Deep Context Architecture principles.

- relates_to::[[Self-Sovereign Identity]]↑
  - The principal authority framework from agency law applies to agent systems as well as identity systems. Authority delegation, escalation protocols, and the principal-agent relationship bridge both domains.

- relates_to::[[Synpraxis]]↑
  - Synpraxis addresses how independent agents achieve outcomes together; commission architecture is a specific synpractic pattern where Groundskeeper and Gardeners coordinate without constant synchronization.
