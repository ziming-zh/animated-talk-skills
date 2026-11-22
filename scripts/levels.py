#!/usr/bin/env python3
"""Check that the music can be heard under the voice.

Prints the A-weighted level of each file (close to what the ear hears at low volume)
and where its energy sits. For a voice clip, only the windows where someone speaks
count. Then, from the first music file and the voice clips, it prints how far the
music sits under the voice at the player's two volumes.

  python3 levels.py talk/music.m4a talk/voice/start-0.m4a talk/zh/voice/start-0.m4a
  python3 levels.py --mus 0.2 --duck 0.1 talk/music.m4a talk/voice/*-0.m4a

Aim for the music about 15 dB(A) under the voice while it speaks, and about 9 dB(A)
under between clips. Energy below 150 Hz is lost on laptop speakers, and energy at
150-400 Hz is covered by the voice, so most of a loop's sound should sit above 400 Hz.
Runs under the Kokoro venv in ~/.local/share/tts (it needs numpy).
"""
import os, sys

TTS = os.path.expanduser("~/.local/share/tts")
try:
    import numpy as np
except ImportError:
    py = os.path.join(TTS, "venv/bin/python")
    os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])

import argparse, struct, subprocess, tempfile

ap = argparse.ArgumentParser()
ap.add_argument("files", nargs="+", help="m4a or wav files; names under voice/ are read as voice")
ap.add_argument("--mus", type=float, default=0.2, help="the player's music volume between clips")
ap.add_argument("--duck", type=float, default=0.1, help="the player's music volume while the voice speaks")
args = ap.parse_args()
SR = 44100


def load(f):
    with tempfile.TemporaryDirectory() as t:
        w = os.path.join(t, "x.wav")
        subprocess.run(["afconvert", "-f", "WAVE", "-d", "LEI16@%d" % SR, "-c", "1", f, w], check=True)
        b = open(w, "rb").read()
        i = 12
        while i < len(b):
            cid, sz = b[i:i + 4], struct.unpack("<I", b[i + 4:i + 8])[0]
            if cid == b"data":
                return np.frombuffer(b[i + 8:i + 8 + sz - sz % 2], dtype="<i2").astype(float) / 32768
            i += 8 + sz + sz % 2


def a_weight(f):
    f2 = f * f
    ra = 12194 ** 2 * f2 ** 2 / ((f2 + 20.6 ** 2) * np.sqrt((f2 + 107.7 ** 2) * (f2 + 737.9 ** 2)) * (f2 + 12194 ** 2))
    return ra * 10 ** (2.0 / 20)


def level(x, speech):
    fr = np.fft.rfftfreq(len(x), 1 / SR)
    y = np.fft.irfft(np.fft.rfft(x) * a_weight(fr), len(x))
    if speech:
        w = SR // 20
        e = np.array([np.mean(y[k:k + w] ** 2) for k in range(0, len(y) - w, w)])
        y2 = np.mean(e[e > e.max() * 10 ** -3.5])
    else:
        y2 = np.mean(y ** 2)
    return 10 * np.log10(y2)


def bands(x):
    p = np.abs(np.fft.rfft(x)) ** 2
    fr = np.fft.rfftfreq(len(x), 1 / SR)
    edges = [(0, 150), (150, 400), (400, 1000), (1000, 3000), (3000, SR // 2)]
    return "  ".join("%d-%dHz %2.0f%%" % (a, b, 100 * p[(fr >= a) & (fr < b)].sum() / p.sum()) for a, b in edges)


music, voices = None, []
for f in args.files:
    speech = "voice" in os.path.relpath(f).split(os.sep)[:-1]
    x = load(f)
    lv = level(x, speech)
    print("%-28s %6.1f dB(A)   %s" % (os.path.relpath(f)[-28:], lv, bands(x)))
    if speech:
        voices.append(lv)
    elif music is None:
        music = lv
if music is not None and voices:
    v = min(voices)
    for name, g in (("while the voice speaks", args.duck), ("between clips", args.mus)):
        print("music %s (volume %.2f): %.1f dB(A) under the quietest voice"
              % (name, g, v - (music + 20 * np.log10(g))))
