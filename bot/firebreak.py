"""firebreak.py PNG PLAN [maxy]: plan a two-tile firebreak (unburnt buildings touching flames + their neighbours)
from a screenshot read by firemap.py. Claudeville 4, Apr 2011 plane-crash fire."""
import sys, os
png, out = sys.argv[1], sys.argv[2]
sys.argv = ['firemap.py', png]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'firemap.py')).read().split('print("burning')[0])
ring = set(front)
for (x, y) in list(front):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            p = (x + dx, y + dy); t = m.t(*p)
            if p in fire and not fire[p] and t and not is_rubble(t) and not is_road(t) and not is_line(t): ring.add(p)
open(out, 'w').write("# firebreak from %s\n" % png + "".join("bulldoze %d %d %d %d\n" % (x, y, x, y) for x, y in sorted(ring)))
print("firebreak tiles:", len(ring))
