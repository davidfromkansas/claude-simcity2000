# Attempt 19 strategy (from the reflection on attempts 1-18)

Attempts 17 and 18 both stopped near 29,000 with the same plan: dense homes outran jobs (unemployment
11-14% for a decade, 200-300 empty dense home tiles) while every new block of job land needed a loan.
Attempt 14, with light homes, kept unemployment at 4-7%.

## Plan
Attempt 17's schedule and mixed layout (factories only next to homes, police, airport, stadium) with:
1. **Light homes** everywhere (plans `a19-*`, the original light `a11-day1`): fewer residents per block, so
   jobs keep up and fewer homes stand empty.
2. **More factory cells** (district 6 gets one more).
3. **Second seaport at ~20,000** (`a15-seaport2`) - planned in 18 but never built.
4. **Population reminders** in `pace.json` (ordinances at 10,000, zoo at 13,000, homes 7% at 15,000,
   airport + seaport at 20,000, stadium at 25,000): the play loop stops at each until it is done.
5. Everything else as attempt 17 (trip checks, gated builds, loans for land and capacity).
