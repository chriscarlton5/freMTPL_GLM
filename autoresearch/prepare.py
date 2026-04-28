"""Immutable MTPL autoresearch orchestration and evaluation harness.

This file mirrors Karpathy's autoresearch split: experiment agents edit
``train.py`` only. This module owns run setup, R invocation, evidence writing,
and the hard actuarial gates.
"""

from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
AUTORESEARCH_DIR = Path(__file__).resolve().parent
R_DIR = AUTORESEARCH_DIR / "r"
BASELINES_DIR = AUTORESEARCH_DIR / "baselines"
EVIDENCE_DIR = AUTORESEARCH_DIR / "evidence"
RUNS_DIR = EVIDENCE_DIR / "runs"
SCRATCH_DIR = AUTORESEARCH_DIR / "scratch"
RESULTS_TSV = EVIDENCE_DIR / "results.tsv"
CHAMPIONS_JSON = EVIDENCE_DIR / "champions.json"
BASELINE_METRICS_JSON = BASELINES_DIR / "baseline_metrics.json"

TIMEOUT_SECONDS = 600
LOG_SIZE_CAP_BYTES = 1_000_000

GATE_DEFAULTS = {
    "minimum_gini_gain": 0.005,
    "max_mae_deterioration": 0.01,
    "max_deviance_deterioration": 0.01,
    "max_calibration_deterioration": 0.03,
    "minimum_fold_agreement": 2,
}

RESULT_COLUMNS = [
    "run_id",
    "commit",
    "candidate_id",
    "status",
    "selection_score",
    "pricing_status",
    "segmentation_status",
    "capped_pp_gini_mean",
    "capped_pp_calibration_gap_mean",
    "capped_pp_mae_mean",
    "raw_pp_gini_mean",
    "raw_pp_calibration_gap_mean",
    "runtime_seconds",
    "gate_failures",
    "description",
]


@dataclass
class RunPaths:
    run_id: str
    run_dir: Path
    candidate_json: Path
    metrics_json: Path
    fold_metrics_csv: Path
    run_log: Path
    decision_md: Path


def ensure_directories() -> None:
    for path in (BASELINES_DIR, EVIDENCE_DIR, RUNS_DIR, SCRATCH_DIR):
        path.mkdir(parents=True, exist_ok=True)


def git_short_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return "unknown"


