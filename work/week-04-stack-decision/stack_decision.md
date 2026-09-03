# Portfolio Stack Decision

**Candidate:** Shivam Sharma  
**Track:** General AI Fluency  
**Phase:** Stack Decision | Week 4  
**Date:** September 2026  
**Status:** Completed  

---

## My Four Constraints

### Cost
- **Budget**: ₹0 ($0). The portfolio must be completely free to build, host, and maintain.
- **Free-Tier Viability**: Any hosting or platform considered must offer an indefinite free tier with no hidden paywalls, forced credit card requirements, or surprise charges. If a free tier has limits (bandwidth, build minutes, or serverless cold starts), those limits must be documented honestly.

### Skill Level
- **Background**: Computer Science and Engineering student/researcher.
- **Competencies**: Strong proficiency in Python, machine learning workflows (PyTorch, Scikit-Learn), Git/GitHub, and core programming. Familiar with basic web development concepts (HTML, CSS, JavaScript).
- **Hard Constraint**: I am not willing to turn this portfolio into a month-long frontend framework rabbit hole. The purpose of this portfolio is to showcase my AI/ML research and engineering capability, not to demonstrate mastery of complex JavaScript state-management ecosystems.

### Portfolio Needs
The portfolio structure is directly governed by the approved Week 3 content map ([`work/week-03-through-line/content_map.md`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/work/week-03-through-line/content_map.md)):
- **Home Page**: Hero section displaying the one-line claim, system architecture diagram, featured projects highlight, "How I Work" methodology pillars, and primary CTA (`Explore My Work`).
- **Work / Case Studies Page**: In-depth 3-beat technical case studies (**Problem → What I Did → What Came Of It**) for:
  1. *Project AEGIS* (PyTorch Autoencoder anomaly detection, ROC-AUC 0.912, MSE loss distributions).
  2. *ResearchMind* (Hybrid dense/sparse RAG pipeline, LaTeX section chunking, 94.2% precision).
  3. *Selected ML Experiments* (FlyRank refresh opportunity ranking, GroupShuffleSplit validation, 3.08x lift).
- **About Page**: Academic background, CS fundamentals, research focus, and GATE 2027 technical foundation.
- **Contact Page**: Technical inquiry form, GitHub profile link, LinkedIn, and direct email CTA.
- **Project Links & Documentation**: Code repository links, terminal logs, and model receipts.

### How My Work Must Be Displayed
- **Primary Proof**: Real, empirical project evidence—not decorative illustrations or AI-generated stock graphics.
- **Visual Artifacts**:
  - Technical architecture flowcharts (`hero_architecture.png`).
  - Empirical metric charts (Autoencoder MSE reconstruction loss histogram `project_aegis_diagram.png`).
  - Codebase SVG artifacts (`outputs/charts/top_feature_importance.svg`, `confidence_mix.svg`).
  - Monospace code blocks and terminal logs.
- **Future Growth**: Capable of supporting clean interactive data visualizations (e.g., interactive loss threshold sliders or query filters) without rebuilding the site from scratch.

---

## Option 1: Plain HTML + CSS + JavaScript + GitHub Pages

- **Technology**: Vanilla HTML5, CSS3, modern vanilla JavaScript.
- **Hosting**: GitHub Pages (via repository GitHub Actions).
- **Backend Required**: No. Completely static.
- **What It Supports Well**: 
  - Zero build step, instant deployment, zero package dependencies, and permanent stability.
  - Excellent for fast-loading static case studies, reading technical documentation, and rendering pre-generated SVG charts.
- **Limitations**:
  - Code duplication: Headers, navigation bars, footer components, and layout wrappers must be manually copied across every HTML file, or stitched together using custom client-side `fetch()` scripts.
  - Scaling friction: Adding new case studies or modular project cards becomes repetitive and error-prone.
  - Interactive widgets (e.g., sliders or interactive charts) require manual DOM manipulation and custom script management.
