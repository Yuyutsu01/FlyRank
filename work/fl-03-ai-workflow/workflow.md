# No-Code AI Workflow: Research & Technical Paper Analysis Pipeline

**Track:** General AI Fluency | FL-03  
**Task Origin:** FL-01 Audit Task 6 ("Reading Deep Learning & AI Research Papers") & Task 7 ("Literature Review Synthesis")  
**Target Domain:** AI/ML Research, System Architecture, and Empirical Benchmarking  
**Status:** Completed & Validated  

---

## 1. System Objective & Design Philosophy

The objective of this workflow is to transition from ad-hoc, informal AI querying to a **deterministic, repeatable, no-code research analysis pipeline**. 

In machine learning research, relying on single-shot LLM summaries leads to severe hallucinations: models invent benchmark numbers, confuse ablation studies with primary results, and gloss over vital computational limitations. 

This workflow enforces a strict **Source-Grounded, Human-in-the-Loop Pipeline**:
$$\text{RAW PAPER} \xrightarrow{\text{Grounded Extraction}} \text{VERIFIED EVIDENCE} \xrightarrow{\text{Structured Drafting}} \text{CRITIQUE \& AUDIT} \xrightarrow{\text{Final Polish}} \text{RESEARCH BRIEF}$$

---

## 2. Tool Roles & Division of Responsibilities

We intentionally combine two complementary no-code tools:

| Platform | Primary Function | Why Selected |
|---|---|---|
| **Google NotebookLM** | Source-Grounded Extraction & Citation Anchoring | Strictly constrains extraction to the uploaded PDF/source text; eliminates external internet hallucinations; provides clickable inline source citations for immediate verification. |
| **Claude Project** | Technical Synthesis, Drafting, Adversarial Review & Formatting | Superior reasoning capability for parsing complex mathematical notations, identifying methodology edge cases, and generating clean, publishable Markdown briefs. |

---

## 3. Five-Step Step-by-Step Specification

### Step 1: GATHER (Source Ingestion & Scope Definition)
- **Purpose**: Establish strict boundary conditions and prevent noise injection.
- **Input**: Peer-reviewed conference paper (PDF), ArXiv pre-print, or technical whitepaper.
- **Process**:
  1. Upload clean PDF into a dedicated NotebookLM notebook.
  2. Record metadata: Title, Authors, Venue, Year, Primary Claim, and GitHub Code Link (if released).
  3. Verify document completeness (ensure equations, appendices, and tables are fully parsed).
- **Output**: Source notebook initialized with indexed citations.
- **Handoff to Step 2**: Document text index ready for grounded extraction queries.
- **Human Responsibility**: Verify that the uploaded PDF is the camera-ready version or authoritative ArXiv release, not an unverified blog post.

### Step 2: SYNTHESIZE (Source-Grounded Evidence Extraction)
- **Purpose**: Extract empirical findings, architecture details, and limitations without hallucination.
- **Tool**: **NotebookLM**
- **Input**: Synthesize Prompt applied against the indexed source.
- **Process**: Run the parameterized Extraction Prompt targeting:
  - Exact problem formulation and baseline comparison.
  - Core mathematical/algorithmic mechanism.
  - Empirical benchmark datasets, metrics, and quantitative gains.
  - Explicitly reported failure modes and resource constraints.
- **Output**: Structured extraction notes with exact source page citations.
- **Handoff to Step 3**: Paste extraction notes directly into the Claude Project conversation.
- **Human Responsibility**: Click source citation badges to confirm that claimed metric numbers match the paper's actual tables.

### Step 3: DRAFT (Structured Research Brief Generation)
- **Purpose**: Synthesize the raw extraction into a standardized 5-section technical research brief.
- **Tool**: **Claude Project** ("AI/ML Research & Learning")
- **Input**: Extraction notes from Step 2 + Drafting Prompt.
- **Process**: Claude constructs a standardized research brief:
  1. *Executive Summary & Core Claim*
  2. *Problem Formulation & Baseline Deficiencies*
  3. *Technical Architecture / Methodological Innovation*
  4. *Empirical Validation & Benchmark Results*
  5. *Critical Limitations, Compute Overhead & Open Questions*
- **Output**: Initial draft of the technical research brief.
- **Handoff to Step 4**: Full text draft passed to the review prompt.
- **Human Responsibility**: Check that the architectural description makes conceptual sense and reflects realistic ML systems engineering.

### Step 4: REVIEW (Adversarial Audit & Fact-Checking)
- **Purpose**: Rigorously test every factual claim, check for overconfidence, and audit limitations.
- **Tool**: **Claude Project** (Acting as Skeptical Peer Reviewer)
- **Input**: Initial draft + Review Prompt + Source text snippets.
- **Process**:
  - Audit every metric claim against baseline numbers.
  - Flag any instances where the draft confused correlation with causality.
  - Search for omitted ablation results or computational bottlenecks (e.g., training FLOPs, memory footprint).
- **Output**: Detailed critique highlighting:
  - *Confirmed Claims*
  - *Questionable / Overstated Claims*
  - *Required Corrections*
- **Handoff to Step 5**: Corrected draft incorporating all critique items.
- **Human Responsibility**: Mandatory human gate. Verify any flagged discrepancy directly in the original PDF. Workflow halts if numbers do not match.

### Step 5: FORMAT (Standardized Research Brief Production)
- **Purpose**: Produce a clean, publishable GitHub-flavored Markdown brief.
- **Tool**: **Claude Project**
- **Input**: Audited and corrected draft + Formatting Prompt.
- **Process**: Enforce uniform typography, monospace code/metric blocks, LaTeX equation formatting, and structured markdown tables.
- **Output**: Final standardized Research Brief saved under `work/fl-03-ai-workflow/runs/`.
- **Handoff**: Archival in repository knowledge base.
- **Human Responsibility**: Final visual scan of tables and math syntax.
