---
created: 2026-03-31
author: Christopher Allen
status: accepted
brief_summary: "Agent system prompts open with the medieval estate name plus professional archetype descriptors: 'You are the Groundskeeper — a knowledge curator and taxonomy coordinator.' The invented name serves the human user (estate metaphor coherence); the archetype anchor activates stronger behavioral patterns in the LLM (per Assistant Axis research showing professional roles cluster assistant-aligned). Three approaches considered: subtitle anchoring (adopted), trait composition (rejected), leave as-is (rejected)."
tagline: "Medieval name for the human, professional archetype for the model — subtitle anchoring activates richer behavior"
---

- is_a::[[Decision Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Deep Context Architecture]]
- in_precinct::[[Garden Precinct]]

# Subtitle Anchoring for Persona Activation

## Context

Estate agent system prompts need to establish identity. The medieval estate names (Groundskeeper, Chamberlain, Seneschal) serve the human user — they place the agent within the estate metaphor and encode functional scope. But the LLM has limited pretraining data on medieval estate roles. "Groundskeeper" activates a thinner behavioral pattern than "information architect" or "knowledge curator" would, because the latter are well-represented professional archetypes with rich behavioral associations in training data.

The [[The Persona Selection Model|Anthropic Persona Selection Model]] explains why: post-training selects among characters already learned during pretraining. Named professional archetypes activate stronger behavioral clusters than invented or historically thin role names. The [[Persona Vectors and the Assistant Axis|Assistant Axis research]] further shows that professional roles cluster as assistant-aligned archetypes — they naturally produce helpful, structured, domain-expert behavior.

## Decision

Use **subtitle anchoring**: the medieval estate name plus professional archetype descriptors from the Assistant Axis 275 archetypes.

Format: "You are the [Estate Name] — a [archetype 1] and [archetype 2] for this knowledge [scope]."

Examples:
- "You are the Groundskeeper — a knowledge curator and taxonomy coordinator for this knowledge garden."
- "You are the Chamberlain — a tactical coordinator and session orchestrator for this knowledge estate."
- "You are the Seneschal — a strategic steward and architectural advisor for this knowledge estate."

The invented name serves human recognition; the archetype subtitle activates LLM behavioral patterns. Both operate simultaneously — the agent identifies as Groundskeeper (for the human) while behaving as a knowledge curator (for the model).

## Consequences

**Positive**: Richer behavioral activation without abandoning the estate metaphor. The subtitle compounds rather than conflicts — "Groundskeeper who is a knowledge curator" is a more specific position in persona space than either term alone.

**Negative**: Worker agents share archetypes. "Editor" appears in Gardener, Pruner, and Scribe definitions. The overlap may undermine specialization if the shared archetype activates a dominant behavioral cluster that overrides the role-specific instructions. This remains an open question.

**Trade-off**: The subtitle occupies system prompt space that could hold behavioral instructions. The hypothesis is that archetype activation is more token-efficient than explicit behavioral specification — a few archetype words activate a cluster of behaviors that would otherwise require paragraphs of instruction.

## Alternatives Considered

**Trait composition**: Define each persona through a list of independent behavioral traits ("skeptical, collaborative, deferential to evidence"). Rejected because the Anthropic research shows cross-trait inference — traits are not independent dimensions but cluster together. A trait list may contain internally inconsistent combinations that the model resolves in unpredictable ways.

**Leave as-is**: Use only the medieval estate name without archetype anchoring. Rejected because the research shows measurable activation differences between well-represented and novel names. Leaving the archetype unspecified means the model selects from whatever "Groundskeeper" activates in its persona space — likely a mix of literal groundskeeper (building maintenance) and metaphorical gardening associations, without the knowledge-work behavioral patterns the role requires.

## Sources

- Chatelaine Session 10 + Groundskeeper Session 71 (2026-03-26) — subtitle anchoring adopted
- [[The Persona Selection Model]] — mechanistic theory of why archetype names activate richer behavior
- [[Persona Vectors and the Assistant Axis]] — empirical research on professional role clustering

## Relations

- implements::[[Naming Carries Relational Weight]]
  - Subtitle anchoring is naming-as-architecture applied to system prompt design: the archetype subtitle is an architectural choice that activates specific behavioral clusters
- relates_to::[[English Stewardship Vocabulary Over Latin or Corporate Terms]]
  - The medieval names require subtitle anchoring precisely because feudal English terms are thinner in pretraining data than professional archetypes
- relates_to::[[Vocabulary Collision Navigation]]
  - The dual-naming pattern (estate name + professional archetype) is itself a vocabulary collision navigation: two naming traditions serving different audiences within the same prompt
- relates_to::[[Six Approaches to Persona Architecture — Synthesis]]
  - The synthesis's Axis 2 (diversity mechanisms) discusses archetype anchoring as the estate's diversity strategy
