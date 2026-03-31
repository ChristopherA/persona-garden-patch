---
created: 2026-03-30
part_of: "[itsolelehmann (2026) LLM Council for Decision Quality](itsolelehmann%20%282026%29%20LLM%20Council%20for%20Decision%20Quality.html)"
---

- is_a::[Citation Form](../../forms/Citation%20Form.html)
- has_status::[Seed Stage](../../forms/Seed%20Stage.html)
- in_domain::[Agentic Architecture](../../domains/Agentic%20Architecture.html)
- in_precinct::[Garden Precinct](../../glosses/Garden%20Precinct.html)

# itsolelehmann (2026) LLM Council for Decision Quality — Analysis

## Source Context

Ole Lehmann describes rebuilding Andrej Karpathy's LLM Council — originally a multi-model polling system — as a Claude Code skill using sub-agents with different thinking styles instead of different models. The article is practitioner-oriented: it describes the architecture, walks through a real product-format decision, and provides the skill for readers to use.

## Core Mechanism: Perspective Diversity Through Role Assignment

Karpathy's original LLM Council achieves diversity by polling different foundation models (GPT, Claude, Gemini) on the same question. The premise is that different training data and architectures produce genuinely different reasoning patterns. Lehmann's adaptation replaces model diversity with **role-constrained prompting** within a single model. Five sub-agents receive the same question but with different analytical mandates:

1. **Contrarian** — assumes a fatal flaw exists and searches for it
2. **First Principles Thinker** — strips assumptions and rebuilds the problem
3. **Expansionist** — searches for underexplored upside and adjacent opportunities
4. **Outsider** — responds without domain context, catching the curse of knowledge
5. **Executor** — demands a concrete first step for Monday morning

This substitution raises a question the article does not address: does role-constrained prompting within a single model produce genuine reasoning diversity, or does it produce the appearance of diversity from the same underlying distribution? Karpathy's multi-model approach has a structural advantage — different models trained on different data genuinely see different things. Lehmann's single-model approach relies on the model's ability to suppress its default reasoning when given a role constraint. The article presents this as a simple substitution ("different thinking styles instead of different models"), but the mechanisms differ in kind.

## The Anonymization Step: Suppressing Social Dynamics

After all five advisors respond, the skill anonymizes responses — shuffling which advisor maps to which letter — before the peer review phase. Lehmann describes this as structural but does not explain what it prevents. The implied mechanism: without anonymization, reviewers might evaluate responses based on the role that produced them rather than the content. A Contrarian's objection might be dismissed as "that's what contrarians do" rather than engaged on its merits.

This is an interesting design choice because it addresses a problem that exists even within language model outputs. Models exhibit something analogous to social deference — they respond differently to arguments presented as authoritative versus those presented as speculative. By stripping provenance before the review phase, the architecture prevents the review agents from engaging in role-based reasoning ("the Executor's concerns are just about implementation details") and forces content-based evaluation.

The parallel to the estate's own persona architecture is direct: when personas review each other's work, the review is structured but not anonymized. The personas know who produced what. Lehmann's design suggests this might introduce systematic biases in persona review — a persona's critique might be shaped by its model of the producing persona rather than by the content alone.

## Peer Review as the Value-Creating Step

Lehmann identifies the peer review round, not the initial five-way divergence, as the step that produces the most value. The three review questions are:

1. Which response is strongest and why?
2. Which has the biggest blind spot?
3. What did all five miss?

The third question is the one Lehmann calls "the most valuable." He claims that "every time I've run the council, the peer review round catches something no individual advisor saw." This is a strong claim, and the mechanism is worth examining.

What the peer review round actually does is **force comparison**. When you read five perspectives side by side, differences between them become visible — and the space where all five agree (or all five are silent) becomes a detectable gap. No single advisor can see its own blind spot; the blind spot is defined by what is absent from the response. But when five responses are compared, absence in all five becomes a positive signal — a "negative space" that the review round can identify.

This mechanism — gap-detection through multi-perspective comparison — is distinct from the more commonly discussed benefit of ensemble methods (averaging away noise). The council does not average. It does not vote. It identifies what the field of responses fails to cover. This is closer to adversarial testing than to consensus-building.

## The Product Decision Case Study

Lehmann walks through his own use of the council for a product-format decision: self-paced course versus live workshop. The case study illustrates the architecture's value proposition through a concrete outcome.

The individual advisor contributions map to their assigned roles predictably:

- **First Principles** reframes the decision around the speed variable (AI tools change every few weeks; filmed content goes stale)
- **Contrarian** attacks completion rates (3-5% for self-paced courses means 95% disappointed customers)
- **Executor** runs the timeline math (8-12 weeks to produce a course vs 2-3 weeks for a workshop)
- **Expansionist** identifies the both-in-one approach (live workshop with recording provides both formats)
- **Outsider** flags the assumption that the audience understands why they need the tool

