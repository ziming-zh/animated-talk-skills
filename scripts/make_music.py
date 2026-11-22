#!/usr/bin/env python3
"""Make the background music for an animated talk.

An original, calm ambient loop, synthesized from scratch (no samples, so no
licensing question): soft pad chords, a sparse bell arpeggio and a low bass,
through a simple reverb. The bells and an octave-up layer of the pad carry most of
the sound, above the voice's range, so the music is still heard on laptop speakers
under the narration. Everything is laid down circularly, so the loop is seamless.
Writes music.m4a next to the page. The player plays it whenever the voice does,
and dips it while the voice speaks.

  python3 make_music.py --out path/to/talk/music.m4a
Runs under the Kokoro venv in ~/.local/share/tts (it needs numpy and soundfile).
"""
import os, subprocess, sys, tempfile

TTS = os.path.expanduser("~/.local/share/tts")
try:
    import numpy as np
    import soundfile as sf
except ImportError:
    py = os.path.join(TTS, "venv/bin/python")
    os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])

import argparse
_ap = argparse.ArgumentParser()
_ap.add_argument("--out", required=True, help="where to write music.m4a, next to the page")
OUT = os.path.abspath(_ap.parse_args().out)
SR = 44100
BAR = 4.0                       # seconds per chord
rng = np.random.default_rng(7)
# levels: the pad and bass are kept low, since they share the voice's range and small
# speakers barely play them; the bells and the pad's upper octave carry the music
PAD, AIR, BASS, BELL = 0.022, 0.014, 0.02, 0.06

def hz(m):                      # midi note to Hz
    return 440.0 * 2 ** ((m - 69) / 12)

# Fmaj7 - G6 - Em7 - Am7, four passes: bells sparse, full, turned around, then thinning out
CHORDS = [[53, 57, 60, 64], [55, 59, 62, 64], [52, 55, 59, 62], [57, 60, 64, 67]]
ROOTS = [41, 43, 40, 45]
BELLS = [
    [72, 76, 79, 76, 72, 69, None, None],
    [71, 74, 76, 74, 71, None, 67, None],
    [71, 67, 64, 67, 71, None, None, 74],
    [72, 69, 64, 69, 72, None, 76, None],
]
PASSES = 4
LOOP = BAR * len(CHORDS) * PASSES
N = int(LOOP * SR)
L = np.zeros(N)
R = np.zeros(N)

def env(n, a, r):
    e = np.ones(n)
    ia, ir = int(a * SR), int(r * SR)
    e[:ia] = np.sin(np.linspace(0, np.pi / 2, ia)) ** 2
    e[-ir:] *= np.cos(np.linspace(0, np.pi / 2, ir)) ** 2
    return e

def add(buf, start, sig):      # circular, so whatever runs past the end lands at the start
    idx = (int(round(start * SR)) + np.arange(len(sig))) % N
    np.add.at(buf, idx, sig)

for rep in range(PASSES):
    for ci, chord in enumerate(CHORDS):
        t0 = (rep * len(CHORDS) + ci) * BAR
        # pad: each note a few slightly detuned sines, overlapping the next chord
        dur = BAR + 1.6
        n = int(dur * SR)
        t = np.arange(n) / SR
        e = env(n, 1.4, 1.8)
        for m in chord:
            f = hz(m)
            for side, det in ((L, -0.12), (R, 0.12)):
                w = (np.sin(2 * np.pi * (f + det) * t + rng.uniform(0, 6.28))
                     + 0.18 * np.sin(2 * np.pi * 2 * (f - det) * t)
                     + 0.06 * np.sin(2 * np.pi * 3 * f * t))
                trem = 1 + 0.08 * np.sin(2 * np.pi * 0.23 * t + m)
                add(side, t0 - 0.6, PAD * w * e * trem)
                add(side, t0 - 0.6, AIR * np.sin(2 * np.pi * 2 * (f + det) * t + m) * e * trem)
        # bass
        f = hz(ROOTS[ci])
        b = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)
        bass = BASS * b * env(n, 0.8, 2.0)
        add(L, t0 - 0.3, bass); add(R, t0 - 0.3, bass)
        # bells an octave above the tune, eighth notes at half the bar, quieter on the first pass
        full = BELLS[ci]
        line = [full[:4] + [None] * 4, full, full[::-1], [full[0], None, None, full[3]] + [None] * 4][rep]
        for k, m in enumerate(line):
            if m is None:
                continue
            bd = 2.4
            bn = int(bd * SR)
            bt = np.arange(bn) / SR
            f = hz(m + 12)
            tone = (np.sin(2 * np.pi * f * bt) + 0.3 * np.sin(2 * np.pi * 2.01 * f * bt) * np.exp(-bt * 3)
                    + 0.12 * np.sin(2 * np.pi * 3.98 * f * bt) * np.exp(-bt * 6))
            a = np.minimum(1, bt / 0.006) * np.exp(-bt * 1.7)
            pan = 0.5 + 0.35 * np.sin(k * 1.3 + ci)
            g = BELL * (0.8 + 0.2 * rng.random())
            add(L, t0 + k * BAR / 8 + 0.02 * rng.random(), g * (1 - pan) * 2 * tone * a)
            add(R, t0 + k * BAR / 8 + 0.02 * rng.random(), g * pan * 2 * tone * a)


# reverb: convolve with decaying stereo noise, circularly so the loop stays seamless
def reverb(x, seed):
    ir_n = int(3.2 * SR)
    g = np.random.default_rng(seed).standard_normal(ir_n) * np.exp(-np.arange(ir_n) / SR * 2.1)
    g[: int(0.02 * SR)] = 0
    k = np.zeros(N); k[:ir_n] = g / np.sqrt(np.sum(g ** 2))
    return np.real(np.fft.ifft(np.fft.fft(x) * np.fft.fft(k)))

wl, wr = reverb(L, 1), reverb(R, 2)
L, R = 0.7 * L + 0.55 * wl, 0.7 * R + 0.55 * wr
# soften the very top and drop rumble, in the frequency domain so the loop stays seamless
fr = np.fft.rfftfreq(N, 1 / SR)
shape = 1 / (1 + (fr / 6500) ** 2) * (fr / np.sqrt(fr ** 2 + 70 ** 2))
L = np.fft.irfft(np.fft.rfft(L) * shape, N)
R = np.fft.irfft(np.fft.rfft(R) * shape, N)
st = np.stack([L, R], 1)
st /= np.max(np.abs(st)) / 0.7

with tempfile.TemporaryDirectory() as tmp:
    wav = os.path.join(tmp, "m.wav")
    sf.write(wav, st.astype(np.float32), SR)
    subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-b", "96000", wav, OUT], check=True)
print("wrote", OUT, "%.0fs loop" % LOOP)
