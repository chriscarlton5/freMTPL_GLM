# lightgbm_frequency_ranking_push

## Hypothesis
Prior capped-severity flexibility mainly helped fold 3. A controlled frequency-ranking push may improve capped pure premium Gini across at least two folds without worsening capped MAE or calibration.

## Candidate Change
LightGBM challenger that keeps champion severity and capped severity settings while adding a more flexible, still regularized frequency option to test whether fold-balanced segmentation lift is frequency-led.

## CV Metric Summary
- Capped pure premium Gini: 0.1827
- Capped pure premium calibration gap: -0.0144
- Capped pure premium MAE: 217.5647
- Raw pure premium Gini: 0.1976
- Raw pure premium calibration gap: -0.0469
- Runtime seconds: 31.567034

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
Frequency is generally the more stable component in MTPL pricing. This candidate keeps severity stable and limits the extra flexibility to one frequency-grid option with minimum leaf and L2 controls.

## Decision
discard

Gate failures: pricing_transparent_model_or_documented_blend, pricing_capped_calibration_tight, segmentation_minimum_capped_gini_gain, segmentation_minimum_fold_agreement

Log truncated: False
