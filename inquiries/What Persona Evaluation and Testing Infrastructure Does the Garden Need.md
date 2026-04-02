---
created: 2026-03-26
author: Christopher Allen
brief_summary: "Production persona systems use quantitative evaluation: Big Five scoring, persona vector monitoring, PSI drift detection, pass@k consistency metrics. The garden's persona architecture has none of this. Four open questions about behavioral consistency testing, drift detection, role adherence metrics, and whether human-validated psychometric instruments apply to LLM constructs."
tagline: "What would it mean to test whether a garden persona is working?"
---

- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Agentic Architecture\]\]](../domains/Agentic%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# What Persona Evaluation and Testing Infrastructure Does the Garden Need

## Research Question

Production persona systems use quantitative evaluation: Big Five personality scoring, persona vector monitoring, Psychological Stability Index drift detection, pass@k consistency metrics for behavioral scenarios. The garden's persona architecture has no equivalent evaluation or testing infrastructure. What would persona evaluation look like for the garden's operational agents — Gardeners, Groundskeepers, Chancellors — whose personas are defined in garden persona nodes and rendered into Claude Code agent files?

## What Is Being Determined

Whether garden personas need formal evaluation at all, and if so, what metrics and methods are appropriate for operational (not conversational) agent personas. The garden's agents do knowledge management work — creating nodes, triaging content, running commissions — rather than engaging in open-ended conversation. Whether that distinction changes what "persona stability" means is itself one of the questions.

## Open Questions

**1. Behavioral Consistency Testing**: The deterministic personality research ran agents through 50+ diverse scenarios and measured whether behavioral outputs matched persona specifications. The same approach applied to garden agents would mean: given a sample commission, does the Gardener behave as its persona declares? Does it "prefer incremental change over large rewrites"? Does it "create ghost links rather than speculative content"? A scenario suite for garden personas would need to define what compliance looks like for each behavioral specification — which requires those specifications to be operationally precise enough to pass or fail.

**2. Drift Detection**: [\[\[Persona Drift Causes Detection and Prevention\]\]](../patterns/Persona%20Drift%20Causes%20Detection%20and%20Prevention.html) identifies a key finding from the Assistant Axis research: emotional conversations cause 7.3x drift acceleration compared to neutral task completion. Garden agents operate in extended sessions that occasionally involve ambiguous or contested content decisions. Should there be a mechanism — perhaps a behavioral anchor check at commission boundaries — to detect when a Gardener has drifted from its persona specification during a session? The commission return is already a boundary event; it may be a natural evaluation point.

**3. Role Adherence Metrics**: Voice agent evaluation uses role adherence — "whether the bot maintains its persona throughout the conversation." For garden agents, role adherence might mean something more structural: does the Gardener maintain its scope constraints (not editing outside commission scope)? Does it follow its commit discipline? Does it apply its escalation protocol when encountering boundary questions? These are measurable — they show up in commit histories and session logs — but currently unmeasured.

**4. The Ontological Error Question**: Psychometric instruments (Big Five, Myers-Briggs, HEXACO) were developed and validated on human respondents. Research on applying them to LLMs finds that models score consistently but that the constructs being measured may differ from human constructs — the instrument may not be measuring personality in the same sense it measures human personality. If garden personas are evaluated, what constructs should be measured? And are those constructs better captured by instruments developed specifically for LLM behavioral evaluation than by instruments borrowed from human psychology? The answer may affect whether existing psychometric research transfers to garden persona design.

## Sources

- [\[\[Psychometric Personality Frameworks for AI Agents\]\]](../models/Psychometric%20Personality%20Frameworks%20for%20AI%20Agents.html) — Big Five and related instruments applied to LLM evaluation
- [\[\[Persona Drift Causes Detection and Prevention\]\]](../patterns/Persona%20Drift%20Causes%20Detection%20and%20Prevention.html) — drift mechanisms including the 7.3x emotional conversation finding
- [\[\[Role Prompting Improves Style but Not Accuracy\]\]](../patterns/Role%20Prompting%20Improves%20Style%20but%20Not%20Accuracy.html) — evidence on what persona specifications reliably change vs. what they do not
- [\[\[Persona Vectors and the Assistant Axis\]\]](../models/Persona%20Vectors%20and%20the%20Assistant%20Axis.html) — mechanistic level at which persona specifications operate
- Research note: [[Persona and Agent Personalities]]↑, lines 519-539

## Relations

- extracted_from::[[Persona and Agent Personalities]]↑

- relates_to::[\[\[Persona Form\]\]](../forms/Persona%20Form.html)
  - Evaluation infrastructure would require persona node specifications to be precise enough to operationalize as pass/fail criteria.

- relates_to::[\[\[Persona Drift Causes Detection and Prevention\]\]](../patterns/Persona%20Drift%20Causes%20Detection%20and%20Prevention.html)
  - Drift detection is one of the four open questions; the drift inquiry frames what mechanisms are known.

- relates_to::[\[\[Psychometric Personality Frameworks for AI Agents\]\]](../models/Psychometric%20Personality%20Frameworks%20for%20AI%20Agents.html)
  - The ontological error question concerns whether human-validated psychometric instruments apply to LLM persona evaluation.

- relates_to::[\[\[Role Prompting Improves Style but Not Accuracy\]\]](../patterns/Role%20Prompting%20Improves%20Style%20but%20Not%20Accuracy.html)
  - Understanding what persona specifications actually change is prerequisite to knowing what a persona evaluation should measure.

- relates_to::[Augmentation Over Autonomy in Agent Architecture](../decisions/Augmentation%20Over%20Autonomy%20in%20Agent%20Architecture.html)
  - Role adherence metrics would measure whether agents stay within their designated scope — a direct test of the augmentation principle.

- relates_to::[Structured Disagreement Through Persona Review](../patterns/Structured%20Disagreement%20Through%20Persona%20Review.html)
  - Structured disagreement mechanisms could be part of a behavioral consistency suite — does the Evaluator persona reliably produce distinct stances?

- directed_at::[[Christopher Allen]]↑
  - The ontological error question (whether human psychometric instruments apply to LLM constructs) requires a judgment call about research quality standards and what counts as sufficient evidence for garden design decisions.
