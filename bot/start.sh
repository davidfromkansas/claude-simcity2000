#!/bin/bash
# Start a virtual screen and SimCity 2000 inside DOSBox.
export DISPLAY=:99
pgrep -x Xvfb >/dev/null || (Xvfb :99 -screen 0 640x480x24 -nolisten tcp >/tmp/xvfb.log 2>&1 &)
sleep 1
pgrep -x dosbox >/dev/null || (SDL_AUDIODRIVER=dummy dosbox -conf "$(dirname "$0")/dosbox.conf" >/tmp/dosbox.log 2>&1 &)
sleep 3
xdotool search --name DOSBox | head -1 | xargs -I{} xdotool windowmove {} 0 0
