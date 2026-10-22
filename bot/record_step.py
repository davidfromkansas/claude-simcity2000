"""Keep the per-attempt record that the checks alone used to throw away. Called by step.sh after every step.

usage: python3 -I record_step.py STEP_OUTPUT_FILE

Writes into the attempt's dashboard/data/ (and saves/):
  checks.jsonl   every step's full check output (health, audit, stall) with the game date
  unlocks.json   the first game date each unlock / service appeared (links, ports, stadium, zoo, ...)
  budget.json    one row per game year: January cash, change over the year, loans, tax rates, population,
                 estimated property tax (1.29 x pop x rate) and the budget-window screenshot path
  saves/<prefix><N>/<YYYY>-<MM>.SC2 (prefix C3A, C4A, ...)   a copy of the save at the first step of each game year
The budget-window screenshot itself is taken by step.sh (it needs the game) when this prints BUDGET_SHOT.
"""
import json
import os
import shutil
import sys
import time

BOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BOT)
import sc2parse  # noqa: E402
from citymap import City, is_road, is_rail, N  # noqa: E402

REPO = os.path.dirname(BOT)
RUN = sc2parse.RUN
DATA = os.path.join(REPO, RUN["dashboard"], "data")
SAVES = os.path.join(REPO, "saves", "%s%s" % (RUN.get("prefix", "C3A"), RUN.get("attempt")))
MONTHS = sc2parse.MONTHS


def load(name, default):
    p = os.path.join(DATA, name)
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return default


def dump(name, obj):
    json.dump(obj, open(os.path.join(DATA, name), "w"), indent=1)


def unlocks(c):
    tiles = list(c.tiles())
    edge = [(x, y) for x, y in tiles if x in (0, N - 1) or y in (0, N - 1)]
    count = lambda code: sum(1 for x, y in tiles if c.t(x, y) == code)
    zone = lambda k: any(c.zone(x, y) == k for x, y in tiles)
    s = c.misc["services"]
    return {
        "road link": any(is_road(c.t(*p)) for p in edge),
        "rail link": any(is_rail(c.t(*p)) for p in edge),
        "seaport": zone(9), "airport": zone(8),
        "stadium": count(0xD7) >= 16, "zoo": count(0xDA) >= 16, "marina": count(0xF8) >= 9,
        "fire station": s["fire"]["count"] > 0, "police station": s["police"]["count"] > 0,
        "school": s["schools"]["count"] > 0, "hospital": s["health"]["count"] > 0,
    }


def main(out_path):
    os.makedirs(DATA, exist_ok=True)
    text = open(out_path).read() if os.path.exists(out_path) else ""
    c = City()
    m = c.misc
    date, year = m["date"], m["year"]
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    with open(os.path.join(DATA, "checks.jsonl"), "a") as f:
        f.write(json.dumps({"date": date, "t": now, "output": text}) + "\n")

    u = load("unlocks.json", {})
    for name, have in unlocks(c).items():
        if have and name not in u:
            u[name] = date
    dump("unlocks.json", u)

    # first step of a new game year: keep a dated copy of the save and a budget row
    os.makedirs(SAVES, exist_ok=True)
    have_year = any(f.startswith("%d-" % year) for f in os.listdir(SAVES))
    if not have_year:
        shutil.copy(sc2parse.SAVE, os.path.join(SAVES, "%d-%02d.SC2" % (year, MONTHS.index(m["month"]) + 1)))
        b = load("budget.json", [])
        prev = b[-1] if b else None
        t = m["tax"]
        pops = m["taxed_pop"]
        est = 1.29 * (t["res"] * pops["res"] + t["com"] * pops["com"] + t["ind"] * pops["ind"]) / 100
        row = {"year": year, "date": date, "cash": m["money"], "loans": m["bonds"],
               "cash_change": (m["money"] - prev["cash"]) if prev else None,
               "population": m["population"], "tax": t, "est_property_tax": round(est),
               "budget_shot": "budget/%d.png" % year}
        b.append(row)
        dump("budget.json", b)
        print("BUDGET_SHOT %d" % year)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
