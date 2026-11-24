# Narration, voice, subtitles, music

Each step's narration is one string in the scene's `steps` array. The voice reads it, the subtitles show it on the picture, and screen readers get it in full.

## 1. How narration should sound

- **Spoken, plain, precise.** Use short sentences and everyday words. Make the narration conversational, but keep the key lines exact. If the key insight sounds too casual, replace it with a plain statement of what to do.
- **Every sentence carries the point.** If a sentence could be deleted without losing a step of the argument, delete it. Lines like "and it's a sneaky one" and "here's the catch" go.
- **Name the point outright.** "That's a ⟨term⟩: ⟨what it means here⟩." Don't circle up to it with "So this, from the very beginning, …". On strong words like "wrong", see `story.md` §7.
- **Nothing promotional.** A stirring line with no mechanism is cut. Say what is done and why.
- **No idioms or cute phrasing.** "There goes the deadline" and "looks great on paper" make the listener decode. Say the plain fact instead.
- **Precise words for a technical audience.** "Code is cheap" overstates; "implementation got cheaper" says what is true.
- **Not too long.** Keep each step to 1–4 sentences. When a step is too long, cut the clause that explains what the picture already shows.

## 2. Linking scenes

- **The first sentence of a scene connects to the last scene:** "Now zoom out." "That plan rests on one assumption." "So check for it early."
- **Signpost the structure out loud:** "Part one: …", "First … Second … Third …", "Here's that rule at work on the example."
- **Mark examples as examples:** "Say you …", "Take a …". A listener can't tell an unmarked example from a claim.
- **Don't introduce a frame the listener doesn't have**, such as "The first question asks…" when no question was posed.
- **When simplifying the narration, keep the logic and the story line intact.**

## 3. Pronunciation

`make_voice.py` rewrites screen text into spoken text before synthesis. Its default rules:
- `v2` becomes "version 2";
- `PhD`, `GPU` and `GCC` are spelled out;
- parentheses become commas.

Add the talk's own terms with `--say say.json`, for example `[["\\bKV\\b", "K V"], ["\\bNVMe\\b", "N V M E"]]`. Listen to any clip whose text has an acronym, a version, a file name or a number with a unit.

## 4. Voices

| Language | Default | Notes |
|---|---|---|
| English | Kokoro `af_bella`, speed 1.1 | modern and lively; runs locally |
| Chinese | edge-tts `zh-CN-YunjianNeural`, rate −4% | a mature male voice |

Choose the voice by listening, against the weight of the content:
- A robotic, old-sounding or childish voice makes a serious talk feel less serious.
- A voice with wrong tones (common for Chinese in small local models) is unusable however natural it otherwise sounds.
- Play the author two or three samples of the same sentence, and let them pick.

Kokoro also has other voices, and `make_voice.py` supports CosyVoice 2 and macOS `say`. These are alternatives if the author wants a different sound.

edge-tts sends the text to Microsoft's read-aloud service, so it suits public narration only. That service is not an officially licensed API; the same voices are sold as Azure Speech. Tell the author this when choosing it.

**Render all clips of one language with one engine and voice.** A run with the wrong engine leaves some clips in another voice, and a listener hears the switch at once. `make_voice.py` defaults Chinese to edge, and its cache key includes the engine and voice.

## 5. Subtitles

- **Draw them on the picture**, at the bottom, one short line at a time. Don't put the moving narration under the stage. When the picture moves and the text below it moves too, the viewer can't follow both.
- **How lines are split and timed.** The player splits a step's text at sentence ends, then at commas or colons near the middle. Lines run up to about 105 Latin or 44 CJK characters. Each line starts at a pause in the voice (see `engine.md` §5). `C` toggles subtitles.
- **Read the subtitles in sequence**, as a viewer would. Abrupt jumps ("the question is…" out of nowhere) show up there first.

## 6. Music

`make_music.py` synthesizes an original, calm, seamless ambient loop (pads, sparse bells, low bass, reverb). It uses no samples, so there is no licensing question.

The player starts the music with the first voice clip, whether the talk plays itself or the reader steps through by hand. It plays at volume 0.2 between clips and dips to 0.1 while the voice speaks. When the reader steps by hand, it fades out about 9 s after the last clip ends.

**The music must be heard on laptop speakers.** Laptop speakers barely play below 150 Hz, and the voice covers 150–400 Hz. A loop whose sound is mostly low pads and bass disappears under the narration, even when it plays. Put the melody and an upper layer of the pad above 400 Hz, and keep the bass quiet.

Check every new loop with `scripts/levels.py`. Aim for:
- about 15 dB(A) under the voice while it speaks;
- about 9 dB(A) under the voice between clips;
- most of the sound above 400 Hz.

## 7. After every narration change

1. Run `make_voice.py` for English. For Chinese, run `make_zh.py`, then `make_voice.py --lang zh`. Only changed clips are remade, and clips for removed steps are deleted.
2. Check that the clip count equals the step count (the script prints both).
3. Play the changed scenes in the browser pane.

The author treats this as part of the edit: the voice always matches the text.

## 8. Autoplay timing

With voice, the player advances when a clip ends. The pause is 0.65 s between steps and 1.3 s between scenes. Without voice, each step stays up for 4.2–11.5 s, scaled to its text length. A tick bar under the stage shows the time left.
