"""Tax controller (after attempt 12): let each zone's demand set its tax rate.

Every attempt left money on the table while a demand bar sat at maximum (attempts 9, 11, 12: shops or
factories at max for years at 6-8%), and every attempt ran out of money. Tax income is about
1.29 x population x rate, so the rate is the only lever on income per person.

Rule, per zone (homes, shops, factories), once the city has 3,000+ people:
  demand >= 1000                    -> rate + 1 (up to MAX)  (1800 in attempt 13 until Dec 2006: homes sat at 6% with demand 500-1500 while the budget ran -$818/yr)
  demand <= -300 at two checks in a row -> rate - 1 (down to MIN)
One step per zone per check. Changes are made in the game's tax window, verified from the save, and
logged to the dashboard. Enabled per attempt with "taxctl": true in run.json; play.sh runs it each step.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = "/tmp/sc/taxctl.json"
MIN, MAX = 5, 12
KMAX = {}
ARROW_X = {"res": 249, "com": 327, "ind": 397}
UP_Y, DOWN_Y = 302, 311


def sc(*a):
    subprocess.run([os.path.join(HERE, "sc")] + [str(x) for x in a], capture_output=True)


def decide(m, state):
    moves = {}
    if m["population"] < 3000:
        return moves
    for k in ("res", "com", "ind"):
        d, r = m["demand"][k], m["tax"][k]
        neg = state.get(k, 0) + 1 if d <= -300 else 0
        state[k] = neg
        if r < MIN:                      # raise to the floor (attempt 17: homes 6% minimum)
            moves[k] = 1
        elif d >= 1000 and r < KMAX.get(k, MAX):
            moves[k] = 1
        elif neg >= 2 and r > MIN:
            moves[k] = -1
            state[k] = 0
    return moves


def main():
    run = json.load(open(os.path.join(HERE, "run.json")))
    if not run.get("taxctl"):
        return
    m = p.parse(p.SAVE)
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    global MAX
    MAX = run.get("taxmax", MAX)         # attempt 14: a ceiling per attempt (12% factory tax broke attempt 13)
    global MIN
    MIN = run.get("taxmin", MIN)
    global KMAX                          # attempt 19: per-zone ceilings (factory demand fell to -800 at 10%)
    KMAX = {k: run["taxmax_" + k] for k in ("res", "com", "ind") if "taxmax_" + k in run}         # attempt 17: homes sat at 4% all of attempt 16 while unemployment, not tax, held them back
    if sys.argv[1:2] == ["set"]:          # taxctl.py set R C I : set rates directly (start of an attempt)
        want = dict(zip(("res", "com", "ind"), map(int, sys.argv[2:5])))
        moves = {k: want[k] - m["tax"][k] for k in want if want[k] != m["tax"][k]}
    else:
        moves = decide(m, state)
    json.dump(state, open(STATE, "w"))
    if not moves:
        print("TAXCTL: no change (taxes %s)" % m["tax"])
        return
    sc("click", 47, 297); subprocess.run(["sleep", "1.2"]); sc("click", 437, 165); subprocess.run(["sleep", "1"])
    for k, d in moves.items():
        for _ in range(abs(d)):
            sc("click", ARROW_X[k], UP_Y if d > 0 else DOWN_Y); subprocess.run(["sleep", "0.3"])
    sc("click", 430, 307); subprocess.run(["sleep", "0.6"])
    sc("click", 459, 123); subprocess.run(["sleep", "0.5"])
    sc("pause")
    subprocess.run([os.path.join(HERE, "sc"), "save"], capture_output=True)
    after = p.parse(p.SAVE)["tax"]
    ok = all(after[k] == m["tax"][k] + d for k, d in moves.items())
    names = {"res": "homes", "com": "shops", "ind": "factories"}
    text = "Tax controller: " + ", ".join("%s %d -> %d (demand %d)" % (names[k], m["tax"][k], after[k], m["demand"][k])
                                          for k in moves)
    print("TAXCTL:", text, "" if ok else "- CHECK FAILED, taxes now %s" % after)
    if ok:
        subprocess.run([os.path.join(HERE, "sc"), "log", "budget", text], capture_output=True)
    else:
        print("FAIL tax controller could not set the rates")


if __name__ == "__main__":
    main()
