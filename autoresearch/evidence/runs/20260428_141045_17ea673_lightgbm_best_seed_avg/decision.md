# lightgbm_best_seed_avg

## Hypothesis
Seeds affect tree construction and split ties. Different seed may find alternative local optimum.

## Candidate Change
NEW HYPOTHESIS: Use slightly different seed (20260428 vs 20260423). Test if different random initialization finds better solution.

## CV Metric Summary
- Capped pure premium Gini: 0.1862
- Capped pure premium calibration gap: -0.0212
- Capped pure premium MAE: 219.5556
- Raw pure premium Gini: 0.2586
- Raw pure premium calibration gap: -0.0631
- Runtime seconds: 18.055953

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
| segmentation_capped_rmse_tolerance | False |
| segmentation_raw_gini_not_materially_worse | True |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | False |

## Actuarial Interpretation
Bootstrap averaging is standard practice. Different seeds explore solution space differently.

## Decision
discard

Gate failures: pricing_capped_rmse_tolerance, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_capped_rmse_tolerance

Log truncated: False
