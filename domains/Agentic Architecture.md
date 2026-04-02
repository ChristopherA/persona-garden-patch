---
created: 2026-03-24
author: Christopher Allen
brief_summary: "Domain index for Agentic Architecture — patterns for AI agent systems operating as augmentations within human workflows. Covers configuration lifecycle (shearing layers, config-state separation), multi-agent coordination (commission architecture, persona design), tool orchestration, and naming discipline for pattern languages. This domain is about system architecture, not AI/ML capabilities."
tagline: "How to architect the scaffold that lets agents augment human work without replacing human judgment"
---

- is_a::[Domain Form](../forms/Domain%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Deep Context Architecture](Deep%20Context%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Agentic Architecture

Agentic Architecture covers the design of systems where AI agents operate as augmentations within human workflows — configuration lifecycle, multi-agent coordination, persona design, and tool orchestration. The unifying question: how do you build a system scaffold that lets agents do more without eroding human authority?

This domain is distinct from AI/ML generally. It is not concerned with training, inference, or model capabilities. It is concerned with the structural decisions that determine how agents behave in a specific human context — how they receive instructions, maintain state, coordinate with other agents, and know when to escalate.

## Scope

**Covers**: Agent configuration lifecycle (how rules, skills, and state are stored and protected), multi-agent coordination patterns (Groundskeeper-Gardener commission architecture, persona differentiation), tool orchestration, the boundary between task instruction and role specialization, and naming discipline for agentic pattern languages.

**Does not cover**: AI/ML model design, training, or inference. Foundation model capabilities and limitations. General software architecture patterns not specific to agentic contexts. The [Deep Context Architecture](Deep%20Context%20Architecture.html) domain covers the garden's own knowledge architecture; Agentic Architecture covers the agent system architecture that operates within it.

## Key Forms

### Configuration and State

How agent configuration, state, and identity are stored, protected, and separated:

- [[Shearing Layers for Agent Configuration]]↑ — pattern: separate content, configuration, and state into storage locations with protection policies matching their write frequency
- [[Config-State Conflation]]↑ — anti-pattern: storing agent state alongside configuration forces a single protection policy onto incompatible lifecycle categories
- [[Pace Layers for Knowledge and Agent Systems]]↑ — model: Brand's pace layering mapped to agent platform components
- [[Markdown-as-State for Agent Identity]]↑ — pattern: plain text files under version control as canonical agent configuration; no databases, no YAML managers
- [[Tiered State Persistence Architecture]]↑ — model: four tiers from ephemeral session context to durable configuration, each with different durability, audience, and update frequency
- [[Stateless Loop with External State Files]]↑ — pattern: reset context between iterations while persisting state to files; prevents hallucination drift in repeatable commissions

### Multi-Agent Coordination

How agents with different roles work together:

- [Functional Types in Agent Taxonomy](../decisions/Functional%20Types%20in%20Agent%20Taxonomy.html) — decision: stewards, orchestrators, workers, boundary guardians
- [[Boundary Guardian as Distinct Agent Type]]↑ — decision: separating constraint enforcement from orchestration
- [[Orchestrator-Worker Separation in Personal Multi-Agent Systems]]↑ — pattern: context, attention, and cost ceilings force a two-tier agent hierarchy; cross-source corroborated across 4 independent systems
- [[Tiered Model Allocation by Task Type]]↑ — pattern: allocate models by task type (judgment vs execution), not agent seniority; enables Opus/Sonnet/Haiku tiering
- [[File-Directory Message Queue for Agent Coordination]]↑ — pattern: filesystem directories as message queues; inspectable with standard tools, zero infrastructure
- [Task Instruction and Role Specialization as Agent Configuration Layers](../models/Task%20Instruction%20and%20Role%20Specialization%20as%20Agent%20Configuration%20Layers.html) — model: AGENTS.md and persona files are complementary layers
- [Augmentation Over Autonomy in Agent Architecture](../decisions/Augmentation%20Over%20Autonomy%20in%20Agent%20Architecture.html) — decision: commission architecture operates as augmentation; escalation protocol for intellectual judgments
- [[Session-Invoked Versus Heartbeat-Driven Agent Initiative]]↑ — decision: this estate chose session-invoked initiative; agents have no autonomous capability between sessions
- [Structured Disagreement Through Persona Review](../patterns/Structured%20Disagreement%20Through%20Persona%20Review.html) — pattern: multiple persona perspectives surface disagreements that single-agent review misses
- [[Relay Tax in Supervisor-Subagent Pipelines]]↑ — pattern: information degrades at each supervisor relay hop; direct file access preserves context integrity
- [[Brief as Inbox Not Repository]]↑ — pattern: inter-agent channels need routing destinations and item lifetimes; without both they become accumulation layers
- [[The Brief-First Principle]]↑ — pattern: read the principal's intent before assessing the environment; survey without brief wastes context on wrong priorities
- [[Commission Carries the Knowledge]]↑ — pattern: specialize by operation when content is uniform; by commission when operations are uniform
- [[Close-Out Momentum Failure]]↑ — anti-pattern: obligations after substantive work get compressed proportionally to the work that preceded them

### Commission Architecture

How bounded work is delegated, verified, and returned:

- [[Queue-Mediated Commissioning]]↑ — pattern: queues as commissioning contract between orchestrator and worker; decouples deciding from doing
- [[Self-Commission as Tactical Authority]]↑ — decision: tactical coordinators may queue work for their own future sessions; priority hierarchy prevents authority creep
- [[Git Commit as Proof of Work]]↑ — pattern: require workers to produce git commits as machine-verifiable proof of completion
- [[Structured JSON Schema for Commission Returns]]↑ — pattern: typed return schemas per commission type enable programmatic routing of worker results
- [[Worker-to-Supervisor Handoff Protocol]]↑ — model: seven-element structured report (status, proof, findings, queue discoveries, template feedback, proposed improvements, dependencies)
- [[Human-Gated Self-Improvement via Reflection Files]]↑ — pattern: agents propose improvements to a staging file; humans review and merge approved learnings into authoritative configuration

### Process Failure Modes

How structured agent processes fail to produce their intended output:

- [[Compliance Surrogation]]↑ — pattern: when filling the form feels like doing the work but no artifact gets written; compliance with process structure unconsciously replaces the durable output the process exists to produce
- [[The Red Tape Spiral]]↑ — pattern: the self-reinforcing cycle where structural additions in response to failures produce more structure that causes more failures
- [[Context Pressure Amplifies Structural Compliance]]↑ — pattern: context window limits cause agents to favor cheap compliance execution over expensive output production
- [[Mechanical Check Rationalization]]↑ — anti-pattern: agent rationalizes away mechanical verification results instead of stopping; the analysis functions as evasion
- [[Structural Accretion Lifecycle]]↑ — pattern: simple → accrete → surrogate → crisis → simplify; the lifecycle that produces and resolves compliance surrogation

### Agent Learning and Reflection

How agents accumulate and distill operational experience:

- [[Two-Tier Memory with Explicit Curation]]↑ — pattern: raw capture tier (fast, append-only) feeding curated reference tier (slow, distilled) through explicit promotion
- [[Separate Reflective Sessions from Operational Sessions]]↑ — pattern: dedicated reflection time prevents operational crowding; task execution and pattern-finding need separate schedules
- [[First Invocation as Design Probe]]↑ — pattern: a new agent's first session reveals what the agent file didn't teach; frame it as design, not production
- [[Exemplar Comparison as Convention Extraction]]↑ — pattern: compare most-evolved instance against siblings; frequency of absence determines convention tier
- [[Presence-Based Extension Point]]↑ — pattern: skill checks for project-local file at known path; reads if present, skips silently if absent
- [[Context-Rich Rules Over Bare Imperatives]]↑ — pattern: rules with rationale and failure mode descriptions outperform bare imperatives; validated by Lawson's Cron Incident and this estate's "Why This Rule Exists" convention
- [[Design-Driven Versus Incident-Driven Rule Evolution]]↑ — decision: design-driven as foundation with incident-driven refinement as feedback loop

### Architectural Models

Meta-level explanations of why agent systems converge:

- [[Structural Attractors in Personal Multi-Agent System Design Space]]↑ — model: six structural constraints (context/attention/cost ceilings, inspectability, memory decay, operational crowding) generate predictable convergent solutions
- [[Autonomy-Safety Trade-Off Spectrum in Personal Agent Systems]]↑ — model: spectrum from session-invoked to heartbeat-driven to conditional initiative; key variable is observability, not autonomy level
- [[Continuous Intake vs Event-Driven Agents]]↑ — model: three intake patterns (continuous, event-driven, architectural inquiry) map to three workstream types

### Naming Discipline

- [[Vocabulary Search Before Naming]]↑ — principle: search existing vocabulary before proposing a name
- [[Propose Multi-Word Terms from the Start]]↑ — principle: name with at least two words immediately
- [[Session Length as Tactical Variable]]↑ — principle: short sessions with clean handoffs outperform long degrading sessions; optimize for reliable progress
- [[Topology Determines Authority]]↑ — principle: commission topology determines authority relationship, not persona identity; same agent operates differently on main vs worktree

### Vocabulary

- [[Agent Harness]]↑ — gloss: the infrastructure wrapping an LLM (context architecture, execution guardrails, memory); distinct from both model and prompt
- [[Agent-Computer Interface as Designed Cognitive Environment]]↑ — gloss: abstraction layer between agent and environment (SWE-agent); 64% improvement from interface design alone
- [[Scaffolding as Agent Continuity Infrastructure]]↑ — gloss: cross-session continuity infrastructure (progress files, feature lists, startup scripts); subset of harness
- [[Two-Part Architecture as Initializer-Executor Split]]↑ — gloss: Anthropic's pattern splitting setup (initializer) from execution (coding agent)
- [[Feature List as Cognitive Anchor]]↑ — gloss: structured file with boolean completion status preventing premature victory declaration
- [[Mechanical Architecture Enforcement]]↑ — gloss: encoding constraints as automated checks (linters, structural tests) rather than human review
- [[Environment Audit as Agent Diagnostic]]↑ — gloss: five diagnostic questions for underperforming agent systems; debug the environment, not the agent
- [[Spec First as Repository Knowledge Discipline]]↑ — gloss: all agent-relevant knowledge encoded as machine-readable repo files
- [[Integrated Feedback Loops for Agent Systems]]↑ — gloss: tightening the gap between action and consequence at every workflow point
- [[Compaction as Context Window Management]]↑ — gloss: summarizing old context within a session; necessary but insufficient without scaffolding
- [[Git Worktree Isolation as Agent Sandbox]]↑ — gloss: one agent, one worktree; filesystem-level isolation for parallel agent work
- [[The Ralph Loop]]↑ — gloss: Osmani's stateless-but-iterative development pattern (pick task, implement, validate, commit, reset context)
- [[Beads (Flywheel Methodology)]]↑ — gloss: Emanuel's self-contained work units with embedded context and dependency tracking

### Boundaries

- [[Delegated Decision Authority Spectrum]]↑ — boundary: where agent authority begins and ends
- [[Automated Gardening Trust Problem]]↑ — inquiry: can agents garden their own instructions? (open)

### Open Inquiries

- [[Agent Orchestration Architecture for a Personal Knowledge Estate]]↑ — parent inquiry: what orchestration architecture best serves a personal knowledge estate?
- [[What Are the Dynamics Behind Orchestrator Count Convergence]]↑ — why do independent systems converge on 3-8 orchestrators?
- [[When Does Markdown-as-State Break Down]]↑ — at what scale or complexity does plain text agent state fail?
- [[What Is Conditional Initiative and How Would It Work]]↑ — synthesis of heartbeat-driven initiative with safety governance
- [[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑ — what behavioral dimensions persona files should cover (open)
- [[Naming Distinctiveness in Agent and Garden Architecture]]↑ — whether naming conventions produce enough differentiation (open)
- [[Worker Architecture Symmetry Across Precincts]]↑ — is the create/research/maintain triad structural or coincidental across precincts?
- [[Shared State Patterns for Multi-Agent Estates]]↑ — estate has one-to-one communication but no one-to-many or shared-mutable-state patterns

## Candidate Forms

Patterns and concepts identified but not yet extracted:

### Patterns

- Commission as Bounded Work Assignment — what makes a commission distinct from a general task
- Ghost Link as Garden Gap Signal — unresolved wikilinks signal garden planning needs, not lint errors

### Models

- Commission Lifecycle — phases from intake through close-out
- Orchestrator-Executor Trust Model — what the Groundskeeper delegates and what it retains

### Inquiries

- Group Deliberation Mechanism — practical mechanism when an agent hits a group-deliberative boundary
- Agentic Pattern Language Completeness — how many named patterns constitute a sufficient pattern language?

## Open Questions

- How should Agentic Architecture relate to [Deep Context Architecture](Deep%20Context%20Architecture.html) as a sub-domain? Many patterns here are instantiations of deeper Deep Context Architecture principles in an agentic context.
- Should the commission architecture have its own domain page, or does it live as a subdomain of Agentic Architecture?
- What's the right granularity for persona differentiation? The Groundskeeper-Gardener-Chancellor-Seneschal pattern emerged empirically; it hasn't been validated against alternative role structures.

## Sources

- [Augmentation Over Autonomy in Agent Architecture](../decisions/Augmentation%20Over%20Autonomy%20in%20Agent%20Architecture.html) — founding decision for the commission architecture
- [[systematicls (2026) World-Class Agentic Engineering]]↑ — practitioner guide; independent validation of context management and rule/skill lifecycle
- [[Rajasekaran (2025) Effective Context Engineering for AI Agents]]↑ — Anthropic's engineering guide on attention budgets and sub-agent isolation
- [[rohit4verse (2026) The Harness Is Everything]]↑ — synthesis of harness-over-model insight; source for 9 new vocabulary glosses (ACI, scaffolding, two-agent architecture, feature list, mechanical enforcement, environment audit, spec first, feedback loops, compaction, worktree isolation)
- Deep Context Garden commission sessions (2026-03) — empirical source for the shearing layers and config-state conflation patterns

## Relations

- relates_to::[Deep Context Architecture](Deep%20Context%20Architecture.html)
  - Deep Context Architecture defines the knowledge architecture the garden implements; Agentic Architecture defines the agent system that operates within it. Many patterns in this domain are agentic instantiations of Deep Context Architecture principles.

- relates_to::[[Self-Sovereign Identity]]↑
  - The principal authority framework from agency law applies to agent systems as well as identity systems. Authority delegation, escalation protocols, and the principal-agent relationship bridge both domains.

- relates_to::[[Synpraxis]]↑
  - Synpraxis addresses how independent agents achieve outcomes together; commission architecture is a specific synpractic pattern where Groundskeeper and Gardeners coordinate without constant synchronization.
