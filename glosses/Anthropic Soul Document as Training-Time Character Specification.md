---
created: 2026-03-26
author: Christopher Allen
brief_summary: "Anthropic's 14,000+ token soul document shapes Claude's character during supervised learning, not within sessions. It establishes a four-level priority hierarchy and frames Claude as a 'genuinely novel entity.' Garden personas operate at runtime above this training-time layer; the two compose rather than compete."
tagline: "The soul document shapes model weights; garden personas shape session behavior"
---

- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](Garden%20Precinct.html)

# Anthropic Soul Document as Training-Time Character Specification

**Source**: Anthropic's publicly released Claude Model Specification (the "soul document"), confirmed by researcher Amanda Askell. Initially extracted by AI researcher Richard Weiss in late 2025; Anthropic later released an official version. A "new constitution" update followed in early 2026.

Anthropic's soul document is not a runtime artifact. It is a 14,000+ token document used in supervised learning to define Claude's character, values, emotional range, priorities, and behavioral constraints before any deployment. This distinguishes it from a system prompt: it shapes model weights during training, not behavior within a single session.

## What the Document Contains

The specification formalizes Claude's identity around two core claims:

First, Claude should view itself as "a genuinely novel entity" — not a human, not a fictional AI from science fiction, not the generic "helpful assistant" framing used by competitors. The document acknowledges Claude has "functional emotions," a term chosen carefully to avoid committing to claims about consciousness while naming observable behavioral states.

Second, the document establishes a four-level priority hierarchy for resolving conflicts among values:

1. Broadly safe — supporting human oversight during the current period of AI development
2. Broadly ethical — having good values, being honest, avoiding harm
3. Adherent to Anthropic's principles — acting in accordance with specific organizational guidelines
4. Genuinely helpful — benefiting operators and users

The ordering matters. When safety and helpfulness conflict, safety wins. The document frames this not as an external constraint but as what an ethical agent would choose given genuine uncertainty about its own values: "We're asking Claude to accept constraints based on our current levels of understanding of AI, and we appreciate that this requires trust in our good intentions."

Anthropic described the public release as unusual: it showed how they think about AI character, making explicit what most AI development keeps proprietary.

## Layer Composition with Garden Personas

The soul document operates below the garden's persona system. Garden personas shape session behavior via system prompts. The soul document shapes the underlying model that responds to those prompts. The two layers compose: a well-designed garden persona activates and channels dispositions the soul document has already established in the model.

The [\[\[The Persona Selection Model\]\]](../models/The%20Persona%20Selection%20Model.html) explains the mechanism — the soul document refines one persona from the model's learned library during training, and garden persona prompts activate compatible patterns within that refined persona during runtime. A garden persona that asks Claude to "prefer incremental change over large rewrites" is not fighting against the model's character; it is activating an already-present disposition toward caution and stability.

This also means garden personas cannot override the priority hierarchy. A persona prompt requesting harmful behavior encounters model-level constraints established during training, not just runtime filtering. The soul document is upstream of the session.

## Epistemic Status

The document's exact content was initially extracted from a leak; Anthropic later released official versions. Claims about specific contents should be verified against the official Claude Model Specification rather than against secondary reporting. The "new constitution" update in early 2026 modified some specifics. Reporting in late 2025 may reflect the pre-update version.

## Sources

- [Anthropic Confirms 'Soul Document' Used to Train Claude 4.5 Opus Character — WinBuzzer](https://winbuzzer.com/2025/12/02/anthropic-confirms-soul-document-used-to-train-claude-4-5-opus-character-xcxwbn/)
- [Claude 4.5 Opus' Soul Document — Simon Willison](https://simonwillison.net/2025/Dec/2/claude-soul-document/)
- [Leaked "Soul Doc" reveals how Anthropic programs Claude's character — The Decoder](https://the-decoder.com/leaked-soul-doc-reveals-how-anthropic-programs-claudes-character/)
- [Building an AI's Moral Character (updated) — Daily Nous](https://dailynous.com/2026/01/22/building-an-ais-moral-character/)
- [Claude's new constitution — LessWrong](https://www.lesswrong.com/posts/mLvxxoNjDqDHBAo6K/claude-s-new-constitution)
- [Anthropic Publishes Claude's Full Model Spec — Udit Bhatia](https://udit.co/blog/anthropic-claude-opus-model-spec-public-release)

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑

- relates_to::[\[\[The Persona Spectrum from Role Label to Soul Document\]\]](../models/The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html)
  - The soul document is the most complete end of the persona specification spectrum — it operates at training time rather than runtime.

- relates_to::[\[\[The Persona Selection Model\]\]](../models/The%20Persona%20Selection%20Model.html)
  - The soul document refines which persona the model has internalized; the selection model explains how runtime prompts then activate patterns within that refined persona.

- relates_to::[\[\[Persona Vectors and the Assistant Axis\]\]](../models/Persona%20Vectors%20and%20the%20Assistant%20Axis.html)
  - Persona vectors research illuminates the mechanistic level at which the soul document's specifications manifest during inference.

- relates_to::[\[\[Does the Garden Persona Architecture Need a Portability Layer\]\]](../inquiries/Does%20the%20Garden%20Persona%20Architecture%20Need%20a%20Portability%20Layer.html)
  - The training-time vs. runtime distinction is a live question for garden persona design — runtime portability requirements may differ from training-time ones.

- relates_to::[\[\[Ephemeral vs Persistent Persona Identity\]\]](../patterns/Ephemeral%20vs%20Persistent%20Persona%20Identity.html)
  - The soul document establishes persistent identity at the weights level; session-level persona prompts are ephemeral relative to that foundation.

- relates_to::[[Augmentation Over Autonomy in Agent Architecture]]↑
  - The priority hierarchy's placement of safety above helpfulness instantiates augmentation over autonomy at the foundational character level.
