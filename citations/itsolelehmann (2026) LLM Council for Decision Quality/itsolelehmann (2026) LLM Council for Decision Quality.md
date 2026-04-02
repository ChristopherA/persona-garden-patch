---
created: 2026-03-30
author: Christopher Allen
citation_slug: "itsolelehmann-2026-llm-council-decision-quality"
publication_year: 2026
canonical: "https://x.com/itsolelehmann/status/2038661433626333649"
brief_summary: "Ole Lehmann reimplements Karpathy's multi-model LLM Council as a Claude Code skill using five role-constrained sub-agents (Contrarian, First Principles, Expansionist, Outsider, Executor) plus an anonymized peer review round and chairman synthesis. The peer review step — especially the 'what did all five miss?' question — reliably surfaces blind spots that no individual advisor catches, making gap detection through multi-perspective comparison the key mechanism."
tagline: "Five adversarial thinking roles plus anonymous peer review surface what single-perspective AI advice hides"
---

- is_a::[Citation Form](../../forms/Citation%20Form.html)
- has_status::[Seed Stage](../../forms/Seed%20Stage.html)
- in_domain::[Agentic Architecture](../../domains/Agentic%20Architecture.html)
- in_precinct::[Garden Precinct](../../glosses/Garden%20Precinct.html)
- cites_work_by::[[@itsolelehmann]]↑

# itsolelehmann (2026) LLM Council for Decision Quality

## Bibliographic Entry

* _**How to finally trust Claude's advice (using Karpathy's LLM Council method)**_ (2026). [microcontent]. _Lehmann, Ole._ X, March 30, 2026. Retrieved 2026-03-30 from: <https://x.com/itsolelehmann/status/2038661433626333649>

## Summary

Lehmann adapts Karpathy's LLM Council — originally a multi-model polling system — into a Claude Code skill that spawns five sub-agents with adversarial thinking roles. Each advisor responds independently, responses are anonymized, five reviewers evaluate the full field, and a chairman model synthesizes the final recommendation. The peer review round, particularly the question "what did all five miss?", produces the highest-value output by detecting gaps in the negative space between perspectives. A product-format case study shows the architecture catching a reinforcing relationship between arguments that no individual advisor identified.

## Key Points

- **Role-constrained diversity replaces model diversity**: Karpathy's council polls different models; Lehmann uses five thinking-style roles within a single model. Whether role-constrained prompting produces genuine reasoning diversity or the appearance of diversity from one probability distribution remains an open question with direct implications for persona architecture.

- **Anonymization prevents role-based evaluation bias**: After the five advisors respond, the skill shuffles which advisor maps to which letter before peer review. This forces reviewers to evaluate content rather than deferring to or dismissing responses based on the role that produced them. The estate's persona review currently lacks this step.

- **The peer review round, not the five-way divergence, creates the most value**: Lehmann identifies the comparison step as where blind spots surface. Five perspectives side by side make the gap between them visible — and more importantly, make the space where all five are silent into a detectable signal.

- **Gap detection operates on absence, not presence**: The "what did all five miss?" question detects what the field of responses fails to cover. This differs from ensemble averaging (cancels noise) and adversarial debate (tests claims). It is a distinct multi-agent mechanism that deserves its own pattern name.

- **Emergent argument interactions span role boundaries**: In the case study, the Contrarian's completion-rate argument and the First Principles speed argument reinforce each other in a way neither saw. This reinforcing combination — not either argument alone — is the strategic insight. Emergence requires a structured comparison step that individual agents cannot perform.

- **Five adversarial roles cover five decision-making blind spots**: Contrarian (risk blindness), First Principles (assumption lock-in), Expansionist (scope myopia), Outsider (expertise bias), Executor (implementation gap). The set lacks roles for ethics, long-term consequences, and systemic effects — suggesting it is a minimal covering set for business decisions, not a universal one.

- **Chairman synthesis trades human authority for decision speed**: The architecture ends with a model synthesizing a "clear recommendation and one concrete next step." This reintroduces sycophancy risk at the synthesis layer and contrasts with the estate's pattern where the human decides after reviewing structured disagreement.

- **Sycophancy framed specifically as framing sensitivity**: The article defines the sycophancy problem as the model picking up on "your assumptions, your framing, your emotional lean." This is narrower than the full sycophancy problem but has a clear architectural solution: force multiple framings simultaneously.

## Key Quotes

