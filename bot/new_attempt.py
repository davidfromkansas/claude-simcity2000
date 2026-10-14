"""Set up the folders and run.json for a new Claudeville 3 attempt.

usage: python3 -I bot/new_attempt.py N
Then in the game: load C3BASE.SC2, Save City As C3A<N>.SC2, start record.sh and publish.py loop.
"""
import datetime as dt
import json
import os
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C3 = os.path.join(REPO, "claudeville-3")

n = int(sys.argv[1])
base = os.path.join(C3, "attempt-%d" % n)
for sub in ("dashboard/data", "dashboard/shots", "recording-timelapse", "post-mortem"):
    os.makedirs(os.path.join(base, sub), exist_ok=True)
shutil.copy(os.path.join(C3, "dashboard-template.html"), os.path.join(base, "dashboard", "index.html"))
json.dump({"attempt": n, "status": "playing", "started": dt.date.today().isoformat()},
          open(os.path.join(base, "attempt.json"), "w"), indent=1)
run = {"save": "/opt/sc2k/game/C3A%d.SC2" % n, "city": "Claudeville 3", "attempt": n,
       "dashboard": "claudeville-3/attempt-%d/dashboard" % n,
       "recordings": "claudeville-3/attempt-%d/recording-timelapse" % n,
       "rec": "/opt/sc2k/rec-c3a%d" % n, "bonds": 0}
json.dump(run, open(os.path.join(REPO, "bot", "run.json"), "w"))
lst = json.load(open(os.path.join(C3, "attempts.json")))
if not any(a["attempt"] == n for a in lst):
    lst.append({"attempt": n, "status": "playing", "reason": ""})
for a in lst:
    if a["attempt"] == n:
        a["status"] = "playing"
json.dump(lst, open(os.path.join(C3, "attempts.json"), "w"), indent=1)
print("attempt", n, "ready:", base)
