#!/usr/bin/env python3
"""Autonomous research loop - minimal, robust."""

import json, subprocess, sys, time, random
from pathlib import Path

RP = Path(".")
TP = RP / "autoresearch/train.py"
CHAMP = RP / "autoresearch/evidence/champions.json"

def champion(): 
    return json.load(open(CHAMP))["pricing"]["aggregate"]["capped_pp_gini_mean"]

def run():
    out = subprocess.run([sys.executable, str(TP)], capture_output=True, text=True, timeout=180, cwd=str(RP)).stdout
    for line in out.split("\n"):
        if "capped_pp_gini_mean" in line:
            return float(line.split(":")[1].strip())
    return 0.0

def gen(i, champ):
    random.seed(int(time.time()*1000) + i)
    
    # 65% fine-tune, 20% explore, 15% paradigm
    r = random.random()
    if r < 0.15:
        s, ff, l2, leaves = "ps", random.uniform(0.44, 0.52), random.uniform(12, 18), random.randint(12, 20)
    elif r < 0.35:
        s, ff, l2, leaves = "ex", random.uniform(0.48, 0.54), random.uniform(10, 16), random.randint(14, 22)
    else:
        s, ff, l2, leaves = "ft", 0.515 + random.uniform(-0.008, 0.008), 13.0 + random.uniform(-0.4, 0.4), 16 + random.choice([-2,-1,0,1,2])
    
    ff = max(0.48, min(0.54, ff))
    l2 = max(8, min(18, l2))
    leaves = max(12, min(28, leaves))
    
    cand = {
        "id": f"lightgbm_{s}_{i+1:04d}", "is_baseline": False, "model_type": "lightgbm",
        "description": f"{s}: FF={ff:.3f} L2={l2:.1f}", "hypothesis": s, "actuarial_rationale": "auto",
        "lightgbm": {
            "nrounds": 175, "early_stopping_rounds": 22,
            "frequency_grid": [
                {"num_leaves": leaves, "min_data_in_leaf": 1700, "learning_rate": 0.036,
                 "feature_fraction": ff, "bagging_fraction": ff, "lambda_l2": l2},
                {"num_leaves": leaves+8, "min_data_in_leaf": 1400, "learning_rate": 0.031,
                 "feature_fraction": ff-0.05, "bagging_fraction": ff, "lambda_l2": l2-2},
            ],
            "severity_grid": [
                {"num_leaves": 7, "min_data_in_leaf": 200, "learning_rate": 0.036,
                 "feature_fraction": ff, "bagging_fraction": ff, "lambda_l2": l2-2},
                {"num_leaves": 11, "min_data_in_leaf": 150, "learning_rate": 0.031,
                 "feature_fraction": ff-0.05, "bagging_fraction": ff, "lambda_l2": l2-3},
            ],
            "capped_severity_grid": [
                {"num_leaves": 7, "min_data_in_leaf": 200, "learning_rate": 0.036,
                 "feature_fraction": ff, "bagging_fraction": ff, "lambda_l2": l2-2},
                {"num_leaves": 11, "min_data_in_leaf": 150, "learning_rate": 0.031,
                 "feature_fraction": ff-0.05, "bagging_fraction": ff, "lambda_l2": l2-3},
            ],
        },
    }
    content = json.dumps(cand, indent=2).replace('"is_baseline": false', '"is_baseline": False')
    TP.write_text(f'from prepare import run_experiment\nCANDIDATE = {content}\nif __name__ == "__main__": run_experiment(CANDIDATE)')

champ = champion()
print(f"Starting | Champion: {champ:.4f}")

i = 0
while True:
    gen(i, champ)
    gini = run()
    
    improved = gini > champ + 0.001
    if improved:
        champ = gini
        print(f"[NEW] {gini:.4f}")
    else:
        print(f"{i+1}: {gini:.4f}")
    
    subprocess.run(["git", "add", "autoresearch/train.py"], cwd=RP, capture_output=True)
    subprocess.run(["git", "commit", "-m", f"auto: iter{i+1} gini{gini:.4f}"], cwd=RP, capture_output=True)
    
    i += 1
    if i % 20 == 0:
        print(f"[CHECK] {i} iterations, champ={champ:.4f}")