# lightgbm_frequency_focused

## Hypothesis
Frequency drives ranking Gini. Previous run showed best Gini on folds 1 & 3. More frequency flexibility should push total Gini past 0.005 gain threshold while keeping calibration in check.

## Candidate Change
LightGBM focused on frequency flexibility (primary driver of Gini). More aggressive frequency grid while keeping severity regularized. Target: clear the 0.005 Gini delta threshold.

## CV Metric Summary
- Capped pure premium Gini: 0.1818
- Capped pure premium calibration gap: -0.012
- Capped pure premium MAE: 217.8381
- Raw pure premium Gini: 0.1946
- Raw pure premium calibration gap: -0.0365
- Runtime seconds: 18.248324

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
Frequency-focused LightGBM is standard actuarial practice - severity has high variance, so we regularize there. Frequency drives ranking. Documentation: all hyperparameters, methodology, and validation results.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
