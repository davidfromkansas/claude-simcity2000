"""Set up the folders and run.json for a new attempt of a challenge (Claudeville 3 by default, or Claudeville 4).

usage: python3 -I bot/new_attempt.py N [claudeville-3|claudeville-4]
Then in the game: load C3BASE.SC2 (both challenges use the same flat map), Save City As <prefix><N>.SC2
(C3A<N> / C4A<N>), start record.sh and publish.py loop. begin_attempt.sh does all of this.
"""
import datetime as dt
import json
import os
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHALLENGES = {"claudeville-3": ("Claudeville 3", "C3A"), "claudeville-4": ("Claudeville 4", "C4A")}

n = int(sys.argv[1])
slug = sys.argv[2] if len(sys.argv) > 2 else "claudeville-3"
name, prefix = CHALLENGES[slug]
C = os.path.join(REPO, slug)
base = os.path.join(C, "attempt-%d" % n)
for sub in ("dashboard/data", "dashboard/shots", "recording-timelapse", "post-mortem"):
    os.makedirs(os.path.join(base, sub), exist_ok=True)
shutil.copy(os.path.join(C, "dashboard-template.html"), os.path.join(base, "dashboard", "index.html"))
json.dump({"attempt": n, "status": "playing", "started": dt.date.today().isoformat()},
          open(os.path.join(base, "attempt.json"), "w"), indent=1)
run = {"save": "/opt/sc2k/game/%s%d.SC2" % (prefix, n), "city": name, "challenge": slug, "prefix": prefix,
       "attempt": n,
       "dashboard": "%s/attempt-%d/dashboard" % (slug, n),
       "recordings": "%s/attempt-%d/recording-timelapse" % (slug, n),
       "rec": "/opt/sc2k/rec-%s%d" % (prefix.lower(), n), "bonds": 0}
json.dump(run, open(os.path.join(REPO, "bot", "run.json"), "w"))
lst = json.load(open(os.path.join(C, "attempts.json")))
if not any(a["attempt"] == n for a in lst):
    lst.append({"attempt": n, "status": "playing", "reason": ""})
for a in lst:
    if a["attempt"] == n:
        a["status"] = "playing"
json.dump(lst, open(os.path.join(C, "attempts.json"), "w"), indent=1)
print("attempt", n, "of", name, "ready:", base)
