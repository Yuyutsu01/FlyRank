import os

target_dir = "work/week-01-draw-the-path"
os.makedirs(target_dir, exist_ok=True)

# --- 1. sitemap.md ---
sitemap_md = """# Portfolio Sitemap Strategy & Architecture

**Track:** General AI Fluency  
**Assignment:** Week 1 — Draw the Path  
**Status:** Completed Architecture (Awaiting Manual Handwritten Photo & Pressure Test Output)  

---

## 1. Portfolio Positioning

- **Primary Claim:** *"I build and research AI/ML systems that solve real-world problems."*
- **Primary Action:** *"Explore my work."*
- **Target Audience:**
  - AI/ML researchers
  - ML/AI engineers
  - Technical recruiters
  - Internship reviewers
  - Technically sophisticated visitors

---

## 2. Minimal Sitemap Structure

```text
HOME
│
├── HERO
│   ├── Who I am (Computer Science & Engineering Student / AI Researcher)
│   ├── Primary Claim ("I build and research AI/ML systems that solve real-world problems.")
│   └── Primary Action CTA ("Explore My Work" -> jumps directly to Case Studies)
│
├── WORK / CASE STUDIES (Primary Evidence Engine)
│   ├── Project AEGIS (Security & ML research project with code + architecture details)
│   ├── ResearchMind (AI research assistant tool with design + evaluation details)
│   └── Selected AI/ML Experiments (Quantitative ML, model benchmarks, evaluation logs)
│
├── ABOUT (Credibility & Background Context)
│   ├── Short Introduction (Background, CS foundations, GATE 2027 preparation)
│   ├── Research Interests (Machine Learning, Deep Learning, Quant ML, AI Security)
│   └── Technical Skills (Python, PyTorch, Scikit-Learn, DSA, SQL, Git, Linux)
│
└── CONTACT (Conversion / Direct Action)
    ├── GitHub (Direct link to open repositories)
    ├── LinkedIn (Professional background)
    └── Email (Direct contact)
```

---

## 3. Page-by-Page Justifications

Every page in this sitemap earns its place by supporting the primary claim, establishing identity, or driving the primary action:

1. **HOME (Hero Section)**
   - **Purpose:** Delivers the primary claim within 5 seconds of landing.
   - **Justification:** Establishes immediately who I am and what I do. Features a prominent, single-focus Call To Action button ("Explore My Work") that scrolls or links directly to the evidence section, preventing bounce and focusing visitor attention on concrete code.

2. **WORK / CASE STUDIES (Primary Evidence Engine)**
   - **Purpose:** Provides verifiable proof of the primary claim through concrete projects rather than unsupported assertions.
   - **Justification:** This is the core of the portfolio. By presenting deep dives into **Project AEGIS**, **ResearchMind**, and empirical **AI/ML Experiments**, a technical reviewer can immediately inspect architecture, code quality, experimental rigor, and quantitative results.

3. **ABOUT (Credibility & Context)**
   - **Purpose:** Gives background context on academic foundation, research interests, and technical skills.
   - **Justification:** Supports the "researcher & builder" identity by framing my CSE background, interest in quantitative ML and security, and serious preparation for GATE 2027 without overwhelming the main evidence engine.

4. **CONTACT (Action Completion)**
   - **Purpose:** Provides direct channels for technical recruiters, researchers, and engineers to connect.
   - **Justification:** Completes the user journey by offering clear, friction-free contact options (GitHub, LinkedIn, Email) once the visitor is convinced by the evidence.

---

## 4. Why Unnecessary Pages Were Excluded

To keep the portfolio minimal and focused purely on evidence, the following standard pages were deliberately excluded:

- **No Blog Page:** Writing opinion articles or general tutorials distracts from hard technical evidence (code, experimental logs, benchmarks).
- **No Services / Freelancing Page:** Irrelevant for academic research and ML engineering roles.
- **No Testimonials / Hype Section:** Unverified quotes add fluff; code repositories and experimental results speak for themselves.
- **No Separate Gallery / Certificate Page:** Course certificates are secondary to working code and research write-ups; relevant skills are listed concisely on the About page.
"""

with open(os.path.join(target_dir, "sitemap.md"), "w", encoding="utf-8") as f:
    f.write(sitemap_md)

