# MTPL Autoresearch V2

V2 is the second-generation autonomous research harness for the French MTPL pricing project. It was built after the first autonomous loop exposed a useful but uncomfortable lesson: repeated cross-validation search can make a candidate look like a new champion even when the improvement does not survive blind holdout validation.

The goal of V2 is therefore narrower and stricter than V1:

> Improve the pricing champion on robust, staged evidence, not on repeated-CV leaderboard movement.

V2 began with `lightgbm_regularized_challenger` as the pricing champion and promoted `v2_lgb_stronger_l2` after that candidate cleared the configured blind-holdout promotion gates.

This remains an exploratory side-project workflow, not a production rate filing. The point is to demonstrate better autonomous model governance: explicit hypotheses, duplicate detection, idea-family budgets, seed checks, holdout promotion rules, and auditable promotion memos.

## Why V2 Exists

The original autonomous loop did find `lightgbm_best_191`, a candidate with stronger repeated-CV metrics than the initial LightGBM. But a locked post-selection robustness check changed the interpretation:

| Model | Blind Holdout Capped PP Gini | Blind Holdout Raw PP Gini | Blind Holdout Capped MAE | Blind Holdout Capped Cal Gap |
| --- | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | `0.2075` | `0.3860` | `215.4846` | `-0.0056` |
| `lightgbm_best_191` | `0.2065` | `0.3879` | `215.0472` | `-0.0099` |

`lightgbm_best_191` was not useless: it improved raw Gini and capped MAE. But it failed to beat the initial LightGBM on the primary capped pure-premium Gini objective. That made it a research signal, not a pricing champion.

V2 was designed around that failure mode. It tries to prevent the agent from spending hundreds of runs nudging the same hyperparameters around the same validation surface.

## Actuarial Target

The target remains policy-level expected annual loss cost, or pure premium:

```text
pure premium = expected annual claim frequency * expected claim severity
```

The modeling structure remains frequency/severity:

- Frequency is modeled with a Poisson-style target and exposure treatment.
- Severity is modeled on positive claim amounts.
- Capped severity uses the existing 99.5% severity cap as a body-of-loss stability view.
- Raw pure premium remains monitored because large losses still matter, but capped pure-premium Gini is the primary pricing segmentation target for promotion.

V2 does not redefine the actuarial metrics. R remains the source of truth for data preparation, splits, model fitting, prediction, and metric calculation.

## Design Principles

V2 changes the autonomous researcher in five ways.

First, candidates are structured. Every candidate declares an idea family, hypothesis, expected mechanism, intended metric improvements, known tradeoff risk, parent candidate, and model specification.

Second, the current champion is explicit. The champion lives in `config.json`, and every promotion is measured against that benchmark rather than against the last attractive CV run.

Third, promotion is staged. A candidate must pass CV, seed-stability, and blind-holdout evidence before it can be treated as an improvement.

Fourth, the loop has memory. Duplicate specs are blocked, idea-family budgets prevent repeated local hill-climbing, and research memory records failed paths.

Fifth, V2 separates research evidence from champion promotion. A candidate can be useful as `research_only` without being promoted.

## Architecture

V2 lives under `autoresearch/v2/` and writes evidence under `autoresearch/evidence/v2/`.

Important files:

- `config.json`: current champion, promotion gates, seed list, idea-family budgets, and known non-promoted candidates.
- `controller.py`: validates structured candidates, checks duplicates and budgets, calls the R evaluator, applies promotion gates, and writes reports.
- `loop.py`: generates a curated queue of governed candidates and submits them to the controller.
- `candidates/`: hand-authored benchmark and replay candidates.
- `generated/`: candidates created by the V2 loop.
- `../r/v2_runner.R`: R-side evaluator that reuses the existing modeling functions and produces CV, seed, holdout, prediction-stability, and importance-stability evidence.

The controller does not edit `autoresearch/train.py`, does not mutate V1 evidence, and does not update `autoresearch/evidence/champions.json`.

## Candidate Families

V2 recognizes these idea families:

| Family | Purpose |
| --- | --- |
| `new_feature` | Add materially new actuarial signal from existing fields. |
| `transparent_glm` | Test reviewable GLM interactions or structures. |
| `model_structure` | Change model architecture or learning structure without local over-search. |
| `calibration` | Improve level fit without hiding ranking deterioration. |
| `stability` | Improve generalization, seed stability, or variance control. |
| `hyperparameter_tuning` | Allowed only in limited budget; not the default research mode. |

The early V2 queue deliberately tested transparent GLM interactions before returning to LightGBM structure. Those GLM candidates did not promote, which is useful evidence: the initial LightGBM still captured signal that the attempted transparent interactions did not recover.

## Promotion Rules

The current promotion gates are configured in `config.json`.

A candidate must satisfy all of the following:

- Holdout capped pure-premium Gini improves by at least `0.001`.
- Capped MAE deterioration is no worse than `0.5%`.
- Capped RMSE deterioration is no worse than `0.5%`.
- Absolute capped calibration gap is within `3%`.
- Absolute capped calibration deterioration is no worse than `0.5` percentage points.
- Raw pure-premium Gini deterioration is no worse than `0.002`.
- No policy leakage.
- No invalid or negative predictions.

