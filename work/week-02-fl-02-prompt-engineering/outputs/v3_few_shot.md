# Version 3 — Few-Shot Examples

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

Now analyze the following research paper using a similar level of specificity:

[Attached Paper Text: Attention Is All You Need by Vaswani et al., 2017]
```

### Actual AI Output Excerpt
> "Problem: The authors investigate whether self-attention mechanisms alone can replace recurrent and convolutional networks for sequence transduction tasks.
> Method: They compare the Transformer (Base and Big variants) against recurrent baselines (GNMT, Deep-Att) and convolutional baselines (ConvS2S, ByteNet) using the WMT 2014 English-to-German and English-to-French datasets.
> Result: The Transformer Big model improves English-to-German BLEU to 28.4 (+2.0 BLEU over the best ensemble) while requiring $3.1 \times 10^{19}$ FLOPs (1/4 the compute of ByteNet).
> Limitation: The evaluation is limited because the model relies on static sinusoidal positional encodings that do not generalize natively to sequence lengths longer than those observed during training."

### What Changed in Prompt
- **Added Technique:** `Few-Shot Examples` (Provided a 4-line exemplar showing Problem/Method/Result/Limitation framing).

### Observed Change in Output
- **High Conciseness & Precision**: Output immediately adopted the exact 4-part concise structural pattern from the example, extracting exact FLOP numbers ($3.1 \times 10^{19}$) and baseline model names (GNMT, ConvS2S, ByteNet).

### Why It Mattered
- Few-shot prompting anchors the output format and density without needing complex prose instructions, proving that examples communicate formatting intent faster than descriptions.

### What Still Failed
- **Incomplete Research Scope**: The 4-line exemplar was too brief; it omitted dedicated sections for Research Gap, Hardware Setup, and Future Research Directions.

### What to Try Next
- Add an explicit 8-section output structure to enforce complete coverage across all research dimensions.
