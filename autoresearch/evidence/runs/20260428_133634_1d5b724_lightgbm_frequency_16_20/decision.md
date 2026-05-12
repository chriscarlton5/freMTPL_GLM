# lightgbm_frequency_16_20

## Hypothesis
Best run had 14,22 leaves at 0.1845 Gini. Try 16,20 leaves for even more granular frequency splits.

## Candidate Change
LightGBM with exact params from best run (14,22 leaves) but with frequency at (16,20) to see if 16 leaves helps.

## CV Metric Summary
- Capped pure premium Gini: 0.1841
- Capped pure premium calibration gap: -0.0146
- Capped pure premium MAE: 217.5943
- Raw pure premium Gini: 0.2008
- Raw pure premium calibration gap: -0.0484
- Runtime seconds: 19.082345

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
Fine-tuning leaf counts is standard. Keep balanced regularization.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain

Log truncated: False
