# lightgbm_expanded_regularized_grid

## Hypothesis
The aggressive capped-severity run improved fold 3 but hurt folds 1 and 2. Keeping champion options in the grid while adding conservative alternatives may allow fold-specific inner validation to improve capped pure premium Gini without sacrificing fold agreement.

## Candidate Change
Regularized LightGBM challenger with an expanded inner-validation grid. It keeps the current champion settings available while adding more conservative frequency options and previously useful capped severity options.

## CV Metric Summary
- Capped pure premium Gini: 0.182
- Capped pure premium calibration gap: -0.0142
- Capped pure premium MAE: 217.578
- Raw pure premium Gini: 0.1976
- Raw pure premium calibration gap: -0.0385
- Runtime seconds: 28.54748

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
This remains a segmentation/research candidate only. The broader grid is still constrained by minimum leaf sizes, feature/bagging fractions, and L2 regularization so that any gain is less likely to be a sparse black-box artifact.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
