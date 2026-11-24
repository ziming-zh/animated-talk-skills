# The Chinese version

The Chinese page is built from the English one by `scripts/make_zh.py`. The narration, stage text and article are each **rewritten** in Simplified Chinese, not translated. What matters most is that the story line holds together and each sentence follows from the last.

## 1. Terms that stay in English

Engineers read many technical terms as-is. Translating them makes the text harder to read, not easier. Keep in English:
- the field's working vocabulary, such as cache, patch, workload, module, test suite, hit rate;
- named techniques and concepts, such as garbage collection or load balancing;
- code, file and function names.

A literal translation of such a term, such as 夜间任务 for nightly job, reads worse than the English word.

For a term the reader may not know, add the expansion once: "LRU（最近最少使用）".

Keep each term the same throughout. Never mix it with a translation of itself.

## 2. Natural Chinese, without 翻译腔 (translationese)

Signs of translated Chinese, and their fixes:

| Translated | Natural |
|---|---|
| 由于……因此…… | 既然……就…… / 因为……所以…… |
| 然而 | 可 / 不过 / 但 |
| 构建 | 搭 / 做 |
| 自底向上 / 自顶向下 | 从下往上 / 从上往下 |
| 彼此制衡 | 互相牵制 |
| 在无人察觉的情况下违反 | 悄悄违反 |
| 抗拒每一次修改 | 处处别扭 |
| 当……时，……便…… | 一……就…… |
| ……是关于……的证据 | ……能从侧面反映出…… |

Long English-style clauses become several short Chinese clauses. A sentence that keeps its English word order reads stiff even when every word is right.

Colloquial words are a case-by-case choice, never a blanket substitution:
- A colloquial word can read well in a full phrase ("花了多少工夫") and be unclear on its own ("看这份工夫").
- Slang (挂了 for a failed test) fits only where the tone is casual and the meaning is obvious.

## 3. Concise and clear

- **Stage text is shortest.** A long clause on the stage becomes two or three short labels, each one idea.
- **One idea per sentence.** A sentence that holds a cause, a consequence and a conclusion becomes two or three sentences.
- **No vague words.** "不崩溃" doesn't say what is meant, and "研究系统没有那么多可依靠的" leaves the reader asking: rely on what? Say the thing itself.
- **The key line stays short.** Cut any clause that only restates or adds a second point.
- **Sentences connect.** Each sentence follows from the last with 所以, 可是, 于是 or 这说明. Paragraphs where the sentences don't follow from each other are the most common problem in the Chinese.

## 4. Highlighted insights in Chinese

Each one must read like something a Chinese writer would say, not a translated English sentence:
- one claim, with its subject clear;
- the contrast or the reason inside the sentence (……，而不是…… / 哪怕……，也……);
- short enough to read in one breath.

## 5. Building it

1. Write `zh/narration.json`: `{"scene-id": {"title": "...", "steps": [...]}}`, with one string per English step.
2. Write `zh/strings.json` with these keys:
   - `arrays`: the exact JS array literal from the page → Chinese array. Use this for multi-line labels and for `ACTS`, `RAIL` and `PARTS`.
   - `strings`: the exact string literal → Chinese.
   - `raw`: template literals, the `<title>`, the date, and anything else.
   - `meta`: description and og tags.
3. Write `article/zh.json` in the same format as the English article.
4. Run `python3 make_zh.py --src talk/index.html --narr … --strings … --article …`, then `python3 make_voice.py --page talk/index.html --lang zh`.
5. **Read the warnings every time.**
   - A "not found" means the English changed and the Chinese entry no longer applies.
   - A step-count mismatch means a scene's Chinese narration is out of date.

   A change to the English page's header or hints reaches the Chinese page only if `strings.json` covers it. Otherwise the Chinese page ships with English in it, or with a broken link, and the only sign is the warning.
6. Open the Chinese page in the browser pane, step through it, and play some clips.

The script already translates the player's own interface: the buttons, the hints, the language switch with 中文 marked current, and the CJK font fallbacks.

## 6. Voice

The default is edge-tts `zh-CN-YunjianNeural` at −4% (see `narration.md` §4). Pronunciation rules for Chinese:
- `v2` → 版本2;
- `GPU` is spelled out letter by letter;
- `90%` → 百分之90.

## 7. Review pass for Chinese

1. Read the narration of each scene aloud in order. Check that each sentence follows from the last.
2. Read the stage labels alone. Are they short, and do they read naturally?
3. Read the article for 翻译腔 (translationese), using the table above. Fix every instance, not only the one you spotted.
4. Check that the English terms are kept consistently, and never mixed with a translation of the same term.
