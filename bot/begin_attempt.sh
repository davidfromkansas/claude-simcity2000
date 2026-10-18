#!/bin/bash
# begin_attempt.sh N [claudeville-3|claudeville-4] : start attempt N of a challenge from the base map, the same way
# every time. Starts the game if needed, loads C3BASE.SC2 (the flat map both challenges use), saves it as
# <prefix><N>.SC2 (C3A<N> / C4A<N>), maximizes the city window,
# turns Auto-Goto off, zooms in, resets calibration, takes loan #1, starts recorder + publisher.
set -e
cd "$(dirname "$0")"
n=$1; [ -n "$n" ] || { echo "usage: begin_attempt.sh N [challenge]"; exit 1; }
python3 -I new_attempt.py "$n" "${2:-claudeville-3}"
pre=$(python3 -I -c "import json;print(json.load(open('run.json'))['prefix'])")
rm -f "/opt/sc2k/game/$pre$n.SC2"   # attempt 19 restart: an "Overwrite?" prompt threw every later click off
if ! pgrep -x dosbox >/dev/null; then
  bash start.sh; sleep 6
  sleep 25                                   # splash screen, then the title menu
  ./sc click 317 175; sleep 2                 # Load Saved City
else
  ./sc pause; ./sc menu 25 7 45 23; sleep 1.5  # File > Load City
  ./sc click 317 261; sleep 2                 # "save your city?" -> No
fi
./sc click 400 138; for i in $(seq 12); do ./sc key End BackSpace >/dev/null; done
./sc type 'C3BASE.SC2'; ./sc click 239 376; sleep 4
./sc click 559 119; sleep 1                   # maximize the city window (no-op if already full)
./sc menu 25 7 60 119; sleep 1.5              # File > Save City As
./sc click 400 138; for i in $(seq 12); do ./sc key End BackSpace >/dev/null; done
./sc type "$pre$n.SC2"; ./sc click 239 376; sleep 2; ./sc click 320 245; sleep 0.5
./sc peek 120 7 >/dev/null 2>&1; ./sc key Escape
# Auto-Goto is stored ON in the base map: toggle it off
./sc menu 120 7 135 39; sleep 0.3
./sc click 45 230; sleep 0.8; rm -f /tmp/sc/cal.json   # zoom in, recalibrate on next build
./sc click 47 297; sleep 1.2; ./sc click 437 203; sleep 1.2; ./sc click 290 307; sleep 1.2
./sc click 267 260; sleep 1; ./sc click 430 307; sleep 0.8; ./sc click 459 123; sleep 0.5; ./sc pause
python3 -c "import json;r=json.load(open('run.json'));r['bonds']=1;json.dump(r,open('run.json','w'))"
./sc save | cut -c1-80
rm -f /tmp/sc/rec.stop
(DISPLAY=:99 nohup bash record.sh >/dev/null 2>&1 &)
(nohup python3 -I publish.py loop >/tmp/sc/pub.log 2>&1 &)
./sc peek 120 7 >/dev/null 2>&1; cp /tmp/sc/now.png /tmp/sc/options.png; ./sc key Escape
echo "attempt $n started; check /tmp/sc/options.png shows Auto-Goto unchecked"
