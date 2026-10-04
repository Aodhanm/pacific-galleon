#!/usr/bin/env python3
"""
Render the REAL St Matthew Passion final chorus from MIDI through the
storm-organ synth. This replaces the optical transcription entirely.

  python3 render_midi.py [SEMITONES] [BPM] [BARS] [STEM]
  defaults:              0           60    all    all

Source: tobis-BWV_0244_68.mid - 23 tracks, full double-choir and orchestra
scoring (flauto traverso, oboes, violins, viola, SATB x2, organo e continuo),
7857 note-ons, 3/4. Its key-signature meta event says 2 flats, which is
WRONG; the pitch content is unambiguously C minor, so trust the notes.
Its opening line - Eb5 F5 G5 F5 Eb5 D5 C5 - matches the hand-verified
bar 1 exactly, note for note and rhythm for rhythm.
"""
import numpy as np
import struct, wave, os, sys

# PACIFIC GALLEON fork of passion-organ/scripts/render_midi.py: same
# storm-organ synth, but source MIDI and output come from the
# environment, because this renders OUR OWN arrangements (music/*.mid,
# built by make_tunes.py), which are clean to ship.
SRC = os.path.expanduser(os.environ["MIDI_SRC"])
SR    = 44100

# ---- the SECOND TIME THROUGH. Organists do not play a chorale twice the
# same way: the second verse gets a fuller registration and a broader hand.
# HOLD   stretches every note, so the line is sustained instead of detached
# SWELL  0..1 opens the box: more reed, more weight in the inner parts and
#        the pedal, a brighter cutoff, a 16 ft coupler under the bass, and
#        more of the building in the sound
HOLD   = float(os.environ.get("HOLD", "1.0"))
SWELL  = float(os.environ.get("SWELL", "0.0"))
OUTTAG = os.environ.get("OUTTAG", "")

TRANS = int(sys.argv[1]) if len(sys.argv) > 1 else 0
BPM   = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
NBARS = sys.argv[3] if len(sys.argv) > 3 else "all"
STEM  = sys.argv[4] if len(sys.argv) > 4 else "all"
rng   = np.random.default_rng(7)
hz    = lambda m: 440.0 * 2.0 ** ((m - 69) / 12.0)

# ------------------------------------------------------------- MIDI parse
def parse_midi(path):
    d = open(path, "rb").read()
    assert d[:4] == b"MThd", "not a MIDI file"
    fmt, ntrk, div = struct.unpack(">HHH", d[8:14])
    i, tracks = 14, []
    for _ in range(ntrk):
        if d[i:i + 4] != b"MTrk":
            break
        ln = struct.unpack(">I", d[i + 4:i + 8])[0]
        tracks.append(d[i + 8:i + 8 + ln])
        i += 8 + ln

    notes, tempos = [], []
    for ti, trk in enumerate(tracks):
        name, j, t, running = None, 0, 0, None
        pending = {}
        while j < len(trk):
            dt = 0
            while j < len(trk) and trk[j] & 0x80:
                dt = (dt << 7) | (trk[j] & 0x7F); j += 1
            if j >= len(trk):
                break
            dt = (dt << 7) | trk[j]; j += 1; t += dt
            if j >= len(trk):
                break
            b = trk[j]
            if b == 0xFF:
                mt = trk[j + 1]; j += 2
                ln2 = 0
                while trk[j] & 0x80:
                    ln2 = (ln2 << 7) | (trk[j] & 0x7F); j += 1
                ln2 = (ln2 << 7) | trk[j]; j += 1
                data = trk[j:j + ln2]; j += ln2
                if mt == 0x03 and name is None:
                    name = data.decode("latin1").replace("\r", " ") \
                               .replace("\n", " ").strip()
                elif mt == 0x51 and len(data) >= 3:
                    tempos.append((t, int.from_bytes(data, "big")))
            elif b in (0xF0, 0xF7):
                j += 1; ln2 = 0
                while trk[j] & 0x80:
                    ln2 = (ln2 << 7) | (trk[j] & 0x7F); j += 1
                ln2 = (ln2 << 7) | trk[j]; j += 1 + ln2
            else:
                if b & 0x80:
                    running = b; j += 1
                st = running
                if (st & 0xF0) in (0xC0, 0xD0):
                    j += 1
                else:
                    pit, vel = trk[j], trk[j + 1]; j += 2
                    if (st & 0xF0) == 0x90 and vel > 0:
                        pending.setdefault(pit, []).append((t, vel))
                    elif (st & 0xF0) == 0x80 or ((st & 0xF0) == 0x90 and vel == 0):
                        if pending.get(pit):
                            t0, v0 = pending[pit].pop(0)
                            notes.append((t0, t - t0, pit, v0, ti, name))
        for pit, lst in pending.items():          # unterminated notes
            for t0, v0 in lst:
                notes.append((t0, div, pit, v0, ti, name))
    return notes, div


notes, DIV = parse_midi(SRC)
notes.sort()
names = {}
for _, _, _, _, ti, nm in notes:
    if nm and ti not in names:
        names[ti] = nm
