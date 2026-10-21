# Claudeville 4 · Attempt 10 strategy (from claudeville-4/reflection.md)

Goal: 200,000 by Jan 2050, same map, Medium, disasters on.

## What seven attempts show
- Attempt 6 is the best (120,770): fire rules, the loan rule, shore pumps, and the most people per loan (~4,400).
- Attempt 7 used the same rules with more aggressive land use and went broke (~2,900 people per loan); its control
  failures are now guarded (cash check, edge guard, strip generator fixes, people-per-loan floor in the loan guard).

## Plan: replay attempt 6, tighter
1. **Attempt 6's build order and timing**, plan by plan (its plans are in bot/plans: a20-day1, a20-2003, a19-2002,
   a19-2004, zoo, a19-pumps-s + c4a6-pumps-power, a19-2006, c4a6-airport, c4a6-east-homes, a20-district5,
   c4a5-stadium, c4a6-fire1, c4a6-coal-e, c4a5-westblock (c4a7-westblock), c4a5-south, c4a5-se, links, seaport 2,
   pumps-mid, zoo 2, south bands, coal-s, c4a6-west (2015), west 2-5, south-west grids, marina, zoo 3, east side ...).
2. **Every loan through the guard** (now also refuses under 3,000 people per loan from 30,000 people).
3. **Taxes steady at 8-9% from 30,000 people**; cut only when unemployment passes 8%.
4. Plans attempt 6 put in the far corners (c4a6-coal-sw2, c4a6-coal-nw2, c4a6-west-edge) are replaced by inland sites.
5. Pumps on shore tiles only.
6. Keep fire rules, keep ~$3-5k cash from 20,000 people.

## Attempt 9 additions (after attempt 8)
- Attempt 8 followed this plan and was ahead of attempt 6 until a fire in Nov 2038 that I let run unwatched.
- **Every disaster: run `bot/disaster.sh`** (watched 10-second bursts; it stops when the fire grows) and cut a tight
  firebreak ring around the real burning cluster.
- **Taxes held at 8%** (controller 7-9); attempt 8's 2022-24 recession followed a drift to 9-10%.
- After any restart use `bot/load.sh` only.

## Attempt 10 additions (after attempt 9: pre-fire 94,400 in 2028, 97,880 at 2050)
- Attempt 9 followed this plan and led every earlier attempt until a 2028 alien-ship great fire.
- **Every disaster or fire: pause, Emergency -> Dispatch Firefighters** (`sc tool 68 58 135 81`, click each flame
  cluster; one unit per fire station) **and re-dispatch after each burst**. Then `bot/disaster.sh` (watched bursts,
  whole-map rubble check). Firebreaks only where trucks cannot reach.
- **One fire station per ~6,000 people from the start** (firegrid.py every January), plants with their own station.
- **Never build at the north map edge (y < 12)** until autocal handles views that cannot centre; build.py's per-step
  landing check stops a plan whose clicks land off.
- After a fire: rebuild roads/lines straight onto rubble (no bulldozing), then `powerfix.py` for dark districts.
- Late loans (after ~2038) pay back in cash by 2050; take them before cash nears -$80k.
