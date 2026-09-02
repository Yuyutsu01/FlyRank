# Project Interviews & Discovery Transcripts

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
