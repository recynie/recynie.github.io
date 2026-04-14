---
title: "Language-guided expertise evolution for protein optimization"
collection: publications
category: manuscripts
permalink: /publication/language-guided-protein-optimization
excerpt: 'This work reframes protein optimization as evolving an explicit expertise pool, using language-guided multi-agent feedback instead of parameter-heavy reinforcement learning.'
date: 2026-03-05
venue: 'ICLR 2026 Workshop on AI with Recursive Self-Improvement'
slidesurl: 'https://recynie.github.io/files/language-guided-expertise-evolution-for-protein-optimization-poster.pdf'
paperurl: 'https://recynie.github.io/files/language-guided-expertise-evolution-for-protein-optimization.pdf'
bibtexurl: 'https://recynie.github.io/files/language-guided-expertise-evolution-for-protein-optimization.bib'
citation: 'Xingyue Liu, Zijie Xing, Runze Wang, Luoming Hu, and Yanming Shen, “Language-guided expertise evolution for protein optimization,” <i>ICLR 2026 Workshop on AI with Recursive Self-Improvement</i>, 2026'
---
Abstract
======

This work starts from a simple observation: in scientific optimization tasks, the bottleneck is often not model capacity but missing explicit expertise. Instead of adapting an LLM through reinforcement learning, the paper reformulates protein design as the problem of optimizing an external expertise pool. That expertise is organized into reusable blocks, evolved through a mutation tree, and refined with dense language feedback rather than sparse scalar rewards.

Framework
======

- **Generator** proposes candidate protein mutations conditioned on sampled expertise.
- **Critique** turns experimental outcomes into fine-grained language feedback.
- **Curator** updates the expertise pool by refining, retaining, and branching high-utility expertise blocks.
- The expertise pool is represented as a block-based mutation tree, making the optimization process explicit and interpretable.

Main contributions
======

- Reformulate protein design as optimization over reusable external expertise rather than over model parameters.
- Introduce a block-based expertise pool with mutation trees for modular knowledge accumulation.
- Use language-guided multi-agent evolution to refine expertise in a discrete space with denser feedback than standard RL.
- Show higher success rates and substantially better sample efficiency than reinforcement-learning baselines.

Reported results
======

- The paper reports faster convergence and better final solution quality than RL-based baselines on protein stability optimization.
- The accompanying workshop poster reports an **average Pass@1 of 52.3%** on a held-out validation set of 200 proteins.
- The poster also reports an **8% improvement over the backbone model** and stronger performance than the RL-based **Pro-1 Hla (2025)** baseline with lower resource consumption.
- According to the poster, the method achieves better results with **2037 rollouts**, compared with **5000+ rollouts** for Pro-1.

Why it matters
======

The core shift in this paper is from implicit parameter updates to explicit knowledge evolution. That makes the adaptation process more interpretable, more modular, and potentially easier to transfer to other scientific tasks where feedback is sparse or expensive.
