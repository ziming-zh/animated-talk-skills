# Corrections from the first talk, before → after

These are the author's actual corrections while making "How to use agents to build complex systems". The author's comment is quoted when it shows the reason. Read this before writing, and come back to it when a sentence feels off: most new problems are one of these again.

## 1. Story and transitions

| Before | Author's comment | After |
|---|---|---|
| "Both options are costly", as the author's own situation | "要把它 model 成…很多系统 researcher 或者 PhD student 在开发中的一个非常常见的困扰" (model it as a very common struggle for systems researchers and PhD students) | The trade-off every researcher meets: rewrite, or keep patching |
| A slide titled "Bitter lesson from ⟨the author's internal project⟩" | Don't name the project | "a practical system I'm developing" (later: "a GPU memory system I'm building") |
| A context-heavy example in the opening | "大家没有这个 context" (people don't have this context) | Removed; one familiar running example (a cache) introduced later |
| Layers before any definition | "我们还没解释什么是abstraction呢" (we haven't explained what an abstraction is yet) | A scene "What is an abstraction?", then "Now zoom out" |
| "Lots of pieces, and you can swap any of them out." | "Why？rationale 没有讲清楚" (Why? The rationale isn't clear) | "small pieces, each carrying out the decision above it. As long as a piece keeps to its design, you can rewrite it however you like. That's why agents can safely take these over." |
| "If you're a systems PhD student, …" | Not only systems PhDs | "If you're building something that's been built before, …" |
| "Most tasks land close to the guess. But this one takes three times as long." | More convincing: the agent needs a patch for every new workload | "task C needs a new patch for every new workload, and ends up three times over. That's not just a slow task." |
| A rewrite where opportunity two drifted from "autoresearch: effort as a signal" | It changed the outline's meaning | Restored: "Give an agent a downstream task with a clear metric… how the agent's work goes tells you something about your design." |
| "But here's the catch. And honestly, it's the core problem. What if the key idea at the top is wrong?" | Not "wrong key idea"; say the problem: agents make things work without asking whether it's the right thing | "They're so good at making things work that they never stop to ask: are we doing the right thing, or just doing things right?" |
| "Here's the catch:" after the opportunity scenes | Too abrupt; give the reader a buffer | "That vision rests on one assumption: when a design doesn't fit, the struggle shows. With agents, it often doesn't." |
| "With agents, every broken piece just gets patched until it passes." | Why? There's a gap | "each task's goal is to make its check pass, and the cheapest way there is a local patch, not a rethink of the design above. So every broken piece gets patched until it passes" |
| A long explanation of loud vs. silent failure | Do we need this much? Give the intuition: local fixes feel great, globally you've drifted | An animation: workaround on workaround, each passing; zoom out; more workloads, everything breaks |
| "And one question is still open: if a model can find the bug in review, why can't it write the right code in the first place?" | "这个 transition 根本接不上" (this transition doesn't connect at all) | Cut. The tool follows from everything before: "So we built all of this into ThinSpec" |

## 2. Honest, exact claims

| Before | After |
|---|---|
| "your core abstraction is really just a guess" | "your core abstraction is your best understanding so far, and it keeps evolving as you learn" |
| "You're going after something nobody's done before." | "You're after a solution nobody understands yet" |
| "and you couldn't judge one until you'd built it" | "since intuition alone can't tell you whether an abstraction is right, you had to build each one to find out" |
| "the abstraction was wrong from the start" (in the analysis) | "improper", "doesn't fit": rightness depends on assumptions |
| "so rewriting it touches nothing else" / "the new one must still do" everything | "the new version must pass most of what the old one passed" ("at least the majority"; the old one has patches) |
| "the behaviour it has already demonstrated is still correct" | "whatever it got right is still worth checking against" |

## 3. Plain words

| Before | Author's comment | After |
|---|---|---|
| "There goes the deadline." | Unclear; say the process is messy | "you're rewriting most of the system, with old and new code that don't fit together for a long while" |
| "Looks great on paper, but it never really ships." | Say maintenance debt, hard to deploy | "until the maintenance debt makes the system hard to deploy" |
| "Code is cheap." | Lacks a researcher's rigor | "Implementation got cheaper" |
| "same year can try seven" | "怪怪的句子" (dictated as "乖乖"): weird, not spoken | "Try four at once, keep the one that holds up, and branch again from there." |
| "room to change course" | rejected | (cut) |
| A title "Three tricks, three practices" (dictated as "free tricks, free practices") | "非常的 AI flavor" (very AI-flavored): count-based slogan titles | Practices named by what they do |
| "ordinary software" | rejected | "three questions systems already ask" |
| "That's what makes systems research hard. It's also what makes it fun." | wordy | cut |
| ", and it's a sneaky one." | "这种废话都删掉" (delete all filler like this) | cut |
| "fires on effort" | readers won't get it | cut |
| "as a PhD student" | reads badly | cut |

## 4. The key insight and the practices

| Before | Author's comment | After |
|---|---|---|
| "That's what makes it a silent failure… Build the alarms in, so the first wrong turn rings a bell…" | "too promotional, 没有什么干货" (no real substance) | Two concrete needs: surface signs of a wrong abstraction proactively, and keep the design flexible enough to change, with the new version verified |
| "No crash will tell you, so you have to ask" | Too casual; name what we want: proactively | "So check proactively, with three questions systems already ask." |
| The end of the key-insight scene adding "warning signs" and "adaptive design" | Trivializes the core insight; too many elements | Only the silent-failure line remains |
| Practices: "Human maintainable abstraction knowledge / Iterate fast / Get honest results" | These are needs, not practices; no link from invariants to them | "Maintain the spec, not the code / Isolate each design, verify new against old / Make checks fine-grained and multi-objective" |
| "Independent oracles" as the third technique | Not the same dimension as the other two | The author chose "mutation testing". Then they asked whether it really links to closing shortcuts, proposed "Could the result be hacked?" (back to reward hacking) and "anti-pattern". The page ended with "patch overfitting" from program repair, which the assistant chose and the author didn't object to |
| "Let the old version judge the new" | Reads strangely: the old one is naive, but what it proved should carry over | "verify new against old"; "what the old version got right still counts" |
| "Can you swap one part? Break nothing?" | "到底是在讲啥？看不懂" (what is this even saying? I can't follow) | "Did a big change break what already worked?" |
| "Assume every check will be gamed" | Too abstract; what do we do? | "Does a passing check mean the goal is met?" → fine-grained and multi-objective checks |
| "Does the new version match the old?" | "这本身就有 differential testing 的行为" (that in itself is what differential testing does): circular | "Did a big change break what already worked?" |
| The three questions → techniques → practices, one abstract sentence each | "读者看完之后就完全 lost 了" (readers will be completely lost after reading this) | Each question followed at once by a cache case: "For the cache: never serve a stale read." |
| Bans "no timeouts", "no redirecting" | Generic fixes, so the reader can't see what a ban is for | "no fixes tuned to the workloads we tested"; "the cache never orders writes: it only drops" |
| "A ban turns each failure into a rule that no later agent repeats." | "太浅" (too shallow); AGENTS.md lists already do this; the deeper point is that bans refine the workload's properties | "Each ban records one property of the workload. The more bans you collect, the more clearly the problem is defined." |
| "Another lesson, another line: don't meet the rule by giving up the goal." | "读起来很蠢" (reads as dumb): a generic truth, not an insight | cut |
| "Each design … gets its own module, with the same few hooks: on read, on write, nightly." | Say the fundamental difference in how agents write code | "Agents organise code by when it runs, not by which design it serves", because they follow the request path and nothing says which design a line belongs to |
| A Parnas reference | "非常的 digressing" (a big digression) | cut |
| "Automated program repair ran into this first: patches that passed the tests by deleting code" | digresses | cut |
| "How to catch these ripples early is still open, and it's what I'm studying next." | digress | cut |
| "it proposes a finer check, and you approve it" | Don't stress approvals; readers will worry about too much asking | "tightens the check" |
| Fine-grained = per workload | "我的 fine-grained 其实是指尽量用一些和底层设计相关的指标" (by fine-grained I mean metrics tied to the underlying design) | "measure what the design itself should do: how often an evicted entry is needed again, not just the hit rate" |
| "The agent is the best at finding a check's shortcuts" | "come out of nowhere" | "an agent hacks a check by searching for the cheapest way to pass, and that same search finds the check's holes" |
| "Here's how the alarm fires. Before agents, the code fought you… ThinSpec brings the thinking back" | Delete it; not needed | cut |
| "Comparing new against old is still up to you." | More confusing; the point is the new passes what the old passed, so the effect is stable and verifiable | "the new version must pass what the old one passed, so every change stays stable and verifiable" |
| "now with the alarm" | Say ThinSpec | "Now the loop on the cache, with ThinSpec." |
| "That's a silent failure. Nothing broke…" (zh: 这个抽象从一开始……) | "乱七八糟" (a mess); state it directly | "That's a silent failure: every check passes, yet the abstraction was wrong from the start." The author let "wrong" stand in this short punchline. Elsewhere they asked for "improper" (see story.md §7) |
| Takeaways: "Iterate on the abstraction / Silent failure / Keep a thin spec, judge by results" | Shallow | "A wrong abstraction is a silent failure. / Let every correction refine the spec. / Trust effort over passing checks." |

## 5. The stage

| Before | Author's comment | After |
|---|---|---|
| Title slide with an extra row, "narrated or click", a lab name, the author's name | Too much text | Title, one line of context, the question, a play button, a small picture |
| A leftover test style that turned transitions off in the author's pane, plus thin motion in newer scenes | "很多之前很 fancy 的动画都删掉了" (a lot of the earlier fancy animation got deleted) | Style removed and the page reloaded; motion added back (camera push, typed and shaking elements) |
| A silent-failure picture with one component | Should be many branches into the center, all breaking under more workloads | A branching system; a person tests more workloads; failures on every branch |
| v1, v2, v3 drawn in sequence | Agents allow parallel work | v1–v4 side by side |
| v1 → v2 swap described | Show the difference between the two slides with an animation; make v1 more complex | Same layout in both scenes; tangled edits vs. one module sliding out |
| Only the wrong implementation shown | How does v2 gather things together? | The isolated version drawn |
| An overview with the three practices small | "三个 practice 应该是重点" (the three practices should be the focus) | The practices get the space |
| Three scenes on something everyone knows | "12 面可以很简单的讲一下" (slide 12 can be covered very briefly) | One scene |
| "A test fails, and the agent finds a workaround. Green. … Green again. Up close, this feels great." | "不要老 green 的" (stop saying green all the time) | "A test fails, and it finds a workaround. Another test fails, another workaround. Up close, it looks like progress." |
| One busy scene for fine-grained and multi-objective | "版面有些乱了" (the layout's gotten messy) | Its own scene, with an example for each |
| Slide 14: text on the right describing three agents | Too much text, then too abstract | One cache module with three tries animated on it; the spec small on the left |
| The bans on slide 14 without their meaning | The article's insight should be on the stage | Each ban shows the workload property it records; the problem statement sharpens |

## 6. The article

| Before | Author's comment | After |
|---|---|---|
| Every scene expanded and autoplaying under the player | Too much; distracting | A few stills at key turns |
| The narration copied as the article | Presentation order reads badly | Rewritten for reading, as one linear line |
| "Switching means rewriting most of the system, and for a long while half the code is new, half is old, and nothing quite fits." | Chopped too fine | "Switching means rewriting most of the system, and for a long time the new and old code sit side by side without fitting together." |
| "Agents remove the pain." | Remove what pain? | "Agents cut most of this cost, because they make implementation cheap." |
| "Both options are costly for the same reason, which is that implementing an abstraction takes months, so changing your mind about one is expensive." | Effortful | "Both options cost so much for the same reason: building an abstraction takes months." |
| "The old version, patches and all, is the reference: what it has demonstrated still holds." | Chopped, hard to read | "The old version may be full of patches, but whatever it got right is still worth checking against." |
| "The structure is inverted so that each design has its own on-read, on-write and nightly hooks" | What's inverted? Add a figure | "The practice, then, is to organise code by design instead of by when it runs…", plus the figure |
| A practice written as "the first half… the second half…" | Be linear | Linked with "so" and "with each design in its own module, …" |
| A cache paragraph with "namely", "as a prohibition / as a property" | Dry, too many rare words and long sentences | Insight first; a short example after |
| "像 cache hit rate 这样的单一数字……" (a single number like the cache hit rate) | "例子味道太重了" (it reads too much like an example) | The general statement first, then one concrete case |
| A section that opens with a question | "有点呆" (a bit clumsy) | A statement |
| "Why research systems hurt" | A bad title | "The cost of changing an abstraction" |
| "In a research system, the abstraction isn't designed first and then built. It is discovered while the code is being written." | Not elegant | "In research, an abstraction is not designed and then built; it is discovered in the building." |
| A highlighted line about the cost before agents | Not an insight: that was true before agents | Not highlighted |
| "两条路都很贵，原因是同一个……" as an insight (both paths are expensive, for the same reason) | When skimmed, which two paths? | Not highlighted; the paragraph says what the two are |
| A list of five-plus takeaways | Too many | Three, organizing the insights |
| A GPU-system number with no lesson | Add what it's worth | "So even a detour isn't wasted. What the old version got right becomes the foundation for the next." |
| Figures without captions | | Every figure captioned |

## 7. Chinese

See `chinese.md` §2–4 for the full tables. The most telling ones:

| Before | After |
|---|---|
| 写者 / 夜间任务 / 淘汰 | writer / nightly job / evict |
| 让副本保持新鲜，在写入……到达时 | 保持副本新鲜 / 过期源于写入 / 写入可能乱序 |
| 每条 ban 记录的是一种失败做法搞错了的 workload 特性，所以这些 ban 合在一起…… | 每条 ban 都记下了 workload 的一个特性。ban 积累得越多，问题就定义得越清楚。 |
| 一个任务所需的工作量，是关于其上层设计的证据。 | 一个任务花了多少工夫，能从侧面反映出它上面的设计合不合适。 |
| 这就是 silent failure：系统没崩，也没报错，check 全都通过，可抽象从一开始就错了。所以不能等东西坏了再说。 | 这就是 silent failure：check 全都通过，可抽象从一开始就错了。 |
| 现在在 cache 上走一遍完整流程，这次带上报警。 | 现在用 ThinSpec 在 cache 上走一遍完整流程。 |

## 8. Voice and media

- **English:** macOS say → Premium Ava → Kokoro am_michael ("老气", sounds old) → **Kokoro af_bella 1.1**.
- **Chinese:** Kokoro zf_xiaoxiao (wrong tones; the author: "这个中文这么讲的这么差", the Chinese sounds this bad) → CosyVoice 2 ("太幼稚了；不够有深意", too childish, not enough depth) → more mature female voices → "试一下男声音" (try a male voice) → **edge-tts YunjianNeural −4%**.
- **Subtitles:** under the stage → **on the picture**. With text moving under a moving picture, "非常容易 distracted" (it's very easy to get distracted).
- **Music:** added under autoplay, original and synthesized.
- **URL:** "all-green-wrong-design" was rejected. Use a slug that names the topic: `agentic-research-system-design`.
