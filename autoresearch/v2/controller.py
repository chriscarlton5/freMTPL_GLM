"""Governed v2 autonomous research controller.

The v2 controller evaluates structured candidate JSON and can promote a model
only after CV, seed stability, and blind holdout evidence beat the configured
pricing champion. It does not edit train.py or mutate v1 evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
V2_DIR = Path(__file__).resolve().parent
AUTORESEARCH_DIR = V2_DIR.parent
CONFIG_PATH = V2_DIR / "config.json"
EVIDENCE_DIR = AUTORESEARCH_DIR / "evidence" / "v2"
RUNS_DIR = EVIDENCE_DIR / "runs"
REGISTRY_PATH = EVIDENCE_DIR / "registry.json"
MEMORY_PATH = EVIDENCE_DIR / "research_memory.md"
R_RUNNER = AUTORESEARCH_DIR / "r" / "v2_runner.R"

REQUIRED_CANDIDATE_FIELDS = {
    "schema_version",
    "candidate_id",
    "idea_family",
    "hypothesis",
    "expected_mechanism",
    "intended_metric_improvements",
    "known_tradeoff_risk",
    "parent_candidate_id",
    "model_spec",
}


def resolve_rscript() -> str:
    env_path = os.environ.get("RSCRIPT") or os.environ.get("R_SCRIPT")
    candidates = [
        env_path,
        shutil.which("Rscript"),
        r"C:\Program Files\R\R-4.5.3\bin\Rscript.exe",
        r"C:\Program Files\R\R-4.5.2\bin\Rscript.exe",
        r"C:\Program Files\R\R-4.5.1\bin\Rscript.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)
    raise RuntimeError("Could not find Rscript. Set RSCRIPT to the full Rscript.exe path.")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def spec_hash(model_spec: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(model_spec).encode("utf-8")).hexdigest()


def load_registry() -> dict[str, Any]:
    if not REGISTRY_PATH.exists():
        return {"schema_version": 1, "runs": []}
    return load_json(REGISTRY_PATH)


def save_registry(registry: dict[str, Any]) -> None:
    write_json(REGISTRY_PATH, registry)


def validate_candidate(candidate: dict[str, Any], config: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    missing = sorted(REQUIRED_CANDIDATE_FIELDS - set(candidate))
    if missing:
        failures.append(f"missing fields: {', '.join(missing)}")
    if candidate.get("schema_version") != 1:
        failures.append("schema_version must be 1")
    if candidate.get("idea_family") not in config["allowed_idea_families"]:
        failures.append(f"idea_family is not allowed: {candidate.get('idea_family')}")
    model_spec = candidate.get("model_spec")
    if not isinstance(model_spec, dict):
        failures.append("model_spec must be an object")
    else:
        for field in ("id", "model_type"):
            if field not in model_spec:
                failures.append(f"model_spec missing {field}")
    if not candidate.get("hypothesis"):
        failures.append("hypothesis must be non-empty")
    if not candidate.get("expected_mechanism"):
        failures.append("expected_mechanism must be non-empty")
    if not candidate.get("known_tradeoff_risk"):
        failures.append("known_tradeoff_risk must be non-empty")
    return failures


def family_completed_count(registry: dict[str, Any], family: str) -> int:
    return sum(
        1
        for row in registry.get("runs", [])
        if row.get("idea_family") == family and row.get("status") not in {"duplicate", "schema_failed", "budget_exhausted"}
    )


def duplicate_entry(registry: dict[str, Any], digest: str) -> dict[str, Any] | None:
    return next((row for row in registry.get("runs", []) if row.get("spec_hash") == digest), None)


def make_run_dir(candidate_id: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_id = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in candidate_id)
    return RUNS_DIR / f"{timestamp}_{safe_id}"


def append_memory(line: str) -> None:
    MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not MEMORY_PATH.exists():
        MEMORY_PATH.write_text("# V2 Research Memory\n\n", encoding="utf-8")
    with MEMORY_PATH.open("a", encoding="utf-8") as handle:
        handle.write(line.rstrip() + "\n")


def run_r_evaluation(candidate_path: Path, benchmark_path: Path, output_dir: Path, seeds: list[int]) -> None:
    command = [
        resolve_rscript(),
        str(R_RUNNER),
        str(candidate_path),
        str(benchmark_path),
        str(output_dir),
        str(REPO_ROOT),
        ",".join(str(seed) for seed in seeds),
    ]
    completed = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
    log_text = ""
    if completed.stdout:
        log_text += "[stdout]\n" + completed.stdout
        if not completed.stdout.endswith("\n"):
            log_text += "\n"
    if completed.stderr:
        log_text += "[stderr]\n" + completed.stderr
        if not completed.stderr.endswith("\n"):
            log_text += "\n"
    (output_dir / "run.log").write_text(log_text, encoding="utf-8")
    if completed.returncode != 0:
        raise RuntimeError(f"R v2 runner failed with exit code {completed.returncode}; see {output_dir / 'run.log'}")


def read_holdout_rows(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    benchmark = next(row for row in rows if row["role"] == "benchmark")
    candidate = next(row for row in rows if row["role"] == "candidate")
    return benchmark, candidate


def f(row: dict[str, str], key: str) -> float:
    value = row.get(key, "")
    if value == "":
        return 0.0
    return float(value)


def promotion_decision(
    candidate: dict[str, Any],
    benchmark: dict[str, str],
    candidate_row: dict[str, str],
    config: dict[str, Any],
) -> tuple[str, dict[str, Any], list[str]]:
    gates = config["promotion_gates"]
    benchmark_id = config["current_pricing_champion_id"]
    candidate_model_id = candidate["model_spec"]["id"]

    if candidate_model_id == benchmark_id:
        return "current_champion", {"current_champion": True}, []

    deltas = {
        "holdout_capped_pp_gini_gain": f(candidate_row, "capped_pp_gini") - f(benchmark, "capped_pp_gini"),
        "holdout_raw_pp_gini_gain": f(candidate_row, "raw_pp_gini") - f(benchmark, "raw_pp_gini"),
        "capped_pp_mae_deterioration": (f(candidate_row, "capped_pp_mae") - f(benchmark, "capped_pp_mae"))
        / max(abs(f(benchmark, "capped_pp_mae")), 1e-12),
        "capped_pp_rmse_deterioration": (f(candidate_row, "capped_pp_rmse") - f(benchmark, "capped_pp_rmse"))
        / max(abs(f(benchmark, "capped_pp_rmse")), 1e-12),
        "capped_pp_calibration_abs_deterioration": abs(f(candidate_row, "capped_pp_calibration_gap"))
        - abs(f(benchmark, "capped_pp_calibration_gap")),
        "candidate_abs_capped_pp_calibration_gap": abs(f(candidate_row, "capped_pp_calibration_gap")),
        "bad_prediction_count": int(float(candidate_row.get("bad_prediction_count") or 0)),
        "policy_leakage_count": int(float(candidate_row.get("policy_leakage_count") or 0)),
    }
    failures: list[str] = []
    if deltas["holdout_capped_pp_gini_gain"] < gates["min_holdout_capped_pp_gini_gain"]:
        failures.append("holdout capped PP Gini did not beat champion by required margin")
    if deltas["capped_pp_mae_deterioration"] > gates["max_capped_pp_mae_deterioration"]:
        failures.append("capped PP MAE deterioration exceeded tolerance")
    if deltas["capped_pp_rmse_deterioration"] > gates["max_capped_pp_rmse_deterioration"]:
        failures.append("capped PP RMSE deterioration exceeded tolerance")
    if deltas["candidate_abs_capped_pp_calibration_gap"] > gates["max_abs_capped_pp_calibration_gap"]:
        failures.append("absolute capped PP calibration gap exceeded tolerance")
    if deltas["capped_pp_calibration_abs_deterioration"] > gates["max_capped_pp_calibration_abs_deterioration"]:
        failures.append("capped PP calibration deterioration exceeded tolerance")
    if deltas["holdout_raw_pp_gini_gain"] < -gates["max_raw_pp_gini_deterioration"]:
        failures.append("raw PP Gini deteriorated beyond tolerance")
    if deltas["bad_prediction_count"] != 0:
        failures.append("candidate produced invalid predictions")
    if deltas["policy_leakage_count"] != 0:
        failures.append("candidate leaked policies across train and holdout")

    return ("promote" if not failures else "research_only"), deltas, failures


def write_markdown_report(
    path: Path,
    candidate: dict[str, Any],
    benchmark: dict[str, str],
    candidate_row: dict[str, str],
    status: str,
    deltas: dict[str, Any],
    failures: list[str],
) -> None:
    failure_text = "none" if not failures else "\n".join(f"- {failure}" for failure in failures)
    text = f"""# V2 Promotion Report: {candidate['candidate_id']}

