"""powerfix.py OUT.plan : plan the shortest power lines from the powered grid to every dark zone area.

Claudeville 4 attempt 9 (Oct 2028): after the great fire most east-bank blocks had zones but no buildings, and empty
zones do not carry power, so whole districts that used to be fed through their buildings went dark (130+ audit FAILs).
For each dark area (audit's zone regions with no powered tile in or next to them) this runs a breadth-first search from
the powered tiles over empty land, rubble and empty zone tiles, crossing a road only straight through one road tile
(junctions cannot take a line), and writes the path as line steps. Paths found earlier count as powered for later areas.
"""
import os
import sys
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from citymap import City, is_road, is_rubble, conducts, nbrs  # noqa: E402
import sc2parse as p  # noqa: E402

N = 128


def main(out):
    c = City()
    bit = p.chunks(p.SAVE)["XBIT"]
    reach = set(c.power_reach())
    water = lambda x, y: bit[y * N + x] & 4
    free = lambda x, y: (c.t(x, y) == 0 or is_rubble(c.t(x, y))) and not water(x, y)
    road = lambda x, y: is_road(c.t(x, y)) and not water(x, y) and not conducts(c.t(x, y))
    # existing lines and buildings cut off from the plants carry power once joined: pass through them for free
    cond = lambda x, y: conducts(c.t(x, y))
    lines, dark = [], 0
    targets = list(c.zone_regions()) + [("pump", [q]) for q in c.tiles() if c.t(*q) == 0xDC]   # pumps need power too
    for k, reg in targets:
        if any(q in reach or any(r in reach for r in nbrs(*q)) for q in reg):
            continue
        dark += 1
        goal = {r for q in reg for r in list(nbrs(*q)) + [q]}
        prev, dq = {}, deque()
        for q in reach:
            prev[q] = None
            dq.append(q)
        end = None
        while dq and end is None:
            x, y = dq.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in prev:
                    continue
                if road(nx, ny):
                    # straight through one road tile: the tile beyond must be free, and the road must not continue
                    # along the move direction (that would make the line run along the road)
                    bx, by = nx + dx, ny + dy
                    if not (0 <= bx < N and 0 <= by < N) or not (free(bx, by) or cond(bx, by)) or (bx, by) in prev:
                        continue
                    if (x, y) not in reach and road(x, y):
                        continue
                    prev[(nx, ny)] = (x, y)
                    prev[(bx, by)] = (nx, ny)
                    if (bx, by) in goal:
                        end = (bx, by)
                        break
                    dq.append((bx, by))
                    continue
                if not free(nx, ny) and not cond(nx, ny):
                    continue
                prev[(nx, ny)] = (x, y)
                if (nx, ny) in goal:
                    end = (nx, ny)
                    break
                dq.append((nx, ny))
        if end is None:
            print("powerfix: no path to %s area at %s" % (k, min(reg)))
            continue
        path, q = [], end
        while q is not None and q not in reach:
            if free(*q) or road(*q):
                path.append(q)
            reach.add(q)
            q = prev[q]
        lines += path
        reach |= set(path) | c.flood(list(reach & set(prev)), lambda x, y: cond(x, y) or (x, y) in reach)
    lines = sorted(set(lines))
    steps = ["# powerfix.py: %d line tiles for %d dark zone areas" % (len(lines), dark)]
    steps += ["line %d %d %d %d" % (x, y, x, y) for x, y in lines]
    open(out, "w").write("\n".join(steps) + "\n")
    print("powerfix: %d dark areas, %d line tiles (~$%d) -> %s" % (dark, len(lines), 5 * len(lines), out))


main(sys.argv[1])
