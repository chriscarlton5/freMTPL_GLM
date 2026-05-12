# Robustness Validation Report

This report is a locked post-selection validation layer. It does not update autoresearch champions, gates, or historical run evidence.

## Recommendation

Holdout validation does not fully support promoting `lightgbm_best_191`; keep it as an autoresearch signal and favor the initial LightGBM or GLM for defensibility.

## Blind Holdout Metrics

| Model | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `baseline_enhanced_glm_splines` | 0.2005 | 0.3517 | 217.0520 | 0.0118 | 0 | 0 |
| `lightgbm_regularized_challenger` | 0.2075 | 0.3860 | 215.4846 | -0.0056 | 0 | 0 |
| `lightgbm_best_191` | 0.2065 | 0.3879 | 215.0472 | -0.0099 | 0 | 0 |

## Seed Metric Stability

| Model | Metric | Mean | SD | Min | Max | Worst Delta |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | `capped_pp_gini` | 0.2082 | 0.0022 | 0.2062 | 0.2115 | 0.0033 |
| `lightgbm_regularized_challenger` | `raw_pp_gini` | 0.3865 | 0.0030 | 0.3816 | 0.3893 | 0.0049 |
| `lightgbm_regularized_challenger` | `capped_pp_mae` | 215.6989 | 1.1356 | 214.2095 | 217.1355 | 1.4894 |
| `lightgbm_regularized_challenger` | `capped_pp_calibration_gap` | -0.0036 | 0.0110 | -0.0181 | 0.0104 | 0.0145 |
| `lightgbm_best_191` | `capped_pp_gini` | 0.2054 | 0.0027 | 0.2013 | 0.2084 | 0.0041 |
| `lightgbm_best_191` | `raw_pp_gini` | 0.3773 | 0.0103 | 0.3654 | 0.3883 | 0.0119 |
| `lightgbm_best_191` | `capped_pp_mae` | 215.1280 | 1.1803 | 214.0018 | 216.9021 | 1.7742 |
| `lightgbm_best_191` | `capped_pp_calibration_gap` | -0.0088 | 0.0116 | -0.0197 | 0.0088 | 0.0176 |

## Policy Prediction Stability

| Model | Prediction | Sampled Policies | Median CV | P95 CV | Max CV |
| --- | --- | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | `capped_pp` | 1000 | 0.0480 | 0.0916 | 0.1370 |
| `lightgbm_regularized_challenger` | `raw_pp` | 1000 | 0.0635 | 0.1253 | 0.2752 |
| `lightgbm_best_191` | `capped_pp` | 1000 | 0.0497 | 0.0889 | 0.1454 |
| `lightgbm_best_191` | `raw_pp` | 1000 | 0.0831 | 0.1364 | 0.2022 |

## Interpretability Stability

| Model | Component | Mean Top-5 Jaccard | Most Common Top Feature | Status |
| --- | --- | ---: | --- | --- |
| `lightgbm_regularized_challenger` | `frequency` | 1.0000 | `DriverAge` | stable |
| `lightgbm_regularized_challenger` | `severity` | 1.0000 | `DriverAge` | stable |
| `lightgbm_regularized_challenger` | `capped_severity` | 1.0000 | `DriverAge` | stable |
| `lightgbm_best_191` | `frequency` | 1.0000 | `DriverAge` | stable |
| `lightgbm_best_191` | `severity` | 1.0000 | `DriverAge` | stable |
| `lightgbm_best_191` | `capped_severity` | 1.0000 | `DriverAge` | stable |

## Governance Note

`lightgbm_best_191` remains a CV-selected autoresearch champion unless this holdout and stability evidence is reviewed by a human model owner. Python generated candidate specs and launched runs; R remains the metric, split, and modeling source of truth.
