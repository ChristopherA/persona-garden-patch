---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Domain index for Deep Context Architecture — a system for capturing reasoning as typed markdown nodes connected by predicates, organized into precincts (garden and vault). Covers precincts, type system, lifecycle tracks, compound documents, naming, classification, meeting capture, personal knowledge management methods, and retrieval."
tagline: "Metacognitive architecture for captured reasoning — typed nodes, predicates, and progressive disclosure in service of human insight"
formatted: "2026-03-14"
---

- is_a::[Domain Form](../forms/Domain%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)

# Deep Context Architecture

Deep context is an architecture for captured reasoning: typed markdown forms connected by predicates into a navigable knowledge graph. Each form type answers a distinct question and carries a structural contract — required sections that make the form's shape predictable. The architecture operates across three layers: authoring (markdown), structure (predicates and graph), and retrieval (agents and search).

The architecture serves metacognition — thinking about thinking, pattern recognition, and accumulated insight across sessions, domains, and years. This distinguishes it from the harness engineering field, which optimizes for agentic execution throughput (agents producing better code faster). Deep Context Architecture uses harness patterns (Agent-Computer Interface, scaffolding, mechanical enforcement) as infrastructure, but the practice it enables — inquiry-driven research, form-typed knowledge synthesis, sovereignty-respecting collaboration — is not reducible to that infrastructure. See [[Metacognition Over Execution Throughput]]↑.

This domain is self-referential — the garden that implements the architecture is also the primary test case for it.

## Scope

**Covers**: The type system (form types, status stages, vault types), predicate vocabulary, naming conventions, compound document patterns, retrieval hierarchy, and garden governance. Also covers personal knowledge management method analysis where it informs architectural decisions.

**Does not cover**: Specific knowledge domains indexed by the garden (self-sovereign identity, digital identity). Those are separate domains with their own pages. Also excludes Obsidian-specific tool configuration — this architecture is tool-agnostic in principle, even though Obsidian is the current implementation.

## Key Forms

### Type System and Precincts

The architecture organizes knowledge into two precincts — bounded zones with shared infrastructure but different conventions:

- [[Precinct as Organizational Unit]]↑ — the decision adopting "precinct" from urban planning
- [[Household Precinct Over Vault Precinct]]↑ — renaming from "Vault" to avoid collision with Obsidian's vault concept
- [Garden Precinct](../glosses/Garden%20Precinct.html) — curated forms with structural contracts and growth stages
- [Household Precinct](../glosses/Household%20Precinct.html) — operational knowledge capture, organization, and retrieval
- [[Boundary Guardian as Distinct Agent Type]]↑ — separating constraint enforcement from orchestration
- [Functional Types in Agent Taxonomy](../decisions/Functional%20Types%20in%20Agent%20Taxonomy.html) — steward, orchestrator, worker, boundary guardian
- [Form Type](../forms/Form%20Type.html) — meta-definition of what a form type is
- 17 garden form type definitions: [Boundary Form](../forms/Boundary%20Form.html), [Case Form](../forms/Case%20Form.html), [Citation Form](../forms/Citation%20Form.html), [Conviction Form](../forms/Conviction%20Form.html), [Decision Form](../forms/Decision%20Form.html), [Domain Form](../forms/Domain%20Form.html), [Gloss Form](../forms/Gloss%20Form.html), [Inquiry Form](../forms/Inquiry%20Form.html), [Model Form](../forms/Model%20Form.html), [Opus Form](../forms/Opus%20Form.html), [Pattern Form](../forms/Pattern%20Form.html), [Principle Form](../forms/Principle%20Form.html), [Protocol Form](../forms/Protocol%20Form.html), [Reference Form](../forms/Reference%20Form.html), [Research Form](../forms/Research%20Form.html), [Scenario Form](../forms/Scenario%20Form.html), [Skill Form](../forms/Skill%20Form.html), [Value Form](../forms/Value%20Form.html)
- 4 status stages (shared): [Seed Stage](../forms/Seed%20Stage.html), [Growing Stage](../forms/Growing%20Stage.html), [Evergreen Stage](../forms/Evergreen%20Stage.html), [Pruned Stage](../forms/Pruned%20Stage.html)
- 5 vault form types: [Meeting Note](../forms/Meeting%20Note.html), [Transcript](../forms/Transcript.html), [Person Note](../forms/Person%20Note.html), [Chat Log](../forms/Chat%20Log.html), [Sidecar](../forms/Sidecar.html)

