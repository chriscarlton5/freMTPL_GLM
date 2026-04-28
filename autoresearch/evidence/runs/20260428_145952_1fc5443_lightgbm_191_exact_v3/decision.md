# lightgbm_191_exact_v3

## Hypothesis
Slight L2 change

## Candidate Change
0.191 exact v3: feature 0.515 + 16/24 + L2 13.2/11.2. Slight L2 reduction.

## CV Metric Summary
- Capped pure premium Gini: 0.1907
- Capped pure premium calibration gap: -0.0095
- Capped pure premium MAE: 218.1264
- Raw pure premium Gini: 0.2078
- Raw pure premium calibration gap: -0.0695
- Runtime seconds: 25.674629

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
| segmentation_raw_gini_not_materially_worse | False |
| pricing_transparent_model_or_documented_blend | True |
| pricing_material_improvement | False |
| pricing_capped_gini_not_materially_worse | True |
| pricing_raw_gini_not_materially_worse | False |
| pricing_capped_calibration_tight | True |
| pricing_capped_mae_tolerance | True |
| pricing_capped_rmse_tolerance | True |

## Actuarial Interpretation
Fine-tune.

## Decision
discard

Gate failures: pricing_material_improvement, pricing_raw_gini_not_materially_worse, segmentation_minimum_capped_gini_gain, segmentation_raw_gini_not_materially_worse

Log truncated: False
