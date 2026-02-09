#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIガバナンスブログを Type C（実務の問い→定義→運用5点→マッピング→失敗3例→チェックリスト→参考）で一本ずつ書き直す。
"""
import re
from pathlib import Path

from ai_governance_articles_data import get_article_data, OPERATIONAL_FIVE

BASE = Path(__file__).resolve().parent.parent
BLOG_DIR = BASE / "blog" / "ai-governance"

# prose ブロックの開始パターン（lead から）
PROSE_START = re.compile(r'(\s*<div className="prose prose-lg prose-slate[^>]*>\s*\n\s*<p className="lead text-xl text-slate-600 mb-10 leading-relaxed font-medium">)')
# prose の終端: </div> の直後に not-prose の div が来る
PROSE_END = re.compile(r'\n(\s*</div>\s*\n\s*<div className="not-prose mt-20 p-10 bg-slate-900)')

def _escape_js_template_literal(s):
    """JS テンプレートリテラル用にエスケープ（` \\ $ をエスケープ）。"""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

def _escape_jsx_attr_string(s):
    """JSX 属性内の文字列用（改行は \\n に、\\ と \" をエスケープ）。"""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")

def build_prose_content(slug, title, data):
    """Type C の本文（JSX）を組み立てる。インフォグラフィック3種（Mermaid×2、CompareCard×1）を記事別に挿入。"""
    q = data["question"]
    definition = data["definition"]
    mapping = data["mapping_note"]
    failures = data["failures"]
    unique = data["unique_sentence"]
    checklist = data["checklist"]
    refs = data["refs"]
    m1 = _escape_js_template_literal(data.get("mermaid_1", "graph LR\n    A[確認] --> B[記録]"))
    m2 = _escape_js_template_literal(data.get("mermaid_2", "graph TD\n    X[要件] --> Y[手続き]"))
    card_cap = _escape_jsx_attr_string(data.get("card_caption", "観点と失敗の対比"))
    card_lt = _escape_jsx_attr_string(data.get("card_left_title", "観点・要件"))
    card_rt = _escape_jsx_attr_string(data.get("card_right_title", "よくある失敗"))
    card_left_items = _escape_jsx_attr_string("\n".join(data.get("card_left_items", [])))
    card_right_items = _escape_jsx_attr_string("\n".join(data.get("card_right_items", [])))

    # 運用5点
    op_items = "\n".join(
        f'                                    <li><strong>{label}</strong>：{desc}</li>'
        for label, desc in OPERATIONAL_FIVE
    )

    # 失敗3例
    fail_items = "\n".join(f"                                    <li>{f}</li>" for f in failures)

    # チェックリスト
    cl_items = "\n".join(f"                                    <li>{c}</li>" for c in checklist)

    # 参考
    ref_items = "\n".join(
        f'                                    <li><a href="{url}" target="_blank" rel="noopener noreferrer" className="text-brand-blue hover:underline">{label}</a></li>'
        for label, url in refs
    )

    # KeyPoint の title は「固有の一文」。本文に unique 全文と CTA を入れる。
    keypoint_body = unique + " 相談・ロードマップ整理はお気軽にご連絡ください。"

    block = f'''                                <p className="lead text-xl text-slate-600 mb-10 leading-relaxed font-medium">
{q}
                                </p>

                                <h2>1. 定義を揃える</h2>
                                <p>{definition}</p>

                                <div className="not-prose my-8">
                                    <MermaidDiagram chart={{`{m1}`}} />
                                </div>

                                <h2>2. 最低限の運用要件（5点）</h2>
                                <ul className="list-disc pl-6 space-y-2">
{op_items}
                                </ul>

                                <h2>3. 規制・標準との対応関係（マッピング）</h2>
                                <p>{mapping}</p>

                                <div className="not-prose my-8">
                                    <MermaidDiagram chart={{`{m2}`}} />
                                </div>

                                <h2>4. 失敗パターン（現場で燃える3例）</h2>
                                <ul className="list-disc pl-6 space-y-2">
{fail_items}
                                </ul>

                                <CompareCard caption="{card_cap}" leftTitle="{card_lt}" leftItems={{"{card_left_items}"}} rightTitle="{card_rt}" rightItems={{"{card_right_items}"}} />

                                <KeyPoint title="固有の一文">
                                {keypoint_body}
                                </KeyPoint>

                                <h2>5. すぐ使えるチェックリスト</h2>
                                <ul className="list-disc pl-6 space-y-2">
{cl_items}
                                </ul>

                                <h2>6. 参考・参照</h2>
                                <ul className="list-disc pl-6 space-y-2 text-slate-700">
{ref_items}
                                </ul>'''
    return block


def extract_title(html_content):
    m = re.search(r'<meta property="og:title" content="([^"]+)"', html_content)
    return m.group(1) if m else ""


def main():
    count = 0
    for path in sorted(BLOG_DIR.glob("*.html")):
        if path.name == "index.html":
            continue
        slug = path.stem
        html = path.read_text(encoding="utf-8")
        title = extract_title(html)
        if not title:
            print(f"Skip (no og:title): {path.name}")
            continue
        data = get_article_data(slug, title)
        new_prose = build_prose_content(slug, title, data)

        # 置換: <p className="lead ... から </div>\n                        <div className="not-prose mt-20 の手前まで
        start_pat = re.compile(
            r'<p className="lead text-xl text-slate-600 mb-10 leading-relaxed font-medium">\s*\n.*?'
            r'(?=\s*</div>\s*\n\s*<div className="not-prose mt-20 p-10 bg-slate-900)',
            re.DOTALL
        )
        # 先に prose の開始 div の直後から、not-prose の直前までを取得するパターン
        pattern = re.compile(
            r'(<div className="prose prose-lg prose-slate prose-headings:font-bold prose-a:text-brand-blue hover:prose-a:text-blue-500 mx-auto">)\s*\n\s*'
            r'<p className="lead text-xl text-slate-600 mb-10 leading-relaxed font-medium">.*?'
            r'(\s*</div>\s*\n\s*<div className="not-prose mt-20 p-10 bg-slate-900 rounded-2xl text-center relative overflow-hidden">)',
            re.DOTALL
        )
        def repl(m):
            return m.group(1) + "\n" + new_prose + "\n                        " + m.group(2)
        new_html = pattern.sub(repl, html)
        if new_html == html:
            print(f"No match: {path.name}")
            continue
        path.write_text(new_html, encoding="utf-8")
        count += 1
        if count % 20 == 0:
            print(f"Done {count} ...")
    print(f"Rewrote {count} articles.")


if __name__ == "__main__":
    main()
