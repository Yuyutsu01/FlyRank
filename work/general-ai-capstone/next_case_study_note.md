# How to Add the Next Case Study: Standard Operating Procedure

**Track:** General AI Fluency | Impact Project Capstone  
**Target:** Maintaining Portfolio Freshness & Evidence-First Narrative  
**Status:** Canonical Reference  

---

## 1. Where the Next Case Study Goes

Every new piece of work is integrated into two exact repository locations:

1. **Internal Canonical Source of Truth:**
   - File: [`work/week-02-frame-it-as-cases/portfolio_cases.md`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/work/week-02-frame-it-as-cases/portfolio_cases.md)
   - Action: Append a new level-1 heading `# [Project Name]` following the exact three-beat shape below.

2. **Public Portfolio Display:**
   - File: [`portfolio/index.html`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/portfolio/index.html)
   - Section: Under `<section id="work">` as a featured project card styled with `style.css`.
   - Link to Live Proof: Point the card CTA directly to the GitHub repository, live interactive demo, or technical research paper.

---

## 2. The Three-Beat Template (Reused from Week 2)

Do not invent a new structure or write marketing fluff. Every case study must adhere strictly to the established three-beat format:

```markdown
# [Project Name]

## The Problem
[2-3 sentences. Define the real-world friction, operational bottleneck, or engineering failure mode. Name who experiences the problem, what existing solutions fail to do, and why it matters.]

## What I Did
- [Technical Architecture: What framework/model/method was chosen and why (e.g., PyTorch Autoencoder vs. Isolation Forest, Hybrid RAG vs. Naive Vector Search).]
- [Data Pipeline: How raw data was extracted, transformed, and cleaned; note what was intentionally excluded (e.g., PII, target leakage).]
- [Algorithmic Formulation: Objective function, mathematical loss, or chunking strategy used.]
- [Engineering Trade-off: Name one deliberate compromise made (e.g., higher training compute accepted for sub-millisecond inference; latency penalty accepted for factual precision).]

## What Came Of It
- **Quantitative Benchmark**: [One precise, verified metric: ROC-AUC, Precision@K, F1-Score, or percentage gain compared directly against a named baseline.]
- **Efficiency or Error Delta**: [Concrete operational impact (e.g., 64% false positive alert reduction, 3.55x lift in targeting decaying assets).]
- **Honest Status & Active Failure Modes**: [Non-negotiable. What still fails, where the model degrades, and what is currently being debugged (e.g., complex merged PDF tables, anomalous admin scripts).]
```

---

## 3. Four-Step Execution Workflow (5 Minutes in Claude Project)

Because our Claude Project already contains our Voice Card, Identity Kit, and Content Map, drafting the next case takes under 5 minutes:

1. **Open Claude Project ("AI/ML Portfolio Build")**:
   - Do NOT start a blank chat. Open the dedicated project where standing instructions are loaded.

2. **Send the Three-Beat Ingestion Prompt**:
   ```text
   Here are my raw engineering notes for [Project Name]:
   [Paste 5-10 bullet points covering the problem, stack, metrics, and what failed]

   Draft a new case study using our canonical 3-beat shape (The Problem, What I Did, What Came Of It).
   Ensure the Voice Card is respected: direct, technical, clear, grounded, and evidence-driven.
   Do not add marketing hype. Include the honest failure mode.
   ```

3. **Verify Numbers Against Ground Truth**:
   - Manually verify that all quoted metrics match actual experiment logs before accepting the text.

4. **Deploy to Portfolio**:
   - Append the markdown to `work/week-02-frame-it-as-cases/portfolio_cases.md`.
   - Add the card HTML block to `portfolio/index.html`.
   - Run `git add . && git commit -m "Add case study for [Project Name]" && git push origin main`.
   - GitHub Pages will automatically deploy the live update.
