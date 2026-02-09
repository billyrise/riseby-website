#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
既存の AIガバナンス記事 HTML に「前の記事」「次の記事」「カテゴリに戻る」「関連記事3件」の
ナビゲーションを一括で差し込む。apply_llm_article.py で新規生成する記事には最初から含まれるため、
本スクリプトはナビ未対応の既存ファイルのみを更新する。
使い方:
  python scripts/patch_article_nav.py           # ナビ未対応の記事のみに挿入
  python scripts/patch_article_nav.py --refresh # 全記事の articleNav と関連記事ブロックを再計算で上書き
"""
import re
import sys
from pathlib import Path

# apply_llm_article の関数を利用
sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_llm_article import (
    OUT_DIR,
    parse_design_full_list,
    build_article_nav_js_and_jsx,
)


def refresh_one(path, article_nav_js, nav_related_jsx):
    """既にナビがある HTML の articleNav 行とナビ・関連ブロックを再計算結果で置換する。戻り値: 'refreshed' | 'no_match'。"""
    text = path.read_text(encoding="utf-8")
    if "const articleNav =" not in text:
        return "no_match"
    # 1) const articleNav = { ... }; の行を置換（1行で書かれている想定）
    article_nav_pattern = re.compile(
        r"const articleNav = \{.*?\};",
        re.DOTALL,
    )
    if not article_nav_pattern.search(text):
        return "no_match"
    text = article_nav_pattern.sub(article_nav_js, text, count=1)
    # 2) ナビ・関連ブロック（mt-12 の div のみ）を置換。nav_related_jsx はすでに </div> で終わるので、
    #    suffix の「ナビの</div>」は削除し「content の </div>」と CTA だけ残す（</div> が1つ多いと DOM が壊れる）
    start_marker = "not-prose mt-12 pt-8 border-t border-slate-200 space-y-8"
    # suffix = ナビの</div> + contentの</div> + CTA。ナビは新 jsx で置換するので、残すのは contentの</div> 以降のみ
    suffix = "                        </div>\n                        </div>\n                        <div className=\"not-prose mt-20 p-10 bg-slate-900"
    pos = text.find(start_marker)
    if pos == -1:
        return "no_match"
    line_start = text.rfind("\n", 0, pos) + 1
    if pos > 0 and line_start == 1:
        line_start = 0
    suffix_pos = text.find(suffix)
    if suffix_pos == -1:
        return "no_match"
    # 残すのは2つ目の "</div>\n" 以降（content の閉じタグ + CTA）。1つ目はナビの閉じなので捨てる
    first_div_close = "                        </div>\n"
    replace_end = suffix_pos + len(first_div_close)
    text = text[:line_start] + nav_related_jsx.strip() + text[replace_end:]
    path.write_text(text, encoding="utf-8")
    return "refreshed"


def patch_one(path, article_nav_js, nav_related_jsx):
    """1つの HTML に articleNav とナビ・関連ブロックを挿入する。戻り値: 'patched' | 'already_has_nav' | 'no_match'。"""
    text = path.read_text(encoding="utf-8")
    if "const articleNav =" in text:
        return "already_has_nav"
    # 1) <script type="text/babel"> の直後に articleNav を挿入
    pattern1 = re.compile(
        r'(<script type="text/babel">)\s*\n(\s*)(const \{\s*useState)',
        re.MULTILINE,
    )
    if not pattern1.search(text):
        return "no_match"
    text = pattern1.sub(
        r"\1\n\2" + article_nav_js + r"\n\2\3",
        text,
        count=1,
    )
    # 2) 「次の一歩」の段落終了（</p> または />）と CTA の間にナビ・関連ブロックを挿入
    # 既存ファイルは <p dangerouslySetInnerHTML=... /> で閉じている
    pattern2 = re.compile(
        r'( />\s*\n)(\s*</div>\s*\n\s*<div className="not-prose mt-20 p-10 bg-slate-900)',
        re.MULTILINE,
    )
    if not pattern2.search(text):
        # 新形式（apply で生成）は </p> で閉じている
        pattern2b = re.compile(
            r'(</p>\s*)\n(\s*)(</div>\s*\n\s*<div className="not-prose mt-20 p-10 bg-slate-900)',
            re.MULTILINE,
        )
        if not pattern2b.search(text):
            return "no_match"
        text = pattern2b.sub(
            r"\1\n" + nav_related_jsx + r"\n\2\3",
            text,
            count=1,
        )
    else:
        text = pattern2.sub(
            r"\1" + nav_related_jsx + r"\n\2",
            text,
            count=1,
        )
    path.write_text(text, encoding="utf-8")
    return "patched"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Patch or refresh article nav in AI governance HTML")
    parser.add_argument("--refresh", action="store_true", help="Overwrite existing articleNav and related block for all articles")
    args = parser.parse_args()

    full_list = parse_design_full_list()
    by_slug = {a["slug"]: a["no"] for a in full_list}
    patched = 0
    refreshed = 0
    skipped_nav = 0
    skipped_no = 0
    no_match = 0
    for path in sorted(OUT_DIR.glob("*.html")):
        if path.name == "index.html":
            continue
        slug = path.stem
        no = by_slug.get(slug)
        if no is None:
            skipped_no += 1
            continue
        article_nav_js, nav_related_jsx = build_article_nav_js_and_jsx(no)
        if args.refresh:
            result = refresh_one(path, article_nav_js, nav_related_jsx)
            if result == "refreshed":
                refreshed += 1
                print(path.name)
            else:
                no_match += 1
        else:
            result = patch_one(path, article_nav_js, nav_related_jsx)
            if result == "patched":
                patched += 1
                print(path.name)
            elif result == "already_has_nav":
                skipped_nav += 1
            else:
                no_match += 1
    if args.refresh:
        print(f"Refreshed: {refreshed}, slug not in list: {skipped_no}, no_match: {no_match}")
    else:
        print(f"Patched: {patched}, already had nav: {skipped_nav}, slug not in list: {skipped_no}, no_match: {no_match}")


if __name__ == "__main__":
    main()
