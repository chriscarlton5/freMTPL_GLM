# lightgbm_dart_booster

## Hypothesis
DART applies dropout to trees - prevents overfitting from greedy trees. Different optimization path may find new local optimum.

## Candidate Change
NEW HYPOTHESIS: Use DART booster ( dropout + tree) instead of GBDT. Drops trees during training to reduce overfitting.

## CV Metric Summary
- Capped pure premium Gini: 0.1851
- Capped pure premium calibration gap: -0.0098
- Capped pure premium MAE: 218.0687
- Raw pure premium Gini: 0.2004
- Raw pure premium calibration gap: -0.0494
- Runtime seconds: 18.960343

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
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
DART is alternative boosting method. Has different bias-variance tradeoff. Sometimes finds better solutions than GBDT.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
