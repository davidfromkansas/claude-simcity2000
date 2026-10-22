"""overlap.py PLAN... : count planned tiles that are already occupied on the current map (attempt 11: reused plans assumed
another attempt's neighbours). Run before building any reused plan."""
import sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from citymap import City
c = City()
for p in sys.argv[1:]:
    occ = tot = 0; ex = []
    for ln in open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'plans','%s.plan') % p):
        f = ln.split()
        if not f or f[0].startswith('#'): continue
        nums = [int(v) for v in f if v.lstrip('-').isdigit()]
        if f[0] in ('coal', 'zoo', 'stadium', 'fire', 'police', 'gas'):
            n = 4 if f[0] in ('coal', 'zoo', 'stadium', 'gas') else 3
            x0, y0 = nums[:2]; x1, y1 = x0 + n - 1, y0 + n - 1
        elif len(nums) >= 4: x0, y0, x1, y1 = nums[:4]
        else: continue
        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y0, y1) + 1):
                tot += 1
                if c.t(x, y) or c.zone(x, y):
                    occ += 1; ex.append((x, y))
    print(p, 'tiles', tot, 'occupied', occ, ex[:6])
