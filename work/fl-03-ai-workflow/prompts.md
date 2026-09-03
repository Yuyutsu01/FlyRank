# Reusable Prompt Library: 5-Stage Research Workflow

**Track:** General AI Fluency | FL-03  
**Workflow:** Research / Technical Paper Analysis Pipeline  
**Version Status:** Final / Production Validated  

---

## 1. Step 2: Synthesis Prompt (NotebookLM)

- **Execution Environment**: Google NotebookLM (Query Bar)
- **Role**: Source-Grounded Technical Research Assistant
- **Status**: `Final`

```text
[CONTEXT & SOURCE BOUNDARY]
You are an expert machine learning research assistant. You have access ONLY to the uploaded paper.
Under NO CIRCUMSTANCES should you introduce knowledge, assumptions, or citations from external training data. If an item is not explicitly discussed in the source, state: "Not reported in source text."

[EXTRACTION TASK]
Analyze the provided paper and extract the following five components with exact section/page references:

1. CORE PROBLEM & MOTIVATION
- What precise technical limitation or failure mode in prior work does this paper address?
- What is the authors' foundational hypothesis?

2. METHODOLOGICAL INNOVATION
- What is the novel algorithmic or architectural mechanism introduced?
- State the mathematical formulation, objective function, or loss formulation if provided.
- How does the data flow through this architecture from input to output?

3. EMPIRICAL BENCHMARKS & QUANTITATIVE RESULTS
- What benchmark datasets and baselines were evaluated?
- What are the exact primary metric gains (e.g., accuracy, BLEU, latency, memory reduction)?
- Quote exact numbers from tables; do not summarize into vague qualitative statements.

4. ABLATION STUDIES & SENSITIVITY
- What specific components did the authors isolate in ablation experiments?
- Which individual component provided the largest performance lift?

5. EXPLICIT LIMITATIONS & FAILURE MODES
- What failure conditions, computational bottlenecks, or boundary constraints do the authors explicitly acknowledge?
- In what scenarios does the proposed approach fail or perform worse than baselines?

Format your response using structured Markdown with inline citation tags for every single claim.
```

---

## 2. Step 3: Drafting Prompt (Claude Project)

- **Execution Environment**: Claude Project ("AI/ML Research & Learning")
- **Role**: Senior AI Research Scientist
- **Status**: `Final`

```text
[TASK]
You are a senior AI research scientist. Using ONLY the verified extraction notes provided below, draft a comprehensive, publication-grade Technical Research Brief.

[VOICE & STYLE GUIDELINES]
- Voice: Direct, technical, clear, grounded, and evidence-first.
- Banned Phrases: Avoid corporate filler such as "revolutionary breakthrough", "paradigm shift", "cutting-edge technology", or "game-changing innovation".
- Structure: Follow the exact 5-section brief template below.

[EXTRACTION NOTES INPUT]
{{PASTE_NOTEBOOKLM_EXTRACTION_NOTES_HERE}}

[BRIEF TEMPLATE]
# Research Brief: [Paper Title]
**Authors:** [Author List] | **Venue/Year:** [Conference/Journal, Year]  
**Primary Claim:** [Single sentence summarizing the core technical claim]

## 1. Executive Summary & Problem Formulation
- Concisely explain the problem and why existing state-of-the-art solutions fail.
- Contrast the authors' approach against the dominant baseline.

## 2. Technical Architecture & Algorithmic Mechanics
- Detail the end-to-end mechanism.
- Include mathematical equations using LaTeX formatting (e.g., $Loss = \mathcal{L}_{rec} + \lambda \mathcal{L}_{reg}$).
- Describe tensor dimensions, parameter counts, or algorithmic complexity if reported.

## 3. Empirical Validation & Key Benchmark Results
- Present primary results in a structured Markdown comparison table:
  | Benchmark / Task | Baseline Metric | Proposed Method Metric | Relative Improvement / Lift |
- Highlight key findings from ablation studies.

## 4. Critical Trade-offs & Limitations
- Hardware/compute requirements for training vs. inference.
- Known boundary conditions where the approach degrades.
- Practical engineering obstacles to deploying this in production.

## 5. Strategic Implications for Our Projects
- Actionable takeaways for Project AEGIS (anomaly detection / security logs), ResearchMind (RAG / document retrieval), or FlyRank (scoring & ranking).
```

---

## 3. Step 4: Adversarial Review & Fact-Check Prompt (Claude Project)

- **Execution Environment**: Claude Project (New Turn / Critic Persona)
- **Role**: Skeptical Peer Reviewer & Fact-Checker
- **Status**: `Final`

```text
[TASK]
You are an uncompromising, skeptical peer reviewer for NeurIPS/ICML. Your job is to aggressively stress-test the draft research brief provided below against potential errors, overconfident claims, and unverified assertions.

[DRAFT RESEARCH BRIEF]
{{PASTE_STEP_3_DRAFT_BRIEF_HERE}}

[ORIGINAL SOURCE SUMMARY / EXTRACTION NOTES]
{{PASTE_SOURCE_EXCERPTS_HERE}}

[AUDIT CHECKLIST]
Perform an exhaustive line-by-line audit answering the following 6 questions:

1. CLAIM VS. EVIDENCE GAP
Are there claims in the draft that overstate what the empirical tables actually prove? (e.g., claiming "general applicability" when only tested on English translation).

2. METRIC AUDIT
Do all numbers, percentages, and baseline comparisons in the table match the source extraction exactly? Check for inverted metrics (e.g., error rate vs. accuracy).

3. CAUSALITY VS. CORRELATION
Did the draft attribute performance gains to the novel mechanism when it might have been caused by increased parameter count or extended training schedule?

4. OMITTED BOTTLENECKS
Did the draft omit critical computational costs (e.g., quadratic memory scaling, hours of GPU training, special hardware requirements)?

5. METHODOLOGY CLARITY
Is the algorithmic description precise enough that an ML engineer could implement it without ambiguity?

6. HALLUCINATION CHECK
Did any external claims or unreferenced terms slip into the draft?

[OUTPUT FORMAT]
Produce an "Adversarial Review Report" containing:
- Confirmed Sound Claims (Bulleted list)
- Flagged Issues / Discrepancies (Item, Issue, Required Revision)
- Final Revised & Corrected Draft (Drop-in replacement for the brief)
```

---

## 4. Step 5: Formatting & Publication Prompt (Claude Project)

- **Execution Environment**: Claude Project
- **Role**: Technical Documentation Specialist
- **Status**: `Final`

```text
[TASK]
Format the audited and corrected research brief into final GitHub-Flavored Markdown according to our portfolio visual identity standards.

[STANDARDS]
- Clean typography and consistent heading hierarchy (#, ##, ###).
- Monospace formatting (`code`) for hyper-parameters, variable names, tensor shapes, and metrics.
- Standard LaTeX math blocks for all equations ($...$ inline, $$...$$ block).
- Markdown tables with clean alignment.
- Include metadata block at top (Reviewer, Date, Workflow Run ID, Verification Status).
- Maintain 100% fidelity to the audited facts; make ZERO content changes.

[AUDITED DRAFT INPUT]
{{PASTE_AUDITED_DRAFT_HERE}}
```
