# Version 5 — Step Decomposition & Ground-Truth Verification

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

Work through the analysis in the following order:
Step 1: Identify the research problem and research gap.
Step 2: Identify the proposed method and explain its key components.
Step 3: Identify the dataset, experimental setup, baselines, and evaluation metrics.
Step 4: Extract the main experimental findings.
Step 5: Identify limitations explicitly stated by the authors.
Step 6: Separate author-supported conclusions from your own interpretation.
Step 7: Identify plausible research directions based on the limitations.

Do not invent information that is absent from the paper. If something cannot be established from the paper, explicitly state that it is unclear or not reported.

[Attached Paper Text: Attention Is All You Need by Vaswani et al., 2017]
```

---

## Output Comparison: Claude vs. ChatGPT

### 1. Claude Execution Output Excerpt
> "1. **Research Problem**: Recurrent architectures compute along symbol positions, precluding parallelization within training examples (Section 1).
> 2. **Research Gap**: Prior attention mechanisms were used *alongside* recurrence, not as a standalone architecture (Section 2).
> 3. **Proposed Approach**: Transformer relying entirely on Multi-Head Self-Attention ($h=8$ or $16$) and Sinusoidal Positional Encodings (Section 3.2, 3.5).
> 4. **Dataset and Experimental Setup**: WMT 2014 En-De (4.5M pairs) & En-Fr (36M pairs). Trained on 8 NVIDIA P100 GPUs (Base: 100k steps/12h; Big: 300k steps/3.5 days) (Section 5.1, 5.2).
> 5. **Evaluation Metrics**: Case-preserved BLEU score and training compute (FLOPs) (Section 5.3).
> 6. **Main Results**:
>    - En-De: **28.4 BLEU** (Table 2, Transformer Big), outperforming previous best ensemble by +2.0 BLEU.
>    - En-Fr: **41.8 BLEU** (Table 2, Transformer Big).
> 7. **Limitations**:
>    - *Stated by Authors*: Restricted max sequence length of 512 tokens in training (Section 5.1).
>    - *Unstated/Unclear*: Inference latency on standard single-GPU/CPU hardware is not reported.
> 8. **Potential Research Directions**: Extending attention to local/restricted neighborhoods to handle ultra-long sequences (Section 7)."

### 2. ChatGPT Execution Output Excerpt
> "1. **Research Problem**: Sequential processing in RNNs makes training slow for long sequences.
> 2. **Research Gap**: Existing models couldn't train efficiently on large parallel datasets without recurrent bottlenecks.
> 3. **Proposed Approach**: The Transformer model using Multi-Head Attention, residual connections, and layer normalization.
> 4. **Dataset and Experimental Setup**: WMT 2014 En-De and En-Fr datasets, trained using 8 P100 GPUs.
> 5. **Evaluation Metrics**: BLEU metric.
> 6. **Main Results**: Achieved 28.4 BLEU on English-German and 41.8 BLEU on English-French.
> 7. **Limitations**: Author-stated: max sequence length 512. Additional interpretation: self-attention requires quadratic memory $O(n^2)$ which limits long-context windows.
> 8. **Potential Research Directions**: Efficient attention variants, sparse attention, applying to vision tasks."

---

## Detailed Cross-Model Comparison Table

| Dimension | Claude (Claude 3.5 Sonnet) | ChatGPT (GPT-4o) |
|---|---|---|
| **Tone** | Highly formal, academic, and methodologically precise. Uses exact notation ($h=8$, $100k$ steps). | Accessible, structured, conversational, slightly broader summaries. |
| **Accuracy** | 100% grounded in paper text; cited specific section numbers (Section 3.2, 5.1). | Accurate core facts, but omitted exact GPU step counts ($100k$ / $300k$) and dataset pair numbers. |
| **Structure** | Strictly followed 8-section layout and explicitly separated Stated vs. Unstated limitations. | Followed 8-section layout, but merged author-stated limitations with general external knowledge. |
| **Failure Points** | Highly dense phrasing; slightly less readable for a beginner CS student. | Included external interpretation ($O(n^2)$ quadratic memory) without explicitly tagging it as unstated in text. |
