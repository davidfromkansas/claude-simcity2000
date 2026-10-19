#!/bin/bash
# run the city to its end: step.sh until Jan 2050, new rubble (fire: stop and act), or the date stops moving (game over)
cd /home/user/claude-simcity2000/bot
prev=""; same=0
for i in $(seq 1 120); do
  out=$(bash step.sh 2>&1 | grep -v -e xdo -e "Can't open display")
  line=$(echo "$out" | grep -m1 " pop ")
  echo "$line" | cut -c1-90
  if [ -z "$RUBBLE_OK" ] && echo "$out" | grep -q "new rubble"; then
    echo "$out" | grep "rubble" | head -2; echo "RUBBLE STOP: find the fire and clear a firebreak"; break
  fi
  d=$(echo "$line" | cut -c1-8)
  if [ -n "$d" ] && [ "$d" = "$prev" ]; then same=$((same+1)); else same=0; fi
  prev=$d
  if [ $same -ge 3 ]; then
    ./sc snap >/dev/null 2>&1
    if [ "$(convert /tmp/sc/now.png -format "%[pixel:p{238,52}]" info:)" = "srgb(255,0,0)" ]; then
      echo "DISASTER at $d: the calendar is frozen (red arrow at 241,52 jumps to it)"; break; fi
    echo "DATE STUCK at $d: game over or a dialog"; break
  fi
  echo "$line" | grep -qE "^[A-Z][a-z]{2} 20[5-9][0-9] " && { echo "DEADLINE"; break; }
done
echo DONE
