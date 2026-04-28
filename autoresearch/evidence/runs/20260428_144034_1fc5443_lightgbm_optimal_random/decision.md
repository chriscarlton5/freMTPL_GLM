# lightgbm_optimal_random

## Hypothesis
Fine-tune the winning randomization config.

## Candidate Change
Optimal randomization: feature 0.58 / bagging 0.58 + 16/25 leaves. Fine-tune around 0.1874 winner.

## CV Metric Summary
- Capped pure premium Gini: 0.1831
- Capped pure premium calibration gap: -0.0215
- Capped pure premium MAE: 216.8669
- Raw pure premium Gini: 0.1999
- Raw pure premium calibration gap: -0.0379
- Runtime seconds: 24.425828

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | False |
| segmentation_capped_calibration_tolerance | True |
| segmentation_capped_mae_tolerance | True |
| segmentation_capped_rmse_tolerance | True |
| segmentation_raw_gini_not_materially_worse | True |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Refine best configuration.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
