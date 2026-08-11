import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

os.environ["PYTHONIOENCODING"] = "utf-8"

def build_w01_notebook():
    nb = nbformat.v4.new_notebook()
    
    # Cell 0: Title & Header
    c0_md = nbformat.v4.new_markdown_cell(
        "# ML-02 — Research Question and Provisional Lane\n\n"
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        "(https://colab.research.google.com/github/Yuyutsu01/FlyRank/blob/main/work/notebooks/w01_research_question.ipynb?flush_cache=true)\n\n"
        "This notebook establishes the research question, decision framing, data evidence, and technical scope "
        "for the Applied Search Intelligence capstone project."
    )
    
    # Cell 1: Section 1 Markdown
    c1_md = nbformat.v4.new_markdown_cell(
        "## 1. My lane (or freestyle) and why\n\n"
        "**Selected Lane: Lane 2 — Refresh / Content Opportunity Scoring**\n\n"
        "Content decay is one of the highest-leverage operational challenges faced by digital publishers and SEO teams. "
        "As search engine algorithms, competitor content, and user intents evolve over time, existing pages lose organic visibility "
        "and traffic silently. Editorial teams have limited weekly bandwidth and cannot manually audit thousands of published articles. "
        "I selected **Lane 2** because it directly addresses this operational bottleneck: rather than relying on arbitrary manual audits "
        "or naive static age rules (e.g., 'update every article older than 6 months'), we construct a data-driven prioritization model "
        "that scores content decay risks and maps them to transparent, actionable review recommendations."
    )
    
    # Cell 2: Section 1 Code
    c2_code = nbformat.v4.new_code_cell(
        "# --- Section 1: Lane Confirmation ---\n"
        "LANE_NAME = 'Lane 2: Refresh / Content Opportunity Scoring'\n"
        "PRIMARY_GOAL = 'Prioritize content refresh opportunities using machine-learned decline risk and transparent reason codes.'\n\n"
        "print(f'Selected Lane: {LANE_NAME}')\n"
        "print(f'Primary Goal: {PRIMARY_GOAL}')"
    )
    
    # Cell 3: Section 2 Markdown
    c3_md = nbformat.v4.new_markdown_cell(
        "## 2. The question: decision, action, cost of a wrong call\n\n"
        "**Research Question:** *\"Which declining or high-demand content items in a client portfolio should an editorial team "
        "review and refresh first to maximize organic traffic recovery and prevent further decay?\"*\n\n"
        "- **Decision Improved:** Deciding which specific pages to allocate limited weekly editorial, copywriting, and SEO auditing bandwidth to.\n"
        "- **Unit of Analysis:** A single pseudonymized content item (`content_id`) associated with a pseudonymized client portfolio (`client_id`) over a trailing 90-day evaluation window.\n"
        "- **Output:** A prioritized opportunity score (0–100) paired with transparent reason codes (e.g., `stale_visible_page`, `declining_with_demand`, `page_one_decay_risk`, `low_ctr_visible_page`) and recommended editorial review actions.\n"
        "- **Who Acts & Action Taken:** Content Editors, Copywriters, and SEO Managers. They inspect flagged pages, update outdated information, expand thin content sections, or optimize titles/meta descriptions for improved click-through rates.\n"
        "- **Cost of a Wrong Call:**\n"
        "  - *False Positive (recommending a healthy page for refresh)*: Wasted editor hours spent rewriting content that did not need changes, incurring unnecessary labor cost.\n"
        "  - *False Negative (missing a severely declining high-traffic page)*: Sustained loss of organic search impressions and traffic to competitors, leading to compounding revenue loss.\n"
        "- **Why Data / ML Helps:** Static heuristic rules (e.g., 'rewrite all pages older than 180 days') fail because age alone is a weak predictor of traffic loss. ML earns its place by modeling complex non-linear interactions across historical impression volume, ranking position tiers, CTR gaps, and age decay to surface high-impact opportunities that simple rules miss."
    )
    
    # Cell 4: Section 2 Code
    c4_code = nbformat.v4.new_code_cell(
        "# --- Section 2: Problem Framing Specifications ---\n"
        "framing_specs = {\n"
        "    'unit_of_analysis': 'Pseudonymized content item (content_id)',\n"
        "    'decision_improved': 'Weekly editorial refresh priority allocation',\n"
        "    'primary_actor': 'Content Editors & SEO Managers',\n"
        "    'primary_output': 'Ranked Priority Score (0-100) + Reason Codes',\n"
        "    'evaluation_metric': 'Precision@50 on holdout clients',\n"
        "    'false_positive_cost': 'Wasted editorial labor auditing healthy pages',\n"
        "    'false_negative_cost': 'Compounding loss of organic search traffic and revenue'\n"
        "}\n\n"
        "print('=== PROBLEM FRAMING SUMMARY ===')\n"
        "for key, val in framing_specs.items():\n"
        "    print(f'{key.replace(\"_\", \" \").title():<22}: {val}')"
    )
    
    # Cell 5: Section 3 Markdown
    c5_md = nbformat.v4.new_markdown_cell(
        "## 3. Quick look at the data (2-3 real numbers)\n\n"
        "To validate that Lane 2 is worth pursuing over the next 7 weeks, we analyze `data/raw/content_refresh_anonymized.csv` "
        "(30,000 pages across 32 clients) and extract three empirical findings:\n\n"
        "1. **Baseline Traffic Decay Rate**: **16,262 out of 30,000 pages (54.2%)** exhibit a downward traffic trend (`trend_direction == 'down'`). Traffic decay is not an edge case—it affects more than half of the published inventory.\n"
        "2. **High-Demand Vulnerability**: Looking at high-visibility pages ($\ge 500$ 90-day impressions), **3,554 out of 4,874 pages (72.9%)** are in a downward trend. High-traffic assets are disproportionately suffering from decay, representing substantial traffic at risk.\n"
        "3. **Page 1 Click-Through Rate Gap**: For pages ranking on Page 1 (`avg_position` between 1.0 and 10.0), declining pages have a mean CTR of only **0.49%**, whereas growing/stable pages on Page 1 average **0.90%** (nearly **1.8x higher**). This highlights a clear, actionable opportunity: many declining Page 1 pages suffer from snippet or intent mismatch that can be addressed via targeted refreshes."
    )
    
    # Cell 6: Section 3 Code
    c6_code = nbformat.v4.new_code_cell(
        "# --- Section 3: Data Evidence Calculation ---\n"
        "import pandas as pd\n"
        "import numpy as np\n\n"
        "# Load starter dataset\n"
        "df = pd.read_csv('data/raw/content_refresh_anonymized.csv')\n\n"
        "# 1. Total pages & overall decline rate\n"
        "total_pages = len(df)\n"
        "declining_pages = df['trend_direction'].str.lower().eq('down').sum()\n"
        "decline_rate = declining_pages / total_pages\n\n"
        "# 2. High-visibility pages decline rate (impressions_90d >= 500)\n"
        "high_vis_df = df[df['impressions_90d'] >= 500]\n"
        "high_vis_total = len(high_vis_df)\n"
        "high_vis_declining = high_vis_df['trend_direction'].str.lower().eq('down').sum()\n"
        "high_vis_decline_rate = high_vis_declining / high_vis_total\n\n"
        "# 3. Page 1 (avg_position 1-10) mean CTR comparison: Down vs Stable/Up\n"
        "page1_df = df[(df['avg_position'] > 0) & (df['avg_position'] <= 10)]\n"
        "ctr_down = page1_df[page1_df['trend_direction'] == 'down']['ctr'].mean()\n"
        "ctr_stable_up = page1_df[page1_df['trend_direction'].isin(['stable', 'up'])]['ctr'].mean()\n\n"
        "print('=== SUPPORTING DATA EVIDENCE FOR LANE 2 ===')\n"
        "print(f'1. Total Dataset Size         : {total_pages:,} pages across {df[\"client_id\"].nunique()} clients')\n"
        "print(f'   Overall Decline Rate       : {decline_rate:.1%} ({declining_pages:,} pages with trend_direction=\"down\")')\n"
        "print(f'2. High-Visibility Pages (>=500 imp): {high_vis_total:,} pages')\n"
        "print(f'   High-Vis Decline Rate      : {high_vis_decline_rate:.1%} ({high_vis_declining:,} high-traffic pages declining)')\n"
        "print(f'3. Page 1 Mean CTR Comparison  : Declining Pages = {ctr_down:.2f}% vs Stable/Up Pages = {ctr_stable_up:.2f}%')\n"
        "print(f'   CTR Lift Ratio             : {ctr_stable_up / ctr_down:.2f}x higher CTR on non-declining Page 1 pages')"
    )
    
    # Cell 7: Section 4 Markdown
    c7_md = nbformat.v4.new_markdown_cell(
        "## 4. Careful words: what I can and can't claim\n\n"
        "**Careful Boundaries on Technical Claims:**\n\n"
        "- **What I CAN Claim:**\n"
        "  - **Observed Associations**: We measure empirical statistical relationships in historical search performance data (e.g., how position, CTR, and update recency relate to observed traffic trends).\n"
        "  - **Decision-Support Utility**: We demonstrate that machine-learned rankings improve the precision of prioritization ($\text{Precision@50}$) over random sorting or simple hand-written rules.\n"
        "  - **Directional Insights**: We identify high-probability risk factors and candidate cohorts for editorial review.\n\n"
        "- **What I CAN NEVER Claim:**\n"
        "  - **Causal Proof**: Predicting that a page is a good refresh candidate does *not* prove that updating it will cause organic traffic to recover. Causal claims require randomized A/B experiments.\n"
        "  - **Reverse-Engineering Search Algorithms**: We do not claim to discover internal search engine ranking algorithms or secret ranking factors.\n"
        "  - **Guaranteed Outcomes**: We do not claim guaranteed ranking positions or traffic gains for any specific page."
    )
    
    # Cell 8: Section 4 Code
    c8_code = nbformat.v4.new_code_cell(
        "# --- Section 4: Claim Scope Summary ---\n"
        "claim_scope = {\n"
        "    'ALLOWED_CLAIMS': [\n"
        "        'Observed empirical relationships between search signals and traffic trends',\n"
        "        'Decision-support ranking lift (Precision@K) over naive baselines',\n"
        "        'Directional prioritization of content review queues'\n"
        "    ],\n"
        "    'DISALLOWED_CLAIMS': [\n"
        "        'Causal proof that refreshing content guarantees traffic recovery',\n"
        "        'Reverse-engineering Google search ranking algorithms',\n"
        "        'Deterministic guarantees of ranking gains or revenue increases'\n"
        "    ]\n"
        "}\n\n"
        "print('=== CLAIM SCOPE BOUNDARIES ===')\n"
        "print('\\n[ALLOWED CLAIMS]')\n"
        "for claim in claim_scope['ALLOWED_CLAIMS']:\n"
        "    print(f' - {claim}')\n\n"
        "print('\\n[DISALLOWED CLAIMS]')\n"
        "for claim in claim_scope['DISALLOWED_CLAIMS']:\n"
        "    print(f' - {claim}')"
    )
    
    # Cell 9: Self-Check Markdown
    c9_md = nbformat.v4.new_markdown_cell(
        "## Self-check\n\n"
        "Before you submit, confirm each line honestly:\n\n"
        "- [x] Every section above is filled — markdown thinking AND the code that backs it\n"
        "- [x] The notebook runs top to bottom with no errors (Runtime → Run all)\n"
        "- [x] No client names, URLs, or private queries anywhere\n"
        "- [x] My claims use careful words: observed, measured, directional, decision-support\n"
        "- [x] Committed to my repo under `work/notebooks/` — then submit your repo URL on the card. Done."
    )
    
    nb.cells = [c0_md, c1_md, c2_code, c3_md, c4_code, c5_md, c6_code, c7_md, c8_code, c9_md]
    
    nb_path = "work/notebooks/w01_research_question.ipynb"
    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Successfully built {nb_path}.")

def execute_w01_notebook():
    nb_path = "work/notebooks/w01_research_question.ipynb"
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": "."}})
    
    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Successfully executed and saved outputs for {nb_path}.")

if __name__ == "__main__":
    build_w01_notebook()
    execute_w01_notebook()
