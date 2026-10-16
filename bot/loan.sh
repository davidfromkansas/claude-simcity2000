#!/bin/bash
# loan.sh : issue one $10,000 loan in a single call (attempt 13 left the game running six months while a
# loan dialog sat open). Re-pauses, then checks from the save that the loan count went up by one and
# updates run.json. Exits 1 if the game refused (e.g. "credit rating" at founding).
cd "$(dirname "$0")"
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
