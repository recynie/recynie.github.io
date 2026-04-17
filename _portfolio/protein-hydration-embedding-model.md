---
title: "Protein hydration embedding model"
excerpt: "A project on learning hydration-aware protein representations and using them for downstream prediction and protein design."
collection: portfolio
permalink: /portfolio/protein-hydration-embedding-model/
---

Protein hydration is a key factor for protein function. However, current protein embedding models and protein language models do not explicitly encode hydration information during training. This project asks a simple question: can hydration-aware protein representations improve downstream tasks?

My current work focuses on learning a surface hydration signal from protein structures and distilling it into a lightweight model that can be combined with existing protein embeddings. The goal is not to build a new water prediction model from scratch, but to capture the part of hydration information that is usually missing from sequence-only or structure-only representations.

A related direction is hydration-guided protein design. I am exploring whether local surface hydration can be used as a preference signal for inverse folding models, so that redesigned proteins can be optimized with a more mechanistic objective than charge or coarse stability predictors alone.

Potential downstream applications include stability prediction, protein representation learning, and fixed-backbone protein redesign.
