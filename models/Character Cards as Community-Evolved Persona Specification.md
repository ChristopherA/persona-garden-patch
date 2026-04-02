---
created: 2026-03-26
author: Christopher Allen
brief_summary: "Character Cards is a V2/V3 open specification for portable AI persona definition, originating in the roleplay AI community. Personas are encoded as JSON metadata embedded in PNG image files, with a lorebook mechanism for conditional knowledge activation and V3 decorator syntax for advanced prompt insertion control."
tagline: "Roleplay community's portable persona format: avatar image as identity container"
---

- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Character Cards as Community-Evolved Persona Specification

The roleplay AI community independently developed a structured persona specification format called Character Cards. Now at Version 3, the specification predates the agentic AI industry's persona work and represents a parallel evolution from the same problem: how to portably define an AI personality.

## Structure

Character cards are stored as PNG or APNG image files with JSON metadata embedded in PNG tEXt chunks (the `ccv3` chunk). The character's avatar image is the transport container for the full personality specification — a design choice that prioritizes shareability over readability.

**The V2/V3 specification includes**:

| Component | Purpose |
|-----------|---------|
| Name, description, personality | Core identity |
| First message, alternate greetings | Conversation initialization |
| System prompt | Behavioral instructions |
| Post-history instructions | Persistent behavioral constraints |
| Lorebook (embedded) | Contextual knowledge activated by keywords |
| Assets | Alternative icons, backgrounds, emotions |
| Decorators (V3) | Advanced activation rules: turn-based triggers, conditional insertion |

**The lorebook mechanism** is the most distinctive contribution: a series of keyword-activated entries that insert relevant context into the prompt only when triggered by conversation content. "Character cards define who the AI is. Lorebooks define what the AI knows." This separation — identity from knowledge — parallels the SOUL.md/IDENTITY.md split in [\[\[SoulSpec Portable Agent Identity Standard\]\]](SoulSpec%20Portable%20Agent%20Identity%20Standard.html) but adds a conditional activation layer that neither SoulSpec nor the garden persona architecture provides.

Lorebooks stack: a character-level book layers on top of a world-level book, enabling compositional knowledge. An agent specializing in medieval history can carry a character-level lorebook for personal backstory and activate a world-level lorebook for period context when keywords trigger it.

**V3 additions**: The V3 specification adds decorator syntax for advanced features: activating entries only after a certain number of turns (preventing premature context injection), positioning content at specific locations in the prompt, and scoping entries to specific user personas embedded in the card. These extend conditional activation from keyword-based to turn-based and position-based.

## Cross-Format Comparison

| Format | Transport | Identity | Knowledge | Activation |
|--------|-----------|----------|-----------|------------|
| Character Cards V3 | PNG/APNG + JSON | Name + personality + system prompt | Lorebook (keyword/turn) | Conditional (keyword, turn, position) |
| SoulSpec | Markdown files | SOUL.md + IDENTITY.md | AGENTS.md | Always-on |
| Garden Persona Form | Obsidian markdown | Persona node | Agent file | Always-on |

Character cards evolved for interactive fiction; SoulSpec evolved for agentic coding tools; the garden persona form evolved for knowledge management agents. All three solve the same problem — portable behavioral identity specification — but optimize for different consumers and different interaction patterns.

## Boundaries

The character card specification assumes a single-user, single-agent interaction context. It does not address multi-agent coordination or the coordination limits that apply when multiple agents share a workspace. The lorebook activation mechanism assumes a long-running conversational context where turns accumulate; this maps poorly to stateless agent invocations.

The PNG transport format prioritizes shareability over auditability. Version control and diff tooling work poorly with binary containers. The metadata is human-readable only after extraction from the image file.

The specification does not address training-time persona embedding (Level 5 in [\[\[The Persona Spectrum from Role Label to Soul Document\]\]](The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html)). Character cards operate entirely at inference time, relying on the prompt to shape behavior rather than trained weights.

## Sources

- [Character Card Specification V2 — GitHub](https://github.com/malfoyslastname/character-card-spec-v2)
- [Character Card Specification V3 — GitHub](https://github.com/kwaroran/character-card-spec-v3/blob/main/SPEC_V3.md)
- [V3 Concepts — lorebook decorators and assets](https://github.com/kwaroran/character-card-spec-v3/blob/main/concepts.md)
- [Building Deep AI Characters: Using Lorebooks and Character Cards Together — HammerAI](https://www.hammerai.com/blog/building-deep-ai-characters)

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑
- relates_to::[\[\[SoulSpec Portable Agent Identity Standard\]\]](SoulSpec%20Portable%20Agent%20Identity%20Standard.html)
- relates_to::[\[\[The Persona Spectrum from Role Label to Soul Document\]\]](The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html)
- relates_to::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)
- relates_to::[Task Instruction and Role Specialization as Agent Configuration Layers](../models/Task%20Instruction%20and%20Role%20Specialization%20as%20Agent%20Configuration%20Layers.html)
- relates_to::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- relates_to::[[Conditional Knowledge Activation]]↑
- relates_to::[[Lorebook Pattern]]↑
