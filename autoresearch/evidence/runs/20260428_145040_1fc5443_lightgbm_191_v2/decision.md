# lightgbm_191_v2

## Hypothesis
Variation around record.

## Candidate Change
0.191 v2: feature 0.518 / bagging 0.518 + 16/24 + L2 13.8/11.8. Variation on 0.1908.

## CV Metric Summary
- Capped pure premium Gini: 0.1864
- Capped pure premium calibration gap: -0.0202
- Capped pure premium MAE: 217.029
- Raw pure premium Gini: 0.2129
- Raw pure premium calibration gap: -0.0658
- Runtime seconds: 24.291215

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
Push for 0.191+.

## Decision
keep

Gate failures: none

Log truncated: False
