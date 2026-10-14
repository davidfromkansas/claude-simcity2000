"""Stall alarm: a zone type with demand that has not grown for 6 game months gets checked at once.

usage: python3 -I stall.py      (run after every save; step.sh does this)
Keeps a short history per attempt in /tmp/sc/stall-A<N>.json. When homes, shops or factories have had
positive demand for >= 150 game days while their working buildings did not increase and empty zoned
land exists, it prints STALL and a diagnosis of sample empty and abandoned tiles of that type:
can power reach it, is a pipe near, distance to road, land value, pollution, crime, plus the link check.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from citymap import City, is_road, nbrs, N  # noqa: E402
import sc2parse  # noqa: E402

TYPES = {"res": (1, 2), "com": (3, 4), "ind": (5, 6)}
NAME = {"res": "homes", "com": "shops", "ind": "factories"}
ABANDONED = (0x8A, 0x8B)
WINDOW = 150          # game days (6 months of 25 days)


def counts(c):
    out = {}
    for k, codes in TYPES.items():
        built = empty = 0
        for x, y in c.tiles():
            if c.zone(x, y) in codes:
                t = c.t(x, y)
                if t >= 0x70 and t not in ABANDONED:
                    built += 1
                elif t == 0:
                    empty += 1
        out[k] = {"built": built, "empty": empty}
    return out


def road_dist(c, x, y):
    for r in range(0, 8):
        for j in range(max(0, y - r), min(N, y + r + 1)):
            for i in range(max(0, x - r), min(N, x + r + 1)):
                if is_road(c.t(i, j)):
                    return r
    return 99


def describe(c, reach, net, x, y):
    region_power = any(q in reach for q in [(x, y), *nbrs(x, y)])
    pipe = any(abs(i - x) <= 2 and abs(j - y) <= 2 for i, j in net) if net else False
    return ("(%d,%d) power-reach %s, pipe near %s, road %d tiles away, land value %d, pollution %d, crime %d"
            % (x, y, "yes" if region_power else "NO", "yes" if pipe else "NO", road_dist(c, x, y),
               c.land_value(x, y), c.half(c.plt, x, y), c.half(c.crm, x, y)))


def diagnose(c, k):
    reach = c.power_reach()
    pumps = [(x, y) for x, y in c.tiles() if c.t(x, y) == 0xDC]
    net = c.flood(pumps, lambda x, y: c.pipe(x, y)) if pumps else set()
    codes = TYPES[k]
    empty = [(x, y) for x, y in c.tiles() if c.zone(x, y) in codes and c.t(x, y) == 0]
    aband = [(x, y) for x, y in c.tiles() if c.zone(x, y) in codes and c.t(x, y) in ABANDONED]
    pick = lambda l: [l[i * len(l) // 3] for i in range(min(3, len(l)))]
    lines = ["  empty   " + describe(c, reach, net, *p) for p in pick(empty)]
    lines += ["  abandon " + describe(c, reach, net, *p) for p in pick(aband)]
    if not any(is_road(c.t(x, y)) for x, y in c.tiles() if x in (0, N - 1) or y in (0, N - 1)):
        lines.append("  NO NEIGHBOR LINK (no road on the map edge)")
    return lines


def main():
    m = sc2parse.parse(sc2parse.SAVE)
    c = City()
    run = sc2parse.RUN
    path = "/tmp/sc/stall-A%s.json" % run.get("attempt", 0)
    hist = json.load(open(path)) if os.path.exists(path) else []
    day = m["founded"] * 300 + m["days"]
    hist = [h for h in hist if h["day"] < day] + [{"day": day, "demand": m["demand"], "n": counts(c)}]
    hist = hist[-40:]
    json.dump(hist, open(path, "w"))
    old = [h for h in hist if h["day"] <= day - WINDOW]
    if not old:
        print("stall check: not enough history yet")
        return 0
    base = old[-1]
    span = [h for h in hist if h["day"] >= base["day"]]
    alarms = 0
    for k in TYPES:
        demand_on = all(h["demand"][k] > 0 for h in span)
        grew = hist[-1]["n"][k]["built"] > base["n"][k]["built"]
        if demand_on and not grew and hist[-1]["n"][k]["empty"] > 0:
            alarms += 1
            print("STALL %s: demand positive for %d days but no new buildings (%d built, %d empty tiles)"
                  % (NAME[k], day - base["day"], hist[-1]["n"][k]["built"], hist[-1]["n"][k]["empty"]))
            print("\n".join(diagnose(c, k)))
    if not alarms:
        print("stall check: OK")
    return 1 if alarms else 0


if __name__ == "__main__":
    sys.exit(main())
