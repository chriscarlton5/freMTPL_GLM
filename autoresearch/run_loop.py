#!/usr/bin/env python3
"""Autonomous research loop - local MTPL experiments with tracked evidence."""

import json, subprocess, sys, time, random, argparse
from pathlib import Path

RP = Path(".")
TP = RP / "autoresearch/train.py"
CHAMP = RP / "autoresearch/evidence/champions.json"
RESULTS = RP / "autoresearch/evidence/results.tsv"
LOOP_STATE = RP / "autoresearch/evidence/loop_state.json"
GIT_QUEUE = RP / "autoresearch/scratch/git_queue"

def champion(): 
    return json.load(open(CHAMP))["pricing"]["aggregate"]["capped_pp_gini_mean"]

def sh(args, check=False):
    return subprocess.run(args, cwd=str(RP), capture_output=True, text=True, check=check)

def run():
    out = subprocess.run([sys.executable, str(TP)], capture_output=True, text=True, timeout=240, cwd=str(RP)).stdout
    for line in out.split("\n"):
        if "capped_pp_gini_mean" in line:
            return float(line.split(":")[1].strip())
    return 0.0

def current_iter():
    if not LOOP_STATE.exists():
        return 0
    try:
        return int(json.load(open(LOOP_STATE)).get("iter", 0))
    except Exception:
        return 0

def latest_run_dir():
    if not RESULTS.exists():
        return None
    lines = [line for line in RESULTS.read_text().splitlines() if line.strip()]
    if len(lines) <= 1:
        return None
    run_id = lines[-1].split("\t", 1)[0]
    path = RP / "autoresearch/evidence/runs" / run_id
    return str(path).replace("\\", "/") if path.exists() else None

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
    TP.write_text(f'from prepare import run_experiment\nCANDIDATE = {content}\nif __name__ == "__main__": run_experiment(CANDIDATE)\n')

def commit_and_push(message, paths):
    GIT_QUEUE.mkdir(parents=True, exist_ok=True)
    job_name = f"{int(time.time() * 1000)}_{message.lower().replace(' ', '_').replace(':', '')}.json"
    job_path = GIT_QUEUE / job_name
    job_path.write_text(json.dumps({"message": message, "paths": paths, "push": True}, indent=2) + "\n")

    deadline = time.time() + 120
    while job_path.exists() and time.time() < deadline:
        time.sleep(1)
    return not job_path.exists()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-iterations", type=int, default=0)
    args = parser.parse_args()

    champ = champion()
    start = current_iter()
    print(f"Starting | Champion: {champ:.4f} | Iteration: {start}")

    completed = 0
    while args.max_iterations <= 0 or completed < args.max_iterations:
        i = start + completed
        gen(i, champ)
        commit_and_push(f"auto: candidate iter{i+1}", ["autoresearch/train.py"])

        gini = run()
        was_new = gini > champ
        if was_new:
            champ = gini

        run_dir = latest_run_dir()
        LOOP_STATE.write_text(json.dumps({"champion": champ, "iter": i + 1}, indent=2) + "\n")
        evidence_paths = ["autoresearch/evidence/results.tsv", "autoresearch/evidence/champions.json", "autoresearch/evidence/loop_state.json"]
        if run_dir:
            evidence_paths.append(run_dir)
        commit_and_push(f"auto: evidence iter{i+1} gini{gini:.4f}", evidence_paths)

        label = "NEW" if was_new else "run"
        print(f"[{label}] iter={i+1} gini={gini:.4f} champion={champ:.4f}")
        completed += 1

if __name__ == "__main__":
    main()
