"""Pace check: is the city on the strategy's own schedule?

Attempt 10's strategy said "attempt 4's pace" (~650 home tiles by 2005) but the block plans only
zoned ~410, and nothing compared the two until the post-mortem. This check reads the attempt's
pace.json (targets by year: population, zoned home tiles) and compares the current save.

pace.json: {"2002": {"population": 5000, "home_tiles": 600}, "2005": {...}, ...}
Targets in between are interpolated. Prints one line: "PACE: ok ..." or "PACE: behind ...".
Behind = population or zoned home tiles under 70% of the target for this date.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def target(goals, t, key):
    pts = sorted((int(y), g[key]) for y, g in goals.items() if key in g)
    if not pts or t <= pts[0][0]:
        return None if not pts or t < pts[0][0] else pts[0][1]
    for (y0, v0), (y1, v1) in zip(pts, pts[1:]):
        if y0 <= t <= y1:
            return v0 + (v1 - v0) * (t - y0) / (y1 - y0)
    return pts[-1][1]


def check(save=None, goals=None):
    run = json.load(open(os.path.join(HERE, "run.json")))
    if goals is None:
        path = os.path.join(HERE, "..", os.path.dirname(run["dashboard"]), "pace.json")
        if not os.path.exists(path):
            return "PACE: no pace.json for this attempt"
        goals = json.load(open(path))
    save = save or p.SAVE
    m = p.parse(save)
    z = p.chunks(save)["XZON"]
    homes = sum(1 for v in z if (v & 15) in (1, 2))
    t = m["year"] + MONTHS.index(m["month"]) / 12
    out, behind = [], False
    for key, have in (("population", m["population"]), ("home_tiles", homes)):
        want = target(goals, t, key)
        if want is None:
            continue
        out.append("%s %d/%d" % (key, have, want))
        behind |= have < 0.7 * want
    return "PACE: %s %s" % ("behind" if behind else "ok", " ".join(out))


def land(save=None):
    """LAND line (after attempt 11, which ran out of factory land unnoticed for a year): a zone type is
    short when its demand is high (>= 1000; 1500 missed attempt 12's factory shortage at 1,260) but under 30 of its tiles are empty."""
    save = save or p.SAVE
    m = p.parse(save)
    c = p.chunks(save)
    b, z = c["XBLD"], c["XZON"]
    empty = {"res": 0, "com": 0, "ind": 0}
    for i in range(16384):
        t = z[i] & 15
        if 1 <= t <= 6 and (b[i] == 0 or 1 <= b[i] <= 4):
            empty[("res", "res", "com", "com", "ind", "ind")[t - 1]] += 1
    short = ["%s (demand %d, %d empty)" % (k, m["demand"][k], empty[k]) for k in empty
             if m["demand"][k] >= 1000 and empty[k] < 30]
    return "LAND short: " + ", ".join(short) if short else "LAND ok: empty %s" % empty


if __name__ == "__main__":
    print(check())
    print(land())
