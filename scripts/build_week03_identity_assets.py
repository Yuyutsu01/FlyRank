import os

base_dir = "work/week-03-identity-kit"
os.makedirs(base_dir, exist_ok=True)

# 1. logo.svg
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <!-- Container Background -->
  <rect width="512" height="512" rx="96" fill="#0F172A"/>
  
  <!-- Subtle Outer Accent Ring -->
  <rect x="16" y="16" width="480" height="480" rx="80" fill="none" stroke="#2563EB" stroke-width="12" opacity="0.8"/>
  
  <!-- Monogram "SS" Geometry -->
  <g fill="none" stroke-width="38" stroke-linecap="round" stroke-linejoin="round">
    <!-- First 'S' (Electric Blue) -->
    <path d="M 215 165 C 215 130, 145 130, 145 165 C 145 210, 215 210, 215 255 C 215 295, 145 295, 145 260" stroke="#2563EB"/>
    <!-- Second 'S' (Off White) -->
    <path d="M 365 215 C 365 180, 295 180, 295 215 C 295 260, 365 260, 365 305 C 365 345, 295 345, 295 310" stroke="#F8FAFC"/>
  </g>
  
  <!-- Precision Accent Dot -->
  <circle cx="390" cy="385" r="18" fill="#2563EB"/>
</svg>
"""

with open(os.path.join(base_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. style-note.md
style_note_md = """# Portfolio Visual Identity Specification

**Candidate:** Shivam Sharma  
**Target Role:** AI / ML Research & Engineering Internships  
**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** Identity Kit  

---

## 1. Typography

- **Heading Font**: `Space Grotesk` (Google Fonts) — Technical, modern, geometric sans-serif for section headers and titles.
- **Body Font**: `Inter` (Google Fonts) — Highly legible, clean, neutral sans-serif for paragraphs and technical descriptions.
- **Code & Metrics**: `JetBrains Mono` / `Fira Code` — Monospace for code snippets, hyper-parameters, and evaluation metrics.

---

## 2. Color Palette

| Token Purpose | Color Name | HEX Code | Usage |
|---|---|---|---|
| **Main** | Deep Navy | `#0F172A` | Primary structural background & dark container cards |
| **Text** | Near Black | `#111827` | Primary high-contrast text color on light elements |
| **Background** | Off White | `#F8FAFC` | Light surface background & clean page foundation |
| **Accent** | Electric Blue | `#2563EB` | Interactive elements, CTA buttons, and focus highlights |

---

## 3. Mood

**Precise, technical, calm, and evidence-first.**

---

## 4. Two-Line Style Note

