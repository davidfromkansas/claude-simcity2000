"""Power map: usage pmap.py X0 X1 Y0 Y1
P/u = powered/unpowered building, +/! = powered/unpowered power line, = road, W pump (w unpowered), . other"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p
x0, x1, y0, y1 = map(int, sys.argv[1:5])
c = p.chunks(p.SAVE); b, bt = c["XBLD"], c["XBIT"]
print("    " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
for y in range(y0, y1 + 1):
    r = ""
    for x in range(x0, x1 + 1):
        i = y * 128 + x; t = b[i]; on = bt[i] & 64
        if 0x0E <= t <= 0x1C or 0x43 <= t <= 0x46: r += "+" if on else "!"
        elif t == 0xDC: r += "W" if on else "w"
        elif 0x1D <= t <= 0x2B: r += "="
        elif t >= 0x70: r += "P" if on else "u"
        else: r += "."
    print("%3d " % y + r)
