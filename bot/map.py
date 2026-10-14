"""Print a tile map of an area from the current save.  usage: map.py X0 X1 Y0 Y1 [pipes]"""
import sys, struct, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p
x0, x1, y0, y1 = map(int, sys.argv[1:5]); pipes = len(sys.argv) > 5
c = p.chunks(p.SAVE); b, z, bt, u = c["XBLD"], c["XZON"], c["XBIT"], c["XUND"]
alt = struct.unpack(">16384H", c["ALTM"]); ter = c["XTER"]
print("    " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
for y in range(y0, y1 + 1):
    r = ""
    for x in range(x0, x1 + 1):
        i = y * 128 + x; t = b[i]; zz = z[i] & 15
        if pipes: r += "+" if u[i] else ("~" if bt[i] & 4 else "."); continue
        if bt[i] & 4 and not t: ch = "~"
        elif 0x1D <= t <= 0x2B: ch = "="
        elif 0x0E <= t <= 0x1C: ch = "|"
        elif 0x43 <= t <= 0x46: ch = "x"
        elif t == 0xDC: ch = "W"
        elif t in (0x8A, 0x8B): ch = "A"
        elif t >= 0xC0: ch = "P"
        elif zz: ch = "rRcCiI"[zz - 1] if t < 0x70 else "hHsSfF"[zz - 1]
        elif t: ch = "#"
        elif ter[i]: ch = "^"
        else: ch = "."
        r += ch
    print("%3d " % y + r)
