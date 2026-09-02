# Visual Identity Specification: Technical Portfolio

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
