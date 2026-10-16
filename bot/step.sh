#!/bin/bash
# One check step: run ~3-4 game months, pause, save, print health, then the city check (audit.py)
# and the stall alarm (stall.py). Any FAIL or STALL must be dealt with before the next step.
# Every step's output is kept (record_step.py: checks.jsonl, unlocks.json, yearly save copy, budget row);
# at the first step of each game year a screenshot of the Budget window is saved too.
cd "$(dirname "$0")"
out=/tmp/sc/step_out.txt
{
./sc run cheetah ${1:-1.5}; ./sc pause
./sc save | cut -c1-160
python3 -I -c "
import sys;sys.path.insert(0,'.');import sc2parse as p;m=p.parse(p.SAVE);g=m['graphs'];c=p.chunks(p.SAVE);b=c['XBLD'];bt=c['XBIT']
print('spare water/power',g['water_pct'][:1],g['power_pct'][:1],'unpowered',sum(1 for i in range(16384) if 0x70<=b[i]<0xC0 and not bt[i]&64),'dry',sum(1 for i in range(16384) if 0x70<=b[i]<0xC0 and not bt[i]&16),'rubble',sum(1 for v in b if 1<=v<=4))"
python3 -I audit.py | grep -v "^OK"
python3 -I stall.py
python3 -I pace.py
echo "paused: $(./sc paused)"
} 2>&1 | grep -v -e xdo -e "Can't open display" | tee $out
shot=$(python3 -I record_step.py $out | sed -n 's/^BUDGET_SHOT //p')
if [ -n "$shot" ]; then
  dash=$(python3 -c "import json;print(json.load(open('run.json'))['dashboard'])")
  mkdir -p "../$dash/budget"
  ./sc click 47 297; sleep 1.2; ./sc snap /tmp/sc/budget_full.png >/dev/null
  convert /tmp/sc/budget_full.png -crop 330x250+158+112 "../$dash/budget/$shot.png"
  ./sc click 459 123; sleep 0.5; ./sc pause
fi
