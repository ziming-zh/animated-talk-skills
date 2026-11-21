# Narration, voice, subtitles, music

Each step's narration is one string in the scene's `steps` array. The voice reads it, the subtitles show it on the picture, and screen readers get it in full.

## 1. How narration should sound

- **Spoken, plain, precise.** Short sentences, everyday words. "把所有旁白都改得口语一点" (make all the narration more conversational), but the key lines stay exact. "No crash will tell you, so you have to ask" was too casual for the key insight. The fix was to state what to do: check proactively.
- **Every sentence carries the point.** If a sentence could be deleted without losing a step of the argument, delete it. Cut lines like "and it's a sneaky one", "That's what makes systems research hard. It's also what makes it fun.", "Here's the catch."
- **Name the point outright.** "That's a silent failure: every check passes, yet the abstraction doesn't fit the problem." Not "So this abstraction, from the very beginning, …". On "wrong" versus "improper", see `story.md` §7.
- **Nothing promotional.** "Build the alarms in, so the first wrong turn rings a bell" was rejected as "too promotional, no substance". Say what is done and why.
- **No idioms or cute phrasing.** "There goes the deadline", "looks great on paper", "the same year can try seven", "room to change course" were all rejected. Say the plain fact: "you're rewriting most of the system, with old and new code that don't fit together for a long while."
- **Precise words for a technical audience.** "Code is cheap" lacked a researcher's rigor. "Implementation got cheaper" kept it.
- **Not too long.** Keep each step to 1–4 sentences. When the author says "太长了", cut the clause that explains what the picture already shows.

## 2. Linking scenes

- The first sentence of a scene connects to the last scene: "Now zoom out." "That vision rests on one assumption." "So check proactively, with three questions systems already ask."
- Signpost structure out loud: "Practice one: …", "First … Second … Third …", "Here's that thin spec at work on the cache."
- Mark examples as examples: "Say you guess, before each task, how much work it will take." The author couldn't tell an earlier version was an example.
- Don't introduce a frame the listener doesn't have ("The first question asks…" when no question was posed).
- When simplifying the narration, keep the logic and the story line intact ("narration 如果要简化仍然要保证叙述逻辑和故事线通顺").

## 3. Pronunciation

`make_voice.py` rewrites screen text into spoken text before synthesis. Its default rules turn `v2` into "version 2", `AGENTS.md` into "agents dot M D", spell out `PhD`/`GPU`/`GCC`, and turn parentheses into commas. Add the talk's own terms with `--say say.json`, for example `[["\\bThinSpec\\b", "Thin Spec"], ["\\bUVM\\b", "U V M"]]`. Listen to any clip whose text has an acronym, a version, a file name or a number with a unit.

## 4. Voices: what was tried and chosen

| Language | Tried | Verdict |
|---|---|---|
| English | macOS `say` (Samantha) | robotic |
| English | macOS Premium "Ava" | acceptable, not natural enough |
| English | Kokoro `am_michael` | "sounds old, not lively" |
| **English** | **Kokoro `af_bella`, speed 1.1** | **chosen: modern, lively** |
| Chinese | Kokoro `zf_xiaoxiao` | wrong tones |
| Chinese | CosyVoice 2 (0.5B, zero-shot) | "too childish, not enough depth" |
| Chinese | more mature female neural voices | tried; the author then asked for a male voice |
| **Chinese** | **edge-tts `zh-CN-YunjianNeural`, rate −4%** | **chosen: mature male** |

The author did not want a clone of their own voice, just a recent, very natural one. Kokoro runs locally.

edge-tts sends the text to Microsoft's read-aloud service, so it suits public narration only. That service is not an officially licensed API; the same voices are sold as Azure Speech. Tell the author this when choosing it.

Render all clips of one language with one engine and voice. In the first talk, one run on the wrong engine left six Chinese clips in an old voice, and all 72 had to be redone. `make_voice.py` now defaults Chinese to edge, and its cache key includes the engine and voice.

## 5. Subtitles

- Draw them on the picture, at the bottom, one short line at a time. Don't put the moving narration under the stage: "图又在动，下面的字又在动，非常容易 feel distracted" (the picture moves and the text below moves too, which is very distracting).
- The player splits a step's text at sentence ends, then at commas or colons near the middle. Lines run up to about 105 Latin or 44 CJK characters. Each line's time is weighted by length, with CJK characters weighted heavier, and synced to the clip's playback. `C` toggles subtitles.
- Read the subtitles in sequence, as a reader would. Abrupt jumps ("the question is…" out of nowhere) show up there first.

## 6. Music

`make_music.py` synthesizes an original, calm, seamless ambient loop (pads, sparse bells, low bass, reverb), with no samples and no licensing question. The player plays it only during autoplay with sound on, at volume 0.15, and dips it to 0.06 while the voice speaks.

## 7. After every narration change

1. Run `make_voice.py` for English, and `make_zh.py` then `make_voice.py --lang zh` for Chinese. Only changed clips are remade, and clips for removed steps are deleted.
2. Check that the clip count equals the step count (the script prints both).
3. Play the changed scenes in the browser pane.

The author treats this as part of the edit: "语音对应更新了吧" (the voice has been updated to match, right?).

## 8. Autoplay timing

With voice, the player advances when a clip ends. The pause is 0.65 s between steps and 1.3 s between scenes. Without voice, each step stays up for 4.2–11.5 s, scaled to its text length. A tick bar under the stage shows the time left.