These thresholds are intentionally stricter than a simple "Gini went up" rule. The point is to promote robust pricing candidates, not leaderboard artifacts.

## V2 Results

V2 promoted `v2_lgb_stronger_l2`, a LightGBM stability candidate that increases the L2 penalties from the initial regularized LightGBM while preserving its broader structure.

| Model | Role | Holdout Capped PP Gini | Holdout Raw PP Gini | Holdout Capped MAE | Holdout Capped Cal Gap |
| --- | --- | ---: | ---: | ---: | ---: |
| `lightgbm_regularized_challenger` | Starting champion | `0.2075` | `0.3860` | `215.4846` | `-0.0056` |
| `v2_lgb_stronger_l2` | V2 promoted champion | `0.2089` | `0.3858` | `215.5038` | `-0.0054` |

Promotion deltas:

| Metric | Delta |
| --- | ---: |
| Holdout capped PP Gini | `+0.00138` |
| Holdout raw PP Gini | `-0.00021` |
| Capped MAE deterioration | `+0.009%` |
| Capped RMSE deterioration | `-0.001%` |
| Absolute capped calibration deterioration | `-0.00021` |
| Bad predictions | `0` |
| Policy leakage | `0` |

The improvement is modest, but it is exactly the kind of improvement V2 was designed to recognize: capped ranking improved enough to clear the promotion margin, while raw ranking, calibration, error, leakage, and prediction validity stayed within tolerance.

The promotion report is:

```text
autoresearch/evidence/v2/runs/20260512_161535_v2_lgb_stronger_l2/promotion_report.md
```

## Failed Paths

V2 also recorded research-only or failed candidates:

| Candidate | Outcome | Main Reason |
| --- | --- | --- |
| `lightgbm_best_191` | `research_only` | Did not beat the starting champion on holdout capped PP Gini. |
| `v2_glm_age_car_interaction` | `research_only` | MAE, calibration, and raw Gini deteriorated. |
| `v2_glm_power_brand_interaction` | `research_only` | Capped Gini, MAE, calibration, and raw Gini failed gates. |
| `v2_glm_age_powerbrand` | `research_only` | Capped Gini, MAE, calibration, and raw Gini failed gates. |
| `v2_glm_region_density_interaction` | `error` | Known `DensityBand` factor-level mismatch. |
| `v2_lgb_higher_leaf_floor` | `research_only` | Did not beat holdout capped PP Gini gate. |
| `v2_lgb_lower_learning_rate` | `research_only` | Raw PP Gini deteriorated beyond tolerance. |
| `v2_lgb_conservative_feature_fraction` | `research_only` | Capped PP Gini and raw PP Gini failed gates. |

These failures matter. V2 is not just a search loop; it is a record of which ideas were tried, why they failed, and which modeling paths should not be repeated without a new hypothesis.

## How To Run

Run one structured candidate:

```powershell
python autoresearch/v2/controller.py autoresearch/v2/candidates/lightgbm_best_191.json
```

Run the curated autonomous loop:

```powershell
python autoresearch/v2/loop.py --max-iterations 3
```

The loop writes generated candidates under:

```text
autoresearch/v2/generated/
```

Evidence is written under:

```text
autoresearch/evidence/v2/runs/
```

The current champion and promotion gates are in:

```text
autoresearch/v2/config.json
```

## Output Statuses

| Status | Meaning |
| --- | --- |
| `current_champion` | The submitted candidate is the configured benchmark. |
| `promote` | The candidate passed all promotion gates. |
| `research_only` | The candidate produced useful evidence but failed at least one promotion gate. |
| `duplicate` | The model spec was already evaluated. |
| `budget_exhausted` | The idea family reached its configured budget. |
| `schema_failed` | The structured candidate JSON is incomplete or invalid. |
| `error` | The R evaluator or controller failed; inspect the run log. |

## Evidence Layout

Each full V2 run writes:

```text
candidate.json
cv_fold_metrics.csv
decision.json
feature_importance_by_seed.csv
feature_importance_summary.csv
holdout_comparison.csv
prediction_stability_summary.csv
promotion_report.md
r_metrics.json
run.log
seed_metrics.csv
seed_summary.csv
```

The registry is:

```text
autoresearch/evidence/v2/registry.json
```

The research memory is:

```text
autoresearch/evidence/v2/research_memory.md
```

## Governance Interpretation

V2 did not try to hide the V1 failure. It used that failure as a design constraint.

The important methodological change is that a candidate can no longer become champion because it wins the repeated CV loop. It must beat the configured champion on blind holdout and remain acceptable on calibration, error, raw Gini, leakage, prediction validity, and stability checks.

The current V2 champion, `v2_lgb_stronger_l2`, is still not a production-filed model. A real filing would need additional review: proxy-variable analysis, rate impact testing, territorial/fairness review, business constraints, monitoring, and signoff. But as an autonomous modeling experiment, V2 is a stronger actuarial research scaffold than V1 because it promotes only after post-selection validation.
