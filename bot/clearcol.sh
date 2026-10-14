#!/bin/bash
# clearcol.sh X Y0 Y1 : bulldoze every non-road tile in column X from Y0 to Y1, then lay road over it.
cd "$(dirname "$0")"; X=$1; Y0=$2; Y1=$3
for ((a=Y0; a<=Y1; a+=12)); do b=$((a+11)); [ $b -gt $Y1 ] && b=$Y1
  ./vis.sh $X $a $X $b >/dev/null || continue
  ./sc tool 22 58 60 65; sleep 0.4
  for y in $(python3 -I -c "
import sys;sys.path.insert(0,'.');import sc2parse as p;bl=p.chunks(p.SAVE)['XBLD']
print(' '.join(str(y) for y in range($a,$b+1) if not 0x1d<=bl[y*128+$X]<=0x2b and bl[y*128+$X] not in (0,)))"); do
    ./sc click $(python3 -I tile.py $X $y); sleep 0.25; done
  ./sc tool 22 105 55 113; sleep 0.4; ./sc drag $(python3 -I tile.py $X $a) $(python3 -I tile.py $X $b); sleep 0.4; ./sc nodlg 2>/dev/null
  ./sc save >/dev/null
done
