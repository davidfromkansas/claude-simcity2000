#!/bin/bash
# Re-calibrate tile.py: place a road tile at screen center on empty land, read it from the save, then bulldoze it.
# usage: calib.sh SX SY STEP   (SX,SY must be empty flat land)
cd "$(dirname "$0")"
before=$(python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;c=p.chunks(p.SAVE);b=c['XBLD'];print(' '.join(str(i) for i in range(16384) if 0x1d<=b[i]<=0x2b))")
./sc tool 22 105 55 113; sleep 0.3; ./sc click $1 $2; sleep 0.3; ./sc save >/dev/null
python3 -I - "$before" "$1" "$2" "$3" <<'PY'
import sys; sys.path.insert(0,'.'); import sc2parse as p
before=set(map(int,sys.argv[1].split()))
c=p.chunks(p.SAVE); b=c['XBLD']
new=[i for i in range(16384) if 0x1d<=b[i]<=0x2b and i not in before]
if len(new)!=1: print('calibration failed', new); sys.exit(1)
x,y=new[0]%128,new[0]//128
import struct
a=struct.unpack('>16384H',c['ALTM'])[new[0]]&31
import json; s=float(sys.argv[4]); sx,sy=float(sys.argv[2]),float(sys.argv[3])
json.dump({"s":s,"ox":sx-s*(y-x),"oy":sy-s/2*(x+y),"alt":a},open('/tmp/sc/cal.json','w'))
print('calibrated on tile',x,y,'alt',a)
PY
./sc click 22 58; sleep 0.2; ./sc click $1 $2; sleep 0.2
