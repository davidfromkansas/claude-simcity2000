"""Recreate attempt 5's mistakes in the current save (in memory) and check the audit catches each one.
usage: python3 -I test_audit.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from citymap import City, N
from audit import audit

def run(name, change):
    c = City(); c.b = bytearray(c.b); c.u = bytearray(c.u); change(c)
    fails = [t for l, t in audit(city=c) if l == "FAIL"]
    print("%-34s %s" % (name, "caught: " + fails[0] if fails else "MISSED"))
    return bool(fails)

def no_link(c):
    for x in range(N):
        for y in (0, N - 1):
            c.b[y * N + x] = c.b[x * N + y] = 0
def parks(c):   # parks between every power column and the home zones beside it
    for y in range(N):
        for x in range(N):
            if 0x0E <= c.b[y*N+x] <= 0x1C and y > 25: c.b[y*N+x] = 0x0D
def pipe_gap(c):  # cut the pipe next to every pump
    for y in range(N):
        for x in range(N):
            if c.b[y*N+x] == 0xDC:
                for dx in (1, 2):
                    if c.b[y*N+x+dx] != 0xDC: c.u[y*N+x+dx] = 0
ok = [run("no neighbor link", no_link), run("parks block power", parks), run("pumps cut off from pipes", pipe_gap)]
print("all caught" if all(ok) else "SOME MISSED"); sys.exit(0 if all(ok) else 1)
