#!/bin/bash
# loan.sh : issue one $10,000 loan in a single call (attempt 13 left the game running six months while a
# loan dialog sat open). Re-pauses, then checks from the save that the loan count went up by one and
# updates run.json. Exits 1 if the game refused (e.g. "credit rating" at founding).
cd "$(dirname "$0")"
# Claudeville 4 attempts 1-2: loans outran tax (each $10k costs ~$500 a year for ever) and both cities ended at
# -$100,000. From 20,000 people a loan needs the last January's tax + ordinances to cover the bond payments
# minus ~$2,500 afterwards - a deficit no bigger than that lasts to 2050 (LOAN_OK=1 overrides; say why in the log).
if [ -z "$LOAN_OK" ]; then
  python3 -I - <<'PY' || exit 1
import json, os, sys
sys.path.insert(0, ".")
import sc2parse as p
r = json.load(open("run.json")); d = p.parse(p.SAVE)
pop, bonds = d.get("population", 0), r.get("bonds", 0)
b = []
try:
    b = json.load(open(os.path.join("..", r.get("dashboard", ""), "data", "budget.json")))
except Exception:
    pass
tax = b[-1].get("est_property_tax", 0) if b else 0
income = tax * 1.15                      # ordinances add ~15%
need = (bonds + 1) * 500 - 2500       # a ~$2.5k yearly deficit spends the -$100k margin over ~40 years
if pop >= 20000 and income < need:
    print("LOAN: refused by the loan budget - yearly tax ~$%d vs ~$%d of bond payments after this loan (LOAN_OK=1 to override)" % (income, need))
    sys.exit(1)
PY
fi
./sc save >/dev/null; before=$(python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;print(p.parse(p.SAVE)['money'])")
./sc pause >/dev/null 2>&1
./sc click 47 297; sleep 1.2; ./sc click 437 203; sleep 1.2; ./sc click 290 307; sleep 1.2
./sc click 267 260; sleep 1; ./sc click 430 307; sleep 0.8; ./sc click 430 307; sleep 0.6; ./sc click 459 123; sleep 0.5
./sc pause >/dev/null 2>&1; ./sc save >/dev/null
after=$(python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;print(p.parse(p.SAVE)['money'])")
if [ $((after - before)) -ge 9000 ]; then
  python3 -c "import json;r=json.load(open('run.json'));r['bonds']=r.get('bonds',0)+1;json.dump(r,open('run.json','w'));print('LOAN: ok, loans now',r['bonds'])"
  ./sc save | cut -c1-60; echo "paused: $(./sc paused)"
else echo "LOAN: refused or failed (cash did not rise by $10,000)"; exit 1; fi
