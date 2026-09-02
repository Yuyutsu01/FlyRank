# Prompt Iteration Log: FL-02 Prompt Engineering

**Track:** General AI Fluency  
**Phase:** Setup | Week 2  
**Assignment:** FL-02 — Prompt Engineering  
**Selected Real Task:** Research-Paper Analysis  

---

## Iteration Progress Summary

```text
V0: Naive Baseline
  └─► V1: + Role Assignment
        └─► V2: + Context & Motivation
              └─► V3: + Few-Shot Examples
                    └─► V4: + Output Structure
                          └─► V5: + Step Decomposition & Anti-Hallucination
                                └─► Cross-Model Comparison (Claude vs ChatGPT)
```

---

## 1. V0 — Naive Baseline
- **Prompt:** `"Analyze this research paper and explain it to me."`
- **What Changed:** Initial baseline starting point.
- **Observed Output:** High-level summary of Transformer model; generic prose without technical formulas or hardware details.
- **Why It Mattered:** Establishes the baseline quality of unguided AI outputs.
- **What Still Failed:** Fails to explain *how* self-attention works, omits dataset specs, ends with generic fluff.
- **What to Try Next:** Add role assignment to set technical expectations.
- **Full Output Artifact:** [outputs/v0_naive.md](outputs/v0_naive.md)

---

## 2. V1 — Role Assignment
- **Prompt:** Added `"You are an experienced machine learning researcher."`
- **What Changed:** `+ Role Assignment`
- **Observed Output:** Jargon density increased; introduced $O(1)$ path length, sequence recurrence trade-offs, and multi-head subspaces.
- **Why It Mattered:** Forces the AI to adopt expert vocabulary and focus on technical architecture.
- **What Still Failed:** Assumed advanced user knowledge; dense unguided paragraphs.
- **What to Try Next:** Add user context and learning goals.
- **Full Output Artifact:** [outputs/v1_role.md](outputs/v1_role.md)

---

## 3. V2 — Context + Motivation
- **Prompt:** Added student background and learning goals (understanding problem formulation, experiments, limitations).
- **What Changed:** `+ Context & Motivation`
- **Observed Output:** Shifted output focus directly to problem formulation, experimental design, and evaluation metrics.
- **Why It Mattered:** Aligns generated content with user-specific educational objectives.
- **What Still Failed:** Unstructured continuous prose; missing hardware and dataset numbers.
- **What to Try Next:** Provide a few-shot exemplar.
- **Full Output Artifact:** [outputs/v2_context.md](outputs/v2_context.md)

---

## 4. V3 — Few-Shot Examples
- **Prompt:** Added a 4-line exemplar demonstrating Problem/Method/Result/Limitation density.
- **What Changed:** `+ Few-Shot Examples`
- **Observed Output:** Adopted exact 4-part concise structural pattern; extracted FLOPs ($3.1 \times 10^{19}$) and baseline model names.
- **Why It Mattered:** Demonstrates that concrete examples communicate formatting and density faster than prose instructions.
- **What Still Failed:** Exemplar was too brief; missed hardware setup and future directions.
- **What to Try Next:** Add a complete 8-section output structure.
- **Full Output Artifact:** [outputs/v3_few_shot.md](outputs/v3_few_shot.md)

---

## 5. V4 — Output Structure
- **Prompt:** Added an 8-section numbered output schema.
- **What Changed:** `+ Output Structure`
- **Observed Output:** Generated explicit numbered headings covering hardware setup (P100 GPUs), datasets (4.5M/36M pairs), and future directions.
- **Why It Mattered:** Prevents the AI from omitting secondary technical details by creating explicit slots.
- **What Still Failed:** Unverified limitations listed without distinguishing paper proof vs AI speculation.
- **What to Try Next:** Add step-by-step process decomposition and anti-hallucination constraints.
- **Full Output Artifact:** [outputs/v4_structure.md](outputs/v4_structure.md)

---

## 6. V5 — Step Decomposition & Ground-Truth Verification
- **Prompt:** Added 7-step process order and explicit rule: do not invent information, state when something is unavailable.
- **What Changed:** `+ Step Decomposition & Anti-Hallucination`
- **Observed Output:** Generated rigorous, step-by-step paper analysis with clear separation of author-backed facts vs unstated information.
- **Why It Mattered:** Ensures 100% auditability and ground-truth reliability.
- **Full Output Artifact:** [outputs/v5_decomposition.md](outputs/v5_decomposition.md)

---

## 7. Cross-Model Comparison (Claude vs. ChatGPT on V5 Prompt)

| Dimension | Claude (Claude 3.5 Sonnet) | ChatGPT (GPT-4o) |
|---|---|---|
| **Tone** | Highly formal, academic, and methodologically precise ($h=8$, $100k$ steps). | Accessible, structured, conversational. |
| **Accuracy** | 100% grounded in paper text; cited section numbers (Section 3.2, 5.1). | Accurate core facts, but omitted exact step counts ($100k$/$300k$). |
| **Structure** | Strictly followed 8-section layout; explicitly tagged Stated vs. Unstated limitations. | Followed layout, but merged external knowledge into limitations section. |
| **Failure Points** | Highly dense phrasing; slightly less readable for beginners. | Included external interpretation ($O(n^2)$ memory) without tagging as unstated in text. |
