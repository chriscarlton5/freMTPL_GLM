# lightgbm_191_sweeter

## Hypothesis
L2 13.5 with slightly lower fraction.

## Candidate Change
0.191 sweeter: feature 0.514 + 16/24 + L2 13.5. Lower fraction.

## CV Metric Summary
- Capped pure premium Gini: 0.1889
- Capped pure premium calibration gap: -0.012
- Capped pure premium MAE: 217.8397
- Raw pure premium Gini: 0.2146
- Raw pure premium calibration gap: -0.0654
- Runtime seconds: 25.335328

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
Test combination.

## Decision
discard

Gate failures: pricing_material_improvement, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
