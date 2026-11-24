---
name: animated-talk
description: Turn a rough outline (a slide deck, talk notes, the argument of a paper or a project) into a narrated, animated web talk that readers can follow, with an SVG scene player, voice, subtitles and music, a separate article underneath for reading, and optionally a Chinese version. Use whenever the user wants to make an idea, a PPT or a research talk into an animation, an explainer video, an animated blog post or an interactive story. Also use when they give feedback on such a talk's story, slides, on-screen text, narration, voice, article or translation, or ask to publish one.
---

# Animated talk: from an outline deck to a talk people can follow

This skill takes a rough outline deck and makes:
- a narrated, animated talk that plays in the browser;
- an article under it for people who would rather read;
- optionally, a Chinese version of both.

Before writing any text, read `references/reasons.md`. It explains why the author corrects what they correct, so you can find the next problem before they do.

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

Each principle answers one of the causes in `references/reasons.md`. When unsure, check the work against them.

1. **One line.** The talk is a single chain of claims.
   - Each scene answers the question the last one raised.
   - Each turn says which assumption breaks.
   - Cut anything that is not on the line: history, citations, future work, a second example.
2. **Define before use, motivate before claim.**
   - A concept the talk depends on gets its own scene before it is used.
   - A claim comes with its reason in the next breath.
   - An abstract premise starts from an experience the reader has had.
3. **One running example everyone knows.**
   - Pick a small, familiar system and carry it through every part.
   - Never use examples that need the author's private context.
   - Never name internal projects, labs or people.
4. **The picture carries the mechanism. The voice carries the sentences. The screen carries labels.**
   - On screen: labels, key numbers, at most one short line.
   - If the screen needs a sentence, animate the thing instead.
5. **Every sentence carries the point.**
   - No filler, no throat-clearing, no promotional lines.
   - The key insight is said in one direct sentence.
6. **Say exactly what is true.**
   - No absolutes the author can't defend.
   - No idioms a listener has to decode.
   - No words that sound clever but don't say what is done.
7. **The video walks through; the article motivates, then zooms in.**
   - A viewer can follow a step-by-step example.
   - A reader needs the point first, then only the details that help.
8. **A correction is a pattern, not a line.** When the author flags one sentence, fix every sentence like it:
   - in the narration, on the stage and in the article;
   - in both languages;
   - then re-render the voice and check again.

   When the parallel items are renamed or reframed, update every place that lists them.

## Workflow

Steps 1–3 settle the story before anything is drawn, which is the cheapest place to fix it. Steps 4–7 build and polish the talk. Steps 8–10 produce the article, the Chinese version and the publication.

### 1. Read the outline and set the frame

- **Extract the outline.** Write each slide's claim as one sentence. For a .pptx, unzip it and read the `<a:t>` runs of `ppt/slides/slideN.xml` in order.
- **Tag each item.** Mark it as a claim, evidence, an example, an internal detail or an open question.
- **Write down the author's intent:**
  - what the reader should believe, or do, at the end;
  - what each part of the outline is for.

  Keep that meaning when rewording. A rewrite that turns a specific point into a generic one has lost it.
- **Write down the author's key terms and what each one means**, and confirm them before building on them. A term the author uses in a narrow sense is easy to read in its common sense, and the wrong reading spreads to every scene built on it.
- **Note the outline's own transitions.** Reuse the ones that already work.
- **Settle the frame:**
  - **Audience.** Name the widest group that shares the problem, not one narrow role.
  - **Where it lives**, and its URL slug. The slug names the topic; don't use a catchy phrase.
  - **Languages.**
- **List what needs private context**, and decide how to replace it:
  - internal project names → a plain description ("a system I'm building");
  - lab or meeting names, the author's name → remove;
  - domain-heavy examples → the running example.

### 2. Write the spine and show it before drawing

- **Write the spine** as 10–15 numbered sentences, one claim each. Each one links to the one before with *because*, *so*, *but* or *which raises the question*.
- **For a talk that argues for an approach, this arc works:**
  1. **Problem:** the problem the audience already feels, in their words.
  2. **Opportunity:** what changed that could help.
  3. **Twist:** the assumption the opportunity rests on, and why it breaks.
  4. **Key insight:** one sentence, named with a term the audience's field already uses.
  5. **Parts:** what to do, in parallel parts. Each starts from a well-known technique and says what changes now.
  6. **Tool**, if there is one: each part becomes one mechanism.
  7. **Worked loop:** the whole thing run once on the example.
  8. **Takeaways:** three of them, which organize the insights.

  Not every talk needs every act. Keep the order of motivation: the problem before the answer, and the reason before the claim.
- **Choose the running example now**, and check that every part can be shown on it.
- **Show the spine to the author and ask what is wrong.** A wrong link found here costs one sentence, not a scene.
- **Don't block on the answer.** Keep planning scenes while the author reads the spine, and fold their answer in. Hold off on drawing details until the spine is settled.

`references/story.md` covers this step in detail.

### 3. Plan scenes and steps

- **A scene is one idea**, in 1–5 steps. A step is one beat: one narration chunk plus one visual change.
- **Make a table:** act · scene id · title · one line per step · what moves.
  - The title states the scene's claim ("Retries double the load"), not its topic ("Retries").
