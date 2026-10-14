"""Read a SimCity 2000 .SC2 save file and return city metrics as a dict.

Format notes: https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md
"""
import json
import os
import struct
import sys

GRAPHS = ["city_size", "residents", "commerce", "industry", "traffic", "pollution",
          "value", "crime", "power_pct", "water_pct", "health", "education",
          "unemployment", "gnp", "nation_pop", "fed_rate"]
SERVICES = {"police": 0x998, "fire": 0xA04, "health": 0xA70, "schools": 0xADC,
            "colleges": 0xB48, "roads": 0xBB4, "highways": 0xC20, "bridges": 0xC8C,
            "rail": 0xCF8, "subway": 0xD64, "tunnel": 0xDD0}
_RUN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run.json")
RUN = json.load(open(_RUN)) if os.path.exists(_RUN) else {"save": "/opt/sc2k/game/CLAUDE.SC2", "docs": "."}
SAVE = RUN["save"]   # the save file of the city being played now
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def unrle(data):
    out, i = bytearray(), 0
    while i < len(data):
        n = data[i]
        if n < 128:
            out += data[i + 1:i + 1 + n]
            i += 1 + n
        else:
            out += bytes([data[i + 1]]) * (n - 127)
            i += 2
    return bytes(out)


def chunks(path):
    raw = open(path, "rb").read()
    assert raw[:4] == b"FORM" and raw[8:12] == b"SCDH", "not a SimCity 2000 city"
    out, i = {}, 12
    while i + 8 <= len(raw):
        name = raw[i:i + 4].decode("latin1")
        size = struct.unpack(">I", raw[i + 4:i + 8])[0]
        body = raw[i + 8:i + 8 + size]
        out[name] = body if name in ("ALTM", "CNAM") else unrle(body)
        i += 8 + size
    return out


def ints(b):
    return list(struct.unpack(">%di" % (len(b) // 4), b[:len(b) // 4 * 4]))


def parse(path):
    c = chunks(path)
    m = ints(c["MISC"])
    g = lambda off: m[off // 4]
    days = g(0x10)
    year = g(0x0C) + days // 300
    month = min((days % 300) // 25, 11)
    xgrp = ints(c.get("XGRP", b""))
    graphs = {}
    for k, name in enumerate(GRAPHS):
        sec = xgrp[k * 52:(k + 1) * 52]
        graphs[name] = sec[:12] if sec else []   # monthly values, newest first
    services = {k: {"count": g(off), "funding": g(off + 4)} for k, off in SERVICES.items()}
    xval = c.get("XVAL", b"")
    xcrm = c.get("XCRM", b"")
    xplt = c.get("XPLT", b"")
    xtrf = c.get("XTRF", b"")
    avg = lambda b: round(sum(b) / len(b), 1) if b else 0
    zoned, dev = [0, 0, 0], [0, 0, 0]
    xz, xb = c.get("XZON", b""), c.get("XBLD", b"")
    for i in range(len(xz)):
        zt = xz[i] & 15
        if 1 <= zt <= 6:
            k = (zt - 1) // 2          # 0 res, 1 com, 2 ind
            zoned[k] += 1
            if xb[i] >= 0x70:          # a building stands on the tile
                dev[k] += 1
    # City health: what actually stalled attempt 1 (water, power, abandonment, traffic jams).
    bits = c.get("XBIT", b"")
    blds = [i for i in range(len(xb)) if 0x70 <= xb[i] < 0xC0]
    nb = max(1, len(blds))
    health = {
        "buildings": len(blds),
        "watered_pct": round(100 * sum(1 for i in blds if bits[i] & 16) / nb),
        "powered_pct": round(100 * sum(1 for i in blds if bits[i] & 64) / nb),
        "abandoned": sum(1 for t in xb if t in (0x8A, 0x8B)),
        "jammed_road_tiles": sum(1 for v in c.get("XTRF", b"") if v >= 240),
    }
    name = c.get("CNAM", b"\x00")[1:].split(b"\x00")[0].decode("latin1")
    return {
        "city": name,
        "year": year, "month": MONTHS[month], "days": days,
        "date": "%s %d" % (MONTHS[month], year),
        "founded": g(0x0C),
        "difficulty": g(0x1C),
        "money": g(0x14),
        # 0x930 is the average bond interest rate (x1,000,000), not a count: 50000 after one 5% bond,
        # 45000 after a second at 4%. The count of $10,000 bonds is kept by hand in run.json "bonds".
        "bonds": RUN.get("bonds", 1) if g(0x930) else 0,
        "bond_raw": g(0x930),
        "population": g(0x102C) + g(0x1020),
        "arco_population": g(0x1020),
        # Developed tiles per zone type, counted from the zone + building maps.
        # (MISC 0x5F8.. turned out to count only dense residential, so it is not used.)
        "res_tiles": dev[0], "com_tiles": dev[1], "ind_tiles": dev[2],
        "zoned_tiles": {"res": zoned[0], "com": zoned[1], "ind": zoned[2]},
        "demand": {"res": g(0x718), "com": g(0x71C), "ind": g(0x720)},
        "tax": {"res": g(0x780), "com": g(0x7EC), "ind": g(0x858)},
        "taxed_pop": {"res": g(0x77C), "com": g(0x7E8), "ind": g(0x854)},
        "workforce_pct": g(0x44), "life_expectancy": g(0x48), "education_eq": g(0x4C),
        "crime_total": g(0x2C), "traffic": g(0x30), "pollution": g(0x34),
        "land_value_total": g(0x28), "city_value": g(0x24),
        "avg_land_value": avg(xval), "avg_crime": avg(xcrm),
        "avg_pollution": avg(xplt), "avg_traffic": avg(xtrf),
        "reward_level": g(0x20),
        "ordinances": g(0xFA0),
        "speed": g(0xFEC),
        "no_disasters": g(0x1000),
        "services": services,
        "health": health,
        "graphs": graphs,
    }


if __name__ == "__main__":
    print(json.dumps(parse(sys.argv[1] if len(sys.argv) > 1 else SAVE), indent=1))
