"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_power_brand_dual_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Power:Brand to both raw and capped severity."
    ),
    "hypothesis": (
        "Power:Brand in capped severity was the strongest transparent pricing "
        "near miss. Adding the same repair-cost interaction to raw severity may "
        "improve raw monitoring metrics while preserving the capped gain."
    ),
    "actuarial_rationale": (
        "Power and brand are plausible severity dimensions tied to vehicle "
        "repair cost. This remains a transparent GLM, but should be rejected if "
        "the extra sparse interaction complexity is not supported by CV metrics."
    ),
    "frequency": {
        "use_splines": True,
        "interactions": [],
    },
    "severity": {
        "use_splines": True,
        "interactions": ["Power:Brand"],
    },
    "capped_severity": {
        "use_splines": True,
        "interactions": ["Power:Brand"],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
