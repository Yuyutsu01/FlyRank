# Prompt Ladder: Research Paper Analysis

**Track:** General AI Fluency  
**Phase:** Setup | Week 2  
**Assignment:** Prompt Ladder  
**Target Task:** Systematic Technical Analysis of Machine Learning Research Papers  

---

## Task Overview

We analyze how single, incremental prompt modifications ("layers") systematically transform the quality, focus, and reliability of AI outputs when analyzing a machine learning research paper (Target Paper: *Attention Is All You Need* by Vaswani et al., 2017).

---

## 1. Baseline: Weak Prompt

### Exact Prompt
```text
Explain this research paper.
[Attached Paper Text: Attention Is All You Need]
```

### AI Output Excerpt
> "This paper presents the Transformer, a new network architecture based on attention mechanisms. It replaces recurrent neural networks (RNNs) and convolutional neural networks (CNNs) in sequence-to-sequence tasks like machine translation. Transformers are faster to train and achieve state-of-the-art results on BLEU scores for English-to-German and English-to-French translation tasks. Overall, AI is changing how translation works."

### What Changed in Prompt
- Initial weak baseline. No goal, audience, format, or quality constraints specified.

### What Improved in Output
- N/A (Baseline starting point).

### What Still Failed in Output
- **High-level fluff & superficial summary**: Explains *what* the paper is in generic terms without explaining *how* self-attention works or *why* positional encodings are required.
- **Irrelevant fluff**: Concludes with a generic sentence ("Overall, AI is changing how translation works") that adds zero technical value.

### What to Try Next
- Add a specific goal to force the model to focus on technical contributions and core methodology.

---

## 2. Version 1: Clearer Goal

### Exact Prompt
```text
Explain this research paper so I can understand the main research contribution and methodology.
[Attached Paper Text: Attention Is All You Need]
```

### AI Output Excerpt
> "The main research contribution of this paper is the Transformer architecture, which dispenses with recurrence and convolutions entirely. Instead, it relies solely on self-attention mechanisms to compute representations of its input and output. The methodology uses Scaled Dot-Product Attention and Multi-Head Attention, allowing the model to jointly attend to information from different representation subspaces at different positions."

### What Changed in Prompt
- **Added Layer:** `+ Clearer Goal` (Specifically instructed to explain the *main research contribution* and *methodology*).

### What Improved in Output
- **Technical Focus**: Output eliminated generic introductory fluff and immediately identified the core architectural novelty (dispensing with RNNs/CNNs in favor of self-attention).
- **Core Methodology Mentioned**: Introduced specific mathematical components like Scaled Dot-Product Attention and Multi-Head Attention.

### What Still Failed in Output
- **Undefined Technical Depth**: Uses specialized jargon without tailoring the explanation depth to a specific background level (e.g. assumes prior knowledge of dot-product attention without context).
- **Unstructured Paragraph**: Information is presented in a dense block of text, making key takeaways hard to skim.

### What to Try Next
- Add a defined target audience to scope the technical depth and terminology expectations.

---

## 3. Version 2: Defined Audience

### Exact Prompt
```text
Explain this research paper so that a machine learning researcher who already understands basic ML can understand the main research contribution and methodology.
[Attached Paper Text: Attention Is All You Need]
```

### AI Output Excerpt
> "For an ML researcher: The paper's main contribution is replacing sequential $O(n)$ recurrence with $O(1)$ constant-path self-attention, enabling parallel training across sequence lengths. The core methodology relies on Query-Key-Value ($Q, K, V$) projections where Attention $(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$. Multi-head attention splits $d_{\text{model}}$ into $h$ heads to capture distinct positional relationships simultaneously."

### What Changed in Prompt
- **Added Layer:** `+ Defined Audience` (Targeted at a *machine learning researcher who already understands basic ML*).

### What Improved in Output
- **Appropriate Technical Rigor**: Removed basic definitions of machine learning and jumped directly to asymptotic computational complexity ($O(1)$ path length vs. $O(n)$ for RNNs) and matrix projection mechanics ($Q, K, V$).
- **Mathematical Clarity**: Included the exact scaling factor $\frac{1}{\sqrt{d_k}}$ and explained *why* it prevents vanishing gradients in softmax at high dimensions.

