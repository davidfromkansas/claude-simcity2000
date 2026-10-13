"""Read a SimCity 2000 .SC2 save file and return city metrics as a dict.

Format notes: https://github.com/dfloer/SC2k-docs/blob/master/sc2%20file%20spec.md
"""
import json
import struct
import sys

GRAPHS = ["city_size", "residents", "commerce", "industry", "traffic", "pollution",
          "value", "crime", "power_pct", "water_pct", "health", "education",
          "unemployment", "gnp", "nation_pop", "fed_rate"]
SERVICES = {"police": 0x998, "fire": 0xA04, "health": 0xA70, "schools": 0xADC,
            "colleges": 0xB48, "roads": 0xBB4, "highways": 0xC20, "bridges": 0xC8C,
            "rail": 0xCF8, "subway": 0xD64, "tunnel": 0xDD0}
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
    name = c.get("CNAM", b"\x00")[1:].split(b"\x00")[0].decode("latin1")
    return {
        "city": name,
        "year": year, "month": MONTHS[month], "days": days,
        "date": "%s %d" % (MONTHS[month], year),
        "founded": g(0x0C),
        "difficulty": g(0x1C),
        "money": g(0x14),
        "bonds": g(0x930),          # bonds currently floated
        "population": g(0x102C) + g(0x1020),
        "arco_population": g(0x1020),
        "res_tiles": g(0x5F8), "com_tiles": g(0x600), "ind_tiles": g(0x608),
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
        "graphs": graphs,
    }


if __name__ == "__main__":
    print(json.dumps(parse(sys.argv[1]), indent=1))
