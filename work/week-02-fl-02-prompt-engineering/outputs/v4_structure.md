# Version 4 — Output Structure

### Exact Prompt
```text
You are an experienced machine learning researcher.

I am a computer science student developing my machine learning and research skills. I am analyzing this paper to understand how researchers formulate problems, design experiments, evaluate models, and identify limitations.

Use the following example to understand the level of analysis I want:

Example:
Problem: The authors investigate whether X can improve Y.
Method: They compare method A against baseline B using dataset C.
Result: Method A improves metric D over baseline B.
Limitation: The evaluation is limited because dataset C does not represent scenario E.

Analyze the paper using this structure:

1. Research problem
2. Research gap
3. Proposed approach
4. Dataset and experimental setup
5. Evaluation metrics
6. Main results
7. Limitations
8. Potential research directions

[Attached Paper Text: Attention Is All You Need by Vaswani et al., 2017]
```

### Actual AI Output Excerpt
> "1. **Research Problem**: Sequential computation in RNNs prevents training parallelization.
> 2. **Research Gap**: Existing attention models still rely on recurrent hidden states to preserve order.
> 3. **Proposed Approach**: Transformer using Multi-Head Attention, Positional Encodings, and LayerNorm.
> 4. **Dataset and Experimental Setup**: WMT 2014 En-De (4.5M pairs) and En-Fr (36M pairs). Trained on 8 NVIDIA P100 GPUs (Base: 12h, Big: 3.5 days).
> 5. **Evaluation Metrics**: BLEU score and total training FLOPs.
> 6. **Main Results**: En-De 28.4 BLEU, En-Fr 41.8 BLEU.
> 7. **Limitations**: High memory footprint for long sequences; potential sensitivity to hyper-parameter tuning.
> 8. **Potential Research Directions**: Applying self-attention to image, audio, and video inputs."

### What Changed in Prompt
- **Added Technique:** `Output Structure` (Mandated an 8-section numbered schema).

### Observed Change in Output
- **Complete Structural Organization**: Output generated explicit numbered headings covering hardware setup (P100 GPUs), datasets (4.5M/36M pairs), and future directions (vision/audio modalities).

### Why It Mattered
- Output structuring prevents the AI from skipping secondary yet vital technical details (like experimental compute setup) by creating explicit slots that must be filled.

### What Still Failed
- **Unverified Assumptions**: In Section 7 (Limitations), the model listed "sensitivity to hyper-parameter tuning" without specifying whether the paper explicitly proved this or if it was AI speculation.

### What to Try Next
- Add step-by-step decomposition and strict anti-hallucination ground-truth verification constraints.
