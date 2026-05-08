---
title: "KnowEvo: Knowledge Evolution for Protein Optimization"
collection: publications
category: manuscripts
permalink: /publication/KnowEvo
excerpt: 'KnowEvo: An optimization method for knowledge base for protein design tasks.'
date: 2026-05-07
venue: 'NeurIPS 2026 (Under review)'
slidesurl: 
paperurl: 'https://recynie.github.io/files/KnowEvo.pdf'
bibtexurl: 
citation: 
---

Abstract
======

Large language models (LLMs) have shown promise in scientific discovery tasks such as protein optimization, but remain limited by the lack of a mechanism for persistent and reusable  knowledge accumulation. Existing approaches adapt LLMs through parameter optimization or trajectory refinement, but in both cases, knowledge remains implicit, either encoded in opaque model weights or scattered across transient solution histories. As a result, knowledge cannot be systematically inspected, attributed, or reused. We propose _KnowEvo_, a framework that treats externalized knowledge itself as the optimization target. 

Our key insight is that scientific knowledge is inherently modular: multiple interacting mechanisms jointly determine the design outcomes. This makes knowledge evolution fundamentally challenging, as improvements cannot be attributed to individual components in isolation. To address this, _KnowEvo_ represents knowledge as executable expertise blocks and organizes their refinements into strategy mutation trees, enabling structured exploration over a combinatorial knowledge space. The framework combines a forward exploration phase that adaptively allocates evaluation budget across strategy variants with a backward revision phase in which an agentic sandbox converts rollout evidence into localized program improvements. This design enables persistent accumulation, attribution, and refinement of mechanistic expertise across iterative experimentation.

We evaluate _KnowEvo_ on protein optimization tasks including thermostability and solubility. Results show that knowledge evolution consistently improves over initial expert heuristics and outperforms monolithic program evolution and prior LLM-guided evolution baselines across ranking metrics such as pass@$k$, MRR, MAP, and NDCG@5. Codes are available at [https://anonymous.4open.science/r/KnowEvo-6E3B/](https://anonymous.4open.science/r/KnowEvo-6E3B/).

Contributions
======

The main contributions of this paper are:
- We reformulate scientific discovery as optimization over externalized, persistent knowledge rather than over model parameters, decoupling domain adaption from expensive finetuning.
- We represent knowledge as executable expertise blocks organized into mutation trees, and propose a knowledge evolution mechanism that combines adaptive evaluation budget allocation with agentic evidence-driven revision.
- We demonstrate that _KnowEvo_ outperforms root expert heuristics, monolithic program evolution, and prior LLM-guided evolution methods. 
