import os

target_dir = "work/week-01-what-are-you-proving"
os.makedirs(target_dir, exist_ok=True)

# 1. proof_statement.md
proof_statement_md = """# What Are You Proving?

**Track:** General AI Fluency  
**Phase:** Setup | Week 1  
**Assignment:** What Are You Proving?  
**Status:** Completed  

---

## 1. Primary Claim

I can design, build, and experimentally validate machine learning and AI systems for real-world problems, and I demonstrate that ability through working implementations, research-driven experiments, and measurable results.

---

## 2. Audience

AI/ML research leads and engineering managers evaluating candidates for research or engineering internships.

---

## 3. Primary Action

Explore my selected projects and case studies.

---

## 4. Proof Statement

I can design, build, and experimentally validate machine learning and AI systems for real-world problems, and I demonstrate that ability through working implementations, research-driven experiments, and measurable results. This portfolio is for AI/ML research leads and engineering managers evaluating candidates for research or engineering internships who need evidence of practical technical ability beyond coursework or a résumé. The primary action I want them to take is to explore my selected projects and case studies so they can evaluate how I approach problems, build systems, and validate my work.

---

## 5. Why This Needs to Exist

A CV or LinkedIn profile can list my skills and projects, but they cannot demonstrate how I actually approach technical problems, build AI/ML systems, or validate whether they work; this portfolio exists to provide that evidence.
"""

with open(os.path.join(target_dir, "proof_statement.md"), "w", encoding="utf-8") as f:
    f.write(proof_statement_md)

# 2. ai_interview.md
ai_interview_md = """# AI Interview: Portfolio Positioning & Proof Discovery

**Role:** Critical AI Interviewer & Portfolio Strategist  
**Candidate:** Shivam (Computer Science & Engineering Student / AI Researcher)  
**Objective:** Interrogate candidate positioning to narrow down 5 broad claims into 1 defensible claim, 1 specific audience, and 1 primary action.  

---

## 1. Initial Positioning

### Candidate's Initial Thoughts:
> "I am a CSE student passionate about Machine Learning, Deep Learning, Python, research, AI security, quantitative finance, and software engineering. I want to build a portfolio for companies, recruiters, and research labs showing everything I have worked on."

### Interviewer's Initial Assessment:
> "Your initial statement is five claims wearing a trench coat. Saying you are passionate about ML, DL, Python, security, and quant finance tells me you haven't decided what you are capable of proving. Recruiters and research leads don't care about 'passion'—they care about evidence. We need to isolate ONE capability you can genuinely prove, ONE decision-maker who cares, and ONE action you want them to take."

---

## 2. Questions and Answers

### Round 1: Testing the Core Claim
- **Interviewer:** "You mentioned ML, Deep Learning, Quantitative Finance, and AI Security. If I give you 30 seconds to show an engineering manager ONE thing that proves your technical competence, what do you show them?"
- **Candidate:** "I would show them my working implementations—like Project AEGIS and ResearchMind—where I didn't just read about models, but built datasets, trained PyTorch architectures, and evaluated quantitative metrics."
- **Interviewer Critique:** "Good. So the claim isn't 'I know AI theory' or 'I am interested in research.' The claim is that you can **design, build, and experimentally validate** machine learning systems."

### Round 2: Narrowing the Audience
- **Interviewer:** "Who specifically needs to see this? Don't say 'recruiters' or 'everyone'."
- **Candidate:** "I want to reach AI/ML research leads and engineering managers who hire for research or ML engineering internships."
- **Interviewer Critique:** "Accepted. A Research Lead or Engineering Manager has a high bar for technical truth. They don't care about course grades; they want to see how you approach unstructured problems, structure experiments, and handle edge cases."

### Round 3: Locking Down the Single Action
- **Interviewer:** "What is the ONE action you want this Engineering Manager to take after arriving on your homepage?"
- **Candidate:** "I want them to click on my selected projects and read my case studies."
- **Interviewer Critique:** "Perfect. The primary action is **'Explore my selected projects and case studies.'** Not 'contact me immediately,' not 'download my resume,' but inspecting the evidence."

### Round 4: The Honest Rationale
- **Interviewer:** "Why does this portfolio need to exist at all? Why isn't your resume or LinkedIn profile enough?"
- **Candidate:** "A resume lists bullet points and tech stacks, but it cannot show my actual code quality, how I design experiments, how I handle failure modes, or how I prove a model works."
- **Interviewer Critique:** "That is your honest rationale: *A CV or LinkedIn profile can list my skills and projects, but they cannot demonstrate how I actually approach technical problems, build AI/ML systems, or validate whether they work; this portfolio exists to provide that evidence.*"

---

## 3. Final Decision

### Claim
I can design, build, and experimentally validate machine learning and AI systems for real-world problems, and I demonstrate that ability through working implementations, research-driven experiments, and measurable results.

### Audience
AI/ML research leads and engineering managers evaluating candidates for research or engineering internships.

### Action
Explore my selected projects and case studies.

---

## 4. What Changed

1. **Shifted from Broad Buzzwords to Single Defensible Claim:** Replaced vague assertions ("passionate about AI/ML/Python/Research") with a single, verifiable technical capability: designing, building, and experimentally validating systems.
2. **Defined Specific Decision-Maker:** Refused generic "recruiters/everyone" in favor of AI/ML Research Leads and Engineering Managers who evaluate technical depth for internships.
3. **Focused Single Primary Action:** Directed all portfolio architecture toward driving the visitor to inspect concrete project case studies rather than bouncing or reading fluff.
4. **Established Factual Portfolio Purpose:** Defined the portfolio's unique purpose as providing proof of engineering approach and experimental validation that static CVs cannot convey.
"""

with open(os.path.join(target_dir, "ai_interview.md"), "w", encoding="utf-8") as f:
    f.write(ai_interview_md)

# 3. README.md
readme_md = """# Week 1 — What Are You Proving?

**Track:** General AI Fluency  
**Phase:** Setup | Week 1  
**Assignment:** What Are You Proving?  
**Status:** **Completed**  

---

## 1. Objective

The objective of this assignment is to lock down the core positioning of the technical portfolio—defining exactly **One Claim**, **One Audience**, and **One Action**—before designing the sitemap or building any web pages.

---

## 2. Core Positioning Summary

- **Primary Claim:** *"I can design, build, and experimentally validate machine learning and AI systems for real-world problems, and I demonstrate that ability through working implementations, research-driven experiments, and measurable results."*
- **Audience:** *"AI/ML research leads and engineering managers evaluating candidates for research or engineering internships."*
- **Primary Action:** *"Explore my selected projects and case studies."*

---

## 3. Assignment File Map

| File Path | Description | Status |
|---|---|---|
| [proof_statement.md](proof_statement.md) | Official Proof Statement, Claim, Audience, Action, and Rationale | **Completed** |
| [ai_interview.md](ai_interview.md) | Interactive AI Interview transcript documenting positioning discovery | **Completed** |

---

## 4. Submission Checklist

- [x] Defined exactly ONE primary capability claim
- [x] Defined exactly ONE specific target audience (AI/ML Research Leads & Engineering Managers)
- [x] Defined exactly ONE primary action ("Explore my selected projects and case studies")
- [x] Crafted full single-paragraph Proof Statement
- [x] Authored one-line honest rationale explaining why the portfolio must exist beyond a CV/LinkedIn
- [x] Conducted AI interview pressure test and documented transcript in `ai_interview.md`
"""

with open(os.path.join(target_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Successfully generated all files in work/week-01-what-are-you-proving/")
