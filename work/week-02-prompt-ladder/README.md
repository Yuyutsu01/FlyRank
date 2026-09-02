# Week 2 — Prompt Ladder

**Track:** General AI Fluency  
**Phase:** Setup | Week 2  
**Assignment:** Prompt Ladder  
**Status:** **Completed**  

---

## 1. Objective

The objective of this assignment is to demonstrate that single, deliberate prompt modifications ("layers") systematically improve AI output quality, evaluating the effect of each layer on the actual output text rather than relying on intuition.

---

## 2. Selected Task & 6-Run Ladder Structure

- **Selected Task**: Research Paper Analysis (*Attention Is All You Need*, Vaswani et al., 2017)
- **Run Ladder Breakdown**:
  1. **Baseline**: Weak Prompt (`"Explain this research paper."`)
  2. **Version 1**: `+ Clearer Goal`
  3. **Version 2**: `+ Defined Audience`
  4. **Version 3**: `+ Specific Output Format`
  5. **Version 4**: `+ Quality Criteria` (Identified friction point: excessive verbosity disclaimer)
  6. **Version 5**: `+ Verification Requirements` (Final Reusable Prompt)

---

## 3. Assignment File Map

| Artifact | File Path | Description | Status |
|---|---|---|---|
| **Prompt Ladder Master** | [prompt_ladder.md](prompt_ladder.md) | Full 6-run ladder with prompt diffs, output excerpts, and output analysis | **Completed** |
| **Evidence Checklist** | [EVIDENCE_REQUIRED.md](EVIDENCE_REQUIRED.md) | Run tracking and evidence status | **Completed** |

---

## 4. Submission Checklist

- [x] Created exactly 6 runs (Baseline + 5 versions)
- [x] Each version adds exactly ONE named layer
- [x] Analyzed the OUTPUT changes (what improved in output text, not just prompt diffs)
- [x] Included at least one version demonstrating an honest failure/friction point (Version 4 excessive caution)
- [x] Formulated Final Reusable Prompt in `prompt_ladder.md`
- [x] Documented Key Learning summarizing the most impactful prompt layer