print(f"{len(notes)} notes, {len(names)} named tracks, division {DIV}",
      file=sys.stderr)

# -------------------------------------------------------- role assignment
def role_of(nm, pitch):
    """Track names differ between the two encodings, so handle both."""
    n = (nm or "").lower()
    if "ii" in n.replace("iii", "") and ("oboe" in n or "violino" in n):
        return "harm"
    if any(k in n for k in ("flauto", "oboe i", "violino i", "soprano",
                            "treble 1", "1st violin")):
        return "mel"
    if any(k in n for k in ("organo", "continuo", "basso", "bass", "d'bass")):
        return "bass"
    return "harm"

SPB = 60.0 / BPM
def beats(ticks):
    return ticks / DIV

end_beat = max(beats(t0 + dur) for t0, dur, *_ in notes)
if NBARS != "all":
    lim = int(NBARS) * 4.0
    notes = [n for n in notes if beats(n[0]) < lim]
    end_beat = min(end_beat, lim)
TAIL = 5.0
TOTAL = end_beat * SPB + TAIL
N = int(TOTAL * SR)
t_axis = np.arange(N) / SR
print(f"{end_beat:.0f} beats = {end_beat/4:.0f} bars -> {TOTAL/60:.1f} min",
      file=sys.stderr)

# ------------------------------------------------------------- the organ
FLUE = [(1.0, 1.00), (2.0, 0.50), (3.0, 0.30), (4.0, 0.20),
        (6.0, 0.11), (8.0, 0.07), (12.0, 0.035)]
REED = [(1.0, 0.80), (3.0, 0.55), (5.0, 0.38), (7.0, 0.26),
        (9.0, 0.17), (11.0, 0.11), (13.0, 0.07)]
DETUNE = (-0.0020, 0.0, 0.0021)
AMP     = {"mel": 0.95 + 0.10 * SWELL,
           "harm": 0.16 + 0.26 * SWELL,      # the inner parts come forward
           "bass": 0.34 + 0.30 * SWELL}      # and the pedal takes weight
REEDAMT = {"mel": 0.62 + 0.22 * SWELL,
           "harm": 0.16 + 0.34 * SWELL,
           "bass": 0.14 + 0.30 * SWELL}
ROLLOFF = {"mel": 4600.0 + 2200 * SWELL,     # brighter: the box is open
           "harm": 900.0 + 1500 * SWELL,
           "bass": 700.0 + 900 * SWELL}
SPREAD  = {"mel": 0.00, "harm": 0.34, "bass": 0.24}

L = np.zeros(N, dtype=np.float32)
R = np.zeros(N, dtype=np.float32)

def note(start_s, dur_s, midi, amp, reed, cut, spread):
    attack = 0.020 + 0.010 * SWELL
    release = 0.090 + 0.130 * SWELL          # it rings on in a fuller room
    dur_s = dur_s * HOLD
    n = int((dur_s + release) * SR)
    i0 = int(start_s * SR)
    n = min(n, N - i0)
    if n <= 4:
        return
    tt = np.arange(n) / SR
    f0 = hz(midi)
    drift = 1.0 + 0.0013 * np.sin(2 * np.pi * 0.19 * tt + midi) \
                + 0.0008 * np.sin(2 * np.pi * 0.07 * tt + 1.3)
    cd = np.cumsum(drift) / SR
    sig = np.zeros(n, dtype=np.float32)
    for stack, w in ((FLUE, 1.0 - reed), (REED, reed)):
        for mult, pa in stack:
            if f0 * mult > SR * 0.45:
                continue
            roll = 1.0 / (1.0 + (f0 * mult / cut) ** 2.0)
            if w * pa * roll < 0.004:
                continue
            for dt in DETUNE:
                sig += (w * pa * roll * np.sin(
                    2 * np.pi * f0 * mult * (1 + dt) * cd + mult * 0.7)
                        ).astype(np.float32)
    sig /= len(DETUNE)
    a_n = max(1, int(attack * SR)); r_n = max(1, int(release * SR))
    e = np.concatenate([np.linspace(0, 1, a_n) ** 1.25,
                        np.full(max(0, n - a_n - r_n), 1.0),
                        np.linspace(1, 0, r_n) ** 1.6]).astype(np.float32)
    e = e[:n] if len(e) >= n else np.pad(e, (0, n - len(e)))
    sig *= e * amp
    pan = 0.5 + spread * np.sin(midi * 1.7)
    L[i0:i0 + n] += sig * np.sqrt(1 - pan)
    R[i0:i0 + n] += sig * np.sqrt(pan)

