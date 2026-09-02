# Version 1 — Role Assignment

### Exact Prompt
```text
You are an experienced machine learning researcher.

Analyze this research paper and explain it to me.

[Attached Paper Text: Attention Is All You Need by Vaswani et al., 2017]
```

### Actual AI Output Excerpt
> "As a machine learning researcher, I view this paper as a paradigm shift in sequence modeling. The Transformer architecture eliminates sequential recurrence entirely, replacing $O(n)$ path length dependencies with $O(1)$ constant-time self-attention. The key technical contribution lies in Scaled Dot-Product Attention and Multi-Head Attention, allowing the network to jointly process representations across multiple feature subspaces."

### What Changed in Prompt
- **Added Technique:** `Role Assignment` (`"You are an experienced machine learning researcher."`)

### Observed Change in Output
- **Elevated Vocabulary & Technical Depth**: Output immediately dropped generic prose and introduced formal ML concepts like $O(1)$ path length, sequence recurrence trade-offs, and multi-head representation subspaces.

### Why It Mattered
- Setting a domain expert persona forces the language model to adopt domain-appropriate technical framing and prioritize architectural innovation over high-level summaries.

### What Still Failed
- **Assumed Audience**: The AI assumed the user possessed advanced ML background knowledge without tailoring explanations, creating dense, unguided paragraphs.

### What to Try Next
- Add user context and motivation to align the technical depth with the learner's specific background and goals.
