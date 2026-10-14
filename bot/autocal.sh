#!/bin/bash
# autocal.sh : find where the view is. Places one road tile at a few screen spots until one lands,
# reads its tile from the save, calibrates tile.py (zoom 3), then bulldozes it.
cd "$(dirname "$0")"
roads() { python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;c=p.chunks(p.SAVE);b=c['XBLD'];print(' '.join(str(i) for i in range(16384) if 0x1d<=b[i]<=0x2b))"; }
./sc key Escape; ./sc save >/dev/null; before=$(roads)
./sc tool 22 105 55 113; sleep 0.3
for pt in "330 250" "450 360" "200 360" "470 150" "200 160" "560 260" "130 260"; do
  set -- $pt; ./sc click $1 $2; sleep 0.3; ./sc save >/dev/null
  r=$(python3 -I - "$before" "$1" "$2" <<'PY'
import sys, struct, json; sys.path.insert(0,'.'); import sc2parse as p
before=set(map(int,sys.argv[1].split())); c=p.chunks(p.SAVE); b=c['XBLD']
new=[i for i in range(16384) if 0x1d<=b[i]<=0x2b and i not in before]
if len(new)!=1: sys.exit(1)
x,y=new[0]%128,new[0]//128; a=struct.unpack('>16384H',c['ALTM'])[new[0]]&31
sx,sy=float(sys.argv[2]),float(sys.argv[3])
json.dump({"s":8.0,"ox":sx-8*(y-x),"oy":sy-4*(x+y),"alt":a},open('/tmp/sc/cal.json','w')); print(x,y)
PY
)
  if [ -n "$r" ]; then
    for k in 1 2 3; do ./sc click 22 58; sleep 0.4; ./sc click $1 $2; sleep 0.5; ./sc save >/dev/null
      python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;b=p.chunks(p.SAVE)['XBLD'];x,y=map(int,'$r'.split());sys.exit(0 if not 0x1d<=b[y*128+x]<=0x2b else 1)" && break; done
    echo "view calibrated on tile $r (screen $1,$2)"; exit 0; fi
done
echo "autocal failed"; exit 1