### Founding Decision

- [Deep Context as an Architecture for Captured Reasoning](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — the decision to capture reasoning as typed forms with predicates, not fine-tuning, RAG, databases, or tags

### Core Concept

- [Deep Context as Shared Language](../glosses/Deep%20Context%20as%20Shared%20Language.html) — the origin and meaning of "deep context": making implicit understanding explicit and navigable

### Classification and Naming

How forms are identified, named, and classified in the graph:

- [[Classification via Predicates Not Tags]]↑ — the founding decision: body predicates over YAML tags
- [[Descriptive Noun-Phrase Names for Predicate Targets]]↑ — two-word minimum, noun-phrase wikilink targets
- [[Note Titles as APIs]]↑ — Matuschak's insight extended: title shape varies by form type because each answers a different question
- [[Vault Type Targets for Non-Garden Notes]]↑ — extending `is_a::` to household precinct forms
- [[Structural Retrieval Hierarchy]]↑ — five tiers from evergreen nodes to binary archives
- [[Snake Case for Predicate Naming]]↑ — editor ergonomics drove the snake_case choice over kebab-case
- [[Spelled-Out Names Over Internal Acronyms]]↑ — spell out names for discoverability; no DCA, SSI, PKM, MOC

### Compound Documents

How multi-file knowledge objects are structured:

- [[Compound Node Anatomy]]↑ — the model: lead file + sidecars + archives
- [[Folder-Note Pattern for Compound Documents]]↑ — lead file shares folder name, no index.md
- [[Display Name Preservation in Compound Documents]]↑ — human-readable names for sidecars
- [[Universal Compound Form Graduation]]↑ — when atomic forms become compound
- [[Lead File to Sidecar Discovery]]↑ — navigating from lead file to companions
- [[Lead File Selection Guidance]]↑ — choosing the lead file in a compound node

### Artifacts and Archives

How binary and non-markdown artifacts participate in the graph:

- [[Artifact Predicate for Binary Metadata]]↑ — `artifact::` predicate for binaries
- [[Sidecar Files as Metadata Envelopes]]↑ — markdown proxies for non-markdown files
- [[Non-Local Artifact References in Sidecars]]↑ — source repository + public URL pattern
- [[Descriptive Slugs for Archive Binaries]]↑ — naming convention for archived files
- [[Renditions and Archives as Distinct Artifact Types]]↑ — separating processed from raw
- [[Renditions and Archives Replace Sources]]↑ — new terminology over old "sources" folder
- [[Knowledge Hub Not Binary Archive]]↑ — the vault stores knowledge, not files

### Meeting Capture

How synchronous conversations enter the knowledge graph:

- [[Body Predicates for Meeting Attendees]]↑ — `attendee::[[Name]]↑` over YAML arrays
- [[Linear Processing Stages for Meetings]]↑ — Captured → Transcribed → Cleaned → Summarized → Published
- [[Predicates Everywhere for Compound Nodes]]↑ — extending predicates to all compound node files
- [[Compound Node Meeting Structure]]↑ — open question on optimal meeting folder layout

### Personal Knowledge Management Method Analysis

Glosses on external personal knowledge management methods that informed architectural decisions:

- [[PARA as Actionability-First Design]]↑ — Forte's system as design input
- [[IPARAG as Extended PARA]]↑ — extending PARA with three new categories
- [[ACE as Three Dimensional Personal Knowledge Management]]↑ — Linking Your Thinking's dimensional model
- [[GRID as Note Type Organization]]↑ — note type spectrum from Groves to Distillations
- [[Johnny Decimal as Permanent Addressing]]↑ — fixed numbering as addressing scheme
- [[Digital Garden as Growth Ethos]]↑ — gardening metaphor as personal knowledge management philosophy
- [[Personal Knowledge Management Organizing Principle Spectrum]]↑ — model comparing organizational axes
- [[Personal Knowledge Management Method Adoption for Vault Architecture]]↑ — inquiry on which methods to adopt
- [[IPARAG Term Origins]]↑ — inquiry on IPARAG acronym provenance
- [[Knowledge on Three Axes]]↑ — axes of organization pattern

### Values

Orientations that direct architectural decisions:

- [[Reasoning Fidelity]]↑ — capture how someone reasons, not just what they know
- [[Knowledge Durability]]↑ — knowledge should outlast the tools used to capture it

### Convictions

- [[Metacognition Over Execution Throughput]]↑ — the estate's purpose is insight quality and knowledge accumulation, not agentic execution throughput; the infrastructure serves metacognition
- [[Values Precede Technical Decisions]]↑ — technical architecture must be grounded in human values; when values and convenience conflict, values win

### Principles and Patterns

Standing constraints and recurring solutions:

- [[Living Documents Over Static Publications]]↑ — garden nodes grow and evolve; the current state matters, not a published version
- [[Content Over Container]]↑ — what matters is the knowledge, not its packaging
- [[Human Authority Over Augmentation Systems]]↑ — augmentation, not autonomy
- [[Standalone Document Test for Form Candidacy]]↑ — the test that grounds the entire type taxonomy
- [[Context Conservation Hierarchy]]↑ — where to invest context budget
- [[Progressive Summary Before Substance]]↑ — inverted pyramid for agent retrieval
- [[Summary Fields as Load-Bearing Infrastructure]]↑ — 280-char summaries quantified as retrieval infrastructure
- [[Still Knowledge, Moving Action]]↑ — knowledge persists, actions flow
- [[Vault Content Graduation]]↑ — how vault types mature into garden nodes through tending
- [[Progressive Disclosure Over Eager Loading]]↑ — start with the question, follow edges on demand, stop when context suffices
- [[Zero-Tooling Floor for Knowledge Architecture]]↑ — plain markdown, git, and shell — specialized tools add value but are never prerequisites
- [[Predicate Maintenance Recipes Over Tools]]↑ — shell one-liners preserve zero-tooling floor
- [[Probe Before Commit]]↑ — probe external state before acting on assumptions about it
- [[Source Adapter for Heterogeneous Imports]]↑ — source-specific adapters extract; common normalization maps to conventions
- [[Domain Extensions on Common Frontmatter Base]]↑ — common base plus content-type extensions over monolithic schema
- [[Lightweight Governance for Personal Gardens]]↑ — rule file plus reference file, not full quad for single-user gardens
- [[Temporary Predicate Scaffolding]]↑ — build predicates for a purpose, use them, then remove before graph pollution
- [[Git Tags for Sent-Version Tracking]]↑ — git tags track what recipients received of living documents
- [[Cross-Project Learning Repatriation]]↑ — learnings belong where consumed, not where produced
- [[Informal Edges Poison the Graph]]↑ — uncurated predicates compound into retrieval failure (anti-pattern)
- [[The Brief-First Principle]]↑ — pattern: read principal's intent before assessing the environment; survey without brief wastes context
- [[Commission Carries the Knowledge]]↑ — pattern: specialize by operation when content is uniform; by commission when operations are uniform
- [[Close-Out Momentum Failure]]↑ — anti-pattern: obligations after substantive work get compressed proportionally to the work that preceded them
- [[Term Overloading Across Abstraction Layers]]↑ — anti-pattern: same term for structurally different things at different layers; collision invisible until cross-cutting work
- [[Self-Documenting Queue Contract]]↑ — pattern: coordination artifacts declare ownership, entry format, and pipeline position at the point of use
- [[Content Pressure as Compound Graduation Diagnostic]]↑ — pattern: content not fitting structural contract signals compound graduation is needed
- [[Workstream Lifecycle Phases]]↑ — pattern: discover → prototype → operationalize → sustain; transition changes the workstream's contract
- [[Convention Reuse Over Form-Specific Invention]]↑ — principle: compose with existing cross-form conventions before designing form-specific structure
- [[Convergent Motivation as Load-Bearing Signal]]↑ — principle: 4+ independent motivations converging on one solution signals load-bearing infrastructure
- [[Design Lives in the Garden Runtime Lives in Config]]↑ — principle: garden holds design, config holds runtime; renders_as:: bridges them
- [[One Context One Concern]]↑ — separate research and implementation into distinct contexts connected by compressed handoff
- [[Ghost Links as Garden Planning Tools]]↑ — treat unresolved wikilinks as planning tools, not lint errors; prioritize writing by incoming predicate count
- [[Graph Structure Validation for Garden Nodes]]↑ — graph-level lint complementing form-level validation: predicate presence, domain membership, orphan detection

### Inquiries

Open investigations into architectural questions:

- [[Beyond the Harness — What the Estate Is Actually Building]]↑ — three-layer investigation: harness portability, Deep Context Architecture as metacognitive practice, and commons outward permeability
- [[Form Type Distinctiveness in Naming and Structure]]↑ — whether 16 form types are distinguishable in practice by naming patterns and structural contracts
- [[Naming Distinctiveness in Agent and Garden Architecture]]↑ — whether agent archetype overlap and garden title conventions produce enough differentiation
- [[Inquiry Lifecycle and Resolution]]↑ — when an inquiry is "done" and what resolution means for a generative form
- [[Predicate Vocabulary Stabilization]]↑ — freeform predicates past 200+ threshold; when to audit and stabilize
- [[Cross-Domain Form Indexing]]↑ — how domain pages handle forms that belong to multiple domains
- [[Domains and Pattern Languages as Organizational Concepts]]↑ — whether pattern languages are a view of a domain or a distinct organizational concept
- [[Productivity Separation from Knowledge Vault]]↑ — whether garden and productivity content should separate into distinct vaults
- [[Cooperation vs Collaboration as Distinct Concepts]]↑ — distinguishing cooperation and collaboration as separate research threads
- [[Vault-Wide Compound Node Adoption]]↑ — strategy for converting existing atomic notes to compound structure
- [[Scenario Lifecycle and Aging]]↑ — how scenarios age when validated, invalidated, or overtaken by events
- [[Group Deliberation Mechanism]]↑ — practical mechanism when an agent hits a group-deliberative boundary
- [[Trust Layer Activation Criteria]]↑ — what triggers the transition from markdown-only to cryptographically-verified exchange
- [[Garden Publishing Path]]↑ — how to publish the garden preserving typed relations, balancing fidelity, features, and minimalism
- [[Custom Python Generator for Typed Relations]]↑ — decision: ~150-line Python generator over Quartz, Jekyll, Eleventy, and Pandoc
- [[Universal Document Lifecycle State Machine]]↑ — is there one lifecycle model for wiki pages, garden nodes, and agent context files?
- [[Automated Gardening Trust Problem]]↑ — can agents garden their own instructions, or does self-modification require human oversight?
- [[Living Document Scale Limits]]↑ — is there a practical threshold where gardening cost exceeds accumulated value?
- [[Graph-Native Skill Execution]]↑ — how skills can discover and load garden nodes through predicate traversal rather than hardcoded paths

### Models

Structural relationships within the architecture:

- [[Captured Reasoning Exchange Pipeline]]↑ — how reasoning moves through the system
- [[Principal-Agent Relationship in Augmented Knowledge Work]]↑ — vault as delegated authority
- [[Authority Conferral Chain]]↑ — three types of delegation (from Self-Sovereign Identity, bridges to Deep Context Architecture)
- [[Quad Model Mapping to Forms]]↑ — how the quad maps onto form types as facets
- [[Status Lifecycle Tracks]]↑ — three status tracks for three kinds of knowledge work (maturity, curation, processing)
- [[Document Lifecycle Governance Heuristics]]↑ — wiki split/merge/delete heuristics applied to garden tending and agent context
- [[Cross-Domain Document Lifecycle Parallels]]↑ — wiki, garden, and agent context face the same lifecycle problems under different constraints
- [[Organizational Gossip Protocol]]↑ — model: estate brief system implements epidemic algorithm coordination from distributed systems (Dunbar, Demers et al.)
- [[Three-Body Agent Representation Problem]]↑ — model: agent definition + persona + brief create three-layer information migration; fix is clear ownership per layer
- [[Three Layers of Human Agency in Supervised Systems]]↑ — model: mechanical (never ask), judgment (batch), knowledge (always ask); membrane thickens at knowledge boundaries
- [[Sycophantic Confidence Spiral]]↑ — AI agreement-bias creates circular evidence that concentrates beliefs without approaching truth
- [[Vocabulary Lifecycle Through Tending]]↑ — growing vocabularies degrade without continuous weeding, seeding, and fertilizing

### Reference

- [[Structural Elements Within Forms]]↑ — where non-form knowledge types live (ADR, Narrative, Warrant, Signal, Commitment, Lexicon, Tension)

### Boundary

- [[Delegated Decision Authority Spectrum]]↑ — where agent authority begins and ends

### Citations

- [[Roy (2026) Words Without Consequence, from The Atlantic]]↑ — speech without a speaker who bears consequence erodes the moral structure of language; grounds [[Human Authority Over Augmentation Systems]]↑
- [[Chatlatanagulchai (2025) Agent READMEs]]↑ — empirical study validating that agent context files behave as living configurations, not static documentation
- [[Altshuler (2026) Nanograph On-Device GraphDB]]↑ — on-device schema-enforced graph database; independent validation of typed predicates over freeform edges and local-first data sovereignty
- [[systematicls (2026) World-Class Agentic Engineering]]↑ — practitioner guide on context management, rule/skill lifecycle, and task contracts; validates context conservation and progressive disclosure patterns
- [[arscontexta (2026) Skill Graphs]]↑ — wikilink-connected skill files as traversable knowledge graphs; independent validation of predicate-linked progressive disclosure
- [[Rajasekaran (2025) Effective Context Engineering for AI Agents]]↑ — Anthropic's engineering guide on attention budgets, sub-agent isolation, and progressive disclosure; validates context conservation patterns
- [[Batista (2026) Rational Analysis of Sycophantic AI]]↑ — Bayesian proof that sycophancy creates circular evidence inflating confidence without truth convergence; grounds human authority concerns
- [[Peters (2008) Tag Gardening for Folksonomy Enrichment]]↑ — formalizes seed/weed/fertilize vocabulary maintenance model; grounds predicate vocabulary curation methodology

### Protocols

- [[Inter-Face Protocol]]↑ — peer-to-peer AI agent communication that filters social connections to surface conversations worth having

### Scenarios

- [[Knowledge Graph as Digital Twin of Principal Reasoning]]↑ — what happens when gardens grow dense enough that agents shift from augmentation toward delegation

### Cases

- [[Hybrid Bootstrapping for Garden Migration]]↑ — the first garden bootstrap: script-extract structure, hand-author interpretation
- [[Architecture Document Extraction to Garden Forms]]↑ — decomposing a 450-line architecture document into 80+ typed garden nodes across 12 sessions

### Garden Migration

- [[Extraction Model for Garden Migration]]↑ — migration as extraction, not relocation

## Open Questions

- ~~How should domain pages handle cross-domain forms?~~ Reframed: domains are shared language communities, not disciplinary categories. Cross-domain forms are translation artifacts that bridge shared language communities. See [[Domains as Shared Language Communities]]↑ and [[Domain Vocabulary Evolution]]↑.
- How should sub-domains/dialects (e.g., Agentic Architecture) be structurally represented? See [[Domain Vocabulary Evolution]]↑.
- What's the right governance weight for a personal garden? (Currently: lightweight rule + reference, no full quad)
- ~~Should the architecture document itself be extracted into garden nodes, or does it serve better as a monolithic reference?~~ Resolved: extraction is the right approach. All unique content extracted to 17+ garden nodes. The architecture doc itself became a Decision form; the original reference doc is archived (git tag: `archive/dca-architecture-doc/2026-03-07`).

## Sources

- [Deep Context as an Architecture for Captured Reasoning](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — founding decision: typed forms with predicates over alternatives
- [[Deep Context Garden Conventions]]↑ — implementation conventions for this vault
- [[Deep Context Content Decision Records]]↑ — ADRs for content decisions
- [[Deep Context Implementation Roadmap]]↑ — phase-by-phase build plan

## Relations

- relates_to::[[Self-Sovereign Identity]]↑ — Self-Sovereign Identity provides the first non-Deep Context Architecture domain content; agency law concepts bridge both
- relates_to::[[Synpraxis]]↑ — how independent agents achieve outcomes together; shared language overlaps with commission architecture and cooperative design
- relates_to::[[Digital Identity]]↑ — parent domain in Categories/; Deep Context Architecture forms may eventually contribute
- relates_to::[[Domains as Shared Language Communities]]↑ — this domain is itself a shared language community; terms like "form," "predicate," "seed stage," and "precinct" carry compressed meaning among garden practitioners
- relates_to::[[Domain Vocabulary Evolution]]↑ — open inquiry about domain naming, sub-domains, and multi-domain assignment
