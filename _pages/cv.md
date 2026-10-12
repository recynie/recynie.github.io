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

**Contact:** aroma@mail.dlut.edu.cn · +86 15842668147 · [recynie.github.io](https://recynie.github.io)

Education
======

- Dalian University of Technology, School of Future Technology
- Undergraduate in Artificial Intelligence, 2023–2027

Academic performance
======

- Academic score: 87.0/100
- First five semesters academic rank: 13/64
- Second-year academic rank: 4/64

**Language tests:** CET-4 (618), CET-6 (591)

**Selected coursework:** Probability and Statistics (96), Deep Learning (96), Programming for Artificial Intelligence (92)

Research experience
======

**Language-guided expertise evolution for protein optimization** (Apr. 2025 – May 2026)

**Advisor:** Prof. Yanming Shen

- Developed a self-evolving agent system for protein optimization through explore–verify–refine cycles, accumulating executable prior knowledge in a code-based knowledge base.
- Represented knowledge as a code population, with gating mechanisms to match and optimize target protein sub-distributions.
- Used Thompson sampling during training and lower confidence bound (LCB) scoring for final knowledge selection to balance exploration and exploitation.
- Built an agent workspace containing parent-node strategies, validation results, and metrics to support feedback-driven exploration and analysis.
- Built a high-concurrency agent system from scratch, decoupling exploration from knowledge updates and supporting multiple servers for efficient resource use.
- An early version won the Best Innovation Award at the Bohr + SciMaster AI4S Agent Development Competition (only two teams awarded) and reached the MiraclePlus startup camp interview round (top 10%). This work led to co-first-author papers accepted at ICLR 2026 RSI Workshop and NeurIPS 2026.

**Molecular representation learning** (Oct. 2024 – Dec. 2024)

**Advisor:** Prof. Yanming Shen

- Integrated molecular motifs into GNNs and LLMs to improve representation learning beyond the limits of 1-WL testing and one-dimensional SMILES representations.
- For Uni-Motif, designed and evaluated three substructure feature fusion mechanisms and compared motif decomposition strategies.
- For S<sup>2</sup>Token, proposed and evaluated substructure-aware tokenization and reproduced leading baselines to validate motif-augmented performance gains.
- Co-authored papers published in *Expert Systems with Applications* and *Information Processing & Management*.

**Protein hydration and crystallization condition prediction** (Dec. 2023 – Present)

**Advisor:** Prof. Song Xue

- Modeled relationships among protein sequences, structures, and chemical environments to predict crystallization conditions.
- Built a crystallization condition database of roughly 7,000 proteins by extracting, filtering, and integrating records from the Protein Data Bank.
- Used Foldseek to cluster structurally similar proteins and analyze solution-component combinations and crystallization condition distributions.
- Fine-tuned SaProt, a pretrained structure-aware protein language model, on the crystallization condition task.
- Found that protein language models struggle to represent crystallization conditions. Current work adds hydration as a downstream modality and develops hydration-aware protein representations.

Publications
======

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Personal projects
======

**Self-Aware Agent** (Mar. 2026) — [GitHub](https://github.com/recynie/self-aware-agent) · [Project details]({{ '/portfolio/self-aware-agent/' | relative_url }})

- Explores agent-controlled context management by formalizing chat history, tool calls, skills, and other inputs as context items that the agent can manage and assemble.

**pi-goal** (Aug. 2026) — [GitHub](https://github.com/recynie/pi-goal) · [Project details]({{ '/portfolio/pi-goal/' | relative_url }})

- Developed a verifiable `/goal` extension for long-horizon tasks, with interactive requirement clarification and explicit deliverables and termination criteria.
- Uses an independent fresh-context verifier to check outputs against the agreed criteria, improving alignment and reducing premature completion.

Competitions and awards
======

- **Sep. 2025:** National First Prize, Mechanical Engineering Innovation & Creativity Competition – AI-based Non-Destructive Testing Image Evaluation Track (team leader). Detected weld defects in X-ray images; handled data preprocessing, model deployment, and fine-tuning of YOLOv8, RT-DETR, and DEIM.
- **Jun. 2025:** First Prize, Dalian University of Technology Information Security Competition (team leader). Designed a benchmark and testing platform for LLM text watermark attacks; proposed the project direction, built the code framework, and reproduced paraphrasing attacks. The team reproduced five attack papers.

Scholarships
======

- National Scholarship, 2024–2025
- Academic Excellence Scholarship, 2024–2025
- Academic Excellence Scholarship, 2023–2024

Research interests
======

- **Autonomous scientific research:** Improve AI's long-horizon research ability through iterative idea development with experimental feedback to propose valuable, feasible ideas.
- **Protein representation:** Develop structure-aware and hydration-aware protein representations to improve downstream task performance.

Skills
======

- **AI agents:** Self-evolving agents, agent harness design
- **AI for Science:** Protein representation learning, molecular representation learning, protein optimization
