"""Tree plan (after the land-value research, attempt 19): put small parks inside home blocks.

Land value is summed per 4x4 block: each tree/small-park tile adds +20 (water +12, empty +4, buildings 0).
Dense homes need land value 32 / 96 / 192 to grow into small 2x2 / large 2x2 / 3x3 towers (~140 / ~200 / ~700
people vs ~19 for a 1x1). This writes a build plan that places PER park tiles in every 4x4 block that holds
mostly home zone, on EMPTY home tiles nearest the block centre (never on buildings, roads or lines).

usage: python3 -I treeplan.py OUT.plan [PER] [X0 X1 Y0 Y1]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse as p  # noqa: E402

N = 128


def main():
    out = sys.argv[1]
    per = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    x0, x1, y0, y1 = map(int, sys.argv[3:7]) if len(sys.argv) > 6 else (0, N - 1, 0, N - 1)
    c = p.chunks(p.SAVE)
    b, z = c["XBLD"], c["XZON"]
    lines = ["# trees inside home blocks (+20 land value per tile per 4x4 block): %d per block" % per]
    n = 0
    for by in range(y0 // 4, y1 // 4 + 1):
        for bx in range(x0 // 4, x1 // 4 + 1):
            tiles = [(x, y) for x in range(bx * 4, bx * 4 + 4) for y in range(by * 4, by * 4 + 4)
                     if x0 <= x <= x1 and y0 <= y <= y1]
            homes = [(x, y) for x, y in tiles if (z[y * N + x] & 15) in (1, 2)]
            if len(homes) < 8:
                continue
            have = sum(1 for x, y in tiles if 0x05 <= b[y * N + x] <= 0x0D)
            free = [(x, y) for x, y in homes if b[y * N + x] == 0]
            cx, cy = bx * 4 + 1.5, by * 4 + 1.5
            free.sort(key=lambda t: (t[0] - cx) ** 2 + (t[1] - cy) ** 2)
            for x, y in free[:max(0, per - have)]:
                lines.append("park %d %d %d %d" % (x, y, x, y))
                n += 1
    open(out, "w").write("\n".join(lines) + "\n")
    print("treeplan: %d park tiles (~$%d) -> %s" % (n, n * 20, out))


if __name__ == "__main__":
    main()
