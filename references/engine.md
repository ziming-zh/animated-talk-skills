# The page engine and the build scripts

The whole talk is a single HTML file, with no build step and no framework:
- a scene engine that draws SVG;
- a player with voice, subtitles, music, a scene rail and keyboard controls;
- the article, kept as JSON inside the page.

Start from `assets/template/index.html`. The first talk's page is the full worked example: `~/Desktop/ziming-zh.github.io/static/blog/agentic-research-system-design/index.html`, with 23 scenes.

## 1. Page layout

```
<head>      title, description and og meta, Google Fonts (Bricolage Grotesque, Inter, JetBrains Mono, Newsreader, IBM Plex Mono, Noto Serif SC)
<style>     color tokens on :root, a dark theme under prefers-color-scheme, stage, player, article, full-screen styles
<header>    ← home link · date · language switch (EN / 中文)
<section.player>  rail of scenes · stage (tick bar, act flash, click hint, subtitle line) · caption (eyebrow, title) · controls
<div.after>  <details> "Read it as an article" holding <script type="application/json" id="article"> · footer links
<script>    SVG helpers · the story (ACTS, RAIL, PARTS, chapter(), scenes) · the player
```

## 2. A scene

The build scripts find scenes by exactly this shape, so keep it:

```js
scene({
  id: "tangle", act: 4, title: "Agents file code by when it runs",
  steps: [
    "Narration for step 0.",
    "Narration for step 1."
  ],
  svg() {
    let s = "";
    s += B(120, 250, 220, 90, "Input", { k: "card", s: 0, fx: "pop" });
    return s;
  }
});
```

The fields:
- `id`: names the voice clips (`voice/<id>-<k>.m4a`) and the deep link (`#id`). A scene id that starts with `practice-` doesn't flash the act name, because a chapter card already shows it.
- `act`: an index into `ACTS` (full names, shown as the eyebrow and in the act flash) and `RAIL` (short names shown above the stage).
- `title`: shown under the stage. Make it state the claim.
- `steps`: one narration string per step. The number of steps is the number of beats in the scene.
- `svg()`: returns SVG markup for a 1200 × 675 box. Keep content above y ≈ 560, because the subtitles cover the bottom band.

## 3. Step attributes: every helper takes an options object `o`

| Option | Effect |
|---|---|
| `s: k` | Visible from step k on |
| `x: k` | Hidden from step k on (with `s`, the element shows during [s, x)) |
| `d: sec` | Delay before the element enters at its step; orders the beat inside a step |
| `fx` | Entrance: `"rise"`, `"pop"`, `"draw"` (strokes draw in; paths only), `"grow-x"`, `"grow-y"`. With no fx, a plain fade |
| `dur`, `tt` | Duration of the draw, or of the transition |
| `m: k, mx, my, ms, md` | From step k, move by (mx, my), scale by ms, after a delay of md seconds |
| `count: n, from, fmt: "{}×", cdur` | A number that counts from `from` to n when it shows |
| `type: true, tdur` | Text that types itself in |
| `act: "play"` | Clicking it starts autoplay (`"replay"` restarts from the beginning) |
| `c`, `st` | Extra classes (`"spin"`, `"cta"`); extra inline style |

`G(inner, o)` groups elements. When a group both fades and moves, `G` splits it into two nested groups so the two transforms don't fight. To scale a whole drawing, wrap it: ``s += `<g transform="translate(-300 -92) scale(1.25)">${inner}</g>` ``.

## 4. Helpers

| Helper | Draws | Notable options |
|---|---|---|
| `T(x, y, str \| [lines], o)` | text | `size`, `lh`, `f: "disp" \| "mono"`, `col`, `a: "middle" \| "end"`, `w` (weight), `ls`, `it`, `raw` |
| `B(x, y, w, h, label \| [lines], o)` | a box with a centred label | `k` (kind), `r`, `size`, `sub` (a smaller second label), `ss`, `a: "start"`, `pad`, `dash`, `f`, `sf`, `extra` |
| `P(d, o)` / `L(x1, y1, x2, y2, o)` | a path or line | `col`, `sw`, `dash`, `fx: "draw"` |
| `AR(x1, y1, x2, y2, o)` / `ARC([x1, y1, c1x, c1y, c2x, c2y, x2, y2], o)` | an arrow or curved arrow; draws in, and the head follows | `col`, `sw`, `hs`, `dash` |
| `CK(x, y, z, col, o)` / `XX(...)` | a check mark or a cross | `sw` |
| `circ(cx, cy, r, o)`, `badge(cx, cy, r, "ok" \| "bad", o)` | a circle; a filled disc with a check or a cross | |
| `cycle(cx, cy, r, col)` | a round arrow, for "it changes" (wrap it in `G(..., {c: "spin"})`) | |
| `warn(cx, cy, z, col)` | a warning triangle | |
| `codeWall(x, y, w, h, seed, rows)` | a minimap of a large file | |
| `pointer(x, y)` | a mouse cursor | |
| `chapter(n)` | the chapter card for `PARTS[n]` | |

Box kinds (`k`): `card`, `panel`, `core`, `design`, `code`, `term`, `tile`, `ghost`, `blue`, `green`, `orange`, `red`, `amber`, `solid-blue`, `solid-ink`, `solid-amber`, `ring-red`, `ring-amber`.

Colors (`col`), each with a dark-mode value:
- base colors: `ink`, `ink2`, `ink3`, `line`, `line2`, `paper`, `fill`;
- `blue`, `green`, `red`, `orange` and `amber`, each with `-ink` and `-soft` variants;
- code colors: `code-bg`, `code-fg`, `code-dim`, `code-kw`, `code-str`, `code-fn`, `code-warn`, `code-bad`.

