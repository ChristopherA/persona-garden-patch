---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Pattern form type: a problem-solution pair in Alexandrian tradition. Required: tagline, Heart, Problem, Forces, Solution. Standard (Growing): Context, Consequences, Examples, Relations. Optional: Also Known As, Resulting Context, Known Results, Sources. Designed to accommodate multiple pattern language traditions and imports at varying completeness levels."
tagline: "What resolves this recurring tension? — the structural contract for pattern forms"
---

- is_a::[Form Type](Form%20Type.html)
- has_status::[Seed Stage](Seed%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Pattern Form

**Core question**: "What resolves this recurring tension?"

A problem-solution pair in Alexandrian tradition. Generalized from experience, reusable across domains. Stable; validated or invalidated by cases. The contract is tiered to accommodate pattern languages imported at varying levels of completeness — from stub imports (name + heart + connections) that grow over time, to fully articulated patterns with forces, consequences, and empirical validation.

## Structural Contract

The contract is organized in three tiers aligned with the status lifecycle. A pattern enters at Seed with the required elements and grows toward Evergreen as sections are added.

### Required (minimum for Seed stage)

- **`tagline:`** in frontmatter — Machine-readable summary for LLM progressive disclosure and graph traversal. Concise, functional. Distinct from Heart: the tagline serves machines and scanning; the Heart serves human readers who have stopped to read.
- **Heart** — Body section (H2) for human readers. Two to three sentences that ARE the pattern at card scale — the name plus the Heart must stand alone as a complete expression. Not a summary of the longer pattern; the pattern itself, compressed. Tells you what happens, what to do, and why it matters. Evocative and connecting, not clinical. Drawn from the Group Works tradition (groupworksdeck.org) where the card text IS the Heart — a reader holding only the card gets the whole pattern. The Heart is the first thing a reader sees after the predicates; everything that follows elaborates what the Heart already said.
- **Problem** — What goes wrong without this pattern. A concise statement of the recurring difficulty.
- **Forces** — Competing demands or constraints pulling against each other. Name at least two forces in genuine tension. Forces are the engine of a pattern — without them, the Problem is a complaint and the Solution is advice. Present in every major pattern tradition: explicit in Coplien, implicit in Alexander's prose, folded into Discussion in the Public Sphere Project. The garden requires them as a named section.
- **Solution** — What resolves the problem. Stated directly, not as a recommendation.

### Standard (expected for Growing stage)

- **Context** — The domain or situation where this tension arises. Some traditions place Context before Problem (Alexander), others fold it into the Problem statement. The garden does not prescribe ordering between standard sections.
- **Consequences** — What follows from applying the solution, including trade-offs.
- **Examples** — Concrete instances across domains that illustrate the pattern in action. Brief, separated by domain. Distinct from Known Results: examples show the pattern operating; Known Results provide empirical evidence. Present as a distinct section in Björk and Holopainen's game design patterns and in PLML.
- **Relations** — Connections to other nodes: patterns this composes with, principles it embodies, cases that validate or invalidate it.

### Optional (enrichment, any stage)

- **Also Known As** — Alternate names for the pattern across different domains or traditions. A pattern known as "Play Bow" in animal behavior may be "Breaking the Ice" in social contexts. List the aliases; don't explain them unless the naming carries meaning.
- **Resulting Context** — What state the system is in after applying the solution, and what patterns follow. Distinct from Consequences (which describe trade-offs): Resulting Context describes the setup for the next pattern. From PLML and implicit in Alexander's pattern chaining — each pattern creates the conditions that invoke the next.
- **Known Results** — Concrete evidence (metrics, deployment data) that validate the pattern.
- **Sources** — Origin material or experience the pattern was generalized from.

Naming heuristic: Alexandrian evocative — name the solution, lean toward imagery. "Progressive Summary Before Substance" not "Summary Pattern." For anti-patterns, name the failure mode as a claim — a phrase you can agree or disagree with. "Informal Edges Poison the Graph" not "Precedent Poisoning."

## Typical Predicates

- `is_a::[Pattern Form](Pattern%20Form.html)`
- `has_status::[Seed Stage](Seed%20Stage.html)` or `[Evergreen Stage](Evergreen%20Stage.html)`
- `in_domain::[[Domain Name]]↑`
- `extracted_from::[[Source Document]]↑` — provenance
- `validated_by::[Case Form](Case%20Form.html)` — evidence the pattern works
- `composes_with::[[Related Pattern]]↑` — how patterns combine
- `relates_to::[Principle Form](Principle%20Form.html)` — values the pattern embodies
- `in_collection::[[Pattern Language Name]]↑` — membership in a pattern language collection (compound folder)

## Exemplars

- [[Progressive Summary Before Substance]]↑ — Alexandrian structure with clear forces and resolution (Deep Context Architecture)
- [[Tag You're It]]↑ — cooperative play pattern with Problem/Forces/Examples/Also Known As (Synpraxis)
- [[Knowledge on Three Axes]]↑ — cross-domain pattern with mapping table
- [[Three-Part Enforcement Stack]]↑ — pattern from Self-Sovereign Identity domain with enforcement layers
- [[Informal Edges Poison the Graph]]↑ — anti-pattern naming: failure mode as a claim

## Category

Action form — captures *what to do* and *what happened*.

## Sources

Definition from [Deep Context as an Architecture for Captured Reasoning](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 82-83.

## Relations

- relates_to::[Decision Form](Decision%20Form.html) — decisions instantiate patterns in specific contexts
- relates_to::[Principle Form](Principle%20Form.html) — principles compress patterns into standing constraints
- relates_to::[Model Form](Model%20Form.html) — models provide the structural context in which patterns operate
- relates_to::[Inquiry Form](Inquiry%20Form.html) — inquiries that identify recurring dynamics may crystallize into patterns
