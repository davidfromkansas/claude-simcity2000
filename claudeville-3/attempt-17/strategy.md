# Attempt 17 strategy (from the reflection on attempts 1-16)

Goal: 100,000 people by Jan 2050. Same flat map, Medium, disasters on, loans allowed.

## The idea: attempt 16 with enough jobs and some land value
Attempt 16 broke the ~20,000 wall (24,870) by putting factories only next to homes, then ran out of jobs
(unemployment 14-20% with hundreds of empty dense homes) and money (nine loans, homes taxed at 4%).

## Schedule (attempt 16's sequence)
`a15-day1` (#1) -> `a17-2003` (job-heavier blocks 3+4, police; #2) + `a12-power1` -> `a12-2003b` (seaport
+ pumps; #3) -> `a15-east` + `a13-link2` -> `a17-district5` (job-heavier, police; #4) + coal -> `a14-zoo` +
`a14-district6` (#5) -> factory cells next to homes (`a11-factories2`, `a16-mix1`), `a16-north`, airport at
~20,000.

## Rules
1. Factories only next to homes (`trips.py`); job land leads: aim for unemployment under 8%.
2. Homes taxed 6-7% (controller floor 6), shops/factories up to 7%.
3. Police in each district (crime -> land value); plants and factories away from home cells where possible.
4. Capacity ahead; every build checked before the clock runs; loans for land and capacity, up to ~9.
