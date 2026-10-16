#!/bin/bash
# autocal.sh : find where the view is. Places one road tile at a few screen spots until one lands,
# reads its tile from the save, calibrates tile.py (zoom 3), then bulldozes it.
cd "$(dirname "$0")"
roads() { python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;c=p.chunks(p.SAVE);b=c['XBLD'];print(' '.join(str(i) for i in range(16384) if 0x1d<=b[i]<=0x2b))"; }
./sc key Escape; ./sc save >/dev/null; before=$(roads)
./sc tool 22 105 55 113; sleep 0.3
./sc snap /tmp/sc/calview.png >/dev/null
# skip spots that show water: a test road there would build a bridge (attempt 9 left one on the lake)
wet() { convert /tmp/sc/calview.png -format "%[fx:(p{$1,$2}.b-p{$1,$2}.r>0.25 && p{$1,$2}.b-p{$1,$2}.g>0.15)?1:0]" info:; }
for pt in "330 250" "450 360" "200 360" "470 150" "200 160" "560 260" "130 260" "400 300" "260 300" "400 200" "260 200" "520 400" "150 400" "520 100" "150 100" "330 400" "330 110" "580 350" "580 150"; do
  set -- $pt; [ "$(wet $1 $2)" = 1 ] && continue
  ./sc click $1 $2; sleep 0.4; ./sc nodlg 2>/dev/null; ./sc save >/dev/null
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
    for k in 1 2 3; do ./sc tool 22 58 60 65; sleep 0.4; ./sc click $1 $2; sleep 0.3; ./sc click $1 $2; sleep 0.5; ./sc save >/dev/null
      python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;b=p.chunks(p.SAVE)['XBLD'];x,y=map(int,'$r'.split());sys.exit(0 if b[y*128+x]==0 else 1)" && break; done
    echo "view calibrated on tile $r (screen $1,$2)"; exit 0; fi
done
echo "autocal failed"; exit 1
