# Week 2 — FL-02: Prompt Engineering

**Track:** General AI Fluency  
**Phase:** Setup | Week 2  
**Assignment:** FL-02 — Prompt Engineering  
**Status:** **Completed**  

---

## 1. Objective

The objective of this assignment is to take one real task from the FL-01 workflow audit (**Research-Paper Analysis**) and systematically improve the prompt using five named prompting techniques, documenting observed output changes across 6 runs and comparing final prompt execution across two frontier models (Claude & ChatGPT).

---

## 2. The 5 Prompting Techniques Applied

| Version | Technique Added | Single Prompt Change | Observed Output Impact |
|---|---|---|---|
| **V0** | **Naive Baseline** | `"Analyze this research paper..."` | Generic high-level summary; lacks technical depth. |
| **V1** | **Role Assignment** | `"You are an experienced ML researcher."` | Elevated technical jargon ($O(1)$ complexity, representation subspaces). |
| **V2** | **Context + Motivation** | Student background & learning goals. | Aligned output directly with problem formulation & experiment design. |
| **V3** | **Few-Shot Examples** | 4-line Problem/Method/Result exemplar. | Adopted concise, precise structural pattern; extracted FLOPs ($3.1 \times 10^{19}$). |
| **V4** | **Output Structure** | 8-section numbered schema. | Ensured 100% structural coverage (P100 GPUs, datasets, future directions). |
| **V5** | **Step Decomposition** | 7-step process + anti-hallucination rule. | Enforced 100% ground-truth grounding and separated stated vs. unstated facts. |

---

## 3. Assignment File Map

| Artifact | File Path | Description | Status |
|---|---|---|---|
| **Iteration Log** | [prompt_iteration_log.md](prompt_iteration_log.md) | Full 6-version iteration log & cross-model comparison | **Completed** |
| **Final Reusable Prompt** | [final_reusable_prompt.md](final_reusable_prompt.md) | Parameterized prompt template without personal context | **Completed** |
| **Evidence Status** | [EVIDENCE_REQUIRED.md](EVIDENCE_REQUIRED.md) | Evidence tracking checklist | **Completed** |
| **Output Run 0** | [outputs/v0_naive.md](outputs/v0_naive.md) | V0 Naive Baseline prompt & output | **Completed** |
| **Output Run 1** | [outputs/v1_role.md](outputs/v1_role.md) | V1 Role Assignment prompt & output | **Completed** |
| **Output Run 2** | [outputs/v2_context.md](outputs/v2_context.md) | V2 Context & Motivation prompt & output | **Completed** |
| **Output Run 3** | [outputs/v3_few_shot.md](outputs/v3_few_shot.md) | V3 Few-Shot Examples prompt & output | **Completed** |
| **Output Run 4** | [outputs/v4_structure.md](outputs/v4_structure.md) | V4 Output Structure prompt & output | **Completed** |
| **Output Run 5** | [outputs/v5_decomposition.md](outputs/v5_decomposition.md) | V5 Step Decomposition & Cross-Model comparison | **Completed** |

---

## 4. Submission Checklist

- [x] Reused real task from FL-01 workflow audit (**Research-Paper Analysis**)
- [x] Created exactly 6 versions (V0 through V5)
- [x] Each version adds exactly ONE named technique
- [x] Analyzed observed OUTPUT text changes for each version
- [x] Executed V5 prompt on BOTH **Claude** and **ChatGPT** with detailed comparison table
- [x] Formulated parameterized reusable template without personal context in `final_reusable_prompt.md`
