# Checklists to run before showing the author anything

The author reviews by playing the whole talk and reading the whole article, so do the same first. Each item below is something the first talk got wrong at least once.

## Story

- [ ] **The line reads straight through.** List each scene's title and the first sentence of its narration, and read the list in order. It should read as the argument, with no jumps.
- [ ] **Nothing is used before it is defined**, whether a concept, a term or a component.
- [ ] **An abstract premise comes with the experience behind it.** Before "when a design doesn't fit, the struggle shows", say what everyone has felt: when you write the code yourself, you feel whether the design fits.
- [ ] **Every claim has its reason nearby.** When a reader would ask "why?", the answer comes within a sentence or two.
- [ ] **Every turn names what breaks.** No bare "but", and no "here's the catch".
- [ ] **The key insight is one sentence**, said plainly, and nothing next to it dilutes it.
- [ ] **The parallel parts are the same kind of thing**, all practices (or all of one kind), on the same dimension. Each comes from a known technique named professionally.
- [ ] **Every insight has its deeper reason** in the talk. None comes out of nowhere.
- [ ] **One running example is used throughout.** No example needs the author's private context.
- [ ] **On the stage, the right way is shown wherever the contrast is the point.**
- [ ] **In an overview, each abstract question is followed at once by a one-line case from the running example.**
- [ ] **Each part's question states the risk**, not the technique's own operation.
- [ ] **Every act boundary is bridged:** the act ends on its root cause, and the next act opens as the answer.
- [ ] **A reader would want to keep going after scene 1**, and the end answers the opening question.
- [ ] **The author's key terms are used in the sense they confirmed.**
- [ ] **No absolutes the author can't defend.** Check each with "is this always true?".
- [ ] **No digressions:** history, citations, future work, a second unresolved problem.
- [ ] **Everything the talk says the tool does, the tool does.**
- [ ] **No private names:** no projects, labs, meetings or people.
- [ ] **The talk keeps the meaning of each of the outline's points.**
- [ ] **The takeaways are three**, each a claim plus how, together covering the insights.

## Stage

- [ ] **Each scene has one main picture.** Side material is small.
- [ ] **On-screen text is labels, key numbers, and at most one short line per element.**
- [ ] **No sentence on the stage repeats the narration.**
- [ ] **The mechanism is animated**, not described in text.
- [ ] **Each step changes what its narration names**, in the order the narration says it.
- [ ] **Before/after pairs share a layout.**
- [ ] **No text is hidden under the subtitles** (keep it above y ≈ 560). Nothing overlaps, no band is empty, and nothing is left over from an earlier step.
- [ ] **Colors keep their meaning across scenes.** No "green" in any wording.
- [ ] **It holds at phone width and in full screen.**
- [ ] **A viewer would get each scene without the narration**, or at least wouldn't be misled by it. If it is too abstract, draw the concrete thing.

## Narration

- [ ] **Every sentence carries the point.** Delete any sentence that could go without losing a step.
- [ ] **No filler, no promotional lines, no idioms**, and no wording that's too casual for the key lines.
- [ ] **Each scene's first sentence connects to the last scene.** Structure is signposted, and examples are marked as examples.
- [ ] **Read the subtitles in sequence.** Nothing appears abruptly.
- [ ] **Each step is 1–4 sentences.**
- [ ] **The music can be heard under the voice.** `levels.py` puts it about 15 dB(A) under the voice while it speaks, with most of its sound above 400 Hz. Step by hand once and check that the music starts.
- [ ] **`make_voice.py` has been run** (and `--lang zh`). Clip count equals step count, and the changed scenes have been listened to.

## Article

- [ ] **The article is written for reading**, not pasted from the narration.
- [ ] **Each section goes problem → solution**, and each paragraph develops its first sentence.
- [ ] **Each point is motivated first**, and its example is short, with only the helpful details.
- [ ] **No choppy fragments, no heavy "which is that" clauses, no rare words**, and no "both" or "this" whose referent is out of view.
- [ ] **No section opens with a question.** The section titles name the point.
- [ ] **Highlighted insights are real, specific to the new setting, and readable alone** when skimmed.
- [ ] **There are a few still figures, each with a caption**, each placed after the paragraph it illustrates.
- [ ] **The project link is placed where the tool comes in**, and the article ends with three takeaways.
- [ ] **Each substantive section has one highlighted point**, and each parallel part has one figure.

## Chinese

- [ ] **Everything is rewritten, not translated.** No 翻译腔 (translationese). Sentences connect.
- [ ] **Engineering terms stay in English**, consistently.
- [ ] **Stage labels are short**, and the key lines are short.
- [ ] **`make_zh.py` prints no warnings.** Every "not found" or step mismatch has been explained or fixed.
- [ ] **The Chinese page has been opened in the browser pane.** The language switch, the keyboard hint and the clips all work.

## Before publishing

- [ ] **The whole talk has been played through in the browser pane**, in both languages, with no console errors.
- [ ] **It has been stepped through by hand too.** Next goes one sentence at a time, lands at the start of each sentence, and moves on to the next step after a clip's last sentence.
- [ ] **The URL slug names the topic.**
- [ ] **Only the talk's files and its sources are staged.** Nothing from others' uncommitted work, and no build files.
- [ ] **The author has said to commit and push.**
- [ ] **After the deploy, the English page, the `zh/` page and one clip have been checked live.**
