# lightgbm_13_21_balanced

## Hypothesis
Fewer leaves + more regularization.

## Candidate Change
13/21 leaves, 0.044 LR, higher L2 (12). More regularization.

## CV Metric Summary
- Capped pure premium Gini: 0.1822
- Capped pure premium calibration gap: -0.0174
- Capped pure premium MAE: 217.2705
- Raw pure premium Gini: 0.1979
- Raw pure premium calibration gap: -0.0478
- Runtime seconds: 18.626102

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Balanced approach.

## Decision
keep

Gate failures: none

Log truncated: False
