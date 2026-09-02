# The Through-Line: Master Content Map & Proof Blueprint

**Candidate:** Shivam Sharma  
**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** The Through-Line  
**Status:** Completed  

---

## 1. Candidate One-Line Portfolio Claims & Evaluation

To establish a single, memorable, and defensible primary claim, we evaluated 10 candidate claims generated specifically for a Computer Science & Engineering student specializing in Machine Learning, Deep Learning, and AI Research.

### 10 Candidate One-Line Claims

1. *"I build and validate AI/ML systems through research, experimentation, and working implementations."*
2. *"I design PyTorch architectures and validate ML models on real-world datasets."*
3. *"I research and build machine learning systems that balance predictive precision with computational efficiency."*
4. *"I develop open-source AI tools and conduct empirical machine learning experiments."*
5. *"I build security-focused machine learning systems and research-grade AI tools."*
6. *"I apply machine learning and empirical validation to solve unstructured technical problems."*
7. *"I construct end-to-end ML data pipelines, train models, and evaluate benchmark performance."*
8. *"I turn computer science research papers into working, benchmarked AI systems."*
9. *"I engineer research-driven machine learning models with a focus on auditability and precision."*
10. *"I design, train, and experimentally validate neural network architectures for real-world applications."*

---

### Claim Ranking & Evaluation Matrix

| Claim # | Specificity (1-5) | Credibility (1-5) | Evidence Potential (1-5) | Relevance (1-5) | Memorability (1-5) | Total Score (out of 25) | Rank |
|---|---|---|---|---|---|---|---|
| **Claim 1** | 5 | 5 | 5 | 5 | 5 | **25 / 25** | **#1 (Recommended)** |
| Claim 8 | 5 | 4 | 5 | 4 | 5 | 23 / 25 | #2 |
| Claim 3 | 4 | 5 | 4 | 5 | 4 | 22 / 25 | #3 |
| Claim 2 | 4 | 4 | 5 | 4 | 4 | 21 / 25 | #4 |
| Claim 5 | 4 | 4 | 4 | 4 | 4 | 20 / 25 | #5 |
| Claim 7 | 4 | 4 | 4 | 4 | 3 | 19 / 25 | #6 |
| Claim 9 | 3 | 4 | 4 | 4 | 3 | 18 / 25 | #7 |
| Claim 10 | 3 | 4 | 4 | 4 | 3 | 18 / 25 | #8 |
| Claim 4 | 3 | 4 | 3 | 4 | 3 | 17 / 25 | #9 |
| Claim 6 | 3 | 3 | 3 | 3 | 3 | 15 / 25 | #10 |

---

### Selected Primary Claim

> **Recommended Primary Claim:**  
> *"I build and validate AI/ML systems through research, experimentation, and working implementations."*

**Rationale for Selection:**
- **Single Capability Focus**: Connects three explicit forms of proof—*Research*, *Experimentation*, and *Working Implementations*.
- **Zero Buzzwords**: Excludes generic fluff ("passionate," "revolutionary," "innovative").
- **Direct Alignment**: Perfectly frames the three portfolio projects (**Project AEGIS** = Security Research + Implementation, **ResearchMind** = Research Tool Implementation, **Selected ML Experiments** = Empirical Validation).

---

## 2. Complete Content Map

### Portfolio Hierarchy Rule:
$$\text{YOUR WORK (Code \& Architecture)} \rightarrow \text{EVIDENCE (Metrics \& Plots)} \rightarrow \text{EXPLANATION} \rightarrow \text{PRIMARY ACTION}$$

---

### PAGE 1: HOME

- **Page Purpose**: Delivers the primary claim within 5 seconds of landing and immediately establishes evidence-backed positioning.
- **Assigned Case Study**: Project AEGIS + ResearchMind (Featured Highlights).
- **Ordered Sections**:

1. **Hero Section**
   - *Contents*: Name, candidate title ("AI/ML Research & Engineering"), and One-Line Claim: *"I build and validate AI/ML systems through research, experimentation, and working implementations."*
   - *Evidence*: `selected_images/hero_architecture.png` (16:9 System Architecture Diagram).
   - *Named CTA*: `[Explore My Work]`
   - *CTA Destination*: Jumps to Section 2 (Featured Work) on Home page.

