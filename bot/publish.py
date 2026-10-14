"""Dashboard publisher.

  python3 publish.py loop        every 5 min: screenshot + metrics + push
  python3 publish.py once        do one round now (no wait)
  python3 publish.py log TYPE TEXT   add an activity-feed entry
"""
import datetime as dt
import fcntl
import json
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Dashboard folder: run.json "dashboard" (repo-relative) or the older docs/<docs> layout.
DOCS = os.path.normpath(os.path.join(REPO, sc2parse.RUN["dashboard"]) if "dashboard" in sc2parse.RUN
                        else os.path.join(REPO, "docs", sc2parse.RUN.get("docs", ".")))
# Finished video parts go here (repo-relative); default is the dashboard's recordings/.
VIDS = os.path.normpath(os.path.join(REPO, sc2parse.RUN.get("recordings", os.path.relpath(os.path.join(DOCS, "recordings"), REPO))))
DATA = os.path.join(DOCS, "data")
SAVE = sc2parse.SAVE
REC = sc2parse.RUN.get("rec", "/opt/sc2k/rec")
BRANCH = "claude/dreamy-ritchie-bw5sjl"
LOCK = "/tmp/sc/git.lock"
INTERVAL = 300


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load(name, default):
    try:
        return json.load(open(os.path.join(DATA, name)))
    except (OSError, ValueError):
        return default


def dump(name, obj):
    tmp = os.path.join(DATA, name + ".tmp")
    json.dump(obj, open(tmp, "w"), separators=(",", ":"))
    os.replace(tmp, os.path.join(DATA, name))


def flat(m):
    """Turn parsed save into one row for the charts."""
    gr = m["graphs"]
    last = lambda k: (gr.get(k) or [0])[0]
    s = m["services"]
    return {
        "t": now(), "date": m["date"], "gy": round(m["founded"] + m["days"] / 300, 3),
        "year": m["year"], "population": m["population"], "money": m["money"],
        "bonds": m["bonds"],
        "res_tiles": m["res_tiles"], "com_tiles": m["com_tiles"], "ind_tiles": m["ind_tiles"],
        "dem_r": m["demand"]["res"], "dem_c": m["demand"]["com"], "dem_i": m["demand"]["ind"],
        "tax_r": m["tax"]["res"], "tax_c": m["tax"]["com"], "tax_i": m["tax"]["ind"],
        "crime": m["avg_crime"], "pollution": m["avg_pollution"], "traffic": m["avg_traffic"],
        "land_value": m["avg_land_value"], "city_value": m["city_value"],
        "life_exp": m["life_expectancy"], "edu": m["education_eq"], "workforce": m["workforce_pct"],
        "health": last("health"), "unemployment": last("unemployment"),
        "power_pct": last("power_pct"), "water_pct": last("water_pct"),
        "police": s["police"]["count"], "fire": s["fire"]["count"],
        "schools": s["schools"]["count"], "hospitals": s["health"]["count"],
        "colleges": s["colleges"]["count"],
        "watered_pct": m["health"]["watered_pct"], "powered_pct": m["health"]["powered_pct"],
        "abandoned": m["health"]["abandoned"], "jammed": m["health"]["jammed_road_tiles"],
        "rail": s["rail"]["count"], "subway": s["subway"]["count"], "arco_pop": m["arco_population"],
        "zoned_res": m["zoned_tiles"]["res"], "zoned_com": m["zoned_tiles"]["com"], "zoned_ind": m["zoned_tiles"]["ind"],
    }


def record_metrics():
    if not os.path.exists(SAVE):
        return None
    m = sc2parse.parse(SAVE)
    rows = load("metrics.json", [])
    row = flat(m)
    if not rows or rows[-1]["gy"] != row["gy"] or rows[-1]["money"] != row["money"]:
        rows.append(row)
        dump("metrics.json", rows)
    m["updated"] = now()
    dump("latest.json", m)
    return m


def screenshot(m):
    os.makedirs("/tmp/sc", exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    png = "/tmp/sc/pub.png"
    win = subprocess.run(["xdotool", "search", "--name", "DOSBox"], capture_output=True, text=True,
                         env={**os.environ, "DISPLAY": ":99"}).stdout.split()
    subprocess.run(["import", "-display", ":99", "-window", win[0] if win else "root", png], check=True)
    jpg = os.path.join(DOCS, "shots", stamp + ".jpg")
    subprocess.run(["convert", png, "-quality", "80", jpg], check=True)
    shutil.copy(jpg, os.path.join(DOCS, "live.jpg"))
    shots = load("shots.json", [])
    shots.append({"t": now(), "file": "shots/" + stamp + ".jpg",
                  "date": m["date"] if m else "", "population": m["population"] if m else 0})
    dump("shots.json", shots)


def recordings():
    """Copy finished video parts into docs (the newest one is still recording)."""
    if not os.path.isdir(REC):
        return
    parts = sorted(f for f in os.listdir(REC) if f.endswith(".mp4"))
    listed = load("recordings.json", [])
    names = {r["file"] for r in listed}
    for f in parts[:-1]:
        src = os.path.join(REC, f)
        rel = os.path.relpath(os.path.join(VIDS, f), DOCS)
        if rel in names or os.path.getsize(src) < 10000:
            continue
        if os.path.getsize(src) > 90e6:   # GitHub file limit is 100 MB
            continue
        os.makedirs(VIDS, exist_ok=True)
        shutil.copy(src, os.path.join(VIDS, f))
        listed.append({"file": rel, "t": now(), "mb": round(os.path.getsize(src) / 1e6, 1)})
    dump("recordings.json", listed)


def push(msg):
    os.makedirs("/tmp/sc", exist_ok=True)
    with open(LOCK, "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        git = lambda *a: subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True)
        git("add", DOCS, VIDS)
        if git("diff", "--cached", "--quiet").returncode == 0:
            return
        git("commit", "-q", "-m", msg)
        for wait in (2, 4, 8, 16, 0):
            if git("push", "-q", "origin", BRANCH).returncode == 0:
                return
            time.sleep(wait)


def log(kind, text):
    m = sc2parse.parse(SAVE) if os.path.exists(SAVE) else None
    feed = load("activity.json", [])
    feed.append({"t": now(), "date": m["date"] if m else "", "type": kind, "text": text,
                 "population": m["population"] if m else 0, "money": m["money"] if m else 0})
    dump("activity.json", feed)


def once():
    m = record_metrics()
    screenshot(m)
    recordings()
    push("Dashboard update: %s, pop %s" % (m["date"], m["population"]) if m else "Dashboard update")


if __name__ == "__main__":
    for sub in ("data", "shots"):
        os.makedirs(os.path.join(DOCS, sub), exist_ok=True)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "once"
    if cmd == "log":
        log(sys.argv[2], " ".join(sys.argv[3:]))
    elif cmd == "metrics":
        record_metrics()
    elif cmd == "loop":
        while True:
            try:
                once()
            except Exception as e:  # keep the loop alive
                print(now(), "error:", e, flush=True)
            time.sleep(INTERVAL)
    else:
        once()
