#!/usr/bin/env python3
"""Build assets/marquee-pacific-galleon.svg  (760 x 190).

Golden hour at Cabo San Lucas, looking west past your own rail: the Manila
galleon running for the cape with the sun behind her, your ship coming up on
her quarter with a broadside away, El Arco at Land's End to the right, and the
prize already open on your own deck in the foreground.

The lettering is carried as OUTLINE PATHS (see text_to_paths.py): Trattatello
is a macOS system font and live <text> would fall back to a plain serif
everywhere else, which is how the doghole marquee solves the same problem.
"""
import io
from text_to_paths import layout

W, H = 760, 190
HZ = 124.0                     # the horizon

def centred(text, font, size, baseline, tracking=0.0):
    _, w = layout(text, font, size, 0, 0, tracking)
    paths, _ = layout(text, font, size, (W - w) / 2, baseline, tracking)
    return paths, w

o = []
A = o.append

A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img"')
A('     aria-label="Marquee: Pacific Galleon. The Manila galleon running for Cabo San Lucas at sunset with an '
  'English private ship coming up on her quarter, a broadside away, the arch at Land\'s End beyond, and the '
  'opened treasure in the foreground">')

# ----------------------------------------------------------------- defs
A('''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#0B1430"/>
    <stop offset=".22" stop-color="#1B2A50"/>
    <stop offset=".46" stop-color="#4A4668"/>
    <stop offset=".66" stop-color="#9A6A58"/>
    <stop offset=".82" stop-color="#D99A58"/>
    <stop offset="1"   stop-color="#F6C878"/>
  </linearGradient>
  <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#C98F57"/>
    <stop offset=".10" stop-color="#7E6A66"/>
    <stop offset=".34" stop-color="#2E4664"/>
    <stop offset="1"   stop-color="#0A1326"/>
  </linearGradient>
  <radialGradient id="sunGlow" cx=".5" cy=".5" r=".5">
    <stop offset="0"   stop-color="#FFF3CE" stop-opacity=".95"/>
    <stop offset=".34" stop-color="#FFD089" stop-opacity=".55"/>
    <stop offset="1"   stop-color="#E88B45" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="rock" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5A4256"/><stop offset=".55" stop-color="#3A2B3E"/>
    <stop offset="1" stop-color="#1C1626"/>
  </linearGradient>
  <linearGradient id="rockLit" x1="1" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#C98A62"/><stop offset=".5" stop-color="#7B5550"/>
    <stop offset="1" stop-color="#32273A"/>
  </linearGradient>
  <linearGradient id="canvasG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFF0D2"/><stop offset=".55" stop-color="#E8D2AC"/>
    <stop offset="1" stop-color="#B9977C"/>
  </linearGradient>
  <linearGradient id="canvasShade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#C9AE90"/><stop offset="1" stop-color="#7E6557"/>
  </linearGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6B4526"/><stop offset=".5" stop-color="#4A2E19"/>
    <stop offset="1" stop-color="#241509"/>
  </linearGradient>
  <linearGradient id="rail" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#2A1B10"/><stop offset=".25" stop-color="#160D06"/>
    <stop offset="1" stop-color="#090501"/>
  </linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFE9A3"/><stop offset=".45" stop-color="#E8B341"/>
    <stop offset="1" stop-color="#9A6716"/>
  </linearGradient>
  <linearGradient id="smoke" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFE6C0" stop-opacity=".85"/>
    <stop offset="1" stop-color="#8C7E78" stop-opacity=".15"/>
  </linearGradient>
  <clipPath id="seaClip"><rect x="0" y="118" width="760" height="72"/></clipPath>
  <clipPath id="frame"><rect x="0" y="0" width="760" height="190"/></clipPath>
</defs>
<g clip-path="url(#frame)">''')

