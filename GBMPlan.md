# GBMPlan.md: LightGBM Comparison for Actuarial Loss Cost Modeling

## Summary

This project extends the existing freMTPL GLM work with a focused LightGBM comparison. The actuarial goal is not to win a generic machine learning benchmark. The goal is to estimate credible annual expected loss cost, or pure premium, while understanding whether a more flexible model improves risk segmentation.

The central question is:

> Does LightGBM add useful signal beyond the GLM benchmark for frequency, severity, pure premium, ranking, calibration, or interaction discovery?

The final comparison should explain whether the extra model complexity is actuarially worth it.

## Objective

The final target is:

```text
expected annual pure premium = expected annual claim frequency * expected claim severity
```

The supporting goals are:

- Rank risks so higher predicted risks show higher observed loss costs.
- Calibrate aggregate predictions so predicted claims and losses are close to observed holdout results.
- Identify nonlinearities and interactions that the GLM may miss.
- Explain whether GBM adds practical value versus the simpler GLM.

## Implementation

- Keep the implementation R-based and LightGBM-only.
- Reuse the existing policy-level train/holdout split, seed, cleanup, predictors, and GLM outputs.
- Train a frequency GBM with a Poisson objective, exposure weighting, and annualized predictions.
- Train raw and 99.5% capped severity GBMs with a Gamma objective on positive claim rows.
- Derive pure premium from frequency times severity. Do not train a separate pure-premium model in v1.
- Keep the holdout set untouched. Use a small validation split inside the training data for early stopping and a small tuning grid.

## Comparison Layer

- Frequency:
  - observed versus predicted claims
  - annual frequency MAE and RMSE
  - calibration by predicted-frequency decile
  - ordered Lorenz/pricing lift Gini
- Severity:
  - raw and capped observed versus predicted mean severity
  - raw and capped MAE and RMSE
  - calibration by predicted-severity decile
  - explicit tail-sensitivity discussion
- Pure premium:
  - aggregate observed loss cost versus predicted loss cost
  - policy-level ranking/lift
  - ordered Lorenz/pricing lift Gini
  - actual versus predicted loss cost by decile

## Model Value Framing

LightGBM is considered useful if it materially improves risk ranking, calibration, or interaction discovery without producing unstable or hard-to-explain results.

The report should say the result plainly:

- If GBM improves frequency but not severity, say that directly.
- If GBM improves metrics only marginally, conclude that GLM remains preferable for simplicity.
- If GBM exposes meaningful nonlinear patterns, present them as feature-engineering insight, not automatically as a production pricing model.

## Interpretation

- Report LightGBM feature importance for frequency, raw severity, and capped severity.
- Add selected partial dependence plots for top features.
- Add simple interaction views for likely actuarial patterns:
  - `DriverAge x CarAge`
  - `Power x Brand`
  - `Region x logDensity`
- Tie every interpretation back to expected claim cost or risk segmentation.

## Deliverables

- `GBMPlan.md`: this implementation plan.
- `mtpl_gbm_analysis.R`: reusable analysis script.
- `mtpl_gbm_report.Rmd`: narrative report comparing GLM and GBM.
- `docs/glm.html`: preserved GLM report.
- `docs/index.html`: GBM comparison report suitable for the portfolio site.
- `README.md`: updated to describe the full GLM-to-GBM modeling story.

## Test Plan

- Confirm the train/holdout split matches the GLM project exactly.
- Verify no policy leakage between train, validation, and holdout.
- Confirm predictions are finite, nonnegative, and annualized correctly.
- Validate pure premium calculations using policy-level total observed loss from `freMTPLsev`.
- Render the GBM report end to end.
- Check that the final report directly answers:
  - Did GBM rank risks better?
  - Did GBM calibrate frequency, severity, and pure premium better?
  - Did GBM reveal meaningful interactions?
  - Is the improvement worth the added complexity?

## Assumptions

- This remains a side-project demonstration of actuarial modeling competency, not a production pricing indication.
- GLM is the benchmark model; GBM is the challenger.
- The success criterion is credible expected loss cost estimation and risk segmentation, not simply the lowest error metric.
- If LightGBM setup becomes nontrivial, pause before switching packages.
