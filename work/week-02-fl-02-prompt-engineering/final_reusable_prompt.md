# Final Reusable Prompt Template

This prompt template is fully parameterized for reuse by any user across any technical domain or material analysis task.

---

```text
You are an experienced [DOMAIN_ROLE] researcher.

The user is a [USER_BACKGROUND] analyzing [MATERIAL_TYPE] for the purpose of [PURPOSE].

Use the following example to understand the level of analysis required:

Example:
Problem: [EXAMPLE_PROBLEM]
Method: [EXAMPLE_METHOD]
Result: [EXAMPLE_RESULT]
Limitation: [EXAMPLE_LIMITATION]

Analyze the provided material using the following structure:

1. Research problem
2. Research gap
3. Proposed approach
4. Dataset and experimental setup
5. Evaluation metrics
6. Main results
7. Limitations
8. Potential research directions

Work through the analysis in the following order:
Step 1: Identify the research problem and research gap.
Step 2: Identify the proposed method and explain its key components.
Step 3: Identify the dataset, experimental setup, baselines, and evaluation metrics.
Step 4: Extract the main experimental findings.
Step 5: Identify limitations explicitly stated by the authors.
Step 6: Separate author-supported conclusions from your own interpretation.
Step 7: Identify plausible research directions based on the limitations.

Requirements:
- Use only claims supported by the material.
- Clearly distinguish between evidence explicitly supported by the text and external interpretation.
- Do not invent missing details, metrics, or citations.
- If information is unavailable or unstated in the material, explicitly write "Unstated in text".

Material to analyze:
[INPUT_MATERIAL]
```
