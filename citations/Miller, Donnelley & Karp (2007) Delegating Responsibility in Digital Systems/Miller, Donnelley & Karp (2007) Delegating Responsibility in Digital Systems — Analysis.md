---
created: 2026-04-02
part_of: "[[Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems]]"
role: analysis
---

- is_a::[[Citation Form]]
- has_status::[[Seed Stage]]
- in_domain::[[Agentic Architecture]]
- in_precinct::[[Garden Precinct]]
- part_of::[[Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems]]

# Miller, Donnelley & Karp (2007) Delegating Responsibility in Digital Systems — Analysis

## The Accountability Gap in Capability Systems

The paper addresses what was, at the time of writing, the strongest remaining objection to object-capability security. By 2007, Miller and colleagues had refuted most criticisms of the OCap model — the "Capability Myths Demolished" paper (Miller, Yee & Shapiro, 2003) handled confinement, delegation control, and revocation. But accountability remained open. ACL-based systems could answer "who did this?" because every action was tagged with a user identity. Capability systems, operating on anonymous bearer rights, could not. This was not a theoretical quibble — it was the practical reason that system designers chose ACLs despite their well-documented security weaknesses.

The paper's move is to refuse the binary. Rather than arguing that capabilities don't need accountability (the purist position) or that capabilities should incorporate identity at the base level (which would compromise their safety properties), Miller, Donnelley, and Karp show that accountability can be layered on top of the capability substrate. The accountability mechanism respects the capability model's invariants while adding a new property the model didn't originally provide.

## The Horton Protocol as Architectural Pattern

Horton — Higher-Order Responsibility Tracking of Objects in Networks — works through interposition. Between Alice (delegator) and Bob (delegate), Carol acts as an intermediary that wraps capabilities in proxy objects. When Bob exercises a capability obtained through Carol, the proxy records Bob's identity alongside the action. The key constraint: neither Alice nor Bob needs modification. The protocol layers onto existing OCap objects transparently.

This interposition pattern has structural implications beyond the specific protocol. It demonstrates that object-capability systems are extensible through layering rather than modification — a capability system can gain new properties (here, accountability) without changing its foundation. The layering is non-invasive: systems can add Horton to specific delegation paths that need tracking without imposing it system-wide. This selective application matters for performance and complexity management — not every delegation needs accountability tracking, and Horton doesn't force it.

The protocol handles both the base case (establishing accountability between previously unconnected parties) and the inductive case (bootstrapping new accountability relationships from existing ones). The inductive case uses sealed/unsealed gift-wrapping — a pattern native to OCap systems — to extend accountability chains through existing trusted connections. This means accountability can grow organically along the same paths that authority flows, without requiring a separate trust infrastructure.

## Proactive vs. Reactive Security as Design Dimensions

The paper's framing of proactive and reactive security as orthogonal dimensions is analytically sharp. ACL systems optimize for reactive security (blame assignment, access suspension) at the expense of proactive security (programs inherit ambient authority, the confused deputy problem persists). Capability systems optimize for proactive security (least authority, no ambient authority) at the apparent expense of reactive security (anonymous bearer rights, no blame attribution).

Miller, Donnelley, and Karp show these are not trade-offs but design dimensions that can be addressed independently. Proactive security is a property of the authorization model (capabilities). Reactive security is a property of the accountability layer (Horton). A system can have both — and Horton demonstrates that adding the accountability layer does not compromise the proactive safety guarantees of the capability foundation.

This framing directly challenges the implicit assumption in much security architecture that identity and authorization are a single concern. ACL systems merge them (identity IS authorization). Horton separates them (authorization is capabilities; identity is a tracking layer). The separation enables systems that are simultaneously safer (no ambient authority) and more accountable (every exercise of delegated authority is attributable).

## Delegation of Responsibility as a Distinct Concept

The paper's most important conceptual contribution may be the distinction between three things that are often conflated:

1. **Delegation of authority** — granting someone the power to act (capability systems do this)
2. **Assignment of responsibility** — recording who did what (identity systems do this)
3. **Delegation of responsibility** — granting authority coupled with accountability for its use (Horton does this)

Most systems provide (1) or (2) but not (3). Capability systems delegate authority cleanly but anonymously. Identity systems assign responsibility but with ambient authority that makes the assignment unreliable (the confused deputy can't be blamed for being confused — the system's architecture caused the confusion). Horton provides (3) by coupling (1) and (2): when authority is delegated through Horton, accountability for its exercise is simultaneously established.

This distinction is immediately relevant to agent delegation architectures. When a human principal delegates authority to an AI agent, the principal needs not just delegation of authority (the agent can act) but delegation of responsibility (the agent's actions are attributable, and the accountability chain traces back to the principal through the delegation). Current agent systems mostly implement (1) — API keys, tool access, file permissions — without (3). The agent has authority but no protocol-level mechanism ensures its exercise is tracked as the principal's delegated responsibility.

## Significance for the Agentic Architecture Domain

Horton provides a concrete protocol-level answer to the question: how do you maintain accountability in systems built on delegated authority? This is not just a capability-security concern — it is the fundamental question for any multi-agent system where principals delegate to agents who may further delegate to sub-agents.

The proxy/stub architecture maps directly to agent intermediation: a supervisor agent that interposes between a principal and worker agents could implement Horton-style accountability — wrapping delegated capabilities in proxies that record which worker exercised what authority. The sealed/unsealer pattern for identity maps to agent attestation: each agent's identity is cryptographically bound to its actions without requiring a central identity registry.

The paper's concluding statement — "If digital systems are to mediate ever more of our interactions, we must be able to delegate responsibility within them" — reads as prescient given the 2025-2026 expansion of agentic AI. The authors were thinking about networked software objects; the architectural pattern applies equally to networks of AI agents operating on human behalf.
