---
created: 2026-03-26
author: Christopher Allen
brief_summary: "When a persona node changes in the garden, how should that change propagate to the agent configuration files that implement it? Explores automated rendition generation, drift detection, multi-platform sync, and the boundary between what belongs in the persona node versus the agent file. Blocked until the architecture moves beyond Claude Code to multiple frameworks."
tagline: "How do persona design changes flow downstream to agent files — and how do we know when they drift?"
---

- is_a::[Inquiry Form](../forms/Inquiry%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Agentic Architecture](../domains/Agentic%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# How Should Persona Node Changes Sync to Agent Configuration Files

## Research Question

Given the decision that [persona nodes are the design authority](../decisions/Persona%20Nodes%20as%20Design%20Authority%20for%20Agent%20Configuration.html) and agent configuration files are downstream renditions: what is the sync mechanism? When a persona node's behavioral scope, blind spots, or operational architecture changes, how does that change reach the Claude Code agent file, a future SOUL.md, or an AGENTS.md entry?

## Why This Matters

Today the sync is manual — a human or agent edits the persona node, then separately edits the agent file. This works for eight personas on one platform. It breaks when:

- **Scale increases** — 20+ personas across multiple projects
- **Platforms multiply** — the same persona renders to Claude Code, OpenAI, Ollama, SoulSpec
- **Drift accumulates silently** — the persona node says one thing, the agent file says another, and no one notices until behavior surprises

The [portability inquiry](Does%20the%20Garden%20Persona%20Architecture%20Need%20a%20Portability%20Layer.html) asks whether personas should be portable across frameworks. This inquiry asks the prior question: how do changes flow from source to rendition within *any* framework?

## Open Sub-Questions

1. **Automated rendition generation**: Should a skill or script generate agent files from persona nodes? What would the template look like? How much of a persona node maps mechanically to an agent file versus requiring human judgment?

2. **Drift detection**: How would the system detect when an agent file has diverged from its persona node? Hash comparison? Predicate-based consistency checks? A `last_synced::` predicate on the agent file?

3. **Reverse flow**: When operational experience reveals that an agent file needs a behavioral change, should the change go directly to the agent file (fast, but creates drift) or always through the persona node first (slower, but maintains authority)?

4. **Rendition scope**: What belongs in the persona node versus the agent file? The persona carries design rationale and blind spots — but should it also carry platform-specific rendering hints (`renders_as::claude-code`, `renders_as::soulspec`)?

5. **Compound persona structure**: Victoria Gracia's compound personas (system prompt + cultural context documents) suggest that deep personas need more than a single file. How does the compound node pattern (lead file + Renditions/) map to multi-platform persona delivery?

## Current Status

**Blocked**: Cannot fully explore until the architecture moves beyond Claude Code. The single-platform case (persona node → one Claude Code agent file) is simple enough that manual sync works. The interesting questions emerge with multiple target platforms, which requires at least one additional framework integration to test against.

## Sources

- [Persona Nodes as Design Authority for Agent Configuration](../decisions/Persona%20Nodes%20as%20Design%20Authority%20for%20Agent%20Configuration.html) — the decision this inquiry investigates the implementation of
- Dialogue between Christopher Allen and Peter Kaminski (March 2026) on compound personas and reflection personas
- Victoria Gracia's compound persona work — empirical validation of deep persona structure

## Relations

- motivated_by::[Persona Nodes as Design Authority for Agent Configuration](../decisions/Persona%20Nodes%20as%20Design%20Authority%20for%20Agent%20Configuration.html)
  - This inquiry asks how to implement the decision's downstream-rendition model.

- relates_to::[Does the Garden Persona Architecture Need a Portability Layer](Does%20the%20Garden%20Persona%20Architecture%20Need%20a%20Portability%20Layer.html)
  - The portability inquiry asks whether to support multiple frameworks; this inquiry asks how changes flow to renditions regardless of framework count.

- relates_to::[Persona Drift Causes Detection and Prevention](../patterns/Persona%20Drift%20Causes%20Detection%20and%20Prevention.html)
  - Drift between persona node and agent file is a form of persona drift — but at the design level, not the runtime level.
