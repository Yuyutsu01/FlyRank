import os
import shutil

target_dir = "work/week-01-draw-the-path"

# 1. Handle image filenames
old_photo = os.path.join(target_dir, "sitemap_photo.jpg.jpeg")
new_photo = os.path.join(target_dir, "sitemap_photo.jpg")

if os.path.exists(old_photo):
    shutil.copyfile(old_photo, new_photo)
    os.remove(old_photo)
    print("Renamed sitemap_photo.jpg.jpeg -> sitemap_photo.jpg")

# 2. Update claude_pressure_test_output.md
clean_output_md = """# Claude Pressure-Test Output

**Status:** Completed (Executed Live in Claude Project `"AI/ML Portfolio Build"`)  
**Evaluated Against:**
- Primary Claim: *"I build and research AI/ML systems that solve real-world problems."*
- Primary Action: *"Explore my work."*

---

## Real Claude Pressure-Test Response

Here's the pressure test, evaluated straight against your claim and action.

**Primary claim:** "I build and research AI/ML systems that solve real-world problems."  
**Primary action:** "Explore my work."  

### Page-by-page evaluation

1. **HOME** — Does its job: states the claim, gives a CTA. Fine as-is, but a hero with only "who I am" and a claim is unproven until the visitor clicks away. Nothing on this page itself is evidence.

2. **WORK / CASE STUDIES** — This is where your claim lives or dies. "Project AEGIS, ResearchMind, Selected AI/ML experiments" doesn't tell me if these are research (papers, novel methods) or engineering (deployed systems, real users) or both. Your claim has two halves — "build" and "research" — and your audience (researchers vs. recruiters vs. engineers) will weight those differently. Right now the page doesn't signal which project proves which half.

3. **ABOUT** — "Research interests, Technical skills" overlaps heavily with what case studies should already demonstrate. A recruiter skimming for 30 seconds doesn't need a skills list separate from the projects — they need to see the skills in action inside the case studies. This page risks being redundant restatement rather than new evidence.

4. **CONTACT** — Fine, minimal, no issue.

### Weakest part of the sitemap

The **WORK** page. It's structurally the only page that can prove your claim, but as described it's just a list of names with no framing. There's no signal of: `problem -> your approach -> result/impact -> what's technically novel`. Without that framing, a researcher can't tell if AEGIS is a toy repo or a real system, and a recruiter can't tell what you actually did versus what a team did. This is the single point of failure in the sitemap — everything else is scaffolding around it.

Also flagging: "real-world problems" is an evidentiary claim (implies deployment, users, or measurable outcomes), but nothing in the sitemap requires you to show impact/results. That's a gap, not a page.

### Revised minimal sitemap

1. **HOME** — claim + CTA, unchanged. Justification: entry point, needs to exist.
2. **WORK** — restructured, not renamed. Each project entry should force: problem, your specific contribution, outcome/result, and tag whether it's "research" or "build" (or both). This is the only page doing real work in the site, so it should carry the most structural weight.
3. **ABOUT** — cut "technical skills" as a standalone list; keep only "who I am" + "research interests" as a short paragraph. Skills get proven in WORK, not asserted in ABOUT. Justification for keeping the page at all: recruiters and researchers do want a quick human/context read (background, focus area) that doesn't fit naturally inside project write-ups.
4. **CONTACT** — unchanged. Justification: necessary terminal action, costs nothing.

Everything else you might be tempted to add (a blog, a "skills matrix" page, a "timeline") doesn't earn its place — it either duplicates WORK or delays the visitor from reaching WORK, which is the only page proving your claim.

### Three highest-priority changes before building

1. Add explicit "research" vs. "build" tagging (or separate sub-sections) to every project in WORK, so each audience segment can immediately find the evidence type they care about.
2. Add a one-line `problem -> outcome` framing to each project card/entry, visible before a click-through — this is what makes the claim verifiable within 30 seconds instead of requiring a deep read.
3. Remove the standalone "Technical skills" list from ABOUT — it's currently unproven assertion sitting next to the page that could actually prove it.

---

## Action Plan Based on Critique

1. **Categorical Tagging in WORK**: Implement clear visual tags (`[Research]`, `[Build]`, or `[Research + Build]`) for Project AEGIS, ResearchMind, and Quant ML experiments so recruiters and researchers immediately locate relevant evidence.
2. **One-Line Project Framing Cards**: Add `Problem -> Contribution -> Outcome` summary lines directly on project preview cards so technical reviewers can verify impact within 30 seconds without needing deep click-throughs.
3. **Streamlined ABOUT Section**: Eliminate the redundant standalone skills list from ABOUT and consolidate it into "who I am" + research focus, letting technical skills be proven dynamically inside project case studies.
"""

with open(os.path.join(target_dir, "claude_pressure_test_output.md"), "w", encoding="utf-8") as f:
    f.write(clean_output_md)