> Space Grotesk for headings and Inter for body text. Deep navy and off-white form the foundation, with electric blue used sparingly for interaction and emphasis.
> 
> Mood: precise, technical, calm, and evidence-first, keeping the visual system quiet so the work remains the loudest thing on the page.
"""

with open(os.path.join(base_dir, "style-note.md"), "w", encoding="utf-8") as f:
    f.write(style_note_md)

# 3. identity-kit.html
identity_kit_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shivam Sharma — Portfolio Visual Identity Kit</title>
  
  <!-- Google Fonts: Space Grotesk, Inter, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --font-heading: 'Space Grotesk', sans-serif;
      --font-body: 'Inter', sans-serif;
      --font-code: 'JetBrains Mono', monospace;

      --color-main: #0F172A;
      --color-text: #111827;
      --color-bg: #F8FAFC;
      --color-accent: #2563EB;
      --color-card-bg: #FFFFFF;
      --color-border: #E2E8F0;
      --color-muted: #64748B;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--color-bg);
      color: var(--color-text);
      line-height: 1.6;
      padding: 40px 20px;
    }

    .container {
      max-width: 960px;
      margin: 0 auto;
    }

    header {
      border-bottom: 2px solid var(--color-main);
      padding-bottom: 24px;
      margin-bottom: 40px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .header-title h1 {
      font-family: var(--font-heading);
      font-size: 28px;
      color: var(--color-main);
      letter-spacing: -0.5px;
    }

    .header-title p {
      font-size: 14px;
      color: var(--color-muted);
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .header-logo {
      width: 56px;
      height: 56px;
    }

    .section {
      background-color: var(--color-card-bg);
      border: 1px solid var(--color-border);
      border-radius: 8px;
      padding: 32px;
      margin-bottom: 32px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .section-title {
      font-family: var(--font-heading);
      font-size: 20px;
      color: var(--color-main);
      margin-bottom: 20px;
      border-bottom: 1px solid var(--color-border);
      padding-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .section-title span {
      display: inline-block;
      width: 8px;
      height: 20px;
      background-color: var(--color-accent);
      border-radius: 2px;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }

    /* Swatches */
    .swatch-card {
      border: 1px solid var(--color-border);
      border-radius: 6px;
      overflow: hidden;
      background-color: #fff;
    }

    .swatch-color {
      height: 90px;
      width: 100%;
    }

    .swatch-info {
      padding: 12px;
    }

    .swatch-name {
      font-weight: 600;
      font-size: 14px;
      color: var(--color-main);
    }

    .swatch-hex {
      font-family: var(--font-code);
      font-size: 13px;
      color: var(--color-muted);
    }

    /* Typography Samples */
    .type-sample {
      margin-bottom: 20px;
    }

    .type-label {
      font-size: 12px;
      text-transform: uppercase;
      color: var(--color-muted);
      font-family: var(--font-code);
      margin-bottom: 4px;
    }

    .sample-heading {
      font-family: var(--font-heading);
      font-size: 24px;
      font-weight: 700;
      color: var(--color-main);
    }

    .sample-body {
      font-family: var(--font-body);
      font-size: 15px;
      color: var(--color-text);
    }

    .sample-code {
      font-family: var(--font-code);
      font-size: 13.5px;
      background-color: var(--color-main);
      color: #E2E8F0;
      padding: 16px;
      border-radius: 6px;
      line-height: 1.5;
    }

    /* Style Note Blockquote */
    .style-note-box {
      background-color: var(--color-bg);
      border-left: 4px solid var(--color-accent);
      padding: 20px;
      border-radius: 0 6px 6px 0;
      font-size: 15px;
    }

    .style-note-box p {
      margin-bottom: 12px;
    }

    .style-note-box p:last-child {
      margin-bottom: 0;
      font-weight: 600;
      color: var(--color-main);
    }

    /* Component Samples */
    .btn-primary {
      display: inline-block;
      background-color: var(--color-accent);
      color: #ffffff;
      font-family: var(--font-heading);
      font-weight: 700;
      font-size: 14px;
      padding: 12px 24px;
      border-radius: 6px;
      text-decoration: none;
      border: none;
      cursor: pointer;
    }

    .btn-primary:hover {
      background-color: #1D4ED8;
    }

    .component-card {
      border: 1px solid var(--color-border);
      border-radius: 6px;
      padding: 20px;
      background-color: #fff;
    }

    .component-card h4 {
      font-family: var(--font-heading);
      color: var(--color-main);
      margin-bottom: 8px;
    }

    footer {
      text-align: center;
      font-size: 13px;
      color: var(--color-muted);
      margin-top: 40px;
      border-top: 1px solid var(--color-border);
      padding-top: 20px;
    }
  </style>
</head>
<body>

  <div class="container">
    
    <!-- Header -->
    <header>
      <div class="header-title">
        <h1>SHIVAM SHARMA</h1>
        <p>AI / ML Research & Engineering — Visual Identity Kit</p>
      </div>
      <div class="header-logo">
        <img src="logo.svg" alt="SS Monogram Logo" width="56" height="56">
      </div>
    </header>

    <!-- 1. Style Note -->
    <div class="section">
      <div class="section-title"><span></span> Two-Line Style Note</div>
      <div class="style-note-box">
        <p>"Space Grotesk for headings and Inter for body text. Deep navy and off-white form the foundation, with electric blue used sparingly for interaction and emphasis."</p>
        <p>"Mood: precise, technical, calm, and evidence-first, keeping the visual system quiet so the work remains the loudest thing on the page."</p>
      </div>
    </div>

    <!-- 2. Color Palette -->
    <div class="section">
      <div class="section-title"><span></span> Color Palette</div>
      <div class="grid-4">
        
        <div class="swatch-card">
          <div class="swatch-color" style="background-color: #0F172A;"></div>
          <div class="swatch-info">
            <div class="swatch-name">Main (Deep Navy)</div>
            <div class="swatch-hex">#0F172A</div>
          </div>
        </div>

        <div class="swatch-card">
          <div class="swatch-color" style="background-color: #111827;"></div>
          <div class="swatch-info">
            <div class="swatch-name">Text (Near Black)</div>
            <div class="swatch-hex">#111827</div>
          </div>
        </div>

        <div class="swatch-card">
          <div class="swatch-color" style="background-color: #F8FAFC; border-bottom: 1px solid #E2E8F0;"></div>
          <div class="swatch-info">
            <div class="swatch-name">Background (Off White)</div>
            <div class="swatch-hex">#F8FAFC</div>
          </div>
        </div>

        <div class="swatch-card">
          <div class="swatch-color" style="background-color: #2563EB;"></div>
          <div class="swatch-info">
            <div class="swatch-name">Accent (Electric Blue)</div>
            <div class="swatch-hex">#2563EB</div>
          </div>
        </div>

      </div>
    </div>

    <!-- 3. Typography -->
    <div class="section">
      <div class="section-title"><span></span> Typography System</div>
      
      <div class="type-sample">
        <div class="type-label">Heading Font — Space Grotesk</div>
        <div class="sample-heading">I build and research AI/ML systems that solve real-world problems.</div>
      </div>

      <div class="type-sample">
        <div class="type-label">Body Font — Inter</div>
        <div class="sample-body">
          This portfolio is designed for AI/ML research leads and engineering managers evaluating candidates for research or engineering internships. It prioritizes empirical evidence, code quality, and experimental benchmarks over generic claims.
        </div>
      </div>

      <div class="type-sample">
        <div class="type-label">Monospace Code & Metrics — JetBrains Mono</div>
        <div class="sample-code">
# Empirical Random Forest Evaluation on Client-Holdout Test Split
Precision@50 = 0.740  # ~3.08x lift over hand-written baseline rule (0.240)
Validation Strategy: GroupShuffleSplit(groups=client_id, test_size=0.25)
        </div>
      </div>
    </div>

    <!-- 4. Monogram Logo & UI Treatment -->
    <div class="section">
      <div class="section-title"><span></span> Monogram Logo & Component Treatment</div>
      
      <div class="grid-2">
        <div class="component-card" style="text-align: center;">
          <img src="logo.svg" alt="Monogram Logo" width="96" height="96" style="margin-bottom: 12px;">
          <h4>Geometric Monogram ("SS")</h4>
          <p style="font-size: 13px; color: var(--color-muted);">Suitable for header logo, favicon, and small-scale site identity.</p>
        </div>

        <div class="component-card">
          <h4>Primary CTA & Button Treatment</h4>
          <p style="font-size: 13.5px; color: var(--color-text); margin-bottom: 16px;">
            Single-focus interaction button designed to drive visitors to case studies.
          </p>
          <a href="#" class="btn-primary">Explore My Work</a>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer>
      Shivam Sharma — FlyRank Internship Repository — Week 3 Visual Identity Kit
    </footer>

  </div>

</body>
</html>
"""

