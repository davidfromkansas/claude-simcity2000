# Claude plays SimCity 2000

CURRENT CHALLENGE: Claudeville 3 — 100,000 people by Jan 2050, Medium, disasters on, loans allowed, same flat map
(saves/claudeville-3-base.SC2). Up to 20 attempts; post-mortem after each miss. Active attempt is in bot/run.json
(save, dashboard, recordings). Folder: claudeville-3/attempt-N/. Overview list: claudeville-3/attempts.json.
(The goal text below is from challenges 1-2.)

Goal: 5,000 residents within 30 game years (founded Jan 2000 → by 2030), then 3 consecutive
years of positive budget with zero bonds. NEVER issue a bond.

## If the container restarted
1. `apt-get install -y dosbox xdotool imagemagick` and re-download the game to /opt/sc2k/game
   (https://archive.org/download/SimCity-2/simcity2000.zip). Restore the save from `saves/CLAUDE.SC2`.
2. `bot/start.sh`, then `bot/record.sh &` and `python3 -I bot/publish.py loop &`.
3. In game: File > Load City > CLAUDE.SC2.

## Each turn
1. `bot/sc snap` and look at /tmp/sc/now.png. Keep the game paused (Alt+P) while thinking.
2. Act with `bot/sc click/drag/menu/key`. Menus need `sc menu MX MY IX IY` (hold-and-release).
3. `bot/sc save` after every turn (prints date/pop/cash/bonds) and copy the save to `saves/`.
4. `bot/sc log <type> "<what and why>"` for every decision (types: build, zone, budget, strategy, fix, milestone).
5. Update `city-notes.md` with layout and strategy.
6. Every January (the yearly check), write that year's journal entry for the dashboard's "Year by year" section:
   `python3 -I bot/yearlog.py add YEAR TONE "title" "what happened" "watching next" "move 1" "move 2" ...`
   TONE is good | setback | milestone | steady. Leave out moves for a year with no changes and say why in "what happened".
   Numbers (population, cash, unemployment, water, power, abandoned, loans) are filled in from the save data automatically.

## Lessons learned (important)
- Alt-key shortcuts do NOT work. Use menus: `sc menu 67 7 75 55` (Llama), `75 71` (Cheetah), `75 23` (Pause), then `sc key Escape`.
- Toolbar buttons with options need a long press: `sc tool BX BY IX IY` (e.g. power lines `22 82 55 90`, gas plant via `22 82 60 105` then click 199 255;
  road `22 105 55 113`; light res `22 128 75 135`; light com `47 128 100 135`; light ind `68 128 120 135`; water pump `47 82 85 105`; pipes `47 82 85 90`).
- Query a tile: shift+click.
- Use `bot/tile.py` for tile->screen. Calibrate after every scroll/zoom by placing one road tile, saving, and reading its (x,y) from the save
  (`python3 -I tile.py cal X Y SX SY STEP`, STEP 8 at zoom 3). +x goes down-left, +y goes down-right on screen.
- ALWAYS verify a build by saving and printing a tile map from the save (XBLD/XZON); screenshots are misleading.
- Zones must touch the road directly. Never put power lines between a zone and its road. Power lines must touch side-by-side (diagonal does not connect).
- A budget window pops up every January and blocks clicks; close it with `sc click 457 123`.
- Clicking to dismiss dialogs can place a tile with the current tool: dismiss the "Game Saved" box by clicking the box itself (320 228).

## Lessons from Claudeville 3
- EMPTY ZONES DO NOT CARRY POWER. Only power lines and built buildings do. Run power lines across zone bands every ~4-8 tiles.
- Water pumps need power too.
- Without a neighbor road link, commercial/industrial demand stays negative. Build it early ($1,000, prompt appears when a road reaches the map edge; the edge tile needs a drag from the tile next to it).
- Tool info panel can block clicks; it was dragged to the top right (382-555, 32-56). Keep targets out of it.
- `bot/center.sh X Y` scrolls to any tile; then verify with `bot/calib.sh SX SY 8` on empty land.
- `sc save` now only clicks the 'Game Saved' box if it is really there (stray clicks used to place roads).

## Current layout (city refounded Jan 2000 on a flat map)
- Gas plant x57-60 y7-10. Main road y=11 x60-100. Side road x=80 y3-10.
- Zones rows y8-10 and y12-14: industry x62-69, commercial x70-79, residential x81-99.
- Power lines y=7 and y=15 (x61-99), x=61 y7-15.

## Screen map (640x480)
Menu bar y=7: File 25, Speed 67, Options 120, Disasters 185, Windows 252, Newspaper 320.
Toolbar is the left column (x 10-80).
- The save's graphs `water_pct` and `power_pct` are SPARE capacity (%), not coverage. Near 0 = shortage
  (attempt 1's 2018 water collapse showed 0-19%). Keep both above ~25%. `watered_pct`/`powered_pct`
  (buildings on pipes/lines) stay ~100% even during a shortage.
- Homes must be within ~10-15 road tiles of jobs. Use thin alternating bands (homes/shops/factories/shops/homes)
  with cross streets every 10 tiles. Far-apart districts fail (attempt 1).
- Options > Auto-Goto is stored in the save and was ON in the base map: turn it off after loading.
- Speed-ups agreed with the user (Oct 2026): DOSBox frameskip=3; build each block from one scripted plan and check the
  map from the save afterwards; render timelapses only while the game is paused. Keep checking the city every 3-4
  game months (do NOT skip to yearly checks) and keep the normal camera recalibration.
- `sc paused` looks for the green *PAUSED* label anywhere in the top strip, so the tool panel can sit anywhere there.
- Attempt 5 lessons: the neighbor link only exists if $1,000 was charged and a road tile sits ON the map edge (y=0);
  parks do not carry power, so never put them between a power line and a zone; bulldozer drags can destroy
  neighbouring buildings, so bulldoze tile by tile. If a zone with demand does not grow for 6 months, query tiles at once.

## Controller (built Oct 2026 after attempt 5) - use these, not hand-typed clicks
- `bot/build.py PLAN` builds from a plan file (road/line/pipe/zone/pump/park/coal/gas/fire/police/link/bulldoze/dezone),
  then checks EVERY planned tile in the save, re-places gaps tile by tile, checks the cash charged (link must cost $1,000),
  and reports + repairs any tile OUTSIDE the plan that changed. Bulldoze is tile by tile (2 clicks: rubble, then clear).
  Plans live in `bot/plans/*.plan`. A build is not done until it prints "BUILD: checked".
- `bot/audit.py` city check from the save (neighbor link, power reach through lines/buildings, pumps joined to pipes,
  road access, spare capacity). Any FAIL = fix before running the game. `bot/test_audit.py` proves it catches attempt 5's mistakes.
- `bot/stall.py` stall alarm: demand but no growth for 6 game months -> diagnosis of sample tiles.
- `bot/step.sh [secs]` = run ~3-4 months + save + health + audit + stall. Use it for every check step.

## Post-mortem rule (from the user)
Every post-mortem must split causes into CONTROL failures (the agent could not carry out its own plan: misplaced or
missing tiles, unnoticed broken links, accidents) and STRATEGY failures (the plan itself was wrong). Control failures
should not happen: call each one out plainly, and fix the controller (new check or tool) BEFORE the next attempt.
Only strategy lapses are acceptable reasons to fail.

## Research findings (Oct 2026, claudeville-3/research/README.md) - plan around these
- Demand caps: homes stall near 15,000 residents until stadium/zoo/marina (more = higher cap); factories need a RAIL or
  highway link off the map edge or a seaport (road link does not count); shops need road links and an airport (~20k+).
- Tax ~= 1.29 x population x rate per year (~$0.10/person at 7%). A $10k bond (~$400-600/yr) pays back only if it adds 5,500+ people.
- Dense homes 30-40 people/tile vs light 10-18. Buildings must reach the other zone types within ~33 road tiles (trips).
- Tools (lab-tested on our map): rail `47 105 85 113` (link prompt $1,500); seaport zone `68 105 100 112` ($150/tile, works on
  our river); airport `68 105 100 128`; zoo `68 155 100 196` ($3,000, 4x4); stadium `68 155 100 212` ($5,000, 4x4, then a
  "Pick a team" dialog: Football 212,212 then Done 440,187); marina `68 155 100 227` ($1,000, 3x3, must straddle the shore).
  All are `build.py` step kinds. Tile codes: rail 0x2D.., seaport zone 9, stadium 0xD7, zoo 0xDA, marina 0xF8.
- Recorder: `bot/record.sh` writes crash-safe fragmented MP4s; stop with `touch /tmp/sc/rec.stop; pkill -INT -f x11grab`.
- Official manual read in full (claudeville-3/research/manual-notes.md): start small and profitable, copy a compact
  module; homes ~= shops + factories (more factories while small); 6x6 squares between roads; power lines consume
  power; pumps on fresh-water banks give 2-3x; industry leads a small city (rail link, seaport); shops near the centre.
