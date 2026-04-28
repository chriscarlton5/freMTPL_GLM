"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "enhanced_glm_power_brand_raw_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Enhanced GLM using natural splines for DriverAge, CarAge, and "
        "logDensity in frequency, raw severity, and capped severity; adds "
        "Power:Brand to raw severity only."
    ),
    "hypothesis": (
        "Power:Brand materially improved raw monitoring when added to both "
        "severity components. Restricting it to raw severity may keep that "
        "signal while avoiding extra capped-pricing complexity."
    ),
    "actuarial_rationale": (
        "Power and brand are plausible repair-cost variables for large raw "
        "claims. This candidate intentionally leaves capped severity unchanged "
        "to protect the stable pricing target."
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
        "interactions": [],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
