# Why the author changes what they change

The author reviews a talk as a first-time viewer would. They play it through, read the article once, and correct wherever they stop. Almost every stop has one of five causes:

1. They can't follow it.
2. They don't believe it.
3. There is nothing in it.
4. It isn't what they meant.
5. It is hard to watch.

Each cause comes from one picture of the audience: smart people from the field, with none of the author's context, who give the talk one pass and stop trusting it when it oversells. Knowing the causes lets you find the next problem before the author does.

## 1. "I can't follow": the reader has only what the talk gave them

The author knows the problem, its history and its vocabulary. The reader knows none of it. Every gap the author fills in their head is a place where the reader stops.

What it looks like:
- **A term or concept used before it is defined.** Give the concept everything depends on its own scene, before it is used.
- **An example that needs private context**, such as the author's project, lab or colleagues, or a domain the audience doesn't work in. Replace it with the one running example everyone knows.
- **A claim without its reason.** Where the reader would ask "why?", answer within the next sentence or two.
- **A step skipped between a claim and its conclusion.** Spell out the mechanism that links them.
- **An abstract premise.** Ground it first in an experience the reader has had, then state it.
- **An abstract principle with no case.** Follow it at once with a one-line case from the running example. Without one, the reader is lost by the third principle.
- **A jump between acts.** End each act on its root cause, and open the next act as the answer to it.
- **A frame the reader was never given.** "The second question…" when no question was posed, or "both" and "this" with the referent out of view.

| Before | After | What was missing |
|---|---|---|
| "Both options are expensive." | "Rewriting and patching are both expensive." | Which two options? |
| "So it's safe to hand off." | "Each piece only has to keep its contract, so it can be rewritten without touching the rest. That's what makes it safe to hand off." | The reason |
| "Users notice latency." | "You've closed a tab because it took too long to load. So have your users." | The experience behind the premise |

## 2. "I don't believe it": peers trust exactness, not force

The audience includes the author's peers. After one overstatement they discount everything else. Exact wording that the author can defend is what makes the argument hold, so the author would rather say less and be right.

What it looks like:
- **Absolutes:** "nobody has done this", "always", "must pass every case". Ask of each one whether it is always true, and say the version that is.
- **More certainty than the evidence gives.** For example, "wrong" for a design that only doesn't fit its assumptions, or "just a guess" for the best understanding so far.
- **Loose wording at the key line:** casual or cute phrasing, idioms the listener has to decode, words that sound clever but don't say what is done.
- **A claim about the author's own tool that it doesn't yet do.** Ask whether to build the feature or cut the claim.
- **Real numbers moved onto a made-up example.** A measurement stays with the system it came from.

| Before | After |
|---|---|
| "It's just a guess." | "It's our best understanding so far, and it changes as we learn." |
| "Nobody has done this." | "Nobody understands it well yet." |
| "Code is free now." | "Implementation got cheaper." |
| "There goes the deadline." | The plain fact: what has to be redone, and for how long. |

## 3. "There's nothing in it": every sentence owes the reader something

The reader gives each sentence a moment of attention. A sentence that returns nothing (no fact, no reason, no step of the argument) wastes that moment and teaches the reader to skim. The author deletes such sentences even when they sound good.

What it looks like:
- **Filler:** "here's the catch", "and it's a sneaky one", "that's what makes it hard, and also what makes it fun".
- **Promotion:** a stirring line that names no mechanism. Say what is done and why.
- **Machine-flavored phrasing:** titles built on a count or a rhyme ("Three tricks, three practices"), chains of punchy fragments, color words used as shorthand ("all green"). Name things by what they do.
- **A generic truth offered as an insight**, such as "don't trade the goal for the rule". If every reader would nod and learn nothing, cut it.
- **A shallow insight**, one the audience already practices. Ask what is different in the new setting, and say that.
- **An insight from nowhere:** a striking claim with no reason behind it. Find the deeper reason and say it first.
- **Digressions:** the history of a field, a citation that needs explaining, future work, a second problem the talk doesn't resolve. Being true and interesting is not enough; a sentence must be on the line.

| Before | After |
|---|---|
| "And that's where it gets interesting." | Cut. |
| "Build in the alarms, so the first wrong turn rings a bell." | The concrete things the reader has to do, each in a plain clause. |
| "Keep a list of past mistakes." (everyone already does this) | What that list gives in the new setting that it didn't before, and why. |

## 4. "That's not what I meant": the talk carries the author's idea

The talk is the author's argument, made in public. A smoother sentence that shifts the meaning is a step backwards, however well it reads.

What it looks like:
- **A rewrite that drifts.** A specific point becomes a generic one, as when "the delay is itself a signal" turns into "it's slow".
- **A key term read in another sense.** The author's word may mean something narrower than its usual meaning, or something different.
- **A working transition from the outline replaced.** Reuse the author's links where they already work.
- **A choice presented as settled.** When the author offered candidates, for a term or a framing, say which one you picked and why, and let them confirm it.

At the start, write down what each point and each key term means to the author, and confirm it with them. Check every rewrite against that list.

## 5. "It's hard to watch": one pair of eyes, and the viewer sets the pace

A viewer can either read or watch, not both at once. They also expect the talk to go where they tell it to. The author corrects anything that splits their attention or takes control away from them.

What it looks like:
- **Two things moving at once.** Put the subtitles on the picture, not under it. Text on the stage doesn't repeat the voice.
- **Text where a picture should be.** If the stage needs a sentence, animate the mechanism instead. Keep the screen to labels and key numbers.
- **Emphasis out of proportion.** The main items get most of the stage. What the audience already knows gets one scene.
- **A page with no motion.** The author wants the talk lively. When a scene is busy, cut text and side elements, not the animation.
- **Controls that skip content.** Next goes to the next sentence, never past something the viewer hasn't heard.
- **Sound that doesn't work as heard.** The music must be heard on laptop speakers, stay under the voice, and start however the viewer moves. The voice must match the text exactly.
- **A voice that undercuts the content.** A robotic, old-sounding or childish voice makes a serious talk feel less serious.
- **A burden up front.** Lead with what something does for the reader, not with what it will ask of them, such as approvals, prompts or setup.
- **The wrong order for the medium.** A viewer can follow a walkthrough. A reader on a page needs the point first, then only the details that help.

## 6. One stop, many fixes

When the author stops at one sentence, the cause is usually a habit, and a habit shows up everywhere. Find every instance: in the narration, on the stage and in the article, in both languages. Fix them all, re-render the voice, and say how many you found.

## Before you show anything

Play the whole talk and read the whole article, as the author will. At each sentence, ask:
1. Could someone with none of the author's context follow this?
2. Would a skeptical peer accept it as stated?
3. What does the reader get from it?
4. Is it still what the author meant?
5. Is it easy to watch, and does it go where the viewer tells it to?
