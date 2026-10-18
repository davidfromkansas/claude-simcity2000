# Bot tools

- `start.sh` – start the virtual screen + SimCity 2000 in DOSBox (game files in `/opt/sc2k/game`).
- `sc` – control helper (screenshot, click, drag, menus, keys, save, log).
- `sc2parse.py` – reads the `.SC2` save file into metrics.
- `publish.py loop` – every 5 minutes: screenshot, metrics, video clips → `docs/` and push (GitHub Pages dashboard).
- `record.sh` – records the screen into 30-minute MP4 clips.