with open(os.path.join(base_dir, "identity-kit.html"), "w", encoding="utf-8") as f:
    f.write(identity_kit_html)

# 4. README.md
readme_md = """# Week 3 — Visual Identity & Identity Kit

**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** Consistency, Not Talent / Identity Kit  
**Status:** **Completed**  

---

## 1. Objective

The objective of this assignment is to establish a restrained, technical visual identity (1–2 fonts, 4 colors, simple monogram logo, and two-line style note) that frames project evidence without upstaging the work.

---

## 2. Portfolio Positioning Alignment

- **Primary Claim:** *"I build and research AI/ML systems that solve real-world problems."*
- **Target Audience:** AI/ML research leads and engineering managers evaluating candidates for research or engineering internships.
- **Primary Action:** *"Explore my work."*
- **Design Philosophy:** Minimal, technical, calm, and evidence-first. The visual system stays quiet so code, architectures, and benchmark metrics remain the loudest elements on the page.

---

## 3. Visual Identity Specifications

### Typography
- **Heading**: `Space Grotesk` (Modern, geometric sans-serif for section headers and titles)
- **Body**: `Inter` (Neutral, highly legible sans-serif for reading text)
- **Code & Metrics**: `JetBrains Mono` (Monospace for terminal output, hyperparameters, and code)

### Color Palette
- **Main (Deep Navy)**: `#0F172A`
- **Text (Near Black)**: `#111827`
- **Background (Off White)**: `#F8FAFC`
- **Accent (Electric Blue)**: `#2563EB`

### Logo Monogram
- Clean, geometric `"SS"` monogram (`logo.svg`) designed for header identity and favicon scale.

### Two-Line Style Note
> Space Grotesk for headings and Inter for body text. Deep navy and off-white form the foundation, with electric blue used sparingly for interaction and emphasis.
> 
> Mood: precise, technical, calm, and evidence-first, keeping the visual system quiet so the work remains the loudest thing on the page.

---

## 4. Assignment File Map

| Artifact | File Path | Description | Status |
|---|---|---|---|
| **Identity Kit HTML Page** | [identity-kit.html](identity-kit.html) | Polished single-page visual identity kit presentation | **Completed** |
| **Style Note Specification** | [style-note.md](style-note.md) | Typography, palette table, mood, & two-line style note | **Completed** |
| **Monogram Logo SVG** | [logo.svg](logo.svg) | Clean geometric "SS" monogram for header/favicon | **Completed** |
| **Master Documentation** | [README.md](README.md) | Assignment summary and submission checklist | **Completed** |

---

## 5. Manual Action Required

> **Claude Project Configuration Note:**  
> Copy the two-line style note below and paste it into your configured Claude Project ("AI/ML Portfolio Build") as a standing instruction:
> 
> *"Space Grotesk for headings and Inter for body text. Deep navy and off-white form the foundation, with electric blue used sparingly for interaction and emphasis. Mood: precise, technical, calm, and evidence-first, keeping the visual system quiet so the work remains the loudest thing on the page."*

---

## 6. How to Preview

To preview the visual identity kit:
1. Open [identity-kit.html](identity-kit.html) directly in any web browser.

---

## 7. Submission Checklist

- [x] Used exactly 2 fonts (`Space Grotesk` for headings, `Inter` for body)
- [x] Defined restrained 4-color palette with HEX codes (`#0F172A`, `#111827`, `#F8FAFC`, `#2563EB`)
- [x] Created clean geometric "SS" monogram logo SVG (`logo.svg`)
- [x] Authored exact two-line style note in `style-note.md`
- [x] Created single-page HTML identity kit (`identity-kit.html`)
- [x] Documented standing instruction requirement for Claude Project
"""

with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Successfully generated all assets in work/week-03-identity-kit/")
