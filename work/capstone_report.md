# Capstone Report — Ranking Signal Analysis & Content Opportunity Scoring

- **Author:** Shivam Sharma
- **Lane:** Ranking Signal Analysis
- **Repo:** https://github.com/Yuyutsu01/FlyRank
- **Date:** September 2026
- **Deployed Paper URL:** https://yuyutsu01.github.io/FlyRank/capstone/

---

## 0. Abstract

Modern search visibility optimization faces severe editorial resource bottlenecks, where content teams must decide which decaying assets justify intensive refresh engineering. Using the FlyRank internship dataset (spanning 30,000 anonymized content records across 32 client domains), we examine which pre-period search and engagement signals correlate with organic traffic decay. We implement an honest client-holdout evaluation (`GroupShuffleSplit` across client portfolios) and train a depth-constrained Random Forest model against a transparent heuristic baseline. The learned model achieves a `Precision@50 = 0.780` compared to `0.220` for the baseline rule, generating a 3.55x lift in identifying genuinely declining content assets. These directional findings demonstrate that search exposure volume, ranking position slippage, and CTR gaps serve as robust leading indicators for editorial prioritization.

---

## 1. Problem Framing

Organic search traffic represents the primary acquisition channel for high-authority digital publications, yet search engine results pages (SERPs) are volatile. Editorial teams face a constant prioritization trade-off: **which existing URLs should receive engineering and content refreshes, and which should be left alone?**

- **Unit of Analysis**: One row per unique content item (`content_id`), aggregated over trailing 90 days.
- **Output**: Calibrated risk probability $p \in [0, 1]$ estimating whether organic traffic will decay, translated into a prioritized Top-K refresh queue.
- **Action Supported**: Allocating copywriters, technical SEOs, and UX designers to decaying high-impact pages.
- **Cost of Misallocation**: High opportunity cost. Refreshing stable evergreen pages wastes scarce human hours; ignoring high-exposure decaying URLs results in compounding traffic and revenue losses.

---

## 2. Data Safety & Warehouse Inventory

### Warehouse Inventory
- Full warehouse release (`hf://datasets/FlyRank/internship-warehouse`, build v20260703):
  - `dim_clients` (104 rows): Pseudonymized client domain metadata.
  - `dim_content` (519,606 rows): Content records.
  - `fact_content_daily_performance` (78,835,655 rows, daily grain across ~17 months).
  - `fact_content_daily_performance_sample` (~11.7M rows): June 2026 sealed holdout.
  - `fact_content_query_90d` (2,414,248 rows): Search query performance.

### Analysis Dataset (`data/raw/content_refresh_anonymized.csv`)
- **Sample Size**: 30,000 content items across 32 client domains.
- **Date Window**: Pre-period 90-day aggregation window.
- **Deliberate Exclusions**:
  - `trend_pct` and `trend_direction`: Excluded from feature inputs $X$ because they encode the post-period outcome window (100% target leakage).
  - Sealed Test Month (`2026-06`): Excluded from model development.
  - Client names, actual URLs, and search query strings: Scrubbed to guarantee public safety.

---

## 3. Baseline Formulation

We established a transparent, explainable heuristic baseline scoring rule prior to training any learned model:
$$\text{Score}_{\text{baseline}} = \log(1 + \text{impressions}_{90d}) \times \left(\frac{\text{days\_since\_last\_update}}{100}\right) \times \left(1 + \frac{\text{avg\_position}}{10}\right)$$

- **Rationale**: Multiplies search exposure by content staleness and rank tier.
- **Baseline Performance on Test Split**:
  - `Precision@10`: 0.200
  - `Precision@20`: 0.200
  - `Precision@50`: **0.220** (worse than the 0.517 random base rate because it over-indexes on stable evergreen documentation).

---

## 4. Model & Feature Engineering

### Decision-Time Feature Matrix ($X$)
1. `impressions_90d`: Historical 90-day search exposure volume.
2. `avg_position`: Mean SERP position.
3. `ctr_gap`: Expected CTR for ranking position ($1.0 / (\text{pos} + 1)$) minus observed CTR (clipped at 0.0).
4. `days_since_last_update`: Days elapsed since last content modification.
5. `word_count`: Document length (median-imputed).

### Model Choice: Random Forest Classifier
- **Configuration**: `n_estimators=100`, `max_depth=6`, `random_state=42`.
- **Pipeline**: Encapsulated with `SimpleImputer(strategy='median')` to prevent leakage.
- **Why It Fits**: Captures non-linear feature interactions (e.g. high impressions combined with position drop) without requiring manual cross-products, while depth constraint prevents overfitting.

---

## 5. Evaluation Design & Results

### Grouped Split Design
- `GroupShuffleSplit` on `client_id` (75% train / 25% test, `random_state=42`).
- **Train Set**: 22,885 rows (24 clients).
- **Test Set**: 7,115 rows (8 held-out clients).
- **Zero Client Leakage**: Zero client overlap; evaluates generalization to unseen domains.

### Primary Benchmark Comparison Table

| System | Precision@10 | Precision@20 | Precision@50 (Primary) | Lift over Baseline |
|---|---:|---:|---:|---:|
| **Dataset Base Rate** | 0.517 | 0.517 | 0.517 | *N/A* |
| **Week-4 Baseline Rule** | 0.200 | 0.200 | 0.220 | **1.00x** (Baseline) |
| **Logistic Regression** | 0.600 | 0.650 | 0.680 | **3.09x** (+0.460) |
| **Random Forest (Champion)** | **1.000** | **0.850** | **0.780** | **3.55x (+0.560)** |

---

## 6. Interpretation & Signal Hierarchy

1. `impressions_90d` (**35.8%**): High-exposure assets face the highest competitive volatility.
2. `avg_position` (**23.5%**): Rank slippage directly triggers traffic loss.
3. `word_count` (**17.9%**): Thin content exhibits weaker topical resilience.
4. `ctr_gap` (**16.1%**): SERP snippet underperformance indicates intent mismatch.
5. `days_since_last_update` (**6.7%**): Content age is the weakest single predictor.

---

## 7. Ranked Recommendations (Action Playbook)

1. **Priority 1: High-Exposure Position Decay URLs** (`impressions_90d > 1,000` & `avg_position` between 3.0–10.0). Immediate content refresh and intent alignment.
2. **Priority 2: SERP Snippet Optimization for Top-5 Ranks** (`ctr_gap > 0.15` despite rank 1–5). Title tag and meta description overhaul.
3. **Priority 3: Thin Content Expansion** (`word_count < 600`). Expand coverage of secondary queries.
4. **Anti-Recommendation**: Do NOT refresh URLs based solely on age (`days_since_last_update`).

---

## 8. Limitations & Reproducibility

- **Limitations**: Observational, non-causal associations; 90-day aggregate snapshot ignores intra-month seasonality; zero claims regarding Google's proprietary algorithm mechanics.
- **Reproducibility**: Run `work/notebooks/capstone.ipynb` top-to-bottom (`random_state=42`).
- **Acknowledgments**: Built on the FlyRank ML Internship dataset (https://flyrank.ai).
