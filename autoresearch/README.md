# MTPL Autoresearch

This folder adapts Karpathy's `autoresearch` pattern to the French MTPL actuarial modeling project.

The goal is not to chase a generic machine-learning leaderboard. The goal is to let a long-running coding agent try incremental actuarial modeling experiments while preserving the governance rules a chief actuary would expect: no leakage, stable validation, calibrated loss-cost behavior, parsimonious model changes, and defensible interpretation.

## Architecture

- `prepare.py` is immutable. It resolves R, runs the candidate, enforces hard gates, writes evidence, and prints the summary block.
- `train.py` is the only experiment file an autonomous agent may edit.
- `program.md` is the human-owned operating manual for the agent.
- `r/harness.R` and `r/candidate_runner.R` are immutable bridges into the existing R modeling workflow.
- `evidence/` is tracked in git and stores the experiment ledger and run evidence.
- `scratch/` is ignored and reserved for bulky or temporary artifacts.

## Modeling Boundary

Python orchestrates. R models.

The current GLM/LightGBM work remains the source of truth for actuarial modeling functions, splits, feature treatment, and metrics. This keeps the autoresearch experiment aligned with the existing report and avoids an unnecessary rewrite into Python.

## Evidence Policy

Unlike Karpathy's original repo, this project tracks small evidence artifacts because actuarial experimentation needs an audit trail. Each run records a TSV ledger row, candidate spec, metrics JSON, fold metrics CSV, run log, and short decision memo. Bulky artifacts such as model binaries and prediction dumps stay out of git.
