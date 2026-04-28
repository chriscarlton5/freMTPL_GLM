# lightgbm_midleaf_stronger_capped_raw_severity_push

## Hypothesis
The best capped segmentation near miss already passes raw Gini monitoring. A slightly broader raw-severity grid may improve raw pure premium monitoring without changing the capped ranking path.

## Candidate Change
LightGBM challenger using the strongest mid-leaf frequency and stronger capped-severity near-miss grids, with an added raw-severity option for monitoring lift.

## CV Metric Summary
- Capped pure premium Gini: 0.1875
- Capped pure premium calibration gap: -0.0152
- Capped pure premium MAE: 217.4857
- Raw pure premium Gini: 0.194
- Raw pure premium calibration gap: -0.0473
- Runtime seconds: 24.690594

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is segmentation research only. The raw-severity option is useful only if it improves monitoring without weakening capped stability.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
