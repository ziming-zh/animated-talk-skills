# From outline to story line

The story is settled before anything is drawn. A wrong link in the story costs a sentence to fix at the spine stage, a scene once drawn, and a voice re-render, an article section and a Chinese pass once everything is built.

## 1. What an outline deck usually gets wrong for a reader

The first talk's outline was 21 slides of a lab discussion. Typical gaps, all of which had to be fixed:

| In the outline | What the reader needed |
|---|---|
| "A system design is layered by abstractions" | What an abstraction is, on its own scene, before layers |
| A slide of the author's own project history (dates, internal terms) | The general pain the audience recognizes: "both options are costly" |
| "Key insight ✗ / Design / ✗ ✗ ✗" diagram | An intuition: patching feels like progress locally, while the whole drifts |
| Three headings: invariants, differential testing, independent oracles | Three parallel practices, each derived from a known technique, on the same dimension |
| A hard domain example (hooks inside autograd) | One familiar example used throughout (a cache) |
| "If AI can review it, why can't it write it right?" | Cut: the transition didn't connect. The tool follows from the earlier observations (raise alarms proactively, at design time), not from a new question |
| Takeaways as three long sentences | Three takeaways that organize the insights, each a claim plus how |

## 2. Write the spine

10–15 numbered sentences, one claim each. Read them aloud in order; each must follow from the one before with *because*, *so*, *but*, or *which raises the question*. If you have to say "also" or "another thing", the line has a fork: merge it or cut it.

The spine of the first talk, as a model:

1. Agents now write most of the code, but in research the core abstraction is our best understanding so far, and it keeps evolving.
2. An abstraction is the simple model a system is built around; a system is layered: core, design decisions, code.
3. Experienced people design top-down; on a new problem you find the structure bottom-up, as you build.
4. So the abstraction often changes midway, and both options (rewrite, or keep patching) cost months.
5. Agents make implementation cheap: try several abstractions at once.
6. And effort becomes a signal: a task far past its estimate says the design above it doesn't fit.
7. That vision assumes a bad design makes itself felt. With agents it doesn't: the cheapest way to pass a check is a local patch.
8. So an improper abstraction is a silent failure: every check passes while the design is wrong.
9. Systems check for silent failures proactively, with three questions; each needs a new practice once agents write the code.
10–12. Practice 1, 2, 3 (each: the problem with agents → why → the practice → the example → the insight).
13. The tool builds the practices in, around a proactive alarm against silent failure.
14. The loop on the example.
15. Three takeaways.

Show the spine to the author and ask what's wrong. Ask specifically: "Is any step a jump? Is any step not what you meant?" Keep planning scenes while they read it; don't wait.

## 3. The arc

Problem → Opportunity → Twist → Key insight → Practices → Tool → Worked loop → Takeaways.

