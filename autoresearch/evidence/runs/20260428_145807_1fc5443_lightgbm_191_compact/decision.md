# lightgbm_191_compact

## Hypothesis
Slightly higher fraction + L2 might beat 0.1908.

## Candidate Change
0.191 compact: feature 0.516 + 16/24 + L2 14.0/12.0. Slightly higher randomization + L2.

## CV Metric Summary
- Capped pure premium Gini: 0.1884
- Capped pure premium calibration gap: -0.0125
- Capped pure premium MAE: 217.7734
- Raw pure premium Gini: 0.2132
- Raw pure premium calibration gap: -0.0656
- Runtime seconds: 25.292964

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
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | True |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Fine-tune attempt.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
