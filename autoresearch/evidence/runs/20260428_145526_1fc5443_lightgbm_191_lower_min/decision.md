# lightgbm_191_lower_min

## Hypothesis
Lower min allows more complexity.

## Candidate Change
0.191 lower: feature 0.515 + lower min_data (1750/1450). More flexibility.

## CV Metric Summary
- Capped pure premium Gini: 0.1859
- Capped pure premium calibration gap: -0.0178
- Capped pure premium MAE: 217.2814
- Raw pure premium Gini: 0.207
- Raw pure premium calibration gap: -0.0675
- Runtime seconds: 25.602479

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
Test complexity.

## Decision
discard

Gate failures: pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