### What Still Failed in Output
- **Lack of Output Structure**: The output remains an unorganized technical narrative. It omits critical sections like dataset details, baseline comparisons, and hyper-parameter configurations.

### What to Try Next
- Add a rigid output structure to force complete coverage across all paper sections.

---

## 4. Version 3: Specific Output Format

### Exact Prompt
```text
Explain this research paper so that a machine learning researcher who already understands basic ML can understand the main research contribution and methodology.

Structure the response as:
1. Problem
2. Research Gap
3. Proposed Method
4. Dataset
5. Experiments
6. Results
7. Limitations
[Attached Paper Text: Attention Is All You Need]
```

### AI Output Excerpt
> "1. **Problem**: Recurrent models process sequences sequentially, preventing parallelization within training batches.
> 2. **Research Gap**: Existing seq2seq models cannot compute parallel representations across arbitrary distance pairs without $O(n)$ operations.
> 3. **Proposed Method**: Transformer model utilizing Multi-Head Self-Attention, Positional Encodings (sine/cosine functions), and Position-wise Feed-Forward Networks.
> 4. **Dataset**: WMT 2014 English-to-German (4.5M sentence pairs) and WMT 2014 English-to-French (36M sentence pairs).
> 5. **Experiments**: Trained Base (8 heads, $d=512$) and Big (16 heads, $d=1024$) models on 8 NVIDIA P100 GPUs for 12h / 3.5 days.
> 6. **Results**: 28.4 BLEU on En-De (outperforming ensembles by +2.0 BLEU); 41.8 BLEU on En-Fr.
> 7. **Limitations**: High memory consumption $O(n^2)$ for very long sequences."

### What Changed in Prompt
- **Added Layer:** `+ Specific Output Format` (Mandated a 7-section structured schema).

### What Improved in Output
- **Comprehensive Coverage**: Successfully forced the model to extract quantitative experimental configurations (P100 GPUs, 12h training time) and exact dataset sizes (4.5M / 36M pairs) that were completely missing in previous versions.
- **Scannable Layout**: Transformed dense paragraphs into clean, distinct sections ideal for quick technical review.

### What Still Failed in Output
- **Unverified Assertions**: The model added unverified commentary in the limitations section without specifying if the authors explicitly stated it or if it was AI speculation.

### What to Try Next
- Add quality criteria requiring the model to distinguish author-proven claims from external speculation.

---

## 5. Version 4: Quality Criteria

### Exact Prompt
```text
Explain this research paper so that a machine learning researcher who already understands basic ML can understand the main research contribution and methodology.

Structure the response as:
1. Problem
2. Research Gap
3. Proposed Method
4. Dataset
5. Experiments
6. Results
7. Limitations

Use only claims supported by the paper. Clearly distinguish between what the authors demonstrate and your own interpretation. Do not invent missing details or results.
[Attached Paper Text: Attention Is All You Need]
```

### AI Output Excerpt
> "*Author-Demonstrated Claims vs. Interpretation:*
> - **Demonstrated**: The authors demonstrate that scaling dot-product attention by $1/\sqrt{d_k}$ prevents entering regions with small gradients when $d_k$ is large.
> - **Demonstrated**: On En-De, Transformer Big achieves 28.4 BLEU using $3.1 \times 10^{19}$ FLOPs, requiring 1/4 the compute of ByteNet.
> - **Interpretation / Unstated**: The authors do *not* provide empirical benchmarks for sequences $> 512$ tokens; the quadratic memory cost $O(n^2)$ is a theoretical derivation rather than an evaluated experimental limit in this paper."

### What Changed in Prompt
- **Added Layer:** `+ Quality Criteria` (Required strict grounding in paper text and explicit separation of author claims vs. AI interpretation).

### What Improved in Output
- **Epistemic Rigor & Truthfulness**: Prevented the model from blurring the line between empirical benchmark findings and theoretical limits. Explicitly flagged what the paper *did not* test ($>512$ tokens).

