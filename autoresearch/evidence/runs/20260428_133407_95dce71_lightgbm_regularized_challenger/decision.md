# lightgbm_regularized_challenger

## Hypothesis
A constrained LightGBM may improve capped pure premium ranking enough to qualify as a segmentation/research champion while preserving capped calibration and error stability.

## Candidate Change
Regularized LightGBM challenger using constrained leaf counts and moderate L2 penalties for frequency, raw severity, and capped severity.

## CV Metric Summary
- Capped pure premium Gini: 0.1827
- Capped pure premium calibration gap: -0.0145
- Capped pure premium MAE: 217.6245
- Raw pure premium Gini: 0.198
- Raw pure premium calibration gap: -0.0471
- Runtime seconds: 20.102742

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
The existing report showed LightGBM can find segmentation signal, but it is not accepted as a pricing level unless calibration and stability also pass. This candidate intentionally limits flexibility to avoid a black-box gift.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