- **Maintenance Burden**: Very low. Zero dependencies to break, update, or audit.
- **Learning Burden**: Lowest. Already familiar with HTML/CSS basics.
- **How Well It Displays My ML Work**: High for static screenshots and text, but inflexible for reusable project templates or interactive data exploration.
- **Two-Week Feasibility**: Guaranteed completion in well under 1 week.
- **Major Trade-off**: Maximum simplicity and stability traded for high development friction and manual boilerplate across multi-page case studies.

---

## Option 2: Next.js + Vercel (Without a Backend Initially)

- **Technology**: Next.js (React), CSS Modules / Tailwind CSS, static/client-side export.
- **Hosting**: Vercel (Hobby Free Tier: 100GB bandwidth, unlimited static deployments).
- **Backend Required**: No. Initially static/client-side only.
- **What It Supports Well**:
  - Reusable component architecture: Global `Navbar`, `Footer`, `CaseStudyLayout`, `MetricBadge`, and `CodeBlock` components defined once and imported everywhere.
  - File-based routing (`/`, `/work`, `/work/aegis`, `/work/researchmind`, `/about`, `/contact`) makes multi-page structure clean and intuitive.
  - Markdown/MDX support: Allows writing technical project explanations in markdown while embedding live interactive React components.
  - Rich interactive capabilities: Easy integration of client-side visualization libraries (Chart.js, Recharts) for interactive metric exploration (e.g., dynamically adjusting anomaly threshold $\tau$ to see precision changes).
- **Limitations**:
  - Build pipeline dependency: Requires Node.js, `npm`, and build step compilation.
  - Dependency drift: Occasional package updates and framework deprecations to manage over time.
- **Maintenance Burden**: Moderate. Standard `npm` dependency audits and static build checks.
- **Learning Burden**: Low-to-Moderate. With modern AI pair-programming (Antigravity/Claude) and basic JavaScript understanding, component syntax is straightforward.
- **How Well It Displays My ML Work**: Excellent. Provides professional, modern presentation for technical case studies, modular metric cards, and interactive diagrams without clutter.
- **Two-Week Feasibility**: Very realistic. Component-driven development accelerates building once core templates are established.
- **Major Trade-off**: Introduces a build toolchain and dependency management in exchange for scalable component reusability and seamless client-side interactivity.

---

## Option 3: Next.js + Vercel + Backend / API Infrastructure

- **Technology**: Next.js frontend on Vercel + Python backend (FastAPI / Flask) deployed on Render / Modal / HuggingFace Spaces.
- **Hosting**: Vercel (Frontend) + Render/Modal/HF Spaces (Backend Free Tiers).
- **Backend Required**: Yes. Dedicated server runtime executing Python model inference.
- **What It Supports Well**:
  - Live, real-time ML inference: Visitors can input raw text strings or log events into the browser and receive live PyTorch model predictions in real time.
- **Limitations**:
  - Free-tier server latency and cold starts: Render and HuggingFace free-tier instances sleep after 15 minutes of inactivity, causing 30–60 second cold start delays that frustrate reviewers.
  - Vercel serverless function limits: Free tier restricts execution time to 10 seconds and memory to 1024MB—insufficient for loading heavy PyTorch models without specialized external infrastructure.
  - Security & Cost Risk: Exposing public inference endpoints requires API rate-limiting, CORS configuration, input sanitization, and monitoring to avoid abuse or unexpected charges.
  - High Failure Surface: If the backend service sleeps, crashes, or times out, the portfolio looks broken to an engineering manager.
- **Maintenance Burden**: High. Two separate codebases, two deployment pipelines, environment variable syncing, and server health monitoring.
- **Learning Burden**: High. Requires configuring production API routing, containerization (Docker), CORS headers, and latency management.
- **How Well It Displays My ML Work**: Impressive if working, but high risk of catastrophic failure (reviewer clicks "Run Demo" and sees a 504 Gateway Timeout).
- **Two-Week Feasibility**: Unlikely. High probability of spending the entire two weeks debugging deployment configs, CORS issues, and cold starts rather than polishing project case studies.
- **Major Trade-off**: Enormous operational complexity and fragile infrastructure added to solve a capability that hiring managers do not demand.

