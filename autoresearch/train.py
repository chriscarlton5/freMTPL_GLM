"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_component_scalars",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Baseline transparent enhanced GLM using natural splines for DriverAge, "
        "CarAge, and logDensity in frequency, raw severity, and capped severity; "
        "adds component-level frequency, raw severity, and capped severity "
        "calibration scalars estimated only inside each training fold."
    ),
    "hypothesis": (
        "Fold-internal component calibration can improve loss-cost level while "
        "preserving the enhanced GLM's transparent segmentation structure."
    ),
    "actuarial_rationale": (
        "Component scalars are easy to audit and separate frequency, raw severity, "
        "and capped severity bias. They should only be retained if they improve "
        "calibration without weakening capped pure premium lift or stability."
    ),
    "frequency": {
        "use_splines": True,
        "interactions": [],
    },
    "severity": {
        "use_splines": True,
        "interactions": [],
    },
    "capped_severity": {
        "use_splines": True,
        "interactions": [],
    },
    "calibration": {
        "component_scalars": True,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
