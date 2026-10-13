# Claude plays SimCity 2000

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

## Screen map (640x480)
Menu bar y=7: File 25, Speed 67, Options 120, Disasters 185, Windows 252, Newspaper 320.
Toolbar is the left column (x 10-80).