- "Claude just tells you what you want to hear. Every time. You can't trust it." (Opening — problem statement)

- "I rebuilt it to work entirely inside Claude using sub-agents with different thinking styles instead of different models." (Architecture — the key substitution)

- "After all 5 advisors respond, the skill anonymizes everything. Shuffles which advisor maps to which letter. The reviewers don't know who said what." (Peer review — anonymization step)

- "That last question is the most valuable one. Every time I've run the council, the peer review round catches something no individual advisor saw." (Peer review — gap detection claim)

- "When you read 5 perspectives side by side, the gap between them reveals what nobody thought to mention." (Peer review — negative space mechanism)

- "The Contrarian's completion rate argument and the First Principles Thinker's speed argument actually reinforce each other in a way neither advisor saw alone." (Case study — emergent interaction)

## Influence

This article provides the most concrete practitioner implementation of structured multi-agent disagreement for decision quality. Its direct connection to the estate's [Structured Disagreement Through Persona Review](../../patterns/Structured%20Disagreement%20Through%20Persona%20Review.html) pattern makes it load-bearing for the persona strategy discussion: it demonstrates anonymization, gap-detection naming, and the role-vs-model diversity question that the estate's architecture must address. The 198,000+ views and 2,000+ bookmarks indicate significant practitioner uptake of the council pattern.

## Limitations

- **Single practitioner testimony**: All effectiveness claims are anecdotal from Lehmann's own experience. No controlled comparison, no user study, no systematic evaluation of the council's error rate or failure modes.
- **Marketing context**: The article promotes Lehmann's newsletter and workshop simultaneously. The product-decision case study doubles as workshop advertising, which may shape which outcomes are reported.
- **Role diversity assumed equivalent to model diversity**: The substitution is presented as simple but the mechanisms differ in kind. No evidence provided that single-model role-constrained prompting produces the same quality of diversity as multi-model polling.
- **No failure mode discussion**: When does the council fail? When do all five advisors converge on the same wrong answer? When does the peer review miss the gap? Only success cases are reported.
- **Fixed role set without justification**: No argument that the five-role set is complete, optimal, or sufficient for question types beyond business decisions.

## Sources

- Source clipping: [How to finally trust Claude's advice using Karpathy's LLM Council method (@itsolelehmann)](Renditions/How%20to%20finally%20trust%20Claude's%20advice%20using%20Karpathy's%20LLM%20Council%20method%20%28@itsolelehmann%29.html)
- Referenced work: Karpathy's LLM Council (described in article; no direct citation provided by the author)
- Analysis: [itsolelehmann (2026) LLM Council for Decision Quality — Analysis](itsolelehmann%20%282026%29%20LLM%20Council%20for%20Decision%20Quality%20—%20Analysis.html)
- Insights: [[itsolelehmann (2026) LLM Council for Decision Quality — Insights]]↑

## Relations

- relates_to::[Structured Disagreement Through Persona Review](../../patterns/Structured%20Disagreement%20Through%20Persona%20Review.html)
  - The council implements the same core pattern — multiple constrained perspectives plus structured comparison — but adds anonymization and forced synthesis that the estate's version lacks. The comparison surfaces specific design questions for estate persona review.

- relates_to::[[itsolelehmann (2026) Ultimate Guide to Claude Skills 2.0]]↑
  - Same author, complementary topic. The Skills 2.0 guide addresses skill maintenance lifecycle; this article describes a specific high-value skill architecture. Together they represent Lehmann's practitioner methodology for Claude Code skill engineering.

- relates_to::[[Human Authority Over Augmentation Systems]]↑
  - The council's chairman synthesis step trades human authority for decision speed — a direct tension with this principle. The estate's alternative (structured disagreement without forced synthesis) preserves authority at the cost of higher cognitive load.

- relates_to::[Functional Types in Agent Taxonomy](../../decisions/Functional%20Types%20in%20Agent%20Taxonomy.html)
  - Lehmann's five adversarial roles represent an analytical taxonomy distinct from the estate's operational taxonomy. The estate has stewards, orchestrators, workers, and boundary guardians (who do things); the council has contrarians, first-principles thinkers, expansionists, outsiders, and executors (who evaluate things). These axes are complementary.

- relates_to::[[Tiered Model Allocation by Task Type]]↑
  - If single-model role diversity is weaker than multi-model diversity, the model allocation pattern could extend to structured review: assign different models to different review personas rather than constraining one model into multiple roles.
