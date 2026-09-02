import os

base_dir = "work/week-03-visual-identity"
os.makedirs(base_dir, exist_ok=True)

# 1. visual_identity.md
visual_identity_md = """# Visual Identity Specification: Technical Portfolio

**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** Consistency, Not Talent (and Frame, Not Upstage)  
**Status:** Completed  

---

## 1. Design Philosophy & Direction

> **Core Principle:** *"The design frames the work; it never upstages it."*

For an AI/ML research and engineering portfolio targeting technical decision-makers (AI/ML Research Leads and Engineering Managers), decorative "AI startup" aesthetics (glowing 3D neural networks, neon robots, colorful gradient explosions) degrade credibility. 

Our visual identity is **Minimal, Technical, Evidence-First, Quiet, and High-Contrast**. Visual elements exist strictly to render system architectures, empirical loss distributions, code snippets, and benchmark metrics scannable within 30 seconds.

---

## 2. Token Specifications

### Typography System
- **Body & Headlines**: `Inter` / `System UI` sans-serif (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`).
  - *Rationale*: Clean, highly legible at small sizes, zero distraction.
- **Code, Metrics & Data Tables**: `JetBrains Mono` / `Fira Code` monospace (`"JetBrains Mono", "Fira Code", monospace`).
  - *Rationale*: Signals technical precision when displaying formulas, hyperparameters, metrics, and terminal outputs.

### Color Palette (Restrained Dark Palette)
- **Base Background (`#11111b`)**: Dark slate/charcoal background for eye comfort during deep technical reviews.
- **Container Card (`#181825`)**: Slightly lighter dark surface with a subtle 1px border (`#313244`).
- **Body Text (`#cdd6f4`)**: Off-white text to maximize contrast without harsh pure-white glare.
- **Primary Technical Accent (`#89b4fa`)**: Muted blue for structural headers, primary CTA buttons, and pipeline nodes.
- **Success Metric Accent (`#a6e3a1`)**: Muted mint green for high-precision metrics, passing unit tests, and verified benchmarks.
- **Risk / Anomaly Accent (`#f38ba8`)**: Subdued red/coral for loss thresholds, anomaly markers, and failure modes.

### Spacing & Layout Rules
- **8px Grid System**: All margins, padding, and gaps follow multiples of 8px (`8px`, `16px`, `24px`, `32px`, `48px`).
- **Container Width**: Max content width capped at `960px` to maintain optimal line lengths (65–75 characters per line).

### Component Treatments
- **Buttons**:
  - *Primary CTA*: Solid background (`#89b4fa`), dark bold text (`#11111b`), 6px border-radius, `[Explore My Work]`.
  - *Secondary Links*: Text link with subtle underline hover (`#89b4fa`).
- **Cards & Images**:
  - All project diagrams and data visual plots use a standardized **16:9 Aspect Ratio** (`1000px x 562.5px`).
  - Enclosed in a 1px border (`#313244`) with 6px rounded corners.
  - Zero drop shadows or glowing neon effects.

---

## 3. Hierarchy Rule

```text
YOUR WORK (Code & Architecture)
  ↓
EVIDENCE (Metrics & Loss Plots)
  ↓
EXPLANATION (Technical Problem & Decisions)
  ↓
DECORATION (Subtle framing elements only)
```
"""

with open(os.path.join(base_dir, "visual_identity.md"), "w", encoding="utf-8") as f:
    f.write(visual_identity_md)

