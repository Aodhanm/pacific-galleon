#!/usr/bin/env python3
"""Build assets/art-pacific-galleon.svg  (400 x 520), the cabinet front panel.

⚠ THE CABINET SHOWS A BAND OF THIS, NOT THE WHOLE THING. The .art box is
214px tall with object-fit:cover, so at object-position 50% 46% roughly
y=140..345 of these coordinates is what a player ever sees, and the coin
door then sits over x=137..263, y=288..345. So everything that matters
lives between y=140 and y=288, and the centre-bottom is left as water.

The scene is the same hour as the marquee and the title screen: the Manila
galleon running for the cape with the sun going down behind El Arco, your
own ship coming up on her quarter with a broadside away, and the prize
already open on your own rail in the corner.

(The ship drawings are deliberately a separate copy from build_marquee.py.
These are leaf art assets at different scales and compositions; keeping
them independent means tuning one can never break the other.)
"""
import io
from text_to_paths import layout

W, H = 400, 520
HZ = 214.0                       # the horizon, inside the visible band

o = []
A = o.append

A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img"')
A('     aria-label="Cabinet art: the Manila galleon running for Cabo San Lucas at sunset, an English private '
  'ship coming up on her quarter with a broadside away, the arch at Land\'s End beyond, and an opened chest '
  'of treasure on the rail in the foreground">')

A('''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#070C22"/>
    <stop offset=".30" stop-color="#10193C"/>
    <stop offset=".54" stop-color="#2E2B52"/>
    <stop offset=".70" stop-color="#6E4E58"/>
    <stop offset=".86" stop-color="#C98A55"/>
    <stop offset="1"   stop-color="#F7CC80"/>
  </linearGradient>
  <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="#D59B5E"/>
    <stop offset=".07" stop-color="#8A7068"/>
    <stop offset=".26" stop-color="#2D4563"/>
    <stop offset=".70" stop-color="#101E38"/>
    <stop offset="1"   stop-color="#05091A"/>
  </linearGradient>
  <radialGradient id="sunGlow" cx=".5" cy=".5" r=".5">
    <stop offset="0"   stop-color="#FFF5D4" stop-opacity=".95"/>
    <stop offset=".32" stop-color="#FFD089" stop-opacity=".5"/>
    <stop offset="1"   stop-color="#E88B45" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="rock" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5C4458"/><stop offset=".55" stop-color="#3A2B3E"/>
    <stop offset="1" stop-color="#191324"/>
  </linearGradient>
  <linearGradient id="rockLit" x1="1" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#D0906A"/><stop offset=".5" stop-color="#7B5550"/>
    <stop offset="1" stop-color="#2F2437"/>
  </linearGradient>
  <linearGradient id="canvasG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFF2D8"/><stop offset=".55" stop-color="#E7D1AB"/>
    <stop offset="1" stop-color="#B2906F"/>
  </linearGradient>
  <linearGradient id="canvasShade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#C6AA8C"/><stop offset="1" stop-color="#75604F"/>
  </linearGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6E4726"/><stop offset=".5" stop-color="#492D18"/>
    <stop offset="1" stop-color="#1F1207"/>
  </linearGradient>
  <linearGradient id="rail" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#32200F"/><stop offset=".22" stop-color="#180E05"/>
    <stop offset="1" stop-color="#070300"/>
  </linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFEBA8"/><stop offset=".45" stop-color="#E8B341"/>
    <stop offset="1" stop-color="#95620F"/>
  </linearGradient>
  <clipPath id="frame"><rect x="0" y="0" width="400" height="520"/></clipPath>
  <clipPath id="seaClip"><rect x="0" y="214" width="400" height="306"/></clipPath>
</defs>
<g clip-path="url(#frame)">''')

