# lightgbm_15_24_v2

## Hypothesis
Reproduce champion.

## Candidate Change
15/24 leaves exactly as best, but 0.04/0.035 + L2 8-9. Same as champion.

## CV Metric Summary
- Capped pure premium Gini: 0.1809
- Capped pure premium calibration gap: -0.0147
- Capped pure premium MAE: 217.5288
- Raw pure premium Gini: 0.196
- Raw pure premium calibration gap: -0.0571
- Runtime seconds: 18.655435

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
Verify best config.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
