# Week 4 — Empty but Live: Ship a Blank Page

**Track:** General AI Fluency  
**Phase:** Empty but Live | Week 4  
**Status:** **Completed & Configured for Deployment**  

---

## 1. Assignment Objective

The objective of this assignment is to ship a minimal, publicly accessible website foundation to verify deployment pipelines, hosting architecture, and mobile responsiveness before undertaking full portfolio content development.

---

## 2. Website Structure & Simplicity

The website is intentionally minimal and contains zero bloated frameworks, JavaScript dependencies, or external runtime libraries.

```text
portfolio/
├── index.html       # Clean semantic HTML5 container
└── style.css        # Responsive CSS utilizing established visual identity
```

### Rendered Page Content
```text
[• Portfolio Foundation — Live]
Shivam Sharma
AI / ML Research & Engineering
```

---

## 3. Visual Identity Reused

The page strictly implements the visual identity established in Week 3 ([`work/week-03-identity-kit/style-note.md`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/work/week-03-identity-kit/style-note.md)):
- **Heading Typography**: `Space Grotesk` (Google Fonts, 700 weight)
- **Body / Role Typography**: `Inter` (Google Fonts, 500 weight)
- **Background Color**: `#F8FAFC` (Off White)
- **Card Background**: `#FFFFFF` (White with subtle 1px border `#E2E8F0`)
- **Primary Text Color**: `#0F172A` (Deep Navy)
- **Accent Color**: `#2563EB` (Electric Blue)
- **Status Indicator**: `#10B981` (Live Emerald)
- **Mood**: Precise, technical, calm, and evidence-first.

---

## 4. Hosting & Deployment Method

- **Hosting Platform**: **GitHub Pages**
- **Deployment Pipeline**: GitHub Actions ([`.github/workflows/deploy-portfolio.yml`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/.github/workflows/deploy-portfolio.yml))
- **Target Public URL**: `https://yuyutsu01.github.io/FlyRank/`
- **Verification Status**:
  - Local responsive rendering verified.
  - Deployment configuration committed and pushed.
  - Manual step: Ensure GitHub Pages source is set to **GitHub Actions** in repository settings (`Settings -> Pages -> Source: GitHub Actions`).

---

## 5. Claude Project Standing Context

Detailed tracking of the three prerequisite assets is documented in [CLAUDE_PROJECT_CONTEXT.md](CLAUDE_PROJECT_CONTEXT.md):
1. **Identity Kit**: `work/week-03-identity-kit/style-note.md`
2. **Case Studies**: `work/week-02-frame-it-as-cases/portfolio_cases.md`
3. **Content Map**: `work/week-03-through-line/content_map.md`

> [!IMPORTANT]
> **Manual Action Required**: Upload/add these three markdown files into the project knowledge of your configured Claude Project ("AI/ML Portfolio Build") prior to starting full portfolio page implementation.

---

## 6. Submission & Quality Checklist

- [x] Real static HTML/CSS project created under `portfolio/`
- [x] Uses previously selected visual identity (Space Grotesk, Inter, #0F172A, #F8FAFC, #2563EB)
- [x] Minimal content: candidate name and AI/ML focus
- [x] Responsive layout verified for desktop and mobile viewport widths
- [x] Deployment workflow configured via GitHub Pages (`.github/workflows/deploy-portfolio.yml`)
- [x] Identity kit, case studies, and content map mapped in `CLAUDE_PROJECT_CONTEXT.md`
- [x] Claude Project upload clearly marked as a manual user action
- [x] Zero secrets, tokens, or fabricated URLs committed
- [x] Previous assignments untouched
