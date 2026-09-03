# Deployment Notes: Empty but Live Portfolio

**Candidate:** Shivam Sharma  
**Track:** General AI Fluency  
**Phase:** Empty but Live | Week 4  
**Date:** September 2026  

---

## 1. Hosting Architecture & Platform Selection

- **Selected Hosting Platform**: **GitHub Pages** (via GitHub Actions)
- **Rationale**: 
  - Native integration with the existing `https://github.com/Yuyutsu01/FlyRank` public repository.
  - Zero third-party vendor lock-in; does not require external SaaS accounts or API credentials.
  - Completely isolated deployment targeting `./portfolio` directory while leaving data and pipeline directories protected.
- **Workflow File**: [`.github/workflows/deploy-portfolio.yml`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/.github/workflows/deploy-portfolio.yml)

---

## 2. Deployment Status & Target Public URL

- **Configured Public URL**: `https://yuyutsu01.github.io/FlyRank/`
- **Deployment Status**: Configured via GitHub Actions workflow `.github/workflows/deploy-portfolio.yml` and pushed to `main`.
- **Live Verification Status**:
  - The repository workflow is committed and pushed.
  - **Manual GitHub Configuration Required**: To complete public serving, navigate to repository settings:
    1. Go to `https://github.com/Yuyutsu01/FlyRank/settings/pages`
    2. Under **Build and deployment** > **Source**, select: **GitHub Actions**
    3. The `Deploy Portfolio to GitHub Pages` action will run automatically and serve `https://yuyutsu01.github.io/FlyRank/`.

---

## 3. Local Verification & Mobile Responsiveness Check

- **Local Preview**: Verified via standard browser rendering.
- **Mobile Responsive Audit**:
  - Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
  - Breakpoint: `@media (max-width: 480px)` scales padding to `36px 24px`, heading to `26px`, and role font to `15px`.
  - Layout: Centered flexible box (`display: flex; align-items: center; justify-content: center; min-height: 100vh`).
  - Render test: Passes horizontal scrolling check (0 horizontal overflow) and touch target spacing on mobile screen dimensions (375px - 414px width).

---

## 4. Manual Verification Checklist for User

1. [ ] Push latest commits to GitHub `main` branch.
2. [ ] Open `https://github.com/Yuyutsu01/FlyRank/settings/pages` and ensure **Source** is set to **GitHub Actions**.
3. [ ] Wait for GitHub Actions build to complete (approx. 45–60 seconds).
4. [ ] Open `https://yuyutsu01.github.io/FlyRank/` in desktop browser and verify the live page.
5. [ ] Open `https://yuyutsu01.github.io/FlyRank/` on mobile phone/second device to verify mobile responsiveness as required by the assignment.
