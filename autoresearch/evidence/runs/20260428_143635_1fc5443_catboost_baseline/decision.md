# catboost_baseline

## Hypothesis
CatBoost's ordered boosting may perform differently on freMTPL.

## Candidate Change
CatBoost instead of LightGBM. Different gradient boosting algorithm. May find different patterns.

## CV Metric Summary
- Capped pure premium Gini: 0.1377
- Capped pure premium calibration gap: 0.002
- Capped pure premium MAE: 219.6371
- Raw pure premium Gini: 0.1423
- Raw pure premium calibration gap: 0.0088
- Runtime seconds: 15.324305

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
| pricing_capped_gini_not_materially_worse | False |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Alternative algorithm exploration.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_gini_not_materially_worse, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement, segmentation_raw_gini_not_materially_worse

Log truncated: False
