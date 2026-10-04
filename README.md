# PACIFIC GALLEON

The English raiders of the Pacific, 1579 to 1743, and the Manila
galleon off Cabo San Lucas. Top-down sailing in the doghole engine
(`~/doghole/`): same physics, same flat-vector language, square rig.

    python3 serve_nocache.py                       # port 8914
    open http://127.0.0.1:8914/play.html           # the open-water chase scaffold
    open "http://127.0.0.1:8914/play.html?ship=duke"   # or desire, centurion

Design and build order: `PLAN.md`. Status: **open-water scaffold** only.
One English ship, one galleon running the coast, the chase, a boarding
card when you lay her alongside. No land, guns, grapple or boarding yet.

Files: `play.html` (page, loop, HUD, cards) · `ships.js` (classes,
square-rig physics, drawing) · `sea.js` (water, weather; becomes
`cape.js` work when the Cabo shore goes in).

Dev hooks in the console: `__dev.put(x,y,hdg)`, `__dev.wind(from,kn)`,
`__dev.close()` drops you 120 yards astern of the prize.
