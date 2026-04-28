"""Editable MTPL autoresearch candidate.

Experiment agents may edit this file only. The evaluation harness, data split,
metrics, and hard gates live in prepare.py and autoresearch/r/.
"""

from prepare import run_experiment


CANDIDATE = {
    "id": "simple_glm_power_brand_capped_severity",
    "is_baseline": False,
    "model_type": "glm",
    "description": (
        "Simpler GLM using linear DriverAge, CarAge, and logDensity terms in "
        "all components; adds Power:Brand to capped severity only."
    ),
    "hypothesis": (
        "The Power:Brand capped-severity signal may not require spline "
        "flexibility. A simpler linear GLM could retain the small capped-pricing "
        "gain with better parsimony and stability."
    ),
    "actuarial_rationale": (
        "This is a transparent parsimony test. Linear continuous effects are "
        "easier to explain than splines, but the model must not give up too much "
        "predictive power or calibration."
    ),
    "frequency": {
        "use_splines": False,
        "interactions": [],
    },
    "severity": {
        "use_splines": False,
        "interactions": [],
    },
    "capped_severity": {
        "use_splines": False,
        "interactions": ["Power:Brand"],
    },
}


if __name__ == "__main__":
    run_experiment(CANDIDATE)
