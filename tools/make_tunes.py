#!/usr/bin/env python3
"""
Build the game's three cues as OUR OWN MIDI arrangements.

The three COMPOSITIONS are public domain: Rule, Britannia! (Arne, 1740),
The British Grenadiers (traditional march, 17th-18th c.), and the Marcha
Real / Marcha Granadera (anonymous, in print by 1761). Downloaded MIDI
encodings carry their encoders' terms, so none of them ships. Instead:
each reference file is used ONLY to verify the melody line, note for
note; the arrangement written out here (voicing, inner part, bass) is
this script's own, so the files it emits are clean to ship.

  python3 make_tunes.py <ref.mid> <out.mid> [--drop-short 0.15]

Reads the reference, takes the top line as the tune, harmonizes it in
the detected key (I ii IV V vi, chosen per half bar by melody fit), and
writes format-1 MIDI with tracks named Soprano / Violino II / Continuo,
which is what the organ renderer's role mapping expects.
"""
import struct, sys, os

# ----------------------------------------------------------- MIDI in
def parse_midi(path):
    d = open(path, "rb").read()
    assert d[:4] == b"MThd", "not midi"
    fmt, ntrk, div = struct.unpack(">HHH", d[8:14])
    i, tracks = 14, []
    for _ in range(ntrk):
        if d[i:i+4] != b"MTrk": break
        ln = struct.unpack(">I", d[i+4:i+8])[0]
        tracks.append(d[i+8:i+8+ln]); i += 8+ln
    notes = []
    for trk in tracks:
        j, t, running = 0, 0, None
        pending = {}
        while j < len(trk):
            dt = 0
            while j < len(trk) and trk[j] & 0x80:
                dt = (dt<<7)|(trk[j]&0x7F); j += 1
            if j >= len(trk): break
            dt = (dt<<7)|trk[j]; j += 1; t += dt
            if j >= len(trk): break
            b = trk[j]
            if b == 0xFF:
                j += 2
                ln2 = 0
                while trk[j] & 0x80: ln2=(ln2<<7)|(trk[j]&0x7F); j+=1
                ln2=(ln2<<7)|trk[j]; j += 1+ln2
            elif b in (0xF0,0xF7):
                j += 1; ln2 = 0
                while trk[j]&0x80: ln2=(ln2<<7)|(trk[j]&0x7F); j+=1
                ln2=(ln2<<7)|trk[j]; j += 1+ln2
            else:
                if b & 0x80: running = b; j += 1
                st = running
                if (st & 0xF0) in (0xC0,0xD0): j += 1
                else:
                    pit, vel = trk[j], trk[j+1]; j += 2
                    if (st&0xF0)==0x90 and vel>0: pending.setdefault(pit,[]).append(t)
                    elif (st&0xF0)==0x80 or ((st&0xF0)==0x90 and vel==0):
                        if pending.get(pit):
                            t0 = pending[pit].pop(0)
                            notes.append((t0, t-t0, pit))
    notes.sort()
    return notes, div

# ----------------------------------------------- the tune: top line
def top_line(notes, div, drop_short):
    # group by onset (within a 32nd), take the highest voice
    groups = []
    for t0, dur, pit in notes:
        if groups and abs(t0 - groups[-1][0]) < div/8:
            groups[-1][1].append((pit, dur))
        else:
            groups.append([t0, [(pit, dur)]])
    mel = []
    for t0, g in groups:
        pit, dur = max(g)
        # accompaniment-only beats sit well under the running top line
        if mel and pit < mel[-1][2] - 9 and dur <= div:
            continue
        mel.append((t0, dur, pit))
    # clip overlaps at the next melody onset, drop ornaments
    out = []
    for i, (t0, dur, pit) in enumerate(mel):
        if i+1 < len(mel): dur = min(dur, mel[i+1][0] - t0)
        if dur <= 0: continue
        if dur / div < drop_short: continue
        out.append((t0, dur, pit))
    # an accompaniment note that leaked through reads as a single deep
    # dip between two high neighbours; a real melody turn does not
    clean = []
    for i, (t0, dur, pit) in enumerate(out):
        prev = out[i-1][2] if i > 0 else pit
        nxt = out[i+1][2] if i+1 < len(out) else pit
        if prev - pit > 0 and nxt - pit > 0 and (prev-pit) + (nxt-pit) > 12:
            continue
        clean.append((t0, dur, pit))
    return clean

