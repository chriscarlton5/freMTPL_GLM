# MTPL Autoresearch V2

V2 changes the autonomous researcher from a repeated-CV hill climber into a staged promotion system. It began with `lightgbm_regularized_challenger` as the pricing champion and promoted `v2_lgb_stronger_l2` after that candidate beat the configured blind-holdout gates.

## Run

```powershell
python autoresearch/v2/controller.py autoresearch/v2/candidates/lightgbm_best_191.json
```

Reports are written under `autoresearch/evidence/v2/runs/`. The registry and research memory live under `autoresearch/evidence/v2/`.

To run the curated autonomous loop:

```powershell
python autoresearch/v2/loop.py --max-iterations 3
```

The loop generates structured candidates under `autoresearch/v2/generated/`, submits them to the controller, and stops if any candidate is promoted. Future runs benchmark against the current champion in `config.json`.

## Outcomes

- `current_champion`: the submitted candidate is the configured benchmark.
- `promote`: the candidate beats all holdout promotion gates.
- `research_only`: the candidate has useful evidence but fails at least one promotion gate.
- `reject`: the candidate fails integrity, schema, budget, or duplicate checks.
- `duplicate`: the model spec was already evaluated.
- `budget_exhausted`: the idea family has reached its configured budget.

## Guardrails

The controller reads structured candidate JSON. It does not edit `autoresearch/train.py`, mutate v1 evidence, or update `champions.json`. R remains the source of truth for modeling, splits, and metrics.
