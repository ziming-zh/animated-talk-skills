---
name: animated-talk
description: Turn a rough outline (a slide deck, talk notes, the argument of a paper or a project) into a narrated, animated web talk that readers can follow, with an SVG scene player, voice, subtitles and music, a separate article underneath for reading, and optionally a Chinese version. Use whenever the user wants to make an idea, a PPT or a research talk into an animation, an explainer video, an animated blog post or an interactive story. Also use when they give feedback on such a talk's story, slides, on-screen text, narration, voice, article or translation, or ask to publish one.
---

# Animated talk: from an outline deck to a talk people can follow

This skill takes a rough outline deck and makes:
- a narrated, animated talk that plays in the browser;
- an article under it for people who would rather read;
- optionally, a Chinese version of both.

The first talk made this way was "How to use agents to build complex systems":
- live at https://aisys.me/blog/agentic-research-system-design/;
- source in `~/Desktop/ziming-zh.github.io/`, under `static/blog/agentic-research-system-design/` and `tools/`.

It took about 210 rounds of the author's feedback to get there. This skill writes down what those rounds taught, so the next talk starts where that one ended.

Before writing any text, read `references/corrections.md`: it shows the author's corrections as before → after pairs.

## Why an outline is not yet a talk

An outline deck is the author's notes:
- claims in shorthand;
- examples only the author has the context for;
- jumps the author fills in when speaking.

Readers need something else:
- **One line of claims**, each motivated by the one before. The reader never has to ask "what is that?" or "why?".
- **One running example they already understand**, used everywhere.
- **Pictures that move to show the mechanism**, so the screen needs only labels.
- **A voice that says one point per sentence**, plainly.
- **A separate article for readers.** Watching and reading need different orders and different amounts of detail.

Drawing is the smaller part of the work. Most of it is finding the line, saying it plainly, and checking every sentence against it.

## What you make

```
talk/                       published folder, e.g. static/blog/<slug>/
  index.html                the page: player, styles, engine, scenes, narration (steps), article JSON inlined
  voice/<scene>-<k>.m4a     one narration clip per step
  music.m4a                 an original ambient loop
  zh/index.html, zh/voice/  the Chinese page: built by make_zh.py, never edited by hand
sources (kept out of the published folder, e.g. tools/):
  article/en.json, article/zh.json      the article in each language
  zh/narration.json, zh/strings.json    Chinese narration and stage text
```

**Start from the template.** Copy `assets/template/index.html`. It has the engine, the player, the styles and three demo scenes. The demo scenes show every animation feature.

The build scripts live in `scripts/`. `references/engine.md` documents the engine and the scripts.

## Principles

Every correction in the first talk came back to one of these. When unsure, check the work against them.

1. **One line.** The talk is a single chain of claims.
   - Each scene answers the question the last one raised.
   - Each turn says which assumption breaks.
   - Cut anything that is not on the line: history, citations, future work, a second example.
2. **Define before use, motivate before claim.**
   - A concept the talk depends on gets its own scene before it is used.
   - A claim comes with its reason in the next breath.
3. **One running example everyone knows.**
   - Pick a small, familiar system (the first talk used a cache in front of a database) and carry it through every part.
   - Never use examples that need the author's private context.
   - Never name internal projects, labs or people.
4. **The picture carries the mechanism. The voice carries the sentences. The screen carries labels.**
   - On screen: labels, key numbers, at most one short line.
   - If the screen needs a sentence, animate the thing instead.
5. **Every sentence carries the point.**
   - No filler, no throat-clearing ("here's the catch"), no promotional lines.
   - The key insight is said in one direct sentence.
6. **Say exactly what is true.**
   - No absolutes the author can't defend ("nobody has done this", "is just a guess", "must pass every case").
   - No idioms a listener has to decode.
   - No words that sound clever but don't say what you do.
7. **The video walks through; the article motivates, then zooms in.**
   - A viewer can follow a step-by-step example.
   - A reader needs the point first, then only the details that help.
8. **A correction is a pattern, not a line.** When the author flags one sentence, fix every sentence like it:
   - in the narration, on the stage and in the article;
   - in both languages;
   - then re-render the voice and check again.

   When the parallel items (the practices) are renamed or reframed, update every place that lists them: the overview, the chapter cards, the tool scene, the takeaways, the article and the Chinese strings.

## Workflow

Steps 1–3 settle the story before anything is drawn, which is the cheapest place to fix it. Steps 4–7 build and polish the talk. Steps 8–10 produce the article, the Chinese version and the publication.

### 1. Read the outline and set the frame

