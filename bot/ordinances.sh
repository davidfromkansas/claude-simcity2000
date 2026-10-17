#!/bin/bash
# ordinances.sh : turn on the four finance ordinances + City Beautification (attempt 19 did this by hand at 10,000).
# Budget window -> City Ordinances book -> tick Sales/Income Tax, Gambling, Parking Fines and City Beautification.
# Runs only when no ordinance is on yet (the boxes toggle); checks the ordinance bits from the save before and after.
cd "$(dirname "$0")"
./sc save >/dev/null; before=$(python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;print(p.parse(p.SAVE)['ordinances'])")
[ "$before" != 0 ] && { echo "ORDINANCES: already on (bits $before) - clicking again would turn them off"; exit 0; }
./sc pause >/dev/null 2>&1
./sc click 47 297; sleep 1.2; ./sc click 437 184; sleep 1.2
for y in 113 130 147 164; do ./sc click 265 $y; sleep 0.3; done
./sc click 459 247; sleep 0.4
./sc snap /tmp/sc/ordinances.png >/dev/null
./sc click 175 390; sleep 0.8; ./sc click 459 123; sleep 0.6; ./sc pause >/dev/null 2>&1
./sc save >/dev/null; after=$(python3 -I -c "import sys;sys.path.insert(0,'.');import sc2parse as p;print(p.parse(p.SAVE)['ordinances'])")
echo "ORDINANCES: bits $before -> $after (screenshot /tmp/sc/ordinances.png); paused: $(./sc paused)"
