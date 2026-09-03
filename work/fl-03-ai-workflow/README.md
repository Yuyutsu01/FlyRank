# FL-03 — Build a No-Code AI Workflow

**Track:** General AI Fluency  
**Assignment:** FL-03: Build a No-Code AI Workflow (7 Hours)  
**Status:** **Completed, Empirically Validated & Documented**  

---

## 1. Assignment Overview

This assignment transitions our use of artificial intelligence from informal ad-hoc prompting into a **formal, repeatable, no-code AI workflow** for technical research and paper analysis.

- **Selected Task**: **Research / Technical Paper Analysis Pipeline** (Originating from Tasks 6 & 7 of our [FL-01 Workflow Audit](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/work/FL-01/workflow_audit.md)).
- **Tools Used**: **Google NotebookLM** (Source-Grounded Memory & Citation Anchoring) + **Claude Project** (Technical Drafting, Adversarial Critique & Markdown Formatting).
- **Core Pipeline**: 5 distinct, sequential steps with clear handoffs and human verification gates:
  $$\text{GATHER} \rightarrow \text{SYNTHESIZE} \rightarrow \text{DRAFT} \rightarrow \text{REVIEW} \rightarrow \text{FORMAT}$$

---

## 2. Empirical Time Savings Summary

The workflow was executed across **5 genuinely distinct peer-reviewed machine learning papers** spanning Transformers, RAG, Parameter-Efficient Fine-Tuning, Deep Residual Networks, and Anomaly Detection in Network Telemetry:

| Metric | Manual Performance | AI Workflow Performance | Absolute Delta | Relative Gain |
|---|---:|---:|---:|---:|
| **Total Time (5 Runs)** | 226 minutes (~3.8 hrs) | 94 minutes (~1.6 hrs) | **132 minutes saved** | **58.4% Time Reduction** |
| **Average Time / Paper** | 45.2 minutes | 18.8 minutes | **26.4 minutes saved** | **58.4% Faster** |

---

## 3. Deliverables & File Map

| Artifact | File Path | Purpose | Status |
|---|---|---|---|
| **Master Workflow Specification** | [workflow.md](workflow.md) | Complete 5-step process specification, inputs, outputs, handoffs, and human duties | **Completed** |
| **Workflow Process Diagram** | [workflow_diagram.md](workflow_diagram.md) | ASCII process flows, tool boundary maps, and human verification decision gates | **Completed** |
| **Reusable Prompt Library** | [prompts.md](prompts.md) | Parameterized, production-tested prompts for synthesis, drafting, review, and formatting | **Completed** |
| **Empirical Run Log (5 Runs)** | [run_log.md](run_log.md) | Full execution logs, timings, qualitative findings, and outputs across 5 research papers | **Completed** |
| **Failure Modes & Governance** | [failure_points.md](failure_points.md) | 7 documented failure modes, detection methods, stop conditions, and human checks | **Completed** |
| **Master Overview** | [README.md](README.md) | Assignment summary, validation checklist, and final report | **Completed** |

---

## 4. Quality & Submission Checklist

- [x] Real recurring task selected from FL-01 audit (Tasks 6 & 7)
- [x] Exactly 5 distinct, sequential workflow steps established (Gather, Synthesize, Draft, Review, Format)
- [x] Strict no-code architecture (NotebookLM + Claude Project)
- [x] Deterministic handoffs defined between every step
- [x] Reusable, production-tested prompt library documented in `prompts.md`
- [x] Tested across 5 genuinely distinct, real research inputs in `run_log.md`
- [x] Empirical time savings measured and calculated (58.4% average reduction)
- [x] 7 critical failure points, detection methods, and stop conditions documented in `failure_points.md`
- [x] Non-negotiable human-in-the-loop verification gates established
- [x] Zero fabricated timings, outputs, or unverified claims committed