- **Extract the outline.** Write each slide's claim as one sentence. For a .pptx, unzip it and read the `<a:t>` runs of `ppt/slides/slideN.xml` in order.
- **Tag each item.** Mark it as a claim, evidence, an example, an internal detail or an open question.
- **Write down the author's intent:**
  - what the reader should believe, or do, at the end;
  - what each part of the outline is for.

  Keep that meaning when rewording. In the first talk, the outline's second "opportunity" was autoresearch: an agent's effort on a task reveals how hard the design makes it. A rewrite that drifted to "agents are fast" lost that meaning and had to be undone.
- **Write down the author's key terms and what each one means**, and confirm them before building on them. "Fine-grained" meant metrics tied to the design ("和底层设计相关的指标"), not per-workload metrics. The wrong reading had already reached the slides.
- **Note the outline's own transitions.** Reuse the ones that already work: "注意每页之间的 transition…还是挺清楚的" (mind the transitions between pages… they're actually quite clear).
- **Settle the frame:**
  - **Audience.** Keep it broad: "researchers building systems", not "systems PhD students".
  - **Where it lives**, and its URL slug. Name the topic; don't use a catchy phrase.
  - **Languages.**
- **List what needs private context**, and decide how to replace it:
  - internal project names → "a GPU memory system I'm building";
  - lab or meeting names, the author's name → remove;
  - domain-heavy examples → the running example.

### 2. Write the spine and show it before drawing

- **Write the spine** as 10–15 numbered sentences, one claim each. Each one links to the one before with *because*, *so*, *but* or *which raises the question*.
- **Use this arc.** It worked for the first talk:
  1. **Problem:** the problem the audience already feels, in their words.
  2. **Opportunity:** what changed that could help.
  3. **Twist:** the assumption the opportunity rests on, and why it breaks.
  4. **Key insight:** one sentence, named with a term the audience's field already uses.
  5. **Practices:** each starts from a well-known technique, says what changes now, and gives the practice.
  6. **Tool:** each practice becomes one mechanism.
  7. **Worked loop:** the whole loop run on the example.
  8. **Takeaways:** three of them, which organize the insights.
- **Choose the running example now**, and check that every practice can be shown on it.
- **Show the spine to the author and ask what is wrong.** In the first talk the author asked for this late ("把叙事线抽出来跟我讲一遍"). Do it first: a wrong link found here costs one sentence, not a scene.
- **Don't block on the answer.** Keep planning scenes while the author reads the spine, and fold their answer in. Hold off on drawing details until the spine is settled.

`references/story.md` covers this step in detail.

### 3. Plan scenes and steps

- **A scene is one idea**, in 1–5 steps. A step is one beat: one narration chunk plus one visual change.
- **Make a table:** act · scene id · title · one line per step · what moves.
  - The title states the scene's claim, e.g. "Agents file code by when it runs".
- **Give the concept everything depends on its own scene**, e.g. "What is an abstraction?". Center on it, then zoom out to the whole system.
- **Give each parallel part a chapter card:** "Part n of N · from ⟨technique⟩", the part's title, and the question it answers.
- **Overview scenes give the main items the most space.** In the first talk, the three practices first appeared small next to many other elements, and nobody could read them.
- **Don't spend several scenes on what the audience already knows.** One scene will do.

### 4. Build the scenes

- **Animate the mechanism as it happens.** In the first talk, the silent-failure scene showed this sequence:
  1. an agent patches one failing test after another, and each one passes;
  2. the camera zooms out to many components built the same way;
  3. the system meets more workloads, and every branch breaks somewhere.
- **Use one main picture.** The spec, legends and side notes go small at the side.
- **Keep text to a minimum.**
  - Labels and key numbers only.
  - At most one short line per element.
  - Sentences belong in the narration.
- **Draw before and after in the same layout**, so the change is the only difference.
  - Make the "before" convincingly messy.
  - When the contrast is the point, show the right way next to the wrong one.
- **Show parallel work in parallel.** Draw v1–v4 being built at once, not one after another.
- **Keep it lively.** The author wants motion: scene transitions, a camera push, typed and shaking elements. When a slide is too busy, cut text and side elements, not the animation.
- **Put the article's insights on the stage too.** If the article says "each ban records a property of the workload", show each property under its ban.
- **Check every step in the browser pane**, both at full size and at phone width.

Details are in `references/scenes.md` and `references/engine.md`.

### 5. Write the narration

- Write in a spoken register, with plain words.
  - Use 1–4 sentences per step.
  - The first sentence of each scene connects to the last scene.
- Signpost the structure: "Practice one: …", "First … Second … Third …", "Take a cache …", "Say you …".
- Say the key insight in one direct sentence, for example: "That's a silent failure: every check passes, yet the abstraction doesn't fit the problem."
- Avoid:
  - filler ("and it's a sneaky one");
  - "here's the catch";
  - promotional lines with nothing to think about;
  - idioms ("there goes the deadline");
  - slang where precision matters.

