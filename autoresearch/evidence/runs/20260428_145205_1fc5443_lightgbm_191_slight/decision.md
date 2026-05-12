# lightgbm_191_slight

## Hypothesis
Different leaves.

## Candidate Change
0.191 slight: feature 0.513 / bagging 0.513 + 15/23 + L2 13.0/11.0. Slight leaf reduction.

## CV Metric Summary
- Capped pure premium Gini: 0.1827
- Capped pure premium calibration gap: -0.0221
- Capped pure premium MAE: 216.8009
- Raw pure premium Gini: 0.2143
- Raw pure premium calibration gap: -0.0661
- Runtime seconds: 25.441717

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
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Check 15/23.

## Decision
discard

Gate failures: pricing_capped_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
