# Claudeville 3 · Attempt 1 post-mortem

**Result: missed.** Ended early in January 2022 (game year 22 of 50) with **9,190 people** and four
$10,000 loans. The straight-line pace to 100,000 needed about 44,000 by then. With $40,000 of debt
and a layout that fought against growth, 100,000 by 2050 was out of reach, so the attempt was
stopped to restart with a better plan.

| Year | People | Cash | Loans | Unemployed | Abandoned |
|---|---|---|---|---|---|
| 2000 | 0 | $10,000 | 0 | – | 0 |
| 2005 | 640 | $1,946 | 0 | 38% | 45 |
| 2010 | 3,120 | $5,909 | 1 | 28% | 144 |
| 2012 | 5,310 | $2,918 | 1 | 12% | 84 |
| 2015 | 6,070 | $2,014 | 1 | 19% | 160 |
| 2018 | 9,050 | $7,144 | 3 | 17% | 193 |
| 2021 | 6,800 | $8,196 | 4 | 45% | 469 |
| 2022 | 9,190 | $5,642 | 4 | 32% | 409 |

## What happened, phase by phase

**2000–2002: a dead start.** A full starter town was built on day one (avenue, four streets, homes,
shops, factories, coal plant, pumps), but only 30 people lived there after two years. Empty zones in
SimCity 2000 do not carry electricity; only power lines and finished buildings do. Each zone row was
powered only along one edge. Power lines through the zones fixed it, and the water pumps also had
no power.

**2003–2008: slow climb, no money.** Growth started, but tax income was tiny (about $57 a year at
1,400 people), so every expansion waited. Shops were over-built and factories were short. Without a
road link to a neighbor city, shop and factory demand stayed negative until 2005.

**2008–2011: first loan, first real fix.** A $10,000 bond paid for more homes, a factory district and
river pumps. Growth was still only 18–28% a year until Claude noticed that the only north–south road
was the main avenue on the west edge: the far east blocks were about 60 road tiles from jobs. Two
connector roads gave the best year of the game (+44%, unemployment 28% → 12%).

**2012–2015: the game ran unattended.** A bug in Claude's "is the game paused?" check (it looked at
the spot where the tool panel used to be) let the game run on its own for about three game years.
Water and power ran out unnoticed.

**2015–2018: borrowing to build out.** A second coal plant, a dense east district, more factories,
fire and police stations, a second neighbor link. Growth of 14–22% a year, but two more loans.

**2018–2021: collapse.** Population fell from 9,050 to 6,800 and unemployment rose to 45%. The
newspaper reported a water shortage ("Claudeville 3 Drying Up!") that Claude's own water number had
hidden. Factory rows built 30+ road tiles from any homes never filled, even with factory demand maxed.

**2021–2022: the test that explained it.** Homes were zoned right next to the empty factory rows.
Within one year the factory rows filled, population jumped 35% and unemployment fell from 45% to 32%.

## Top causes

1. **Homes were far from jobs.** The layout put homes in the north, shops in the middle and factories
   in the south, 20 to 60 road tiles apart, with only one or two north–south roads. In SimCity 2000 a
   trip that is too long fails, so people stay jobless and factories stay empty at the same time.
   *Evidence:* connector roads gave +44% in 2011; factory rows y64–69 stayed empty for 4 years with
   factory demand maxed, then filled within a year once homes were placed next to them.
2. **Empty zones don't carry power.** Two lost years at the start. *Evidence:* in 2001 only zone
   tiles touching a power line were marked powered in the save file.
3. **Wrong water number.** Claude counted buildings on pipes (always about 95–99%), but the game's
   own water graph showed supply at 0–19% of need in 2018. *Evidence:* newspaper headline, game graph.
4. **No money early, then too much debt.** Medium income is very small until the city is big. Loans
   came late (2008), one at a time, and were spent on spread-out districts that did not grow.
5. **Unattended running.** The broken pause check let three years pass with no health checks.

## What changes next time

- **Compact, mixed layout from day one:** narrow bands of homes, shops and factories next to each
  other (homes never more than ~10 road tiles from jobs), with a cross street every 8–10 tiles.
  Grow the city as a tight block outward, never as far-apart districts.
- **Power lines across every zone band** every 4–6 tiles, and to every pump.
- **Several neighbor links early,** placed near the factories.
- **Water by the game's own graph** (save file graph `water_pct`), not by pipes; read the newspaper
  headline every January; add pumps right on the water's edge before the graph drops.
- **Borrow early and on purpose:** one $10,000 bond in year one to build the compact starter city
  quickly, since growth compounds. Keep taxes low (about 4–5%) while small.
- **Never leave the game unattended:** the pause check now reads the panel's real position; after
  every run, check the date moved by the expected amount.

Next: [attempt 2 strategy](../claudeville-3/attempt-2/strategy.md)
