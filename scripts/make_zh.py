#!/usr/bin/env python3
"""Build the Simplified Chinese page of a talk from the English one.

  python3 make_zh.py --src talk/index.html --narr zh/narration.json --strings zh/strings.json [--article article/zh.json]
  python3 make_voice.py --page talk/index.html --lang zh

Writes talk/zh/index.html. Three inputs, all kept next to the talk's sources:

  narration.json  {"scene-id": {"title": "...", "steps": ["...", ...]}, ...}
                  The Chinese narration, rewritten (not translated) scene by scene, one string per step.
  strings.json    {"arrays":  {"<an exact JS array literal from the page>": ["...", "..."]},
                   "strings": {"<an exact string literal from the page>": "..."},
                   "raw":     [["<exact page text>", "<replacement>"], ...],
                   "meta":    {"description": "...", "og:title": "...", "og:description": "..."}}
                  Stage text. Arrays are replaced first (multi-line labels), then single string literals.
                  Template literals and anything else go in raw. Code, file and function names, and terms
                  an engineer reads as-is (agent, spec, cache, patch, workload, evict...) stay in English.
  article zh.json The Chinese article, same format as the English one.

The player's own interface (buttons, hints, language switch, fonts) is translated here.
Rerun after every edit to the English page, and read the warnings: a "not found" means an English
string changed and its Chinese entry no longer applies; a step-count mismatch means the Chinese
narration has to be updated for that scene.
"""
import argparse, importlib.util, json, os, re

UI_RAW = [
    ('<html lang="en">', '<html lang="zh-CN">'),
    ('--f-disp:"Bricolage Grotesque","Inter",system-ui,sans-serif;',
     '--f-disp:"Bricolage Grotesque","Inter","PingFang SC","Hiragino Sans GB","Noto Sans SC","Microsoft YaHei",system-ui,sans-serif;'),
    ('--f-body:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;',
     '--f-body:"Inter","PingFang SC","Hiragino Sans GB","Noto Sans SC","Microsoft YaHei",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'),
    ('--f-mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;',
     '--f-mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,"PingFang SC","Noto Sans SC",monospace;'),
    # the language switch: on the Chinese page, 中文 is current and EN goes up one level
    ('<a href="./" aria-current="page" lang="en">EN</a><a href="zh/" lang="zh-CN">中文</a>',
     '<a href="../" lang="en">EN</a><a href="./" aria-current="page" lang="zh-CN">中文</a>'),
    ('<div class="hint" id="hint">click to continue →</div>', '<div class="hint" id="hint">点击继续 →</div>'),
    ('<p class="rotate">Turn your phone sideways for a bigger stage. Swipe or tap to step.</p>',
     '<p class="rotate">把手机横过来，画面更大。滑动或点击逐步播放。</p>'),
    ('<p class="keys"><kbd>→</kbd> or click: next step &nbsp;·&nbsp; <kbd>←</kbd> back &nbsp;·&nbsp; <kbd>P</kbd> play or pause &nbsp;·&nbsp; <kbd>M</kbd> sound on or off &nbsp;·&nbsp; <kbd>C</kbd> subtitles on or off &nbsp;·&nbsp; <kbd>F</kbd> full screen</p>',
     '<p class="keys"><kbd>→</kbd> 或点击：下一步 &nbsp;·&nbsp; <kbd>←</kbd> 上一步 &nbsp;·&nbsp; <kbd>P</kbd> 播放或暂停 &nbsp;·&nbsp; <kbd>M</kbd> 声音开关 &nbsp;·&nbsp; <kbd>C</kbd> 字幕开关 &nbsp;·&nbsp; <kbd>F</kbd> 全屏</p>'),
    ('<summary>Read it as an article</summary>', '<summary>阅读文章版</summary>'),
    ('fetch("music.m4a")', 'fetch("../music.m4a")'),
    ('`PART ${n + 1} OF ${PARTS.length} · FROM ${PARTS[n][2].toUpperCase()}`', '`第 ${n + 1} 部分 / 共 ${PARTS.length} · 来自 ${PARTS[n][2]}`'),
    ('`Scene ${i + 1}: ${SCENES[i].title}`', '`第 ${i + 1} 幕：${SCENES[i].title}`'),
]
UI_STRINGS = {
    "An animated story": "动画故事", "Play the story": "播放故事", "Play": "播放", "Pause": "暂停", "Replay": "重播",
    "Next step": "下一步", "Previous step": "上一步", "Scenes": "场景", "Full screen": "全屏",
    "Sound on": "声音开", "Sound off": "声音关", "Sound on: voice and music (M)": "声音开：配音和音乐（M）",
    "Sound off (M)": "声音关（M）", "Read it as an article": "阅读文章版",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="the English page")
    ap.add_argument("--narr", required=True)
    ap.add_argument("--strings", required=True)
    ap.add_argument("--article", default=None)
    a = ap.parse_args()
    dst = os.path.join(os.path.dirname(os.path.abspath(a.src)), "zh/index.html")
    s = open(a.src, encoding="utf-8").read()
    narr = json.load(open(a.narr, encoding="utf-8"))
    tr = json.load(open(a.strings, encoding="utf-8"))
    warn = []
    for x, y in UI_RAW + [tuple(p) for p in tr.get("raw", [])]:
        if x not in s:
            warn.append("not found: " + x[:70])
        s = s.replace(x, y)
    for k, v in tr.get("meta", {}).items():
        s = re.sub(r'(<meta (?:name|property)="' + re.escape(k) + r'" content=")[^"]*(")', lambda m: m.group(1) + v + m.group(2), s)

    # narration and titles, scene by scene
    def scene(m):
        sid, en = m.group(2), json.loads(m.group(5))
        z = narr.get(sid)
        if not z:
            warn.append("no Chinese narration for scene " + sid)
            return m.group(0)
        if len(z["steps"]) != len(en):
            warn.append(f"{sid}: {len(en)} English steps, {len(z['steps'])} Chinese")
        steps = "[\n" + ",\n".join("    " + json.dumps(t, ensure_ascii=False) for t in z["steps"]) + "\n  ]"
        return m.group(1) + sid + m.group(3) + json.dumps(z["title"], ensure_ascii=False) + m.group(4) + steps + m.group(6)
    s = re.sub(r'(id: ")([^"]+)(", act: \d+, title: )"[^"]*"(,\n  steps: )(\[.*?\])(,\n  svg\(\))', scene, s, flags=re.S)

    # stage text: whole arrays first, then single literals (the narration is already Chinese, so it is left alone)
    for x, y in tr.get("arrays", {}).items():
        if x not in s:
            warn.append("array not found: " + x[:60])
        s = s.replace(x, json.dumps(y, ensure_ascii=False))
    strings = {**UI_STRINGS, **tr.get("strings", {})}
    s = re.sub(r'"((?:[^"\\\n]|\\.)*)"', lambda m: json.dumps(strings[m.group(1)], ensure_ascii=False) if m.group(1) in strings else m.group(0), s)

    if a.article:
        here = os.path.dirname(os.path.abspath(__file__))
        spec = importlib.util.spec_from_file_location("make_article", os.path.join(here, "make_article.py"))
        art = importlib.util.module_from_spec(spec); spec.loader.exec_module(art)
        s = art.inject(s, art.block(a.article))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(s)
    for w in warn:
        print("warning:", w)
    print("wrote", dst)


if __name__ == "__main__":
    main()
