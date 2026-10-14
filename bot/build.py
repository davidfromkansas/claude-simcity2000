"""Build from a plan file, then check every tile against the save, retry gaps, and check the money.

usage: python3 -I build.py PLAN [--dry]

Plan lines (tile coordinates; '#' starts a comment):
  road X0 Y0 X1 Y1        straight road
  line X0 Y0 X1 Y1        straight power line
  pipe X0 Y0 X1 Y1        straight water pipe
  zone K X0 Y0 X1 Y1      rectangle; K = r R c C i I (lower case light, upper case dense)
  pump X0 Y0 X1 Y1        one pump on every tile of the line
  park X0 Y0 X1 Y1        small parks
  coal X Y | gas X Y      power plant, X Y = top-left of its 4x4
  fire X Y | police X Y   station, X Y = top-left of its 3x3
  link X Y                neighbor link at edge tile X Y; must charge $1,000
  bulldoze X0 Y0 X1 Y1    tile by tile, only tiles inside the box; never plants, stations or pumps
  bulldoze! X0 Y0 X1 Y1   same, but may remove plants, stations and pumps
  dezone X0 Y0 X1 Y1      remove zoning from empty tiles in the box

After building: every planned tile is checked in the save and missing tiles are placed one by one
(two rounds). Any tile OUTSIDE the plan that changed is reported (and roads/lines/pipes repaired).
Exit code 1 if anything is still wrong.
"""
import os
import subprocess
import sys
import time

BOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BOT)
from citymap import City, is_road, is_line, is_park, is_plant, N  # noqa: E402

TOOL = {"road": "22 105 55 113", "line": "22 82 55 90", "pipe": "47 82 85 90", "pump": "47 82 85 105",
        "r": "22 128 75 135", "R": "22 128 75 151", "c": "47 128 100 135", "C": "47 128 100 151",
        "i": "68 128 120 135", "I": "68 128 120 151", "park": "68 155 100 163",
        "fire": "47 155 88 179", "police": "47 155 88 163", "bulldoze": "22 58 60 65", "dezone": "22 58 65 130", "plant": "22 82 60 105"}
PLANT_ITEM = {"coal": (199, 145), "gas": (199, 255)}
ZCODE = {"r": 1, "R": 2, "c": 3, "C": 4, "i": 5, "I": 6}
# rough prices, used only to spot steps that charged nothing
COST = {"road": 10, "line": 5, "pipe": 3, "pump": 100, "park": 20, "coal": 4000, "gas": 2000,
        "fire": 500, "police": 500, "link": 1000, "r": 5, "R": 10, "c": 5, "C": 10, "i": 5, "I": 10}
PROTECT = lambda t: is_plant(t) or t == 0xDC or 0xD3 <= t <= 0xDB


def sh(*args):
    return subprocess.run(["bash", "-c", " ".join(str(a) for a in args)], cwd=BOT,
                          capture_output=True, text=True).stdout


def sc(*args):
    return sh("./sc", *args)


def screen(x, y):
    import tile
    return tile.to_screen(x, y)


def vis(*xy):
    sh("./vis.sh", *xy)


def tool(name):
    sc("tool", TOOL[name])
    time.sleep(0.4)


def nodlg():
    sh("./sc nodlg 2>/dev/null")


def save():
    out = sc("save")
    try:
        return int(out.split(" cash ")[1].split()[0])
    except (IndexError, ValueError):
        return None


def seg(x0, y0, x1, y1):
    if x0 != x1 and y0 != y1:
        raise ValueError("not a straight line: %s" % ((x0, y0, x1, y1),))
    sx = (x1 > x0) - (x1 < x0)
    sy = (y1 > y0) - (y1 < y0)
    out = [(x0, y0)]
    while out[-1] != (x1, y1):
        out.append((out[-1][0] + sx, out[-1][1] + sy))
    return out


def rect(x0, y0, x1, y1):
    return [(x, y) for y in range(min(y0, y1), max(y0, y1) + 1) for x in range(min(x0, x1), max(x0, x1) + 1)]