## Decision

`{status}`

## Candidate

- Idea family: `{candidate['idea_family']}`
- Parent: `{candidate.get('parent_candidate_id')}`
- Hypothesis: {candidate['hypothesis']}
- Expected mechanism: {candidate['expected_mechanism']}
- Known tradeoff risk: {candidate['known_tradeoff_risk']}

## Blind Holdout Comparison

| Model | Role | Capped PP Gini | Raw PP Gini | Capped PP MAE | Capped Cal Gap | Bad Preds | Leakage |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `{benchmark['model_id']}` | benchmark | {float(benchmark['capped_pp_gini']):.4f} | {float(benchmark['raw_pp_gini']):.4f} | {float(benchmark['capped_pp_mae']):.4f} | {float(benchmark['capped_pp_calibration_gap']):.4f} | {benchmark['bad_prediction_count']} | {benchmark['policy_leakage_count']} |
| `{candidate_row['model_id']}` | candidate | {float(candidate_row['capped_pp_gini']):.4f} | {float(candidate_row['raw_pp_gini']):.4f} | {float(candidate_row['capped_pp_mae']):.4f} | {float(candidate_row['capped_pp_calibration_gap']):.4f} | {candidate_row['bad_prediction_count']} | {candidate_row['policy_leakage_count']} |

