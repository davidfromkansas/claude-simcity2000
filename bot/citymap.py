"""Tile classes for a SimCity 2000 save, shared by audit.py, build.py and stall.py.

XBLD codes: 0x01-0x04 rubble, 0x05-0x0D trees/parks, 0x0E-0x1C power lines, 0x1D-0x2B roads,
0x43-0x46 road/power crossings, 0x70+ buildings, 0xC9-0xD2 power plants, 0xD3 fire station, 0xDC pump.
XZON low nibble: 1/2 light/dense homes, 3/4 shops, 5/6 factories.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse  # noqa: E402

N = 128
ZONES = {1: "light homes", 2: "dense homes", 3: "light shops", 4: "dense shops",
         5: "light factories", 6: "dense factories"}


def is_road(t):
    return 0x1D <= t <= 0x2B or 0x43 <= t <= 0x46


def is_rail(t):
    return 0x2C <= t <= 0x42 or 0x47 <= t <= 0x4A


def is_line(t):
    return 0x0E <= t <= 0x1C or 0x43 <= t <= 0x46


def is_park(t):
    return 0x05 <= t <= 0x0D


def is_rubble(t):
    return 0x01 <= t <= 0x04


def is_plant(t):
    return 0xC9 <= t <= 0xD2


def is_building(t):
    return t >= 0x70


def conducts(t):
    """Power flows through lines, crossings and any building (pumps and plants included)."""
    return is_line(t) or is_building(t)


def nbrs(x, y):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= x + dx < N and 0 <= y + dy < N:
            yield x + dx, y + dy


class City:
    def __init__(self, path=None):
        self.path = path or sc2parse.SAVE
        c = sc2parse.chunks(self.path)
        self.b, self.z, self.bit, self.u = c["XBLD"], c["XZON"], c["XBIT"], c["XUND"]
        self.val, self.crm, self.plt = c.get("XVAL", b""), c.get("XCRM", b""), c.get("XPLT", b"")
        self.misc = sc2parse.parse(self.path)

    def t(self, x, y):
        return self.b[y * N + x]

    def zone(self, x, y):
        return self.z[y * N + x] & 15

    def pipe(self, x, y):
        return self.u[y * N + x] != 0 or self.t(x, y) == 0xDC

    def powered(self, x, y):
        return bool(self.bit[y * N + x] & 0x40)

    def watered(self, x, y):
        return bool(self.bit[y * N + x] & 0x10)

    def half(self, arr, x, y):
        return arr[(y // 2) * 64 + x // 2] if arr else 0

    def land_value(self, x, y):
        return self.half(self.val, x, y)

    def tiles(self):
        for y in range(N):
            for x in range(N):
                yield x, y

    def flood(self, seeds, ok):
        seen, todo = set(seeds), list(seeds)
        while todo:
            x, y = todo.pop()
            for p in nbrs(x, y):
                if p not in seen and ok(*p):
                    seen.add(p)
                    todo.append(p)
        return seen

    def power_reach(self):
        """Tiles power can reach from the plants, tracing lines and buildings like the game does.
        Empty zones and parks do NOT carry power."""
        seeds = [(x, y) for x, y in self.tiles() if is_plant(self.t(x, y))]
        return self.flood(seeds, lambda x, y: conducts(self.t(x, y)))

    def zone_regions(self):
        """Connected areas of one zone type (4-neighbour)."""
        seen, out = set(), []
        for x, y in self.tiles():
            k = self.zone(x, y)
            if 1 <= k <= 6 and (x, y) not in seen:
                reg = self.flood([(x, y)], lambda a, b, k=k: self.zone(a, b) == k)
                seen |= reg
                out.append((k, reg))
        return out