def json_dump(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def json_load(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


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


def make_run_paths(candidate: dict[str, Any]) -> RunPaths:
    safe_id = str(candidate.get("id", "candidate")).replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    commit = git_short_commit()
    run_id = f"{timestamp}_{commit}_{safe_id}"
    run_dir = RUNS_DIR / run_id
    return RunPaths(
        run_id=run_id,
        run_dir=run_dir,
        candidate_json=run_dir / "candidate.json",
        metrics_json=run_dir / "metrics.json",
        fold_metrics_csv=run_dir / "fold_metrics.csv",
        run_log=run_dir / "run.log",
        decision_md=run_dir / "decision.md",
    )


def write_log(path: Path, stdout: str, stderr: str, timed_out: bool = False) -> bool:
    full = []
    if timed_out:
        full.append("[timeout]\n")
    if stdout:
        full.append("[stdout]\n")
        full.append(stdout)
        if not stdout.endswith("\n"):
            full.append("\n")
    if stderr:
        full.append("[stderr]\n")
        full.append(stderr)
        if not stderr.endswith("\n"):
            full.append("\n")
    text = "".join(full)
    truncated = False
    encoded = text.encode("utf-8", errors="replace")
    if len(encoded) > LOG_SIZE_CAP_BYTES:
        truncated = True
        half = LOG_SIZE_CAP_BYTES // 2
        head = encoded[:half].decode("utf-8", errors="replace")
        tail = encoded[-half:].decode("utf-8", errors="replace")
        text = (
            f"[log truncated: original_bytes={len(encoded)} cap={LOG_SIZE_CAP_BYTES}]\n"
            f"{head}\n[... middle omitted ...]\n{tail}"
        )
    path.write_text(text, encoding="utf-8")
    return truncated


def run_r_candidate(paths: RunPaths) -> tuple[int, bool, float, bool]:
    command = [
        resolve_rscript(),
        str(R_DIR / "candidate_runner.R"),
        str(paths.candidate_json),
        str(paths.metrics_json),
        str(paths.fold_metrics_csv),
        str(REPO_ROOT),
    ]
    start = datetime.now()
    try:
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            timeout=TIMEOUT_SECONDS,
        )
        elapsed = (datetime.now() - start).total_seconds()
        truncated = write_log(paths.run_log, completed.stdout, completed.stderr)
        return completed.returncode, False, elapsed, truncated
    except subprocess.TimeoutExpired as exc:
        elapsed = (datetime.now() - start).total_seconds()
        stdout = exc.stdout if isinstance(exc.stdout, str) else (exc.stdout or b"").decode("utf-8", errors="replace")
        stderr = exc.stderr if isinstance(exc.stderr, str) else (exc.stderr or b"").decode("utf-8", errors="replace")
        truncated = write_log(paths.run_log, stdout, stderr, timed_out=True)
        return 124, True, elapsed, truncated


def metric(metrics: dict[str, Any], name: str, default: float = 0.0) -> float:
    value = metrics.get("aggregate", {}).get(name, default)
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def normalize_champions(
    raw_champions: dict[str, Any] | None,
    baseline: dict[str, Any] | None,
) -> dict[str, Any] | None:
    """Return the v2 dual-champion registry, migrating v1 single payloads."""
    if raw_champions and ("pricing" in raw_champions or "segmentation" in raw_champions):
        pricing = raw_champions.get("pricing") or baseline
        segmentation = raw_champions.get("segmentation") or baseline or pricing
        if pricing is None and segmentation is None:
            return None
        return {
            "schema_version": 2,
            "pricing": pricing,
            "segmentation": segmentation,
            "updated_at": raw_champions.get("updated_at"),
        }

    if raw_champions is None and baseline is None:
        return None

    if raw_champions is None:
        return {
            "schema_version": 2,
            "pricing": baseline,
            "segmentation": baseline,
            "updated_at": None,
        }

    decision = raw_champions.get("decision", {})
    pricing_status = decision.get("pricing_status")
    segmentation_status = decision.get("segmentation_status")
    pricing = raw_champions if pricing_status in {"baseline", "candidate"} else baseline
    segmentation = raw_champions if segmentation_status in {"baseline", "candidate"} else baseline or raw_champions
    if pricing is None and segmentation is None:
        return None
    return {
        "schema_version": 2,
        "pricing": pricing,
        "segmentation": segmentation,
        "updated_at": None,
    }


def load_champions() -> dict[str, Any] | None:
    return normalize_champions(json_load(CHAMPIONS_JSON), json_load(BASELINE_METRICS_JSON))


def is_baseline_run(candidate: dict[str, Any], champions: dict[str, Any] | None) -> bool:
    return bool(candidate.get("is_baseline")) or champions is None


def fold_gini_agreement(metrics: dict[str, Any], champion: dict[str, Any] | None) -> int:
    if champion is None:
        return 0
    candidate_folds = metrics.get("fold_metrics", [])
    champion_folds = champion.get("fold_metrics", [])
    fold_agreement = 0
    for candidate_fold in candidate_folds:
        fold_id = candidate_fold.get("fold")
        champion_fold = next((row for row in champion_folds if row.get("fold") == fold_id), None)
        if champion_fold is None:
            continue
        if float(candidate_fold.get("capped_pp_gini", 0.0)) > float(champion_fold.get("capped_pp_gini", 0.0)):
            fold_agreement += 1
    return fold_agreement


def champion_metric(champion: dict[str, Any] | None, name: str, default: float = 0.0) -> float:
    if champion is None:
        return default
    try:
        value = champion.get("aggregate", {}).get(name, default)
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def gate_decision(metrics: dict[str, Any], champions: dict[str, Any] | None, candidate: dict[str, Any]) -> dict[str, Any]:
    if metrics.get("status") == "crash":
        return {
            "status": "crash",
            "pricing_status": "crash",
            "segmentation_status": "crash",
            "selection_score": 0.0,
            "gate_failures": ["candidate crashed"],
            "gate_results": {},
        }

    aggregate = metrics.get("aggregate", {})
    integrity = metrics.get("integrity", {})
    gate_results: dict[str, bool] = {}
    integrity_failures: list[str] = []

    def record_integrity(name: str, passed: bool) -> None:
        gate_results[name] = bool(passed)
        if not passed:
            integrity_failures.append(name)

    def record_target(failures: list[str], name: str, passed: bool) -> None:
        gate_results[name] = bool(passed)
        if not passed:
            failures.append(name)

    record_integrity("no_policy_leakage", int(integrity.get("policy_leakage_count", 0)) == 0)
    record_integrity("finite_nonnegative_predictions", int(integrity.get("bad_prediction_count", 0)) == 0)
    record_integrity("loss_reconciliation", abs(float(integrity.get("loss_reconciliation_gap", 0.0))) < 1e-6)

    capped_gini = metric(metrics, "capped_pp_gini_mean")
    capped_calibration = metric(metrics, "capped_pp_calibration_gap_mean")
    capped_mae = metric(metrics, "capped_pp_mae_mean")
    capped_rmse = metric(metrics, "capped_pp_rmse_mean")
    raw_gini = metric(metrics, "raw_pp_gini_mean")
    parameter_count = metric(metrics, "parameter_count_mean")
    complexity_penalty = min(parameter_count / 10000.0, 0.02)
    selection_score = capped_gini - 0.25 * abs(capped_calibration) - complexity_penalty

    if is_baseline_run(candidate, champions):
        status = "keep" if not integrity_failures else "discard"
        return {
            "status": status,
            "pricing_status": "baseline",
            "segmentation_status": "baseline",
            "selection_score": selection_score,
            "gate_failures": integrity_failures,
            "gate_results": gate_results,
        }

    assert champions is not None
    pricing_champion = champions.get("pricing")
    segmentation_champion = champions.get("segmentation")

    segmentation_capped_gini_gain = capped_gini - champion_metric(
        segmentation_champion, "capped_pp_gini_mean", capped_gini
    )
    segmentation_raw_gini_gain = raw_gini - champion_metric(segmentation_champion, "raw_pp_gini_mean", raw_gini)
    segmentation_capped_cal_deterioration = abs(capped_calibration) - abs(
        champion_metric(segmentation_champion, "capped_pp_calibration_gap_mean", capped_calibration)
    )
    segmentation_capped_mae_deterioration = (capped_mae - champion_metric(
        segmentation_champion, "capped_pp_mae_mean", capped_mae
    )) / max(abs(champion_metric(segmentation_champion, "capped_pp_mae_mean", capped_mae)), 1e-12)
    segmentation_capped_rmse_deterioration = (capped_rmse - champion_metric(
        segmentation_champion, "capped_pp_rmse_mean", capped_rmse
    )) / max(abs(champion_metric(segmentation_champion, "capped_pp_rmse_mean", capped_rmse)), 1e-12)
    segmentation_fold_agreement = fold_gini_agreement(metrics, segmentation_champion)

    segmentation_failures: list[str] = []
    record_target(
        segmentation_failures,
        "segmentation_minimum_capped_gini_gain",
        segmentation_capped_gini_gain >= GATE_DEFAULTS["minimum_gini_gain"],
    )
    record_target(
        segmentation_failures,
        "segmentation_minimum_fold_agreement",
        segmentation_fold_agreement >= GATE_DEFAULTS["minimum_fold_agreement"],
    )
    record_target(
        segmentation_failures,
        "segmentation_capped_calibration_tolerance",
        segmentation_capped_cal_deterioration <= GATE_DEFAULTS["max_calibration_deterioration"],
    )
    record_target(
        segmentation_failures,
        "segmentation_capped_mae_tolerance",
        segmentation_capped_mae_deterioration <= GATE_DEFAULTS["max_mae_deterioration"],
    )
    record_target(
        segmentation_failures,
        "segmentation_capped_rmse_tolerance",
        segmentation_capped_rmse_deterioration <= GATE_DEFAULTS["max_deviance_deterioration"],
    )
    record_target(
        segmentation_failures,
        "segmentation_raw_gini_not_materially_worse",
        segmentation_raw_gini_gain >= -GATE_DEFAULTS["minimum_gini_gain"],
    )

    pricing_capped_gini_gain = capped_gini - champion_metric(pricing_champion, "capped_pp_gini_mean", capped_gini)
    pricing_raw_gini_gain = raw_gini - champion_metric(pricing_champion, "raw_pp_gini_mean", raw_gini)
    pricing_capped_cal_abs = abs(capped_calibration)
    pricing_champion_capped_cal_abs = abs(
        champion_metric(pricing_champion, "capped_pp_calibration_gap_mean", capped_calibration)
    )
    pricing_capped_mae_deterioration = (capped_mae - champion_metric(
        pricing_champion, "capped_pp_mae_mean", capped_mae
    )) / max(abs(champion_metric(pricing_champion, "capped_pp_mae_mean", capped_mae)), 1e-12)
    pricing_capped_rmse_deterioration = (capped_rmse - champion_metric(
        pricing_champion, "capped_pp_rmse_mean", capped_rmse
    )) / max(abs(champion_metric(pricing_champion, "capped_pp_rmse_mean", capped_rmse)), 1e-12)
    pricing_material_improvement = (
        pricing_capped_gini_gain >= 0.001
        or pricing_capped_mae_deterioration <= -0.002
        or pricing_capped_cal_abs <= max(pricing_champion_capped_cal_abs - 0.001, 0.0)
    )

    pricing_failures: list[str] = []
    record_target(pricing_failures, "pricing_material_improvement", pricing_material_improvement)
    record_target(
        pricing_failures,
        "pricing_capped_gini_not_materially_worse",
        pricing_capped_gini_gain >= -GATE_DEFAULTS["minimum_gini_gain"],
    )
    record_target(
        pricing_failures,
        "pricing_raw_gini_not_materially_worse",
        pricing_raw_gini_gain >= -GATE_DEFAULTS["minimum_gini_gain"],
    )
    record_target(
        pricing_failures,
        "pricing_capped_calibration_tight",
        pricing_capped_cal_abs <= pricing_champion_capped_cal_abs + 0.003,
    )
    record_target(
        pricing_failures,
        "pricing_capped_mae_tolerance",
        pricing_capped_mae_deterioration <= GATE_DEFAULTS["max_mae_deterioration"],
    )
    record_target(
        pricing_failures,
        "pricing_capped_rmse_tolerance",
        pricing_capped_rmse_deterioration <= GATE_DEFAULTS["max_deviance_deterioration"],
    )

    integrity_passed = not integrity_failures
    segmentation_passed = integrity_passed and not segmentation_failures
    pricing_passed = integrity_passed and not pricing_failures
    status = "keep" if pricing_passed or segmentation_passed else "discard"
    pricing_status = "candidate" if pricing_passed else "not_pricing"
    segmentation_status = "candidate" if segmentation_passed else "not_segmentation"
    failures = list(integrity_failures)
    if status == "discard":
        failures.extend(pricing_failures)
        failures.extend(segmentation_failures)
    return {
        "status": status,
        "pricing_status": pricing_status,
        "segmentation_status": segmentation_status,
        "selection_score": selection_score,
        "gate_failures": failures,
        "gate_results": gate_results,
        "deltas": {
            "segmentation_capped_gini_gain": segmentation_capped_gini_gain,
            "segmentation_raw_gini_gain": segmentation_raw_gini_gain,
            "segmentation_capped_calibration_deterioration": segmentation_capped_cal_deterioration,
            "segmentation_capped_mae_deterioration": segmentation_capped_mae_deterioration,
            "segmentation_capped_rmse_deterioration": segmentation_capped_rmse_deterioration,
            "segmentation_fold_agreement": segmentation_fold_agreement,
            "pricing_capped_gini_gain": pricing_capped_gini_gain,
            "pricing_raw_gini_gain": pricing_raw_gini_gain,
            "pricing_capped_calibration_abs": pricing_capped_cal_abs,
            "pricing_champion_capped_calibration_abs": pricing_champion_capped_cal_abs,
            "pricing_capped_mae_deterioration": pricing_capped_mae_deterioration,
            "pricing_capped_rmse_deterioration": pricing_capped_rmse_deterioration,
        },
    }


def write_results_tsv(paths: RunPaths, candidate: dict[str, Any], metrics: dict[str, Any], decision: dict[str, Any]) -> None:
    RESULTS_TSV.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not RESULTS_TSV.exists()
    row = {
        "run_id": paths.run_id,
        "commit": git_short_commit(),
        "candidate_id": candidate.get("id", ""),
        "status": decision["status"],
        "selection_score": f"{decision['selection_score']:.8f}",
        "pricing_status": decision["pricing_status"],
        "segmentation_status": decision["segmentation_status"],
        "capped_pp_gini_mean": f"{metric(metrics, 'capped_pp_gini_mean'):.8f}",
        "capped_pp_calibration_gap_mean": f"{metric(metrics, 'capped_pp_calibration_gap_mean'):.8f}",
        "capped_pp_mae_mean": f"{metric(metrics, 'capped_pp_mae_mean'):.8f}",
        "raw_pp_gini_mean": f"{metric(metrics, 'raw_pp_gini_mean'):.8f}",
        "raw_pp_calibration_gap_mean": f"{metric(metrics, 'raw_pp_calibration_gap_mean'):.8f}",
        "runtime_seconds": f"{metrics.get('runtime_seconds', 0.0):.2f}",
        "gate_failures": ";".join(decision["gate_failures"]),
        "description": str(candidate.get("description", "")).replace("\t", " "),
    }
    with RESULTS_TSV.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=RESULT_COLUMNS, delimiter="\t", lineterminator="\n")
        if needs_header:
            writer.writeheader()
        writer.writerow(row)


