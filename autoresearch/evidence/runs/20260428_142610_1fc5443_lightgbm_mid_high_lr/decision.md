# lightgbm_mid_high_lr

## Hypothesis
Balance between high LR and stability.

## Candidate Change
NEW: Mid-high LR (0.048/0.043) with very high min_data. Balance exploration.

## CV Metric Summary
- Capped pure premium Gini: 0.1843
- Capped pure premium calibration gap: -0.0185
- Capped pure premium MAE: 217.1424
- Raw pure premium Gini: 0.199
- Raw pure premium calibration gap: -0.0432
- Runtime seconds: 17.567376

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
| pricing_material_improvement | True |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Mid-high exploration.

## Decision
keep

Gate failures: none

Log truncated: False
