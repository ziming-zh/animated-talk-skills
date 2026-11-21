# The article under the player

The article is a collapsed "Read it as an article" section under the player. It is a **separate text written for reading**. It is not the narration pasted in. The talk follows the order of a presentation, and a reader needs a different order and much less example detail.

What the article went through in the first talk:

1. Every scene was expanded under the player and autoplayed. The author found it too distracting.
2. Only key stills were kept, but with the narration's text. The author found it disjointed.
3. The article was rewritten as a linear text with a few stills. This version was kept.

## 1. Structure

- **Linear.** One thread from the first section to the last. Each section's first paragraph picks up where the last one ended.
- **Each section goes problem → solution.** State what goes wrong first, then what to do.
- **Each paragraph develops its first sentence.** The first sentence states the paragraph's point, and every other sentence serves it. If a sentence doesn't, it belongs in another paragraph.
- **Explicit links between sentences.** Use *because*, *so*, *but*, *then*, *that is why*. Jumps between sentences were the most common complaint ("句子与句子之间缺乏明确的逻辑关系").
- **No meta-structure.** Don't write "the first half of this practice…"; connect with *so*.
- **Section titles** name the point or the plain topic: "The cost of changing an abstraction", "Practice 2: isolate each design, verify the new against the old". Avoid a clever title ("Why research systems hurt" was rejected).
- **Don't open the article or a section with a question** (the author called it "有点呆", a bit clumsy). Don't open with a frame the reader doesn't have ("The first question asks…"). Open with a statement of the situation. The video may pose questions out loud; on the page, state the point.

The first talk's 11 sections:
1. When agents write the code
2. Abstractions, and how a system is built from them
3. The cost of changing an abstraction
4. What agents change
5. Key insight: with agents, an improper abstraction is a silent failure
6. Checking for it proactively
7. Practice 1
8. Practice 2
9. Practice 3
10. ThinSpec
11. Takeaways

## 2. Motivate, then zoom in

"这是 ppt demo 和文章的重要区别": this is the key difference between a slide demo and an article. A video can walk through an example step by step. On the page, an example costs a reader real effort.

- State the point and why it matters first.
- Then give a short example, with only the details that help the point land. Cut the rest.
- One example per point. Its job is to serve the insight above it, not to be a story of its own. When the point is the process (failures narrowing the problem), stop before the solution ("不用讲正确方法", no need to give the correct method). One cache paragraph was "太 dry 了，其实就是一个例子" (too dry; it's just an example). The fix was to lead with the insight and use the example as its evidence.
- If an example needs more than a few sentences, add a figure and shorten the text.
- Keep detail-heavy specifics (exact metrics, numbers) out of the general statement. Say the general version, then one concrete case.

## 3. Sentences

The register is formal but plain. Two failure modes came up, and the fix lies between them:

- **Too choppy.** Clipped fragments and colon-chains: "Switching means rewriting most of the system, and for a long while half the code is new, half is old, and nothing quite fits." Or: "The old version, patches and all, is the reference: what it has demonstrated still holds."
- **Too heavy.** "…for the same reason, which is that…", "namely", long nested clauses, rare words. "Both options are costly for the same reason, which is that implementing an abstraction takes months, so changing your mind about one is expensive."
- **Plain.** "Both options cost so much for the same reason: building an abstraction takes months." Or: "The old version may be full of patches, but whatever it got right is still worth checking against."

Check every sentence for:
- a vague phrase the reader can't unpack ("Agents remove the pain": what pain?);
- an absolute claim;
- a pronoun or "both", "this", "these" whose referent is out of view.

## 4. Highlighted insights

- Give each substantive section one highlighted point. The author asked for one on a section that had none: "抽象这一节再拉出一个要点吧" (pull out one more key point for the abstraction section).
- Pick the real insights: the ones specific to the new setting, which a reader would quote. For example: "Agents organise code by when it runs, not by which design it serves."
- Leave out common knowledge from before the new setting. The cost of changing an abstraction was true before agents too, so it is not an insight here.
- Each one must make sense when **skimmed on its own**. "两条路都很贵，原因是同一个" (both paths are expensive, for the same reason) fails on its own: which two paths?
- Render them in a distinct, elegant serif: Newsreader italic for English, Noto Serif SC for Chinese. Each has a left rule in the accent color. In the JSON: `{"insight": "..."}`.
- An insight gets its supporting reason in the paragraph around it (see `story.md` §5).
- Write each one elegantly. "In a research system, the abstraction isn't designed first and then built. It is discovered while the code is being written." became "In research, an abstraction is not designed and then built; it is discovered in the building."

## 5. Figures

- Use a few stills at the turns of the argument, not one per scene, and never animated. Animation next to text pulls the eye away from reading.
- Give each parallel part (each practice) one figure. The author asked for this: "practice 1-3 挑一张 animation 帮助理解" (pick one animation for each of practices 1–3 to help understanding).
- A figure goes right after the paragraph it illustrates: `"fig": {"scene": "...", "step": k, "after": j}`.
- When a passage is hard to follow in words, add a figure. "The structure is inverted…" was unclear until a figure of "one module per design" sat beside it.
- **Every figure has a caption** that says what to see in it: "Code organised by design: the cache only calls each module, and each module holds all of one design's code."

## 6. Takeaways and ending

- **Three takeaways, which organize the section insights.** Each one is a claim plus how to act on it. An earlier list of five or more read as a recap, and the author asked for three: "保留三点，但把这些 insight 都组织起来" (keep three, but organize the insights into them).
- **Give an entry point to the project:** `{"link": {"href": "https://github.com/...", "text": "Project on GitHub →"}}`. In the first talk it sits at the end of the tool's section, just before the takeaways, where the reader has just learned what the tool does.
- **Where the text describes a detour, add what it was worth.** For example: "So even a detour isn't wasted. What the old version got right becomes the foundation for the next."

## 7. Review passes for the article

1. **Extract the line.** List the first sentence of every paragraph and read them in order. That list should read as the argument.
2. **Skim test.** Read only the headings and the highlighted lines. Each should make sense, and together they should tell the story.
3. **Full reread for clarity.** Mark any phrase a reader would have to stop on. Rewrite it, then check its neighbors.
4. **Read for choppiness and heaviness.** Find one bad sentence, then look for every sentence like it.
5. **Do the same passes on the Chinese article** (see `chinese.md`).
