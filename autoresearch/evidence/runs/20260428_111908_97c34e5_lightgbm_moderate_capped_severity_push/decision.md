# lightgbm_moderate_capped_severity_push

## Hypothesis
The flexible capped-severity run improved two folds but not enough on mean Gini, while the aggressive run lifted mean Gini mostly through fold 3. A moderate capped-severity grid may increase mean capped Gini without sacrificing fold 1 or fold 2.

## Candidate Change
LightGBM challenger that preserves the current frequency and raw severity grids while adding moderate capped-severity flexibility between the prior flexible and aggressive attempts.

## CV Metric Summary
- Capped pure premium Gini: 0.1808
- Capped pure premium calibration gap: -0.0228
- Capped pure premium MAE: 216.7784
- Raw pure premium Gini: 0.198
- Raw pure premium calibration gap: -0.0471
- Runtime seconds: 19.941388

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
This is segmentation research only. It keeps the more stable frequency signal fixed and tests whether capped severity can add controlled lift without creating an unsupported black-box severity artifact.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
