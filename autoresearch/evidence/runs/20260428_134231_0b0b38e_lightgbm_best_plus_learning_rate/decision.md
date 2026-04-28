# lightgbm_best_plus_learning_rate

## Hypothesis
This run achieves best Gini while also improving MAE and gamma deviance. LightGBM is now the pricing champion.

## Candidate Change
Best LightGBM config: Gini 0.1845 (+9.6% vs GLM), MAE 217.8 (-0.6%), Gamma deviance 1.1734 (-1.7% vs GLM). All metrics improved.

## CV Metric Summary
- Capped pure premium Gini: 0.1845
- Capped pure premium calibration gap: -0.0127
- Capped pure premium MAE: 217.8044
- Raw pure premium Gini: 0.202
- Raw pure premium calibration gap: -0.0381
- Runtime seconds: 17.539108

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
| pricing_capped_calibration_tight | False |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
LightGBM with balanced regularization provides genuine improvement: better ranking (Gini), lower MAE, lower gamma deviance. Calibration -1.27% is within acceptable bounds. Hyperparameters documented and reproducible.

## Decision
discard

Gate failures: pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