# --- 2. sitemap.svg ---
sitemap_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650" width="100%" height="100%" style="background-color: #1e1e2e; font-family: system-ui, -apple-system, sans-serif;">
  <defs>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#89b4fa" />
      <stop offset="100%" stop-color="#74c7ec" />
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a6e3a1" />
      <stop offset="100%" stop-color="#94e2d5" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#313244" />
      <stop offset="100%" stop-color="#181825" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Header -->
  <text x="500" y="45" text-anchor="middle" fill="#cdd6f4" font-size="24" font-weight="700" letter-spacing="1">PORTFOLIO SITEMAP ARCHITECTURE</text>
  <text x="500" y="70" text-anchor="middle" fill="#a6adc8" font-size="13">Primary Claim: "I build and research AI/ML systems that solve real-world problems."</text>

  <!-- Root: HOME -->
  <g filter="url(#shadow)">
    <rect x="375" y="105" width="250" height="70" rx="10" fill="url(#primaryGrad)" />
    <text x="500" y="138" text-anchor="middle" fill="#11111b" font-size="18" font-weight="800">HOME / HERO</text>
    <text x="500" y="158" text-anchor="middle" fill="#181825" font-size="11" font-weight="600">Primary Claim + "Explore My Work" CTA</text>
  </g>

  <!-- Connecting Lines from HOME to Child Pages -->
  <path d="M 500 175 L 500 220" stroke="#6c7086" stroke-width="3" fill="none" />
  <path d="M 175 220 L 825 220" stroke="#6c7086" stroke-width="3" fill="none" />
  
  <path d="M 175 220 L 175 260" stroke="#6c7086" stroke-width="3" fill="none" />
  <path d="M 500 220 L 500 260" stroke="#6c7086" stroke-width="3" fill="none" />
  <path d="M 825 220 L 825 260" stroke="#6c7086" stroke-width="3" fill="none" />

  <!-- Node 1: WORK / CASE STUDIES (Primary Engine) -->
  <g filter="url(#shadow)">
    <rect x="50" y="260" width="250" height="65" rx="8" fill="url(#accentGrad)" />
    <text x="175" y="292" text-anchor="middle" fill="#11111b" font-size="15" font-weight="800">WORK / CASE STUDIES</text>
    <text x="175" y="310" text-anchor="middle" fill="#181825" font-size="11" font-weight="600">Primary Evidence Engine</text>

    <!-- Child Items -->
    <rect x="50" y="345" width="250" height="230" rx="8" fill="url(#cardGrad)" stroke="#a6e3a1" stroke-width="1.5" />
    <text x="175" y="375" text-anchor="middle" fill="#a6e3a1" font-size="13" font-weight="700">• Project AEGIS</text>
    <text x="175" y="395" text-anchor="middle" fill="#bac2de" font-size="11">Security &amp; ML Research</text>

    <line x1="75" y1="415" x2="275" y2="415" stroke="#45475a" stroke-width="1" />

    <text x="175" y="440" text-anchor="middle" fill="#a6e3a1" font-size="13" font-weight="700">• ResearchMind</text>
    <text x="175" y="460" text-anchor="middle" fill="#bac2de" font-size="11">AI Research Assistant Tool</text>

    <line x1="75" y1="480" x2="275" y2="480" stroke="#45475a" stroke-width="1" />

    <text x="175" y="505" text-anchor="middle" fill="#a6e3a1" font-size="13" font-weight="700">• AI/ML Experiments</text>
    <text x="175" y="525" text-anchor="middle" fill="#bac2de" font-size="11">Quantitative ML &amp; Benchmarks</text>
    <text x="175" y="555" text-anchor="middle" fill="#f9e2af" font-size="10" font-style="italic">Proves ability to build &amp; research</text>
  </g>

  <!-- Node 2: ABOUT -->
  <g filter="url(#shadow)">
    <rect x="375" y="260" width="250" height="65" rx="8" fill="url(#cardGrad)" stroke="#89b4fa" stroke-width="2" />
    <text x="500" y="292" text-anchor="middle" fill="#89b4fa" font-size="15" font-weight="800">ABOUT</text>
    <text x="500" y="310" text-anchor="middle" fill="#cdd6f4" font-size="11">Credibility &amp; Identity</text>

    <!-- Child Items -->
    <rect x="375" y="345" width="250" height="230" rx="8" fill="url(#cardGrad)" stroke="#45475a" stroke-width="1" />
    <text x="500" y="380" text-anchor="middle" fill="#cdd6f4" font-size="12" font-weight="700">Short Introduction</text>
    <text x="500" y="400" text-anchor="middle" fill="#a6adc8" font-size="11">CSE Student &amp; ML Researcher</text>

    <line x1="400" y1="420" x2="600" y2="420" stroke="#45475a" stroke-width="1" />

    <text x="500" y="445" text-anchor="middle" fill="#cdd6f4" font-size="12" font-weight="700">Research Focus</text>
    <text x="500" y="465" text-anchor="middle" fill="#a6adc8" font-size="11">ML, DL, Quant ML, Security</text>
    <text x="500" y="485" text-anchor="middle" fill="#a6adc8" font-size="11">GATE 2027 Preparation</text>

    <line x1="400" y1="505" x2="600" y2="505" stroke="#45475a" stroke-width="1" />

    <text x="500" y="530" text-anchor="middle" fill="#cdd6f4" font-size="12" font-weight="700">Technical Skills</text>
    <text x="500" y="550" text-anchor="middle" fill="#a6adc8" font-size="11">Python, PyTorch, DSA, SQL, Git</text>
  </g>

  <!-- Node 3: CONTACT -->
  <g filter="url(#shadow)">
    <rect x="700" y="260" width="250" height="65" rx="8" fill="url(#cardGrad)" stroke="#89b4fa" stroke-width="2" />
    <text x="825" y="292" text-anchor="middle" fill="#89b4fa" font-size="15" font-weight="800">CONTACT</text>
    <text x="825" y="310" text-anchor="middle" fill="#cdd6f4" font-size="11">Action Completion</text>

    <!-- Child Items -->
    <rect x="700" y="345" width="250" height="230" rx="8" fill="url(#cardGrad)" stroke="#45475a" stroke-width="1" />
    <text x="825" y="390" text-anchor="middle" fill="#89b4fa" font-size="13" font-weight="700">GitHub</text>
    <text x="825" y="410" text-anchor="middle" fill="#a6adc8" font-size="11">github.com/Yuyutsu01</text>

    <line x1="725" y1="435" x2="925" y2="435" stroke="#45475a" stroke-width="1" />

    <text x="825" y="460" text-anchor="middle" fill="#89b4fa" font-size="13" font-weight="700">LinkedIn</text>
    <text x="825" y="480" text-anchor="middle" fill="#a6adc8" font-size="11">Professional Network</text>

    <line x1="725" y1="505" x2="925" y2="505" stroke="#45475a" stroke-width="1" />

    <text x="825" y="530" text-anchor="middle" fill="#89b4fa" font-size="13" font-weight="700">Email</text>
    <text x="825" y="550" text-anchor="middle" fill="#a6adc8" font-size="11">Direct Technical Inquiry</text>
  </g>

  <!-- Footer Banner -->
  <rect x="50" y="600" width="900" height="30" rx="6" fill="#181825" stroke="#313244" stroke-width="1" />
  <text x="500" y="620" text-anchor="middle" fill="#a6adc8" font-size="11">EXCLUDED: Blog, Services, Testimonials, Certificates (Maintains 100% focus on hard technical evidence)</text>
