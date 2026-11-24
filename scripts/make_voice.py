#!/usr/bin/env python3
"""Make the narration clips for an animated talk.

Reads every scene's `steps` from the page and speaks each one, writing
voice/<scene-id>-<step>.m4a next to the page. A clip is remade only when its
text, engine, voice or speed changed, and clips for steps that no longer exist
are removed. Run it after every narration edit.

  python3 make_voice.py --page path/to/talk/index.html                 # English: Kokoro af_bella at 1.1x
  python3 make_voice.py --page path/to/talk/index.html --lang zh --engine edge   # Chinese: zh/index.html, YunjianNeural -4%
  python3 make_voice.py --page ... --say say.json   # extra pronunciations: [["\\\\bUVM\\\\b", "U V M"], ...]
  python3 make_voice.py --page ... --force          # remake every clip

Engines (all set up under ~/.local/share/tts; this script re-runs itself in the right venv):
  kokoro    kokoro-onnx in venv/, with kokoro-v1.0.onnx and voices-v1.0.bin. English default.
            af_bella at 1.1 was chosen as lively and modern; am_michael sounded old.
  edge      Microsoft neural voices through the edge-tts package in edge-venv/. Chinese default:
            zh-CN-YunjianNeural at -4% (a mature male voice). English: en-US-AndrewNeural.
  cosyvoice CosyVoice 2 0.5B in cv-venv/ and cosyvoice/, cloning a short prompt clip. Sounded too young.
  say       macOS voices; download Premium ones in System Settings > Accessibility > Spoken Content.
Kokoro's Chinese voice (zf_xiaoxiao) gets tones wrong; use edge for Chinese.
The scene format the script looks for:  id: "x", act: N, title: "...",\n  steps: [...],\n  svg()
"""
import argparse, hashlib, json, os, re, subprocess, sys, tempfile

TTS = os.path.expanduser("~/.local/share/tts")

# how a word on screen should be said; add the talk's own terms with --say
SAY = [
    (r"\bv(\d)\b", r"version \1"),
    (r"\bPhD\b", "P H D"),
    (r"\bGPU\b", "G P U"),
    (r"\bGCC\b", "G C C"),
    (r"\(([^)]*)\)", r", \1,"),
]
SAY_ZH = [
    (r"\bv(\d)\b", r"版本\1"),
    (r"\bGPU\b", "G P U"),
    (r"\bGCC\b", "G C C"),
    (r"(\d+)%", r"百分之\1"),
    (r"(\d+) 到 (\d+)", r"\1到\2"),
]


def spoken(text, rules):
    for a, b in rules:
        text = re.sub(a, b, text)
    return text


def steps(src):
    out = []
    for m in re.finditer(r'id: "([^"]+)", act: \d+, title: [^\n]*\n  steps: (\[.*?\]),\n  svg\(\)', src, re.S):
        for k, t in enumerate(json.loads(m.group(2))):
            out.append((f"{m.group(1)}-{k}", t))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", required=True, help="the English page; --lang zh uses zh/index.html next to it")
    ap.add_argument("--engine", choices=["kokoro", "say", "cosyvoice", "edge"], default=None)
    ap.add_argument("--voice", default=None)
    ap.add_argument("--rate", type=float, default=None, help="kokoro/cosyvoice speed, say words per minute, edge percent change")
    ap.add_argument("--say", default=None, help="a JSON list of [regex, replacement] pronunciations")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--lang", choices=["en", "zh"], default="en")
    a = ap.parse_args()
    page = os.path.abspath(a.page)
    if a.lang == "zh":
        page = os.path.join(os.path.dirname(page), "zh/index.html")
        a.engine = a.engine or "edge"
    a.engine = a.engine or "kokoro"
    out = os.path.join(os.path.dirname(page), "voice")
    cache = os.path.expanduser("~/.cache/animated-talk/%s-%s.json" % (hashlib.sha1(page.encode()).hexdigest()[:12], a.lang))
    rules = list(SAY_ZH if a.lang == "zh" else SAY)
    if a.say:
        rules += [tuple(p) for p in json.load(open(a.say, encoding="utf-8"))]

    if a.engine == "edge":
        a.voice = a.voice or ("zh-CN-YunjianNeural" if a.lang == "zh" else "en-US-AndrewNeural")
        a.rate = a.rate if a.rate is not None else -4
        exe = os.path.join(TTS, "edge-venv/bin/edge-tts")
        if not os.path.exists(exe):
            sys.exit("edge-tts is not set up in " + TTS + " (python3 -m venv edge-venv && edge-venv/bin/pip install edge-tts)")

        def render(line, path):
            subprocess.run([exe, "--voice", a.voice, "--rate=%+d%%" % int(a.rate), "--text", line,
                            "--write-media", path], check=True, capture_output=True)
    elif a.engine == "cosyvoice":
        a.voice = a.voice or "zero_shot_prompt"
        a.rate = a.rate or 1.0
        render = cosyvoice_render(a)
    elif a.engine == "kokoro":
        a.voice = a.voice or ("zf_xiaoxiao" if a.lang == "zh" else "af_bella")
        a.rate = a.rate or (1.05 if a.lang == "zh" else 1.1)
        try:
            import kokoro_onnx  # noqa: F401
        except ImportError:
            py = os.path.join(TTS, "venv/bin/python")
            if not os.path.exists(py):
                sys.exit("kokoro is not set up in " + TTS)
            os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])
        from kokoro_onnx import Kokoro
        import soundfile
        kk = Kokoro(os.path.join(TTS, "kokoro-v1.0.onnx"), os.path.join(TTS, "voices-v1.0.bin"))
        if a.voice not in kk.get_voices():
            sys.exit(f'kokoro has no voice "{a.voice}"')

        def render(line, path):
            audio, sr = kk.create(line, voice=a.voice, speed=a.rate, lang="cmn" if a.lang == "zh" else "en-us")
            soundfile.write(path, audio, sr)
    else:
        a.voice = a.voice or ("Tingting" if a.lang == "zh" else "Samantha")
        a.rate = a.rate or (190 if a.lang == "zh" else 178)
        check_say(a.voice)

        def render(line, path):
            subprocess.run(["say", "-v", a.voice, "-r", str(int(a.rate)), "-o", path, line], check=True)
    run(a, render, page, out, cache, rules)


