#!/bin/bash
# play.sh N [secs] : run up to N check steps (step.sh), but STOP at once when something breaks, so a
# problem is handled within one step instead of after a whole batch (attempt 9 lost 18 months of power
# after a plant burned down mid-batch).
# Stops on: an audit FAIL, buildings without power, new rubble (fire/disaster), the game not paused,
# or the city behind its strategy's pace (pace.py, added after attempt 10).
cd "$(dirname "$0")"
n=${1:-6}; secs=${2:-1.5}; prev_rubble=""
for ((i=1;i<=n;i++)); do
  out=$(bash step.sh "$secs" 2>&1 | grep -v -e xdo -e "Can't open display")
  echo "$out" | grep -v -e "^paused: yes" -e "^AUDIT: passed" -e "stall check: OK"
  rubble=$(echo "$out" | sed -n 's/.*rubble \([0-9]*\).*/\1/p' | head -1)
  reason=""
  echo "$out" | grep -q "^FAIL" && reason="audit FAIL"
  echo "$out" | grep -q "buildings without power" && reason="buildings without power"
  echo "$out" | grep -q "^paused: no" && reason="game was not paused"
  echo "$out" | grep -q "^PACE: behind" && [ -z "$PACE_OK" ] && reason="behind the strategy pace (act, then PACE_OK=1 to run on)"
  [ -n "$prev_rubble" ] && [ -n "$rubble" ] && [ "$rubble" -gt "$prev_rubble" ] && reason="new rubble ($prev_rubble -> $rubble): fire or disaster"
  prev_rubble=$rubble
  if [ -n "$reason" ]; then echo "PLAY STOPPED after step $i: $reason"; exit 1; fi
done
echo "PLAY: $n steps, no alarms"