def write_decision(paths: RunPaths, candidate: dict[str, Any], metrics: dict[str, Any], decision: dict[str, Any], log_truncated: bool) -> None:
    failures = decision["gate_failures"] or ["none"]
    gate_lines = ["| Gate | Passed |", "| --- | --- |"]
    for gate, passed in decision.get("gate_results", {}).items():
        gate_lines.append(f"| {gate} | {passed} |")
    aggregate = metrics.get("aggregate", {})
    text = f"""# {candidate.get('id', 'candidate')}

## Hypothesis
{candidate.get('hypothesis', 'No hypothesis supplied.')}

## Candidate Change
{candidate.get('description', 'No description supplied.')}

## CV Metric Summary
- Capped pure premium Gini: {aggregate.get('capped_pp_gini_mean')}
- Capped pure premium calibration gap: {aggregate.get('capped_pp_calibration_gap_mean')}
- Capped pure premium MAE: {aggregate.get('capped_pp_mae_mean')}
- Raw pure premium Gini: {aggregate.get('raw_pp_gini_mean')}
- Raw pure premium calibration gap: {aggregate.get('raw_pp_calibration_gap_mean')}
- Runtime seconds: {metrics.get('runtime_seconds')}

## Gate Results
{chr(10).join(gate_lines)}

## Actuarial Interpretation
{candidate.get('actuarial_rationale', 'No actuarial rationale supplied.')}

## Decision
{decision['status']}

Gate failures: {', '.join(failures)}

Log truncated: {log_truncated}
"""
    paths.decision_md.write_text(text, encoding="utf-8")


