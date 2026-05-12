# lightgbm_191_more_rounds

## Hypothesis
More rounds may improve.

## Candidate Change
0.191 more: feature 0.515 / bagging 0.515 + 16/24 + 180 rounds. More boosting rounds.

## CV Metric Summary
- Capped pure premium Gini: 0.1882
- Capped pure premium calibration gap: -0.0125
- Capped pure premium MAE: 217.7946
- Raw pure premium Gini: 0.2074
- Raw pure premium calibration gap: -0.0658
- Runtime seconds: 25.577142

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Test more iterations.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