CV_PROMPTS = {"zero_shot_prompt": "希望你以后能够做的比我还好呦。"}


def cosyvoice_render(a):
    """CosyVoice 2 (0.5B), cloning the voice of a short prompt clip in its asset/ folder."""
    cv = os.path.join(TTS, "cosyvoice")
    try:
        import torch  # noqa: F401
    except ImportError:
        py = os.path.join(TTS, "cv-venv/bin/python")
        if not os.path.exists(py):
            sys.exit("CosyVoice is not set up in " + TTS)
        os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])
    sys.path[:0] = [cv, os.path.join(cv, "third_party/Matcha-TTS")]
    here = os.getcwd()
    os.chdir(cv)
    from cosyvoice.cli.cosyvoice import AutoModel
    import torch, torchaudio
    m = AutoModel(model_dir=os.path.join(TTS, "cv-models/CosyVoice2-0.5B"))
    os.chdir(here)
    prompt_wav = os.path.join(cv, "asset", a.voice + ".wav")

    def render(line, path):
        parts = [j["tts_speech"] for j in m.inference_zero_shot(line, CV_PROMPTS[a.voice], prompt_wav, stream=False, speed=a.rate)]
        torchaudio.save(path, torch.cat(parts, dim=1), m.sample_rate)
    return render


def check_say(voice):
    # `say` silently falls back to the default voice for a name it does not have
    listing = subprocess.run(["say", "-v", "?"], capture_output=True, text=True).stdout.splitlines()
    have = [re.split(r"\s{2,}", l)[0] for l in listing]
    if voice not in have:
        sys.exit(f'voice "{voice}" is not installed. Installed voices:\n  ' + "\n  ".join(have))


def run(a, render, page, out, cache_path, rules):
    os.makedirs(out, exist_ok=True)
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    try:
        cache = json.load(open(cache_path))
    except (OSError, ValueError):
        cache = {}
    todo = steps(open(page, encoding="utf-8").read())
    if not todo:
        sys.exit("no steps found in " + page)
    keep = set()
    with tempfile.TemporaryDirectory() as tmp:
        for name, text in todo:
            line = spoken(text, rules)
            key = hashlib.sha1(f"{a.engine}|{a.voice}|{a.rate}|{line}".encode()).hexdigest()
            dst = os.path.join(out, name + ".m4a")
            keep.add(name + ".m4a")
            if not a.force and cache.get(name) == key and os.path.exists(dst):
                continue
            raw = os.path.join(tmp, name + {"say": ".aiff", "edge": ".mp3"}.get(a.engine, ".wav"))
            render(line, raw)
            subprocess.run(["afconvert", "-f", "m4af", "-d", "aac", "-c", "1", "-b", "48000", raw, dst], check=True)
            cache[name] = key
            print("made", name)
    for f in os.listdir(out):
        if f.endswith(".m4a") and f not in keep:
            os.remove(os.path.join(out, f))
            print("removed", f)
    json.dump(cache, open(cache_path, "w"), indent=1)
    print(len(todo), "clips in", out)


if __name__ == "__main__":
    main()
