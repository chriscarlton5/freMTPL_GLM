# lightgbm_15_24_low_lr

## Hypothesis
Lower LR + more trees might help.

## Candidate Change
15/24 with lower LR (0.038/0.033). More boosting rounds.

## CV Metric Summary
- Capped pure premium Gini: 0.18
- Capped pure premium calibration gap: -0.0177
- Capped pure premium MAE: 217.1955
- Raw pure premium Gini: 0.1963
- Raw pure premium calibration gap: -0.0552
- Runtime seconds: 21.21061

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
Slower learning.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
