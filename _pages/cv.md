---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

PDF format of my CV is available: [Curriculum Vitae]({{ '/files/CV-en.pdf' | relative_url }}), [个人简历]({{ '/files/CV-zh.pdf' | relative_url }}).

Education
======

- Dalian University of Technology, School of Future Technology
- Undergraduate student in Artificial Intelligence, 2023-present

Academic performance
======

- Weighted average: 89.76/100
- GPA: 3.98/5
- First 5 semesters academic rank: 13/63

**Language test:** CET-6 (591), CET-4 (618)

**Selected coursework:** Probability and Statistics (96), Deep Learning (96), Programming for Artificial Intelligence (92)

Research experience
======

**Language-guided expertise evolution for protein optimization** (Apr. 2025 - Present)

- Built a multi-agent system for protein optimization that evolves executable code blocks as an external expertise pool instead of tuning model parameters directly.
- Used gating and evolutionary search to specialize different expertise blocks to different sub-distributions in the protein sequence space.
- Introduced dense natural-language feedback from large language models as the fitness signal for code evolution.
- The early version won the Best Exploration Award at the Bohrium + SciMaster AI4S Competition, reached the interview round of MiraclePlus (top 10%), and led to a co-first-author workshop paper at ICLR 2026 RSI. 

**Protein hydration and crystallization condition prediction** (Dec. 2023 - Present)

- Extract structured crystallization conditions from free-text Protein Data Bank records with large language models.
- Curated a high-quality protein sub-database with roughly 7,000 entries that contain both complete crystallization conditions and structural information.
- Built graph neural network models to predict major crystallization variables, including PEG concentration and polymerization degree.
- Studied hydration-aware protein representations that go beyond sequence, structure, and coarse electrostatic descriptors.
- Currently exploring surface hydration-guided protein design through representation learning and preference optimization.

**Motif-driven molecular graph representation learning** (Oct. 2024 - Dec. 2024)

- Studied a motif-based molecular graph representation framework that decouples functional encoding from structural encoding.
- Focused on core experimental work for the resulting publications on motif-aware GNNs and substructure-aware tokenization for molecular LLMs.

Publications
======

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Competitions and awards
======

- 2025 National First Prize, Mechanical Engineering Innovation & Creativity Competition – AI-based Non-Destructive Testing Image Evaluation Track (team leader)
- 2025 Third Prize, Northeast regional round, China Collegiate Computing Contest AIGC Innovation Competition
- 2025 First Prize, Dalian University of Technology Information Security Competition (team leader)

Scholarships
======

- National Scholarship, 2024-2025
- Academic Excellence Scholarship, 2023-2024
- Academic Excellence Scholarship, 2024-2025
