# lightgbm_deeper_less_reg

## Hypothesis
Deeper + less reg explores different solution space.

## Candidate Change
NEW: Try deeper trees (17-26) with reduced regularization (L2=5). Opposite of best - see if different optima found.

## CV Metric Summary
- Capped pure premium Gini: 0.1803
- Capped pure premium calibration gap: -0.018
- Capped pure premium MAE: 217.1576
- Raw pure premium Gini: 0.1968
- Raw pure premium calibration gap: -0.0515
- Runtime seconds: 19.207306

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
Opposite direction exploration.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
