# Attempt 19 strategy (from the reflection on attempts 1-18, revised at the restart on Jan 2000)

Attempts 17 and 18 both stopped near 29,000. Dense homes outran jobs: unemployment sat at 11-14% for a decade,
so home demand stayed negative and no building upgraded. Their home blocks had no trees, so land value
stayed near 20, far below the 96 and 192 that 2x2 and 3x3 buildings need. Light homes (attempts 14 and 19's
first draft) cap out near 23,000. Reaching 100,000 needs big buildings.

## Plan
1. **Dense homes with a 2x2 park in the middle of every home cell**: the `a20-*` plans, and `a20-day1` for day one.
   This is the cheapest land value (+20 per tree tile per 4x4 block).
2. **Jobs first.** The play loop now stops on JOBS (unemployment of 9% or more while home demand is negative).
   The answer is always more job land (factories by the port and rail, shops between homes), never more homes.
3. Attempt 17's schedule and mixed layout: factories only next to homes, police, airport, stadium, and a
   second seaport at about 20,000.
4. **Population reminders** in `pace.json`: ordinances, zoo, airport and seaport, stadium.
5. **Play to Jan 2050.** Microwave power once it appears (2028 on this map), big parks for the home cap, and a
   waterfront district later.

The first day-one build of this attempt was placed at half scale because the zoom-in had not taken
(control failure). No game time had passed, so the attempt was restarted from the base map.
`autocal.sh` now measures the zoom with a second tile, and `begin_attempt.sh` deletes an old save of the
same name first, because its "Overwrite?" prompt threw off every later click.
