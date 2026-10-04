# PACIFIC GALLEON

The English raiders of the Pacific, 1579 to 1743, and the Manila
galleon off Cabo San Lucas. Top-down sailing in the doghole engine
(`~/doghole/`): same physics, same flat-vector language, square rig.

    python3 serve_nocache.py                       # port 8914
    open http://127.0.0.1:8914/play.html           # the open-water chase scaffold
    open "http://127.0.0.1:8914/play.html?ship=duke"   # or desire, centurion

Design and build order: `PLAN.md`. Status: **daytime Cabo build**:
the cape and bay, the ambush, the chase, manual broadsides (SPACE),
she strikes her colours, lay her aboard. Boarding/treasure/second
galleon still to come. Music: Rule Britannia (title), Marcha Real
slow (the sighting), British Grenadiers (the prize).

Files: `index.html` (title: the action off the cape, in profile) ·
`play.html` (page, loop, HUD, combat, cards) · `ships.js` (classes,
square-rig physics, drawing) · `cape.js` (Cabo San Lucas, depth,
weather, the galleon's lane) · `music/` + `tools/` (the three cues and
the pipeline that renders them).

Dev hooks in the console: `__dev.put(x,y,hdg)`, `__dev.wind(from,kn)`,
`__dev.close()` drops you 120 yards astern of the prize.
