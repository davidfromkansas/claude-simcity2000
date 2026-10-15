#!/bin/bash
# Record the game screen in 30-minute MP4 pieces.
# Each piece is a fragmented MP4 with a keyframe every 5 s, so if the container stops mid-recording
# the piece still plays (attempt 7 lost its index that way; the segment muxer buffered too much).
# Stop with: touch /tmp/sc/rec.stop; pkill -INT -f "x11grab"
REC=$(python3 -c "import json;print(json.load(open('$(dirname "$0")/run.json')).get('rec','/opt/sc2k/rec'))")
mkdir -p "$REC" /tmp/sc
rm -f /tmp/sc/rec.stop
while [ ! -e /tmp/sc/rec.stop ]; do
  ffmpeg -nostdin -loglevel error -f x11grab -framerate 10 -video_size 640x480 -i :99 -t 1800 \
    -c:v libx264 -preset veryfast -crf 28 -pix_fmt yuv420p -g 50 \
    -movflags frag_keyframe+empty_moov -flush_packets 1 \
    "$REC/part-$(date -u +%Y%m%d-%H%M%S).mp4"
done
