# Version 2 — Context + Motivation

### Exact Prompt
```text
You are an experienced machine learning researcher.

I am a computer science student developing my machine learning and research skills. I am analyzing this paper to understand how researchers formulate problems, design experiments, evaluate models, and identify limitations.

Analyze this research paper and explain it to me.

[Attached Paper Text: Attention Is All You Need by Vaswani et al., 2017]
```

### Actual AI Output Excerpt
> "From a research perspective tailored for a CS student: The authors formulate the core bottleneck in sequence modeling—sequential computation in RNNs prevents parallelization during training. To solve this, they design the Transformer using self-attention. When evaluating the model, they compare it against state-of-the-art RNN and CNN ensembles on WMT 2014 En-De and En-Fr benchmarks, evaluating both translation quality (BLEU score) and training efficiency (FLOPs)."

### What Changed in Prompt
- **Added Technique:** `Context + Motivation` (Specified CS student background, learning goals regarding problem formulation, experiment design, and limitations).

### Observed Change in Output
- **Pedagogical Alignment**: Output shifted from abstract research commentary to explicitly addressing *problem formulation*, *experimental design*, and *evaluation metrics* (BLEU vs FLOPs).

### Why It Mattered
- Giving the model explicit user context ensures the generated analysis aligns with the user's specific learning objectives rather than guessing what information is relevant.

### What Still Failed
- **Unstructured Layout**: The output remains a continuous block of text, omitting explicit breakdowns of datasets, hardware setups, or stated limitations.

### What to Try Next
- Provide a few-shot example demonstrating the exact structural density and tone expected.
