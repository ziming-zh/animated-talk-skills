# The article under the player

The article is a collapsed "Read it as an article" section under the player. It is a **separate text written for reading**, not the narration pasted in. The talk follows the order of a presentation, and a reader needs a different order and much less example detail.

Two shortcuts don't work:
- **Every scene expanded under the player.** Animation next to text pulls the eye away from reading.
- **Key stills with the narration's text under them.** Spoken sentences read as disjointed on the page.

What works is a linear text written for the page, with a few stills.

## 1. Structure

- **Linear.** One thread runs from the first section to the last. Each section's first paragraph picks up where the last one ended.
- **Each section goes problem → solution.** State what goes wrong first, then what to do.
- **Each paragraph develops its first sentence.** The first sentence states the paragraph's point, and every other sentence serves it. A sentence that doesn't belongs in another paragraph.
- **Explicit links between sentences.** Use *because*, *so*, *but*, *then*, *that is why*. A jump between sentences is the most common reason a reader stops.
- **No meta-structure.** Don't write "the first half of this practice…"; connect with *so*.
- **Section titles** name the point or the plain topic. Avoid clever titles.
- **Don't open the article or a section with a question.** On the page it reads as clumsy. Don't open with a frame the reader doesn't have ("The first question asks…"). Open with a statement of the situation. The video may pose questions out loud; the page states the point.

A typical outline for an argued talk:
1. The situation, and the problem it brings
2. The concept the rest depends on
3. Why the problem is costly
4. What has changed
5. Key insight
6. How to check for it
7. One section per parallel part
8. The tool, if there is one
9. Takeaways

## 2. Motivate, then zoom in

This is the key difference between a slide demo and an article. A video can walk through an example step by step. On the page, an example costs the reader real effort.

- **State the point and why it matters first.**
- **Then give a short example**, with only the details that help the point land. Cut the rest.
- **One example per point.** Its job is to serve the insight above it, not to be a story of its own. When the point is the process, stop before the solution. A paragraph that is all example reads as dry: lead with the insight, and use the example as its evidence.
- **If an example needs more than a few sentences**, add a figure and shorten the text.
- **Keep detail-heavy specifics** (exact metrics, numbers) out of the general statement. Say the general version, then one concrete case.

## 3. Sentences

The register is formal but plain. Two failure modes come up, and the fix lies between them:

- **Too choppy:** clipped fragments and colon-chains. "Shipping is fast. Too fast, maybe: bugs slip out. Nobody notices."
- **Too heavy:** "…for the same reason, which is that…", "namely", long nested clauses, rare words. "The reason both approaches are slow is the same, which is that each of them requires a full rebuild, so that changing one's mind is expensive."
- **Plain:** "Both approaches are slow for the same reason: each needs a full rebuild."

Check every sentence for:
- a vague phrase the reader can't unpack ("this removes the pain": what pain?);
- an absolute claim;
- a pronoun, or "both", "this" or "these", whose referent is out of view.

## 4. Highlighted insights

- **Give each substantive section one highlighted point.** A section without one has nothing for a skimmer to take away.
- **Pick the real insights:** the ones specific to the new setting, which a reader would quote.
- **Leave out what was already common knowledge.** If it was true before the change the talk is about, it is not an insight here.
- **Each one must make sense when skimmed on its own.** "Both paths are expensive, for the same reason" fails alone: which two paths?
- **Render them in a distinct, elegant serif:** Newsreader italic for English, Noto Serif SC for Chinese. Each has a left rule in the accent color. In the JSON: `{"insight": "..."}`.
- **An insight gets its supporting reason** in the paragraph around it (see `story.md` §5).
- **Write each one elegantly.** Two flat sentences often fold into one balanced one: "It isn't designed first and then built. It is found while the code is written." → "It is not designed and then built; it is discovered in the building."

## 5. Figures

- **Use a few stills at the turns of the argument**, not one per scene, and never animated.
- **Give each parallel part one figure.**
- **A figure goes right after the paragraph it illustrates:** `"fig": {"scene": "...", "step": k, "after": j}`.
- **When a passage is hard to follow in words, add a figure** and shorten the passage.
- **Every figure has a caption that says what to see in it**, such as "Code organised by concern: each module holds all of one concern's code."

## 6. Takeaways and ending

- **Three takeaways, which organize the section insights.** Each one is a claim plus how to act on it. A list of five or more reads as a recap.
- **Give an entry point to the project:** `{"link": {"href": "https://github.com/...", "text": "Project on GitHub →"}}`. Place it at the end of the tool's section, just before the takeaways, where the reader has just learned what the tool does.
- **Where the text describes a detour, add what it was worth.** A failed attempt that left something behind is part of the argument.

## 7. Review passes for the article

1. **Extract the line.** List the first sentence of every paragraph and read them in order. That list should read as the argument.
2. **Skim test.** Read only the headings and the highlighted lines. Each should make sense, and together they should tell the story.
3. **Full reread for clarity.** Mark any phrase a reader would have to stop on. Rewrite it, then check its neighbors.
4. **Read for choppiness and heaviness.** Find one bad sentence, then look for every sentence like it.
5. **Do the same passes on the Chinese article** (see `chinese.md`).
