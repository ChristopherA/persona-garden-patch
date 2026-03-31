---
created: 2026-03-31
author: Christopher Allen
status: accepted
brief_summary: "Two-word persona names encode the delegated authority scope as prefix: Estate (estate-level agents), Garden (garden precinct), Household (household precinct). The prefix carries structural information — it tells you the agent's authority boundary before you read the role description. Emerged when the user corrected a universal 'Estate' prefix, revealing that the name should encode scope, not just disambiguate."
tagline: "The prefix carries the boundary — Estate Chamberlain but Household Chancellor, not Estate everything"
---

- is_a::[[Decision Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Deep Context Architecture]]
- in_precinct::[[Garden Precinct]]

# Scope-Encoded Naming as Authority Boundary

## Context

As the estate's agent taxonomy grew beyond single-word names (Groundskeeper, Chancellor), compound names became necessary for disambiguation and formal reference. The initial approach applied "Estate" as a universal prefix — "Estate Chamberlain," "Estate Chancellor," "Estate Groundskeeper." This treated the prefix as a namespace qualifier rather than as a structural signal.

The user corrected this: the Chancellor's scope is the Household Precinct, not the estate. Calling it "Estate Chancellor" would misrepresent its authority boundary. The correction revealed that the prefix is not a namespace — it is an authority declaration.

## Decision

Two-word persona names encode the delegated authority scope as prefix:

| Prefix | Scope | Agents |
|--------|-------|--------|
| **Estate** | Cross-precinct, estate-level | Estate Chamberlain, Estate Seneschal, Estate Chatelaine |
| **Garden** | Garden Precinct | Garden Groundskeeper, Garden Cultivator, Garden Forager, Garden Pruner |
| **Household** | Household Precinct | Household Chancellor, Household Scribe, Household Scholar, Household Lector |

The prefix carries structural information: it tells you the agent's authority boundary before you read the role description. "Estate Chamberlain" means this agent's authority spans the whole estate. "Household Chancellor" means this agent's authority is bounded to the Household Precinct.

In informal reference, the single-word name suffices (Chamberlain, Chancellor, Groundskeeper). The two-word form is for formal contexts: agent definition headers, predicate targets, persona node titles, and architectural documents where the authority boundary matters.

## Consequences

**Positive**: Authority boundaries are visible in the name itself. A new collaborator reading "Garden Groundskeeper" immediately knows this agent operates within the garden — before reading any documentation. The name teaches scope.

**Positive**: Prevents scope creep in agent design. When the prefix declares "Household," any design decision that grants cross-precinct authority creates a visible contradiction with the name. The naming convention applies pressure toward the least authority principle.

**Negative**: Adds a word to every formal agent reference. Informal conversation will naturally drop the prefix, reducing the structural signal to formal contexts only.

**Negative**: The prefix taxonomy must be maintained. A new precinct (e.g., Estate Precinct as a distinct organizational unit) requires a naming decision.

## Alternatives Considered

**Universal "Estate" prefix**: Treating the prefix as namespace rather than scope. Rejected because it misrepresents authority boundaries — "Estate Chancellor" implies estate-level authority that the Chancellor does not have.

**No prefix**: Single-word names only. Rejected because some names are ambiguous without scope (a "Scribe" could serve either precinct), and the authority-boundary signal is architecturally valuable.

**Suffix instead of prefix**: "Chancellor of the Household" vs "Household Chancellor." Rejected for prose flow — the prefix places the boundary first, which is the more useful information for quick comprehension.

## Sources

- Seneschal Session 109b (2026-03-29) — user correction revealing scope-encoding principle
- [[Delegated Decision Authority Spectrum]] — the authority model that scope-encoded names make visible

## Relations

- implements::[[Naming Carries Relational Weight]]
  - The scope prefix is naming-as-architecture: it carries structural information about the authority boundary
- relates_to::[[Subtitle Anchoring for Persona Activation]]
  - Subtitle anchoring handles how the model activates; scope-encoded naming handles how the human reads authority. Both are naming decisions for different audiences
- relates_to::[[English Stewardship Vocabulary Over Latin or Corporate Terms]]
  - The scope prefixes use the estate's own vocabulary (Estate, Garden, Household), consistent with the feudal English decision
- relates_to::[[Vocabulary Collision Navigation]]
  - Scope-encoded naming is a convention that participants in the commons can read without adopting — it translates authority structure through naming
- relates_to::[[Knowledge Estate as Peer Commons Architecture]]
  - The three-tier hierarchy this naming convention makes visible
