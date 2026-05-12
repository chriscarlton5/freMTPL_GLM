# lightgbm_frequency_deeper

## Hypothesis
Frequency is the main Gini driver. Previous best was at 14-22 leaves. Try 16-24 to see if more capacity helps.

## Candidate Change
LightGBM with more leaves on frequency (16-24), regular severity (6-10). Frequency drives Gini - give it more capacity.

## CV Metric Summary
- Capped pure premium Gini: 0.1842
- Capped pure premium calibration gap: -0.0146
- Capped pure premium MAE: 217.6002
- Raw pure premium Gini: 0.2003
- Raw pure premium calibration gap: -0.0483
- Runtime seconds: 19.104536

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
Focus capacity where signal is strongest - standard practice. Severity keeps regularization.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