### What Still Failed in Output (Friction / Degraded Output)
- **Loss of Conciseness**: The response became excessively cautious, spending over 200 words disclaiming minor nuances rather than summarizing core findings.
- **Missing Source References**: Stated numerical metrics without indicating the exact Table or Section in the paper where a reader could verify them.

### What to Try Next
- Add verification requirements directing the model to cite exact Table/Section locations for numerical metrics while trimming verbose disclaimers.

---

## 6. Version 5: Verification Requirements (Final Reusable Prompt)

### Exact Prompt
```text
Analyze the research paper so that a machine learning researcher who already understands basic ML can evaluate its contribution and methodology.

Structure the response as:
1. Problem
2. Research Gap
3. Proposed Method
4. Dataset
5. Experiments
6. Results (with Table/Section citations)
7. Limitations
8. Potential Research Directions

Use only claims supported by the paper. Clearly distinguish between:
- claims explicitly supported by the paper
- reasonable technical interpretation
- unstated/missing information

Do not invent missing details, citations, datasets, metrics, or results.

For every reported numerical result, identify the exact Table or Section number in the paper so it can be independently verified.
[Attached Paper Text: Attention Is All You Need]
```

### AI Output Excerpt
> "1. **Problem**: Sequential execution in RNNs limits parallelization across training samples (Section 1).
> 2. **Research Gap**: Self-attention models previously lacked positional awareness and multi-head representation alignment (Section 2).
> 3. **Proposed Method**: Transformer architecture using Multi-Head Attention $HEADA_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$ and Sinusoidal Positional Encodings $PE_{(pos, 2i)} = \sin(pos/10000^{2i/d_{\text{model}}})$ (Section 3.2, 3.5).
> 4. **Dataset**: WMT 2014 En-De (4.5M pairs) and En-Fr (36M pairs) tokenized with Byte-Pair Encoding (Section 5.1).
> 5. **Experiments**: Trained on 8 NVIDIA P100 GPUs. Base model: 100k steps (12 hours). Big model: 300k steps (3.5 days) (Section 5.2).
> 6. **Results (Verified)**:
>    - En-De BLEU: **28.4** (Table 2, Row 1 — Transformer Big).
>    - En-Fr BLEU: **41.8** (Table 2, Row 1 — Transformer Big).
>    - Training Cost: $3.1 \times 10^{19}$ FLOPs vs. $1.0 \times 10^{20}$ for ConvS2S (Table 2).
> 7. **Limitations**: Max training sequence length capped at 512 tokens (Table 3).
> 8. **Unstated Info**: No latency benchmarks provided for real-time CPU inference."

### What Changed in Prompt
- **Added Layer:** `+ Verification Requirements` (Required exact Table/Section location tags for all numerical metrics).

### What Improved in Output
- **Auditability**: Every quantitative claim is pinned to an exact location (e.g. Table 2, Row 1), making the analysis independently verifiable within 10 seconds.
- **Optimal Balance**: Successfully combined high technical depth, structured layout, and strict ground-truth verification without returning to ungrounded fluff.

---

## Final Reusable Prompt

```text
Analyze the research paper so that a machine learning researcher who already understands basic ML can evaluate its contribution and methodology.

Structure the response as:
1. Problem
2. Research Gap
3. Proposed Method
4. Dataset
5. Experiments
6. Results (with Table/Section citations)
7. Limitations
8. Potential Research Directions

Use only claims supported by the paper. Clearly distinguish between:
- claims explicitly supported by the paper
- reasonable technical interpretation
- unstated/missing information

Do not invent missing details, citations, datasets, metrics, or results.

For every reported numerical result, identify the exact Table or Section number in the paper so it can be independently verified.
```

---

## Key Learning

The single most effective prompt layer was **Version 3: Specific Output Format** combined with **Version 5: Verification Requirements**. Specifying exact sections forced the model to extract technical metrics it previously skipped, while requiring Table/Section citations prevented hallucinated numbers and produced an independently auditable research summary.
