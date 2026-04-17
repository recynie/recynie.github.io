---
title: "Protein crystallization condition prediction"
excerpt: "A project on extracting structured crystallization conditions from PDB records and predicting key experimental variables from protein data."
collection: portfolio
permalink: /portfolio/protein-crystallization-condition-prediction/
---

Protein crystallization records contain valuable experimental information, but much of it is buried in free-text descriptions in the Protein Data Bank. This project focuses on turning those noisy records into a structured resource for modeling crystallization conditions.

I use LLMs to extract crystallization variables from unstructured PDB text, normalize heterogeneous condition names, and filter out incomplete entries. Based on this pipeline, I built a curated protein sub-database with roughly 7,000 entries that contain both structural information and complete crystallization conditions.

On top of this dataset, I build graph neural network models to predict major crystallization variables such as PEG concentration and polymerization degree. More broadly, this project studies how protein sequence and structure can be linked to the experimental environments in which crystals are obtained.
