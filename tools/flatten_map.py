"""Make every land tile of a SimCity 2000 city flat and treeless.

Usage: python3 -I tools/flatten_map.py IN.SC2 OUT.SC2

Land tiles all get the lowest land height (the river/lake level) and no slope.
Water tiles are left as they are, so the river stays usable for water pumps.
"""
import os
import struct
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "bot"))
import sc2parse  # noqa: E402

TREES = range(0x06, 0x0E)   # XBLD codes for trees and forest


def rle(data):
    """Encode bytes with the SC2 run-length scheme (inverse of sc2parse.unrle)."""
    out, i, lit = bytearray(), 0, bytearray()

    def flush():
        while lit:
            part = lit[:127]
            out.append(len(part))
            out.extend(part)
            del lit[:127]

    while i < len(data):
        j = i
        while j < len(data) and data[j] == data[i] and j - i < 128:
            j += 1
        if j - i >= 3:
            flush()
            out += bytes([127 + (j - i), data[i]])
            i = j
        else:
            lit.append(data[i])
            i += 1
    flush()
    return bytes(out)


def raw_chunks(path):
    raw = open(path, "rb").read()
    out, i = [], 12
    while i + 8 <= len(raw):
        name = raw[i:i + 4].decode("latin1")
        size = struct.unpack(">I", raw[i + 4:i + 8])[0]
        out.append((name, raw[i + 8:i + 8 + size]))
        i += 8 + size
    return out


def main(src, dst):
    c = sc2parse.chunks(src)
    alt = [int.from_bytes(c["ALTM"][2 * i:2 * i + 2], "big") for i in range(16384)]
    ter = bytearray(c["XTER"])
    bld = bytearray(c["XBLD"])
    land = [i for i in range(16384) if ter[i] < 0x10]
    level = min(alt[i] & 31 for i in land)
    for i in land:
        alt[i] = (alt[i] & ~31) | level
        ter[i] = 0
        if bld[i] in TREES:
            bld[i] = 0
    new = {"ALTM": b"".join(v.to_bytes(2, "big") for v in alt), "XTER": bytes(ter), "XBLD": bytes(bld)}
    body = bytearray(b"SCDH")
    for name, data in raw_chunks(src):
        if name in new:
            data = new[name] if name == "ALTM" else rle(new[name])
        body += name.encode("latin1") + struct.pack(">I", len(data)) + data
    open(dst, "wb").write(b"FORM" + struct.pack(">I", len(body)) + body)
    print("land tiles", len(land), "level", level, "trees left",
          sum(1 for b in bld if b in TREES), "water tiles", 16384 - len(land))
    # sanity: re-read the output
    d = sc2parse.chunks(dst)
    assert d["XTER"] == bytes(ter) and d["XBLD"] == bytes(bld)
    print(Counter(d["XTER"]).most_common(3))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
