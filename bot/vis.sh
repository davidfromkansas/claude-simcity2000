#!/bin/bash
# vis.sh X1 Y1 [X2 Y2 ...] : make sure all these tiles are inside the safe screen area (recenter + autocal if not).
cd "$(dirname "$0")"
ok() { for ((i=1;i<=$#;i+=2)); do j=$((i+1)); read sx sy < <(python3 -I tile.py ${!i} ${!j});
  [ "$sx" -ge 100 ] && [ "$sx" -le 600 ] && [ "$sy" -ge 64 ] && [ "$sy" -le 440 ] || return 1; done; }
ok "$@" && exit 0
# centre on the midpoint
read cx cy < <(python3 -I -c "import sys;a=list(map(int,sys.argv[1:]));print(round(sum(a[0::2])/len(a[0::2])),round(sum(a[1::2])/len(a[1::2])))" "$@")
./center.sh $cx $cy >/dev/null; ./autocal.sh >/dev/null
ok "$@" || { echo "not all visible"; exit 1; }
