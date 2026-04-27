# MTPL Autoresearch Program

This is the operating manual for an autonomous coding agent running actuarial modeling experiments.

## Setup

1. Work on the dedicated autoresearch branch.
2. Read the in-scope files before experimenting:
   - `autoresearch/README.md`
   - `autoresearch/prepare.py`
   - `autoresearch/train.py`
   - `autoresearch/r/harness.R`
   - `autoresearch/r/candidate_runner.R`
   - `README.md`
   - `mtpl_glm_analysis.R`
   - `mtpl_gbm_analysis.R`
   - `mtpl_gbm_glm_synthesis.R`
3. Confirm R is available. If `Rscript` is not on PATH, `prepare.py` will try `C:\Program Files\R\R-4.5.3\bin\Rscript.exe`.
4. Run the baseline first:

```powershell
python autoresearch/train.py
```

5. Commit and push the baseline evidence before starting the loop.

## Immutable Boundary

You may edit only:

```text
autoresearch/train.py
```

Do not edit:

- `autoresearch/prepare.py`
- `autoresearch/r/harness.R`
- `autoresearch/r/candidate_runner.R`
- metric definitions
- split logic
- leakage checks
- hard gates
- historical evidence

Do not install dependencies or add packages without human approval.

Web research is allowed for actuarial or modeling references, but new dependencies are not.

## Objective

Track two champions:

- Pricing-level champion: strongest calibrated and defensible model for expected loss cost.
- Segmentation/research champion: strongest defensible lift/ranking signal.

Capped pure premium is the primary stable target because raw severity is heavy-tailed. Raw pure premium remains monitored and must not materially deteriorate.

GBM can suggest. GLM must defend. A GBM-only win is a research signal unless it can be translated into transparent terms or a documented blend.

## Hard Gates

A run is keepable only if it passes all relevant gates:

- capped pure premium Gini improves by at least `0.005`
- capped pure premium MAE/RMSE deterioration is below `1%`
- capped pure premium calibration deterioration is below `3` percentage points
- raw pure premium Gini is not materially worse
- at least `2 of 3` folds support the improvement
- no policy leakage
- predictions are finite and nonnegative
- exposure annualization is correct
- observed losses reconcile to severity records
- runtime stays under the 10-minute hard timeout

For GLM-style candidates, use AIC/BIC, parameter count, dispersion, sparse cells, coefficient reasonableness, smoothness, and parsimony as diagnostics. A simpler model with equal metrics beats a complex one.

## Curated Experiment Menu

Start with actuarially defensible ideas:

- spline degree adjustments for `DriverAge`, `CarAge`, and `logDensity`
- age and vehicle-age band refinements
- limited interactions: `DriverAgeBand:CarAgeBand`, `Power:Brand`, `Region:DensityBand`
- component-level calibration scalars estimated only inside the training fold
- constrained LightGBM grids with fewer leaves or stronger regularization
- GLM terms suggested by LightGBM importance/PDP behavior
- capped-severity stability improvements
- transparent blends only when they are documented and gated

After near-misses, combine ideas sparingly.

## Experiment Loop

Loop until interrupted:

1. Inspect git state and identify the current champion commit.
2. Modify only `autoresearch/train.py`.
3. Commit the candidate change.
4. Run:

```powershell
python autoresearch/train.py
```

5. Read the printed summary and the run evidence under `autoresearch/evidence/runs/<run_id>/`.
6. Commit tracked evidence:
   - `autoresearch/evidence/results.tsv`
   - `autoresearch/evidence/champions.json` if updated
   - `autoresearch/baselines/baseline_metrics.json` if created
   - `autoresearch/evidence/runs/<run_id>/candidate.json`
   - `autoresearch/evidence/runs/<run_id>/metrics.json`
   - `autoresearch/evidence/runs/<run_id>/fold_metrics.csv`
   - `autoresearch/evidence/runs/<run_id>/run.log`
   - `autoresearch/evidence/runs/<run_id>/decision.md`
7. Push after every run.
8. If the result is `keep`, the branch advances.
9. If the result is `discard` or `crash`, preserve the evidence, then restore `autoresearch/train.py` to the previous champion with a follow-up commit and push.

Do not ask whether to keep going. Continue until interrupted.

## Git Queue Fallback

If Codex can edit files and run experiments but cannot write to `.git`, use the host-side git worker:

```powershell
powershell -ExecutionPolicy Bypass -File .\autoresearch\tools\git_queue_worker.ps1
```

The worker watches `autoresearch/scratch/git_queue` for JSON jobs written by Codex. Each job stages explicit paths, commits them with the provided message, pushes when requested, and moves the job to `autoresearch/scratch/git_done`. This preserves the audit trail without requiring Codex itself to write `.git/index.lock`.

## Crash Policy

If a run crashes because of an obvious typo or interface mistake, fix it once and rerun. If it crashes again, log the crash, restore the champion `train.py`, and move on.

## Evidence Format

Each run creates a short lab note in `decision.md`:

- hypothesis
- candidate change
- CV metric summary
- gate pass/fail table
- actuarial interpretation
- decision: `keep`, `discard`, or `crash`

`run.log` is tracked up to 1 MB. If a log is larger, `prepare.py` writes a truncated head/tail log and records truncation in the decision memo.
