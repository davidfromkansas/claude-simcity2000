#!/bin/bash
# One check step: run ~3-4 game months, pause, save, print health, then the city check (audit.py)
# and the stall alarm (stall.py). Any FAIL or STALL must be dealt with before the next step.
cd "$(dirname "$0")"
./sc run cheetah ${1:-1.5}; ./sc pause
./sc save | cut -c1-160
python3 -I -c "
import sys;sys.path.insert(0,'.');import sc2parse as p;m=p.parse(p.SAVE);g=m['graphs'];c=p.chunks(p.SAVE);b=c['XBLD'];bt=c['XBIT']
print('spare water/power',g['water_pct'][:1],g['power_pct'][:1],'unpowered',sum(1 for i in range(16384) if 0x70<=b[i]<0xC0 and not bt[i]&64),'dry',sum(1 for i in range(16384) if 0x70<=b[i]<0xC0 and not bt[i]&16),'rubble',sum(1 for v in b if 1<=v<=4))"
python3 -I audit.py | grep -v "^OK"
python3 -I stall.py
echo "paused: $(./sc paused)"
