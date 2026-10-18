"""Fire map (Claudeville 4, Apr 2011 plane crash): flames are not in the save, so read them off the screen.
Prints, for the visible tiles, F = burning, r = rubble, B = building/zone, . = other, and lists
'front' tiles: unburnt buildings next to a burning tile (firebreak candidates).
Usage: firemap.py [png]  (needs a fresh tile.py calibration)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import tile
from citymap import City, is_rubble, is_building, is_road, is_line
png = sys.argv[1] if len(sys.argv) > 1 else "/tmp/sc/now.png"
im = Image.open(png).convert("RGB"); W, H = im.size
m = City()
def flame(x, y):
    sx, sy = tile.to_screen(x, y)
    if not (90 <= sx < W - 20 and 70 <= sy < H - 10): return None
    n = 0
    for dx in range(-5, 6, 2):
        for dy in range(-7, 3, 2):
            r, g, b = im.getpixel((sx + dx, sy + dy))
            if r > 200 and g < 140 and b < 60: n += 1
    return n >= 4
fire = {}
for x in range(128):
    for y in range(128):
        f = flame(x, y)
        if f is not None: fire[(x, y)] = f
front = set()
for (x, y), f in fire.items():
    if f: continue
    t = m.t(x, y)
    if is_rubble(t) or t == 0 or is_road(t): continue
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if fire.get((x + dx, y + dy)): front.add((x, y))
print("burning tiles on screen:", sum(fire.values()), "front tiles:", len(front))
xs = sorted({x for x, y in fire}); ys = sorted({y for x, y in fire})
for y in range(min(ys), max(ys) + 1):
    row = ""
    for x in range(min(xs), max(xs) + 1):
        if (x, y) not in fire: row += " "; continue
        t = m.t(x, y)
        row += "F" if fire[(x, y)] else "*" if (x, y) in front else "r" if is_rubble(t) else "=" if is_road(t) else "B" if t else "."
    print("%3d %s" % (y, row))
print("x from", min(xs))
if "--plan" in sys.argv:
    out = sys.argv[sys.argv.index("--plan") + 1]
    with open(out, "w") as f:
        f.write("# firebreak: unburnt buildings touching flames (firemap.py)\n")
        for x, y in sorted(front): f.write("bulldoze %d %d %d %d\n" % (x, y, x, y))
    print("plan", out, len(front))
