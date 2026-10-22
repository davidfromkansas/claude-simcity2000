#!/bin/bash
# disaster.sh [bursts] : run the game through an active disaster (calendar frozen) safely.
# Attempt 8 (Nov 2038): I let the game run at Cheetah for ~10 minutes during an alien-ship disaster and a ~24-tile
# fire became a great fire (~4,800 rubble tiles). This runs 10-second bursts at Llama, re-centres on the disaster
# after each (red arrow at 241,52), counts flame-coloured pixels, and stops as soon as the fire grows by a third, or
# when the calendar moves (disaster over). Exit 0 = over, 2 = FIRE GROWING (act now: firebreak), 1 = still running.
cd "$(dirname "$0")"
n=${1:-30}
flames() { convert /tmp/sc/now.png -crop 540x380+90+60 -fx '(r>0.85 && g>0.25 && g<0.75 && b<0.25)?1:0' -format '%[fx:mean*w*h]' info: | cut -d. -f1; }
rubble() { ./sc save >/dev/null 2>&1; python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;print(sum(1 for t in p.chunks(p.SAVE)['XBLD'] if 1<=t<=4))"; }
date_sig() { convert /tmp/sc/now.png -crop 120x12+215+14 -format '%#' info:; }
./sc pause >/dev/null 2>&1; ./sc click 241 52 >/dev/null 2>&1; sleep 1; ./sc snap >/dev/null 2>&1
d0=$(date_sig); f0=$(flames); best=$f0; r0=$(rubble)
echo "DISASTER: start, flame pixels $f0"
for i in $(seq 1 "$n"); do
  ./sc menu 67 7 75 55 >/dev/null 2>&1; ./sc key Escape >/dev/null 2>&1      # Llama
  sleep 10
  ./sc menu 67 7 75 23 >/dev/null 2>&1; ./sc key Escape >/dev/null 2>&1      # Pause
  ./sc snap >/dev/null 2>&1
  if [ "$(date_sig)" != "$d0" ]; then echo "DISASTER: over after $i bursts (calendar moved)"; exit 0; fi
  ./sc click 241 52 >/dev/null 2>&1; sleep 1; ./sc snap >/dev/null 2>&1
  f=$(flames); cp /tmp/sc/now.png /tmp/sc/disaster-last.png
  r=$(rubble); echo "DISASTER: burst $i flame pixels $f, rubble $r (start $r0)"
  # C4 attempt 9 (Sep 2028): the flame count only sees the view around the disaster; a fire elsewhere grew into a great
  # fire over 17 bursts. Rubble from the save covers the whole map.
  if [ "$r" -gt $((r0 + 25)) ]; then echo "FIRE SPREADING: rubble $r0 -> $r on the map (paused)"; exit 2; fi
  if [ "$f" -gt $((best + best / 3 + 200)) ]; then echo "FIRE GROWING: $best -> $f pixels (paused; see /tmp/sc/disaster-last.png)"; exit 2; fi
  [ "$f" -lt "$best" ] && best=$f
done
echo "DISASTER: still running after $n bursts (paused)"; exit 1