## Promotion Deltas

```json
{json.dumps(deltas, indent=2, sort_keys=True)}
```

## Gate Failures

{failure_text}

## Supporting Artifacts

- `cv_fold_metrics.csv`
- `seed_summary.csv`
- `prediction_stability_summary.csv`
- `feature_importance_summary.csv`
- `r_metrics.json`
"""
    path.write_text(text, encoding="utf-8")


def record_registry(
    registry: dict[str, Any],
    candidate: dict[str, Any],
    digest: str,
    status: str,
    run_dir: Path | None,
    failures: list[str],
) -> None:
    registry.setdefault("runs", []).append(
        {
            "candidate_id": candidate.get("candidate_id"),
            "model_id": candidate.get("model_spec", {}).get("id"),
            "idea_family": candidate.get("idea_family"),
            "spec_hash": digest,
            "status": status,
            "run_dir": None if run_dir is None else str(run_dir.relative_to(REPO_ROOT)).replace("\\", "/"),
            "failures": failures,
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
    )
    save_registry(registry)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a governed v2 autoresearch candidate.")
    parser.add_argument("candidate", type=Path, help="Path to structured v2 candidate JSON.")
    parser.add_argument("--force", action="store_true", help="Run even if an identical model spec exists in the registry.")
    args = parser.parse_args()

    config = load_json(CONFIG_PATH)
    candidate_path = args.candidate if args.candidate.is_absolute() else REPO_ROOT / args.candidate
    candidate = load_json(candidate_path)
    registry = load_registry()
    digest = spec_hash(candidate.get("model_spec", {}))

    schema_failures = validate_candidate(candidate, config)
    if schema_failures:
        record_registry(registry, candidate, digest, "schema_failed", None, schema_failures)
        raise SystemExit("schema_failed: " + "; ".join(schema_failures))

    duplicate = duplicate_entry(registry, digest)
    if duplicate and not args.force:
        failures = [f"duplicate model spec previously evaluated by {duplicate.get('candidate_id')}"]
        record_registry(registry, candidate, digest, "duplicate", None, failures)
        print("status: duplicate")
        print(f"duplicate_of: {duplicate.get('candidate_id')}")
        return

    family = candidate["idea_family"]
    budget = int(config["idea_family_budgets"][family])
    if family_completed_count(registry, family) >= budget and not args.force:
        failures = [f"idea family budget exhausted for {family}: {budget}"]
        record_registry(registry, candidate, digest, "budget_exhausted", None, failures)
        print("status: budget_exhausted")
        return

    run_dir = make_run_dir(candidate["candidate_id"])
    run_dir.mkdir(parents=True, exist_ok=False)
    shutil.copy2(candidate_path, run_dir / "candidate.json")

    benchmark_path = REPO_ROOT / config["current_pricing_champion_candidate"]
    try:
        run_r_evaluation(candidate_path, benchmark_path, run_dir, [int(seed) for seed in config["stability_seeds"]])
    except Exception as exc:
        failures = [str(exc)]
        record_registry(registry, candidate, digest, "error", run_dir, failures)
        append_memory(f"- `{candidate['candidate_id']}` -> `error` ({candidate['idea_family']}): {failures[0]}")
        raise
    benchmark_row, candidate_row = read_holdout_rows(run_dir / "holdout_comparison.csv")
    status, deltas, failures = promotion_decision(candidate, benchmark_row, candidate_row, config)
    write_markdown_report(run_dir / "promotion_report.md", candidate, benchmark_row, candidate_row, status, deltas, failures)
    write_json(
        run_dir / "decision.json",
        {
            "candidate_id": candidate["candidate_id"],
            "model_id": candidate["model_spec"]["id"],
            "status": status,
            "deltas": deltas,
            "gate_failures": failures,
            "benchmark_model_id": benchmark_row["model_id"],
        },
    )

    record_registry(registry, candidate, digest, status, run_dir, failures)
    append_memory(
        f"- `{candidate['candidate_id']}` -> `{status}` ({candidate['idea_family']}): "
        + ("no gate failures" if not failures else "; ".join(failures))
    )

    print(f"status: {status}")
    print(f"run_dir: {run_dir.relative_to(REPO_ROOT)}")
    print(f"report: {(run_dir / 'promotion_report.md').relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
