import os
import sys
import json
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

os.environ["PYTHONIOENCODING"] = "utf-8"

def update_notebook_01():
    nb_path = "notebooks/01_first_look_and_discovery.ipynb"
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Locate the cell with id 9d8af43b or '# Your discovery here'
    for cell in nb.cells:
        if cell.cell_type == "code" and ("# Your discovery here" in "".join(cell.source) or cell.id == "9d8af43b"):
            cell.source = [
                "# --- Your Turn Discovery: Multi-Angle Analysis ---\n",
                "\n",
                "# Concept: We test three common SEO assumptions using the dataset:\n",
                "# 1. Does filtering for active pages (impressions_90d > 0) improve search volume correlation?\n",
                "# 2. How does CTR vary by content_type in top position tiers?\n",
                "# 3. Does page age (content_age_days) differ between declining ('down') vs growing ('up') pages?\n",
                "\n",
                "# 1. Active pages search volume correlation check\n",
                "active_pages = df[df[\"impressions_90d\"] > 0]\n",
                "corr_active = active_pages[\"search_volume\"].corr(active_pages[\"impressions_90d\"])\n",
                "print(f\"Correlation (impressions > 0): {corr_active:.3f}\")\n",
                "print(\"-> Even for active pages, search volume barely predicts actual traffic received.\\n\")\n",
                "\n",
                "# 2. CTR by content_type in top_3 position tier\n",
                "top3_pages = df[df[\"position_tier\"] == \"top_3\"]\n",
                "ctr_by_type = top3_pages.groupby(\"content_type\")[\"ctr\"].agg([\"mean\", \"median\", \"count\"])\n",
                "print(\"Mean CTR by Content Type in top_3 position tier:\")\n",
                "print(ctr_by_type.round(4))\n",
                "print()\n",
                "\n",
                "# 3. Content age vs trend direction\n",
                "age_by_trend = df.groupby(\"trend_direction\")[\"content_age_days\"].agg([\"median\", \"mean\", \"count\"])\n",
                "print(\"Content Age (Days) by Trend Direction:\")\n",
                "print(age_by_trend.round(1))\n",
                "print(\"-> Observed: Declining ('down') pages have a lower median age (216 days) than growing ('up') pages (291.5 days).\")\n"
            ]
            break

    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Updated {nb_path} with discovery cell code.")

def update_notebook_02():
    nb_path = "notebooks/02_your_first_readable_model.ipynb"
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    for cell in nb.cells:
        if cell.cell_type == "code" and ("# Your experiment here" in "".join(cell.source) or cell.id == "5e35d2e0"):
            cell.source = [
                "# --- Your Turn Experiment: Tree Depth & Honest Client-Holdout Validation ---\n",
                "\n",
                "# Concept:\n",
                "# 1. We test if expanding tree depth from 2 to 3 improves Precision@50.\n",
                "# 2. We perform an honest client-level holdout validation (GroupShuffleSplit on client_id)\n",
                "#    to verify that model performance holds on unseen clients without page leakage across splits.\n",
                "\n",
                "from sklearn.tree import DecisionTreeClassifier, export_text\n",
                "from sklearn.model_selection import GroupShuffleSplit\n",
                "\n",
                "# 1. Depth-3 Tree In-Sample\n",
                "features = [\"content_age_days\", \"days_since_last_update\", \"impressions_90d\", \"avg_position\", \"ctr\", \"word_count\"]\n",
                "X = df[features].replace([np.inf, -np.inf], np.nan).fillna(0)\n",
                "y = df[\"is_declining_label\"].values\n",
                "\n",
                "tree_d3 = DecisionTreeClassifier(max_depth=3, class_weight=\"balanced\", random_state=42)\n",
                "tree_d3.fit(X, y)\n",
                "\n",
                "p50_d2 = precision_at_k(tree.predict_proba(X)[:, 1], y, 50)\n",
                "p50_d3 = precision_at_k(tree_d3.predict_proba(X)[:, 1], y, 50)\n",
                "print(f\"In-sample Precision@50 -> Depth 2: {p50_d2:.3f} | Depth 3: {p50_d3:.3f}\")\n",
                "\n",
                "# 2. Client-Holdout Train/Test Split (20% holdout clients)\n",
                "gss = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)\n",
                "train_idx, test_idx = next(gss.split(X, y, groups=df[\"client_id\"]))\n",
                "\n",
                "X_train, y_train = X.iloc[train_idx], y[train_idx]\n",
                "X_test, y_test = X.iloc[test_idx], y[test_idx]\n",
                "\n",
                "# Train model on train clients only\n",
                "tree_holdout = DecisionTreeClassifier(max_depth=3, class_weight=\"balanced\", random_state=42)\n",
                "tree_holdout.fit(X_train, y_train)\n",
                "\n",
                "# Evaluate hand rule vs depth-3 tree on test clients\n",
                "stale_test = (df.iloc[test_idx][\"days_since_last_update\"] >= 180).astype(int)\n",
                "visible_test = (df.iloc[test_idx][\"impressions_90d\"] >= 500).astype(int)\n",
                "hand_rule_test = stale_test * visible_test * df.iloc[test_idx][\"impressions_90d\"]\n",
                "\n",
                "hr_test_p50 = precision_at_k(hand_rule_test, y_test, 50)\n",
                "tree_test_p50 = precision_at_k(tree_holdout.predict_proba(X_test)[:, 1], y_test, 50)\n",
                "\n",
                "print(f\"\\nClient Holdout Split Evaluation (Test Set):\")\n",
                "print(f\"Hand Rule Precision@50 : {hr_test_p50:.3f}\")\n",
                "print(f\"Depth-3 Tree Precision@50: {tree_test_p50:.3f}\")\n",
                "\n",
                "print(\"\\nReadable Depth-3 Decision Tree Rules:\")\n",
                "print(export_text(tree_holdout, feature_names=features))\n"
            ]
            break

    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Updated {nb_path} with experiment cell code.")

def run_notebook(nb_path):
    print(f"\n--- Running {nb_path} top to bottom ---")
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    # Set execution path to root
    ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})
    
    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Successfully executed and saved outputs for {nb_path}.")

if __name__ == "__main__":
    update_notebook_01()
    update_notebook_02()
    run_notebook("notebooks/01_first_look_and_discovery.ipynb")
    run_notebook("notebooks/02_your_first_readable_model.ipynb")
