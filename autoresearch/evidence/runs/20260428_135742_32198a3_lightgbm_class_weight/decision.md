# lightgbm_class_weight

## Hypothesis
Class imbalance hurts minority class prediction. scale_pos_weight balances the dataset. Standard technique for imbalanced classification.

## Candidate Change
NEW HYPOTHESIS: Frequency has class imbalance (only ~3.5% have claims). Use scale_pos_weight to give more weight to claim events.

## CV Metric Summary
- Capped pure premium Gini: 0.1851
- Capped pure premium calibration gap: -0.0098
- Capped pure premium MAE: 218.0687
- Raw pure premium Gini: 0.2004
- Raw pure premium calibration gap: -0.0494
- Runtime seconds: 18.6932

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
Claim events are rare (~3.5%). Weighting them helps the model focus on predicting risk drivers. Standard ML practice.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain

Log truncated: False
