# lightgbm_less_regularized

## Hypothesis
Too much regularization suppresses signal. Earlier runs at L2=10 hit 0.184+. Try L2=4-7 to find more signal while keeping some regularization.

## Candidate Change
LightGBM with reduced L2 (4-7 vs 10) to capture more signal. Less constrained trees may find better patterns.

## CV Metric Summary
- Capped pure premium Gini: 0.1792
- Capped pure premium calibration gap: -0.0152
- Capped pure premium MAE: 217.5206
- Raw pure premium Gini: 0.1919
- Raw pure premium calibration gap: -0.0542
- Runtime seconds: 18.695791

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
| pricing_transparent_model_or_documented_blend | False |
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Reduced L2 for less constrained fit. Still uses early stopping and bagging to prevent overfitting. Standard tuning practice.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
