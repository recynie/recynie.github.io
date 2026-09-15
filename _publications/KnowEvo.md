---
title: "KnowEvo: Knowledge Evolution for Protein Optimization"
collection: publications
category: manuscripts
permalink: /publication/KnowEvo
excerpt: 'KnowEvo turns experimental feedback into reusable, executable knowledge that evolves through repeated evaluation and revision for protein optimization.'
date: 2026-05-07
venue: 'NeurIPS 2026 (Under review)'
slidesurl: 
paperurl: 'https://recynie.github.io/files/KnowEvo.pdf'
bibtexurl: 
citation: 
---

Overview
======

Scientific discovery depends on accumulating knowledge across experiments. Our starting observation was that an agent could reflect on experimental outcomes, yet often failed to turn those reflections into reusable experience. We wanted to make that experience persistent and open to further testing. Each summary of experience becomes a hypothesis whose usefulness can be evaluated and improved through subsequent experiments.

**KnowEvo treats externalized knowledge as an explicit optimization target.** It represents protein-design expertise as executable knowledge blocks and refines them through repeated evaluation and revision. The goal is to accumulate reusable strategies that improve future design decisions.

How knowledge evolves
======

**Executable knowledge.** Each block expresses a protein-editing strategy with explicit conditions and actions. This gives the knowledge a definite operational meaning: it can be applied without an LLM interpreting it again. Efficient execution also allows more forward evaluations within a given time budget, providing evidence for further revision.

**A tree of alternative strategies.** Feedback from different proteins can suggest different improvements to the same strategy. KnowEvo organizes these revisions into trees that preserve their ancestry and alternative branches. Earlier versions remain available alongside their descendants. This retains diverse strategies as knowledge evolves. An adaptive evaluation policy balances testing promising strategies with exploring uncertain ones.

**Agent-led analysis and revision.** A revision agent can inspect past execution traces, analyze outcomes, and refine the relevant knowledge block. Access to an analysis environment lets it investigate evidence beyond aggregate performance metrics. For example, when faced with many feedback records, the agent can choose to perform statistical analyses to identify changes associated with more consistent gains. This process connects experimental evidence to specific, inspectable revisions.

What the experiments show
======

We study protein stability and solubility, where computational tools provide feedback on proposed mutations. Across both tasks, KnowEvo improves on the initial expert heuristics and the compared program-evolution methods. It finds successful candidates more often and places them earlier in the proposed candidate list. Here, success means improvement under the computational evaluator; these results do not establish wet-lab improvements.

The ablations support preserving alternative knowledge branches: keeping only the latest version in a revision chain substantially reduces performance. The scaling studies also identify two useful axes for further investment: **more revision rounds** and **more agent effort within each revision**. Both can improve strategy quality in the studied setting.

The case studies make these changes concrete. In one stability example, feedback leads a strategy to restrict potentially harmful edits to flexible protein regions. Knowledge evolution can therefore refine the conditions under which a plausible design rule should be applied.

My contributions
======

I contributed across research conception, method design, system development, and paper writing. I designed and implemented the initial end-to-end workflow, and later proposed Thompson-sampling-based evaluation allocation and agent-based knowledge refinement. I also worked on improving evaluation and evolution throughput, enabling the system to conduct iterative experiments more efficiently.

Limitations and outlook
======

KnowEvo focuses on improving knowledge within a defined task and strategy framework. Open-ended exploration remains a challenge. An agent may continue refining a local solution even when a different overall approach would be more useful. Identifying new research questions and extracting feedback that motivates a change of direction require further work.

This limitation motivates my current research on autonomous scientific discovery: agents that formulate research questions, conduct experiments, and use the resulting evidence to reconsider their research direction.