# --------------------------------------------------- key and chords
MAJ = [0,2,4,5,7,9,11]
def detect_key(mel):
    hist = [0]*12
    for t0, dur, pit in mel: hist[pit%12] += dur
    best, tonic = -1, 0
    for k in range(12):
        s = sum(hist[(k+d)%12] for d in MAJ) + hist[k]*.5 + hist[(k+7)%12]*.25
        if s > best: best, tonic = s, k
    return tonic

def harmonize(mel, div, tonic):
    """One chord per half bar (2 beats): I ii IV V vi by melody fit,
    V preferred at phrase ends, I at the final."""
    DEG = [0, 2, 5, 7, 9]                 # I ii IV V vi roots
    win = div*2
    end = max(t0+dur for t0,dur,_ in mel)
    chords = []
    w = (mel[0][0] // win) * win
    while w < end:
        inside = [(t0,dur,p) for t0,dur,p in mel if t0 < w+win and t0+dur > w]
        if inside:
            best, root = -1e9, tonic
            for dg in DEG:
                r = (tonic+dg) % 12
                tones = {r, (r+4)%12 if dg in (0,5,7) else (r+3)%12, (r+7)%12}
                s = sum(dur*(2 if p%12 in tones else -1.2) for t0,dur,p in inside)
                if dg == 0: s *= 1.12     # home wins ties
                if dg == 7: s *= 1.05
                if s > best: best, root = s, (tonic+dg)%12
            third = (root+4)%12 if (root-tonic)%12 in (0,5,7) else (root+3)%12
            chords.append((w, min(win, end-w), root, third))
        w += win
    # the last chord is the tonic, held
    if chords:
        w0, dur0, _, _ = chords[-1]
        chords[-1] = (w0, dur0, tonic, (tonic+4)%12)
    return chords

def near(pc, target):                      # pitch of class pc nearest target
    base = target - ((target - pc) % 12)
    return base if abs(base-target) <= abs(base+12-target) else base+12

# ----------------------------------------------------------- MIDI out
def vlq(n):
    out = [n & 0x7F]; n >>= 7
    while n: out.append((n & 0x7F) | 0x80); n >>= 7
    return bytes(reversed(out))

def track(name, events, extra_meta=b""):
    # events: list of (tick, bytes)
    events = sorted(events, key=lambda e: e[0])
    data = b"\x00\xFF\x03" + vlq(len(name)) + name.encode() + extra_meta
    t = 0
    for tick, ev in events:
        data += vlq(tick - t) + ev; t = tick
    data += b"\x00\xFF\x2F\x00"
    return b"MTrk" + struct.pack(">I", len(data)) + data

def note_events(notes, ch, vel=96):
    ev = []
    for t0, dur, pit in notes:
        ev.append((t0, bytes([0x90|ch, pit, vel])))
        ev.append((t0+dur, bytes([0x80|ch, pit, 0])))
    return ev

def main():
    ref, out = sys.argv[1], sys.argv[2]
    drop_short = .15
    if "--drop-short" in sys.argv:
        drop_short = float(sys.argv[sys.argv.index("--drop-short")+1])
    notes, div = parse_midi(ref)
    mel = top_line(notes, div, drop_short)
    tonic = detect_key(mel)
    chords = harmonize(mel, div, tonic)
    melmean = sum(p for _,_,p in mel)//len(mel)

    harm, bass = [], []
    for w, dur, root, third in chords:
        b = near(root, 45)                         # continuo around A2
        bass.append((w, dur, b))
        harm.append((w, dur, near(third, melmean-8)))
        harm.append((w, dur, near((root+7)%12, melmean-12)))

    hdr = b"MThd" + struct.pack(">IHHH", 6, 1, 4, div)
    # 120 bpm placeholder tempo; the renderer takes BPM on its own argv
    t0trk = track("conductor", [(0, b"\xFF\x51\x03\x07\xA1\x20")])
    mid = hdr + t0trk \
        + track("Soprano", note_events(mel, 0)) \
        + track("Violino II", note_events(harm, 1, 72)) \
        + track("Continuo", note_events(bass, 2, 88))
    open(out, "wb").write(mid)
    NAMES = "C C# D D# E F F# G G# A A# B".split()
    print(f"{os.path.basename(out)}: {len(mel)} melody notes, key {NAMES[tonic]} major, "
          f"{len(chords)} chords, div {div}")
    print("  tune:", " ".join(f"{NAMES[p%12]}{p//12-1}" for _,_,p in mel[:24]))

main()
