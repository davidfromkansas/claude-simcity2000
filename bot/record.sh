#!/bin/bash
# Record the game screen in 30-minute MP4 pieces.
REC=$(python3 -c "import json;print(json.load(open('$(dirname "$0")/run.json')).get('rec','/opt/sc2k/rec'))")
mkdir -p "$REC"
exec ffmpeg -nostdin -loglevel error -f x11grab -framerate 10 -video_size 640x480 -i :99 \
  -c:v libx264 -preset veryfast -crf 28 -pix_fmt yuv420p \
  -f segment -segment_time 1800 -reset_timestamps 1 -strftime 1 \
  "$REC"/part-%Y%m%d-%H%M%S.mp4
