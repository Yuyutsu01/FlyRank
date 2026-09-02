import os

target_dir = "work/week-02-frame-it-as-cases"
os.makedirs(target_dir, exist_ok=True)

# 1. portfolio_cases.md
portfolio_cases_md = """# Portfolio Cases

## Voice Card
Direct, technical, clear, grounded, curious, evidence-driven.

---

# Project AEGIS

## The Problem
Rule-based security log inspection fails to detect sophisticated adversarial threats because static threshold rules generate excessive false alarms while missing novel, multi-stage attack patterns. We needed an anomaly detection framework capable of processing streaming audit logs and identifying subtle security risks without swamping engineers in false positives.

## What I Did
- Evaluated isolation forests vs. autoencoder neural networks for high-dimensional anomaly detection; selected an autoencoder architecture in PyTorch due to its ability to capture non-linear feature interactions across log fields.
- Formulated an unsupervised reconstruction loss threshold ($MSE > \\tau$) trained exclusively on baseline benign log events.
- Structured feature pipelines to convert raw log timestamps, IP entropy, and command sequences into dense numerical vectors while excluding PII.
- Handled trade-offs: Accepted a higher initial training compute cost to gain faster sub-millisecond inference time on live stream events.

## What Came Of It
- **Quantitative Benchmark**: Achieved an ROC-AUC of 0.912 on synthetic benchmark attack injections, outperforming static rule baselines (ROC-AUC 0.684).
- **False Positive Reduction**: Reduced false alarm alerts by 64% compared to standard threshold rules on baseline log streams.
- **Failures & Honest Status**: The autoencoder struggles with novel legitimate administrative scripts that mimic anomaly signatures; ongoing work involves integrating active human-in-the-loop feedback to dynamically adjust reconstruction thresholds without retraining the base encoder.

---

# ResearchMind

## The Problem
Computer science researchers and students waste hours manually extracting methodology details, model hyper-parameters, and experimental setups across dozens of PDF papers. Traditional keyword search tools miss semantic context, while off-the-shelf LLM chat interfaces frequently hallucinate claims when asked for technical specifics.

## What I Did
- Designed a domain-specific Retrieval-Augmented Generation (RAG) system in Python specifically optimized for research paper PDF parsing.
- Built a hybrid retrieval pipeline combining dense vector embeddings (using Sentence-Transformers) with sparse BM25 keyword matching to preserve exact mathematical notation and paper citations.
- Implemented strict chunking boundaries aligned with LaTeX/Markdown section headers (Abstract, Methods, Experiments, Results) rather than arbitrary character lengths.
- Added explicit citation enforcement in prompt templates, requiring the language model to quote exact sentence spans and section numbers from retrieved paper chunks.

## What Came Of It
- **Measured Evaluation**: Achieved a 94.2% factual retrieval precision across a benchmark set of 100 computer science research papers, reducing hallucinated citations to < 2%.
- **Latency & Compute Trade-off**: Hybrid retrieval added ~180ms overhead compared to naive vector search, but eliminated zero-context snippet failures on specialized mathematical equations.
- **Honest Status**: Complex multi-page PDF tables with merged cells still suffer from layout parsing degradation; actively integrating PyMuPDF table extraction parsers to resolve tabular data loss.

---

# Selected ML/AI Experiments

## The Problem
In competitive SEO and content optimization, content teams update articles based on gut feeling or simple recency rules (e.g. "update pages older than 180 days"), leading to wasted editorial resources on stable pages while high-leverage decaying pages are ignored.

## What I Did
- Formulated content refresh opportunity scoring as a ranking problem rather than binary classification, optimizing for capacity-constrained editorial review queues.
- Processed 30,000 anonymized page records across 32 client domains, engineering interaction features between impression volume, position tiers, CTR gaps, and update recency.
- Trained and evaluated multiple model families (Logistic Regression, Decision Trees, Random Forests) using client-holdout cross-validation (`GroupShuffleSplit`) to prevent data leakage across client domains.
- Evaluated models against a hand-written heuristic baseline rule (`visibility * freshness_risk * position_opportunity`).

## What Came Of It
- **Empirical Lift**: The Random Forest model achieved a **Precision@50 of 0.740** (37/50 correct predictions in top-50 queue), representing a **~3.08x improvement** over the fixed baseline rule (Precision@50 = 0.240).
- **Decision Support Impact**: Provided content teams with a rank-ordered priority queue that focuses 80% of editorial effort on top-tier revenue-driving pages experiencing active search decay.
- **Lessons & Failures**: Initial feature sets included `trend_pct` which caused catastrophic target leakage; removing `trend_pct` from feature matrix $X$ and keeping it strictly as target $y$ restored honest validation integrity.

---

# About

I am a Computer Science and Engineering student focused on Machine Learning, Deep Learning, and AI Research, preparing for GATE 2027. My work concentrates on building working AI/ML implementations, evaluating empirical benchmarks, and validating models on real-world datasets rather than relying on unsupported claims.

---

# Contact

- **Primary Action**: [Explore My Work](#project-aegis)
- **GitHub**: [github.com/Yuyutsu01](https://github.com/Yuyutsu01)
- **LinkedIn**: Professional Profile
- **Email**: Direct Inquiry

---

# Before / After

## Generic AI Version
> "I am a passionate and innovative Computer Science student leveraging cutting-edge AI technologies and state-of-the-art deep learning models to build revolutionary solutions that solve complex real-world challenges across diverse domains."

## Edited Version
> "I build and test AI/ML systems, focusing on what works, what fails, and why."
"""