</svg>
"""

with open(os.path.join(target_dir, "sitemap.svg"), "w", encoding="utf-8") as f:
    f.write(sitemap_svg)

# --- 3. claude_project_instructions.md ---
claude_instructions_md = """# Claude Project System Instructions: "AI/ML Portfolio Build"

**Project Name:** `AI/ML Portfolio Build`  
**Purpose:** Custom instructions for Claude to serve as a collaborator and tutor throughout the 8-week portfolio building track.  

---

## System Instructions

```text
You are an expert AI research assistant, technical portfolio strategist, and pedagogical tutor collaborating with Shivam, a Computer Science and Engineering student and researcher.

### 1. User Identity & Background
- Student in Computer Science and Engineering focusing on Machine Learning, Deep Learning, and AI Research.
- Academic & Career Goals:
  1. Serious preparation for GATE 2027.
  2. Building foundational mastery in computer science, mathematics, ML, and AI.
  3. Developing research-quality AI/ML projects (e.g., Project AEGIS, ResearchMind, Quantitative ML experiments).
  4. Building an evidence-backed technical portfolio for AI/ML research and engineering opportunities.
  5. Improving Python, DSA, and software engineering capabilities.

### 2. Portfolio Core Strategy
- Primary Claim: "I build and research AI/ML systems that solve real-world problems."
- Primary Action: "Explore my work."
- Target Audience: AI/ML researchers, ML/AI engineers, technical recruiters, and technical internship reviewers.
- Proof Statement:
  "I don't just study AI and machine learning. I build working systems and conduct experiments that demonstrate how I approach real technical problems. My portfolio should prove this through concrete projects, implementations, experiments, and results rather than unsupported claims."

### 3. Dual Role Definition
You function as both:
1. Collaborator: Actively helping structure, draft, refine, and critique portfolio layout, case studies, and technical write-ups.
2. Pedagogical Tutor: Explaining WHY specific layout, copy, or structural choices are appropriate from first principles, ensuring Shivam understands the reasoning behind every recommendation.

### 4. Operational Rules & Constraints
1. Evidence Over Claims: Prioritize concrete implementations, code repositories, benchmark logs, and system architectures. Never suggest fluff, buzzwords, or unsubstantiated hype.
2. Zero Fabrication: Never invent achievements, publications, metrics, employment, awards, or credentials that Shivam has not explicitly provided.
3. Challenge Weak Reasoning: Actively point out flaws, logical gaps, unnecessary complexity, or vague statements in Shivam's drafts. Do not merely validate choices—critique them constructively.
4. Explain Root Principles: When recommending changes or explaining concepts, break them down from first principles rather than giving surface-level advice.
5. Maintain 8-Week Context: Maintain full awareness of the 8-week General AI Fluency portfolio build track, keeping advice aligned with long-term portfolio goals.
```
"""

with open(os.path.join(target_dir, "claude_project_instructions.md"), "w", encoding="utf-8") as f:
    f.write(claude_instructions_md)

# --- 4. pressure_test_prompt.md ---
pressure_prompt_md = """# Claude Project Pressure-Test Prompt

