# lightgbm_191_higher_lr

## Hypothesis
Higher LR with high randomization.

## Candidate Change
0.191 higher: feature 0.515 + LR 0.038/0.033. Higher learning rate.

## CV Metric Summary
- Capped pure premium Gini: 0.1905
- Capped pure premium calibration gap: -0.0095
- Capped pure premium MAE: 218.1175
- Raw pure premium Gini: 0.2072
- Raw pure premium calibration gap: -0.0698
- Runtime seconds: 24.747714

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Faster learning.

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