---

## Trade-off Comparison

| Dimension | Option 1: Vanilla HTML/CSS/JS | Option 2: Next.js + Vercel (No Backend) | Option 3: Next.js + Full Backend API |
|---|---|---|---|
| **Hosting Cost** | ₹0 (GitHub Pages) | ₹0 (Vercel Hobby) | ₹0 (Vercel + Render Free Tiers) |
| **Backend Required** | No | No | Yes |
| **Component Reusability** | None (Manual copy-paste) | High (React components) | High (React components) |
| **Multi-Page Routing** | Manual HTML files | Automatic file-based routing | Automatic file-based routing |
| **Interactive Data Exploration** | Low (Raw DOM script) | High (Client-side React widgets) | Maximum (Live model inference) |
| **Infrastructure Fragility** | 0% (Static CDN, never breaks) | < 1% (Static edge build) | High (Cold starts, API timeouts) |
| **Maintenance Burden** | Minimal | Moderate (npm packages) | High (2 codebases, API monitoring) |
| **Learning Overhead** | None | Low-Moderate | High (DevOps, Docker, CORS) |
| **2-Week Completion Feasibility** | 100% | 95% | < 50% |
| **Core Value to Audience** | Good (Static proof) | **Optimal (Polished proof + speed)** | Mixed (Fragile live demo) |

---

## Pressure Test

### 1. What breaks if I choose the simplest option (Option 1)?
Nothing breaks technically—the site will load fast and never crash. However, my developer velocity breaks as the portfolio grows. Maintaining consistent headers, footers, case study cards, and metric badges across 5+ pages in plain HTML requires copying and pasting identical markup. If I want to update my navigation links or tweak the visual identity tokens, I have to edit every single HTML file manually. Furthermore, adding interactive data widgets (like an interactive loss threshold slider for AEGIS) requires raw DOM manipulation that becomes messy and difficult to maintain.

### 2. What do I gain from choosing the middle option (Option 2)?
I gain **component modularity, clean routing, and structured presentation** without adding a single server or API endpoint. I can build a single `<CaseStudyHeader />`, `<MetricCard />`, and `<TerminalBlock />`, reusing them across Project AEGIS, ResearchMind, and FlyRank experiments. I can write project writeups cleanly in MDX while embedding interactive client-side charts. Deployment on Vercel is zero-config via GitHub, with instant preview deployments for every pull request.

### 3. What complexity is introduced by the most powerful option (Option 3)?
Option 3 introduces cross-origin requests (CORS), serverless/container deployment, rate-limiting, and severe cold-start latency. On free tiers, Render or HuggingFace containers spin down when idle. If a busy research lead clicks a live inference demo, they will face a 45-second spinning loader while the container cold-starts. That creates a terrible first impression.

### 4. What would I have to maintain?
- With Option 1: Just static files.
- With Option 2: A single `package.json` with Next.js and basic UI dependencies. Updates are straightforward and isolated to one frontend codebase.
- With Option 3: Two separate codebases (frontend + Python API), container specifications, model weight storage, environment secrets, and backend uptime.

### 5. Can I realistically finish the portfolio within two weeks?
- Option 1: Yes, in 3–5 days.
- Option 2: **Yes, comfortably within 10–14 days**. Standard component architecture and AI-assisted web tooling allow building all four planned pages (Home, Work, About, Contact) rapidly.
- Option 3: No. Integrating and debugging live model inference, serialization, and serverless hosting would consume the entire time window, leaving the case studies rushed and superficial.