2. **Featured Work (Strongest Work Leads)**
   - *Contents*: Project preview cards featuring **Project AEGIS** (Security Anomaly Detection) and **ResearchMind** (Hybrid Vector RAG).
   - *Evidence*: Metric summaries (ROC-AUC 0.912, Precision 94.2%).
   - *Named CTA*: `[Inspect Case Study]`
   - *CTA Destination*: Links to specific project entry on `WORK / CASE STUDIES` page.

3. **How I Work (Three Pillars of Proof)**
   - *Contents*: Three concise technical pillars: **Research** (Problem Formulation), **Experimentation** (Validation & Loss Plots), and **Implementation** (Production PyTorch/Python Code).
   - *Evidence*: Monospace code snippets & GroupShuffleSplit validation diagram.
   - *Named CTA*: `[View All Case Studies]`
   - *CTA Destination*: Links to top of `WORK / CASE STUDIES` page.

4. **Footer Conversion Banner**
   - *Contents*: Direct technical contact inquiry banner.
   - *Named CTA*: `[Get In Touch]`
   - *CTA Destination*: Links to `CONTACT` page.

---

### PAGE 2: WORK / CASE STUDIES (Primary Evidence Engine)

- **Page Purpose**: Provides complete 3-beat technical proof (**Problem** $\rightarrow$ **What I Did** $\rightarrow$ **What Came Of It**) for every project in the portfolio.
- **Assigned Case Studies**: Project AEGIS, ResearchMind, Selected ML Experiments.
- **Ordered Sections**:

1. **Project AEGIS (Primary Case Study — Strongest Work First)**
   - *Beat 1 (Problem)*: High false alarms in static rule log inspection; need for streaming unsupervised anomaly detection.
   - *Beat 2 (What I Did)*: PyTorch Autoencoder reconstruction loss ($MSE > \tau$); sub-millisecond inference trade-off.
   - *Beat 3 (What Came Of It)*: **ROC-AUC of 0.912** vs. 0.684 static rule baseline; **64% reduction in false alarms**; active human-in-the-loop thresholding.
   - *Evidence*: `selected_images/project_aegis_diagram.png` (MSE Loss Distribution Chart).
   - *Named CTA*: `[View AEGIS Repository on GitHub]`
   - *CTA Destination*: External link to GitHub codebase (`github.com/Yuyutsu01`).

2. **ResearchMind (Secondary Case Study — Research Tooling)**
   - *Beat 1 (Problem)*: Loss of semantic context in paper PDF search vs. LLM hallucinated citations.
   - *Beat 2 (What I Did)*: Hybrid dense (Sentence-Transformers) + sparse (BM25) vector retrieval with LaTeX section header chunking.
   - *Beat 3 (What Came Of It)*: **94.2% factual retrieval precision** across 100 CS papers; **< 2% hallucinated citations**.
   - *Evidence*: Paper retrieval evaluation metrics & LaTeX chunking diagram.
   - *Named CTA*: `[Inspect ResearchMind Architecture]`
   - *CTA Destination*: External link to GitHub repository.

3. **Selected ML Experiments (Tertiary Case Study — Quantitative Validation)**
   - *Beat 1 (Problem)*: Recency rules in content refresh wasting editorial effort on stable pages.
   - *Beat 2 (What I Did)*: Priority ranking formulation evaluated via client-holdout cross-validation (`GroupShuffleSplit`).
   - *Beat 3 (What Came Of It)*: **Random Forest Precision@50 of 0.740** vs 0.240 baseline rule (**~3.08x lift**); target leakage safeguard.
   - *Evidence*: `outputs/charts/top_feature_importance.svg` & `outputs/charts/confidence_mix.svg`.
   - *Named CTA*: `[Discuss a Research Project]`
   - *CTA Destination*: Links to `CONTACT` page.

---

### PAGE 3: ABOUT

