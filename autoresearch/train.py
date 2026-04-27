"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "baseline_enhanced_glm_splines",
    "is_baseline": True,
    "model_type": "glm",
    "description": (
        "Baseline transparent enhanced GLM using natural splines for DriverAge, "
        "CarAge, and logDensity in frequency, raw severity, and capped severity; "
        "no interactions or calibration scalars."
    ),
    "hypothesis": (
        "The current report's enhanced GLM structure is the right starting "
        "champion for transparent actuarial segmentation."
    ),
    "actuarial_rationale": (
        "Natural splines allow smooth nonlinear age and density effects while "
        "remaining reviewable, parsimonious, and defensible compared with a "
        "direct black-box pricing level."
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
        "component_scalars": False,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