count = {"mel": 0, "harm": 0, "bass": 0}
for t0, dur, pit, vel, ti, nm in notes:
    role = role_of(names.get(ti), pit)
    if STEM not in ("all",) and role != STEM:
        continue
    count[role] += 1
    note(beats(t0) * SPB, max(beats(dur), .12) * SPB, pit + TRANS,
         AMP[role] * (0.55 + 0.45 * vel / 127.0),
         REEDAMT[role], ROLLOFF[role], SPREAD[role])
    # 4' coupler on the tune so it sits above the texture in pitch
    if role == "mel":
        note(beats(t0) * SPB, max(beats(dur), .12) * SPB, pit + TRANS + 12,
             AMP[role] * (0.46 + 0.16 * SWELL), 0.28, 5200.0, 0.0)
    # and on the second verse the organist draws more stops. This is what
    # actually makes a second verse sound bigger: not more volume, which the
    # mastering takes straight back out, but MORE RANKS. A 16 ft under the
    # pedal for weight, and a twelfth and a fifteenth on the upper parts,
    # which is the mixture that gives a full organ its edge.
    if SWELL > 0.05:
        if role == "bass" and pit + TRANS - 12 > 20:
            note(beats(t0) * SPB, max(beats(dur), .12) * SPB, pit + TRANS - 12,
                 AMP[role] * 0.55 * SWELL, 0.10, 420.0, 0.10)
        if role in ("mel", "harm"):
            note(beats(t0) * SPB, max(beats(dur), .12) * SPB, pit + TRANS + 19,
                 AMP[role] * 0.30 * SWELL, 0.30, 6200.0, 0.14)   # the twelfth
            note(beats(t0) * SPB, max(beats(dur), .12) * SPB, pit + TRANS + 24,
                 AMP[role] * 0.22 * SWELL, 0.34, 7000.0, 0.18)   # the fifteenth
print(f"rendered  mel {count['mel']}  harm {count['harm']}  bass {count['bass']}",
      file=sys.stderr)

# ------------------------------------------------------------- the storm
def fft_filter(x, lo=None, hi=None, slope=2.0):
    n = len(x); X = np.fft.rfft(x); f = np.fft.rfftfreq(n, 1 / SR)
    g = np.ones_like(f)
    if hi: g /= (1.0 + (f / hi) ** slope)
    if lo: g *= (f / lo) ** slope / (1.0 + (f / lo) ** slope)
    return np.fft.irfft(X * g, n).astype(np.float32)

def make_ir(sec, dec, seed):
    r = np.random.default_rng(seed); n = int(sec * SR)
    ir = r.normal(0, 1, n) * np.exp(-np.linspace(0, dec, n))
    ir[:int(.03 * SR)] *= np.linspace(0, 1, int(.03 * SR))
    ir = fft_filter(ir, lo=45, hi=2600, slope=1.7)
    return (ir / (np.abs(ir).sum() ** 0.5 + 1e-9)).astype(np.float32)

def conv(x, ir):
    nir = len(ir); blk = 1 << 16
    nfft = 1 << (blk + nir - 1).bit_length()
    IR = np.fft.rfft(ir, nfft)
    out = np.zeros(len(x) + nir, dtype=np.float32)
    for i in range(0, len(x), blk):
        y = np.fft.irfft(np.fft.rfft(x[i:i + blk], nfft) * IR, nfft)
        out[i:i + len(y)] += y[:len(out) - i].astype(np.float32)
    return out[:len(x)]

wl, wr = conv(L, make_ir(1.6, 7.0, 11)), conv(R, make_ir(1.6, 7.0, 23))
for a in (wl, wr, L, R):
    a /= np.abs(a).max() + 1e-9

w = rng.normal(0, 1, N).astype(np.float32)
wind = fft_filter(w, lo=55, hi=640, slope=1.9); wind /= np.abs(wind).max() + 1e-9
gust = np.interp(t_axis, np.linspace(0, TOTAL, 40), rng.random(40)) ** 1.4
bed = (0.05 * wind * (0.5 + gust)).astype(np.float32)

wet = 0.14 + 0.16 * SWELL                 # more of the building in it
ml = 0.94 * L + wet * wl + bed
mr = 0.94 * R + wet * wr + np.roll(bed, 700)
shell = np.clip(t_axis / .6, 0, 1) * np.clip((TOTAL - t_axis) / 3.5, 0, 1)
ml = np.tanh(ml * shell * 1.4); mr = np.tanh(mr * shell * 1.4)
g = 10 ** (-1.2 / 20) / (max(np.abs(ml).max(), np.abs(mr).max()) + 1e-9)

tag = ("" if STEM == "all" else "_" + STEM) + OUTTAG
OUT = os.path.expanduser(os.environ.get("OUT_WAV",
      f"~/pacific-galleon/music/render{tag}.wav"))
st = np.empty(N * 2, np.int16)
st[0::2] = np.int16(np.clip(ml * g, -1, 1) * 32767)
st[1::2] = np.int16(np.clip(mr * g, -1, 1) * 32767)
with wave.open(OUT, "wb") as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
    f.writeframes(st.tobytes())
print(f"{os.path.basename(OUT)}  {TOTAL/60:.1f} min  {TRANS:+d}st  {BPM:.0f}bpm  hold x{HOLD}  swell {SWELL}")
