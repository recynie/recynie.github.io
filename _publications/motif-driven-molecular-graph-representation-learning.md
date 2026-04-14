---
title: "Motif-driven molecular graph representation learning"
collection: publications
category: manuscripts
permalink: /publication/motif-driven-molecular-graph-representation-learning
excerpt: 'Uni-Motif integrates molecular motifs into GNNs through decoupled functional and structural encodings, improving expressiveness across different architectures.'
date: 2025-01-16
venue: 'Expert Systems with Applications'
slidesurl: 
paperurl: 'https://recynie.github.io/files/motif-driven-molecular-graph-representation-learning.pdf'
bibtexurl: 'https://recynie.github.io/files/motif-driven-molecular-graph-representation-learning.bib'
citation: 'Runze Wang, Yuting Ma, *Xingyue Liu*, Zijie Xing, and Yanming Shen, “Motif-driven molecular graph representation learning,” <i>Expert Systems with Applications</i>, vol. 269, p. 126484, 2025'
---
Abstract
======

Subgraph-based GNNs can improve molecular representation learning, but existing approaches often lack a unified way to incorporate motifs across architectures. This paper introduces **Uni-Motif**, a universal motif integration framework that treats each motif as both a chemical identifier and a structural context carrier. The method is built to be compatible with different GNN backbones rather than tied to a single message-passing design.

Key ideas
======

- Decouple each motif into **functional encoding** and **learnable structural encoding**.
- Use functional encoding as a unique motif identifier and structural encoding as local graph context for nodes inside the motif.
- Support both message-passing workflows and global-attention-style workflows within the same motif-aware framework.
- Provide theoretical analysis showing stronger expressiveness than standard local aggregation alone.

Empirical findings
======

- The paper evaluates **seven motif extraction techniques** spanning topology-driven, ring-driven, and rule-driven categories.
- Experiments reported in the paper show that **ring-driven motifs** have a particularly strong effect on downstream performance.
- Across benchmark molecular graph datasets, Uni-Motif achieves competitive or superior results while remaining compatible with different GNN architectures.

Why it matters
======

Molecular motifs are not only structural patterns but also chemically meaningful units. By separating their functional role from their structural role, Uni-Motif gives GNNs a more expressive representation of subtle molecular differences without rewriting the underlying architecture.

Code
======

- [GraphMoLab/Uni-Motif](https://github.com/GraphMoLab/Uni-Motif)
