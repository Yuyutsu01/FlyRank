# Claude Pressure-Test Output

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
