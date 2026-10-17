"""Build a captioned timelapse of one attempt from its 30-minute screen recordings.

Top bar: game date, population, cash and loans (from the dashboard's metrics.json).
Bottom bar: Claude's moves (from activity.json), shown at the real time they were made.

usage: python3 -I tools/timelapse.py RECDIR DASHBOARD_DIR OUT.mp4 "Title" "subtitle" "outro line 1" ["outro line 2" ...]
  RECDIR holds part-YYYYmmdd-HHMMSS.mp4 clips (UTC start time in the name).
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TMP = "/tmp/sc/timelapse"
W, H = 1280, 960
TARGET = 150          # seconds of output for the gameplay part
MIN_SHOW = 4          # seconds of output a move caption stays up


def ts(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def textfile(name, text):
    p = os.path.join(TMP, name)
    open(p, "w").write(text)
    return p


def card(path, lines, seconds):
    args = ["convert", "-size", f"{W}x{H}", "xc:#14211F", "-gravity", "center"]
    y = -((len(lines) - 1) * 70) // 2
    for text, size, color in lines:
        args += ["-font", BOLD if size >= 48 else FONT, "-pointsize", str(size), "-fill", color, "-annotate", f"+0{y:+d}", text]
        y += 70 if size < 48 else 90
    png = path + ".png"
    subprocess.run(args + [png], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-t", str(seconds),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "20", path], check=True)


def short(text, n=86):
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[:n - 1].rsplit(" ", 1)[0] + "…"


def main(recdir, dash, out, title, subtitle, *outro):
    os.makedirs(TMP, exist_ok=True)
    clips = sorted(f for f in os.listdir(recdir) if re.match(r"part-\d{8}-\d{6}\.mp4$", f))
    # Join the clips into one video; timeline t=0 is the first clip's start.
    start = dt.datetime.strptime(clips[0][5:20], "%Y%m%d-%H%M%S").replace(tzinfo=dt.timezone.utc)
    lst = textfile("clips.txt", "".join(f"file '{os.path.join(recdir, c)}'\n" for c in clips))
    joined = os.path.join(TMP, "joined.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", joined],
                               capture_output=True, text=True).stdout)
    speed = max(1.0, dur / TARGET)
    rows = json.load(open(os.path.join(dash, "data", "metrics.json")))
    acts = json.load(open(os.path.join(dash, "data", "activity.json")))
    f = [f"scale={W}:{H}:flags=neighbor", f"drawbox=x=0:y=0:w={W}:h=56:color=black@0.72:t=fill"]
    pts = [(max(0, (ts(r["t"]) - start).total_seconds()),
            f"{r['date']}   {r['population']:,} people   ${r['money']:,}   loans: {r['bonds']}") for r in rows]
    for i, (t, text) in enumerate(pts):
        end = pts[i + 1][0] if i + 1 < len(pts) else 1e6
        if end > t:
            f.append(f"drawtext=fontfile={BOLD}:textfile={textfile(f'top{i}.txt', text)}:fontsize=30:fontcolor=white:"
                     f"x=24:y=13:expansion=none:enable='between(t,{t:.1f},{end:.1f})'")
    f.append(f"drawbox=x=0:y={H-76}:w={W}:h=76:color=0x14211F@0.88:t=fill")
    moves = [((ts(a["t"]) - start).total_seconds(), short(a["text"])) for a in acts if a.get("type") != "milestone" or True]
    for i, (t, text) in enumerate(moves):
        nxt = moves[i + 1][0] if i + 1 < len(moves) else 1e6
        end = max(nxt, t + MIN_SHOW * speed)
        f.append(f"drawtext=fontfile={FONT}:textfile={textfile(f'dec{i}.txt', text)}:fontsize=24:fontcolor=0xFFB27A:"
                 f"x=24:y={H-50}:expansion=none:enable='between(t,{max(t, 0):.1f},{end:.1f})'")
    f += [f"setpts=PTS/{speed:.3f}", "fps=30", "format=yuv420p"]
    body = os.path.join(TMP, "body.mp4")
    fs = textfile("filter.txt", ",".join(f))   # attempt 19: the filter outgrew the command line
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined, "-filter_script:v", fs, "-an",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "26", body], check=True)
    intro, end_card = os.path.join(TMP, "intro.mp4"), os.path.join(TMP, "outro.mp4")
    card(intro, [(title, 72, "#FFB27A"), (subtitle, 32, "white"),
                 ("Goal: 100,000 people within 50 years", 30, "#C9D4D0"),
                 ("Medium difficulty, disasters on, loans allowed", 30, "#C9D4D0")], 4)
    card(end_card, [(outro[0], 64, "#FFB27A")] + [(l, 30, "white") for l in outro[1:]], 6)
    lst = textfile("list.txt", "".join(f"file '{p}'\n" for p in (intro, body, end_card)))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", "-movflags", "+faststart", out], check=True)
    print(out, round(dur), "s of play at", round(speed, 1), "x")


if __name__ == "__main__":
    main(*sys.argv[1:])
