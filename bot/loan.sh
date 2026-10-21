#!/bin/bash
# loan.sh : issue one $10,000 loan in a single call (attempt 13 left the game running six months while a
# loan dialog sat open). Re-pauses, then checks from the save that the loan count went up by one and
# updates run.json. Exits 1 if the game refused (e.g. "credit rating" at founding).
cd "$(dirname "$0")"
# Claudeville 4 attempts 1-2: loans outran tax (each $10k costs ~$500 a year for ever) and both cities ended at
# -$100,000. From 20,000 people a loan is refused when cash projected to 2050 (last January's tax x1.15 for
# ordinances x1.5 for growth, minus ~$500 a loan and service upkeep) would fall below -$80,000 (LOAN_OK=1 overrides).
if [ -z "$LOAN_OK" ]; then
  python3 -I - <<'PY' || exit 1
import json, os, sys
sys.path.insert(0, ".")
import sc2parse as p
r = json.load(open("run.json")); d = p.parse(p.SAVE)
pop, bonds, cash = d.get("population", 0), r.get("bonds", 0), d.get("money", 0)
year = int(str(d.get("date", "Jan 2000")).split()[-1])
b = []
try:
    b = json.load(open(os.path.join("..", r.get("dashboard", ""), "data", "budget.json")))
except Exception:
    pass
tax = b[-1].get("est_property_tax", 0) if b else 0
income = tax * 1.15 * 1.5               # ordinances ~15%; income assumed to grow by half on average as the city grows
fixed = 400 + 100 * d.get("services", {}).get("fire", {}).get("count", 0) // 2   # rough service upkeep
yearly = income - (bonds + 1) * 500 - fixed
end = cash + 10000 + yearly * (2050 - year)
# attempt 7: 32 loans for ~92,000 people (~2,900 each) ran out of money; attempt 6 (the best) kept ~3,300-4,400 each
floor = r.get("loan_floor", 3000)   # attempt 11: 4,000 (attempt 10 went broke at ~2,600 per loan)
if pop >= 30000 and pop / (bonds + 1) < floor:
    print("LOAN: refused - %d people for %d loans is under %d per loan (attempts 7 and 10 went broke under 3,000; LOAN_OK=1 to override)" % (pop, bonds + 1, floor))
    sys.exit(1)
if pop >= 20000 and end < -80000:
    print("LOAN: refused by the loan budget - cash projected to 2050 with this loan: ~$%d (game over near -$100k; LOAN_OK=1 to override)" % end)
    sys.exit(1)
print("LOAN budget: projected 2050 cash ~$%d" % end)
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
