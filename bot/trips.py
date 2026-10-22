"""Trip check (after attempt 15): can empty zone tiles pass the game's trip test?

From the reverse-engineered growth code (sc2kfix, hook_tilegrowthorplacement.cpp; PPP p.400): an empty
zone tile only develops if a simulated trip succeeds. The trip starts at a road within reach of the tile,
then random-walks along roads with a budget of 100 steps (3 per road tile, so ~33 road tiles), and
succeeds when a tile next to the route is a destination zone (any zoned tile of the wanted kind, empty or
built) or when it reaches a road on the map edge (a neighbour connection). Failed trips = no growth,
however high the demand bar. Attempts 10-15 stalled with empty factory land at maximum demand.

This estimates, for each empty zone tile, the share of random trips that succeed (Monte Carlo), using:
  homes -> shops or factories;  shops -> homes;  factories -> homes   (assumption; see README note)
usage: python3 -I trips.py [SAVE] [--all]
Prints a summary per zone type and the worst areas; "TRIPS: weak" when an area of empty tiles of a type
with demand > 500 has 20+ tiles under 30% success.
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p  # noqa: E402

N = 128
STEPS = 33
TRIES = 60
OFFS = [(dx, dy) for dx in range(-3, 4) for dy in range(-3, 4)
        if (dx == 0 or dy == 0 or (abs(dx) <= 2 and abs(dy) <= 2 and abs(dx) + abs(dy) <= 3)) and (dx, dy) != (0, 0)]
WANT = {"res": ("com", "ind"), "com": ("res",), "ind": ("res",)}
KIND = {1: "res", 2: "res", 3: "com", 4: "com", 5: "ind", 6: "ind"}


def is_road(t):
    return 0x1D <= t <= 0x2B or 0x43 <= t <= 0x46 or 0x51 <= t <= 0x59


def run(save=None, show_all=False):
    save = save or p.SAVE
    c = p.chunks(save)
    b, z = c["XBLD"], c["XZON"]
    m = p.parse(save)
    kind = [KIND.get(z[i] & 15) for i in range(N * N)]
    road = [is_road(b[i]) for i in range(N * N)]

    def near_kinds(x, y):
        s = set()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            u, v = x + dx, y + dy
            if 0 <= u < N and 0 <= v < N and kind[v * N + u]:
                s.add(kind[v * N + u])
        return s

    rnd = random.Random(1)

    def trip(x, y, want):
        px, py = None, None
        for _ in range(STEPS):
            if x in (0, N - 1) or y in (0, N - 1):
                return True
            if near_kinds(x, y) & set(want):
                return True
            nb = [(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                  if 0 <= x + dx < N and 0 <= y + dy < N and road[(y + dy) * N + x + dx] and (x + dx, y + dy) != (px, py)]
            if not nb:
                return False
            px, py = x, y
            x, y = rnd.choice(nb)
        return False

    res = {}
    for i in range(N * N):
        k = kind[i]
        if not k or b[i] != 0:
            continue
        x, y = i % N, i // N
        starts = [(x + dx, y + dy) for dx, dy in OFFS if 0 <= x + dx < N and 0 <= y + dy < N and road[(y + dy) * N + x + dx]]
        if not starts:
            res[(x, y)] = (k, 0.0, "no road in reach")
            continue
        ok = sum(trip(*rnd.choice(starts), WANT[k]) for _ in range(TRIES))
        res[(x, y)] = (k, ok / TRIES, "")
    out = []
    for k in ("res", "com", "ind"):
        vals = [v[1] for v in res.values() if v[0] == k]
        if not vals:
            continue
        weak = [xy for xy, v in res.items() if v[0] == k and v[1] < 0.3]
        out.append("%s: %d empty tiles, mean trip success %.0f%%, %d under 30%%" % (k, len(vals), 100 * sum(vals) / len(vals), len(weak)))
        if len(weak) >= 20 and m["demand"][k] > 500:   # small pockets fill anyway (attempt 16: 11 home tiles)
            xs = [x for x, _ in weak]
            ys = [y for _, y in weak]
            out.append("TRIPS: weak %s land (demand %d): %d tiles around x%d-%d y%d-%d" % (k, m["demand"][k], len(weak), min(xs), max(xs), min(ys), max(ys)))
    if show_all:
        for xy, v in sorted(res.items()):
            out.append("%s %s %.2f %s" % (xy, v[0], v[1], v[2]))
    return "\n".join(out) if out else "TRIPS: no empty zone tiles"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    print(run(args[0] if args else None, "--all" in sys.argv))
