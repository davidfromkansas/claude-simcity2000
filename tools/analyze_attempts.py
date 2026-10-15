"""Compare Claudeville 3 attempts from their dashboard metrics and final saves.

usage: python3 -I tools/analyze_attempts.py > claudeville-3/research/our-data.md
Prints Markdown: a yearly table per attempt (people, people per home tile, land value, loans, cash,
demand) and, from each final save, how home tiles split between light and dense buildings.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "bot"))
import sc2parse  # noqa: E402

C3 = os.path.join(ROOT, "claudeville-3")


def yearly(rows):
    out = {}
    for r in rows:
        y = r.get("year")
        if y and (y not in out or r["gy"] > out[y]["gy"]):
            out[y] = r
    return [out[y] for y in sorted(out)]


def save_mix(path):
    c = sc2parse.chunks(path)
    b, z = c["XBLD"], c["XZON"]
    light = dense = empty = 0
    for i in range(len(z)):
        k = z[i] & 15
        if k in (1, 2):
            if b[i] < 0x70:
                empty += 1
            elif k == 2:
                dense += 1
            else:
                light += 1
    return light, dense, empty


def main():
    print("# Our own data: Claudeville 3 attempts 1-7\n")
    print("People per home tile = population / developed home tiles. Land value is the save's average (0-255 scale).\n")
    for n in range(1, 8):
        p = os.path.join(C3, "attempt-%d" % n, "dashboard", "data", "metrics.json")
        if not os.path.exists(p):
            continue
        rows = yearly(json.load(open(p)))
        print("## Attempt %d\n" % n)
        print("| Year | People | Home tiles | People/home tile | Land value | Loans | Cash | Demand R/C/I |")
        print("|---|---|---|---|---|---|---|---|")
        for r in rows:
            rt = r.get("res_tiles") or 0
            ppt = "%.0f" % (r["population"] / rt) if rt else "-"
            print("| %d | %s | %d | %s | %s | %s | %s | %s/%s/%s |" % (
                r["year"], f"{r['population']:,}", rt, ppt, r.get("land_value"), r.get("bonds"),
                f"{r.get('money', 0):,}", r.get("dem_r"), r.get("dem_c"), r.get("dem_i")))
        s = os.path.join(ROOT, "saves", "C3A%d.SC2" % n)
        if os.path.exists(s):
            l, d, e = save_mix(s)
            print("\nFinal save home tiles: %d light built, %d dense built, %d empty.\n" % (l, d, e))
        else:
            print()


if __name__ == "__main__":
    main()
