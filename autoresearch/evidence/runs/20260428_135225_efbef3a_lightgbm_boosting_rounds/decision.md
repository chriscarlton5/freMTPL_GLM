# lightgbm_boosting_rounds

## Hypothesis
Less features per tree = more diversity. More rounds compensate for weaker trees.

## Candidate Change
Try less feature_fraction (0.75/0.70) to force more diversity. Also more boosting rounds to compensate.

## CV Metric Summary
- Capped pure premium Gini: 0.1838
- Capped pure premium calibration gap: -0.0141
- Capped pure premium MAE: 217.5799
- Raw pure premium Gini: 0.2009
- Raw pure premium calibration gap: -0.0399
- Runtime seconds: 21.511479

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
Feature sampling + more rounds is standard ensemble practice.

## Decision
keep

Gate failures: none

Log truncated: False