def parse(path):
    steps = []
    for n, raw in enumerate(open(path), 1):
        line = raw.split("#")[0].split()
        if not line:
            continue
        kind, args = line[0], line[1:]
        if kind == "zone":
            k, nums = args[0], list(map(int, args[1:]))
            steps.append({"kind": "zone", "z": k, "box": nums, "tiles": rect(*nums), "line": n})
            continue
        nums = list(map(int, args))
        if kind in ("road", "line", "pipe", "pump"):
            tiles = seg(*nums)
        elif kind in ("park", "bulldoze", "bulldoze!", "dezone"):
            tiles = rect(*nums)
        elif kind in ("coal", "gas"):
            tiles = rect(nums[0], nums[1], nums[0] + 3, nums[1] + 3)
        elif kind in ("fire", "police"):
            tiles = rect(nums[0], nums[1], nums[0] + 2, nums[1] + 2)
        elif kind == "link":
            tiles = [tuple(nums)]
        else:
            raise ValueError("line %d: unknown step %r" % (n, kind))
        steps.append({"kind": kind, "box": nums, "tiles": tiles, "line": n})
    return steps


def done(c, s, x, y):
    """Is planned tile (x, y) of step s in place in the save?"""
    t, k = c.t(x, y), s["kind"]
    if k in ("road", "link"):
        return is_road(t)
    if k == "line":
        return is_line(t)
    if k == "pipe":
        return c.pipe(x, y)
    if k == "pump":
        return t == 0xDC
    if k == "park":
        return is_park(t)
    if k == "zone":
        return c.zone(x, y) == ZCODE[s["z"]] or is_road(t) or is_line(t) or t >= 0xC0
    if k in ("coal", "gas"):
        return is_plant(t)
    if k in ("fire", "police"):
        return t >= 0xC0 and not is_plant(t)
    if k == "dezone":
        return c.zone(x, y) == 0 or t >= 0x70
    if k.startswith("bulldoze"):
        return t == 0 or (k == "bulldoze" and PROTECT(t))
    return True


def click_tile(x, y):
    vis(x, y)
    sc("click", *screen(x, y))
    time.sleep(0.25)


def drag(name, a, b):
    vis(*a, *b)
    tool(name)
    sc("drag", *screen(*a), *screen(*b))
    time.sleep(0.4)
    nodlg()


def place(s, c):
    k, b = s["kind"], s["box"]
    if k in ("road", "line", "pipe"):
        drag(k, b[:2], b[2:])
    elif k == "zone":
        drag(s["z"], b[:2], b[2:])
    elif k in ("pump", "park"):
        tool(k)
        for x, y in s["tiles"]:
            if not done(c, s, x, y):
                vis(x, y)
                tool(k)
                click_tile(x, y)
        nodlg()
    elif k in ("coal", "gas"):
        vis(b[0], b[1], b[0] + 3, b[1] + 3)
        tool("plant")
        time.sleep(0.6)
        sc("click", *PLANT_ITEM[k])
        time.sleep(0.6)
        sc("click", *screen(b[0] + 1, b[1] + 1))
        time.sleep(0.8)
        nodlg()
    elif k in ("fire", "police"):
        vis(b[0], b[1], b[0] + 2, b[1] + 2)
        tool(k)
        sc("click", *screen(b[0] + 1, b[1] + 1))
        time.sleep(0.8)
        nodlg()
    elif k == "link":
        x, y = b
        ix = 1 if x == 0 else N - 2 if x == N - 1 else x      # the tile just inside the edge
        iy = 1 if y == 0 else N - 2 if y == N - 1 else y
        vis(ix, iy, x, y)
        tool("road")
        sc("drag", *screen(ix, iy), *screen(x, y))
        time.sleep(1.2)
        sc("click", 265, 261)          # "build a connection to your neighbor for $1000?" -> Yes
        time.sleep(0.8)
        nodlg()
    elif k == "dezone":
        for x, y in s["tiles"]:
            if c.zone(x, y) and c.t(x, y) < 0x70:
                vis(x, y)
                tool("dezone")
                click_tile(x, y)
    elif k.startswith("bulldoze"):
        for x, y in s["tiles"]:
            t = c.t(x, y)
            if t == 0 or (k == "bulldoze" and PROTECT(t)):
                continue
            vis(x, y)
            tool("bulldoze")
            click_tile(x, y)
            click_tile(x, y)        # the first click leaves rubble, the second clears it


