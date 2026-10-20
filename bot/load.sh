#!/bin/bash
# load.sh : load the attempt's save (run.json "save") into the running game and check it really is the city.
# Attempt 8 (Oct 2026): after a container restart a hand-typed load landed on a NEW blank map and a build saved over
# the attempt's save. This loads, saves, and refuses to go on unless the save holds "Claudeville 3" with people in it.
cd "$(dirname "$0")"
name=$(python3 -I -c "import json,os;print(os.path.basename(json.load(open('run.json'))['save']))")
if ! pgrep -x dosbox >/dev/null; then
  bash start.sh; sleep 32
  ./sc click 317 175; sleep 2                 # title menu: Load Saved City
else
  ./sc pause; ./sc menu 25 7 45 23; sleep 1.5  # File > Load City
  ./sc click 317 261; sleep 2                 # "save your city?" -> No
fi
./sc click 400 138; for i in $(seq 12); do ./sc key End BackSpace >/dev/null; done
./sc type "$name"; ./sc click 239 376; sleep 4
./sc click 559 119; sleep 1
./sc snap >/dev/null
# read the city from the game WITHOUT overwriting the attempt's save: Save City As a scratch name first
# (remove any old scratch file: its "Overwrite?" prompt stopped the save and the check read a stale copy - Oct 2026)
rm -f /opt/sc2k/game/LOADCHK.SC2
./sc menu 25 7 60 119; sleep 1.5
./sc click 400 138; for i in $(seq 12); do ./sc key End BackSpace >/dev/null; done
./sc type "LOADCHK.SC2"; ./sc click 239 376; sleep 2; ./sc click 320 245; sleep 0.5
python3 -I - <<'PY' || { echo "LOAD FAILED: the game does not hold the attempt's city - do NOT save or build"; exit 1; }
import sys; sys.path.insert(0, '.'); import sc2parse as p
d = p.parse('/opt/sc2k/game/LOADCHK.SC2')
print("LOADCHK:", d.get('city'), d.get('date'), d.get('population'))
sys.exit(0 if d.get('city') == 'Claudeville 3' and d.get('population', 0) > 0 else 1)
PY
# back to the attempt's own file name for later saves (remove it first: an "Overwrite?" prompt throws clicks off;
# LOADCHK.SC2 holds the same city meanwhile)
rm -f "/opt/sc2k/game/$name"
./sc menu 25 7 60 119; sleep 1.5
./sc click 400 138; for i in $(seq 12); do ./sc key End BackSpace >/dev/null; done
./sc type "$name"; ./sc click 239 376; sleep 2; ./sc click 320 245; sleep 0.5; ./sc click 320 228; sleep 0.5
[ -f "/opt/sc2k/game/$name" ] || { echo "LOAD FAILED: $name was not written back - save it by hand (Save City As) before anything else"; exit 1; }
./sc click 45 230; sleep 0.8; rm -f /tmp/sc/cal.json /tmp/sc/center.json      # zoom in, recalibrate on next build
./sc save | tail -1 | cut -c1-80
echo "LOAD OK"