# 2. rejected_images.md
rejected_images_md = """# Image Judgment & Rejection Evaluation Log

**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** Consistency, Not Talent (and Frame, Not Upstage)  

---

## Evaluation Framework (6 Criteria)

1. **Relevance**: Does this help communicate AI/ML work?
2. **Consistency**: Does it fit the visual identity?
3. **Credibility**: Does it look appropriate for a technical portfolio?
4. **Focus**: Does it support the project rather than distract from it?
5. **Originality**: Does it feel specific rather than generic AI art?
6. **Evidence**: Would a real screenshot/architectural plot of my work be better?

---

## Selected Images (Accepted for Portfolio)

### 1. `selected_images/hero_architecture.png`
- **Description**: Clean 16:9 technical pipeline diagram showing streaming data ingestion → feature extraction → ML model engine → Precision@50 review queue.
- **Evaluation**:
  - *Relevance*: 10/10 — Directly visualizes the end-to-end technical system architecture.
  - *Credibility*: 10/10 — Uses monospace font, clean dark card containers, and explicit step labels.
  - *Evidence Value*: High — Explains system workflow within 5 seconds of landing.

### 2. `selected_images/project_aegis_diagram.png`
- **Description**: Empirical reconstruction loss distribution plot ($MSE > \\tau$) comparing benign log events vs. synthetic anomaly injections.
- **Evaluation**:
  - *Relevance*: 10/10 — Proves how the PyTorch Autoencoder detects threats without false alarms.
  - *Credibility*: 10/10 — Generated from actual benchmark evaluation data.
  - *Evidence Value*: Critical — Demonstrates empirical rigor over unsupported claims.

---

## Rejected Images (Explicit Rejection Rationale)

### Rejection Candidate 1: Glowing 3D Neural Network Over Laptop
- **Prompt Attempt**: *"Futuristic glowing 3D hologram of neural network nodes floating above a sleek laptop keyboard in a dark room, cyber aesthetic, 8k render."*
- **Rejection Rationale**:
  - *Relevance*: 2/10 — Purely decorative; communicates zero information about model architecture or data grain.
  - *Credibility*: 1/10 — Looks like stock promotional art for a low-quality crypto/AI landing page.
  - *Verdict*: **REJECTED**. Replaced by `hero_architecture.png` system diagram.

### Rejection Candidate 2: Generic Neon AI Robot Face
- **Prompt Attempt**: *"Cyberpunk robot face made of glowing circuit lines and binary numbers, hyperrealistic render."*
- **Rejection Rationale**:
  - *Relevance*: 0/10 — Totally disconnected from machine learning engineering, quantitative evaluation, or security audit logs.
  - *Credibility*: 0/10 — Destroys technical credibility for engineering managers and research leads.
  - *Verdict*: **REJECTED**.

### Rejection Candidate 3: Abstract Colorful Gradient Explosion
- **Prompt Attempt**: *"Abstract fluid gradient art with vibrant purple, magenta, and cyan waves, modern web background."*
- **Rejection Rationale**:
  - *Consistency*: 3/10 — Violates the quiet, restrained dark color palette (`#11111b` / `#181825`).
  - *Focus*: 2/10 — Competes with text and metrics for visual attention.
  - *Verdict*: **REJECTED**. Replaced by high-contrast monospace code & benchmark tables.
"""

with open(os.path.join(base_dir, "rejected_images.md"), "w", encoding="utf-8") as f:
    f.write(rejected_images_md)

# 3. README.md
readme_md = """# Week 3 — Visual Identity & Image Judgment

**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** Consistency, Not Talent (and Frame, Not Upstage)  
**Status:** **Completed**  

---

## 1. Objective

The objective of this assignment is to define a restrained, technical visual identity and demonstrate deliberate image judgment—selecting only visuals that frame evidence and rejecting generic decorative AI art.

---

## 2. Core Visual Hierarchy

```text
YOUR WORK (Code & Architecture)
  ↓
EVIDENCE (Metrics & Loss Plots)
  ↓
EXPLANATION (Technical Problem & Decisions)
  ↓
DECORATION (Subtle framing elements only)
```

---

## 3. Assignment File Map

| Artifact | File Path | Description | Status |
|---|---|---|---|
| **Visual Identity Specification** | [visual_identity.md](visual_identity.md) | Typography, color palette, spacing, & component specs | **Completed** |
| **Image Judgment Log** | [rejected_images.md](rejected_images.md) | 6-criterion evaluation log for selected & rejected visuals | **Completed** |
| **Hero System Architecture Diagram** | [selected_images/hero_architecture.png](selected_images/hero_architecture.png) | 16:9 technical pipeline diagram | **Completed** |
| **Project AEGIS Loss Plot** | [selected_images/project_aegis_diagram.png](selected_images/project_aegis_diagram.png) | Empirical reconstruction loss plot ($MSE > \\tau$) | **Completed** |

---

## 4. Submission Checklist

- [x] Defined simple, intentional visual identity in `visual_identity.md`
- [x] Selected typography (Inter / System UI + JetBrains Mono)
- [x] Defined restrained dark color palette (`#11111b` base, `#89b4fa` primary accent, `#a6e3a1` success accent)
- [x] Standardized 16:9 aspect ratio and component rules
- [x] Generated & selected 2 high-value technical visuals in `selected_images/`
- [x] Evaluated candidate images using the 6-criterion framework in `rejected_images.md`
- [x] Documented explicit rejection rationales for 3 decorative/generic AI images
- [x] Verified visual hierarchy: Work & Evidence lead, decoration frames
"""

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Successfully generated all Markdown files in work/week-03-visual-identity/")
