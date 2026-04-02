---
created: 2026-03-26
author: Christopher Allen
brief_summary: "A SOUL.md should answer behavioral questions, not identity assertions. Identity claims like 'professional and helpful' resolve nothing when tasks are ambiguous. Five behavioral questions—about obstacles, valuable output, disagreement, proactive surfacing, and failure interpretation—define agents that actually diverge."
tagline: "Behavioral specs resolve ambiguity; identity claims don't"
---

- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](Garden%20Precinct.html)

# Behavioral Questions vs Identity Assertions in Persona Design

**Source**: The SOUL.md pattern, articulated in the DEV Community post "SOUL.md: How We Gave Three AI Agents Distinct Personalities," confirmed by the OpenClaw framework's architecture and the broader practitioner literature on agent persona design.

The SOUL.md pattern's central claim: a persona specification should answer behavioral questions, not state identity. "Professional, helpful, and detail-oriented" tells an agent almost nothing useful. When a task is ambiguous, "helpful" does not resolve it. Behavioral specifications do.

## The Five Behavioral Questions

The SOUL.md pattern identifies five questions that a well-formed persona specification must answer:

1. What do I do when I hit an obstacle?
2. What determines whether my output is valuable vs. just filling a response?
3. When do I disagree, and how?
4. What earns proactive surfacing of a problem vs. waiting to be asked?
5. How do I interpret a failure?

These questions surface at decision points — moments when an agent must choose between two or more plausible next actions. Identity assertions like "I value quality" do not specify which action to take. Behavioral rules like "pause and confirm when scope is ambiguous" do.

## Three-Agent Divergence

The team at Nobody Agents built three agents with distinct personalities by extending a shared core (`SOUL_CORE.md`) with different answers to these questions:

- The **Executor** agent: "speed over caution, direction over permission"
- The **Orchestrator** agent: "pause and confirm when scope is ambiguous"
- The **Mobile** agent: "be the first to notice, not necessarily the first to act"

These specifications diverge at specific decision points. The Executor and the Orchestrator respond differently to scope ambiguity — one proceeds, the other stops. The Mobile agent's priority is detection, not action. Generic identity assertions would collapse these into a single behavior profile.

Generic personas also drive homogeneity across multi-agent systems: multiple agents converge on similar communication styles and risk tolerances. Behavioral specification prevents this convergence by defining rules that diverge precisely where differentiation matters.

## The SOUL Framework

The broader practitioner literature reinforces this through the SOUL framework (Style, Objectives, Understanding, Limits):

- **Style**: tone, vocabulary, sentence structure, formatting preferences
- **Objectives**: what the agent is trying to achieve
- **Understanding**: domain knowledge and context awareness
- **Limits**: what the agent should not do

The framework's claim — that how you define behavior matters more than which model you run — is supported by OpenClaw's architecture: SOUL.md defines personality, communication style, core values, and behavioral guardrails. IDENTITY.md handles metadata (what the agent looks like and what it's called). The separation enforces the behavioral/identity distinction structurally.

## Significance for Garden Personas

The garden's persona nodes already instantiate behavioral specification over identity assertion. "Prefer incremental change over large rewrites" and "when encountering gaps, create ghost links" are behavioral answers, not identity claims. The SOUL.md framing names what the garden is already doing and provides vocabulary for auditing whether a persona has achieved it.

The audit question for any garden persona: does each statement in the persona specification resolve an ambiguous situation, or does it merely describe character? Statements that resolve are behavioral. Statements that describe are identity.

## Sources

- [SOUL.md: How We Gave Three AI Agents Distinct Personalities — DEV Community](https://dev.to/nobody_agents/soulmd-how-we-gave-three-ai-agents-distinct-personalities-and-why-generic-personas-fail-54dg)
- [The Complete SOUL.md Template Guide — DEV Community](https://dev.to/tomleelive/the-complete-soulmd-template-guide-give-your-ai-agent-a-personality-3php)
- [SOUL.md and Identity — Designing Your Agent's Personality — Learn OpenClaw](https://learnopenclaw.com/core-concepts/soul-md)
- [How OpenClaw Implements Agent Identity: Soul, Persona, Multi-Agent — MMNTM](https://www.mmntm.net/articles/openclaw-identity-architecture)

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑

- relates_to::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)
  - Garden persona nodes are evaluated by whether they answer behavioral questions, not whether they assert identity.

- relates_to::[\[\[The Persona Spectrum from Role Label to Soul Document\]\]](../models/The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html)
  - The behavioral/identity distinction maps onto the spectrum: role labels are identity assertions; soul documents are behavioral specifications.

- relates_to::[Task Instruction and Role Specialization as Agent Configuration Layers](../models/Task%20Instruction%20and%20Role%20Specialization%20as%20Agent%20Configuration%20Layers.html)
  - Role specialization that uses identity assertions instead of behavioral rules is less effective at creating divergent agent behavior.

- relates_to::[\[\[Persona Drift Causes Detection and Prevention\]\]](../patterns/Persona%20Drift%20Causes%20Detection%20and%20Prevention.html)
  - Drift is harder to detect when the persona is defined by identity assertions — there is no behavioral anchor to compare against.

- relates_to::[\[\[SoulSpec Portable Agent Identity Standard\]\]](../models/SoulSpec%20Portable%20Agent%20Identity%20Standard.html)
  - SoulSpec adopts the SOUL/IDENTITY distinction at the portable standard level, separating behavioral guidelines from identity metadata.

- relates_to::[Structured Disagreement Through Persona Review](../patterns/Structured%20Disagreement%20Through%20Persona%20Review.html)
  - Productive disagreement between agents requires behavioral specification — identity-only personas cannot reliably produce distinct review stances.
