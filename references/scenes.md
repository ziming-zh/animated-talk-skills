# Designing scenes

A scene shows one idea. A step is one beat: one chunk of narration and one change in the picture. The stage is 1200 × 675; the subtitles cover the bottom band, so keep content above y ≈ 560.

## 1. Animate the mechanism, don't describe it

If the stage needs a sentence to be understood, show the thing happening instead. Examples from the first talk:

- **Silent failure.** A little person and an agent patch one failing test after another; each turns ✓. Zoom out: many branches lead into the core, all built the same way. More workloads arrive and every branch fails somewhere. The intuition — locally it feels great, globally it has drifted — is in the motion.
- **A thin spec at work** (slide 14). First version: three agents and a page of text; the author asked for less text, then said it was too abstract. Final: one cache module (writers, db, cache, reads) as the main picture, with the three tries animated on it. Try 1: workloads A, B, C pass while a skip list grows key by key. Try 2: two value packets reach db and cache in opposite orders; the cache keeps the old value (✗). Try 3: the cache deletes, a refill arrow brings the new value. The spec is small on the left: the invariant, each ban appearing with the workload property it records, and the problem statement sharpening at the end.
- **v1 → v2 swap.** Tangled: eviction lines colored through every function; swapping means editing line by line, and one slip breaks consistency. Isolated: one module per design; change one line and v1 slides out while v2 slides in, the other modules untouched. Same layout in both scenes, so the contrast is the point; v1 was made more complex so the mess reads.
- **Parallel exploration.** "Try four at once" drew v1–v4 side by side with branches, not a sequence.
- **Effort as a signal.** Estimate bars vs. actual bars per task; the one 3× over turns orange.

## 2. Visual hierarchy

- One main picture per scene. Supporting material (the spec, a legend, a code sample) goes small at the side.
- The main items get the space. In an overview of three practices, the three practices are the biggest things on the stage.
- If a scene feels busy, first remove what doesn't carry the main line, then split it into two scenes (the "fine-grained" and "multi-objective" checks became their own scene with an example each).
- Don't spend three scenes on something the audience knows.

## 3. The text budget

- On the stage: labels, key numbers, at most one short line per element.
- Sentences live in the narration and subtitles.
- No UI chatter on the stage ("narrated, or click to step").
- No words that are color jargon ("green", "all green"); say what passed.
- Titles of scenes state the claim ("Agents file code by when it runs"), not the topic.
- Labels say what the thing is in the reader's words ("try 1 · skip stale keys"), not code names.
- After a pass of the narration, read the stage text alone: anything that repeats the narration in full is cut.

## 4. Motion

Motion carries meaning; keep it lively. Available effects: rise, pop, draw (strokes draw in), grow-x/grow-y, move at a step (`m`), numbers that count, text that types, a slow spin for "still evolving".

- Each step changes one thing the narration names at that moment.
- Delays (`d`) order the beat inside a step: cause first, then effect.
- Use a ✗ that turns into a ✓, a red ring on the failing part, a count-up on the number that matters.
- When simplifying a busy scene, cut text and side elements, not the animation. The author wants the page lively, with scene transitions, a camera push, and typed and shaking elements. Once they thought the animations were gone ("很多之前很 fancy 的动画都删掉了", lots of the earlier fancy animations got deleted). A leftover test style had turned the transitions off in their pane, and the newer scenes had thin motion. See `engine.md` §8.

## 5. Color meaning, kept constant across scenes

blue: the spec, designs, the human-kept side · green: passes, correct · red: failure, stale, broken · orange: effort, estimate exceeded, attention · amber: caution, ban · ink/grey: neutral structure. Box kinds in the engine: `core`, `design`, `card`, `panel`, `code`, `term`, `tile`, `ghost`, and solid/ring variants.

## 6. Chapter cards and overview

- Repeated structures (practice n of N) get a chapter card: a big faint number, "PART n OF N · FROM ⟨technique⟩", the title, the question typed out.
- An overview scene lists the parallel items. They are the main point, so they get most of the stage, one per step. Each shows its question, a one-line case from the running example, and the technique it comes from. In the first talk, the practices were first drawn small next to other elements, and the author objected: "三个 practice 应该是重点；但占的版面很小" (the three practices should be the focus, but they take up very little space).

## 7. Takeaways scene

Three rows, each an icon that pictures the claim, a headline (the claim), and one subline (how). Headlines from the first talk: "A wrong abstraction is a silent failure." / "Let every correction refine the spec." / "Trust effort over passing checks."

## 8. Check every step

In the browser pane: step through every scene at desktop size and at phone width (375 px); look for overlaps, empty bands, text under the subtitles, elements left over from a previous step (`x` missing), and items that appear before the narration names them. Open the article and check each still figure.
