"""firegrid.py OUT.plan [SPACING] : plan fire stations wherever the city has none within SPACING/2 tiles.

Claudeville 4 attempt 1 had 3 fire stations for up to 78,000 people; two airport plane-crash fires burned the
whole east bank (2011, 2023). This walks a grid (default every 14 tiles) over the built-up area and, at each grid
point with buildings around it but no station within SPACING/2, picks the nearest free 3x3 lot (empty land,
rubble or empty zoned land; no roads, lines, rails or buildings) touching a power line or building.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from citymap import City, is_building, is_line, is_road, is_rail, N  # noqa: E402
import sc2parse  # noqa: E402

STATION = 0xD3


def plan_tiles(names):
    """Tiles that later plans will use (attempt 2: two stations landed on a seaport road and a road junction)."""
    tiles = set()
    for name in names:
        for raw in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plans", name)):
            w = raw.split("#")[0].split()
            nums = [int(v) for v in w[1:] if v.lstrip("-").isdigit()]
            if len(nums) == 4:
                tiles |= {(x, y) for x in range(min(nums[0], nums[2]), max(nums[0], nums[2]) + 1)
                          for y in range(min(nums[1], nums[3]), max(nums[1], nums[3]) + 1)}
            elif len(nums) == 2:
                tiles |= {(nums[0] + i, nums[1] + j) for i in range(4) for j in range(4)}
    return tiles


def main(out, spacing=14, avoid=()):
    c = City()
    xt = sc2parse.chunks(sc2parse.SAVE)["XTER"]
    wet = lambda x, y: bool(xt[y * N + x] & 0xF0)
    stations = [(x, y) for x in range(N) for y in range(N) if c.t(x, y) == STATION]
    free = lambda x, y: 2 <= x < N - 2 and 2 <= y < N - 2 and c.t(x, y) in (0, 1, 2, 3, 4) and not wet(x, y)
    half = spacing // 2
    used = plan_tiles(avoid)
    picks = []
    for gx in range(half, N, spacing):
        for gy in range(half, N, spacing):
            near = [(x, y) for x in range(gx - half, gx + half) for y in range(gy - half, gy + half)
                    if 0 <= x < N and 0 <= y < N and is_building(c.t(x, y))]
            if len(near) < 12:
                continue                      # not built up here
            if any(abs(sx - gx) <= half + 1 and abs(sy - gy) <= half + 1 for sx, sy in stations + picks):
                continue
            best = None
            for d in range(0, half):
                for x in range(gx - d, gx + d + 1):
                    for y in range(gy - d, gy + d + 1):
                        lot = [(x + i, y + j) for i in range(3) for j in range(3)]
                        if best or not all(free(*p) and p not in used for p in lot):
                            continue
                        ring = [(x + i, y + j) for i in range(-1, 4) for j in range(-1, 4) if (i, j) not in
                                [(a, b) for a in range(3) for b in range(3)]]
                        if any(0 <= p[0] < N and 0 <= p[1] < N and (is_line(c.t(*p)) or is_building(c.t(*p))) for p in ring):
                            best = (x, y)
                if best:
                    break
            if best:
                picks.append(best)
                used |= {(best[0] + i, best[1] + j) for i in range(-1, 4) for j in range(-1, 4)}
    with open(out, "w") as f:
        f.write("# fire stations where the city has none within %d tiles (firegrid.py; %d existing)\n" % (half, len(stations) // 9))
        for x, y in picks:
            f.write("fire %d %d\n" % (x, y))
    print("firegrid: %d existing stations, %d new lots -> %s" % (len(stations) // 9, len(picks), out))


if __name__ == "__main__":
    # firegrid.py OUT.plan [SPACING] [--avoid plan1.plan,plan2.plan]
    av = sys.argv[sys.argv.index("--avoid") + 1].split(",") if "--avoid" in sys.argv else ()
    args = [a for a in sys.argv[2:] if a != "--avoid" and a not in ",".join(av).split(",") and a.isdigit()]
    main(sys.argv[1], int(args[0]) if args else 14, av)