# ------------------------------------------------------------- sky
A(f'<rect width="{W}" height="{HZ+1}" fill="url(#sky)"/>')
A('<!-- the sun, low and right, dropping behind the arch -->')
A('<ellipse cx="86" cy="206" rx="70" ry="44" fill="url(#sunGlow)" opacity=".8"/>')
A('<circle cx="86" cy="204" r="11" fill="#FFF7DE" opacity=".97"/>')
A('<circle cx="86" cy="204" r="16" fill="#FFE3A4" opacity=".28"/>')
A('<!-- cloud strata, lit along the undersides -->')
A('<g>')
for cx, cy, rx, ry, op in [(90,118,86,6,.26),(250,104,70,5,.22),(160,142,98,5.5,.30),
                           (300,138,86,5,.26),(70,164,74,4.5,.30),(250,170,100,5,.28),
                           (150,186,110,4.5,.26),(340,180,60,4,.22),(60,196,66,3.6,.24)]:
    A(f' <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#161F42" opacity="{op}"/>')
    A(f' <ellipse cx="{cx+5}" cy="{cy+ry*.85:.1f}" rx="{rx*.86:.0f}" ry="{ry*.5:.1f}" fill="#F0B174" opacity="{op*.72:.2f}"/>')
A('</g>')
A(f'<rect x="0" y="{HZ-14}" width="{W}" height="15" fill="#EFAF70" opacity=".30"/>')
A(f'<rect x="0" y="{HZ-6}" width="{W}" height="7" fill="#FBD79A" opacity=".34"/>')

# ------------------------------------------- LAND'S END and EL ARCO, right
A('''<!-- ============= LAND'S END, with El Arco at the point =============
     Cavendish: the cape "is very like the Needles at the isle of Wight",
     which is a file of sharp stacks, not a smooth bluff. -->''')
A('<g transform="translate(-190,0)">')
A(' <path d="M400 214 L400 150 L386 155 L372 146 L356 153 L342 145 L328 156 L316 165 L306 178 L300 192 L297 214 Z" fill="url(#rock)"/>')
A(' <path d="M400 214 L400 150 L386 155 L376 152 L368 162 L362 178 L360 196 L362 214 Z" fill="url(#rockLit)" opacity=".5"/>')
A(' <g stroke="#2A1F30" stroke-width=".65" opacity=".5" fill="none">')
A('  <path d="M302 196 L400 180"/><path d="M306 204 L400 190"/><path d="M314 186 L392 172"/>')
A(' </g>')
A(' <!-- THE ARCH, with the sunset showing through the span -->')
A(' <path d="M252 214 L254 192 Q258 172 272 168 Q288 164 295 180 L297 214 L286 214 L284 192 Q282 181 272 182 Q263 183 262 195 L261 214 Z" fill="url(#rock)"/>')
A(' <path d="M254 192 Q258 172 272 168 Q288 164 295 180 L292 185 Q286 172 272 175 Q261 178 259 194 Z" fill="#B57F60" opacity=".5"/>')
A(' <!-- the friars, the outliers off the tip -->')
A(' <path d="M228 214 L230 198 L236 189 L243 198 L244 214 Z" fill="url(#rock)"/>')
A(' <path d="M215 214 L217 205 L221 199 L226 206 L227 214 Z" fill="url(#rock)" opacity=".9"/>')
A(' <path d="M205 214 L206 208 L209 204 L212 209 L213 214 Z" fill="url(#rock)" opacity=".8"/>')
A(' <g fill="#FFF2DA" opacity=".5">')
A('  <ellipse cx="273" cy="214" rx="20" ry="2.4"/><ellipse cx="236" cy="214.5" rx="13" ry="2"/>')
A('  <ellipse cx="220" cy="215" rx="9" ry="1.6"/><ellipse cx="350" cy="214" rx="42" ry="2.2"/>')
A(' </g>')
A('</g>')

