# V2 Research Memory

- `lightgbm_regularized_challenger` -> `current_champion` (model_structure): no gate failures
- `lightgbm_best_191` -> `research_only` (hyperparameter_tuning): holdout capped PP Gini did not beat champion by required margin
- `v2_glm_age_car_interaction` -> `research_only` (transparent_glm): capped PP MAE deterioration exceeded tolerance; capped PP calibration deterioration exceeded tolerance; raw PP Gini deteriorated beyond tolerance
- `v2_glm_power_brand_interaction` -> `research_only` (transparent_glm): holdout capped PP Gini did not beat champion by required margin; capped PP MAE deterioration exceeded tolerance; capped PP calibration deterioration exceeded tolerance; raw PP Gini deteriorated beyond tolerance
- `v2_glm_region_density_interaction` -> `error` (transparent_glm): known DensityBand factor-level mismatch; removed from v2 queue until shared density-band references are implemented.
- `v2_glm_age_powerbrand` -> `research_only` (transparent_glm): holdout capped PP Gini did not beat champion by required margin; capped PP MAE deterioration exceeded tolerance; capped PP calibration deterioration exceeded tolerance; raw PP Gini deteriorated beyond tolerance
- `v2_lgb_higher_leaf_floor` -> `research_only` (model_structure): holdout capped PP Gini did not beat champion by required margin
- `v2_lgb_lower_learning_rate` -> `research_only` (model_structure): raw PP Gini deteriorated beyond tolerance
- `v2_lgb_conservative_feature_fraction` -> `research_only` (stability): holdout capped PP Gini did not beat champion by required margin; raw PP Gini deteriorated beyond tolerance
- `v2_lgb_stronger_l2` -> `promote` (stability): no gate failures
