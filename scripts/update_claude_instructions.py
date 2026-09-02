import os

filepath = "work/week-01-draw-the-path/claude_project_instructions.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

if "Voice Card" not in content:
    content += """

### 5. Voice Card & Tone Instructions
Maintain the following voice card tone across all copy, case studies, and recommendations:
- Tone: **Direct, technical, clear, grounded, curious, evidence-driven.**
- Avoid beige corporate buzzwords, generic hype, or unsupported assertions.
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated claude_project_instructions.md with Voice Card!")
else:
    print("Voice Card already present in claude_project_instructions.md.")
