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
from citymap import City, ZONES, is_road, is_rail, is_building, is_line, is_plant, nbrs, N


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
    plants = sum(1 for x, y in c.tiles() if 0xC9 <= c.t(x, y) <= 0xD1)
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
    # Claudeville 4 (2023): a coal plant sat with no line into the grid for years and its blocks went dark
    ptiles = {(x, y) for x, y in c.tiles() if is_plant(c.t(x, y))}
    pseen = set()
    for p in sorted(ptiles):
        if p in pseen:
            continue
        grp = c.flood([p], lambda x, y: (x, y) in ptiles)
        pseen |= grp
        if not any(q not in ptiles and (is_line(c.t(*q)) or is_building(c.t(*q))) for g in grp for q in nbrs(*g)):
            add("FAIL", "power plant at (%d,%d): no line or building touches it, so its power goes nowhere" % min(grp))

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
        # Claudeville 4 (2012-2023): pipe networks that never reached a pump left ~500 buildings dry for years - FAIL now
        if pumps and len(reg) >= 12 and not any(q in net for p in reg for q in [p, *nbrs(*p)]):
            add("FAIL", "%s %s: no pipe joined to a pump in or next to it (water cannot reach it)" % (ZONES[k], box(reg)))

    # 4. road access
    roads = [[False] * N for _ in range(N)]
    for x, y in c.tiles():
        roads[y][x] = is_road(c.t(x, y))
    def near_road(x, y, r):
        return any(roads[j][i] for j in range(max(0, y - r), min(N, y + r + 1))
                   for i in range(max(0, x - r), min(N, x + r + 1)))
    # Claudeville 4 attempt 2: a seaport road and a neighbour-link road sat unconnected, and a stray calibration
    # road tile blocked a zoo site - every road piece must join the main network
    rtiles = {(x, y) for x, y in c.tiles() if roads[y][x]}
    comps, rseen = [], set()
    for p in sorted(rtiles):
        if p not in rseen:
            comp = c.flood([p], lambda x, y: (x, y) in rtiles)
            rseen |= comp
            comps.append(comp)
    comps.sort(key=len, reverse=True)
    for comp in comps[1:]:
        what = "stray road tile" if len(comp) == 1 else "road piece of %d tiles" % len(comp)
        add("FAIL", "%s at %s is not joined to the main road network" % (what, box(comp)))
    far = []
    for k, reg in regions:
        if not any(near_road(x, y, 1) for x, y in reg):
            add("FAIL", "%s %s: no road touches it" % (ZONES[k], box(reg)))
        far += [p for p in reg if not near_road(p[0], p[1], 3)]
    if far:
        add("WARN", "%d zone tiles more than 3 tiles from a road, e.g. (%d,%d)" % (len(far), *far[0]))

    # 6. demand caps (Prima guide ch.16): homes stop near 15,000 people without stadium/zoo/marina;
    #    factories need a rail/highway link or a seaport; shops need road links or an airport (from ~20,000)
    pop = c.misc.get("population", 0)
    dem = c.misc.get("demand", {})
    count = lambda code: sum(1 for x, y in c.tiles() if c.t(x, y) == code)
    lifters = count(0xD7) // 16 + count(0xDA) // 16 + count(0xF8) // 9
    rail_link = any(is_rail(c.t(x, y)) for x, y in c.tiles() if x in (0, N - 1) or y in (0, N - 1))
    seaport = any(c.zone(x, y) == 9 for x, y in c.tiles())
    airport = any(c.zone(x, y) == 8 for x, y in c.tiles())
    if pop > 10000 and lifters * 15000 + 15000 < pop + 5000:
        add("WARN", "home cap: %d stadium/zoo/marina for %d people - build one before ~%d" % (lifters, pop, 15000 * (lifters + 1)))
    if pop > 3000 and not (rail_link or seaport):
        add("WARN", "factory cap: no rail link off the map edge and no seaport")
    # attempt 17: factories stalled at ~9,300 factory workers - the spec gives 10,000 factory workers per seaport
    # crane / rail / highway link; warn from 8,000 workers per unit of trade capacity
    ind_pop = (c.misc.get("taxed_pop") or {}).get("ind", 0)
    cranes = count(0xE0)                 # seaport crane tile (research script port.py)
    units = max(1, cranes) + (1 if rail_link else 0)
    if ind_pop > 8000 * units:
        add("WARN", "factory trade capacity: %d factory workers for ~%d units (10,000 each) - add a seaport or a rail/highway link" % (ind_pop, units))
    # Claudeville 4: 3 fire stations for 78,000 people - two airport fires burned the whole east bank
    stations = count(0xD2) // 9 if count(0xD2) else sum(1 for x, y in c.tiles() if c.t(x, y) in range(0xD2, 0xD3))
    fires = c.misc.get("services", {}).get("fire", {}).get("count", stations)
    if pop > 6000 and fires * 6000 < pop - 6000:
        add("WARN", "fire cover: %d fire stations for %d people - want one per ~6,000 people (every ~14 tiles)" % (fires, pop))
    if pop > 18000 and not airport:
        add("WARN", "shop cap: no airport (helps from ~20,000 people)")

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
