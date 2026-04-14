---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

A PDF draft of my CV is available [here]({{ '/files/cv.pdf' | relative_url }}).

Education
======
- Dalian University of Technology, School of Future Technology
- Undergraduate student in Artificial Intelligence, 2023-present

Academic performance
======
- Weighted average: 92.3/100
- Second-year academic rank: 4/63
- Second-year comprehensive rank: 23/263
- First four semesters academic rank: 14/63
- CET-6: 618
- CET-4: 591

Selected coursework
======
- Optimization Methods: 98
- Probability and Statistics: 96
- Computer Vision: 96
- Deep Learning: 96
- Foundations of Computer Vision: 93
- Programming for Artificial Intelligence: 92

Research experience
======
### Apr. 2025 - Present

**Language-guided expertise evolution for protein optimization**

- Built a multi-agent system for protein optimization that evolves executable code blocks as an external expertise pool instead of tuning model parameters directly.
- Used gating and evolutionary search to specialize different expertise blocks to different sub-distributions in the protein sequence space.
- Introduced dense natural-language feedback from large language models as the fitness signal for code evolution.
- The early version won the Best Creativity Award in the `玻尔+SciMaster AI4S 智能体开发竞赛`, reached the interview round of MiraclePlus (top 10%), and led to a co-first-author workshop paper at ICLR 2026 RSI.

### Dec. 2023 - Present

**Protein hydration and crystallization condition prediction**

- Extract structured crystallization conditions from free-text Protein Data Bank records with large language models.
- Curated a high-quality protein sub-database with roughly 7,000 entries that contain both complete crystallization conditions and structural information.
- Built graph convolutional models to predict major crystallization variables, including PEG concentration and polymerization degree.
- Currently exploring how hydration information can be incorporated into protein embedding models.

### Oct. 2024 - Dec. 2024

**Motif-driven molecular graph representation learning**

- Studied a motif-based molecular graph representation framework that decouples functional encoding from structural encoding.
- Focused on core experimental work for the resulting publications on motif-aware GNNs and substructure-aware tokenization for molecular LLMs.

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Competitions and awards
======
- 2025 National First Prize, `机械工程创新创意赛无损检测 AI 评片赛` (team leader)
- 2025 Third Prize, Northeast regional round, China Collegiate Computing Contest AIGC Innovation Competition
- 2025 First Prize, Dalian University of Technology Information Security Competition (team leader)

Scholarships
======
- National Scholarship, 2024-2025
- Academic Excellence Scholarship, 2023-2024
- Academic Excellence Scholarship, 2024-2025
