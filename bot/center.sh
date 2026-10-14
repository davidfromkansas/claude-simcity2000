#!/bin/bash
# center.sh X Y : scroll the view (any distance) until tile X,Y is at the screen centre. Needs a valid calibration.
cd "$(dirname "$0")"
for i in 1 2 3 4 5 6; do
  read sx sy < <(python3 -I tile.py "$1" "$2")
  if [ "$sx" -ge 100 ] && [ "$sx" -le 600 ] && [ "$sy" -ge 40 ] && [ "$sy" -le 440 ]; then ./sc goto "$1" "$2"; exit 0; fi
  # step toward the target: clamp into the safe area
  px=$(( sx < 100 ? 100 : (sx > 600 ? 600 : sx) )); py=$(( sy < 40 ? 40 : (sy > 440 ? 440 : sy) ))
  read tx ty < <(python3 -I tile.py inv $px $py)
  ./sc click 68 230; sleep 0.2; ./sc click $px $py; sleep 0.6
  s=$(python3 -I -c "import json;print(json.load(open('/tmp/sc/cal.json'))['s'])")
  python3 -I tile.py cal $tx $ty 324 240 $s >/dev/null
done
echo "could not reach $1 $2"; exit 1
