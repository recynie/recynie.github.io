---
title: "Language-guided expertise evolution for protein optimization"
collection: publications
category: manuscripts
permalink: /publication/language-guided-expertise-evolution-for-protein-optimization.md
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2026-03-05
venue: 'ICLR 2026 RSI Workshop'
# slidesurl: 'https://academicpages.github.io/files/slides1.pdf'
paperurl: 'https://openreview.net/pdf?id=NeNWeyfUJj'
# bibtexurl: 'https://academicpages.github.io/files/bibtex1.bib'
citation: 'X. Liu, Z. Xing, R. Wang, L. Hu, and Y. Shen, “Language-guided expertise evolution for protein optimization,” Mar. 2026, Accessed: Mar. 06, 2026. [Online]. <i>ICLR 2026 RSI Workshop</i>'
---

Abstract
======
Large language models (LLMs) exhibit strong general reasoning abilities, yet their effectiveness in scientific research such as protein design remains limited. Reinforcement learning (RL)–based fine-tuning is a common strategy for adapting LLMs to such domains, but it suffers from sparse scalar rewards and the prohibitive computational cost of parameter updates. In this paper, we propose an alternative perspective in which adaptation can be cast as an optimization of domain expertise rather than model parameters. Consequently, protein design can be formalized as the problem of identifying an optimal expertise pool—a structured, external knowledge that conditions the model’s generation process. To this end, we introduce a block-based expertise pool, where each expertise block represents a modular knowledge about the protein fitness landscape, and design a mutation tree over blocks to model their evolutionary refinement. We then propose a multi-agent framework to optimize this discrete expertise space using language-based feedback as a dense learning signal. Experiments on protein stability optimization demonstrate that optimizing expertise pools yields faster convergence and higher-quality solutions than RL baselines, while significantly reducing computational overhead. Our results suggest that explicit expertise evolution provides a scalable and interpretable alternative to reinforcement learning for adapting LLMs to complex scientific optimization tasks.
