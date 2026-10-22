# Claudeville 4 · Attempt 5 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

## What four attempts show
- **Fire wrecked three of four cities** (attempts 1, 3, 4). The one city without a great fire (attempt 2) got furthest: 97,090.
- **Money ran out in all four** (2031-2039). Every fire rebuild cost loans that never paid back.
- **The airport works now**: a power line through the zone (attempt 4, developed in ~7 months).

## Plan: survive first
1. **No tree parks.** Every plan builds without parks (`"noparks": true` in run.json). Parks were fuel next to every home.
2. **Rubble is fuel.** Bulldoze burned or abandoned rubble promptly whenever cash allows.
3. **Every run stops on new rubble** (`play.sh` and the new `runout.sh`). Then: pause, find the fire, and clear a
   firebreak 2+ tiles wide down to bare land around it, while it is small.
4. **Keep ~$5,000 in hand from 20,000 people** for firebreaks. The loan guard keeps the 2050 projection above -$80k.
5. **Airport far from homes**: the empty north-east corner (about x116-121, y0-3, 15+ rows from any district), with a
   line THROUGH it and its own fire station. Built at ~12,000 people.
6. **Coal plants spread out**, each with a fire station beside it.
7. Same build order as attempt 4 otherwise (it was on pace until the 2017 fire): `seq.sh`, `audit.py` after each step,
   road links on all four edges by 20,000, taxes 10/9/9 while demand is high.
