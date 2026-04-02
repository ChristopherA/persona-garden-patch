---
created: 2026-04-02
part_of: "[[Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems]]"
role: insights
---

- is_a::[[Citation Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Agentic Architecture]]
- in_precinct::[[Garden Precinct]]
- part_of::[[Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems]]

# Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems — Insights

## Insight 1: Accountability as a Non-Invasive Layer

Horton's key architectural move is adding accountability without modifying the authorization substrate. The capability system retains its properties unchanged; the accountability layer interposes transparently. This pattern — extending a system's properties through layering rather than modification — has direct implications for the garden's treatment of agent authority.

The principle [[Human Authority Over Augmentation Systems]] requires that humans retain meaningful oversight of agent actions. Horton shows what "meaningful oversight" looks like at the protocol level: not restricting what agents can do (that's the authorization layer, handled by capability delegation) but ensuring that what agents do is attributable and traceable through the delegation chain. The insight is that authority and accountability are separable concerns that can be addressed by different architectural layers.

**Ghost link**: [[Accountability as a Layer]] -- a potential Pattern Form node describing the architectural pattern of adding accountability through interposition rather than modification. Applicable beyond security: any system that delegates authority can add accountability as a transparent layer. [source: direct from Horton protocol architecture]

## Insight 2: Delegation of Responsibility as a Compound Concept

The paper distinguishes delegation of authority, assignment of responsibility, and delegation of responsibility (authority coupled with accountability). Most digital systems provide only the first two independently. This distinction maps directly to a gap in the garden's agent delegation model.

Current multi-agent architectures typically delegate authority to agents (tool access, file permissions, task scope) and record what agents did (logs, commit history). But these are separate mechanisms — the authority delegation and the responsibility tracking are not coupled at the protocol level. An agent's log records what it did, but the log is a separate artifact from the capability delegation. Horton suggests the coupling should be structural: when authority is delegated, accountability for its exercise should be established in the same act.

**Ghost link**: [[Delegation of Responsibility]] -- a potential Gloss Form node distinguishing this compound concept from its two components. The distinction is load-bearing for any system that delegates to agents. [source: direct from paper's central thesis]

## Insight 3: Inductive Trust for Agent Networks

Horton's handling of the inductive case — bootstrapping new accountability relationships from existing ones through sealed/unsealed gift-wrapping — provides a model for how agent trust networks can grow without central coordination.

In a multi-agent architecture, a principal commissions an orchestrator, who supervises workers. Each introduction (principal → orchestrator → specialist worker) is an inductive step: the new accountability relationship bootstraps from the existing one. Horton's protocol shows how this can be formalized: each introduction carries accountability metadata from the introducer, so the full chain from principal to final worker is reconstructable without any single entity holding all the state.

This matters for sovereignty-as-membrane models of digital identity. The membrane is selectively permeable — each delegation crosses the boundary with specific authority. Horton adds that each boundary crossing also carries accountability, making the membrane auditable without making it opaque.

**Ghost link**: [[Inductive Trust Bootstrapping]] -- a potential Model Form node describing how trust and accountability relationships grow through introduction rather than central registration. [source: analysis-level inference connecting Horton's inductive case to multi-agent architecture]

## Insight 4: The Proxy/Stub Pattern for Agent Intermediation

Horton's proxy/stub architecture — where Carol interposes between Alice and Bob, wrapping capabilities in accountability-tracking proxies — maps to the orchestrator-worker pattern in multi-agent systems. The orchestrator (Carol) wraps the authority it delegates to workers (Bob) in structures that track exercise of that authority, without requiring the workers to implement accountability logic themselves.

This suggests a concrete design direction: commission files could carry accountability metadata (who authorized the work, what authority was delegated, what constraints apply) in a form that the worker agent processes transparently — the way Horton's proxy wraps capabilities without the receiving object knowing it's wrapped.

**Ghost link**: [[Capability Proxy Pattern for Agent Commissions]] -- a potential Scenario Form node exploring how task commissions could function as Horton-style proxies carrying accountability metadata. [source: design-level inference from Horton proxy/stub to multi-agent commission architecture]
