# Failure Modes, Quality Controls & Human-in-the-Loop Governance

**Track:** General AI Fluency | FL-03  
**Workflow:** Research / Technical Paper Analysis Pipeline  
**Status:** Validated  

---

## 1. Where AI Cannot Be Trusted in Research Analysis

Large Language Models (LLMs) operate probabilistically. While they are exceptional at synthesizing text and drafting structured sections, they possess zero authentic comprehension of physical systems, causal mechanisms, or mathematical validity. 

The following seven failure modes represent real, documented failure points identified during our empirical testing:

---

## 2. Exhaustive Failure Mode Taxonomy

### Failure Mode 1: Methodology & Causal Inversion
- **Description**: The AI confuses the causal direction of an architectural modification or attributes performance gains to the wrong component. (e.g., claiming a new activation function caused an accuracy lift when an unmentioned change in learning rate schedule or batch size was the primary driver).
- **Risk Severity**: **HIGH**. Misguides engineering architecture choices for active projects (AEGIS/ResearchMind).
- **Detection Method**: Compare Step 2 extraction against the ablation study tables in the original paper.
- **Human Check**: Cross-examine Table 1 vs. Table 3 to verify which specific component accounts for the claimed delta.
- **Workflow Stop Condition**: **YES**. Pipeline halts at Step 4 until causal attribution is verified.

### Failure Mode 2: Overconfident / Extrapolated Generalization
- **Description**: The AI takes a localized benchmark victory (e.g., WMT 2014 English-to-German) and states: *"This proves Transformers outperform RNNs across all sequence processing domains."*
- **Risk Severity**: **MEDIUM-HIGH**. Misrepresents research scope and degrades technical credibility.
- **Detection Method**: Automated adversarial check in Step 4 Review Prompt ("Claim vs. Evidence Gap").
- **Human Check**: Review the dataset list in Section 3 of the brief; restrict claims strictly to evaluated tasks.
- **Workflow Stop Condition**: **NO**. Claude Step 4 automatically rewrites the claim with proper boundary qualifiers.

### Failure Mode 3: Inverted or Hallucinated Metrics
- **Description**: AI extracts a number correctly but inverts the metric orientation (e.g., reporting an error rate of 3.57% as an accuracy of 3.57%, or swapping precision and recall).
- **Risk Severity**: **CRITICAL**. Renders technical data factually false.
- **Detection Method**: Click citation anchors in NotebookLM to view the original table cell.
- **Human Check**: Mandatory manual spot-check of all numbers in the Step 3 benchmark comparison table.
- **Workflow Stop Condition**: **YES**. Pipeline halts immediately if a number is incorrect.

### Failure Mode 4: Omission of Computational Constraints & Costs
- **Description**: AI enthusiastically summarizes an algorithm while completely omitting training duration, GPU memory footprint, inference latency, or specialized hardware requirements.
- **Risk Severity**: **HIGH**. Leads to unviable production implementations.
- **Detection Method**: Step 4 Review Prompt explicitly probes for training FLOPs, parameter count, and inference latency.
- **Human Check**: Human audits the hardware specification in the paper (e.g., "Trained for 3.5 days on 8 NVIDIA P100 GPUs").
- **Workflow Stop Condition**: **NO**. Injected as mandatory notes in Section 4 ("Critical Trade-offs").

### Failure Mode 5: Contradictory Source Reconciliation Error
- **Description**: When synthesizing multiple papers on the same topic, the AI tries to smooth over legitimate scientific disagreements by fabricating a middle-ground compromise rather than reporting the contradiction.
- **Risk Severity**: **MEDIUM**. Conceals active research controversies.
- **Detection Method**: NotebookLM multi-source query specifically requesting: "List all direct contradictions or disagreements between Source A and Source B."
- **Human Check**: Human reads the discussion sections of both papers to understand why results diverge (e.g., different dataset pre-processing or evaluation splits).
- **Workflow Stop Condition**: **YES**. Disagreements must be explicitly highlighted in the brief.

### Failure Mode 6: Mathematical Notation & Equation Corruption
- **Description**: Converting complex multi-line mathematical proofs or loss functions into single-line LaTeX often results in missing indices, wrong subscript bounds, or omitted normalization constants.
- **Risk Severity**: **MEDIUM**. Creates confusion during model re-implementation.
- **Detection Method**: Visual inspection of rendered LaTeX in Step 5.
- **Human Check**: Compare the rendered formula against Equation (X) in the original PDF.
- **Workflow Stop Condition**: **NO**. Manual edit of the LaTeX string in the final Markdown file.

### Failure Mode 7: Context Window Truncation on Extensive Appendices
- **Description**: In 30+ page papers with extensive supplementary materials, standard LLM contexts may quietly ignore appendix proofs or hyperparameter tables.
- **Risk Severity**: **LOW-MEDIUM**. Misses implementation details.
- **Detection Method**: NotebookLM explicitly tracks page source citations; missing appendix citations indicate truncation.
- **Human Check**: Query NotebookLM specifically on Appendix sections (e.g., "Extract hyperparameter table from Appendix B").
- **Workflow Stop Condition**: **NO**. Re-run targeted extraction on the appendix document slice.

---

## 3. Human-in-the-Loop Governance Framework

```text
┌───────────────────────────────────────────────────────────────────────────┐
│                    HUMAN-IN-THE-LOOP QUALITY GATES                        │
├───────────────────────────────────────────────────────────────────────────┤
│ 1. SOURCE INTEGRITY GATE (Human Pre-Check):                               │
│    Verify camera-ready status and complete PDF text parsing.              │
│                                                                           │
│ 2. METRIC CITATION GATE (Human Mid-Check):                                │
│    Click NotebookLM citations to verify all extracted benchmark numbers.  │
│                                                                           │
│ 3. ADVERSARIAL CRITIQUE GATE (Mandatory Human Approval):                  │
│    Audit Step 4 critique report. Discard hallucinated or overstated       │
│    claims before final formatting.                                        │
│                                                                           │
│ 4. CODE & MATHEMATICAL VALIDITY GATE (Human Final Sign-Off):              │
│    Verify formulas against paper derivations before applying to projects. │
└───────────────────────────────────────────────────────────────────────────┘
```

> **Master Principle:** *AI is an untrusted research accelerator, never an autonomous arbiter of scientific truth. No brief is considered verified until a human has cross-checked primary claims against ground-truth paper tables.*
