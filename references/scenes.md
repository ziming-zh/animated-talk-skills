# Designing scenes

A scene shows one idea. A step is one beat: one chunk of narration and one change in the picture. The stage is 1200 × 675. The subtitles cover the bottom band, so keep content above y ≈ 560.

## 1. Animate the mechanism, don't describe it

If the stage needs a sentence to be understood, show the thing happening instead. Patterns that work:

- **Local fix, global drift.** Up close, one small fix after another, each turning ✓. Then the camera pulls out: many parts built the same way. More inputs arrive, and every part fails somewhere. The intuition, that it feels fine locally while the whole drifts, is in the motion.
- **A rule taking effect.** The main picture is the running example. Each try is animated on it: the first passes a few cases while a workaround grows; the second fails on an ordering the first never met; the third holds. The rules collected along the way sit small at the side, each appearing as it is learned.
- **Before and after a restructure.** In the tangled version, one concern is colored through every function, so changing it means editing line by line. In the clean version, one module per concern: one line changes, the old module slides out and the new one slides in, and nothing else moves. Use the same layout in both, so the contrast is the point. Make the "before" messy enough to read as a mess.
- **Parallel exploration.** Several versions drawn side by side as branches, not in sequence.
- **Measured against expected.** Expected and actual bars side by side; the one far over turns orange.

## 2. Visual hierarchy

- **One main picture per scene.** Supporting material (a spec, a legend, a code sample) goes small at the side.
- **The main items get the space.** In an overview of the parallel parts, the parts are the biggest things on the stage.
- **When a scene feels busy, first remove what doesn't carry the main line.** If it is still busy, split it into two scenes, each with its own example.
- **Don't spend three scenes on something the audience knows.**

## 3. The text budget

- **On the stage:** labels, key numbers, and at most one short line per element.
- **Sentences live in the narration and subtitles.**
- **No interface chatter on the stage**, such as "narrated, or click to step".
- **No color words as jargon** ("green", "all green"). Say what passed.
- **Scene titles state the claim**, not the topic.
- **Labels say what the thing is in the reader's words** ("retry after 2 s"), not code names.
- **After a pass of the narration, read the stage text alone.** Cut anything that repeats the narration in full.

## 4. Motion

Motion carries meaning, so keep the talk lively. The available effects:
- rise, pop, draw (strokes draw in), grow-x and grow-y;
- move at a step (`m`);
- numbers that count up;
- text that types itself in;
- a slow spin, for "still evolving".

How to use them:
- **Each step changes one thing**, the thing the narration names at that moment.
- **Delays (`d`) order the beat inside a step:** the cause first, then the effect.
- **Mark the change:** a ✗ that turns into a ✓, a red ring on the failing part, a count-up on the number that matters.
- **When simplifying a busy scene, cut text and side elements, not the animation.** The author wants the page lively, with scene transitions, a camera push, and typed and shaking elements. If the animations seem to be gone, check for a leftover test style first (see `engine.md` §8).

## 5. Color meaning, kept constant across scenes

- **blue:** the spec, designs, the human-kept side;
- **green:** passes, correct;
- **red:** failure, stale, broken;
- **orange:** effort, an estimate exceeded, attention;
- **amber:** caution, a rule or ban;
- **ink/grey:** neutral structure.

Box kinds in the engine: `core`, `design`, `card`, `panel`, `code`, `term`, `tile`, `ghost`, and solid/ring variants.

## 6. Chapter cards and overview

- **Repeated structures (part n of N) get a chapter card:** a big faint number, "PART n OF N · FROM ⟨technique⟩", the title, and the question typed out.
- **An overview scene lists the parallel items.** They are the main point, so they get most of the stage, one per step. Each shows its question, a one-line case from the running example, and the technique it comes from.

## 7. Takeaways scene

Three rows. Each has an icon that pictures the claim, a headline that states the claim, and one subline that says how to act on it.

## 8. Check every step

Step through every scene in the browser pane, at desktop size and at phone width (375 px). Look for:
- overlaps and empty bands;
- text under the subtitles;
- elements left over from a previous step (a missing `x`);
- items that appear before the narration names them.

Then open the article and check each still figure.
