# Portfolio Cases

## Voice Card
Direct, technical, clear, grounded, curious, evidence-driven.

---

# Project AEGIS

## The Problem
Rule-based security log inspection fails to detect sophisticated adversarial threats because static threshold rules generate excessive false alarms while missing novel, multi-stage attack patterns. We needed an anomaly detection framework capable of processing streaming audit logs and identifying subtle security risks without swamping engineers in false positives.

## What I Did
- Evaluated isolation forests vs. autoencoder neural networks for high-dimensional anomaly detection; selected an autoencoder architecture in PyTorch due to its ability to capture non-linear feature interactions across log fields.
- Formulated an unsupervised reconstruction loss threshold ($MSE > \tau$) trained exclusively on baseline benign log events.
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
