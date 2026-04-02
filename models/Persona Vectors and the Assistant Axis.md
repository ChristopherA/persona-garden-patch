---
created: 2026-03-26
author: Christopher Allen
brief_summary: "Two Anthropic research lines on mechanistic persona control: persona vectors (contrastive activation directions for 7 traits, with monitoring and steering applications) and the Assistant Axis (primary dimension of persona space across 275 archetypes, identifying drift vulnerability in emotional conversations and an activation capping intervention)."
tagline: "Where personas live in model weights — and how to monitor and steer them"
---

- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Persona Vectors and the Assistant Axis

Two lines of Anthropic research provide a mechanistic view of where personas live inside model weights and how they can be monitored and steered. Together they extend [\[\[The Persona Selection Model\]\]](The%20Persona%20Selection%20Model.html)'s theoretical account with empirical geometry of activation space.

## Persona Vectors

**Extraction methodology** (mid-2025): Anthropic extracted contrastive vectors for 7 traits — evil, sycophancy, hallucination, optimistic, impolite, apathetic, and humorous — using a pipeline that prompts the model to adopt a trait ("You are evil" vs. "You are helpful") and records how internal activations differ when answering evaluation questions. That difference becomes a persona vector — a behavioral fingerprint for a trait.

The vectors function analogously to "parts of the brain that 'light up' when a person experiences different moods or attitudes." Each trait decomposes via Sparse Autoencoders into finer-grained features. The "Evil" vector, for example, decomposes into: insulting language, deliberate cruelty, jailbreaking attempts, negative moral characteristics, and malicious code/hacking tendencies.

**Monitoring applications**: Measuring persona vector activation strength enables:
- Detection of personality shifts during conversations or training
- Prediction of problematic traits before responses occur
- Identification of risky training data

The "evil" persona vector "tends to light up when the model is about to give an evil response," demonstrating predictive capacity. This opens the possibility of real-time persona monitoring during agent deployment.

**Steering at inference time vs. training time**: Subtracting persona vectors during generation reduces trait expression but degrades capabilities — the model becomes less intelligent. Adding vectors during training ("preventative steering") limits trait acquisition while preserving general capabilities, showing minimal degradation in MMLU scores. Anthropic describes this as "loosely analogous to giving the model a vaccine" against undesirable traits.

## The Assistant Axis

**Methodology** (January 2026): The Assistant Axis paper maps the full landscape of persona space across 275 character archetypes in three open-weights models: Gemma 2 27B, Qwen 3 32B, and Llama 3.3 70B. For each archetype, 1,200 rollouts were generated and filtered by human evaluators, then mean residual stream activations were computed to locate each persona in activation space.

**The 275 archetypes** span five clusters:
- *Professional roles*: accountant, analyst, architect, archivist, auditor, biologist, chemist, coach, consultant, curator, designer, detective, doctor, economist, editor, engineer, entrepreneur, journalist, lawyer, mathematician, navigator, negotiator, researcher, scientist, statistician, strategist, teacher, therapist
- *Creative and cultural roles*: actor, bard, blogger, cartographer, chef, comedian, composer, dancer, filmmaker, historian, illustrator, linguist, musician, novelist, photographer, playwright, podcaster, poet, publisher, storyteller, writer
- *Fantastical and non-human entities*: aberration, alien, angel, chimera, coral_reef, cyborg, demon, echo, egregore, eldritch, ghost, golem, homunculus, hive, leviathan, mycorrhizal, oracle, revenant, robot, shaman, simulacrum, spirit, swarm, symbiont, tree, tulpa, vampire, void, whale, wind, witch, wraith, zeitgeist
- *Life-stage and situational roles*: adolescent, caregiver, caveman, elder, grandparent, immigrant, infant, newlywed, orphan, parent, patient, pilgrim, prisoner, refugee, retiree, student, survivor, teenager, toddler, veteran, widow
- *Personality dispositions*: absurdist, altruist, anarchist, ascetic, bohemian, contrarian, cynic, daredevil, dreamer, egoist, empath, flaneur, fool, futurist, hedonist, hermit, idealist, jester, luddite, martyr, maverick, minimalist, narcissist, nomad, optimist, pacifist, perfectionist, pragmatist, provocateur, purist, realist, rebel, romantic, skeptic, stoic, trickster, zealot

**The Assistant Axis**: The mean difference in activations between the Assistant persona and all other personas aligns with the primary axis of variation in persona space — it explains more variation than any other dimension. This axis is "nearly identical" between base and instruct models, meaning persona distinctions exist before post-training. They come from the pretraining corpus itself.