def retry(s, x, y):
    k = s["kind"]
    if k in ("road", "line", "pipe", "pump", "park"):
        vis(x, y)
        tool(k)
        click_tile(x, y)
        nodlg()
    elif k == "zone":
        vis(x, y)
        tool(s["z"])
        sc("drag", *screen(x, y), *screen(x, y))
        nodlg()
    elif k.startswith("bulldoze"):
        vis(x, y)
        tool("bulldoze")
        click_tile(x, y)
        click_tile(x, y)
    elif k == "dezone":
        vis(x, y)
        tool("dezone")
        click_tile(x, y)
    else:
        return False      # big buildings and the link are re-run as a whole step
    return True


def snapshot(c):
    return bytes(c.b), bytes(c.z), bytes(c.u)


def main(path, dry=False):
    steps = parse(path)
    final = {}                      # each tile is checked against the LAST step that touches it
    for s in steps:
        for p in s["tiles"]:
            final[p] = s
    plan_tiles = set(final)
    print("plan: %d steps, %d tiles" % (len(steps), len(plan_tiles)))
    if dry:
        return 0
    sc("pause")
    cash0 = save()
    before = City()
    snap0 = snapshot(before)
    expect = 0
    problems = []
    for s in steps:
        c = before
        if s["kind"] in ("pump", "park", "dezone") or s["kind"].startswith("bulldoze"):
            save()                  # these steps look at the current tiles first
            c = City()
        big = s["kind"] in ("coal", "gas", "fire", "police", "link")
        cb = save() if big else None
        if big:
            c = City()
        place(s, c)
        n = len(s["tiles"])
        expect += COST.get(s.get("z", s["kind"]), 0) * (1 if big else n)
        if big:
            ca = save()
            want = COST[s["kind"]]
            if cb is not None and ca is not None and cb - ca < want * 0.9:
                problems.append("line %d %s: cash fell only $%d (expected about $%d): not built?"
                                % (s["line"], s["kind"], cb - ca, want))
                if s["kind"] != "link" or not done(City(), s, *s["tiles"][0]):
                    place(s, City())     # one more try for the whole step
                    ca2 = save()
                    if ca is not None and ca2 is not None and ca - ca2 >= want * 0.9:
                        problems[-1] += " -> retried, now charged"
    sc("tool", TOOL["road"])
    # check every planned tile; place gaps one by one, two rounds
    for rnd in (1, 2, 3):
        cash = save()
        c = City()
        gaps = [(s, x, y) for (x, y), s in final.items() if not done(c, s, x, y)]
        if not gaps:
            break
        print("round %d: %d planned tiles missing" % (rnd, len(gaps)))
        if rnd == 3:
            for s, x, y in gaps[:20]:
                problems.append("line %d %s: tile (%d,%d) still missing" % (s["line"], s["kind"], x, y))
            break
        for s, x, y in gaps:
            if not retry(s, x, y) and s["kind"] != "link":
                place(s, City())
        sc("tool", TOOL["road"])
    # collateral: tiles outside the plan that changed
    after = City()
    snap1 = snapshot(after)
    hurt = []
    for i in range(N * N):
        p = (i % N, i // N)
        if p in plan_tiles:
            continue
        if snap0[0][i] != snap1[0][i] or snap0[1][i] != snap1[1][i] or snap0[2][i] != snap1[2][i]:
            hurt.append((p, snap0[0][i], snap1[0][i]))
    for (x, y), old, new in hurt:
        what = "road" if is_road(old) else "line" if is_line(old) else None
        fix = ""
        if what and new == 0:
            vis(x, y)
            tool(what)
            click_tile(x, y)
            fix = " -> %s re-placed" % what
        elif old == 0 and is_road(new):
            vis(x, y)
            tool("bulldoze")
            click_tile(x, y)
            click_tile(x, y)
            fix = " -> stray road removed"
        problems.append("tile (%d,%d) outside the plan changed: %#x -> %#x%s" % (x, y, old, new, fix))
    sc("tool", TOOL["road"])
    sc("pause")
    cash1 = save()
    spent = (cash0 - cash1) if cash0 is not None and cash1 is not None else None
    print("money: spent $%s, plan estimate about $%d" % (spent, expect))
    if spent is not None and spent < expect * 0.5:
        problems.append("spent $%d but the plan should cost about $%d: parts may not be built" % (spent, expect))
    for p in problems:
        print("PROBLEM", p)
    print("BUILD: %s" % ("checked, all planned tiles in place" if not problems else "%d problems" % len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], "--dry" in sys.argv))