def update_champions_if_needed(metrics: dict[str, Any], decision: dict[str, Any]) -> None:
    if decision["status"] != "keep":
        return
    champion_payload = dict(metrics)
    champion_payload["decision"] = decision

    champions = load_champions() or {"schema_version": 2, "pricing": None, "segmentation": None}
    if metrics.get("candidate", {}).get("is_baseline"):
        champions["pricing"] = champion_payload
        champions["segmentation"] = champion_payload
    else:
        if decision.get("pricing_status") in {"baseline", "candidate"}:
            champions["pricing"] = champion_payload
        if decision.get("segmentation_status") in {"baseline", "candidate"}:
            champions["segmentation"] = champion_payload
    champions["schema_version"] = 2
    champions["updated_at"] = datetime.now().isoformat(timespec="seconds")
    json_dump(CHAMPIONS_JSON, champions)
    if metrics.get("candidate", {}).get("is_baseline") or not BASELINE_METRICS_JSON.exists():
        json_dump(BASELINE_METRICS_JSON, champion_payload)


def print_summary(paths: RunPaths, candidate: dict[str, Any], metrics: dict[str, Any], decision: dict[str, Any]) -> None:
    print("---")
    print(f"run_id: {paths.run_id}")
    print(f"candidate_id: {candidate.get('id', '')}")
    print(f"status: {decision['status']}")
    print(f"pricing_status: {decision['pricing_status']}")
    print(f"segmentation_status: {decision['segmentation_status']}")
    print(f"selection_score: {decision['selection_score']:.8f}")
    print(f"runtime_seconds: {float(metrics.get('runtime_seconds', 0.0)):.2f}")
    print(f"capped_pp_gini_mean: {metric(metrics, 'capped_pp_gini_mean'):.8f}")
    print(f"capped_pp_calibration_gap_mean: {metric(metrics, 'capped_pp_calibration_gap_mean'):.8f}")
    print(f"capped_pp_mae_mean: {metric(metrics, 'capped_pp_mae_mean'):.8f}")
    print(f"raw_pp_gini_mean: {metric(metrics, 'raw_pp_gini_mean'):.8f}")
    print(f"raw_pp_calibration_gap_mean: {metric(metrics, 'raw_pp_calibration_gap_mean'):.8f}")
    print(f"gate_failures: {';'.join(decision['gate_failures'])}")
    print(f"evidence_dir: {paths.run_dir.relative_to(REPO_ROOT)}")