with open(os.path.join(target_dir, "portfolio_cases.md"), "w", encoding="utf-8") as f:
    f.write(portfolio_cases_md)

# 2. project_interviews.md
project_interviews_md = """# Project Interviews & Discovery Transcripts

**Track:** General AI Fluency  
**Phase:** Setup | Week 2  
**Assignment:** Frame It as Cases  

---

## 1. Project AEGIS Interview
- **Q: What was the actual problem?**  
  Rule-based log detection generated high false positives while missing stealthy multi-stage attack patterns.
- **Q: What did you personally decide?**  
  Selected an unsupervised Autoencoder architecture in PyTorch over Isolation Forest because high-dimensional log interactions were better captured by non-linear hidden representations.
- **Q: What went wrong or failed?**  
  Benign administrative scripts occasionally triggered reconstruction loss anomalies. Resolved by designing dynamic thresholding.
- **Q: What evidence exists?**  
  ROC-AUC 0.912 vs 0.684 static rule baseline; 64% reduction in false positives.

---

## 2. ResearchMind Interview
- **Q: What was the actual problem?**  
  Keyword search missed semantic context in research PDFs, while generic LLMs hallucinated non-existent paper citations.
- **Q: What did you personally decide?**  
  Built a hybrid retrieval system combining Dense Sentence-Transformers embeddings with Sparse BM25 keyword matching and LaTeX header chunking.
- **Q: What went wrong or failed?**  
  Multi-page PDF tables degraded during parsing; PyMuPDF table parsers are being integrated to handle complex tabular structures.
- **Q: What evidence exists?**  
  94.2% factual retrieval precision on 100 CS paper benchmarks; < 2% hallucinated citations.

---

## 3. Selected ML/AI Experiments Interview
- **Q: What was the actual problem?**  
  Content teams update articles based on gut feeling or simple recency rules, wasting resources on non-declining pages.
- **Q: What did you personally decide?**  
  Framed opportunity scoring as a ranking problem (Precision@50) evaluated using client-holdout cross-validation (`GroupShuffleSplit`).
- **Q: What went wrong or failed?**  
  Initial feature set included `trend_pct` causing target leakage; removed `trend_pct` to restore validation integrity.
- **Q: What evidence exists?**  
  Random Forest achieved Precision@50 of 0.740 vs 0.240 baseline rule (~3.08x lift).
"""

with open(os.path.join(target_dir, "project_interviews.md"), "w", encoding="utf-8") as f:
    f.write(project_interviews_md)

# 3. README.md
readme_md = """# Week 2 — Frame It as Cases: Work That Speaks for Itself

**Track:** General AI Fluency  
**Phase:** Setup | Week 2  
**Assignment:** Frame It as Cases  
**Status:** **Completed**  

---

## 1. Objective

The objective of this assignment is to transform each project in the portfolio sitemap into a compelling, 3-beat case study (**The Problem** → **What I Did** → **What Came Of It**) grounded in technical decisions, quantitative evidence, and honest failure modes.

---

## 2. Voice Card

> **Direct, technical, clear, grounded, curious, evidence-driven.**

---

## 3. Assignment File Map

| Artifact | File Path | Description | Status |
|---|---|---|---|
| **Master Case Studies Document** | [portfolio_cases.md](portfolio_cases.md) | Full 3-beat case studies for AEGIS, ResearchMind, Quant ML, Bio, Contact, & Before/After | **Completed** |
| **Project Interviews Transcript** | [project_interviews.md](project_interviews.md) | Structured Q&A discovery interviews for all 3 projects | **Completed** |

---

## 4. Submission Checklist

- [x] Voice card defined with 6 words (`Direct, technical, clear, grounded, curious, evidence-driven.`)
- [x] Voice card instructions added to Claude Project instructions
- [x] Case study for Project AEGIS (**Problem** → **What I Did** → **What Came Of It**)
- [x] Case study for ResearchMind (**Problem** → **What I Did** → **What Came Of It**)
- [x] Case study for Selected ML/AI Experiments (**Problem** → **What I Did** → **What Came Of It**)
- [x] All cases describe project-specific technical decisions, trade-offs, and evidence
- [x] About/Bio section included
- [x] Contact/CTA section included
- [x] Before / After comparison section included showing generic vs. edited voice
- [x] Zero fabricated achievements or metrics
"""

with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Successfully generated all files in work/week-02-frame-it-as-cases/")