- **Opening.** The first scene states the problem itself and the question the talk answers, not a slogan. The author rejected "All green, wrong design" as an opener, and later as the URL.
- **Problem.** Model it as a pain the audience lives with ("越贴近复杂系统开发者的心理越好" — the closer to the developer's own experience the better). Name the trade-off they face and why it costs so much ("Both cost so much for the same reason: implementing an abstraction takes months").
- **Bridge every act boundary.** End each act on its root cause, and open the next act as the answer to it. The jump from problem to opportunity was flagged ("中间的 transition 可以再明确一点", the transition in between could be clearer). The fix: "Both cost so much for the same reason: implementing an abstraction takes months. So what if implementation got much cheaper?"
- **Opportunity.** What changed. Keep each opportunity the outline meant; don't let it drift into a generic one.
- **Twist.** Don't jump from opportunity to problem. Name the assumption the opportunity rests on, then show it breaking: "That vision rests on one assumption: when a design doesn't fit, the struggle shows. With agents, it often doesn't." Give the reason, not only the claim: "each task's goal is to make its check pass, and the cheapest way there is a local patch".
- **Key insight.** One sentence, named with a term the audience's field already has (silent failure). Spend the space on the intuition specific to your claim, not on explaining the borrowed term: the author rejected a long "first, a loud failure…" explanation. The supporting elements must not dilute it; the author rejected an ending that added "warning signs" and "adaptive design" next to it.
- **Practices.** Each parallel part follows the same pattern: a question → a one-line case from the running example → the well-known technique that answers it → what breaks once agents write the code → the practice.
  - **Every part needs the concrete case.** Without it the reader is lost. The author's verdict on the version without cases, one abstract sentence per part: "读者看完之后就完全 lost 了" (readers will be completely lost after reading this). The final version gave each question a cache case at once: "What must always be true? For the cache: never serve a stale read." "Say you rewrite how the cache evicts." "Ask for a higher hit rate, and an agent might simply stop evicting."
  - **The question states the risk, never the technique's own operation.** "Does the new version match the old?" is just differential testing restated ("这本身就有 differential testing 的行为", that in itself is what differential testing does). "Did a big change break what already worked?" states the risk.
  - **Name each technique professionally, and gloss it in one clause.** For example: "differential testing: run the old and new versions side by side and compare." ("直接用专业名字就行", just use the professional name; "对于3种办法也可以简单的做个解释", give the three methods a brief explanation too.)
  - **Items must be the same kind of thing:** all practices (what you do), not a mix of practices and needs. "Iterate fast" and "get honest results" are needs.
  - **Items must sit on the same dimension.** "Independent oracles" sat oddly beside invariants and differential testing ("不是一个维度上", not on the same dimension).
  - **Check that each practice really follows from its technique.** For the third part, the author first took mutation testing. They then asked whether it truly connects to closing shortcuts, proposed "Could the result be hacked?" to link back to reward hacking, and suggested "anti-pattern". The page settled on "patch overfitting" (from program repair) and "Does a passing check mean the goal is met?". Confirm such a final pick with the author rather than assuming it.
- **Tool.** Headline it by the key insight it answers: "a proactive alarm against silent failure". Each practice becomes one of its mechanisms.
  - Don't add the tool's alarm as a fourth peer item that repeats the practices. The author objected that it was already covered, and "fires on effort" wouldn't be understood.
  - Lead into the tool from everything before ("So we built all of this into…"), not from a new question.
  - Don't put the user's burden up front, such as approvals and prompts: "读者会担心太多 elicitation" (readers will worry about being prompted too much).
  - State its platforms correctly.
  - Anything the talk says the tool does, it must do.
- **Worked loop.** Run the whole thing once on the running example, including the moment the person decides.
- **Takeaways.** Three. Each organizes several insights into one claim plus how to act on it. Not slogans ("keep a thin spec; judge by results" was rejected as shallow).

## 4. Inside a part: linear, problem first

Within each practice, the order is: what goes wrong → why it goes wrong (the mechanism) → therefore the practice → the example → the insight. No "the first half of this practice… the second half…": connect with *so* and *because*. If a practice has two moves, the second must come out of the first ("With each design in its own module, the comparison that used to be impossible becomes easy").

## 5. Insights need roots

An insight that "comes out of nowhere" reads as a slogan. Find the deeper reason and say it first.

- "The agent is best at finding the check's shortcuts" came out of nowhere. Its root: an agent hacks a check by searching for the cheapest way to pass, and the same search finds the check's holes.
- "Agents organise code by when it runs" needed a why: an agent decides where code goes by following the path a request takes, and nothing in the code says which design a line belongs to.
- "A ban stops agents from repeating a mistake" was too shallow (everyone has AGENTS.md lists). The deeper point: each ban records a property of the workload, and the bans together sharpen the problem definition.

When the author says "这个 insight 很有意思", it deserves emphasis (a highlighted line in the article, its own beat on the stage). When they say "太浅", dig for what is specific to the new setting.

## 6. The running example

- Familiar to everyone in the audience, small enough to show whole (a cache in front of a database).
- Used for the definition, every practice, and the worked loop. Replace any example that needs context (the author's own system) with it; mention the author's system only as a one-line data point ("In a GPU memory system I'm building, the second version took 5 days, down from 25 to 30").
- Real numbers stay with the system they came from. The running example is made up, so never pin the author's real measurements on it: label them as coming from the author's system.
- **The example must show why the mechanism matters, and tie it to the part's headline.**
  - Bans like "no timeouts" or "no redirecting" are generic fixes, so the reader can't tell what the ban is for. "No fixes tuned to the tested workloads" and "the cache never orders writes: it only drops" each teach something.
  - The author also couldn't see how the bans related to the part's claim, "maintain a thin spec" ("没看出来这和这些 ban 有什么关联", I don't see how this relates to these bans). Say how the mechanism serves the claim.
- **Pushback in the example must be insightful, not a generic truth.** "Don't meet the rule by giving up the goal" was rejected as obvious.
- **On the stage, when the contrast is the point, show the right implementation next to the wrong one.** "V2 真正会把这些东西怎么样去聚拢" (how v2 actually gathers these things together) was missing.
- **When the point is the process, don't spell out the answer.** In the article's ban paragraph the author said: "不用讲正确方法；我们的 point 是所有的这些失败，最终都会被用来收敛问题" (no need to give the correct method; our point is that all these failures end up being used to narrow the problem). The example serves the insight, not the solution.

## 7. Honest claims

Prefer the claim the author can defend:

| Too strong | Better |
|---|---|
| "your core abstraction is really just a guess" | "your best understanding so far, and it keeps evolving as you learn" |
| "something nobody's done before" | "a solution nobody understands yet" |
| "you couldn't judge one until you'd built it" | "intuition alone can't tell you whether it's right" |
| "the abstraction was wrong from the start" | "improper", "doesn't fit": "right or wrong 这个事情非常难评" (right versus wrong is very hard to judge), since every abstraction has assumptions it fits |
| "the new one must pass every case" | "must pass most of what the old one passed": the old one has patches, so "at least the majority" |
| "the behaviour it demonstrated is correct" | "whatever it got right is still worth checking against" |
| "rewriting it touches nothing else" | say what isolation actually buys |

Use "improper" or "doesn't fit" by default. The author did let "wrong" stand as shorthand in two short lines: "a wrong abstraction is a silent failure" in the takeaways, and the Chinese punchline "可抽象从一开始就错了" (yet the abstraction was wrong from the start). Don't take that as permission to use it elsewhere.

## 8. Cut digressions

Cut, even when true and interesting: history of a field ("program repair ran into this first…"), citations that need explaining (Parnas), future work ("what I'm studying next"), a second issue the talk doesn't resolve (late-stage coupling between modules), and lines that only say the topic is hard or fun.

## 9. Privacy

No internal project, lab or meeting names; no names of people, including the author's, unless asked. "A practical system I'm developing" is enough.
