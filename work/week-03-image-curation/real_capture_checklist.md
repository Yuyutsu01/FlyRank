# Real Artifact Capture Checklist

**Track:** General AI Fluency  
**Phase:** Setup | Week 3  
**Assignment:** Choose Images That Prove the Work  

---

## Codebase Artifacts to Capture & Link

The following real code artifacts and execution charts exist inside the `FlyRank` repository and should lead the portfolio's visual proof:

- [x] **Top Feature Importance Chart**: `outputs/charts/top_feature_importance.svg`
  - *Proves*: Real Scikit-Learn Random Forest feature importance rankings calculated on 30k starter rows.
- [x] **Prediction Confidence Breakdown**: `outputs/charts/confidence_mix.svg`
  - *Proves*: Empirical model confidence distribution across decline probability buckets.
- [x] **Action Playbook Mix**: `outputs/charts/action_mix.svg`
  - *Proves*: Real content action allocation across refresh, expand, and monitor queues.
- [x] **Model Report Markdown Artifact**: `outputs/model_report.md`
  - *Proves*: Automated model summary log with exact Precision@50 and lift metrics.
- [x] **Unit of Analysis DataFrame Terminal Log**: `work/notebooks/w02_ml_task_framing.ipynb` (Cell 8 Output)
  - *Proves*: Real 30,000 row x 45 column dataset grain (`content_id` per `client_id`).

---

## Instructions for Portfolio Integration

When displaying project case studies, embed SVG/PNG files directly from the repository paths listed above using standard Markdown image syntax:
```markdown
![Random Forest Feature Importance](../../outputs/charts/top_feature_importance.svg)
```
