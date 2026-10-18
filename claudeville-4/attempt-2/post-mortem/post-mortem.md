# Claudeville 4 · Attempt 2 post-mortem

**Result: failed.** Peak **97,090** people (Nov 2038), against a goal of 200,000 by Jan 2050.
The game ended in **January 2039**: cash reached -$102,953 and the mayor was thrown out.
That is better than attempt 1 (87,090, ended Jan 2031) and close to Claudeville 3's winner (107,460).

| Date | People | Loans | Notes |
|---|---|---|---|
| Jul 2002 | 4,330 | 3 | Ahead of attempt 1 (3,430) |
| Jul 2006 | 15,050 | 4 | Seaport, east job strip, district 5 |
| Jul 2008 | 20,780 | 9 | River crossed (two years later than attempt 1, on half the loans) |
| Jul 2010 | 25,630 | 10 | Airport on bare land 17 tiles from any district, with its own fire station |
| Dec 2014 | 46,780 | 17 | Ahead of pace; 16 fire stations |
| Dec 2016 | 59,420 | 19 | Budget only ~$2.5k a year short |
| Jan 2021 | 70,380 | 22 | Two more neighbour road links |
| Jul 2025 | 87,520 | 29 | Past attempt 1's peak; second rail link |
| Nov 2029 | 95,530 | 30 | All demand negative, 10% jobless, cash -$12.7k |
| Nov 2031 | 95,620 | 30 | Growth stalls; taxes raised to 10-11% |
| Nov 2033 | 80,850 | 30 | The tax rise backfired; taxes back to 8/7/8 |
| Sep 2036 | 91,670 | 30 | A monster wrecked the coal plants by the seaport |
| Nov 2038 | 97,090 | 30 | Peak; cash -$93k |
| Jan 2039 | - | 30 | Cash -$102,953: game over |

## What worked
- **Fire cover.** `firegrid.py` put a station every ~14 tiles, 28 in all. There was not one great fire, against two in attempt 1.
- **The isolated airport.** It sat on bare land with its own station; no crash spread into the city.
- **The new audit checks caught attempt 1's slow leaks at once:**
  - pipe networks that never reached a pump;
  - a coal plant with no line into the grid;
  - shop cells cut off from power by the airport road.
- **Fewer loans for the same size:** 30 loans for 97,000 people, against 48 for 87,000 in attempt 1.

## Control failures vs strategy failures

### Control failures
1. **`firegrid.py` put stations on land that later plans needed:**
   - the seaport-2 road and part of its zone;
   - a road junction in the west factory block;
   - the coal-plant lot east of district 3.

   *Fixed:* `--avoid plan1,plan2` keeps those tiles free. It must be used every time, and I forgot it once (2023).
2. **A stray calibration test road again sat on the zoo site (112,59).** The fix from attempt 1 only checks the most recent test road.
   *Fixed:* the new road-network check reports lone road tiles as strays.
3. **The seaport-2 road was left unconnected.** A plan reused from Claudeville 3 assumed roads from another plan. `audit.py` caught neither this nor the cut-off east link road; I found both by reading maps.
   *Fixed after the attempt:* `audit.py` now FAILs any road piece not joined to the main network.
   Run on the final save, it found the **whole south-east district (116 road tiles, x109-125 y98-125) cut off from the
   rest of the city** for the entire game. That likely hurt the shops and jobs there, and every check missed it.
4. **The game crashed to DOS** while the tax controller worked the budget window (Nov 2038). There is no known cause yet.
   Reloading the last save was not a disaster reload.
5. **`pkill -f` killed my own shell twice more.**
   *Rule (again):* kill by PID taken from `ps`, never by pattern.

### Strategy failures
1. **Money set the ceiling, not land.**
   - Thirty loans cost ~$15k a year; property tax brought $7-9k at 87-97,000 people.
   - Claudeville 3's winner had the same pattern (33 loans, ~$12k tax at 105,000) and only lasted because its deadline came first.
   - Under this game's rules (50-bond cap, game over near -$100,000), that shape of city cannot reach 200,000.
2. **The caps were not lifted when demand turned negative (2029).**
   - Shop demand sat near -1,500 for ten years with the smallest airport (24 tiles).
   - Factories ran past the audit's trade capacity (34,000 workers for ~3 trade units).
   - Unemployment was 8-22%.

   A bigger airport and another seaport may have been the missing jobs.
3. **Raising taxes on a stalled city backfired.** At 10-11%, 15,000 people left within two years and income fell anyway.
4. **Taxes were too low earlier, while demand was strong.** The controller let homes fall to 6-7% for long stretches.

## What changes next time (attempt 3)
- **Income per person, not just people:**
  - Research how SimCity 2000 sets property tax (land value per developed tile) and raise land value: parks, water, police, less pollution.
  - Keep taxes at 9-10% from the start while demand is positive.
- **Lift the caps in time:** a larger airport by ~40,000; a seaport or rail link per ~10,000 factory workers; recreation ahead of every ~15,000.
- **A hard loan budget tied to income.** Take a new loan only while yearly tax covers the bond payments plus ~$2k.
- **Controller:**
  - Run `firegrid.py --avoid` with every later plan.
  - The road-network check (done) runs on every step through `play.sh`.