Details are in `references/narration.md`.

### 6. Voice, subtitles and music

- **Voice:** run `scripts/make_voice.py`.
  - English: Kokoro `af_bella` at 1.1.
  - Chinese: edge-tts `zh-CN-YunjianNeural` at −4%.
  - It remakes only the clips whose text changed.
  - Re-run it after every narration edit. The author assumes the voice matches the text.
- **Subtitles** are drawn on the picture, one short line at a time, timed to the voice.
  - Nothing that moves goes under the stage. Two moving things split attention.
- **Music:** run `scripts/make_music.py`.
  - It is original, so there is no licensing question.
  - It plays softly under autoplay only and dips while the voice speaks.

### 7. Review, then play the whole thing

- **Run the checklist** in `references/review.md`.
- **Answer the reader's questions yourself, scene by scene:**
  - "What is that?"
  - "Why?"
  - "How does it know?"
  - "So what?"
  - "Would someone get this without the narration?"
- **Play the whole talk in the browser pane** before showing it. The author reviews by watching all of it: "给我看一下效果" (show me how it looks), "重新完整播放一遍" (play the whole thing again).
- **Ask whether a reader would want to keep going** after the first scene, and whether the end answers the opening question.

### 8. Write the article

Write the article as a separate text for reading. Do not copy the narration into it. Details are in `references/article.md`. In brief:
- linear sections, each going problem → solution;
- each paragraph develops its first sentence;
- motivate first, then zoom into a short example;
- insights highlighted in an elegant serif, each readable on its own;
- a few still figures, each with a caption;
- the project link where the tool comes in, and three takeaways at the end.

### 9. The Chinese version

Rewrite the Chinese; don't translate it. Keep terms an engineer reads as-is in English. Build it with `scripts/make_zh.py`. Details are in `references/chinese.md`.

### 10. Publish

- **One folder per talk** under the site's static area, e.g. `static/blog/<slug>/`, with the build sources in `tools/`. Link the talk from the home page or blog list if asked.
- **The page description and the listing blurb state the insight, not the format.** For "An animated, narrated talk with a written version…", the author asked: "这个可以写的更有insight一点" (this could be written with more insight).
- **Commit only what belongs to the talk:**
  - the talk's folder and its sources;
  - never anyone else's uncommitted work in the same repository;
  - never local build files.
- **Never commit or push without the author's word.**
- **After the deploy**, fetch the live English page, the Chinese page and one voice clip.
- **Other outlets:**
  - a recorded video for YouTube or Bilibili;
  - a 30–60 second clip of the key-insight scene for social media;
  - the page itself as slides, stepped with the arrow keys.

## Working with the author

- **Show early and often.** Open the page in the browser pane and say what changed in a few lines. For wording changes, give a before → after table.
- **Treat every piece of feedback as a pattern.**
  - Find every instance of it in the narration, the stage text and the article, in both languages.
  - Fix them all, and say how many you found.
  - The author asked for this explicitly: "全部查一下，发现类似的对应调整" (check everything and fix the similar ones).
- **Answer review questions honestly.** When the author asks "do you think readers get it?" or "is there too much text?", name the specific gap and propose the cut. Don't reassure.
- **When a pasted paragraph is hard to read**, rewrite it. Then reread the paragraphs around it for the same problem.
- **Check what the talk says about the author's own tool.** The tool must really do it. If it doesn't, ask whether to build the feature or cut the claim.
- **Before a large rewrite, back up the page and the sources** in the scratchpad.
- **Don't wait on approvals for wording.** Apply the change, show it, and keep a backup so it can be reverted.

## Files in this skill

| File | What it covers |
|---|---|
| `references/story.md` | From outline to spine: the arc, transitions, the key insight, parallel parts, examples, honest claims |
| `references/scenes.md` | Designing scenes: animating the mechanism, visual hierarchy, the text budget, before/after, motion, layout |
| `references/narration.md` | Narration, voices, subtitles, music |
| `references/article.md` | The article under the player |
| `references/chinese.md` | The Chinese version: tone, terms, before → after |
| `references/engine.md` | The page engine, the scene API, the build scripts, local preview, deploy |
| `references/review.md` | Checklists to run before showing the author anything |
| `references/corrections.md` | The first talk's corrections as before → after pairs, by theme |
| `assets/template/index.html` | The starter page: engine, player, styles, three demo scenes, a sample article |
| `scripts/make_voice.py` | Narration clips for every step (English or Chinese) |
| `scripts/make_article.py` | Inserts an article JSON into a page |
| `scripts/make_zh.py` | Builds the Chinese page from the English one |
| `scripts/make_music.py` | Synthesizes the background loop |
