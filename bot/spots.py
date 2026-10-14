"""Find NxN spots of empty land (or empty zoned land) inside the city. usage: spots.py N [x0 x1 y0 y1]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p
n = int(sys.argv[1]); x0, x1, y0, y1 = map(int, sys.argv[2:6]) if len(sys.argv) > 5 else (54, 127, 0, 127)
c = p.chunks(p.SAVE); b, t, u = c["XBLD"], c["XTER"], c["XBIT"]
free = lambda x, y: 0 <= x < 128 and 0 <= y < 128 and b[y*128+x] in (0, 1, 2, 3, 4, 5) and t[y*128+x] < 16
out, used = [], set()
for y in range(y0, y1 - n + 2):
    for x in range(x0, x1 - n + 2):
        cells = [(x+i, y+j) for i in range(n) for j in range(n)]
        if all(free(*q) for q in cells) and not used & set(cells):
            out.append((x, y)); used |= set(cells)
print(" ".join("%d,%d" % q for q in out))
