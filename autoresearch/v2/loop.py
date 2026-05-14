"""Autonomous v2 research loop.

This loop generates governed candidate JSON files from a curated idea queue and
submits each candidate to the v2 controller. It stops when a candidate is
promoted or when the requested iteration budget is exhausted.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
V2_DIR = Path(__file__).resolve().parent
GENERATED_DIR = V2_DIR / "generated"
CONTROLLER = V2_DIR / "controller.py"
BENCHMARK_PATH = V2_DIR / "candidates" / "lightgbm_regularized_challenger.json"
EVIDENCE_DIR = V2_DIR.parent / "evidence" / "v2"
REGISTRY_PATH = EVIDENCE_DIR / "registry.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def registry_rows() -> list[dict[str, Any]]:
    if not REGISTRY_PATH.exists():
        return []
    return load_json(REGISTRY_PATH).get("runs", [])


def attempted_candidate_ids() -> set[str]:
    return {str(row.get("candidate_id")) for row in registry_rows()}


def latest_status() -> str | None:
    rows = registry_rows()
    if not rows:
        return None
    return str(rows[-1].get("status"))


def base_lightgbm_model() -> dict[str, Any]:
    return deepcopy(load_json(BENCHMARK_PATH)["model_spec"])


def wrapper(
    candidate_id: str,
    idea_family: str,
    hypothesis: str,
    expected_mechanism: str,
    intended_metric_improvements: list[str],
    known_tradeoff_risk: str,
    parent_candidate_id: str | None,
    model_spec: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "candidate_id": candidate_id,
        "idea_family": idea_family,
        "hypothesis": hypothesis,
        "expected_mechanism": expected_mechanism,
        "intended_metric_improvements": intended_metric_improvements,
        "known_tradeoff_risk": known_tradeoff_risk,
        "parent_candidate_id": parent_candidate_id,
        "model_spec": model_spec,
    }


def glm_candidate(candidate_id: str, use_splines: bool, interactions: list[str], hypothesis: str) -> dict[str, Any]:
    model_spec = {
        "id": candidate_id,
        "is_baseline": False,
        "model_type": "glm",
        "description": f"V2 transparent GLM with splines={use_splines} and interactions={','.join(interactions) or 'none'}.",
        "hypothesis": hypothesis,
        "actuarial_rationale": "Transparent GLM structure tests whether stable actuarial interactions can improve pricing without black-box search.",
        "frequency": {
            "use_splines": use_splines,
            "interactions": interactions,
        },
        "severity": {
            "use_splines": use_splines,
            "interactions": interactions,
        },
        "capped_severity": {
            "use_splines": use_splines,
            "interactions": interactions,
        },
        "calibration": {
            "component_scalars": False,
        },
    }
    return wrapper(
        candidate_id=candidate_id,
        idea_family="transparent_glm",
        hypothesis=hypothesis,
        expected_mechanism="Replace local LightGBM tuning with stable, reviewable interactions across frequency and severity components.",
        intended_metric_improvements=["holdout_capped_pp_gini", "calibration", "interpretability"],
        known_tradeoff_risk="Transparent interactions may be too rigid or too parameter-heavy to beat the LightGBM benchmark.",
        parent_candidate_id="baseline_enhanced_glm_splines",
        model_spec=model_spec,
    )


def lightgbm_variant(candidate_id: str, transform: str, hypothesis: str) -> dict[str, Any]:
    model_spec = base_lightgbm_model()
    model_spec["id"] = candidate_id
    model_spec["description"] = f"V2 LightGBM structural variant: {transform}."
    model_spec["hypothesis"] = hypothesis
    model_spec["actuarial_rationale"] = (
        "V2 variant changes model structure or stability constraints relative to the current benchmark; "
        "it is not a local search around best_191."
    )

    grids = [
        model_spec["lightgbm"]["frequency_grid"],
        model_spec["lightgbm"]["severity_grid"],
        model_spec["lightgbm"]["capped_severity_grid"],
    ]
    if transform == "higher_leaf_floor":
        for grid in grids:
            for params in grid:
                params["min_data_in_leaf"] = int(round(params["min_data_in_leaf"] * 1.25))
    elif transform == "lower_learning_rate":
        model_spec["lightgbm"]["nrounds"] = 180
        model_spec["lightgbm"]["early_stopping_rounds"] = 20
        for grid in grids:
            for params in grid:
                params["learning_rate"] = round(params["learning_rate"] * 0.75, 4)
    elif transform == "conservative_feature_fraction":
        for grid in grids:
            for params in grid:
                params["feature_fraction"] = max(0.75, round(params["feature_fraction"] - 0.1, 4))
                params["bagging_fraction"] = max(0.80, round(params["bagging_fraction"] - 0.05, 4))
    elif transform == "stronger_l2":
        for grid in grids:
            for params in grid:
                params["lambda_l2"] = round(params["lambda_l2"] * 1.5, 4)
    else:
        raise ValueError(f"Unknown transform: {transform}")

    return wrapper(
        candidate_id=candidate_id,
        idea_family="model_structure" if transform in {"higher_leaf_floor", "lower_learning_rate"} else "stability",
        hypothesis=hypothesis,
        expected_mechanism="Change regularization structure enough to test generalization, while staying close to the defensible initial GBM basin.",
        intended_metric_improvements=["holdout_capped_pp_gini", "calibration", "seed_stability"],
        known_tradeoff_risk="May reduce useful segmentation by over-regularizing the already strong benchmark.",
        parent_candidate_id="lightgbm_regularized_challenger",
        model_spec=model_spec,
    )


def idea_queue() -> list[dict[str, Any]]:
    return [
        glm_candidate(
            "v2_glm_age_car_interaction",
            True,
            ["DriverAgeBand:CarAgeBand"],
            "Driver age and vehicle age may interact in a stable, actuarially explainable way.",
        ),
        glm_candidate(
            "v2_glm_power_brand_interaction",
            True,
            ["Power:Brand"],
            "Vehicle power by brand may capture stable vehicle-risk segmentation without GBM opacity.",
        ),
        glm_candidate(
            "v2_glm_age_powerbrand",
            True,
            ["DriverAgeBand:CarAgeBand", "Power:Brand"],
            "Combine the strongest transparent driver/vehicle structure with vehicle-type segmentation.",
        ),
        lightgbm_variant(
            "v2_lgb_higher_leaf_floor",
            "higher_leaf_floor",
            "Raise leaf floors to reduce variance while preserving the initial LightGBM structure.",
        ),
        lightgbm_variant(
            "v2_lgb_lower_learning_rate",
            "lower_learning_rate",
            "Use slower boosting to test whether smoother ensembles improve holdout capped Gini.",
        ),
        lightgbm_variant(
            "v2_lgb_conservative_feature_fraction",
            "conservative_feature_fraction",
            "Moderate feature/bagging randomness without entering the failed best_191 low-fraction basin.",
        ),
        lightgbm_variant(
            "v2_lgb_stronger_l2",
            "stronger_l2",
            "Increase L2 penalties to test whether the benchmark can be stabilized without losing ranking.",
        ),
    ]


def run_controller(candidate_path: Path) -> tuple[str, str]:
    completed = subprocess.run(
        [sys.executable, str(CONTROLLER), str(candidate_path.relative_to(REPO_ROOT))],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    output = (completed.stdout or "") + (completed.stderr or "")
    status = "error"
    for line in output.splitlines():
        if line.startswith("status:"):
            status = line.split(":", 1)[1].strip()
            break
    if completed.returncode != 0:
        status = "error"
    return status, output


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the v2 autonomous research loop.")
    parser.add_argument("--max-iterations", type=int, default=3)
    args = parser.parse_args()

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    attempted = attempted_candidate_ids()
    completed = 0
    for candidate in idea_queue():
        if completed >= args.max_iterations:
            break
        candidate_id = candidate["candidate_id"]
        if candidate_id in attempted:
            continue
        candidate_path = GENERATED_DIR / f"{candidate_id}.json"
        write_json(candidate_path, candidate)
        status, output = run_controller(candidate_path)
        log_path = GENERATED_DIR / f"{candidate_id}.controller.log"
        log_path.write_text(output, encoding="utf-8")
        completed += 1
        print(f"{datetime.now().isoformat(timespec='seconds')} {candidate_id}: {status}")
        if status == "promote":
            print(f"promotion_found: {candidate_id}")
            return
    print(f"completed: {completed}")
    print(f"latest_status: {latest_status()}")


if __name__ == "__main__":
    main()
