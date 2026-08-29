---
title: "LiteratureCLI: Lightweight literature management for research agents"
excerpt: "A local-first, machine-actionable literature layer that gives research agents persistent access to papers, metadata, full text, and bibliographic structure."
collection: portfolio
permalink: /portfolio/literature-cli/
public: true
---

Repository: [literature-cli](https://github.com/recynie/literature-cli)

Motivation
=======

Literature work is a basic component of scientific research: finding papers, resolving their identities, collecting metadata and full text, organizing a reading set, and producing references for later writing. Research agents can already perform parts of this process through web search or individual scholarly APIs. However, these interactions usually produce transient results. The agent still needs a persistent and structured place where literature can accumulate across tasks.

Most reference managers are designed around graphical interfaces and human interaction. Their internal data may be rich, yet their primary workflows are difficult for an agent to inspect, compose, and verify. At the other extreme, search and retrieval tools give agents immediate access to documents but rarely maintain a coherent local literature base. This leaves a gap between discovering a paper and incorporating it into an ongoing research process.

LiteratureCLI explores the idea that literature management should be treated as part of **agentic research infrastructure**. A research agent needs more than search: it needs a durable literature state that can be updated incrementally, queried precisely, and reused by later workflows.

Design
=======

The project provides a local-first literature layer with a command-line and structured-data boundary. The command-line interface makes each operation explicit and composable, while machine-readable output allows an agent to inspect the result and decide what to do next. A companion agent skill maps research intentions onto these operations and supplies workflow-level guidance.

The central design principle is to separate three concerns:

1. **Literature state** stores papers, authors, affiliations, collections, platform identifiers, files, and derived text as persistent structured data.
2. **Literature capabilities** perform operations such as identity resolution, metadata acquisition, search, organization, reference retrieval, and export.
3. **Agent policy** decides when and why those capabilities should be used during a research task.

This separation keeps the data and core operations independent from a particular model or agent harness. The same literature base remains available across sessions, and different agents can operate on it through a stable interface.

Implementation approach
=======

LiteratureCLI uses a layered architecture. A local relational database acts as the source of truth, with explicit entities and relationships for papers, authors, affiliations, and collections. A service layer integrates heterogeneous scholarly sources and normalizes their records into this shared representation. The CLI exposes the service layer through consistent human-readable and structured outputs, while the skill describes higher-level routing and research workflows.

Scholarly identity is a central implementation concern. A paper may appear as an arXiv record, DOI, OpenReview submission, DBLP entry, local PDF, or bibliographic record. The system preserves platform-specific identifiers while resolving these representations into a single local object. This supports deduplication, later metadata enrichment, and links back to the original scholarly sources.

The acquisition layer follows a fallback-oriented design. Structured scholarly APIs provide metadata whenever possible, and multiple open-access services can contribute document locations. LLMs are reserved for semantic tasks where deterministic sources are insufficient, such as normalizing irregular venue descriptions or producing summaries. This division keeps routine data handling predictable while still allowing semantic enrichment.

PDFs and parsed text are stored alongside bibliographic records, turning the literature base into a bridge between reference management and downstream research tasks. The resulting state can support retrieval, synthesis, citation generation, and future agent workflows without repeatedly reconstructing the same corpus.

Insights
=======

Several broader ideas emerged from this project:

- **Research agents need stateful substrates.** Search, browsing, and retrieval provide observations; a literature system turns those observations into a cumulative research asset.
- **A CLI can serve as an effective agent interface.** It offers a small, inspectable action space with explicit inputs, structured outputs, and straightforward verification.
- **Identity resolution is foundational.** Reliable literature automation depends on connecting the many representations of the same paper before applying more advanced reasoning.
- **Deterministic infrastructure and semantic models have complementary roles.** Databases, identifiers, and scholarly APIs establish stable state. LLMs add value at the ambiguous semantic edges.
- **Capabilities and policy should evolve independently.** The literature engine defines what can be done; an agent skill defines how those operations contribute to a research objective.

At a higher level, LiteratureCLI is an experiment in giving scientific agents an external, persistent literature memory. It treats papers as evolving research objects with identity, provenance, relationships, files, and derived content. This creates a foundation on which more capable systems for literature review, evidence tracking, scientific synthesis, and autonomous research can be built.
