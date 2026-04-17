---
title: "Self-Aware Agent: An agent who manages its own context"
excerpt: "A research-oriented agent runtime that treats context as an explicit inventory with provenance, token costs, and inspectable selection policies."
collection: portfolio
permalink: /portfolio/self-aware-agent/
---

Introduction
=======

Context pruning (compaction), skills, subagents, retrieval, memory... many familiar agent techniques are ultimately ways of managing context. In most current systems, this management happens **automatically**: some parts are handled by framework rules, while other parts are delegated to the model itself, such as dynamic pruning or deciding what context a subagent should inherit.

An important shift in viewpoint is that many of these concepts can be treated simply as *context*:
- Chat history: context pairs (user, assistant)
- Skills: a form of progressive disclosure context
- Subagents: new agent instances whose initial context is selected by a parent agent
- Retrieved documents and tool schemas: task-specific context with cost and provenance

If context management is the core of an agent system, then a natural question follows: **can an agent manage all of its context explicitly, instead of relying on opaque defaults?** This project explores that question.

Self-aware agent (SAA)
=======

Self-Aware Agent (SAA) is a research-oriented Python agent runtime built around one central idea: an agent should treat context as an explicit inventory rather than an invisible prompt assembly step. Instead of blindly injecting all available history, skills, and tool descriptions into each model call, SAA represents each context item with metadata such as origin, token cost, and reason for inclusion.

This design turns context selection into something inspectable and controllable. The agent can ask what information it currently has, what each item costs, why a given item was selected, and what was excluded under a fixed budget. In that sense, the agent becomes "self-aware" not because it reflects on itself in a philosophical sense, but because it can reason about the structure of its own working context.

The current implementation focuses on a minimal but testable scaffold: a Python CLI, a context registry, deterministic selection reports, and dry-run style inspection of the prompt payload before execution. This makes the project useful as a runtime experiment, not just a conceptual proposal, and creates a clean base for later work on more adaptive or learned context policies.

Roadmap
=======

The next step is to move from deterministic selection rules toward richer policies that can compare context items by utility, recency, and task relevance while still preserving traceability. A broader goal is to unify chat history, skills, retrieval outputs, tool specifications, and subagent handoff under the same context abstraction, so that these mechanisms are no longer treated as separate hacks but as parts of one coherent runtime design.

In the longer term, this project connects to my broader interest in agentic research systems and AI scientist infrastructure, especially settings where reproducibility, controllability, and transparent reasoning matter more than maximizing raw autonomy.

Repository: [self-aware-agent](https://github.com/recynie/self-aware-agent)