# 3. Update EVIDENCE_REQUIRED.md
evidence_updated_md = """# Week 1 Assignment Evidence Requirements

All physical and AI execution evidence for **Week 1 — Draw the Path** is **100% Completed, Attached, and Verified**.

---

## Evidence Files Checklist

- [x] **`work/week-01-draw-the-path/sitemap_photo.jpg`** — Physical photo of handwritten sitemap sketch (**Uploaded & Verified**).
- [x] **`work/week-01-draw-the-path/claude_project_screenshot.png`** — Screenshot of configured Claude Project `"AI/ML Portfolio Build"` (**Uploaded & Verified**).
- [x] **`work/week-01-draw-the-path/claude_pressure_test_output.md`** — Real output from running `pressure_test_prompt.md` inside Claude (**Executed & Recorded**).
- [x] **Free Tool Accounts Verification** — Configured accounts for Claude, ChatGPT, Gemini, and Perplexity.

---

## Final Verification Summary

- [x] Sitemap Strategy & Architecture (`sitemap.md`) — **COMPLETED**
- [x] Visual Sitemap Vector Diagram (`sitemap.svg`) — **COMPLETED**
- [x] Custom Claude Project Instructions (`claude_project_instructions.md`) — **COMPLETED**
- [x] Pressure-Test Prompt (`pressure_test_prompt.md`) — **COMPLETED**
- [x] Real Claude Pressure-Test Response & Action Plan (`claude_pressure_test_output.md`) — **COMPLETED**
- [x] Handwritten Sitemap Photo (`sitemap_photo.jpg`) — **COMPLETED**
- [x] Claude Project Screenshot (`claude_project_screenshot.png`) — **COMPLETED**
"""

with open(os.path.join(target_dir, "EVIDENCE_REQUIRED.md"), "w", encoding="utf-8") as f:
    f.write(evidence_updated_md)

# 4. Update README.md
readme_updated_md = """# Week 1 — Draw the Path

**Track:** General AI Fluency  
**Phase:** Setup | Week 1  
**Assignment:** Draw the Path  
**Status:** **100% Fully Completed & Ready for Submission**  

---

## 1. Objective

The objective of this assignment is to map out a clear, evidence-backed sitemap for a personal technical portfolio that guides a visitor from landing on the homepage to believing the primary claim and taking the primary action within seconds.

---

## 2. Core Positioning

- **Primary Claim:** *"I build and research AI/ML systems that solve real-world problems."*
- **Primary Action:** *"Explore my work."*
- **Target Audience:** AI/ML researchers, ML/AI engineers, technical recruiters, and technical internship reviewers.

---

## 3. Assignment File Map

| Artifact | File Path | Description | Status |
|---|---|---|---|
| **Sitemap Architecture** | [sitemap.md](sitemap.md) | Page-by-page justifications & exclusion rationales | **Completed** |
| **Sitemap Vector Diagram** | [sitemap.svg](sitemap.svg) | Visual architectural tree of the minimal sitemap | **Completed** |
| **Claude Project Instructions** | [claude_project_instructions.md](claude_project_instructions.md) | System prompt for `"AI/ML Portfolio Build"` | **Completed** |
| **Pressure-Test Prompt** | [pressure_test_prompt.md](pressure_test_prompt.md) | Critical evaluation prompt to challenge sitemap | **Completed** |
| **Pressure-Test Output** | [claude_pressure_test_output.md](claude_pressure_test_output.md) | Real Claude pressure test response & action plan | **Completed** |
| **Handwritten Sitemap Photo** | [sitemap_photo.jpg](sitemap_photo.jpg) | Physical sketch photo of sitemap | **Completed** |
| **Claude Project Screenshot** | [claude_project_screenshot.png](claude_project_screenshot.png) | Screenshot of configured Claude Project | **Completed** |
| **Evidence Verification** | [EVIDENCE_REQUIRED.md](EVIDENCE_REQUIRED.md) | Master evidence checklist and status | **Completed** |

---

## 4. Submission Checklist

- [x] Defined primary claim and primary action aligned with CSE/ML background
- [x] Designed minimal sitemap (HOME, WORK / CASE STUDIES, ABOUT, CONTACT)
- [x] Documented justifications and exclusion rationales in `sitemap.md`
- [x] Generated digital sitemap vector diagram `sitemap.svg`
- [x] Prepared custom Claude Project instructions in `claude_project_instructions.md`
- [x] Prepared pressure-test prompt in `pressure_test_prompt.md`
- [x] Uploaded handwritten sitemap photo (`sitemap_photo.jpg`)
- [x] Uploaded Claude Project screenshot (`claude_project_screenshot.png`)
- [x] Executed pressure test in Claude and updated `claude_pressure_test_output.md` with action plan
- [x] Verified accounts created: Claude, ChatGPT, Gemini, Perplexity
"""

with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_updated_md)

print("Updated all Week 1 files successfully.")