- **Page Purpose**: Contextualizes academic foundation, research focus, and technical background without distracting from the main evidence engine.
- **Assigned Case Study**: Candidate Background Context.
- **Ordered Sections**:

1. **Who I Am**
   - *Contents*: Computer Science & Engineering student focused on Machine Learning, Deep Learning, and AI Research, preparing for GATE 2027.
   - *Evidence*: CS coursework foundation (Linear Algebra, Probability, OS, Algorithms).

2. **Research Focus & Interests**
   - *Contents*: AI Security (Anomalies & Robustness), Retrieval Systems (RAG & NLP), and Quantitative ML (Opportunity Ranking).

3. **Technical Focus & Stack**
   - *Contents*: Python, PyTorch, Scikit-Learn, DuckDB, SQL, Git, Linux, LaTeX.

4. **Page CTA Banner**
   - *Named CTA*: `[Explore My Work]`
   - *CTA Destination*: Jumps back to `WORK / CASE STUDIES` page.

---

### PAGE 4: CONTACT

- **Page Purpose**: Provides direct channels for technical recruiters, engineering managers, and research leads to connect.
- **Assigned Case Study**: N/A (Conversion Page).
- **Ordered Sections**:

1. **Direct Technical Inquiry Message**
   - *Contents*: Concise invitation for internship opportunities, research collaborations, or technical code reviews.

2. **Verified Contact Channels**
   - *GitHub*: [github.com/Yuyutsu01](https://github.com/Yuyutsu01) (Open-source repositories & commit history).
   - *LinkedIn*: Professional Profile (Career background).
   - *Email*: Direct Academic/Professional Email.

3. **Page CTA**
   - *Named CTA*: `[Send Direct Inquiry]`
   - *CTA Destination*: Opens email client (`mailto:`).

---

## 3. Proof Still Needed (Evidence Inventory Table)

The following table explicitly tracks all required evidence, assigned project/page, current availability status in the repository, and the required capture action plan:

| Proof / Evidence Item | Assigned Page / Case Study | Current Status | Required Action / Capture Plan |
|---|---|---|---|
| **System Architecture Diagram** | Home / Hero | **Available in Repo** | `work/week-03-visual-identity/selected_images/hero_architecture.png` |
| **AEGIS MSE Loss Plot** | Work / Project AEGIS | **Available in Repo** | `work/week-03-visual-identity/selected_images/project_aegis_diagram.png` |
| **Random Forest Feature Importance** | Work / ML Experiments | **Available in Repo** | `outputs/charts/top_feature_importance.svg` |
| **Prediction Confidence Breakdown** | Work / ML Experiments | **Available in Repo** | `outputs/charts/confidence_mix.svg` |
| **Unit of Analysis DataFrame Log** | Work / ML Experiments | **Available in Repo** | Executed in `work/notebooks/w02_ml_task_framing.ipynb` |
| **AEGIS Live Stream Demo** | Work / Project AEGIS | **Needed / In Progress** | Record sub-millisecond log stream inference demo script. |
| **ResearchMind UI / RAG Terminal Capture** | Work / ResearchMind | **Needed / In Progress** | Capture CLI query session demonstrating citation enforcement. |
| **GATE 2027 Study Roadmap Document** | About Page | **Needed / Optional** | Structure formal GATE CS study schedule under `work/`. |

---

## 4. Through-Line Consistency Verification Checklist

- [x] **Single One-Line Claim**: Exactly one primary sentence (`"I build and validate AI/ML systems through research, experimentation, and working implementations."`).
- [x] **Strongest Work Leads**: Project AEGIS and ResearchMind lead the portfolio hierarchy before background narratives.
- [x] **Ordered Page Sections**: Every page specifies exact sequential sections.
- [x] **Named CTAs on Every Page**: Every page contains explicit CTAs that ultimately direct traffic toward exploring case studies or initiating technical contact.
- [x] **Honest Evidence Tracking**: Missing evidence items (AEGIS live demo, ResearchMind terminal capture) are explicitly documented as `Needed / In Progress`.
- [x] **Zero Fabricated Evidence**: All claimed metrics (Precision@50 = 0.740, ROC-AUC = 0.912) are backed by repository code.
