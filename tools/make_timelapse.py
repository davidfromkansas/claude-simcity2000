"""Build a captioned timelapse MP4 of attempt 2 from the screen recording.

Captions come from the dashboard data: the game date/population (top bar) and
each decision Claude made (bottom bar), placed at the real time they happened.
usage: python3 tools/make_timelapse.py OUT.mp4
"""
import datetime as dt
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(ROOT, "docs", "run2")
SRC = os.path.join(RUN, "recordings", "part-20261014-003057.mp4")
START = dt.datetime(2026, 10, 14, 0, 30, 57, tzinfo=dt.timezone.utc)
SPEED = 12          # 22 minutes of play -> about 2 minutes
MIN_SHOW = 48       # seconds of original footage a decision caption stays up (4 s of output)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TMP = "/tmp/sc/timelapse"
W, H = 1280, 960

# Short versions of the activity feed, keyed by the feed's timestamps.
DECISIONS = [
    ("00:30:59", "Day one: coal plant, road grid, 10 water pumps, trade link, 5% tax"),
    ("00:33:55", "Year 1 check: only 30% of buildings had water. Fixed the pipe gaps"),
    ("00:34:42", "Shop demand rose, so zoned a small shop block"),
    ("00:39:42", "Too many factories, homes in demand: built the north district"),
    ("00:41:42", "17% unemployed: new factory strip east of the lake"),
    ("00:44:19", "More dense housing north of the lake"),
    ("00:45:34", "Factory strip had no power across the road: added crossings"),
    ("00:47:08", "Long commutes: direct road on the east side of the lake"),
    ("00:48:39", "Shops and factories in demand: shop district by the north homes"),
    ("00:50:06", "Jobs short again: rezoned abandoned homes as factories"),
    ("00:51:13", "GOAL 1 REACHED: 5,970 people in Jan 2015"),
    ("00:51:29", "Goal 2: building frozen, keep every year profitable"),
]


def secs(hms):
    h, m, s = map(int, hms.split(":"))
    return (dt.datetime(2026, 10, 14, h, m, s, tzinfo=dt.timezone.utc) - START).total_seconds()


def textfile(name, text):
    p = os.path.join(TMP, name)
    open(p, "w").write(text)
    return p


def card(path, lines, seconds):
    """Title card: lines of (text, size, color)."""
    args = ["convert", "-size", f"{W}x{H}", "xc:#14211c", "-gravity", "center"]
    y = -((len(lines) - 1) * 70) // 2
    for text, size, color in lines:
        args += ["-font", BOLD if size >= 48 else FONT, "-pointsize", str(size), "-fill", color,
                 "-annotate", f"+0{y:+d}", text]
        y += 70 if size < 48 else 90
    png = path + ".png"
    subprocess.run(args + [png], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-t", str(seconds),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "20", path], check=True)


def main(out):
    os.makedirs(TMP, exist_ok=True)
    rows = json.load(open(os.path.join(RUN, "data", "metrics.json")))
    filters = [f"scale={W}:{H}:flags=neighbor"]
    # Top bar: game date and population, from each dashboard reading.
    pts = []
    for r in rows:
        t = (dt.datetime.fromisoformat(r["t"].replace("Z", "+00:00")) - START).total_seconds()
        pts.append((max(t, 0), f"{r['date']}   {r['population']:,} people   ${r['money']:,}   loans: {r['bonds']}"))
    filters.append(f"drawbox=x=0:y=0:w={W}:h=56:color=black@0.72:t=fill")
    for i, (t, text) in enumerate(pts):
        end = pts[i + 1][0] if i + 1 < len(pts) else 99999
        if end <= t:
            continue
        f = textfile(f"top{i}.txt", text)
        filters.append(f"drawtext=fontfile={BOLD}:textfile={f}:fontsize=30:fontcolor=white:x=24:y=13:expansion=none:"
                       f"enable='between(t,{t:.1f},{end:.1f})'")
    # Bottom bar: Claude's decisions.
    filters.append(f"drawbox=x=0:y={H-76}:w={W}:h=76:color=0x14211c@0.88:t=fill")
    for i, (hms, text) in enumerate(DECISIONS):
        t = secs(hms)
        nxt = secs(DECISIONS[i + 1][0]) if i + 1 < len(DECISIONS) else 99999
        end = max(nxt, t + MIN_SHOW)
        f = textfile(f"dec{i}.txt", "Claude: " + text)
        filters.append(f"drawtext=fontfile={FONT}:textfile={f}:fontsize=28:fontcolor=0xf3d27a:x=24:y={H-54}:expansion=none:"
                       f"enable='between(t,{t:.1f},{end:.1f})'")
    filters += [f"setpts=PTS/{SPEED}", "fps=30", "format=yuv420p"]
    body = os.path.join(TMP, "body.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", SRC, "-vf", ",".join(filters), "-an",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "24", body], check=True)
    intro, outro = os.path.join(TMP, "intro.mp4"), os.path.join(TMP, "outro.mp4")
    card(intro, [("Claudeville II", 72, "#f3d27a"),
                 ("Claude plays SimCity 2000, attempt 2", 34, "white"),
                 ("Goal: 5,000 people within 30 years,", 30, "#c9d6cf"),
                 ("then 3 profitable years with no loans", 30, "#c9d6cf")], 4)
    card(outro, [("Both goals met", 72, "#f3d27a"),
                 ("5,970 people in Jan 2015 (year 15 of 30)", 32, "white"),
                 ("Profitable 2015, 2016, 2017: +$353, +$362, +$372", 32, "white"),
                 ("Zero loans all game", 32, "white"),
                 ("Attempt 1 on the same map: 4,410 people by 2030", 28, "#c9d6cf")], 6)
    lst = textfile("list.txt", "".join(f"file '{p}'\n" for p in (intro, body, outro)))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", "-movflags", "+faststart", out], check=True)


if __name__ == "__main__":
    main(sys.argv[1])
