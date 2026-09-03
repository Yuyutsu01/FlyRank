# Workflow Architecture & Process Diagram

**Track:** General AI Fluency | FL-03  
**Workflow:** Research / Technical Paper Analysis Pipeline  

---

## 1. High-Level Process Flow

```text
========================================================================================
                                NO-CODE AI WORKFLOW PIPELINE
========================================================================================

    [ INPUT: Raw Research Paper (PDF / ArXiv) ]
                        │
                        ▼
    ┌────────────────────────────────────────────────────────┐
    │  STEP 1: GATHER                                        │
    │  • Verify camera-ready PDF source                      │  [HUMAN GATE: Source Authenticity]
    │  • Ingest into Google NotebookLM                       │
    └───────────────────┬────────────────────────────────────┘
                        │ (Document Index)
                        ▼
    ┌────────────────────────────────────────────────────────┐
    │  STEP 2: SYNTHESIZE (NotebookLM)                       │
    │  • Source-grounded query execution                     │
    │  • Extract mechanisms, math, and benchmark tables      │  [HUMAN GATE: Citation Verification]
    │  • Generate citation-anchored extraction notes         │
    └───────────────────┬────────────────────────────────────┘
                        │ (Grounded Extraction Notes)
                        ▼
    ┌────────────────────────────────────────────────────────┐
    │  STEP 3: DRAFT (Claude Project)                        │
    │  • Apply 5-section research brief template             │
    │  • Architecture, mathematical formulation, benchmarks  │
    │  • Synthesize limitations and trade-offs               │
    └───────────────────┬────────────────────────────────────┘
                        │ (Initial Draft Brief)
                        ▼
    ┌────────────────────────────────────────────────────────┐
    │  STEP 4: REVIEW (Claude Project)                       │
    │  • Adversarial peer-review audit                       │
    │  • Overconfidence check & hallucination probe          │  [MANDATORY HUMAN GATE: Fact Audit]
    │  • Baseline discrepancy & compute cost check           │  (Halt pipeline if metrics conflict)
    └───────────────────┬────────────────────────────────────┘
                        │ (Audited & Fact-Checked Draft)
                        ▼
    ┌────────────────────────────────────────────────────────┐
    │  STEP 5: FORMAT (Claude Project)                       │
    │  • GitHub-flavored Markdown & LaTeX equation render    │
    │  • Structured comparison tables & monospace metrics    │  [HUMAN GATE: Final Visual Inspection]
    └───────────────────┬────────────────────────────────────┘
                        │
                        ▼
    [ OUTPUT: Final Verified Research Brief (Markdown) ]
========================================================================================
```

---

## 2. Tool Boundaries & Data Handoffs

```text
┌────────────────────────────────────────┐       ┌────────────────────────────────────────┐
│           GOOGLE NOTEBOOKLM            │       │             CLAUDE PROJECT             │
│        (Source-Grounded Memory)        │       │       (Reasoning & Synthesis Engine)   │
├────────────────────────────────────────┤       ├────────────────────────────────────────┤
│ • Ingests raw PDF text and tables      │       │ • Ingests structured extraction notes  │
│ • Restricts answers strictly to text   │ Handoff│ • Structures 5-beat technical brief    │
│ • Prevents out-of-context hallucination├──────►│ • Runs adversarial fact-check audit    │
│ • Emits inline clickable citations     │ Notes │ • Formats mathematical expressions     │
│                                        │       │ • Produces final GitHub Markdown       │
└────────────────────────────────────────┘       └────────────────────────────────────────┘
                    ▲                                                 ▲
                    │                                                 │
            [Human Operator]                                  [Human Reviewer]
       (Verifies PDF integrity)                         (Validates claims vs. ground truth)
```

---

## 3. Human-in-the-Loop Decision Gates

1. **Gate 1 (Pre-Ingestion)**: Ensure PDF is authentic, complete, and contains all appendices/tables.
2. **Gate 2 (Post-Extraction)**: Click citations in NotebookLM to verify that quantitative metrics (F1, BLEU, ROC-AUC) match original figures.
3. **Gate 3 (Post-Draft Review — Critical)**: Audit flagged discrepancies. If AI overstated a claim beyond what experimental tables support, force correction before proceeding.
4. **Gate 4 (Pre-Publish Approval)**: Final check of formatting, code snippets, and takeaway relevance to active projects (AEGIS, ResearchMind, FlyRank).
