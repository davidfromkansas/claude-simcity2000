"""City check from the save: catches the setup mistakes that cost attempt 5 ten years.

usage: python3 -I audit.py [SAVE]     prints OK / WARN / FAIL lines; exit code 1 if anything FAILs.

FAIL  no road on the map edge (no neighbor link, so no trade)
FAIL  a zone area that power cannot reach (parks, gaps and empty zones do not carry power)
FAIL  a zone area with no road touching it
FAIL  a pump with no power, or not joined to any pipe
WARN  zone areas with no pipe in or next to them, zone tiles more than 3 tiles from a road,
      low spare power/water, buildings without power or water
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from citymap import City, ZONES, is_road, is_building, nbrs, N


def box(reg):
    xs = [p[0] for p in reg]
    ys = [p[1] for p in reg]
    return "x%d-%d y%d-%d" % (min(xs), max(xs), min(ys), max(ys))


def audit(path=None, city=None):
    c = city or City(path)
    out = []
    add = lambda level, text: out.append((level, text))

    # 1. neighbor link
    edge = [(x, y) for x, y in c.tiles() if (x in (0, N - 1) or y in (0, N - 1)) and is_road(c.t(x, y))]
    if edge:
        add("OK", "neighbor link: road on the map edge at " + ", ".join("(%d,%d)" % p for p in edge[:4]))
    else:
        add("FAIL", "no road on the map edge: no neighbor link, so shops and factories get no trade")

    # 2. power reaches every zone area
    reach = c.power_reach()
    plants = sum(1 for x, y in c.tiles() if 0xC9 <= c.t(x, y) <= 0xD2)
    if not plants:
        add("FAIL", "no power plant")
    regions = c.zone_regions()
    dark = []
    for k, reg in regions:
        if not any(p in reach or any(q in reach for q in nbrs(*p)) for p in reg):
            dark.append((k, reg))
    for k, reg in dark:
        add("FAIL", "%s %s (%d tiles): power cannot reach it" % (ZONES[k], box(reg), len(reg)))
    if plants and not dark:
        add("OK", "power reaches all %d zone areas" % len(regions))

    # 3. pumps powered and joined to pipes
    pumps = [(x, y) for x, y in c.tiles() if c.t(x, y) == 0xDC]
    net = c.flood(pumps, lambda x, y: c.pipe(x, y))
    for p in pumps:
        if p not in reach:
            add("FAIL", "pump at (%d,%d) has no power" % p)
    comps, seen = [], set()
    for p in pumps:
        if p in seen:
            continue
        comp = c.flood([p], lambda x, y: c.pipe(x, y))
        seen |= comp
        pipes = [q for q in comp if c.t(*q) != 0xDC]
        if not pipes:
            add("FAIL", "pump(s) near (%d,%d) not joined to any pipe" % p)
        comps.append(comp)
    if pumps and all(any(c.t(*q) != 0xDC for q in comp) for comp in comps):
        add("OK", "%d pumps, all joined to pipes" % len(pumps))
    if not pumps:
        add("WARN", "no water pumps")
    for k, reg in regions:
        if pumps and not any(q in net for p in reg for q in [p, *nbrs(*p)]):
            add("WARN", "%s %s: no pipe in or next to it" % (ZONES[k], box(reg)))

    # 4. road access
    roads = [[False] * N for _ in range(N)]
    for x, y in c.tiles():
        roads[y][x] = is_road(c.t(x, y))
    def near_road(x, y, r):
        return any(roads[j][i] for j in range(max(0, y - r), min(N, y + r + 1))
                   for i in range(max(0, x - r), min(N, x + r + 1)))
    far = []
    for k, reg in regions:
        if not any(near_road(x, y, 1) for x, y in reg):
            add("FAIL", "%s %s: no road touches it" % (ZONES[k], box(reg)))
        far += [p for p in reg if not near_road(p[0], p[1], 3)]
    if far:
        add("WARN", "%d zone tiles more than 3 tiles from a road, e.g. (%d,%d)" % (len(far), *far[0]))

    # 5. capacity and service
    g = c.misc["graphs"]
    for name in ("power_pct", "water_pct"):
        v = (g.get(name) or [None])[0]
        if v is not None and c.misc.get("population", 1) and v < 15 and (name == "power_pct" or pumps):
            add("WARN", "spare %s only %d%%: build more" % (name.split("_")[0], v))
    bl = [(x, y) for x, y in c.tiles() if 0x70 <= c.t(x, y) < 0xC0]
    unp = sum(1 for p in bl if not c.powered(*p))
    dry = sum(1 for p in bl if not c.watered(*p))
    if bl and unp:
        add("WARN", "%d buildings without power" % unp)
    if bl and pumps and dry > len(bl) // 10:
        add("WARN", "%d of %d buildings without water" % (dry, len(bl)))
    return out


if __name__ == "__main__":
    res = audit(sys.argv[1] if len(sys.argv) > 1 else None)
    for level, text in res:
        print("%-4s %s" % (level, text))
    fails = sum(1 for l, _ in res if l == "FAIL")
    print("AUDIT: %s" % ("FAIL (%d problems) - fix before running the game" % fails if fails else "passed"))
    sys.exit(1 if fails else 0)