### 6. Does each option display my actual work properly?
Technical decision-makers (research leads and engineering managers) evaluate **rigor, methodology, code quality, and empirical results**. They inspect GitHub repositories, read architectural explanations, examine loss distributions, and check validation strategies. Option 2 displays all of this with crisp typography, structured cards, interactive charts, and embedded code snippets. Live server inference is a vanity feature that does not change the hiring decision.

### 7. Does a backend solve a real current requirement, or is it unnecessary?
A backend is **completely unnecessary** right now. Every project in my portfolio can be rigorously proven through static artifacts:
- Project AEGIS is proven by the Autoencoder architecture diagram, PyTorch training code on GitHub, and the reconstruction error distribution plot ($MSE > \tau$).
- ResearchMind is proven by the RAG chunking diagram, factual precision benchmarks (94.2%), and open-source codebase.
- FlyRank experiments are proven by Scikit-Learn evaluation scripts, feature importance charts, and client-holdout cross-validation metrics.  
None of these require a live Python backend running on a server.

---

## My Decision

> **Chosen Stack:** **Next.js + Vercel (without a backend initially)**

I chose **Next.js on Vercel** because it provides the exact balance of structure, component reusability, and professional technical presentation required to showcase my AI/ML work, without introducing operational complexity that would derail my schedule. 

It allows me to treat my portfolio like a software engineering project: modular components for case studies, structured layouts for benchmark results, and markdown integration for deep technical documentation. It gives me the flexibility to add client-side interactive data visualizations (e.g., interactive loss sliders or filtering) without requiring a backend.

---

## Why I Rejected the Other Two

1. **Why I Rejected Option 1 (Plain HTML + CSS + JS):**  
   While plain HTML is simple, it penalizes multi-page maintainability. Copying identical headers, navigation menus, and case-study layout wrappers across multiple pages creates tedious maintenance friction. As I expand the portfolio with additional projects, vanilla HTML becomes clunky and disorganized.

2. **Why I Rejected Option 3 (Next.js + Full Backend API):**  
   A live backend introduces high operational fragility (cold starts, CORS, API rate-limiting, and deployment failures) for zero meaningful gain. Technical evaluators spend 60–90 seconds reviewing candidate portfolios; they want to see clean architecture diagrams, empirical benchmark curves, and verified GitHub code, not wait for a free-tier server container to wake up. Adding a backend solves no current requirement and puts the two-week completion deadline at severe risk.

---

## Maintenance Check

**Can I maintain this?**  
**Yes.** Next.js without a backend is a single, self-contained frontend repository. Deployments to Vercel are automated directly from GitHub pushes with zero manual server management. The dependency footprint is small, and there are no external databases, authentication systems, or API endpoints to monitor.

---

## Work Display Check

**Does it show my work well?**  
**Yes, exceptionally well.** Next.js enables modular 3-beat case study layouts, high-contrast monospace code blocks, crisp SVG chart embedding, and responsive media handling. It reinforces my primary claim—*"I build and validate AI/ML systems through research, experimentation, and working implementations"*—by keeping the presentation structured, clean, and evidence-first.

---

## Two-Week Check

**Can I finish it within two weeks?**  
**Yes.** Because the sitemap and content map are already locked down ([`work/week-03-through-line/content_map.md`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/work/week-03-through-line/content_map.md)) and the visual identity tokens are defined ([`work/week-03-identity-kit/style-note.md`](file:///c:/Users/shiva/OneDrive/Desktop/FlyRank/work/week-03-identity-kit/style-note.md)), building the core pages using Next.js reusable components will take approximately 7–10 days, leaving ample time for proof-reading, link verification, and mobile testing.

---

## Backend Decision

**Do I need a backend now?**  
**No.** All current portfolio claims are validated through empirical experiment artifacts, architectural diagrams, metric distributions, and public GitHub code. If a future research project strictly requires live user-interactive inference, an external API endpoint can be added modularly at that time without altering the portfolio's core architecture.