## 5. The player

- **Navigation:**
  - →, Space, Enter or a click: the next sentence. Inside a step's clip, the voice jumps to the start of the next subtitle line; after the last line, the next step.
  - ←: back one sentence, then the previous step.
  - Home / End: first / last step.
  - `P`: play / pause.
  - `M`: sound.
  - `C`: subtitles.
  - `F`: full screen.
  - Clicking a segment of the rail jumps to that scene.
  - `#scene-id` in the URL opens that scene.
- **Autoplay:** each step plays its clip, then waits 0.65 s (1.3 s at the end of a scene) and advances. With no voice, a step stays up 4.2–11.5 s, scaled to its text. The next clip is preloaded.
- **Subtitles:** drawn on the stage, one sentence (or half of a long one) at a time. Each line starts at a pause in the voice: the player decodes the clip, finds its pauses, and matches one pause to each line break, in order, preferring long pauses near the line's share of the text. Until the clip is decoded, the share of the text alone sets the times. Autoplay still advances by step. The full narration also goes to a hidden live region for screen readers.
- **Music:** `music.m4a` through WebAudio, with sound on. It starts with the first voice clip, under autoplay or when stepping by hand, and dips while the voice speaks (volume 0.1, and 0.2 between clips). Stepping by hand, it fades out 9 s after the last clip.
- **Preferences:** sound and subtitles on/off are kept in `localStorage`. With `prefers-reduced-motion`, steps appear without animation.
- **Phones:** below 720 px the rail shows only the current act, and a hint suggests turning the phone sideways.

## 6. The article inside the page

`<script type="application/json" id="article">` holds `{"summary", "sections": [{"h", "p": [...], "fig"}]}`. An item in `p` is one of:
- a string (a paragraph);
- `{"insight": ...}`;
- `{"list": [...]}`;
- `{"link": {"href", "text"}}`.

`fig: {scene, step, after, caption}` draws that scene, frozen at `step`, after item `after`. Figures are drawn the first time the reader opens the article.

Keep the article in `article/en.json` and insert it with `scripts/make_article.py`. Don't edit the JSON inside the page by hand.

## 7. Scripts

| Script | Use |
|---|---|
| `make_voice.py --page talk/index.html [--lang zh] [--engine kokoro\|edge\|cosyvoice\|say] [--voice] [--rate] [--say extra.json] [--force]` | Makes `voice/<id>-<k>.m4a` for every step, remaking only changed clips and removing stale ones. The cache lives in `~/.cache/animated-talk/`. |
| `make_article.py --page talk/index.html --article article/en.json` | Puts the article into the page |
| `make_zh.py --src talk/index.html --narr zh/narration.json --strings zh/strings.json --article article/zh.json` | Writes `talk/zh/index.html`; read its warnings |
| `make_music.py --out talk/music.m4a` | A 64 s seamless ambient loop |
| `levels.py talk/music.m4a talk/voice/start-0.m4a talk/zh/voice/start-0.m4a` | How far the music sits under the voice, and where its sound is |

The TTS engines live in `~/.local/share/tts`. The scripts re-run themselves under the right venv:

| Engine | Setup |
|---|---|
| Kokoro | `venv/` with kokoro-onnx and soundfile, plus `kokoro-v1.0.onnx` and `voices-v1.0.bin` |
| edge-tts | `edge-venv/` |
| CosyVoice 2 | `cv-venv/` and `cosyvoice/`, with the model in `cv-models/CosyVoice2-0.5B` |

macOS `afconvert` encodes the m4a files. Use `make_music.py` and `levels.py` with the Kokoro venv, which has numpy.

The usual order after an edit:

```
make_article.py (if the article changed) → make_zh.py → make_voice.py → make_voice.py --lang zh
```

Python heredocs with Chinese text can fail with "Non-UTF-8 code". Write such edits to a .py file with `# -*- coding: utf-8 -*-` and run the file.

## 8. Previewing locally

- Serve the talk folder with `python3 -m http.server <port> --bind 127.0.0.1`, run in the background. First check the port is free (`lsof -iTCP:<port> -sTCP:LISTEN`): another project may already be serving on it.
- Open it in the browser pane. Add `?v=N` to bust the cache after edits.
- Step with the arrow keys and screenshot the steps that changed. Check the console for errors. Missing voice clips show up as 404s until `make_voice.py` runs.
- Check the layout at phone width with `resize_window` preset `mobile`. Reset it to `desktop` afterwards.
- **When the pane is hidden, CSS transitions and requestAnimationFrame freeze**, so screenshots show half-finished states. Before judging layout, inject a style that turns transitions off. **Reload the page when done:** the author watches the same pane. Once, they saw the leftover style and thought the animations had been removed.
- Open the article and check every figure and caption.

## 9. Deploying (a Hugo site on GitHub Pages)

- Files under `static/` are served as-is: `static/blog/<slug>/` becomes `/blog/<slug>/`.
- Pushing `main` runs the site's publish workflow. The page is live in about a minute.
- Check it live: `curl` the English page, the `zh/` page and one clip. Look for a string from the change you just made.
- Commit only the talk folder and its sources. If someone else has uncommitted work in the repository, stage the talk's paths alone, and leave their changes alone. For a file both of you touched, stage only your version with `git hash-object -w` and `git update-index --cacheinfo`. Keep local build files out: `public/`, `.hugo_build.lock`, `hugo_stats.json`.
- Don't commit or push without the author's word.
