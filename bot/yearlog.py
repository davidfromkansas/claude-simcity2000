"""Year-by-year journal for the dashboard.

Each entry covers one game year: the moves made that year, what happened by the next
January (numbers filled in from metrics.json), and what to watch next.

  python3 -I bot/yearlog.py add YEAR TONE "title" "happened" "watching" ["move" ...]
      TONE: good | setback | milestone | steady
  python3 -I bot/yearlog.py fill     # (re)compute the numbers for every entry
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import publish  # noqa: E402

PATH = os.path.join(publish.DATA, "yearly.json")
KEYS = ["date", "population", "money", "unemployment", "watered_pct", "powered_pct", "abandoned", "jammed", "bonds"]


def snapshot(rows, year):
    """First reading taken in a given game year (the January check)."""
    for r in rows:
        if r["year"] == year:
            return {k: r.get(k) for k in KEYS}
    return None


def fill(entries):
    rows = json.load(open(os.path.join(publish.DATA, "metrics.json")))
    for e in entries:
        e["start"] = snapshot(rows, e["year"])
        e["end"] = snapshot(rows, e["year"] + 1)
    return entries


def save(entries):
    entries.sort(key=lambda e: e["year"])
    json.dump(fill(entries), open(PATH, "w"), indent=1)


if __name__ == "__main__":
    entries = json.load(open(PATH)) if os.path.exists(PATH) else []
    if sys.argv[1] == "add":
        year, tone, title, happened, watching = sys.argv[2:7]
        entries = [e for e in entries if e["year"] != int(year)]
        entries.append({"year": int(year), "tone": tone, "title": title, "moves": sys.argv[7:],
                        "happened": happened, "watching": watching})
    save(entries)
    print(len(entries), "entries")