- **Give the concept everything depends on its own scene.** Center on it, then zoom out to the whole system.
- **Give each parallel part a chapter card:** "Part n of N · from ⟨technique⟩", the part's title, and the question it answers.
- **Overview scenes give the main items the most space.** Items drawn small next to many other elements can't be read.
- **Don't spend several scenes on what the audience already knows.** One scene will do.

### 4. Build the scenes

- **Animate the mechanism as it happens.** Show the cause, then the effect: one local change up close, then the camera pulls out to show what it does to the whole.
- **Use one main picture.** Legends and side notes go small at the side.
- **Keep text to a minimum.**
  - Labels and key numbers only.
  - At most one short line per element.
  - Sentences belong in the narration.
- **Draw before and after in the same layout**, so the change is the only difference.
  - Make the "before" convincingly messy.
  - When the contrast is the point, show the right way next to the wrong one.
- **Show parallel work in parallel**, side by side, not one after another.
- **Keep it lively.** The author wants motion: scene transitions, a camera push, typed and shaking elements. When a slide is too busy, cut text and side elements, not the animation.
- **Put the article's insights on the stage too.** If the article draws a conclusion from an example, show that conclusion on the example.
- **Check every step in the browser pane**, both at full size and at phone width.

Details are in `references/scenes.md` and `references/engine.md`.

### 5. Write the narration

- Write in a spoken register, with plain words.
  - Use 1–4 sentences per step.
  - The first sentence of each scene connects to the last scene.
- Signpost the structure: "Part one: …", "First … Second … Third …", "Take a …", "Say you …".
- Say the key insight in one direct sentence: "That's a ⟨term⟩: ⟨what it means here⟩."
- Avoid filler, set-up phrases, promotional lines, idioms, and slang where precision matters.

Details are in `references/narration.md`.

### 6. Voice, subtitles and music

- **Voice:** run `scripts/make_voice.py`.
  - English: Kokoro `af_bella` at 1.1.
  - Chinese: edge-tts `zh-CN-YunjianNeural` at −4%.
  - It remakes only the clips whose text changed.
  - Re-run it after every narration edit. A narration edit isn't done until the voice matches it.
- **Subtitles** are drawn on the picture, one short line at a time, timed to the voice.
  - Nothing that moves goes under the stage. Two moving things split attention.
- **Music:** run `scripts/make_music.py`.
  - It is original, so there is no licensing question.
  - It starts with the voice, under autoplay or when stepping by hand, and dips while the voice speaks.
  - Check it with `scripts/levels.py`: it must still be heard under the voice on laptop speakers.

### 7. Review, then play the whole thing

- **Run the checklist** in `references/review.md`.
- **Answer the reader's questions yourself, scene by scene:**
  - "What is that?"
  - "Why?"
  - "How does it know?"
  - "So what?"
  - "Would someone get this without the narration?"
- **Play the whole talk in the browser pane, and step through it by hand,** before showing it. The author reviews by watching all of it.
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
- **The page description and the listing blurb state the insight, not the format.** "An animated, narrated talk with a written version" says nothing a reader wants to know.
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
- **Find the reason behind a correction.** Match it to one of the causes in `references/reasons.md`, then look for the same cause everywhere else:
  - in the narration, the stage text and the article, in both languages;
  - fix every instance, and say how many you found.
- **Answer review questions honestly.** When the author asks "do you think readers get it?" or "is there too much text?", name the specific gap and propose the cut. Don't reassure.
- **When a pasted paragraph is hard to read**, rewrite it. Then reread the paragraphs around it for the same problem.
- **Check what the talk says about the author's own tool.** The tool must really do it. If it doesn't, ask whether to build the feature or cut the claim.
- **Before a large rewrite, back up the page and the sources** in the scratchpad.
- **Don't wait on approvals for wording.** Apply the change, show it, and keep a backup so it can be reverted.

## Files in this skill

| File | What it covers |
|---|---|
| `references/reasons.md` | Why the author corrects what they correct: five causes, with general examples |
| `references/story.md` | From outline to spine: the arc, transitions, the key insight, parallel parts, examples, honest claims |
| `references/scenes.md` | Designing scenes: animating the mechanism, visual hierarchy, the text budget, before/after, motion, layout |
| `references/narration.md` | Narration, voices, subtitles, music |
| `references/article.md` | The article under the player |
| `references/chinese.md` | The Chinese version: tone, terms, natural phrasing |
| `references/engine.md` | The page engine, the scene API, the build scripts, local preview, deploy |
| `references/review.md` | Checklists to run before showing the author anything |
| `assets/template/index.html` | The starter page: engine, player, styles, three demo scenes, a sample article |
| `scripts/make_voice.py` | Narration clips for every step (English or Chinese) |
| `scripts/make_article.py` | Inserts an article JSON into a page |
| `scripts/make_zh.py` | Builds the Chinese page from the English one |
| `scripts/make_music.py` | Synthesizes the background loop |
| `scripts/levels.py` | Checks that the music can be heard under the voice |
