"""rebuild.py OUT.plan X0 Y0 X1 Y1 : after a disaster, write a plan that rebuilds the network inside a box.

Takes every road/rail/line/pipe/pump/plant/fire/police/link step from the plans this attempt has built
(run.json "built", in build order), keeps the steps that touch the box, and cuts straight steps that
cross water into their land pieces. Claudeville 4 attempt 1: the hand-made generator dropped the whole
cross-river line `line 21 68 59 68` because part of it was water, so its east-shore end was never rebuilt
and the west bank's north blocks went dark for months. Zones survive fires, so zone steps are not repeated.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sc2parse  # noqa: E402

BOT = os.path.dirname(os.path.abspath(__file__))
KEEP = {"link", "raillink", "rail", "road", "line", "pipe", "pump", "coal", "gas", "fire", "police"}
SKIP = ("firebreak", "stray", "rubtest", "rebuild", "no-airport")


def water_map():
    xt = sc2parse.chunks(sc2parse.SAVE)["XTER"]
    return lambda x, y: bool(xt[y * 128 + x] & 0xF0)


def main(out, x0, y0, x1, y1):
    run = json.load(open(os.path.join(BOT, "run.json")))
    plans = []
    for b in run.get("built", []):
        p = b["plan"]
        if p not in plans and not any(k in p for k in SKIP) and os.path.exists(os.path.join(BOT, "plans", p)):
            plans.append(p)
    wet = water_map()
    inbox = lambda x, y: x0 <= x <= x1 and y0 <= y <= y1
    lines = ["# rebuild of x%d-%d y%d-%d from the plans built so far (rebuild.py)" % (x0, x1, y0, y1)]
    for p in plans:
        for raw in open(os.path.join(BOT, "plans", p)):
            w = raw.split("#")[0].split()
            if not w or w[0] not in KEEP:
                continue
            nums = [int(v) for v in w[1:] if v.lstrip("-").isdigit()]
            if len(nums) == 4 and w[0] in ("road", "line", "pipe", "rail"):
                ax, ay, bx, by = nums
                if ax != bx and ay != by:
                    continue
                pts = [(x, y) for x in range(min(ax, bx), max(ax, bx) + 1) for y in range(min(ay, by), max(ay, by) + 1)]
                if not any(inbox(*q) for q in pts):
                    continue
                run_ = []
                for q in pts + [None]:            # split at water tiles: keep each land piece
                    if q is not None and not wet(*q):
                        run_.append(q)
                        continue
                    if run_ and any(inbox(*r) for r in run_):
                        lines.append("%s %d %d %d %d   # %s" % (w[0], *run_[0], *run_[-1], p))
                    run_ = []
            elif len(nums) >= 2 and inbox(nums[0], nums[1]):
                lines.append(" ".join(w) + "   # " + p)
    open(out, "w").write("\n".join(lines) + "\n")
    print("rebuild plan %s: %d steps from %d plans" % (out, len(lines) - 1, len(plans)))


if __name__ == "__main__":
    main(sys.argv[1], *map(int, sys.argv[2:6]))
