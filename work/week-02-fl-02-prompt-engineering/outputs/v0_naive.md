# Version 0 — Naive Baseline

### Exact Prompt
```text
Analyze this research paper and explain it to me.

[Attached Paper Text: Attention Is All You Need by Vaswani et al., 2017]
```

### Actual AI Output Excerpt
> "This paper introduces the Transformer model, a neural network architecture for machine translation and sequence modeling. It replaces recurrent neural networks (RNNs) and convolutional neural networks (CNNs) with attention mechanisms. The Transformer uses encoder and decoder stacks and achieves better BLEU scores on English-to-German and English-to-French translation datasets. Overall, attention mechanisms help models focus on important words."

### What Changed in Prompt
- Initial naive baseline. No role, context, format, examples, or verification constraints.

### Observed Change in Output
- N/A (Baseline starting point).

### Why It Mattered
- Demonstrates what an unguided AI model produces by default: a high-level summary that covers surface-level claims without technical depth.

### What Still Failed
- **Superficial & Generic**: Fails to explain *how* self-attention works mathematically, omits positional encoding details, ignores training infrastructure (P100 GPUs), and ends with fluff.

### What to Try Next
- Assign an explicit persona/role to elevate the technical vocabulary and analytical focus.
