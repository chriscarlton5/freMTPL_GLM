"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_power_brand_capped_calibrated",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Power:Brand to capped severity and applies component calibration "
        "scalars estimated inside each training fold."
    ),
    "hypothesis": (
        "Power:Brand capped severity was the strongest transparent pricing "
        "near miss, improving capped Gini, calibration, and MAE slightly. "
        "Fold-internal calibration may turn that into a material pricing-level "
        "improvement without leakage."
    ),
    "actuarial_rationale": (
        "This is a transparent pricing candidate. Power and brand are plausible "
        "repair-cost dimensions, and calibration is estimated only inside each "
        "outer training fold to protect the validation fold."
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
        "interactions": ["Power:Brand"],
    },
    "calibration": {
        "component_scalars": True,
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
