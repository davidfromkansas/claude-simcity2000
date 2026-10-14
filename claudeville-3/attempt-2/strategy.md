# Attempt 2 strategy (written before play, from the attempt 1 post-mortem)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.

## The big change: homes close to jobs
Attempt 1 put homes, shops and factories in far-apart districts. Commutes were too long, so people
stayed jobless while factories stood empty. This time the city is one compact block of thin bands,
and every home band touches a job band.

```
 y=20 ── street ───────────────────────────────
 y21-26   HOMES
 y=27 ── street
 y28-33   SHOPS        (jobs, and a buffer from factory smoke)
 y=34 ── street
 y35-40   FACTORIES
 y=41 ── street
 y42-47   SHOPS
 y=48 ── street
 y49-54   HOMES
 y=55 ── street   ... then the pattern repeats: HOMES, SHOPS, FACTORIES, SHOPS, HOMES
```
- Bands are 6 rows (3 rows face each street). Streets run east–west from the main avenue x=76.
- **Cross streets every 10 tiles** (x=86, 96, 106 ...) so no trip has to detour.
- **Power lines across every band** every 10 tiles (x=81, 91, 101 ...), because empty zones don't carry power.
- Grow by adding the next 5-band block south (and later east), never a far-away district.

## Day one (Jan 2000)
- Take one $10,000 bond right away (growth compounds; attempt 1 waited 8 years).
- Main avenue x=76 to the north edge + neighbor link. Coal plant next to the factory band.
- First block: streets y=20–55, x=77–105. Zone homes and factories fully, shops partly
  (shop demand starts low).
- 15 pumps right on the river's edge (x=71–73), pipes under every band. Tax 4%.

## Every January
- Health check from the save file: population, cash, **the game's own water and power graphs**,
  unemployment, abandoned buildings, jammed roads, newspaper headline.
- Fix within the year. Add the next block before the current one fills.
- A second and third neighbor link (east edge, near factories) as soon as cash allows.
- Fire station early (disasters on), then police, schools, hospital as the budget allows.
- Later: dense zoning for homes and shops where land value is high; rail or subway if roads jam.

## Loans
Use bonds whenever a ready expansion is waiting for money, but keep yearly bond payments below about
half of tax income after year 10.

## Safety
- After every run, confirm the game is paused and the date moved as expected.
- Dismiss dialogs with Escape or by clicking the dialog itself, never the map.
