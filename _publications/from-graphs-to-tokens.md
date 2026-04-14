---
title: "From Graphs to Tokens: Substructure-Aware Molecular Representation for Large Language Models"
collection: publications
category: manuscripts
permalink: /publication/from-graphs-to-tokens
excerpt: 'S2Token treats chemically meaningful molecular substructures as tokens, improving both representativeness and generalization for molecular large language models.'
date: 2026-03-28
venue: 'Information Processing & Management'
slidesurl: 
paperurl: 'https://recynie.github.io/files/from-graphs-to-tokens.pdf'
bibtexurl: 'https://recynie.github.io/files/from-graphs-to-tokens.bib'
citation: 'Runze Wang, Zijie Xing, *Xingyue Liu*, Mingqi Yang, Che He, Yanming Shen, “From Graphs to Tokens: Substructure-Aware Molecular Representation for Large Language Models,” <i>Information Processing and Management</i>, vol. 63, no. 6, p. 104771, Sep. 2026'
---
Abstract
======

Large language models have shown promise for molecular reasoning, but graph tokenization remains a bottleneck. This paper introduces **S2Token**, a substructure-aware tokenizer that fragments molecular graphs into chemically meaningful reusable units instead of relying on atom-level or graph-level tokens alone. The method is designed to preserve both representativeness and generalization when aligning molecular graphs with LLM token spaces.

Key ideas
======

- Treat functional molecular substructures as discrete tokens for molecular LLMs.
- Build a balanced substructure vocabulary through graph decomposition.
- Learn dual-view token embeddings that capture both structural and functional attributes of each substructure.
- Model inter-substructure dependencies with a substructure-level alignment mechanism in the LLM embedding space.
- Evaluate generalization with curated cross-dataset benchmarks spanning four molecular tasks.

Main results
======

- On the molecular caption benchmark, S2Token achieves a **12.6% average improvement** across six metrics over the best LLM-based baseline.
- For forward reaction and retrosynthesis, it improves synthesized-molecule fingerprint similarity by **6.6%** and **8.6%**, respectively.
- On molecular property prediction within the generalist evaluation suite, it reduces MAE by **9.7%** and **3.0%** compared with graph- and node-centric tokenization methods.

Why it matters
======

The paper argues that molecular substructures behave like chemically meaningful "subwords." By tokenizing at that level and explicitly modeling both intra-substructure semantics and inter-substructure dependencies, S2Token gives language models a more transferable representation space for unseen molecules.

Code
======

- [GraphMoLab/S2Token](https://github.com/GraphMoLab/S2Token)