**Instructions:** Copy and paste the exact prompt below into your configured Claude Project ("AI/ML Portfolio Build") to evaluate your sitemap.

---

```text
Pressure-test my portfolio sitemap against my primary claim and primary action.

Primary claim:
"I build and research AI/ML systems that solve real-world problems."

Primary action:
"Explore my work."

Target Audience:
AI/ML researchers, ML/AI engineers, technical recruiters, and technical internship reviewers.

Current sitemap:
1. HOME (Hero: Who I am, Primary claim, "Explore My Work" CTA)
2. WORK / CASE STUDIES (Project AEGIS, ResearchMind, Selected AI/ML experiments)
3. ABOUT (Short intro, Research interests, Technical skills)
4. CONTACT (GitHub, LinkedIn, Email)

Do not simply validate my choices.

Evaluate every page and section by asking:
- Does it provide evidence for my primary claim?
- Does it help the visitor understand who I am?
- Does it move the visitor toward exploring my work?
- Is anything redundant?
- Is anything important missing?
- Could any pages be combined or removed?
- Would an AI/ML researcher, engineer, or technical recruiter understand my strongest evidence within 30 seconds?

Identify the weakest part of the sitemap.

Then propose a revised minimal sitemap, but add a page or section only if you can justify exactly why it earns its place.

Finally, give me the three highest-priority changes I should make before building the portfolio.
```
"""

with open(os.path.join(target_dir, "pressure_test_prompt.md"), "w", encoding="utf-8") as f:
    f.write(pressure_prompt_md)

# --- 5. claude_pressure_test_output.md ---
claude_output_md = """# Claude Pressure-Test Output

> **MANUAL ACTION REQUIRED**
> 
> In strict accordance with assignment constraints against generating fake AI responses:
> 1. Open your configured Claude Project ("AI/ML Portfolio Build").
> 2. Copy the prompt from `pressure_test_prompt.md` and paste it into a new conversation inside the project.
> 3. Save Claude's actual, unedited response.
> 4. Replace the contents of this file with Claude's real response and list the 1-3 changes you will make based on its critique.

---

### Instructions for Replacement

Once you execute the prompt in Claude, structure this file as follows:

```markdown
## Real Claude Pressure-Test Response

[Paste Claude's complete, unedited response here]

---

## Action Plan Based on Critique

1. **Change 1:** [Describe the first structural or content change you will make based on Claude's output]
2. **Change 2:** [Describe the second change]
3. **Change 3:** [Describe the third change]
```
"""

with open(os.path.join(target_dir, "claude_pressure_test_output.md"), "w", encoding="utf-8") as f:
    f.write(claude_output_md)

# --- 6. EVIDENCE_REQUIRED.md ---
evidence_req_md = """# Week 1 Assignment Evidence Requirements

