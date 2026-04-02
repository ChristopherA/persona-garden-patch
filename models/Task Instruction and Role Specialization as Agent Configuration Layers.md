---
created: 2026-03-24
author: Christopher Allen
brief_summary: "AGENTS.md (the emerging cross-tool standard for agent project context) provides task instruction — what to build, what conventions to follow, shared project context. Agent persona files provide role specialization — how to think, what to prioritize, when to escalate, how to communicate. These are complementary layers, not competing approaches: AGENTS.md for shared project-level context that any tool can read; persona files for behavioral differentiation that only the host platform uses."
tagline: "AGENTS.md tells the agent what; persona files tell the agent who"
grafted: 2026-04-01
---

- is_a::[Model Form](../forms/Model%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Agentic Architecture](../domains/Agentic%20Architecture.html)
- in_precinct::[Garden Precinct](../glosses/Garden%20Precinct.html)

# Task Instruction and Role Specialization as Agent Configuration Layers

Agentic AI systems receive configuration through multiple channels with different scopes and purposes. Without a model for how these channels relate, teams conflate them or treat them as alternatives — using persona files where shared task context belongs, or using shared context files where behavioral specialization is needed.

Two primary channels serve distinct functions that compose into a coherent whole:

## Structure

### Task Instruction: AGENTS.md

AGENTS.md (emerging across Claude Code, GitHub Copilot, Cursor, and other tools) is a shared, tool-agnostic project context file. It answers: **what does an agent need to know to work in this project?**

- Project architecture, directory conventions, naming rules
- Build and test commands, deployment procedures
- Codebase patterns and anti-patterns
- Domain vocabulary that agents should use
- Constraints on what agents should not modify

AGENTS.md is read by any tool that supports the convention. It is human-authored and committed to the repository. Its content is stable — it changes when project conventions change, not when an individual agent session starts.

### Role Specialization: Agent Persona Files

Agent persona files (agent definitions in platform-specific configuration directories) answer: **how should this agent behave in its assigned role?**

- Thinking stance: what questions to ask, how to reason through problems
- Priority framework: what matters most in this role's scope
- Escalation protocol: when to act autonomously vs. when to check in
- Communication style: how to present findings and ask questions
- Scope boundaries: what this role does not touch

Persona files are behavioral specifications. They are host-platform-specific: a persona file in one tool's configuration is not readable by other tools. Persona files change when role definitions evolve — a different cadence from project conventions.

### The Orchestrator-Worker Pattern

In multi-agent commission architectures, this two-layer model is instantiated as:

| Configuration | Layer | Content |
|---------------|-------|---------|
| Project root context file | Task instruction | Vault conventions, available skills, what not to touch |
| Agent persona: orchestrator | Role specialization | Orchestrator thinking, commission management, merge authority |
| Agent persona: worker | Role specialization | Execution-level focus, form creation, commit discipline |
| Agent persona: organizer | Role specialization | Precinct organization, daily note capture patterns |

The project context file tells any agent what the project is and how to work in it. The persona files tell specific role-agents *how to approach* that work — with different priorities, escalation thresholds, and scope limits.

## Boundaries

This model applies to systems where:
- Multiple agents with different roles work on the same project
- The project has conventions that apply regardless of role
- Role specialization requires behavioral differentiation, not just different task prompts

The model breaks down when:
- A single agent performs all roles (no need for persona differentiation)
- The project has no shared conventions (no AGENTS.md content)
- The host platform does not support persona files (then role specialization must embed in task instruction)

The model also does not address the relationship between these two layers and *session-specific context* — what a single agent carries within an active work session. That is a different layer governed by [[One Context One Concern]]↑ and [[Context Conservation Hierarchy]]↑.

## Sources

- AGENTS.md convention: emerging cross-tool standard (Claude Code, GitHub Copilot, Cursor) for project-level agent context
- Orchestrator-worker commission architecture: documented in garden personas and agent configuration files
- [Augmentation Over Autonomy in Agent Architecture](../decisions/Augmentation%20Over%20Autonomy%20in%20Agent%20Architecture.html) — the decision establishing that personas must escalate to the user on intellectual and editorial judgments
- [[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑ — inquiry on persona design; this model clarifies what persona files govern (behavior) vs. what task instruction governs (content)

## Relations

- relates_to::[Augmentation Over Autonomy in Agent Architecture](../decisions/Augmentation%20Over%20Autonomy%20in%20Agent%20Architecture.html)
  - Role specialization (persona files) is where escalation protocols live. Task instruction (AGENTS.md) sets what to work on; persona files set how to handle decisions within that work.

- relates_to::[[Persona Design Choices Across Analytical Cultural and Professional Axes]]↑
  - That inquiry explores what behavioral dimensions personas should cover; this model clarifies that persona files are the behavioral-specialization layer, separate from task instruction.

- relates_to::[[One Context One Concern]]↑
  - Task instruction and role specialization are loaded once at session start; what agents do within a session (research vs. implementation) is governed by the One Context One Concern pattern.

- relates_to::[[Shearing Layers for Agent Configuration]]↑
  - The shearing layers pattern addresses *where* configuration lives (config vs. state directories); this model addresses *what kind* of content configuration carries (task instruction vs. role specialization).
