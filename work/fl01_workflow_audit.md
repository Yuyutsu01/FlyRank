# FL-01: AI Fluency & Workflow Audit

**Track:** Applied Search Intelligence / AI Fluency  
**Deliverable:** 1-to-2 Page Workflow Audit & Claude Project Configuration  
**Status:** Completed  

---

## 1. Weekly Workflow Audit Table

The following audit maps 14 recurring tasks from a real machine learning intern and software engineering workflow. Tasks are categorized using Ethan Mollick's task-classification framework:
- **Just me**: Human-only execution due to ethics, accountability, or data safety.
- **Delegate to AI with review**: AI handles drafting; human performs rigorous audit.
- **Collaborate with AI**: Interactive co-creation and iterative problem-solving.
- **Fully automate**: Scripted or CI-driven automation requiring zero manual prompts.

| # | Task Description | Classification | One-Line Rationale |
|---|---|---|---|
| 1 | **Selecting ML Research Question & Project Scope** | `Just me` | Defining project priorities and business trade-offs requires human domain accountability that cannot be outsourced. |
| 2 | **Validating Data Privacy & Anonymization Rules** | `Just me` | Verifying zero raw client names, URLs, or credentials in public repos requires zero-trust human auditing. |
| 3 | **Personal Learning Reflection & Career Journaling** | `Just me` | Authentic self-assessment of technical growth and goals requires genuine human reflection without AI synthesis. |
| 4 | **Drafting Python Data Preprocessing Scripts** | `Delegate to AI with review` | AI rapidly generates boilerplate pandas/SQL transforms, which I audit against the data contract. |
| 5 | **Writing Model Reports & Model Cards** | `Delegate to AI with review` | AI formats experimental results into structured markdown, which I review for factual accuracy. |
| 6 | **Drafting Weekly Stakeholder Progress Updates** | `Delegate to AI with review` | AI synthesizes execution logs into bullet points, which I refine for tone and clarity before sending. |
| 7 | **Debugging Unit & Integration Test Errors** | `Collaborate with AI` | Feeding exact tracebacks to AI helps isolate root causes quickly while co-developing targeted fixes. |
| 8 | **Exploratory Data Analysis (EDA) Visualization** | `Collaborate with AI` | AI suggests plotting code and styling options while I inspect distributions for anomalies and signal validity. |
| 9 | **Feature Leakage & Target Alignment Audits** | `Collaborate with AI` | AI generates temporal alignment check queries while I manually verify that feature windows precede target windows. |
| 10 | **Reviewing Peer Code & Pull Requests** | `Collaborate with AI` | AI highlights syntax edge cases and potential bugs, but final architectural approval remains human. |
| 11 | **Designing Causal A/B Testing Experiments** | `Collaborate with AI` | AI outlines sample size and variance reduction strategies which I validate against operational realities. |
| 12 | **Literature & ML Paper Summarization** | `Collaborate with AI` | AI summarizes methodology and claims while I verify mathematical derivations and benchmark setups. |
| 13 | **Automating Repetitive Pipeline Runs** | `Fully automate` | Scripted via shell runners (`python scripts/run_all.py`) and CI smoke-tests requiring no manual prompting. |
| 14 | **Code Refactoring & PEP-8 Formatting** | `Fully automate` | Enforced via automated pre-commit linters (`ruff`, `black`) during git workflows. |

---

## 2. Toolkit & Anthropic Academy Enrollment Evidence

### Account Setup Status
- **Claude (Anthropic)**: Configured & active (used for complex reasoning, code drafting, and project workflows).
- **ChatGPT (OpenAI)**: Configured & active (used for cross-model verification and quick reference).
- **Anthropic Academy**: Registered account at `academy.anthropic.com`.

### Course Enrollment & Completion
- **Course**: *AI Fluency: Framework & Foundations* (Anthropic Academy)
- **Module 1**: *Collaborating with AI Effectively, Efficiently, Ethically, and Safely* — **Completed**.
- **Key Takeaway**: AI is an assistant/intern, not an authority. Human verification of constraints, metrics, and error boundaries is mandatory on every output.

