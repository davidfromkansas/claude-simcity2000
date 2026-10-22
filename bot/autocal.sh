#!/bin/bash
# autocal.sh : find where the view is. Places one road tile at a few screen spots until one lands,
# reads its tile from the save, calibrates tile.py (zoom 3), then bulldozes it.
cd "$(dirname "$0")"
roads() { python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;c=p.chunks(p.SAVE);b=c['XBLD'];print(' '.join(str(i) for i in range(16384) if 0x1d<=b[i]<=0x2b))"; }
./sc key Escape; ./sc save >/dev/null; before=$(roads); bridges=$(python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;b=p.chunks(p.SAVE)['XBLD'];print(' '.join(str(i) for i in range(16384) if 0x51<=b[i]<=0x57) or '-1')"); rm -f /tmp/sc/cal_bridge
# C4 attempt 9 (Oct 2028): sweep() is NOT called on the zoom-fail exits any more - there the calibration is wrong, and
# its bulldozer clicks destroyed two fire stations. Strays are left for build.py's final sweep (verified calibration).
sweep() { for k in 1 2 3; do
  left=$(python3 -I - "$before" <<'PY'
import sys; sys.path.insert(0,'.'); import sc2parse as p
before=set(map(int,sys.argv[1].split())); b=p.chunks(p.SAVE)['XBLD']
print(' '.join('%d,%d' % (i%128,i//128) for i in range(16384) if 0x1d<=b[i]<=0x2b and i not in before))
PY
)
  [ -z "$left" ] && return
  for t in $left; do read sx sy < <(python3 -I tile.py ${t%,*} ${t#*,}); ./sc tool 22 58 60 65; sleep 0.3; ./sc click $sx $sy; sleep 0.3; ./sc click $sx $sy; sleep 0.4; done
  ./sc save >/dev/null; done; }
./sc tool 22 105 55 113; sleep 0.3
./sc snap /tmp/sc/calview.png >/dev/null
# skip spots that show water: a test road there would build a bridge (attempt 9 left one on the lake)
# (attempt 11: a click on a shore tile built a bridge, so look 24 px around the spot too)
wet1() { convert /tmp/sc/calview.png -format "%[fx:(p{$1,$2}.b-p{$1,$2}.r>0.25 && p{$1,$2}.b-p{$1,$2}.g>0.15)?1:0]" info:; }
wet() { for d in "0 0" "24 0" "-24 0" "0 12" "0 -12" "16 8" "-16 -8" "16 -8" "-16 8" "48 0" "-48 0" "0 24" "0 -24" "32 16" "-32 -16" "32 -16" "-32 16"; do set -- $1 $2 $d
  [ "$(wet1 $(($1+$3)) $(($2+$4)))" = 1 ] && { echo 1; return; }; done; echo 0; }
# C4 attempt 12 (Jun 2017): with the view centred over the river every "dry" spot was a shore tile; test roads built a
# $975 suspension bridge and opened the bridge dialog, which swallowed later clicks. Refuse a view that is mostly water.
wetshare=$(convert /tmp/sc/calview.png -crop 400x260+120+110 -fx "(b-r>0.25 && b-g>0.15)?1:0" -format "%[fx:mean]" info:)
if python3 -I -c "import sys; sys.exit(0 if float('$wetshare')>0.40 else 1)"; then
  echo "AUTOCAL VIEW OVER WATER (${wetshare} of the centre is water) - centre the view on built land first"; rm -f /tmp/sc/cal.json; exit 3; fi
for pt in "330 250" "450 360" "200 360" "470 150" "200 160" "560 260" "130 260" "400 300" "260 300" "400 200" "260 200" "520 400" "150 400" "520 100" "150 100" "330 400" "330 110" "580 350" "580 150"; do
  set -- $pt; [ "$(wet $1 $2)" = 1 ] && continue
  # attempt 19: test roads on the map edge started $1,000 neighbour deals (twice: the zoom check adds 4 tiles south) - keep 2+ tiles in (C4-1: a 6-tile margin made calibration fail near the east edge and misplaced roads)
  if [ -f /tmp/sc/center.json ]; then python3 -I -c "
import json,sys; c=json.load(open('/tmp/sc/center.json')); dx=($1-324)/8.0; dy=($2-240)/4.0
x=c['x']+(dy-dx)/2; y=c['y']+(dx+dy)/2; sys.exit(0 if 2<=x<=125 and 2<=y<=121 else 1)" || continue; fi
  ./sc click $1 $2; sleep 0.4; ./sc nodlg 2>/dev/null; ./sc save >/dev/null
  r=$(python3 -I - "$before" "$1" "$2" "$bridges" <<'PY'
import sys, struct, json; sys.path.insert(0,'.'); import sc2parse as p
before=set(map(int,sys.argv[1].split())); c=p.chunks(p.SAVE); b=c['XBLD']
new=[i for i in range(16384) if 0x1d<=b[i]<=0x2b and i not in before]
bridge=[i for i in range(16384) if 0x51<=b[i]<=0x57 and i not in set(map(int,sys.argv[4].split()))]   # C4-12: a suspension bridge (0x51-0x56) was missed
if bridge: open('/tmp/sc/cal_bridge','w').write(' '.join('%d %d' % (i%128,i//128) for i in bridge)); sys.exit(1)
if len(new)!=1: sys.exit(1)
x,y=new[0]%128,new[0]//128; a=struct.unpack('>16384H',c['ALTM'])[new[0]]&31
sx,sy=float(sys.argv[2]),float(sys.argv[3])
json.dump({"s":8.0,"ox":sx-8*(y-x),"oy":sy-4*(x+y),"alt":a},open('/tmp/sc/cal.json','w')); print(x,y)
PY
)
  if [ -f /tmp/sc/cal_bridge ]; then echo "AUTOCAL BRIDGE built at $(cat /tmp/sc/cal_bridge) - remove it (bulldoze plan)"; exit 2; fi
  if [ -n "$r" ]; then
    # attempt 19: the zoom-in did not take and every tile landed at half scale. Check the scale with a
    # second road 32 px right / 16 px down (zoom 3 = same x, y+4) and recalibrate with the measured step.
    # (Jul 2026: at the east map edge the spot 32 px right/down was off the map - also try 32 px left/up)
    for d in 1 -1; do
    b2=$(roads); ./sc tool 22 105 55 113; sleep 0.3; ./sc click $(($1+32*d)) $(($2+16*d)); sleep 0.4; ./sc save >/dev/null
    r2=$(python3 -I - "$b2" "$r" "$1" "$2" "$d" <<'PY'
import sys, json; sys.path.insert(0,'.'); import sc2parse as p
before=set(map(int,sys.argv[1].split())); b=p.chunks(p.SAVE)['XBLD']
new=[i for i in range(16384) if 0x1d<=b[i]<=0x2b and i not in before]
if len(new)!=1: print("none"); sys.exit()
x,y=map(int,sys.argv[2].split()); x2,y2=new[0]%128,new[0]//128; k=((y2-y)-(x2-x))*int(sys.argv[5])
if k<=0: print("%d %d bad" % (x2,y2)); sys.exit()
s=32.0/k; sx,sy=float(sys.argv[3]),float(sys.argv[4]); c=json.load(open('/tmp/sc/cal.json'))
c.update({"s":s,"ox":sx-s*(y-x),"oy":sy-s/2*(x+y)}); json.dump(c,open('/tmp/sc/cal.json','w')); print(x2,y2,s)
PY
)
    case $r2 in none) ;; *) break ;; esac
    done
    set -- $1 $2 $r2
    # C4 attempt 9 (Sep 2020): the second test road did not land ('none'), the zoom went unchecked, and a whole district
    # was rebuilt at half scale 14 tiles off - an unverified zoom is a failure, not a pass
    if [ "$3" = none ]; then
      for k in 1 2 3; do ./sc tool 22 58 60 65; sleep 0.4; ./sc click $1 $2; sleep 0.3; ./sc click $1 $2; sleep 0.5; ./sc save >/dev/null; done
      # (Feb 2026: stopping here gave false alarms where the second spot was built up - try the next spot instead)
      # (Sep 2028: in burned/built views no second spot ever landed - accept the zoom when the first road sits where
      # step 8 predicts from the view centre and the spot is far enough from the centre for a wrong zoom to show)
      if [ -f /tmp/sc/center.json ] && python3 -I -c "
import json,sys; c=json.load(open('/tmp/sc/center.json')); x,y=map(int,'$r'.split()); dx=($1-324)/8.0; dy=($2-240)/4.0
px=c['x']+(dy-dx)/2; py=c['y']+(dx+dy)/2; far=abs($1-324)+abs($2-240)
sys.exit(0 if far>=80 and abs(px-x)+abs(py-y)<=2 else 1)"; then
        python3 -I -c "import json;c=json.load(open('/tmp/sc/cal.json'));c['method']='centre';json.dump(c,open('/tmp/sc/cal.json','w'))"
        echo "view calibrated on tile $r (screen $1,$2); zoom checked against the view centre"; exit 0; fi
      zoomskip=1; continue; fi
    if [ "$3" != none ]; then
      for k in 1 2 3; do ./sc tool 22 58 60 65; sleep 0.4; ./sc click $(($1+32*d)) $(($2+16*d)); sleep 0.3; ./sc click $(($1+32*d)) $(($2+16*d)); sleep 0.5; ./sc save >/dev/null
        python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;b=p.chunks(p.SAVE)['XBLD'];x,y=$3,$4;sys.exit(0 if b[y*128+x]==0 else 1)" && break; done
      if [ "$5" != "8.0" ]; then echo "AUTOCAL ZOOM: step $5 px, not 8 - zoom is wrong; fix the zoom before building"; rm -f /tmp/sc/cal.json; exit 3; fi
    fi
    for k in 1 2 3; do ./sc tool 22 58 60 65; sleep 0.4; ./sc click $1 $2; sleep 0.3; ./sc click $1 $2; sleep 0.5; ./sc save >/dev/null
      python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;b=p.chunks(p.SAVE)['XBLD'];x,y=map(int,'$r'.split());sys.exit(0 if b[y*128+x]==0 else 1)" && break; done
    # attempt C4-1: a test road was left behind at (112,59) and blocked a zoo - every road tile that was not
    # there before must be gone again (retry with the bulldozer, then report)
    for k in 1 2 3 4; do
      left=$(python3 -I - "$before" <<'PY'
import sys; sys.path.insert(0,'.'); import sc2parse as p
before=set(map(int,sys.argv[1].split())); b=p.chunks(p.SAVE)['XBLD']
print(' '.join('%d,%d' % (i%128,i//128) for i in range(16384) if 0x1d<=b[i]<=0x2b and i not in before))
PY
)
      [ -z "$left" ] && break
      for t in $left; do read sx sy < <(python3 -I tile.py ${t%,*} ${t#*,}); ./sc tool 22 58 60 65; sleep 0.3; ./sc click $sx $sy; sleep 0.3; ./sc click $sx $sy; sleep 0.4; done
      ./sc save >/dev/null
    done
    [ -n "$left" ] && echo "AUTOCAL STRAY ROAD left at $left"
    echo "view calibrated on tile $r (screen $1,$2)"
    # attempt 3: near the west-bank map edge the view could not centre, autocal calibrated 20+ tiles away and
    # build clicks then landed 2-4 rows off - warn so build.py's vis() reports it
    python3 -I -c "
import json,sys
c=json.load(open('/tmp/sc/center.json')); x,y=map(int,'$r'.split())
d=abs(x-c['x'])+abs(y-c['y'])
if d>16: print('AUTOCAL STRAY calibration tile %d,%d is %d tiles from the requested centre %d,%d - clicks may land off' % (x,y,d,c['x'],c['y']))
" 2>/dev/null
    exit 0; fi
done
# C4 attempt 9 (Sep 2028 fire): in a fully built view no test road can land - drop power lines on road tiles instead
# (a line on a straight road just makes a harmless crossing) and calibrate from the changed tile; check the zoom with a
# second line 32 px away
xb() { python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;open('$1','wb').write(bytes(p.chunks(p.SAVE)['XBLD']))"; }
lineat() { ./sc save >/dev/null; xb /tmp/sc/lc_b; ./sc tool 22 82 55 90; sleep 0.4; ./sc click $1 $2; sleep 0.5; ./sc nodlg 2>/dev/null; ./sc save >/dev/null; xb /tmp/sc/lc_a
  python3 -I -c "
b=open('/tmp/sc/lc_b','rb').read(); a=open('/tmp/sc/lc_a','rb').read(); L=lambda t: 0x0e<=t<=0x1c or 0x43<=t<=0x46
d=[i for i in range(16384) if L(a[i]) and not L(b[i])]
print('%d %d' % (d[0]%128, d[0]//128) if len(d)==1 else 'none')"; }
n=0; for pt in $(for yy in 236 300 172 364 140 396 268 204 332; do for xx in 316 252 380 188 444 508 156 556; do echo "$xx,$yy"; done; done); do
  n=$((n+1)); [ $n -gt 45 ] && break
  set -- ${pt/,/ }; t1=$(lineat $1 $2); [ "$t1" = none ] && continue
  for d in 1 -1; do t2=$(lineat $(($1+32*d)) $(($2+16*d))); [ "$t2" != none ] && break; done
  [ "$t2" = none ] && continue
  read x1 y1 <<< "$t1"; read x2 y2 <<< "$t2"; k=$(( ((y2-y1)-(x2-x1))*d ))
  # (Dec 2019: a line can snap one tile toward a neighbour, so 3-5 tiles is fine; a wrong zoom gives 2 or 8)
  if [ "$k" -lt 3 ] || [ "$k" -gt 5 ]; then echo "AUTOCAL ZOOM: line check moved $k tiles for 32 px, not 4 - zoom is wrong"; rm -f /tmp/sc/cal.json; exit 3; fi
  python3 -I -c "import json;json.dump({'s':8.0,'ox':$1-8*($y1-$x1),'oy':$2-4*($x1+$y1),'alt':4,'method':'line'},open('/tmp/sc/cal.json','w'))"
  echo "view calibrated on tile $x1 $y1 (screen $1,$2) by power line (crossings left at $t1 and $t2)"; exit 0
done
[ -n "$zoomskip" ] && { echo "AUTOCAL ZOOM: not verified at any spot (second test road never landed) - check the zoom before building"; rm -f /tmp/sc/cal.json; exit 3; }
echo "autocal failed"; exit 1