# ------------------------------------------------------------ sky + sun
A(f'<rect width="{W}" height="{HZ+1}" fill="url(#sky)"/>')
A('<!-- the sun, low and to the right, so both ships come at you in half silhouette -->')
A('<ellipse cx="596" cy="116" rx="150" ry="92" fill="url(#sunGlow)"/>')
A('<circle cx="596" cy="113" r="16" fill="#FFF6DC" opacity=".97"/>')
A('<circle cx="596" cy="113" r="23" fill="#FFE3A4" opacity=".35"/>')

A('<!-- cloud strata: flat, long, lit along their undersides -->')
A('<g>')
for cx, cy, rx, ry, op in [(120,34,104,7,.30),(250,22,74,5,.22),(470,30,120,6,.26),
                           (650,20,86,5,.20),(180,54,120,6,.34),(560,52,130,6,.30),
                           (330,44,96,5,.24),(700,44,70,4,.22),(90,70,86,4.5,.30),
                           (420,66,150,5,.26),(660,68,92,4,.24)]:
    A(f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#1A2342" opacity="{op}"/>')
    A(f'  <ellipse cx="{cx+6}" cy="{cy+ry*.85:.1f}" rx="{rx*.86:.0f}" ry="{ry*.5:.1f}" fill="#F3B877" opacity="{op*.75:.2f}"/>')
A('</g>')

A('<!-- the haze band that always sits on a sunset horizon -->')
A(f'<rect x="0" y="{HZ-16}" width="{W}" height="17" fill="#F0B274" opacity=".30"/>')
A(f'<rect x="0" y="{HZ-7}" width="{W}" height="8" fill="#FBD79A" opacity=".34"/>')

# ------------------------------------------- LAND'S END and EL ARCO, right
A('''<!-- ================= LAND'S END, with the arch =====================
     The granite ridge running out to the southern tip of Baja, and El Arco
     at the very point with the sea through it. Cavendish called this cape
     "very like the Needles at the isle of Wight", which is the shape: a
     file of sharp stacks, not a smooth bluff. -->''')
A('<g>')
# the far ridge inland
A('  <path d="M760 118 L760 54 L742 58 L726 50 L706 56 L690 46 L672 56 L656 62 L640 72 L628 84 L618 96 L612 108 L610 118 Z" fill="url(#rock)" opacity=".95"/>')
# the sunlit western face
A('  <path d="M760 118 L760 54 L742 58 L726 50 L712 57 L704 70 L700 86 L702 102 L706 118 Z" fill="url(#rockLit)" opacity=".55"/>')
# strata
A('  <g stroke="#2A1F30" stroke-width=".7" opacity=".5" fill="none">')
A('   <path d="M616 100 L760 82"/><path d="M620 108 L760 92"/><path d="M628 90 L748 72"/>')
A('  </g>')
# the detached stacks: the arch and the friars
A('  <!-- the arch: two legs and the span, with the sunset showing through -->')
A('  <path d="M560 118 L562 96 Q566 78 578 74 Q592 70 598 84 L600 118 L590 118 L588 96 Q586 86 578 87 Q571 88 570 99 L569 118 Z" fill="url(#rock)"/>')
A('  <path d="M562 96 Q566 78 578 74 Q592 70 598 84 L596 88 Q590 76 578 79 Q568 82 566 98 Z" fill="#B07A5E" opacity=".55"/>')
A('  <!-- the friars, the outlying rocks off the tip -->')
A('  <path d="M534 118 L536 104 L541 96 L547 104 L548 118 Z" fill="url(#rock)"/>')
A('  <path d="M522 118 L524 110 L528 105 L532 111 L533 118 Z" fill="url(#rock)" opacity=".9"/>')
A('  <path d="M512 118 L513 113 L516 110 L519 114 L519 118 Z" fill="url(#rock)" opacity=".8"/>')
A('  <!-- surf breaking at the feet of all of it -->')
A('  <g fill="#FFF2DA" opacity=".55">')
A('   <ellipse cx="579" cy="118" rx="22" ry="2.6"/><ellipse cx="541" cy="118.5" rx="13" ry="2"/>')
A('   <ellipse cx="527" cy="119" rx="9" ry="1.7"/><ellipse cx="640" cy="118" rx="34" ry="2.4"/>')
A('   <ellipse cx="712" cy="118.5" rx="42" ry="2.2"/>')
A('  </g>')
A('</g>')

# --------------------------------------------------------------- the sea
A(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="url(#sea)"/>')
A('<g clip-path="url(#seaClip)">')
A('  <!-- the sun path: a broken column of gold straight down from the sun -->')
A('  <g fill="#FFD79A">')
for y, w2, op in [(120,46,.55),(124,58,.5),(129,70,.45),(135,84,.4),(142,96,.34),
                  (150,112,.3),(159,126,.26),(169,140,.22),(180,152,.18)]:
    A(f'   <rect x="{596-w2/2:.0f}" y="{y}" width="{w2}" height="2.2" rx="1.1" opacity="{op}"/>')
    A(f'   <rect x="{596-w2/3:.0f}" y="{y+2.6:.1f}" width="{w2*.55:.0f}" height="1.4" rx=".7" opacity="{op*.7:.2f}"/>')
A('  </g>')
A('  <!-- swell, long and low -->')
A('  <g stroke="#9FB4CE" stroke-width="1" fill="none" opacity=".16">')
for y in range(124, 190, 7):
    A(f'   <path d="M-10 {y} q90 -2.5 180 0 q90 2.5 180 0 q90 -2.5 180 0 q90 2.5 180 0"/>')
A('  </g>')
A('  <g stroke="#06101F" stroke-width="1.4" fill="none" opacity=".22">')
for y in range(132, 190, 11):
    A(f'   <path d="M-10 {y} q100 3 200 0 q100 -3 200 0 q100 3 200 0 q100 -3 200 0"/>')
A('  </g>')
A('</g>')

A('<!-- the lettering scrim: without it the topmasts fight the title -->')
A('<linearGradient id="scrim" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0" stop-color="#0B0814" stop-opacity=".62"/>'
  '<stop offset=".55" stop-color="#0B0814" stop-opacity=".34"/>'
  '<stop offset="1" stop-color="#0B0814" stop-opacity="0"/></linearGradient>')

# ------------------------------------------------- THE MANILA GALLEON
A('''<!-- ===================== THE MANILA GALLEON =======================
     Centre-right, running for the cape with the sun behind her, so she is
     a warm half-silhouette. Tubby, deep in the water, a high sterncastle,
     three masts under courses and topsails. Seven hundred tons, and the
     accounts have her as "the great S. Anna". -->''')
A('<g transform="translate(352,6)">')
# ---- hull
A('  <path d="M18 128 Q10 124 8 116 L12 110 L30 108 L150 104 L168 100 L176 104 L178 116 Q174 126 160 130 Q90 136 18 128 Z" fill="url(#wood)"/>')
A('  <!-- the sunlit strake along her side -->')
A('  <path d="M14 112 L170 103 L171 108 L15 117 Z" fill="#C58B52" opacity=".55"/>')
A('  <path d="M16 120 L172 111 L173 115 L17 124 Z" fill="#8A5A30" opacity=".5"/>')
# ---- sterncastle, high and square, on the right
A('  <path d="M150 104 L152 80 L178 78 L180 104 Z" fill="#53331C"/>')
A('  <path d="M152 80 L178 78 L180 84 L152 86 Z" fill="#D29A5C" opacity=".5"/>')
A('  <!-- her stern gallery windows, catching the sun -->')
A('  <g fill="#FFD98E" opacity=".9">')
for i in range(4):
    A(f'   <rect x="{156+i*6}" y="88" width="4" height="6" rx=".8"/>')
A('  </g>')
A('  <g fill="#FFE7B0" opacity=".75">')
for i in range(3):
    A(f'   <rect x="{159+i*6}" y="80" width="3.4" height="4" rx=".7"/>')
A('  </g>')
# ---- forecastle
A('  <path d="M12 110 L14 96 L34 95 L36 108 Z" fill="#53331C"/>')
A('  <path d="M14 96 L34 95 L35 99 L14 100 Z" fill="#C98F55" opacity=".45"/>')
# ---- gunports
A('  <g fill="#120A03">')
for i in range(11):
    A(f'   <rect x="{34+i*10.4:.1f}" y="{113-i*.52:.1f}" width="5.6" height="4.4" rx=".6"/>')
A('  </g>')
A('  <g fill="#E8A95E" opacity=".35">')
for i in range(11):
    A(f'   <rect x="{34+i*10.4:.1f}" y="{113-i*.52:.1f}" width="5.6" height="1" rx=".4"/>')
A('  </g>')
# ---- masts and yards
A('  <g stroke="#2A1A0C" stroke-width="2.6" stroke-linecap="round">')
A('   <path d="M46 96 L44 26"/><path d="M92 94 L90 14"/><path d="M140 92 L139 32"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="1.5" stroke-linecap="round">')
A('   <path d="M30 60 L62 58"/><path d="M28 38 L60 36"/>')
A('   <path d="M70 52 L114 50"/><path d="M72 28 L112 26"/><path d="M76 16 L108 15"/>')
A('   <path d="M122 60 L158 58"/><path d="M124 40 L156 39"/>')
A('   <!-- the bowsprit, steeving up sharply as they did -->')
A('   <path d="M14 104 L-26 86"/>')
A('  </g>')
# ---- sails: courses and topsails, bellied to leeward
A('  <g>')
A('   <path d="M31 60 L61 58 Q66 76 62 94 L34 95 Q28 78 31 60 Z" fill="url(#canvasG)"/>')
A('   <path d="M29 38 L59 36 Q63 48 61 57 L32 59 Q27 48 29 38 Z" fill="url(#canvasG)"/>')
A('   <path d="M71 52 L113 50 Q119 72 114 92 L74 94 Q67 72 71 52 Z" fill="url(#canvasG)"/>')
A('   <path d="M73 28 L111 26 Q115 39 113 49 L72 51 Q69 39 73 28 Z" fill="url(#canvasG)"/>')
A('   <path d="M77 16 L107 15 Q110 21 109 25 L75 27 Q74 21 77 16 Z" fill="url(#canvasG)"/>')
A('   <path d="M123 60 L157 58 Q161 74 158 90 L126 91 Q120 75 123 60 Z" fill="url(#canvasG)"/>')
A('   <path d="M125 40 L155 39 Q158 49 157 57 L124 59 Q122 49 125 40 Z" fill="url(#canvasG)"/>')
A('   <!-- a lateen mizzen abaft -->')
A('   <path d="M139 44 L139 88 L166 86 Q152 66 139 44 Z" fill="url(#canvasShade)"/>')
A('   <!-- the spritsail under the bowsprit -->')
A('   <path d="M-18 90 L8 100 L6 110 L-20 100 Z" fill="url(#canvasShade)" opacity=".92"/>')
A('  </g>')
A('  <!-- seams and bolt-ropes, so the canvas is not flat -->')
A('  <g stroke="#A58A6C" stroke-width=".55" opacity=".6" fill="none">')
A('   <path d="M40 59 L42 95"/><path d="M50 58 L52 95"/>')
A('   <path d="M84 51 L86 93"/><path d="M98 50 L100 93"/>')
A('   <path d="M134 59 L136 90"/><path d="M146 58 L147 90"/>')
A('  </g>')
A('  <!-- shrouds -->')
A('  <g stroke="#1E1308" stroke-width=".6" opacity=".8" fill="none">')
A('   <path d="M44 34 L22 96"/><path d="M45 34 L34 96"/><path d="M46 44 L58 97"/>')
A('   <path d="M90 22 L66 95"/><path d="M90 22 L78 95"/><path d="M91 30 L108 95"/>')
A('   <path d="M139 38 L124 92"/><path d="M139 38 L152 92"/>')
A('  </g>')
# ---- her colours: the Cross of Burgundy aft, the royal standard at the main
A('  <!-- the Cross of Burgundy at the ensign staff -->')
A('  <g transform="translate(180,84)">')
A('   <path d="M0 0 L30 -3 L31 14 L1 17 Z" fill="#F2E6D0"/>')
A('   <g stroke="#B3362A" stroke-width="2.2" stroke-linecap="round">')
A('    <path d="M4 3 L27 11"/><path d="M4 13 L27 1"/>')
A('   </g>')
A('   <g stroke="#B3362A" stroke-width=".9" opacity=".8"><path d="M4 3 L27 11"/><path d="M4 13 L27 1"/></g>')
A('  </g>')
A('  <!-- the royal standard at the main truck, which Anson saw her wear -->')
A('  <g transform="translate(90,20)">')
A('   <path d="M0 0 L22 2 L22 11 L0 9 Z" fill="#E8D7B4"/>')
A('   <rect x="7" y="3" width="8" height="5" fill="#B3362A" opacity=".9"/>')
A('   <rect x="7" y="3" width="8" height="5" fill="none" stroke="#8A6A22" stroke-width=".6"/>')
A('  </g>')
A('  <!-- her wake and the water piled under her bow -->')
A('  <path d="M8 124 Q-16 128 -34 124 Q-16 132 10 131 Z" fill="#FFF2DA" opacity=".4"/>')
A('  <ellipse cx="92" cy="131" rx="78" ry="4" fill="#FFF2DA" opacity=".18"/>')
A('</g>')

# --------------------------------------------- THE ENGLISH PRIVATE SHIP
A('''<!-- ================= THE ENGLISH PRIVATE SHIP =====================
     Left, coming up on the galleon's quarter with her larboard broadside
     away. Race-built: lower, leaner, flush-decked, no towering castle.
     She wears the red ensign with the pre-1801 union in the canton, which
     is right for Rogers in 1709 and Anson in 1743. -->''')
A('<g transform="translate(78,14)">')
A('  <path d="M10 126 Q4 121 3 114 L8 109 L24 108 L116 106 L128 103 L134 107 L135 116 Q130 124 118 127 Q66 132 10 126 Z" fill="url(#wood)"/>')
A('  <path d="M7 112 L128 106 L129 110 L8 116 Z" fill="#BE8450" opacity=".5"/>')
A('  <path d="M116 106 L118 90 L135 89 L136 106 Z" fill="#4A2D18"/>')
A('  <g fill="#FFD98E" opacity=".85">')
for i in range(3):
    A(f'   <rect x="{120+i*5}" y="95" width="3.2" height="4.6" rx=".6"/>')
A('  </g>')
A('  <g fill="#120A03">')
for i in range(9):
    A(f'   <rect x="{24+i*9.6:.1f}" y="{112-i*.3:.1f}" width="5" height="4" rx=".6"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="2.3" stroke-linecap="round">')
A('   <path d="M36 100 L34 34"/><path d="M76 98 L74 24"/><path d="M114 96 L113 44"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="1.3" stroke-linecap="round">')
A('   <path d="M22 66 L50 64"/><path d="M20 46 L48 44"/>')
A('   <path d="M58 58 L94 56"/><path d="M60 36 L92 34"/><path d="M64 26 L88 25"/>')
A('   <path d="M100 66 L130 64"/>')
A('   <path d="M9 104 L-26 88"/>')
A('  </g>')
A('  <g>')
A('   <path d="M23 66 L49 64 Q53 82 50 99 L26 100 Q20 82 23 66 Z" fill="url(#canvasG)"/>')
A('   <path d="M21 46 L47 44 Q50 55 49 63 L24 65 Q19 55 21 46 Z" fill="url(#canvasG)"/>')
A('   <path d="M59 58 L93 56 Q98 76 94 96 L62 97 Q56 77 59 58 Z" fill="url(#canvasG)"/>')
A('   <path d="M61 36 L91 34 Q94 46 93 55 L60 57 Q58 46 61 36 Z" fill="url(#canvasG)"/>')
A('   <path d="M65 26 L87 25 Q89 30 88 33 L63 35 Q63 30 65 26 Z" fill="url(#canvasG)"/>')
A('   <path d="M101 66 L129 64 Q132 78 130 92 L104 93 Q99 78 101 66 Z" fill="url(#canvasG)"/>')
A('   <path d="M113 54 L113 92 L136 90 Q124 72 113 54 Z" fill="url(#canvasShade)"/>')
A('  </g>')
A('  <g stroke="#A58A6C" stroke-width=".5" opacity=".55" fill="none">')
A('   <path d="M32 66 L34 100"/><path d="M41 65 L43 100"/>')
A('   <path d="M70 57 L72 96"/><path d="M82 56 L84 96"/>')
A('  </g>')
A('  <g stroke="#1E1308" stroke-width=".55" opacity=".8" fill="none">')
A('   <path d="M34 42 L16 100"/><path d="M34 42 L26 100"/><path d="M35 50 L46 101"/>')
A('   <path d="M74 32 L54 97"/><path d="M74 32 L64 97"/><path d="M75 40 L90 97"/>')
A('  </g>')
A('  <!-- THE RED ENSIGN, with the pre-1801 union in the canton -->')
A('  <g transform="translate(136,93)">')
A('   <path d="M0 0 L30 -2 L31 14 L1 16 Z" fill="#B8342A"/>')
A('   <path d="M0 0 L15 -1 L16 7 L1 8 Z" fill="#1F3566"/>')
A('   <g stroke="#F4F0E6" stroke-width="1" fill="none">')
A('    <path d="M0 0 L16 7"/><path d="M1 8 L15 -1"/>')
A('   </g>')
A('   <g stroke="#F4F0E6" stroke-width="2.2" fill="none"><path d="M0.5 4 L15.5 3"/><path d="M8 -.5 L8.5 7.5"/></g>')
A('   <g stroke="#C03A2A" stroke-width="1.1" fill="none"><path d="M0.5 4 L15.5 3"/><path d="M8 -.5 L8.5 7.5"/></g>')
A('  </g>')
A('  <!-- the union jack at the bow -->')
A('  <g transform="translate(-30,84)">')
A('   <path d="M0 0 L16 4 L15 12 L-1 8 Z" fill="#1F3566"/>')
A('   <g stroke="#F4F0E6" stroke-width=".9" fill="none"><path d="M0 0 L15 12"/><path d="M-1 8 L16 4"/></g>')
A('   <g stroke="#F4F0E6" stroke-width="1.9" fill="none"><path d="M-.5 4 L15.5 8"/><path d="M8 1.6 L7.5 10.4"/></g>')
A('   <g stroke="#C03A2A" stroke-width=".9" fill="none"><path d="M-.5 4 L15.5 8"/><path d="M8 1.6 L7.5 10.4"/></g>')
A('  </g>')
A('  <!-- THE BROADSIDE, just gone: muzzle flashes and the smoke rolling away -->')
A('  <g>')
# a BANK of powder smoke: overlapping rounds, densest at the muzzles and
# thinning as it rolls away to leeward. Flat wide ellipses read as haze.
A('   <g>')
for cx, cy, r, op in [(150,116,17,.52),(166,110,14,.44),(182,116,15,.40),
                      (198,108,12,.33),(206,118,13,.30),(222,112,11,.24),
                      (238,118,10,.19),(252,110,8,.15),(266,117,7,.11),
                      (140,122,13,.46),(176,124,12,.34),(212,124,10,.24)]:
    A(f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#F3DCBC" opacity="{op}"/>')
A('   </g>')
A('   <g fill="#FFB65C">')
for i in (1,3,5,7):
    A(f'    <ellipse cx="{28+i*9.6:.1f}" cy="{114-i*.3:.1f}" rx="2.6" ry="1.7" opacity=".95"/>')
A('   </g>')
A('  </g>')
A('  <path d="M6 122 Q-14 126 -30 122 Q-14 129 8 128 Z" fill="#FFF2DA" opacity=".4"/>')
A('</g>')

A('<!-- her shot falling short of the galleon: three plumes -->')
A('<g fill="#FFF4DF" opacity=".7">')
A(' <path d="M352 132 q3 -14 6 0 q-3 4 -6 0 Z"/><ellipse cx="355" cy="133" rx="7" ry="2"/>')
A(' <path d="M376 137 q2.6 -11 5 0 q-2.5 3 -5 0 Z"/><ellipse cx="378" cy="138" rx="6" ry="1.8"/>')
A(' <path d="M330 141 q2 -9 4 0 q-2 2.6 -4 0 Z"/><ellipse cx="332" cy="142" rx="5" ry="1.6"/>')
A('</g>')

# --------------------------------------------------------------- gulls
A('<g stroke="#FFE9C6" stroke-width="1.1" fill="none" opacity=".6">')
A(' <path d="M236 40 q5 -4 10 0 q5 -4 10 0"/>')
A(' <path d="M268 54 q4 -3 8 0 q4 -3 8 0"/>')
A(' <path d="M702 88 q3.4 -2.6 7 0 q3.4 -2.6 7 0"/>')
A('</g>')

# -------------------------------------- FOREGROUND: your rail and the prize
A('''<!-- ============ YOUR OWN RAIL, and the prize already open ==========
     You are looking out over your own gunwale. Cavendish burned the Santa
     Ana with "500 tunnes of goods in her" because he could not carry it,
     so the chest in the corner is the point of the whole game: it is open,
     it is spilling, and it is nothing like all of it. -->''')
A('<g>')
A(f'  <path d="M0 {H} L0 168 Q120 160 300 163 Q520 167 760 158 L760 {H} Z" fill="url(#rail)"/>')
A(f'  <path d="M0 170 Q120 162 300 165 Q520 169 760 160 L760 166 Q520 175 300 171 Q120 168 0 176 Z" fill="#3E2A17" opacity=".9"/>')
A('  <!-- belaying pins along the rail -->')
A('  <g fill="#1A1008">')
for x in range(330, 760, 46):
    A(f'   <rect x="{x}" y="166" width="4" height="13" rx="1.6"/>')
    A(f'   <rect x="{x-2}" y="164" width="8" height="3.4" rx="1.6"/>')
A('  </g>')
A('  <!-- a gun run out through the port, muzzle still warm -->')
A('  <g>')
A('   <rect x="620" y="150" width="86" height="13" rx="5" fill="#1C1C22"/>')
A('   <rect x="620" y="150" width="86" height="4" rx="2" fill="#4A4A55" opacity=".7"/>')
A('   <ellipse cx="620" cy="156.5" rx="5.5" ry="7" fill="#0A0A0E"/>')
A('   <ellipse cx="620" cy="156.5" rx="3" ry="4" fill="#E8762E" opacity=".5"/>')
A('   <rect x="700" y="146" width="16" height="21" rx="3" fill="#241508"/>')
A('  </g>')
A('  <!-- THE CHEST, open, and overflowing -->')
A('  <g transform="translate(40,128)">')
A('   <!-- the lid, thrown back -->')
A('   <path d="M4 26 L8 6 L96 2 L102 22 Z" fill="#4A2E19"/>')
A('   <path d="M8 6 L96 2 L98 8 L10 12 Z" fill="#6B4526"/>')
A('   <g stroke="#C9A24A" stroke-width="2" fill="none" opacity=".9">')
A('    <path d="M30 4.6 L34 25"/><path d="M72 3 L76 23.4"/>')
A('   </g>')
A('   <!-- the body -->')
A('   <path d="M0 26 L106 22 L108 56 Q54 62 2 56 Z" fill="url(#wood)"/>')
A('   <path d="M0 26 L106 22 L106.6 30 L.6 34 Z" fill="#7A5330" opacity=".8"/>')
A('   <g stroke="#C9A24A" stroke-width="2.4" fill="none">')
A('    <path d="M28 25 L30 59"/><path d="M74 23.4 L77 57"/>')
A('   </g>')
A('   <rect x="46" y="34" width="16" height="13" rx="2" fill="#C9A24A"/>')
A('   <rect x="50" y="38" width="8" height="6" rx="1.4" fill="#2A1B0C"/>')
A('   <!-- what is in it: bars, plate, a rope of pearls, and coin everywhere -->')
A('   <g>')
A('    <path d="M16 24 L44 22 L46 28 L18 30 Z" fill="url(#gold)"/>')
A('    <path d="M50 22 L78 20 L80 26 L52 28 Z" fill="url(#gold)"/>')
A('    <path d="M30 18 L58 16 L60 22 L32 24 Z" fill="#FFE9A3"/>')
A('    <path d="M30 18 L58 16 L58.6 18 L30.6 20 Z" fill="#FFF7D6"/>')
A('   </g>')
A('   <g fill="url(#gold)" stroke="#8A5E14" stroke-width=".4">')
for i,(cx,cy,r) in enumerate([(12,30,4),(20,34,4.4),(30,32,4),(38,35,4.6),(48,31,4),
                              (58,34,4.4),(68,31,4),(78,34,4.4),(88,31,4),(96,35,4),
                              (6,40,4.2),(100,42,4),(16,44,3.6),(90,46,3.6)]):
    A(f'    <ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.62:.1f}"/>')
A('   </g>')
A('   <!-- a rope of pearls over the rim -->')
A('   <g fill="#F6F2E6" opacity=".92">')
for i in range(11):
    A(f'    <circle cx="{62+i*3.4:.1f}" cy="{44+ (i*i)*0.28:.1f}" r="2"/>')
A('   </g>')
A('   <!-- coin spilled out onto the deck -->')
A('   <g fill="url(#gold)" stroke="#8A5E14" stroke-width=".35">')
for cx,cy,r in [(118,52,4),(130,56,3.6),(144,52,3.2),(112,60,3.4),(126,62,3),
                (-8,52,3.6),(-16,58,3.2),(156,57,2.8),(138,62,2.6)]:
    A(f'    <ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.6:.1f}"/>')
A('   </g>')
A('  </g>')
A('</g>')

# ------------------------------------------------------------ the title
A('''<!-- ======================== THE TITLE ==============================
     Trattatello, carried as outline paths so it survives off a Mac. -->''')
A(f'<rect x="0" y="0" width="{W}" height="96" fill="url(#scrim)"/>')
tpaths, tw = centred("PACIFIC GALLEON", "trattatello", 64, 52)
A('<g fill="#120A14" opacity=".55" transform="translate(2,3)">')
A("\n".join(tpaths)); A('</g>')
A('<g fill="#FFF6E0">'); A("\n".join(tpaths)); A('</g>')
A('<g fill="#FFD68A" opacity=".45" transform="translate(-1,-1)">')
A("\n".join(tpaths)); A('</g>')

# the strap line goes on the RAIL, where it is dark and legible, not across
# the galleon's hull where it was unreadable
spaths, sw = layout("THE MANILA SHIP OFF CABO SAN LUCAS  \u00b7  1579 \u2013 1743",
                    "academy", 13, 254, 181, 1.8)
A('<g fill="#000000" opacity=".5" transform="translate(1,1.2)">'); A("\n".join(spaths)); A('</g>')
A('<g fill="#F0D9A8">'); A("\n".join(spaths)); A('</g>')
A('<g stroke="#C9A24A" stroke-width="1" opacity=".5"><path d="M236 177 l10 0"/></g>')

A('</g>')   # frame clip
A('</svg>')

io.open("/Users/aodhan/aodhancoyne-games/assets/marquee-pacific-galleon.svg","w").write("\n".join(o))
print("wrote marquee, title advance", round(tw,1), "subtitle", round(sw,1))