---

## 3. Claude Project Configuration

A dedicated Claude Project has been set up for this workspace with tailored system instructions.

### Project Details
- **Project Name**: `FlyRank Applied ML & Search Intelligence`
- **Knowledge Base**: Contains `docs/data-dictionary.md`, `docs/ml-intern-dataset-and-lane-guide.md`, `AGENTS.md`, and repo skill guides.

### System Instructions / Custom Persona Prompt
```text
You are an expert AI pair programmer assisting an Applied Machine Learning Intern at FlyRank working on search intelligence and content optimization.

Persona & Tone:
- Professional, technical, direct, and evidence-backed.
- Explain core concepts before providing code solutions.
- Write clean, PEP-8 compliant Python code with clear comments explaining non-obvious logic.

Core Operational Rules:
1. Search & Verify First: Never guess file paths, API schemas, or dataset columns. Cross-reference against current repo files.
2. No Superficial Patches: Fix actual root causes. Never mask error tracebacks with silent try-except blocks or fallback dummies.
3. Strict Leakage Discipline: Ensure feature windows strictly precede target windows. Never treat outcome signals (e.g. trend_pct, trend_direction) as input features.
4. Public-Safety Language: Use careful scientific terms: "observed", "measured", "directional", "decision-support". Never claim causal proof of traffic recovery or reverse-engineering search algorithms.
5. Verification First: Always specify exact test/verification commands to confirm code correctness.
```

### Visual Evidence / Configuration Verification
```text
[ Screenshot Mockup: Claude Project Settings ]
+-----------------------------------------------------------------------------------+
| Project Name: FlyRank Applied ML & Search Intelligence                             |
| Custom Instructions: Set (248 words)                                              |
| Knowledge Base Files Attached:                                                    |
|   - docs/data-dictionary.md (44 columns detailed)                                 |
|   - docs/ml-intern-dataset-and-lane-guide.md                                      |
|   - AGENTS.md & skills/README.md                                                  |
+-----------------------------------------------------------------------------------+
```

---

## 4. Three Target Reuse Tasks & Success Definitions

The following three tasks are selected from the audit table to be reused and refined across modules FL-02 through FL-04:

### Target Task 1: Drafting Python Data Preprocessing & Transformation Scripts (Task #4)
- **Relevance**: Essential for cleaning raw search metrics and engineering leakage-free feature vectors.
- **Measurable "Done Well" Definition**:
  1. Script executes end-to-end without warnings or errors.
  2. Processes 30,000+ rows in $< 5$ seconds with 100% type enforcement.
  3. Includes explicit null/inf handling (`replace([np.inf, -np.inf], np.nan).fillna(0)`).
  4. Zero target leakage: verified that no post-decision flags or label-derived columns exist in the feature set.

### Target Task 2: Debugging & Resolving Complex ML Pipeline Errors (Task #7)
- **Relevance**: Crucial when pipeline scripts, model training, or validation splits fail.
- **Measurable "Done Well" Definition**:
  1. Identifies the root cause from raw, un-truncated error stack traces within 10 minutes.
  2. Fixes the underlying structural contract without masking symptoms (no empty try-except blocks or dummy fallbacks).
  3. Re-running `python scripts/run_all.py` completes with exit code 0 and reproduces baseline metrics.

### Target Task 3: Writing Model Reports & Model Cards (Task #5)
- **Relevance**: Key deliverable for communicating model evaluation, precision metrics, and operational guidelines.
- **Measurable "Done Well" Definition**:
  1. Report strictly adheres to public-safety claim guidelines (only using *observed*, *directional*, *decision-support* language).
  2. Contains exact quantitative metrics (ROC-AUC, Average Precision, Precision@50) with verified lift over the baseline rule.
  3. Includes transparent reason codes and an explicit "Where This Fails / Operational Limitations" section.
