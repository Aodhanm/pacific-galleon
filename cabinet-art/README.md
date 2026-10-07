# Cabinet art for the arcade

Generators for the two SVGs the arcade cabinet needs. They write straight into
`~/aodhancoyne-games/assets/`, so edit these and re-run them, never the SVGs.

    python3 build_marquee.py     # -> assets/marquee-pacific-galleon.svg  (760x190)
    python3 build_art.py         # -> assets/art-pacific-galleon.svg      (400x520)

`text_to_paths.py` sets a line of display type as SVG **outline paths**.
Trattatello is a macOS system font: as live `<text>` it falls back to a plain
serif on every other machine and the whole look goes, so the letterforms are
carried in the file itself. This is how `marquee-doghole.svg` solves it too.

⚠ **The cabinet shows only a BAND of the front panel**, not the whole thing:
the `.art` box is 214px tall with `object-fit:cover` at `50% 46%`, so roughly
`y=140..345` is all a player ever sees, and the coin door then covers
`x=137..263, y=288..345`. Everything that matters lives between y=140 and
y=288, and the centre-bottom is left as water. Preview any change at the real
crop before believing it.

The third asset, `still-pacific-galleon.jpg`, is just a 960x720 capture of the
game's own title screen.
