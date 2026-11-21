#!/usr/bin/env python3
"""Put an article (a JSON file) into a talk page, as the text under the player.

The article is written for reading, apart from the narration, which follows the talk.

  python3 make_article.py --page path/to/talk/index.html --article path/to/article/en.json

Article format:
  {"summary": "Read it as an article",
   "sections": [{"h": "Section title",
                 "p": ["a paragraph",
                       {"insight": "a highlighted line, readable on its own"},
                       {"list": ["numbered item", "..."]},
                       {"link": {"href": "https://...", "text": "Project on GitHub →"}}],
                 "fig": {"scene": "scene-id", "step": 2, "after": 1, "caption": "What to see in it."}}]}
`fig` draws that scene, frozen at that step, after item `after` (default: the last item).
"""
import argparse, json, re


def block(path):
    data = json.load(open(path, encoding="utf-8"))
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def inject(page_text, article_json):
    tag = re.compile(r'(<script type="application/json" id="article">)(.*?)(</script>)', re.S)
    if not tag.search(page_text):
        raise SystemExit("the page has no article block")
    return tag.sub(lambda m: m.group(1) + article_json + m.group(3), page_text, count=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", required=True)
    ap.add_argument("--article", required=True)
    a = ap.parse_args()
    s = open(a.page, encoding="utf-8").read()
    open(a.page, "w", encoding="utf-8").write(inject(s, block(a.article)))
    print("article in", a.page)