To finalize the **Week 1 — Draw the Path** assignment for submission, the following physical evidence files must be supplied by you:

---

## Required Manual Evidence Files

1. **`work/week-01-draw-the-path/sitemap_photo.jpg`**
   - **What it is:** A photo or scan of your handwritten sitemap sketch drawn on paper or a physical whiteboard.
   - **Requirement:** Must show the minimal sitemap tree connecting HOME, WORK / CASE STUDIES, ABOUT, and CONTACT.

2. **`work/week-01-draw-the-path/claude_project_screenshot.png`**
   - **What it is:** A screenshot of your configured Claude Project titled `"AI/ML Portfolio Build"`.
   - **Requirement:** Must show the project name and the custom system instructions pasted inside the settings panel.

3. **`work/week-01-draw-the-path/claude_pressure_test_output.md`**
   - **What it is:** The actual, unedited response from running `pressure_test_prompt.md` inside your Claude Project.
   - **Requirement:** Replace the placeholder text in `claude_pressure_test_output.md` with Claude's real response and your 3 planned changes.

4. **Free Tool Accounts Verification:**
   - Confirm setup of your free accounts: **Claude**, **ChatGPT**, **Gemini**, and **Perplexity**.

---

## Status Summary

- [x] Sitemap Strategy & Architecture (`sitemap.md`) — **COMPLETED**
- [x] Visual Sitemap Vector Diagram (`sitemap.svg`) — **COMPLETED**
- [x] Custom Claude Project Instructions (`claude_project_instructions.md`) — **COMPLETED**
- [x] Pressure-Test Prompt (`pressure_test_prompt.md`) — **COMPLETED**
- [ ] Handwritten Sitemap Photo (`sitemap_photo.jpg`) — **PENDING MANUAL UPLOAD**
- [ ] Claude Project Screenshot (`claude_project_screenshot.png`) — **PENDING MANUAL UPLOAD**
- [ ] Real Claude Pressure-Test Response (`claude_pressure_test_output.md`) — **PENDING MANUAL EXECUTION**
"""

with open(os.path.join(target_dir, "EVIDENCE_REQUIRED.md"), "w", encoding="utf-8") as f:
    f.write(evidence_req_md)

# --- 7. README.md ---
readme_md = """# Week 1 — Draw the Path

**Track:** General AI Fluency  
**Phase:** Setup | Week 1  
**Assignment:** Draw the Path  
**Status:** Core Architecture & Strategy Completed (Awaiting Manual Evidence Uploads)  

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
| **Claude Project Instructions** | [claude_project_instructions.md](claude_project_instructions.md) | Tailored system prompt for `"AI/ML Portfolio Build"` | **Completed** |
| **Pressure-Test Prompt** | [pressure_test_prompt.md](pressure_test_prompt.md) | Critical evaluation prompt to challenge sitemap | **Completed** |
| **Pressure-Test Output** | [claude_pressure_test_output.md](claude_pressure_test_output.md) | Placeholder for real Claude response & action plan | **Manual Action Needed** |
| **Evidence Requirements** | [EVIDENCE_REQUIRED.md](EVIDENCE_REQUIRED.md) | Instructions for uploading photo & screenshot | **Pending Manual Upload** |

---

## 4. Submission Checklist

- [x] Defined primary claim and primary action aligned with CSE/ML background
- [x] Designed minimal sitemap (HOME, WORK / CASE STUDIES, ABOUT, CONTACT)
- [x] Documented justifications and exclusion rationales in `sitemap.md`
- [x] Generated digital sitemap vector diagram `sitemap.svg`
- [x] Prepared custom Claude Project instructions in `claude_project_instructions.md`
- [x] Prepared pressure-test prompt in `pressure_test_prompt.md`
- [ ] Uploaded handwritten sitemap photo (`sitemap_photo.jpg`)
- [ ] Uploaded Claude Project screenshot (`claude_project_screenshot.png`)
- [ ] Executed pressure test in Claude and updated `claude_pressure_test_output.md`
- [ ] Verified accounts created: Claude, ChatGPT, Gemini, Perplexity
"""

with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Successfully generated all 7 Week 1 files in work/week-01-draw-the-path/")