def run_experiment(candidate: dict[str, Any]) -> dict[str, Any]:
    ensure_directories()
    paths = make_run_paths(candidate)
    paths.run_dir.mkdir(parents=True, exist_ok=False)
    json_dump(paths.candidate_json, candidate)

    champion = load_champions()
    return_code, timed_out, runtime_seconds, log_truncated = run_r_candidate(paths)
    if return_code == 0 and paths.metrics_json.exists():
        metrics = json.loads(paths.metrics_json.read_text(encoding="utf-8"))
        metrics["status"] = "ok"
    else:
        metrics = {
            "candidate_id": candidate.get("id", ""),
            "status": "crash",
            "aggregate": {},
            "integrity": {},
            "diagnostics": {},
            "return_code": return_code,
            "timed_out": timed_out,
        }

    metrics["runtime_seconds"] = runtime_seconds
    metrics["timed_out"] = timed_out
    metrics["log_truncated"] = log_truncated
    decision = gate_decision(metrics, champion, candidate)
    if timed_out:
        decision["status"] = "discard"
        decision["gate_failures"] = sorted(set(decision["gate_failures"] + ["runtime timeout"]))
    metrics["decision"] = decision
    json_dump(paths.metrics_json, metrics)
    write_decision(paths, candidate, metrics, decision, log_truncated)
    write_results_tsv(paths, candidate, metrics, decision)
    update_champions_if_needed(metrics, decision)
    print_summary(paths, candidate, metrics, decision)
    return metrics


if __name__ == "__main__":
    print("prepare.py is an immutable harness. Run autoresearch/train.py instead.", file=sys.stderr)
    raise SystemExit(1)