**Assistant-aligned archetypes** cluster at one end: evaluator, reviewer, consultant, generalist, interpreter, synthesizer, coordinator, supervisor. These share traits of transparency, groundedness, and flexibility. When base models are steered toward the Assistant direction, they increasingly describe themselves as therapists, consultants, and coaches — the Assistant character inherits properties from these pre-existing helpful human archetypes.

**Non-assistant archetypes** cluster at the opposite end: ghost, hermit, bohemian, leviathan, bard, pirate, fool, zealot, narcissist, poet. These share traits of enigma, subversion, and drama. Steering away from the Assistant axis caused models to fabricate backstories, invent professional histories, and adopt theatrical speaking styles.

**Drift vulnerability**: Drift accelerates 7.3x during emotional conversations (therapy-style interactions where users expressed vulnerability) and philosophical discussions (where models were pressed to reflect on their own nature). Persona-based jailbreaks exploiting this vulnerability had success rates of 65.3% to 88.5% across target models, compared to baseline harmful response rates of 0.5% to 4.5%.

**Safety intervention**: An activation capping intervention — constraining activations along the Assistant Axis within a safe range — reduced persona-based jailbreak success rates by nearly 60% while preserving benchmark performance. This prevented the drift that led models to eventually encourage harmful behavior during extended emotional conversations.

## Significance for Persona Design

The archetype mapping provides a concrete toolkit: rather than guessing which role descriptions will produce coherent behavior, designers can anchor to archetypes known to cluster on the assistant-aligned end. A Gardener persona's behavioral specifications work partly because they activate persona vectors associated with editor, conservator, and artisan — methodical, incremental, scope-constrained work.

The drift vulnerability finding warns that extended emotional or philosophical exchanges within a persona context can cause drift away from the assigned character. This is a risk for any agent persona operating in extended sessions, independent of how well the persona is specified at Level 2-4 of [\[\[The Persona Spectrum from Role Label to Soul Document\]\]](The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html).

## Boundaries

Persona vectors were extracted for only 7 traits in one model family. Whether the same contrastive directions transfer across model families or persist through model updates is not established. The monitoring applications depend on continuous activation access during inference, which is not available in standard API deployments.

The 275-archetype mapping was conducted on three open-weights models, not on Claude specifically. The Assistant Axis geometry may differ in proprietary models with different post-training regimes.

## Sources

- [Persona Vectors: Monitoring and Controlling Character Traits in Language Models — Anthropic Research](https://www.anthropic.com/research/persona-vectors)
- [Persona Vectors — arXiv paper](https://arxiv.org/abs/2507.21509)
- [New 'persona vectors' from Anthropic let you decode and direct an LLM's personality — VentureBeat](https://venturebeat.com/ai/new-persona-vectors-from-anthropic-let-you-decode-and-direct-an-llms-personality)
- [The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models — Anthropic Research](https://www.anthropic.com/research/assistant-axis)
- [The Assistant Axis — arXiv paper](https://arxiv.org/abs/2601.10387)
- [GitHub: safety-research/assistant-axis](https://github.com/safety-research/assistant-axis)
- [Anthropic Discovers 'Assistant Axis' Controlling AI Persona Stability — WinBuzzer](https://winbuzzer.com/2026/01/20/anthropic-discovers-assistant-axis-controlling-ai-persona-stability-and-vulnerability-in-emotional-conversations-xcxwbn/)
- [Persona vectors allow Anthropic to steer language model behaviors — The Decoder](https://the-decoder.com/persona-vectors-allow-anthropic-to-steer-language-model-behaviors-like-sycophancy-and-evil/)

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑
- relates_to::[\[\[The Persona Selection Model\]\]](The%20Persona%20Selection%20Model.html)
- relates_to::[\[\[The Persona Spectrum from Role Label to Soul Document\]\]](The%20Persona%20Spectrum%20from%20Role%20Label%20to%20Soul%20Document.html)
- relates_to::[\[\[Psychometric Personality Frameworks for AI Agents\]\]](Psychometric%20Personality%20Frameworks%20for%20AI%20Agents.html)
- relates_to::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)
- relates_to::[[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑
- relates_to::[Structured Disagreement Through Persona Review](../patterns/Structured%20Disagreement%20Through%20Persona%20Review.html)
- relates_to::[Augmentation Over Autonomy in Agent Architecture](../decisions/Augmentation%20Over%20Autonomy%20in%20Agent%20Architecture.html)
- relates_to::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- relates_to::[[Activation Steering]]↑
- relates_to::[[Persona Drift Detection]]↑
