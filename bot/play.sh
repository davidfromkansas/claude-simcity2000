#!/bin/bash
# play.sh N [secs] : run up to N check steps (step.sh), but STOP at once when something breaks, so a
# problem is handled within one step instead of after a whole batch (attempt 9 lost 18 months of power
# after a plant burned down mid-batch).
# Stops on: an audit FAIL, buildings without power, new rubble (fire/disaster), the game not paused,
# the city behind its strategy's pace (pace.py, added after attempt 10), or spare water/power under
# 10% (attempt 11 ran 18 months short of water while only a WARN line said so), or a zone type with
# high demand and no empty land (attempt 11 ran out of factory land unnoticed).
cd "$(dirname "$0")"
n=${1:-6}; secs=${2:-1.5}; prev_rubble=""
# refuse to start the clock on a failing city (attempt 12 ran 5 months after a build left a FAIL)
./sc save >/dev/null 2>&1
if python3 -I audit.py | grep -q "^FAIL"; then python3 -I audit.py | grep "^FAIL"; echo "PLAY REFUSED: audit FAIL - fix first"; exit 1; fi
for ((i=1;i<=n;i++)); do
  out=$(bash step.sh "$secs" 2>&1 | grep -v -e xdo -e "Can't open display")
  echo "$out" | grep -v -e "^paused: yes" -e "^AUDIT: passed" -e "stall check: OK"
  rubble=$(echo "$out" | sed -n 's/.*rubble \([0-9]*\).*/\1/p' | head -1)
  reason=""
  echo "$out" | grep -q "^FAIL" && reason="$reason; audit FAIL"
  # Claudeville 4 (2011): after the fire, single regrown buildings in burnt bands sit unpowered until neighbours grow;
  # UNPOWERED_OK=N runs on while at most N buildings are unpowered (spare power is checked separately)
  unp=$(echo "$out" | sed -n 's/^WARN \([0-9]*\) buildings without power.*/\1/p' | head -1)
  [ -n "$unp" ] && [ "$unp" -gt "${UNPOWERED_OK:-0}" ] && reason="$reason; buildings without power ($unp; UNPOWERED_OK=N to allow up to N)"
  echo "$out" | grep -q "^paused: no" && reason="$reason; game was not paused"
  echo "$out" | grep -q "WARN spare \(water\|power\) only [0-9]%" && reason="$reason; spare water or power under 10% (build more; no override: attempt 12 hid a power shortage with one)"
  echo "$out" | grep -q "^LAND short" && [ -z "$LAND_OK" ] && reason="$reason; a zone type with high demand has no empty land (LAND line; LAND_OK=1 to run on)"
  echo "$out" | grep -q "^TRIPS: weak" && [ -z "$TRIPS_OK" ] && reason="$reason; empty zone land where the game's trips fail (TRIPS line: zone it next to homes instead)"
  echo "$out" | grep -q "^REMIND:" && reason="$reason; a planned step is due (REMIND line: do it, then add it to run.json done_reminders)"
  echo "$out" | grep -q "^PACE: behind" && [ -z "$PACE_OK" ] && reason="$reason; behind the strategy pace (act, then PACE_OK=1 to run on)"
  [ -n "$prev_rubble" ] && [ -n "$rubble" ] && [ "$rubble" -gt "$prev_rubble" ] && reason="$reason; new rubble ($prev_rubble -> $rubble): fire or disaster"
  prev_rubble=$rubble
  # jobs first (attempt 19 rule, from attempts 15-18: dense homes outran jobs, demand stayed negative, nothing upgraded)
  unemp=$(echo "$out" | sed -n 's/.*unemp \[\([0-9]*\)\].*/\1/p' | tail -1)
  resd=$(echo "$out" | sed -n "s/.*'res': \(-\?[0-9]*\).*/\1/p" | tail -1)
  [ -n "$unemp" ] && [ -n "$resd" ] && [ "$unemp" -ge 9 ] && [ "$resd" -lt 0 ] && [ -z "$JOBS_OK" ] && reason="$reason; JOBS: unemployment ${unemp}% with home demand $resd - add job land before more homes (JOBS_OK=1 to run on)"
  if [ -n "$reason" ]; then echo "PLAY STOPPED after step $i: $reason"; exit 1; fi
  python3 -I taxctl.py | grep -v "no change"     # rates follow demand when run.json has "taxctl": true
done
echo "PLAY: $n steps, no alarms"
