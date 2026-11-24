# From outline to story line

The story is settled before anything is drawn. A wrong link in the story costs one sentence to fix at the spine stage. Once the scene is drawn, it costs the scene. Once everything is built, it costs a voice re-render, an article section and a Chinese pass as well.

## 1. What an outline deck usually lacks for a reader

| In the outline | What the reader needs |
|---|---|
| A key term used as a heading | What it means, on its own scene, before anything is built on it |
| The author's own project history: dates, internal terms | The general pain the audience recognizes |
| A diagram that only makes sense when the author talks over it | The intuition it stands for, shown as motion |
| A list of headings of different kinds | Parallel items of one kind, on one dimension, each from a known technique |
| A hard example from the author's own domain | One familiar example, used throughout |
| A rhetorical question that bridges to the next part | A bridge that follows from what came before |
| Takeaways as long sentences | Three takeaways that organize the insights, each a claim plus how |

## 2. Write the spine

Write the spine as 10–15 numbered sentences, one claim each. Read them aloud in order. Each must follow from the one before with *because*, *so*, *but* or *which raises the question*. If you have to say "also" or "another thing", the line has a fork: merge the branch or cut it.

The shape of a spine for a talk that argues for an approach:

1. The situation the audience is in, and the problem it brings.
2. The concept needed to talk about that problem.
3. Why the problem costs so much today.
4. What has changed that could cut that cost.
5. What becomes possible as a result.
6. The assumption that possibility rests on, and why it breaks.
7. The key insight that follows, in one sentence.
8. How the field already guards against this kind of problem, and why each guard needs a new practice now.
9–11. Each part: what goes wrong → why → the practice → the example → the insight.
12. The tool, if any, building the parts in.
13. One run of the whole loop on the example.
14. Three takeaways.

Show the spine to the author and ask what's wrong. Ask specifically: "Is any step a jump? Is any step not what you meant?" Keep planning scenes while they read it; don't wait.

## 3. The arc

Problem → Opportunity → Twist → Key insight → Parts → Tool → Worked loop → Takeaways. Not every talk needs every act, but keep this order of motivation.

- **Opening.** The first scene states the problem and the question the talk answers. A slogan is not an opener.
- **Problem.** Frame it as a pain the audience lives with, as close to their own experience as possible. Name the trade-off they face and why it costs so much.
- **Bridge every act boundary.** End each act on its root cause, and open the next act as the answer to it: "Both cost so much for the same reason: ⟨root cause⟩. So what if ⟨root cause⟩ went away?"
- **Opportunity.** Say what changed. Keep each opportunity the outline meant; don't let it drift into a generic one.
- **Twist.** Don't jump from the opportunity to the problem. First name the assumption the opportunity rests on. If the assumption is abstract, ground it in an experience the reader has had. Then show the assumption breaking, and give the mechanism, not only the claim.
- **Key insight.** One sentence, named with a term the audience's field already has. Spend the space on the intuition specific to your claim, not on explaining the borrowed term. Nothing next to it may dilute it.
- **Parts.** Each parallel part follows the same pattern: a question → a one-line case from the running example → the well-known technique that answers it → what breaks in the new setting → the practice.
  - **Every part needs its concrete case, at once.** One abstract sentence per part loses the reader.
  - **The question states the risk, never the technique's own operation.** A question that just restates what the technique does is circular.
  - **Name each technique professionally, and gloss it in one clause.**
  - **The items are the same kind of thing:** all practices (what you do), not a mix of practices and needs.
  - **The items sit on the same dimension.** One that answers a different kind of question looks out of place.
  - **Each practice follows from its technique.** Check the link. When the author offers candidates for a name or a framing, say which one you chose and let them confirm it.
- **Tool.** Headline it by the key insight it answers. Each part becomes one of its mechanisms.
  - Don't add a fourth peer item that repeats the parts.
  - Lead into the tool from everything before ("So we built all of this into…"), not from a new question.
  - Lead with what it does for the reader, not with what it asks of them (approvals, prompts, setup).
  - State its platforms correctly.
  - Anything the talk says the tool does, it must do.
- **Worked loop.** Run the whole thing once on the running example, including the moment the person decides.
- **Takeaways.** Three. Each one organizes several insights into one claim plus how to act on it. Not slogans.

## 4. Inside a part: linear, problem first

Within each part, the order is: what goes wrong → why it goes wrong (the mechanism) → so, the practice → the example → the insight. Don't write "the first half of this practice… the second half…": connect with *so* and *because*. If a practice has two moves, the second must come out of the first.

## 5. Insights need roots

An insight with no reason behind it reads as a slogan. Find the deeper reason and say it first.

- **A claim that comes out of nowhere.** Ask what mechanism makes it true, and say the mechanism before the claim.
- **A habit everyone already has.** If the insight describes something the audience already does, ask what it gives in the new setting that it didn't before, and say that.
- **A line the author calls interesting.** Give it emphasis: a highlighted line in the article and its own beat on the stage.
- **A line the author calls shallow.** Dig for what is specific to the new setting.

## 6. The running example

- **Familiar to everyone in the audience, and small enough to show whole:** a cache, a queue, a login flow.
- **Used everywhere:** for the definition, for every part, and for the worked loop. Replace any example that needs context, such as the author's own system, with it. Mention the author's system only as a one-line data point.
- **Real numbers stay with the system they came from.** The running example is made up, so never pin the author's real measurements on it.
- **The example must show why the mechanism matters, and tie back to the part's headline.**
  - A rule any system might have ("add a timeout") teaches nothing. Pick one that only makes sense for this problem.
  - Say how the example serves the part's claim. The reader shouldn't have to guess.
- **Pushback in the example must teach something.** A generic truth is not pushback.
- **On the stage, when the contrast is the point, show the right implementation next to the wrong one.**
- **When the point is the process, don't spell out the answer.** The example serves the insight, not the solution.

## 7. Honest claims

Prefer the claim the author can defend:

| Too strong | Better |
|---|---|
| "X is just a guess" | "X is our best understanding so far, and it changes as we learn" |
| "something nobody's done before" | "something nobody understands well yet" |
| "you can't judge it until you've built it" | "intuition alone can't tell you whether it's right" |
| "the design is wrong" | "the design doesn't fit": right and wrong depend on the assumptions |
| "it must pass every case" | "it must pass most of what the last version passed", when the last version had bugs too |
| "it touches nothing else" | say what isolation actually buys |

A short punchline may keep a strong word as shorthand when the author lets it stand. That is not permission to use the word elsewhere.

## 8. Cut digressions

Cut these even when they are true and interesting:
- the history of a field;
- citations that need explaining;
- future work;
- a second issue the talk doesn't resolve;
- lines that only say the topic is hard or fun.

## 9. Privacy

No internal project, lab or meeting names. No names of people, including the author's, unless they ask. "A system I'm building" is enough.