Each contribution is coherent and useful, but the peer review adds something none saw: the Contrarian's completion-rate argument and the First Principles speed argument *reinforce each other* in a way neither advisor identified. A live workshop solves both problems simultaneously — high completion because attendees show up live, and always-current because you teach the latest version. This *combination* is the strategic insight; the individual arguments are tactical.

This illustrates the gap-detection mechanism concretely. Each advisor operates within its role constraint. The reinforcing relationship between two arguments spans role boundaries — it requires comparing arguments that were produced under different analytical mandates. The review round creates the context for this comparison.

## Architectural Comparison: Council vs Estate Persona Review

The estate's [[Structured Disagreement Through Persona Review]]↑ pattern shares structural requirements with Lehmann's council but differs in several dimensions:

| Dimension | Lehmann's LLM Council | Estate Persona Review |
|-----------|----------------------|----------------------|
| Diversity axis | Thinking style (adversarial roles) | Analytical framework (domain expertise) |
| Number of perspectives | Fixed at 5 | Variable (typically 3-5) |
| Anonymization | Yes (shuffled letter mapping) | No |
| Review protocol | 3 standardized questions | Persona-specific review criteria |
| Convergence mechanism | Chairman synthesis + recommendation | Human decision (no forced synthesis) |
| Sycophancy mitigation | Role constraints force disagreement | Declared blind spots force acknowledgment |
| Output format | HTML report + markdown transcript | Inline review annotations |
| Scope | Decision questions | Content review, architectural review |

The most significant difference is the **convergence gate**. Lehmann's council produces a "chairman synthesis" that delivers a "clear recommendation and one concrete next step." The estate's pattern explicitly avoids forced synthesis — the human decides. This reflects different design philosophies: Lehmann optimizes for decision speed (give the user an answer), while the estate optimizes for human authority (give the human the structured disagreement and let them decide).

## Sycophancy as the Motivating Problem

The article opens with the problem of Large Language Model sycophancy: "Claude just tells you what you want to hear." The five-advisor architecture is presented as a sycophancy mitigation strategy. The reasoning: if you ask one model your question, it picks up on your framing, assumptions, and emotional lean, then confirms them. If you force five different analytical lenses onto the same question, at least some will produce uncomfortable conclusions.

This framing treats sycophancy as a **framing sensitivity** problem — the model's output is shaped by how the question is asked. The council addresses this by asking the same question from multiple framings simultaneously. But sycophancy has other components: the model's tendency to agree with explicit or implicit preferences in the conversation, its tendency to avoid contradiction, and its tendency to match the user's emotional register. Role constraints address framing sensitivity but may not fully address these other components, because the role-constrained sub-agents still share the user's context and question text.

## Named Pattern: Gap Detection Through Multi-Perspective Comparison

The mechanism Lehmann describes — value emerging not from individual perspectives but from the comparison between them — deserves a name. **Gap Detection Through Multi-Perspective Comparison**: when multiple constrained perspectives are compared, the space where all perspectives are silent becomes a detectable signal. This differs from ensemble averaging (which cancels noise) and from debate (which tests claims). It operates on absence rather than presence.

This pattern appears in Lehmann's council (the "what did all five miss?" question), in the estate's persona review (where disagreement between personas reveals assumptions), and in Karpathy's original multi-model design (where model agreement is suspicious rather than reassuring). The pattern is not specific to language models — it applies wherever multiple constrained observers examine the same phenomenon.

## Limitations of This Source

- **Single practitioner testimony**: All claims about the council's effectiveness come from Lehmann's own experience. No controlled comparison, no user study, no systematic evaluation. "Every time I've run the council" is anecdotal.
- **Marketing context**: The article promotes Lehmann's newsletter and workshop. The product decision case study simultaneously demonstrates the council and advertises the workshop. This dual purpose may shape which outcomes are reported.
- **No discussion of failure modes**: When does the council fail? When do the five advisors converge on the same wrong answer? When does the peer review miss the gap? The article presents only success cases.
- **Single-model diversity question unaddressed**: The substitution of model diversity for role diversity is presented as equivalent, but the mechanisms differ. No evidence that role-constrained prompting produces the same quality of diversity as genuinely different models.
- **Fixed role set without justification**: Why these five roles and not others? The Contrarian/First Principles/Expansionist/Outsider/Executor set covers adversarial, structural, creative, naive, and pragmatic perspectives. But there is no argument that this set is complete, optimal, or even sufficient for different question types.

## Sources

- Primary source: [How to finally trust Claude's advice using Karpathy's LLM Council method (@itsolelehmann)](Renditions/How%20to%20finally%20trust%20Claude's%20advice%20using%20Karpathy's%20LLM%20Council%20method%20%28@itsolelehmann%29.html)
- Referenced work: Karpathy's LLM Council (no direct citation provided in the article; described as "Andrej Karpathy built something called the LLM Council")
- Related estate pattern: [[Structured Disagreement Through Persona Review]]↑
