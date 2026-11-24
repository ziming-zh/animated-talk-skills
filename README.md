# animated-talk

A Claude Code skill that turns a rough outline (a slide deck, talk notes, the argument of a paper) into a narrated, animated web talk people can follow. The talk plays in the browser as an SVG scene player with voice, subtitles and music. Under the player sits a separate article written for reading. A Chinese version is optional.

The skill is about more than drawing. Most of what it holds is why an outline isn't yet a talk, and what an author corrects when they watch a draft as a first-time viewer would: whatever they can't follow, don't believe, find empty, didn't mean, or find hard to watch.

For an example of a finished talk, see [How to use agents to build complex systems](https://aisys.me/blog/agentic-research-system-design/).

## Install

```bash
git clone https://github.com/ziming-zh/animated-talk-skills.git ~/.claude/skills/animated-talk
```

Claude Code picks it up in new sessions. Ask it to turn a deck or an idea into an animated talk, or type `/animated-talk`.

## The order of work

1. **Read the outline and set the frame.** Write each slide's claim as one sentence. Note what the author means by each point and each key term. Then fix the audience, the URL and the languages. List anything that needs private context, so it can be replaced.
2. **Write the spine and show it before drawing.** The spine is 10–15 sentences, one claim each, each following from the last. For a talk that argues for an approach, the arc is: problem → opportunity → twist → key insight → parts → tool → worked loop → three takeaways. Pick one running example that everyone knows.
3. **Plan scenes and steps.** A scene holds one idea. A step is one sentence group of narration paired with one change in the picture.
4. **Build the scenes.** Animate the mechanism rather than describing it. Use one main picture per scene, and put only labels and key numbers on screen.
5. **Write the narration.** Keep it spoken and plain, so that every sentence carries the point. Connect each scene to the one before it.
6. **Add the voice, subtitles and music.** Make one clip per step. Subtitles go on the picture. The music is an original loop that dips under the voice; check with `levels.py` that it can still be heard.
7. **Review, then play the whole thing through.** Use the checklists in `references/review.md`, ask a reader's questions of every scene, and step through it by hand.
8. **Write the article.** Write it separately from the narration, as a linear text. Each paragraph motivates its point first, then zooms in. Highlight the insights, add a few captioned stills, and end with three takeaways.
9. **Make the Chinese version.** Rewrite it rather than translate it, and keep engineering terms in English.
10. **Publish.** Commit only the talk's own files, then check the live pages once the push lands.

Each correction from the author is treated as a pattern. Find its cause, then fix every similar sentence, in both languages, along with the stage, the article and the voice.

## Contents

| Path | What it is |
|---|---|
| `SKILL.md` | The process, the principles, and how to work with the author |
| `references/reasons.md` | Why the author corrects what they correct: five causes, with general examples |
| `references/story.md` | From outline to story line |
| `references/scenes.md` | Designing scenes |
| `references/narration.md` | Narration, voices, subtitles, music |
| `references/article.md` | The article under the player |
| `references/chinese.md` | The Chinese version |
| `references/engine.md` | The page engine, the scene API, the scripts, preview and deploy |
| `references/review.md` | Checklists before showing anything |
| `assets/template/index.html` | Starter page: engine, player, styles, three demo scenes, a sample article |
| `scripts/` | `make_voice.py`, `make_article.py`, `make_zh.py`, `make_music.py`, `levels.py` |

## Requirements

The page itself is a single HTML file with no build step. The scripts need Python 3 and macOS `afconvert`. They also need text-to-speech engines in `~/.local/share/tts`; `references/engine.md` lists what each one needs:

- **Kokoro**, which runs locally, for English;
- **edge-tts** for Chinese.
