# The Chinese version

The Chinese page is built from the English one by `scripts/make_zh.py`. The narration, stage text and article are each **rewritten** in Simplified Chinese, not translated. The coherence of the narrative matters most: "叙事线索逻辑连贯是最重要的".

## 1. Terms that stay in English

Engineers read many technical terms as-is. Translating them makes the text harder to read, not easier. In the first talk these stayed in English:

agent, spec, check, patch, workload, cache, evict / eviction, nightly job, writer, invariant, ban, module, silent failure, differential testing, patch overfitting, reward hacking, test suite, hit rate, step back, LRU, workaround, refine.

The author rejected these translations:
- 夜间任务 for nightly job
- 淘汰 for evict
- 写者 for writer

For a term the reader may not know, add the expansion once: "LRU（最近最少使用）".

## 2. Natural Chinese, without 翻译腔 (translationese)

Signs of translated Chinese, and their fixes:

| Translated | Natural |
|---|---|
| 由于……因此…… | 既然……就…… / 因为……所以…… |
| 然而 | 可 / 不过 / 但 |
| 构建 | 搭 / 做 |
| 一个任务所需的工作量，是关于其上层设计的证据。 | 一个任务花了多少工夫，能从侧面反映出它上面的设计合不合适。 |
| 抗拒每一次修改 | 处处别扭 |
| 在无人察觉的情况下违反 | 悄悄违反 |
| 自底向上 / 自顶向下 | 从下往上 / 从上往下 |
| 彼此制衡 | 互相牵制 |
| 当系统随后在更多 workload 上测试时，小故障便到处出现 | 系统一换到更多 workload 上测试，小毛病就到处冒出来 |

Long English-style clauses become several short Chinese clauses. A sentence that keeps its English word order reads stiff even when every word is right.

Colloquial words are a case-by-case choice, never a blanket substitution:
- 工夫 for 工作量 read well in "一个任务花了多少工夫" (how much effort a task took). But the bare "看这份工夫" (look at this effort) was flagged as unclear.
- 挂了 for a failed test is slang. Use it only where the tone is casual and the meaning is obvious.

## 3. Concise and clear

- **Stage text is shortest.** "让副本保持新鲜，在写入导致过期、并且以任意顺序到达时" became three labels: 保持副本新鲜 / 过期源于写入 / 写入可能乱序.
- **One idea per sentence.** "每条 ban 记录的是一种失败做法搞错了的 workload 特性，所以这些 ban 合在一起，描述的正是抽象必须适应的那个问题" became "每条 ban 都记下了 workload 的一个特性。ban 积累得越多，问题就定义得越清楚。"
- **No vague words.**
  - "不崩溃" doesn't say what is meant.
  - "看这份工夫" (look at this effort): what exactly do you look at?
  - "研究系统没有那么多可依靠的" (research systems have little to rely on): rely on what?
  - Say the thing: "只要看 agent 把这些次数花在了什么上" (just look at what the agent spent those runs on).
- **The key line stays short.** "这就是 silent failure：系统没崩，也没报错，check 全都通过，可抽象从一开始就错了。所以不能等东西坏了再说。" was too long. It became: "这就是 silent failure：check 全都通过，可抽象从一开始就错了。"
- **Sentences connect.** Each sentence follows from the last with 所以, 可是, 于是 or 这说明. Paragraphs where "句子与句子之间逻辑不通顺" (the sentences don't follow from each other) were the most common Chinese complaint.

## 4. Highlighted insights in Chinese

Each one must read like something a Chinese writer would say:

- "Agent 决定代码放在哪里，看的是它什么时候运行，而不是它属于哪个设计。"
- "旧版本哪怕满是 patch，它做对的那部分，仍然值得拿来对照。"
- "研究系统的抽象不是先设计好再去实现的，而是在写代码的过程中一点点摸索出来的。"
- "Agent 用来钻 check 空子的那种搜索，正好也能用来找出 check 的漏洞，所以要在动手之前先让它找一遍。"

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

   In the first talk, a later change to the page header (a language switch) and a new keyboard hint went into the English page only. The Chinese page then shipped with an English keyboard hint and a language switch that pointed to `zh/zh/`. A warning had flagged it, and nobody read it.
6. Open the Chinese page in the browser pane, step through it, and play some clips.

The script already translates the player's own interface: the buttons, the hints, the language switch with 中文 marked current, and the CJK font fallbacks.

## 6. Voice

edge-tts `zh-CN-YunjianNeural` at −4% (see `narration.md` §4). Pronunciation rules for Chinese:
- `v2` → 版本2;
- `GPU` is spelled out letter by letter;
- `90%` → 百分之90.

## 7. Review pass for Chinese

1. Read the narration of each scene aloud in order. Check that each sentence follows from the last.
2. Read the stage labels alone. Are they short, and do they read naturally?
3. Read the article for 翻译腔 (translationese), using the table above, and fix every instance, not only the one you spotted.
4. Check that the English terms are kept consistently, and never mixed with a translation of the same term.
