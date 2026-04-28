# lightgbm_shorter_midleaf_stronger_capped

## Hypothesis
Longer boosting around the strongest near miss improved MAE but lost ranking. A shorter budget may stop before the model shifts away from the capped Gini signal.

## Candidate Change
LightGBM challenger using the strongest mid-leaf frequency plus stronger capped-severity near-miss grids with a shorter early-stopped boosting budget.

## CV Metric Summary
- Capped pure premium Gini: 0.1847
- Capped pure premium calibration gap: -0.0161
- Capped pure premium MAE: 217.4537
- Raw pure premium Gini: 0.1965
- Raw pure premium calibration gap: -0.0453
- Runtime seconds: 19.304759

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
This is a segmentation-only sensitivity test. It should advance only if the capped Gini improvement clears the predefined gate across at least two folds without calibration or error deterioration.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
