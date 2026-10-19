"""Dense strip districts (Claudeville 4 attempt 7): zone bands 3 rows deep on both sides of east-west roads 7 rows
apart, so every zone tile is within 3 tiles of a road, with north-south cross streets and power-line columns.
Attempt 6 filled the map at ~112,000 with a 7x7 grid that zoned only 44% of the land.

usage: python3 -I bot/stripplan.py OUT.plan X0 Y0 X1 Y1 TYPES [--cross N] [--line N] [--pipe-from X,Y]
  TYPES  one letter per 3-row band from the top (R homes, C shops, I factories, - leave empty), repeated to the bottom
  rows:  band (Y0..Y0+2), road (Y0+3), band (Y0+4..Y0+6), then the next period starts at Y0+7
  --cross N   north-south road every N columns (default 20; also at X0 and X1)
  --line N    power-line column every N columns between the cross streets (default 10), crossing the roads
  water tiles are left out of zones, roads and lines (the plan is split around them); the bottom band is dropped
  if the area ends before it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p  # noqa: E402

N = 128


def runs(xs):
    """consecutive runs of sorted ints -> [(a, b)]"""
    out = []
    for x in sorted(xs):
        if out and x == out[-1][1] + 1:
            out[-1][1] = x
        else:
            out.append([x, x])
    return [tuple(r) for r in out]


def main():
    a = sys.argv[1:]
    out, x0, y0, x1, y1, types = a[0], *map(int, a[1:5]), a[5]
    opt = {a[i]: a[i + 1] for i in range(6, len(a) - 1, 2)}
    cross, linep = int(opt.get("--cross", 20)), int(opt.get("--line", 10))
    c = p.chunks(p.SAVE)
    t, b = c["XTER"], c["XBLD"]
    wet = lambda x, y: t[y * N + x] >= 16
    used = lambda x, y: b[y * N + x] not in (0, 1, 2, 3, 4, 5)   # anything already built (trees/rubble are 1-5)
    ok = lambda x, y: not wet(x, y) and not used(x, y)
    xs_cross = sorted({x0, x1} | set(range(x0, x1 + 1, cross)))
    xs_line = sorted({x for a_, b_ in zip(xs_cross, xs_cross[1:]) for x in range(a_ + linep // 2, b_ - 2, linep)})
    steps = ["# stripplan.py %s" % " ".join(a[1:])]
    roads_y, bands = [], []
    y, k = y0, 0
    while y + 2 <= y1:
        bands.append((y, y + 2, types[k % len(types)])); k += 1
        if y + 3 <= y1:
            roads_y.append(y + 3)
        if y + 6 <= y1:
            bands.append((y + 4, y + 6, types[k % len(types)])); k += 1
        y += 7
    ys_all = range(y0, min(y1, y - 1) + 1)
    # lines first: a road dragged over a line makes a crossing; a line dragged over roads broke road rows (attempt 7)
    for lx in xs_line:
        for ra, rb in runs([yy for yy in ys_all if ok(lx, yy) or yy in roads_y]):
            steps.append("line %d %d %d %d" % (lx, ra, lx, rb))
    for ry in roads_y:
        for ra, rb in runs([x for x in range(x0, x1 + 1) if ok(x, ry)]):
            steps.append("road %d %d %d %d" % (ra, ry, rb, ry))
    ys_top = range(max(0, y0 - 1), min(y1, y - 1) + 1)   # cross streets reach one row up to join the road above
    for cx in xs_cross:
        for ra, rb in runs([yy for yy in ys_top if not wet(cx, yy)]):
            steps.append("road %d %d %d %d" % (cx, ra, cx, rb))
    skip = set(xs_cross) | set(xs_line)
    for ya, yb, kind in bands:
        if kind == "-":
            continue
        cols = [x for x in range(x0, x1 + 1) if x not in skip and all(ok(x, yy) for yy in range(ya, yb + 1))]
        for ra, rb in runs(cols):
            if rb - ra >= 1:
                steps.append("zone %s %d %d %d %d" % (kind, ra, ya, rb, yb))
    # water: a pipe under every road row and cross street (pipes may cross anything on land)
    for ry in roads_y:
        for ra, rb in runs([x for x in range(x0, x1 + 1) if not wet(x, ry)]):
            steps.append("pipe %d %d %d %d" % (ra, ry, rb, ry))
    for cx in xs_cross:
        for ra, rb in runs([yy for yy in range(max(0, y0 - 2), min(y1, y - 1) + 1) if not wet(cx, yy)]):
            steps.append("pipe %d %d %d %d" % (cx, ra, cx, rb))
    if "--pipe-from" in opt:
        px, py = map(int, opt["--pipe-from"].split(","))
        steps.append("pipe %d %d %d %d" % (px, py, px, y0))
    open(out, "w").write("\n".join(steps) + "\n")
    zt = sum(1 for s in steps if s.startswith("zone"))
    print("stripplan: %d roads rows, %d cross streets, %d line columns, %d zone pieces -> %s" %
          (len(roads_y), len(xs_cross), len(xs_line), zt, out))


main()
