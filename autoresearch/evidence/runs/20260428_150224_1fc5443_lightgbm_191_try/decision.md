# lightgbm_191_try

## Hypothesis
More L2 regularization.

## Candidate Change
0.191 try: feature 0.515 + 16/24 + L2 13.6/11.6. L2 increase again.

## CV Metric Summary
- Capped pure premium Gini: 0.1909
- Capped pure premium calibration gap: -0.0096
- Capped pure premium MAE: 218.1152
- Raw pure premium Gini: 0.2136
- Raw pure premium calibration gap: -0.0657
- Runtime seconds: 25.935998

## Gate Results
| Gate | Passed |
| --- | --- |
| no_policy_leakage | True |
| finite_nonnegative_predictions | True |
| loss_reconciliation | True |
| segmentation_minimum_capped_gini_gain | False |
| segmentation_minimum_fold_agreement | True |
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
Push L2.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