# -------------------------------------------------------------- the sea
A(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="url(#sea)"/>')
A('<g clip-path="url(#seaClip)">')
A(' <g fill="#FFD79A">')
for y, w2, op in [(215,36,.5),(219,46,.46),(224,56,.42),(230,68,.36),(237,80,.3),
                  (245,94,.26),(254,108,.22),(264,122,.18),(275,134,.14)]:
    A(f'  <rect x="{86-w2/2:.0f}" y="{y}" width="{w2}" height="2" rx="1" opacity="{op}"/>')
A(' </g>')
A(' <g stroke="#9FB4CE" stroke-width="1" fill="none" opacity=".14">')
for y in range(220, 360, 8):
    A(f'  <path d="M-10 {y} q60 -2.5 120 0 q60 2.5 120 0 q60 -2.5 120 0 q60 2.5 120 0"/>')
A(' </g>')
A(' <g stroke="#040A16" stroke-width="1.5" fill="none" opacity=".24">')
for y in range(226, 360, 13):
    A(f'  <path d="M-10 {y} q70 3 140 0 q70 -3 140 0 q70 3 140 0"/>')
A(' </g>')
A('</g>')

# ------------------------------------------------- THE MANILA GALLEON
A('''<!-- ================= THE MANILA GALLEON, centre ===================
     Seven hundred tons, deep in the water, a high sterncastle, running
     for the cape. Scaled to .80 of the marquee drawing to fit 400px. -->''')
A('<g transform="translate(100,92) scale(1.30)">')
A('  <path d="M18 128 Q10 124 8 116 L12 110 L30 108 L150 104 L168 100 L176 104 L178 116 Q174 126 160 130 Q90 136 18 128 Z" fill="url(#wood)"/>')
A('  <path d="M14 112 L170 103 L171 108 L15 117 Z" fill="#C58B52" opacity=".55"/>')
A('  <path d="M16 120 L172 111 L173 115 L17 124 Z" fill="#8A5A30" opacity=".5"/>')
A('  <path d="M150 104 L152 78 L178 76 L180 104 Z" fill="#53331C"/>')
A('  <path d="M152 78 L178 76 L180 83 L152 85 Z" fill="#D29A5C" opacity=".5"/>')
A('  <g fill="#FFD98E" opacity=".92">')
for i in range(4):
    A(f'   <rect x="{156+i*6}" y="88" width="4" height="6.4" rx=".8"/>')
A('  </g>')
A('  <g fill="#FFE7B0" opacity=".78">')
for i in range(3):
    A(f'   <rect x="{159+i*6}" y="79" width="3.4" height="4.4" rx=".7"/>')
A('  </g>')
A('  <path d="M12 110 L14 94 L34 93 L36 108 Z" fill="#53331C"/>')
A('  <path d="M14 94 L34 93 L35 98 L14 99 Z" fill="#C98F55" opacity=".45"/>')
A('  <g fill="#120A03">')
for i in range(11):
    A(f'   <rect x="{34+i*10.4:.1f}" y="{113-i*.52:.1f}" width="5.8" height="4.6" rx=".6"/>')
A('  </g>')
A('  <g fill="#E8A95E" opacity=".35">')
for i in range(11):
    A(f'   <rect x="{34+i*10.4:.1f}" y="{113-i*.52:.1f}" width="5.8" height="1" rx=".4"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="3" stroke-linecap="round">')
A('   <path d="M46 96 L44 18"/><path d="M92 94 L90 6"/><path d="M140 92 L139 26"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="1.7" stroke-linecap="round">')
A('   <path d="M30 58 L62 56"/><path d="M28 34 L60 32"/>')
A('   <path d="M70 50 L114 48"/><path d="M72 24 L112 22"/><path d="M76 11 L108 10"/>')
A('   <path d="M122 58 L158 56"/><path d="M124 36 L156 35"/>')
A('   <path d="M14 104 L-30 84"/>')
A('  </g>')
A('  <g>')
A('   <path d="M31 58 L61 56 Q66 76 62 94 L34 95 Q28 78 31 58 Z" fill="url(#canvasG)"/>')
A('   <path d="M29 34 L59 32 Q63 46 61 55 L32 57 Q27 46 29 34 Z" fill="url(#canvasG)"/>')
A('   <path d="M71 50 L113 48 Q119 72 114 92 L74 94 Q67 72 71 50 Z" fill="url(#canvasG)"/>')
A('   <path d="M73 24 L111 22 Q115 37 113 47 L72 49 Q69 37 73 24 Z" fill="url(#canvasG)"/>')
A('   <path d="M77 11 L107 10 Q110 17 109 21 L75 23 Q74 17 77 11 Z" fill="url(#canvasG)"/>')
A('   <path d="M123 58 L157 56 Q161 74 158 90 L126 91 Q120 75 123 58 Z" fill="url(#canvasG)"/>')
A('   <path d="M125 36 L155 35 Q158 47 157 55 L124 57 Q122 47 125 36 Z" fill="url(#canvasG)"/>')
A('   <path d="M139 40 L139 88 L166 86 Q152 64 139 40 Z" fill="url(#canvasShade)"/>')
A('   <path d="M-22 88 L8 100 L6 110 L-24 98 Z" fill="url(#canvasShade)" opacity=".92"/>')
A('  </g>')
A('  <g stroke="#A58A6C" stroke-width=".6" opacity=".55" fill="none">')
A('   <path d="M40 57 L42 95"/><path d="M50 56 L52 95"/>')
A('   <path d="M84 49 L86 93"/><path d="M98 48 L100 93"/>')
A('   <path d="M134 57 L136 90"/><path d="M146 56 L147 90"/>')
A('  </g>')
A('  <g stroke="#1E1308" stroke-width=".65" opacity=".8" fill="none">')
A('   <path d="M44 28 L22 96"/><path d="M45 28 L34 96"/><path d="M46 40 L58 97"/>')
A('   <path d="M90 14 L66 95"/><path d="M90 14 L78 95"/><path d="M91 24 L108 95"/>')
A('   <path d="M139 32 L124 92"/><path d="M139 32 L152 92"/>')
A('  </g>')
A('  <!-- the Cross of Burgundy at the ensign staff -->')
A('  <g transform="translate(180,82)">')
A('   <path d="M0 0 L32 -3 L33 15 L1 18 Z" fill="#F2E6D0"/>')
A('   <g stroke="#B3362A" stroke-width="2.4" stroke-linecap="round">')
A('    <path d="M4 3 L29 12"/><path d="M4 14 L29 2"/>')
A('   </g>')
A('   <g stroke="#B3362A" stroke-width="1" opacity=".8"><path d="M4 3 L29 12"/><path d="M4 14 L29 2"/></g>')
A('  </g>')
A('  <!-- the royal standard at the main truck -->')
A('  <g transform="translate(90,11)">')
A('   <path d="M0 0 L24 2 L24 12 L0 10 Z" fill="#E8D7B4"/>')
A('   <rect x="8" y="3.4" width="9" height="5.4" fill="#B3362A" opacity=".9"/>')
A('   <rect x="8" y="3.4" width="9" height="5.4" fill="none" stroke="#8A6A22" stroke-width=".6"/>')
A('  </g>')
A('  <path d="M8 124 Q-16 128 -36 124 Q-16 133 10 132 Z" fill="#FFF2DA" opacity=".4"/>')
A('  <ellipse cx="92" cy="132" rx="80" ry="4" fill="#FFF2DA" opacity=".16"/>')
A('</g>')

# ------------------------------------------------- THE ENGLISH SHIP, left
A('''<!-- ============ THE ENGLISH PRIVATE SHIP, coming up =============
     Lower, leaner, flush-decked, wearing the red ensign with the pre-1801
     union in the canton, which is right for Rogers 1709 and Anson 1743. -->''')
A('<g transform="translate(2,170) scale(0.38)">')
A('  <path d="M10 126 Q4 121 3 114 L8 109 L24 108 L116 106 L128 103 L134 107 L135 116 Q130 124 118 127 Q66 132 10 126 Z" fill="url(#wood)"/>')
A('  <path d="M7 112 L128 106 L129 110 L8 116 Z" fill="#BE8450" opacity=".5"/>')
A('  <path d="M116 106 L118 88 L135 87 L136 106 Z" fill="#4A2D18"/>')
A('  <g fill="#FFD98E" opacity=".85">')
for i in range(3):
    A(f'   <rect x="{120+i*5}" y="94" width="3.2" height="4.8" rx=".6"/>')
A('  </g>')
A('  <g fill="#120A03">')
for i in range(9):
    A(f'   <rect x="{24+i*9.6:.1f}" y="{112-i*.3:.1f}" width="5" height="4" rx=".6"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="2.8" stroke-linecap="round">')
A('   <path d="M36 100 L34 26"/><path d="M76 98 L74 14"/><path d="M114 96 L113 38"/>')
A('  </g>')
A('  <g stroke="#2A1A0C" stroke-width="1.6" stroke-linecap="round">')
A('   <path d="M22 62 L50 60"/><path d="M20 40 L48 38"/>')
A('   <path d="M58 54 L94 52"/><path d="M60 30 L92 28"/><path d="M64 18 L88 17"/>')
A('   <path d="M100 62 L130 60"/>')
A('   <path d="M9 104 L-30 86"/>')
A('  </g>')
A('  <g>')
A('   <path d="M23 62 L49 60 Q53 80 50 99 L26 100 Q20 80 23 62 Z" fill="url(#canvasG)"/>')
A('   <path d="M21 40 L47 38 Q50 51 49 59 L24 61 Q19 51 21 40 Z" fill="url(#canvasG)"/>')
A('   <path d="M59 54 L93 52 Q98 74 94 96 L62 97 Q56 75 59 54 Z" fill="url(#canvasG)"/>')
A('   <path d="M61 30 L91 28 Q94 42 93 51 L60 53 Q58 42 61 30 Z" fill="url(#canvasG)"/>')
A('   <path d="M65 18 L87 17 Q89 23 88 27 L63 29 Q63 23 65 18 Z" fill="url(#canvasG)"/>')
A('   <path d="M101 62 L129 60 Q132 76 130 92 L104 93 Q99 76 101 62 Z" fill="url(#canvasG)"/>')
A('   <path d="M113 50 L113 92 L136 90 Q124 70 113 50 Z" fill="url(#canvasShade)"/>')
A('  </g>')
A('  <g stroke="#1E1308" stroke-width=".6" opacity=".8" fill="none">')
A('   <path d="M34 36 L16 100"/><path d="M34 36 L26 100"/><path d="M35 46 L46 101"/>')
A('   <path d="M74 22 L54 97"/><path d="M74 22 L64 97"/><path d="M75 32 L90 97"/>')
A('  </g>')
A('  <!-- the red ensign -->')
A('  <g transform="translate(136,91)">')
A('   <path d="M0 0 L32 -2 L33 15 L1 17 Z" fill="#B8342A"/>')
A('   <path d="M0 0 L16 -1 L17 7.5 L1 8.5 Z" fill="#1F3566"/>')
A('   <g stroke="#F4F0E6" stroke-width="1.1" fill="none"><path d="M0 0 L17 7.5"/><path d="M1 8.5 L16 -1"/></g>')
A('   <g stroke="#F4F0E6" stroke-width="2.4" fill="none"><path d="M0.5 4.2 L16.5 3.2"/><path d="M8.5 -.5 L9 8"/></g>')
A('   <g stroke="#C03A2A" stroke-width="1.2" fill="none"><path d="M0.5 4.2 L16.5 3.2"/><path d="M8.5 -.5 L9 8"/></g>')
A('  </g>')
A('  <!-- her broadside, and the powder bank rolling away to leeward -->')
A('  <g>')
for cx, cy, r, op in [(152,114,19,.5),(170,106,15,.42),(188,114,16,.38),
                      (206,104,13,.3),(214,116,14,.28),(232,108,12,.22),
                      (142,120,14,.44),(180,122,13,.32),(218,122,11,.22)]:
    A(f'   <circle cx="{cx}" cy="{cy}" r="{r}" fill="#F3DCBC" opacity="{op}"/>')
A('   <g fill="#FFB65C">')
for i in (1,3,5,7):
    A(f'    <ellipse cx="{28+i*9.6:.1f}" cy="{114-i*.3:.1f}" rx="2.8" ry="1.8" opacity=".95"/>')
A('   </g>')
A('  </g>')
A('</g>')

A('<!-- her shot falling short, between the two of them -->')
A('<g fill="#FFF4DF" opacity=".62">')
A(' <path d="M112 228 q2.4 -10 4.6 0 q-2.4 3 -4.6 0 Z"/><ellipse cx="114" cy="229" rx="5.4" ry="1.7"/>')
A(' <path d="M92 236 q2 -8 4 0 q-2 2.4 -4 0 Z"/><ellipse cx="94" cy="237" rx="4.6" ry="1.5"/>')
A('</g>')
A('<g stroke="#FFE9C6" stroke-width="1" fill="none" opacity=".5">')
A(' <path d="M196 168 q4 -3 8 0 q4 -3 8 0"/><path d="M340 160 q3 -2.4 6 0 q3 -2.4 6 0"/>')
A('</g>')

# --------------------------------- FOREGROUND: your rail, and the prize
A('''<!-- ========== YOUR OWN RAIL, and the chest already open ===========
     This is the bottom of the visible band. The chest sits LEFT so the
     coin door (x=137..263, y=288..345) covers water, not treasure.
     Cavendish burned the Santa Ana with "500 tunnes of goods in her"
     because he could not carry it: hence a chest that is already full
     and still spilling. -->''')
A('<g>')
A(f'  <path d="M0 {H} L0 268 Q90 261 200 264 Q310 267 400 259 L400 {H} Z" fill="url(#rail)"/>')
A('  <path d="M0 270 Q90 263 200 266 Q310 269 400 261 L400 267 Q310 275 200 272 Q90 269 0 276 Z" fill="#45301A" opacity=".9"/>')
A('  <g fill="#1A1008">')
for x in range(292, 400, 34):
    A(f'   <rect x="{x}" y="266" width="4" height="13" rx="1.6"/>')
    A(f'   <rect x="{x-2}" y="264" width="8" height="3.4" rx="1.6"/>')
A('  </g>')
A('  <!-- a grapnel hooked over the rail, line leading away to the prize -->')
A('  <g stroke="#2A1B10" stroke-width="2.6" fill="none" stroke-linecap="round">')
A('   <path d="M196 264 Q216 246 244 238"/>')
A('  </g>')
A('  <g fill="#3A3A44">')
A('   <path d="M236 232 l10 6 -3 7 -10 -6 z"/>')
A('   <path d="M244 230 q7 2 8 10 l-4 1 q-1 -6 -6 -7 z"/>')
A('   <path d="M232 236 q-7 1 -9 8 l4 2 q2 -6 7 -6 z"/>')
A('  </g>')
A('  <!-- THE CHEST -->')
A('  <g transform="translate(4,232)">')
A('   <path d="M4 30 L9 7 L100 3 L107 25 Z" fill="#4A2E19"/>')
A('   <path d="M9 7 L100 3 L102 10 L11 14 Z" fill="#6B4526"/>')
A('   <g stroke="#C9A24A" stroke-width="2.2" fill="none" opacity=".9">')
A('    <path d="M33 5.4 L37 28.6"/><path d="M76 3.6 L81 26.4"/>')
A('   </g>')
A('   <path d="M0 30 L110 26 L112 62 Q56 69 2 62 Z" fill="url(#wood)"/>')
A('   <path d="M0 30 L110 26 L110.6 35 L.6 39 Z" fill="#7A5330" opacity=".8"/>')
A('   <g stroke="#C9A24A" stroke-width="2.6" fill="none">')
A('    <path d="M31 29 L33 65"/><path d="M78 27 L81 63"/>')
A('   </g>')
A('   <rect x="48" y="39" width="17" height="14" rx="2" fill="#C9A24A"/>')
A('   <rect x="52" y="43" width="9" height="6" rx="1.4" fill="#2A1B0C"/>')
A('   <g>')
A('    <path d="M17 28 L47 26 L49 33 L19 35 Z" fill="url(#gold)"/>')
A('    <path d="M54 26 L82 24 L84 31 L56 33 Z" fill="url(#gold)"/>')
A('    <path d="M32 21 L62 19 L64 26 L34 28 Z" fill="#FFE9A3"/>')
A('    <path d="M32 21 L62 19 L62.6 21.4 L32.6 23.4 Z" fill="#FFF7D6"/>')
A('   </g>')
A('   <g fill="url(#gold)" stroke="#8A5E14" stroke-width=".4">')
for cx,cy,r in [(12,34,4.4),(21,38,4.8),(32,36,4.4),(41,40,5),(51,35,4.4),
                (62,38,4.8),(72,35,4.4),(83,38,4.8),(93,35,4.4),(102,40,4.4),
                (6,45,4.6),(105,47,4.4),(17,50,4),(95,52,4)]:
    A(f'    <ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.62:.1f}"/>')
A('   </g>')
A('   <g fill="#F6F2E6" opacity=".92">')
for i in range(12):
    A(f'    <circle cx="{66+i*3.6:.1f}" cy="{50+(i*i)*0.26:.1f}" r="2.1"/>')
A('   </g>')
A('   <g fill="url(#gold)" stroke="#8A5E14" stroke-width=".35">')
for cx,cy,r in [(124,58,4.2),(137,62,3.8),(151,58,3.4),(118,66,3.6),(132,68,3.2),
                (-7,58,3.8),(-15,64,3.4),(163,63,3),(145,69,2.8)]:
    A(f'    <ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.6:.1f}"/>')
A('   </g>')
A('  </g>')
A('</g>')

# ---------------------------------------------------- the name on the panel
# The doghole panel carries its own title; this does the same, inside the
# visible band (y=140..288) and over a scrim so the galleon's upper sails
# do not fight it.
A('<linearGradient id="nameScrim" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0" stop-color="#0A0714" stop-opacity=".0"/>'
  '<stop offset=".30" stop-color="#0A0714" stop-opacity=".62"/>'
  '<stop offset=".72" stop-color="#0A0714" stop-opacity=".58"/>'
  '<stop offset="1" stop-color="#0A0714" stop-opacity="0"/></linearGradient>')
A('<rect x="0" y="132" width="400" height="60" fill="url(#nameScrim)"/>')
_, nw = layout("PACIFIC GALLEON", "trattatello", 31, 0, 0)
npaths, _ = layout("PACIFIC GALLEON", "trattatello", 31, (W-nw)/2, 170)
A('<g fill="#0B0712" opacity=".7" transform="translate(1.4,2)">'); A("\n".join(npaths)); A('</g>')
A('<g fill="#FFF3DC">'); A("\n".join(npaths)); A('</g>')
# (no date line here: it sits over the sails and will not read. The marquee carries it.)

A('</g>')
A('</svg>')

io.open("/Users/aodhan/aodhancoyne-games/assets/art-pacific-galleon.svg","w").write("\n".join(o))
print("wrote cabinet art")
