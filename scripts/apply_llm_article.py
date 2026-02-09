#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cursor で作成したマークダウン（本文＋図1・図2・図3）をパースし、
該当記事の HTML を更新する。
使い方: python apply_llm_article.py <記事番号> <作成した出力.md>
  または: python apply_llm_article.py <記事番号>  # 標準入力から読み取り
"""
import csv
import html as html_module
import re
import sys
from pathlib import Path


def markdown_strong_to_bold_underline(s, for_jsx=False):
    """**で囲まれた部分を太字＋下線のHTMLに変換し、アスタリスクは表示しない。for_jsx=True のときは className（JSX用）、False のときは class（HTML innerHTML用）。"""
    if not s or not isinstance(s, str):
        return s
    attr = 'className' if for_jsx else 'class'
    parts = re.split(r"\*\*([^*]+)\*\*", s)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            out.append(html_module.escape(part))
        else:
            out.append(f"<strong {attr}=\"font-bold underline\">" + html_module.escape(part) + "</strong>")
    return "".join(out)

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "blog" / "ai-governance"
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
FIGURE_HISTORY_PATH = BASE_DIR / "docs" / "ai-governance-briefs" / "figure_usage_history.csv"

# テンプレート → セクション（一覧のサブカテゴリ・関連記事用）
TEMPLATE_TO_SECTION = {
    "T01": "A", "T02": "A", "T03": "A", "T04": "A", "T05": "A",
    "T06": "B", "T07": "B", "T08": "B", "T09": "B", "T10": "B",
    "T11": "C", "T12": "C", "T13": "C", "T14": "C", "T15": "C",
    "T16": "D", "T17": "D", "T18": "D", "T19": "D", "T20": "D",
    "T21": "E", "T22": "E", "T23": "E", "T24": "E", "T25": "I",
    "T26": "F", "T27": "F", "T28": "F", "T29": "F", "T30": "F",
    "T31": "G", "T32": "G",
}

# 関連記事用：同一セクションは最大1件、残り2件は「テーマ的に近い」他セクションから選ぶための親和性マップ
# A=Governance, B=Risk, C=Lifecycle, D=Evidence, E=Security, F=Privacy, G=Legal, I=Procurement
SECTION_AFFINITY = {
    "A": ["B", "D"],   # 統治 ↔ リスク・証跡
    "B": ["D", "A"],   # リスク ↔ 証跡・統治
    "C": ["D", "E"],   # ライフサイクル ↔ 証跡・セキュリティ
    "D": ["B", "C"],   # 証跡 ↔ リスク・ライフサイクル
    "E": ["I", "C"],   # セキュリティ ↔ 調達・ライフサイクル
    "F": ["G", "D"],   # プライバシー ↔ 法務・証跡
    "G": ["F", "D"],   # 法務 ↔ プライバシー・証跡
    "I": ["E", "B"],   # 調達 ↔ セキュリティ・リスク
}


def parse_design_full_list():
    """設計図の 3.2 と 3.3 から全163記事の順序付き一覧を返す。[{no, slug, title_ja, section}, ...]"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    table_32 = []  # no, slug, template_id
    table_33 = []  # no, slug, title_ja
    in_32 = False
    in_33 = False
    for line in text.splitlines():
        if "### 3.2 163記事" in line:
            in_32 = True
            in_33 = False
            continue
        if "### 3.3 記事DNA" in line:
            in_32 = False
            in_33 = True
            continue
        if in_32 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3 and parts[0].isdigit():
                no = int(parts[0])
                if no >= 1 and no <= 163:
                    table_32.append({"no": no, "slug": parts[1], "template_id": parts[2] if len(parts) > 2 else "T01"})
        if in_33 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit():
                no = int(parts[0])
                if no >= 1 and no <= 163:
                    table_33.append({"no": no, "slug": parts[1], "title_ja": parts[2]})
    by_no_32 = {r["no"]: r for r in table_32}
    by_no_33 = {r["no"]: r for r in table_33}
    merged = []
    for no in range(1, 164):
        r33 = by_no_33.get(no)
        r32 = by_no_32.get(no)
        if not r33:
            continue
        tid = (r32 or {}).get("template_id") or "T01"
        sec = TEMPLATE_TO_SECTION.get(tid, "A")
        merged.append({
            "no": no,
            "slug": r33["slug"],
            "title_ja": r33["title_ja"],
            "section": sec,
        })
    return merged


def get_nav_and_related(no, full_list):
    """記事番号 no に対する「前・次・カテゴリに戻る」と関連記事3件を返す。
    関連記事ルール: 同一カテゴリ（section）は最大1件、残り2件は別カテゴリでテーマ的に近い記事（SECTION_AFFINITY を優先）。候補は no より大きい番号のみ（前へ戻らない）。"""
    index_by_no = {a["no"]: i for i, a in enumerate(full_list)}
    if no not in index_by_no:
        return {"prev": None, "next": None, "related": []}
    idx = index_by_no[no]
    prev_a = full_list[idx - 1] if idx > 0 else None
    next_a = full_list[idx + 1] if idx + 1 < len(full_list) else None
    current_sec = full_list[idx]["section"]
    rest = full_list[idx + 1:]  # no より大きい番号のみ

    # 同一セクションは最大1件
    same_sec = [a for a in rest if a["section"] == current_sec][:1]
    other_sec = [a for a in rest if a["section"] != current_sec]

    # 残り2件は別カテゴリ。親和性の高いセクションを優先し、2つは異なるセクションから1件ずつ
    affinity = SECTION_AFFINITY.get(current_sec, [])
    used_sec = set()
    other_related = []
    for sec in affinity:
        if len(other_related) >= 2:
            break
        for a in other_sec:
            if a["section"] == sec and a["section"] not in used_sec:
                other_related.append(a)
                used_sec.add(a["section"])
                break
    for a in other_sec:
        if len(other_related) >= 2:
            break
        if a["section"] not in used_sec:
            other_related.append(a)
            used_sec.add(a["section"])

    related = (same_sec + other_related)[:3]
    return {"prev": prev_a, "next": next_a, "related": related}


def build_article_nav_js_and_jsx(no):
    """記事番号 no 用の articleNav の JS 行とナビ・関連記事の JSX ブロックを返す。(article_nav_js, nav_related_jsx)"""
    full_list = parse_design_full_list()
    nav_related = get_nav_and_related(no, full_list)
    prev_str = "null"
    if nav_related["prev"]:
        p = nav_related["prev"]
        prev_str = '{{ slug: "{}", title_ja: "{}" }}'.format(p["slug"], esc_js(p["title_ja"]))
    next_str = "null"
    if nav_related["next"]:
        n = nav_related["next"]
        next_str = '{{ slug: "{}", title_ja: "{}" }}'.format(n["slug"], esc_js(n["title_ja"]))
    related_parts = [
        '{{ slug: "{}", title_ja: "{}" }}'.format(r["slug"], esc_js(r["title_ja"]))
        for r in nav_related["related"]
    ]
    article_nav_js = "const articleNav = {{ prev: {}, next: {}, related: [ {} ] }};".format(
        prev_str, next_str, ", ".join(related_parts)
    )
    nav_related_jsx = """
                        <div id="article-nav" className="not-prose mt-12 pt-8 border-t border-slate-200 space-y-8">
                            <div className="flex flex-wrap items-center justify-between gap-4">
                                <div className="flex flex-wrap items-center gap-6">
                                    {articleNav.prev && <a href={articleNav.prev.slug + ".html"} className="text-brand-blue hover:underline font-medium">← 前の記事：{articleNav.prev.title_ja}</a>}
                                    {articleNav.next && <a href={articleNav.next.slug + ".html"} className="text-brand-blue hover:underline font-medium">次の記事：{articleNav.next.title_ja} →</a>}
                                </div>
                                <a href="index.html" className="text-slate-600 hover:text-slate-900 font-medium">カテゴリに戻る</a>
                            </div>
                            <div>
                                <h3 className="text-lg font-bold text-slate-900 mb-4">関連記事</h3>
                                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                                    {articleNav.related.map((r, i) => <a key={i} href={r.slug + ".html"} className="block p-5 rounded-xl border border-slate-200 hover:border-brand-blue hover:shadow-md transition"><div className="flex flex-wrap gap-2 mb-2"><span className="bg-red-100 text-red-800 text-xs px-3 py-1 rounded-full font-bold tracking-wide uppercase font-display">AIガバナンス</span><span className="bg-slate-100 text-slate-600 text-xs px-3 py-1 rounded-full font-bold tracking-wide">実装・証跡</span></div><p className="font-bold text-slate-900 mt-1">{r.title_ja}</p></a>)}
                                </div>
                            </div>
                        </div>"""
    return article_nav_js, nav_related_jsx


def parse_design_for_article(no):
    """設計図から記事 no の slug, title_ja, op を取得。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    in_33 = False
    for line in text.splitlines():
        if "### 3.3 記事DNA" in line:
            in_33 = True
            continue
        if in_33 and line.strip().startswith("|") and "|---" not in line and "| No. |" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit() and int(parts[0]) == no:
                op = int(parts[8]) if parts[8].isdigit() else ""
                return {"slug": parts[1], "title_ja": parts[2], "op": op}
    return None


def parse_llm_output(md_text):
    """LLM出力Markdownをパースし、リード・本文・図1〜3・固有の一文・チェックリスト・参考文献・次の一歩を返す。"""
    out = {
        "lead": "",
        "body_sections": [],  # [(heading, html_content), ...] 図挿入は placeholder
        "mermaid1": "",
        "mermaid2": "",
        "mermaid3": "",
        "key_sentence": "",
        "checklist": [],
        "references": "",
        "next_steps": "",
    }
    # 図1・図2・図3を抽出（## 図N（形式）の次のコードブロック）。形式は Mermaid / SVG / HTML / Table 等
    pos = 0
    for i in range(1, 4):
        pat = re.compile(
            r"## 図" + str(i) + r"[（(]([^)）]+)[)）]\s*\n```(?:\w*)\s*\n(.*?)```",
            re.DOTALL,
        )
        m = pat.search(md_text[pos:])
        if m:
            fmt = (m.group(1) or "").strip()
            content = (m.group(2) or "").strip()
            out[f"fig{i}_fmt"] = fmt
            out[f"fig{i}_content"] = content
            out[f"mermaid{i}"] = content if fmt.lower() == "mermaid" else ""
            pos += m.end()
        else:
            out[f"fig{i}_fmt"] = ""
            out[f"fig{i}_content"] = ""
            out[f"mermaid{i}"] = ""
            pos = len(md_text)
    # 後方互換: 新形式で1つも取れていないときだけ従来の Mermaid パターンを試す
    if not (out.get("fig1_fmt") or out.get("fig2_fmt") or out.get("fig3_fmt")):
        mermaid_blocks = re.findall(
            r"## 図[123][（(]Mermaid[)）]\s*\n```(?:mermaid)?\s*\n(.*?)```",
            md_text,
            re.DOTALL,
        )
        if len(mermaid_blocks) >= 3:
            for i, b in enumerate(mermaid_blocks[:3]):
                out[f"mermaid{i+1}"] = b.strip()
                out[f"fig{i+1}_fmt"] = "Mermaid"
                out[f"fig{i+1}_content"] = b.strip()

    # リード
    m = re.search(r"## リード[（(]1段落[)）]\s*\n(.*?)(?=\n## )", md_text, re.DOTALL)
    if m:
        out["lead"] = m.group(1).strip()

    # 本文（## 本文 から ## 図1 まで。見出しと段落をHTMLに変換）
    m = re.search(r"## 本文\s*\n(.*?)(?=\n## 図1)", md_text, re.DOTALL)
    if m:
        body_raw = m.group(1).strip()
        # 「ここに図Nを挿入」をプレースホルダーに
        body_raw = re.sub(r"ここに図1を挿入", "{{MERMAID1}}", body_raw, flags=re.I)
        body_raw = re.sub(r"ここに図2を挿入", "{{MERMAID2}}", body_raw, flags=re.I)
        body_raw = re.sub(r"ここに図3を挿入", "{{MERMAID3}}", body_raw, flags=re.I)
        # ### 見出し → <h2>、段落 → <p>
        lines = body_raw.split("\n")
        current_para = []
        for line in lines:
            if line.strip().startswith("### "):
                if current_para:
                    out["body_sections"].append(("", "".join(current_para)))
                    current_para = []
                out["body_sections"].append((line.replace("###", "").strip(), ""))
            elif line.strip() and not line.strip().startswith("#"):
                if current_para:
                    current_para.append(" ")
                current_para.append(line.strip())
            elif line.strip() == "{{MERMAID1}}" or line.strip() == "{{MERMAID2}}" or line.strip() == "{{MERMAID3}}":
                if current_para:
                    out["body_sections"].append(("", "".join(current_para)))
                    current_para = []
                out["body_sections"].append((f"PLACEHOLDER_{line.strip()}", ""))
        if current_para:
            out["body_sections"].append(("", "".join(current_para)))

    # 本文を取得し、図挿入位置で分割して body_parts に（[html, "M1", html, "M2", html, "M3", html]）
    m = re.search(r"## 本文\s*\n(.*?)(?=\n## 図1)", md_text, re.DOTALL)
    if m:
        body_one = m.group(1).strip()
        body_one = re.sub(r"ここに図1を挿入", "\n{{MERMAID1}}\n", body_one, flags=re.I)
        body_one = re.sub(r"ここに図2を挿入", "\n{{MERMAID2}}\n", body_one, flags=re.I)
        body_one = re.sub(r"ここに図3を挿入", "\n{{MERMAID3}}\n", body_one, flags=re.I)

        def md_to_html(block):
            out_lines = []
            for line in block.split("\n"):
                if line.strip().startswith("### "):
                    title = line.strip().lstrip("#").strip()
                    # 本文見出しで「次の一歩」は結論ブロックと重複するため、表示のみ「まとめとアクション」に置換
                    if title.strip() == "次の一歩" or re.match(r"^\d+\.\s*次の一歩\s*$", title.strip()):
                        title = re.sub(r"次の一歩", "まとめとアクション", title) if title else "まとめとアクション"
                    out_lines.append(f"<h2>{title}</h2>")
                elif line.strip().startswith("- "):
                    out_lines.append(f"<ul><li>{line.strip()[2:]}</li></ul>")
                elif line.strip() and not line.strip().startswith("{{MERMAID"):
                    out_lines.append(f"<p>{markdown_strong_to_bold_underline(line.strip(), for_jsx=True)}</p>")
            return "\n".join(out_lines)

        parts = []
        for seg in re.split(r"(\{\{MERMAID[123]\}\})", body_one):
            seg = seg.strip()
            if seg in ("{{MERMAID1}}", "{{MERMAID2}}", "{{MERMAID3}}"):
                parts.append(seg)
            elif seg:
                parts.append(md_to_html(seg))
        out["body_parts"] = parts if parts else [md_to_html(body_one)]
    else:
        out["body_parts"] = []

    # 固有の一文
    m = re.search(r"## 固有の一文[^\n]*\s*\n(.*?)(?=\n## |\Z)", md_text, re.DOTALL)
    if m:
        out["key_sentence"] = m.group(1).strip().strip("（）")

    # チェックリスト
    m = re.search(r"## チェックリスト[^\n]*\s*\n(.*?)(?=\n## |\Z)", md_text, re.DOTALL)
    if m:
        for line in m.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                out["checklist"].append(line[2:].strip())

    # 参考文献
    m = re.search(r"## 参考文献[^\n]*\s*\n(.*?)(?=\n## |\Z)", md_text, re.DOTALL)
    if m:
        out["references"] = m.group(1).strip()

    # 次の一歩
    m = re.search(r"## 次の一歩[^\n]*\s*\n(.*?)(?=\n## |\Z)", md_text, re.DOTALL)
    if m:
        out["next_steps"] = m.group(1).strip()

    # 図の型（記録用・必須）— A–J の記号を抽出
    m = re.search(r"## 図の型[^\n]*\s*\n(.*?)(?=\n## |\Z)", md_text, re.DOTALL)
    if m:
        block = m.group(1).strip()
        for pattern in [r"図1\s*:\s*([A-J])", r"図1\s*[：:]\s*([A-J])"]:
            g = re.search(pattern, block, re.I)
            if g:
                out["fig1_type"] = g.group(1).upper()
                break
        else:
            out["fig1_type"] = ""
        for pattern in [r"図2\s*:\s*([A-J])", r"図2\s*[：:]\s*([A-J])"]:
            g = re.search(pattern, block, re.I)
            if g:
                out["fig2_type"] = g.group(1).upper()
                break
        else:
            out["fig2_type"] = ""
        for pattern in [r"図3\s*:\s*([A-J])", r"図3\s*[：:]\s*([A-J])"]:
            g = re.search(pattern, block, re.I)
            if g:
                out["fig3_type"] = g.group(1).upper()
                break
        else:
            out["fig3_type"] = ""
    else:
        out["fig1_type"] = out["fig2_type"] = out["fig3_type"] = ""

    # 図の形式（記録用）— 形式名を取得（例: 図1: SVG, 図2: HTML）
    for i in range(1, 4):
        out[f"fig{i}_fmt_record"] = ""
    m = re.search(r"## 図の形式[^\n]*\s*\n(.*?)(?=\n## |\Z)", md_text, re.DOTALL)
    if m:
        block = m.group(1).strip()
        for i in range(1, 4):
            g = re.search(r"図" + str(i) + r"\s*[：:]\s*(\w+)", block)
            if g:
                out[f"fig{i}_fmt_record"] = g.group(1).strip()

    return out


def esc(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${").replace("\n", "\\n")


def esc_js(s):
    """JavaScript のダブルクォート文字列用のエスケープ。"""
    if not s or not isinstance(s, str):
        return ""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")


def esc_json(s):
    """JSON 文字列用のエスケープ（ld+json 等）。"""
    if not s or not isinstance(s, str):
        return ""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")


def esc_html_attr(s):
    """dangerouslySetInnerHTML 用のHTMLをJSテンプレートリテラルに埋め込むためのエスケープ。"""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${").replace("\n", "\\n").replace("</script>", "<\\/script>")


def _strip_internal_fig_codes(content):
    """図のキャプション・ラベルから読者不要な内部コード（T08 など）を除去する。"""
    if not content:
        return content
    return re.sub(r"[（(]T\d{2}[）)]", "", content)


# 図形幅に収めるための1行あたり最大文字数（幅120px・font-size11想定。はみ出さないよう控えめに）
_SVG_LABEL_MAX_CHARS_PER_LINE = 9  # 幅120px内に収める（はみ出し防止）。9で「証跡・監査提出目次」は1行に
_SVG_LINE_DY = 14
_SVG_BOX_Y = 20
_SVG_BOX_HEIGHT = 70
_SVG_BOX_CENTER_Y = _SVG_BOX_Y + _SVG_BOX_HEIGHT // 2  # 55


def _add_space_around_parens(s):
    """括弧（全角・半角）の前後に半角スペースを1つ入れ、折り返ししやすくする。"""
    if not s:
        return s
    s = re.sub(r"([^\s])([（(])", r"\1 \2", s)  # 開き括弧の前
    s = re.sub(r"([）)])([^\s])", r"\1 \2", s)  # 閉じ括弧の後
    return s


def _svg_wrap_parens_small(line):
    """図内の括弧とカッコ内の文字を1pt小さくする。SVG用に括弧部分を <tspan style="font-size:0.9em"> で囲む。"""
    if not line or ("（" not in line and "(" not in line):
        return html_module.escape(line)
    # 括弧ブロック（全角・半角）で分割。括弧ブロックは 0.9em の tspan で囲む
    parts = re.split(r"([（(][^）)]*[）)])", line)
    out = []
    for p in parts:
        if re.match(r"^[（(].*[）)]$", p):
            out.append('<tspan style="font-size:0.9em">' + html_module.escape(p) + "</tspan>")
        else:
            out.append(html_module.escape(p))
    return "".join(out)


def _split_label_to_lines(content, max_chars=_SVG_LABEL_MAX_CHARS_PER_LINE):
    """スペースで区切れるところを優先して複数行に分割。余計な末尾改行は作らない。"""
    content = content.strip().replace("\n", " ").replace("\r", "")
    if not content:
        return []
    if len(content) <= max_chars:
        return [content]
    lines = []
    rest = content
    while rest:
        rest = rest.strip()
        if not rest:
            break
        if len(rest) <= max_chars:
            lines.append(rest)
            break
        chunk = rest[: max_chars + 1]
        # 最後の半角スペースで分割を優先
        last_space = chunk.rfind(" ")
        if last_space > 0:
            split_at = last_space
        else:
            # 句読点・括弧の直後も優先
            for i in range(len(chunk) - 1, max(0, len(chunk) - 5), -1):
                if i < len(rest) and rest[i] in "、。）」":
                    split_at = i + 1
                    break
            else:
                split_at = max_chars
        line = rest[:split_at].strip()
        rest = rest[split_at:].strip()
        if line:
            lines.append(line)
    # どの行も max_chars を超えないように再分割（幅はみ出し防止）
    out = []
    for line in lines:
        while len(line) > max_chars:
            # 最後のスペースで分割を優先
            chunk = line[: max_chars + 1]
            last_space = chunk.rfind(" ")
            split_at = last_space if last_space > 0 else max_chars
            out.append(line[:split_at].strip())
            line = line[split_at:].strip()
        if line:
            out.append(line)
    return out


def _wrap_svg_long_text(svg_content, max_chars=None):
    """SVG内の<text>を図形幅内に収め、括弧前後にスペースを入れ、複数行は縦横中央に。"""
    max_chars = max_chars or _SVG_LABEL_MAX_CHARS_PER_LINE
    if not svg_content or "<svg" not in svg_content or "<text" not in svg_content:
        return svg_content
    pattern = re.compile(r"(<text\s+[^>]*?>)([^<]*?)(</text>)")

    def repl(m):
        pre, content = m.group(1), m.group(2)
        content = content.strip().replace("\n", "").replace("\r", "")
        if not content:
            return m.group(0)
        # 図下キャプション（T番号など）は折り返さない
        if re.search(r"\(T\d{2}\)|レイヤー", content):
            return m.group(0)
        content = _add_space_around_parens(content)
        # 幅はみ出し防止: 必ず max_chars ごとに分割（スペース優先は _split_label_to_lines で）
        lines = _split_label_to_lines(content, max_chars)
        final = []
        for line in lines:
            while len(line) > max_chars:
                chunk = line[: max_chars + 1]
                last_space = chunk.rfind(" ")
                split_at = last_space if last_space > 0 else max_chars
                final.append(line[:split_at].strip())
                line = line[split_at:].lstrip()
            if line:
                final.append(line)
        lines = final
        if len(lines) <= 1:
            # 1行でも括弧部分は1pt小さくする
            return pre + _svg_wrap_parens_small(content) + m.group(3)
        x_m = re.search(r'x=["\'](\d+)["\']', pre)
        y_m = re.search(r'y=["\'](\d+)["\']', pre)
        x_val = x_m.group(1) if x_m else "50"
        # 複数行全体を縦中央に（1行目ベースライン = 中央 - (行数*dy)/2 + 約6）
        n = len(lines)
        block_h = (n - 1) * _SVG_LINE_DY + 11
        new_y = _SVG_BOX_CENTER_Y - block_h // 2 + 6
        pre_new = re.sub(r'y=["\']\d+["\']', f'y="{new_y}"', pre)
        parts = []
        for i, line in enumerate(lines):
            inner = _svg_wrap_parens_small(line)
            if i == 0:
                parts.append(f'<tspan x="{x_val}" dy="0">{inner}</tspan>')
            else:
                parts.append(f'<tspan x="{x_val}" dy="{_SVG_LINE_DY}">{inner}</tspan>')
        inner = "".join(parts)
        return pre_new + inner + m.group(3)

    out = pattern.sub(repl, svg_content)
    # 複数行がはみ出さないよう rect 高さを 44 → 70 に統一
    if "height=" in out and ("44" in out or "56" in out or "60" in out):
        for h in ("44", "56", "60"):
            out = out.replace(f'height="{h}"', f'height="{_SVG_BOX_HEIGHT}"')
    # 矢印をボックス縦中央（y=55）に揃える
    if f'height="{_SVG_BOX_HEIGHT}"' in out and " 42" in out:
        out = out.replace(" 42 ", " 55 ").replace(' 42"', ' 55"')
    if f'height="{_SVG_BOX_HEIGHT}"' in out and " 50" in out:
        out = out.replace(" 50 ", " 55 ").replace(' 50"', ' 55"')
    # 1行ラベルも縦中央に（複数行は上で new_y を設定済みなので、48/50 は1行のみ）
    if f'height="{_SVG_BOX_HEIGHT}"' in out:
        out = out.replace('y="48"', f'y="{_SVG_BOX_CENTER_Y}"').replace('y="50"', f'y="{_SVG_BOX_CENTER_Y}"')
    # 図下キャプション（レイヤー等）の上にスペースを入れて視認性を確保
    if "レイヤー" in out and 'y="100"' in out:
        out = out.replace('y="100"', 'y="118"', 1)
    return out


def _figure_fragment(idx, fmt, content, content_esc):
    """図1つ分のJSX文字列を返す。Mermaid なら MermaidDiagram、それ以外は dangerouslySetInnerHTML。"""
    fmt_lower = (fmt or "").strip().lower()
    if fmt_lower == "mermaid":
        # 図の横幅は記事幅の90%まで許容（他形式と同様）
        return f'<div className="not-prose my-8 w-full max-w-[90%] mx-auto"><MermaidDiagram chart={{`{content_esc}`}} /></div>'
    # SVG / HTML / Table 等は生HTMLとして埋め込む
    escaped = esc_html_attr(content)
    # 図の横幅は記事幅の90%まで許容（おかしな改行を防ぐため。左右に余裕がある場合は広く表示）
    return f'<div className="not-prose my-8 overflow-x-auto w-full max-w-[90%] mx-auto" dangerouslySetInnerHTML={{{{ __html: `{escaped}` }}}} />'


def build_html_from_parsed(no, slug, title_ja, parsed):
    """パース結果と no/slug/title から記事HTMLを組み立てる。図は Mermaid / SVG / HTML に対応。記事下に前後ナビ・カテゴリに戻る・関連記事3件を追加。"""
    article_nav_js, nav_related_jsx = build_article_nav_js_and_jsx(no)
    lead = parsed["lead"] or "本稿の焦点は運用・証跡・監査可能性に落とすための要件を整理する。"
    body_parts = parsed.get("body_parts") or []
    # 各図の形式と内容
    fig_fmt = [parsed.get("fig1_fmt") or "Mermaid", parsed.get("fig2_fmt") or "Mermaid", parsed.get("fig3_fmt") or "Mermaid"]
    fig_content = [parsed.get("fig1_content") or "", parsed.get("fig2_content") or "", parsed.get("fig3_content") or ""]
    m1, m2, m3 = parsed.get("mermaid1", ""), parsed.get("mermaid2", ""), parsed.get("mermaid3", "")
    if not fig_content[0] and m1:
        fig_content[0] = m1
    if not fig_content[1] and m2:
        fig_content[1] = m2
    if not fig_content[2] and m3:
        fig_content[2] = m3
    if not fig_content[0]:
        fig_content[0] = "graph LR\n  A --> B\n  B --> C"
        fig_fmt[0] = "Mermaid"
    if not fig_content[1]:
        fig_content[1] = "graph TD\n  X --> Y\n  Y --> Z"
        fig_fmt[1] = "Mermaid"
    if not fig_content[2]:
        fig_content[2] = "graph TD\n  T1[差し戻し1]\n  T2[差し戻し2]"
        fig_fmt[2] = "Mermaid"
    # 読者不要な内部コード（T08 等）を図から除去
    for i in range(3):
        fig_content[i] = _strip_internal_fig_codes(fig_content[i])
    # SVG図は長いラベルを2行に折り返してはみ出し防止
    for i in range(3):
        if (fig_fmt[i] or "").strip().lower() == "svg" and fig_content[i].strip().startswith("<"):
            fig_content[i] = _wrap_svg_long_text(fig_content[i])
    m1_esc, m2_esc, m3_esc = esc(fig_content[0]), esc(fig_content[1]), esc(fig_content[2])
    # body_parts を HTML と図の挿入に展開（形式に応じて Mermaid または dangerouslySetInnerHTML）
    body_fragments = []
    for i, part in enumerate(body_parts):
        if part == "{{MERMAID1}}":
            body_fragments.append(_figure_fragment(0, fig_fmt[0], fig_content[0], m1_esc))
        elif part == "{{MERMAID2}}":
            body_fragments.append(_figure_fragment(1, fig_fmt[1], fig_content[1], m2_esc))
        elif part == "{{MERMAID3}}":
            body_fragments.append(_figure_fragment(2, fig_fmt[2], fig_content[2], m3_esc))
        else:
            body_fragments.append(part)
    body_html = "\n                                ".join(body_fragments) if body_fragments else ""
    key_sentence = parsed["key_sentence"] or "運用・証跡・監査可能性を具体化するため、明日からRACIの確認と申請フローの文書化のいずれかに着手できる。"
    checklist = parsed["checklist"] or ["RACIを決めているか", "申請フローを文書化しているか", "証跡を保全しているか"]
    checklist_html = "\n".join(f"<li>{c}</li>" for c in checklist[:10])
    refs = parsed["references"]
    if not refs.strip():
        refs = """
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001（AIMS）](https://www.iso.org/standard/42001)
- [AI事業者ガイドライン（経済産業省）](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf)"""
    next_steps = parsed["next_steps"] or "明日から：自部門のAI利用承認者を確認する。証跡の保管場所を一覧化する。"
    # **...** → 太字＋下線のHTMLに変換（アスタリスクは表示しない）
    lead_html = markdown_strong_to_bold_underline(lead)
    # リードは長いと読みにくいので「。」の直後に改行を入れる
    lead_html = lead_html.replace("。", "。<br />")
    key_sentence_html = markdown_strong_to_bold_underline(key_sentence)
    next_steps_html = markdown_strong_to_bold_underline(next_steps)
    lead_escaped = esc_html_attr(lead_html)
    key_sentence_escaped = esc_html_attr(key_sentence_html)
    next_steps_escaped = esc_html_attr(next_steps_html)
    # 参考文献をHTMLリストに（「Label. URL」または「[Label](URL)」形式を <a> に変換）
    ref_lines = []
    _ref_class = "text-brand-blue hover:underline"
    _ref_attr = "target=\"_blank\" rel=\"noopener noreferrer\""
    for line in refs.strip().split("\n"):
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            inner = line[2:].strip()
            # [Label](URL) 形式
            m = re.match(r"\[([^\]]+)\]\((https?://[^)]+)\)", inner)
            if m:
                ref_lines.append(f"<a href=\"{m.group(2)}\" {_ref_attr} class=\"{_ref_class}\">{html_module.escape(m.group(1))}</a>")
                continue
            # Label. https://... 形式（最後の . の後が URL）
            if ". https://" in inner or ". http://" in inner:
                idx = inner.find(". https://") if ". https://" in inner else inner.find(". http://")
                label = inner[:idx].strip()
                url = inner[idx + 2:].strip()  # ". " の直後から
                ref_lines.append(f"<a href=\"{url}\" {_ref_attr} class=\"{_ref_class}\">{html_module.escape(label)}</a>")
                continue
            ref_lines.append(f"<a href=\"#\" class=\"{_ref_class}\">{html_module.escape(inner)}</a>")
    refs_html = "\n".join(f"<li>{r}</li>" for r in ref_lines) if ref_lines else f"<li><a href=\"https://www.nist.gov/itl/ai-risk-management-framework\" {_ref_attr} class=\"{_ref_class}\">NIST AI RMF</a></li>\n<li><a href=\"https://www.iso.org/standard/42001\" {_ref_attr} class=\"{_ref_class}\">ISO/IEC 42001</a></li>"

    # 既存のSHARED_HEAD/TAILと同様のHTML
    # meta description: AIカテゴリ同様にリード（1段落）を要約として使用（SEO・カード表示用）。最大155文字。
    lead_raw = (parsed.get("lead") or "").strip()
    if lead_raw:
        description = lead_raw[:155] + ("…" if len(lead_raw) > 155 else "")
    else:
        description = title_ja + "。運用に落とすための要件・証跡・チェックリストを整理する。"
    description_attr = description.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    title_attr = title_ja.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    title_ja_json = esc_json(title_ja)
    description_json = esc_json(description)
    canonical_url = f"https://riseby.net/blog/ai-governance/{slug}.html"
    # Schema.org BlogPosting 強化（publisher, image, description, dateModified, mainEntityOfPage, articleSection）
    blog_posting_ld = (
        '{{"@context":"https://schema.org","@type":"BlogPosting",'
        '"headline":"{headline}","description":"{desc}",'
        '"datePublished":"2026-02-09","dateModified":"2026-02-09",'
        '"author":{{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net"}},'
        '"publisher":{{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net","logo":{{"@type":"ImageObject","url":"https://riseby.net/assets/images/logo.svg"}}}},'
        '"image":"https://riseby.net/assets/images/og-image.jpg",'
        '"mainEntityOfPage":{{"@type":"WebPage","@id":"{url}"}},'
        '"articleSection":"AIガバナンス","url":"{url}"}}'
    ).format(headline=title_ja_json, desc=description_json, url=canonical_url)
    # BreadcrumbList（SERP用パンくず）
    breadcrumb_ld = (
        '{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{{"@type":"ListItem","position":1,"name":"ホーム","item":"https://riseby.net/"}},'
        '{{"@type":"ListItem","position":2,"name":"ブログ","item":"https://riseby.net/blog/"}},'
        '{{"@type":"ListItem","position":3,"name":"AIガバナンス","item":"https://riseby.net/blog/ai-governance/index.html"}},'
        '{{"@type":"ListItem","position":4,"name":"{name}","item":"{url}"}}]}}'
    ).format(name=title_ja_json, url=canonical_url)
    head = f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <title>{title_attr} | RISEby Blog</title>
    <meta name="description" content="{description_attr}">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="RISEby inc.">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{title_attr} | RISEby Blog">
    <meta property="og:description" content="{description_attr}">
    <meta property="og:image" content="https://riseby.net/assets/images/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_attr} | RISEby Blog">
    <meta name="twitter:description" content="{description_attr}">
    <meta name="twitter:image" content="https://riseby.net/assets/images/og-image.jpg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>tailwind.config = {{ theme: {{ extend: {{ colors: {{ brand: {{ blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' }} }}, fontFamily: {{ sans: ['"Noto Sans JP"', 'sans-serif'], display: ['"Montserrat"', 'sans-serif'] }} }} }} }}</script>
    <style>body {{ font-family: "Noto Sans JP", sans-serif; }}
    .mermaid {{ display: flex; justify-content: center; margin: 2rem 0; background: #f8fafc; padding: 1rem; border-radius: 0.5rem; }}
    .mermaid svg {{ max-width: 100%; }}
    .mermaid .nodeLabel, .mermaid .edgeLabel {{ font-size: 1.125rem !important; }}</style>
    <script type="application/ld+json">{blog_posting_ld}</script>
    <script type="application/ld+json">{breadcrumb_ld}</script>
</head>
<body class="bg-slate-50 text-slate-800">
    <div id="root"></div>
    <script type="text/babel">
        {article_nav_js}
        const {{ useState, useEffect }} = React;
        const Icon = ({{ name, size = 24, className = "" }}) => {{
            const s = size;
            const svg = (children) => React.createElement('svg', {{ xmlns: "http://www.w3.org/2000/svg", width: s, height: s, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 2, strokeLinecap: "round", strokeLinejoin: "round", className }}, children);
            if (name === 'Menu') return svg([React.createElement('line', {{ key: '1', x1: 3, y1: 6, x2: 21, y2: 6 }}), React.createElement('line', {{ key: '2', x1: 3, y1: 12, x2: 21, y2: 12 }}), React.createElement('line', {{ key: '3', x1: 3, y1: 18, x2: 21, y2: 18 }})]);
            if (name === 'X') return svg([React.createElement('line', {{ key: '1', x1: 18, y1: 6, x2: 6, y2: 18 }}), React.createElement('line', {{ key: '2', x1: 6, y1: 6, x2: 18, y2: 18 }})]);
            if (name === 'Mail') return svg([React.createElement('path', {{ key: '1', d: "M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" }}), React.createElement('polyline', {{ key: '2', points: "22,6 12,13 2,6" }})]);
            if (name === 'User') return svg([React.createElement('path', {{ key: '1', d: "M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" }}), React.createElement('circle', {{ key: '2', cx: 12, cy: 7, r: 4 }})]);
            if (name === 'Lightbulb') return svg([React.createElement('path', {{ key: '1', d: "M9 18h6" }}), React.createElement('path', {{ key: '2', d: "M10 22h4" }}), React.createElement('path', {{ key: '3', d: "M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14" }})]);
            return React.createElement('span', {{ className: "inline-block w-4 h-4 bg-gray-300 rounded-full" }});
        }};
        const Header = () => {{
            const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
            const [scrolled, setScrolled] = useState(false);
            useEffect(() => {{ const h = () => setScrolled(window.scrollY > 20); window.addEventListener('scroll', h); return () => window.removeEventListener('scroll', h); }}, []);
            return (
                <header className={{`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${{scrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-white/80 backdrop-blur-sm py-4 shadow-sm'}}`}}>
                    <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
                        <a href="../../index.html" className="flex items-center gap-3 hover:opacity-80"><img src="../../assets/images/logo.svg" alt="RISEby" className="h-8 md:h-9" /></a>
                        <nav className="hidden md:flex items-center gap-8">
                            <a href="../../index.html#services" className="font-bold tracking-wide hover:opacity-70 text-slate-800">サービス</a>
                            <a href="../index.html" className="font-bold tracking-wide text-slate-800">ブログ</a>
                            <a href="../../about.html" className="font-bold tracking-wide hover:opacity-70 text-slate-800">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white hover:bg-slate-800 px-6 py-2.5 rounded-full font-bold">お問い合わせ</a>
                        </nav>
                        <button onClick={{() => setMobileMenuOpen(!mobileMenuOpen)}} className="md:hidden p-2 text-slate-800"><Icon name={{mobileMenuOpen ? "X" : "Menu"}} size={{24}} /></button>
                    </div>
                    {{mobileMenuOpen && (
                        <div className="md:hidden absolute top-full left-0 right-0 bg-white border-t shadow-xl p-4 flex flex-col gap-4">
                            <a href="../../index.html#services" className="text-slate-800 font-bold py-3 border-b border-slate-50">サービス</a>
                            <a href="../index.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">ブログ</a>
                            <a href="../../about.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white text-center py-3.5 rounded-lg font-bold mt-2">お問い合わせ</a>
                        </div>
                    )}}
                </header>
            );
        }};
        const Footer = () => (
            <footer className="bg-[#0B0F19] text-white pt-24 pb-12 border-t border-slate-800">
                <div className="container mx-auto px-4 max-w-7xl">
                    <div className="flex flex-col lg:flex-row justify-between gap-16 mb-24">
                        <div className="lg:w-1/3">
                            <a href="../../index.html" className="block mb-8"><img src="../../assets/images/logo.svg" alt="RISEby" className="h-9 brightness-0 invert opacity-90" /></a>
                            <p className="text-slate-400 text-sm mb-8">複合的な経営課題を、AI・戦略・テクノロジー・人の観点から整理し、実行に落とすコンサルティングファーム。</p>
                            <div className="mb-10 text-sm text-slate-400 space-y-3">
                                <p>〒150-6115 東京都渋谷区渋谷2-24-12</p>
                                <p>渋谷スクランブルスクエア 15階</p>
                                <a href="mailto:contact@riseby.net" className="hover:text-white flex items-center gap-2 mt-6 group"><span className="bg-slate-800 p-2 rounded-full group-hover:bg-slate-700"><Icon name="Mail" size={{16}} /></span>contact@riseby.net</a>
                            </div>
                            <p className="text-slate-600 text-xs">&copy; {{new Date().getFullYear()}} RISEby Inc.</p>
                        </div>
                        <div className="lg:w-2/3 grid grid-cols-2 md:grid-cols-3 gap-8">
                            <div><h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">サービス</h3>
                                <ul className="space-y-3"><li><a href="../../index.html#services" className="text-slate-400 hover:text-white text-xs">サービス一覧</a></li></ul></div>
                            <div><h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">会社</h3>
                                <ul className="space-y-3"><li><a href="../../about.html" className="text-slate-400 hover:text-white text-xs">会社概要</a></li><li><a href="../index.html" className="text-slate-400 hover:text-white text-xs">ブログ</a></li></ul></div>
                        </div>
                    </div>
                    <div className="border-t border-slate-800 pt-10 flex flex-wrap gap-8 justify-center text-xs text-slate-500">
                        <a href="../../about.html" className="hover:text-white">会社概要</a><a href="../../privacy.html" className="hover:text-white">プライバシーポリシー</a>
                    </div>
                </div>
            </footer>
        );
        const MermaidDiagram = ({{ chart }}) => {{
            useEffect(() => {{ if (typeof mermaid !== 'undefined') {{ mermaid.initialize({{ theme: 'base', themeVariables: {{ fontSize: '18px', primaryTextColor: '#334155' }} }}); mermaid.init(); }} }}, []);
            return <div className="mermaid overflow-x-auto max-w-4xl mx-auto text-lg">{{chart}}</div>;
        }};
        const BlogArticle = () => (
            <main className="pt-24 pb-16">
                <article className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-100">
                        <header className="text-center mb-12 border-b border-slate-100 pb-10">
                            <div className="flex justify-center flex-wrap gap-2 mb-4">
                                <span className="bg-red-100 text-red-800 text-xs px-3 py-1 rounded-full font-bold tracking-wide uppercase font-display">AIガバナンス</span>
                                <span className="bg-slate-100 text-slate-600 text-xs px-3 py-1 rounded-full font-bold tracking-wide">実装・証跡</span>
                            </div>
                            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-6 leading-tight">{title_ja}</h1>
                            <div className="flex items-center justify-center space-x-4 text-sm text-slate-500">
                                <time dateTime="2026-02-09">2026.02.09</time><span>&middot;</span>
                                <span className="flex items-center gap-1"><Icon name="User" size={{14}} /> RISEby Editorial Team</span>
                            </div>
                        </header>
                        <div className="prose prose-lg prose-slate prose-headings:font-bold prose-a:text-brand-blue hover:prose-a:text-blue-500 mx-auto">
                                <p className="lead text-xl text-slate-600 mb-4 leading-relaxed font-medium" dangerouslySetInnerHTML={{{{ __html: `{lead_escaped}` }}}} />
                                <p className="not-prose text-sm text-slate-500 mb-10"><a href="#article-nav" className="text-brand-blue hover:underline">← 前後の記事・関連記事・カテゴリに戻るはページ末尾へ</a></p>
                                {body_html}
                                <div className="my-8 bg-blue-50 border-l-4 border-brand-blue p-6 rounded-r-lg not-prose">
                                    <h5 className="font-bold text-brand-blue mb-2 flex items-center gap-2"><Icon name="Lightbulb" size={{20}} />要点</h5>
                                    <div className="text-slate-700 text-base leading-relaxed" dangerouslySetInnerHTML={{{{ __html: `{key_sentence_escaped}` }}}} />
                                </div>
                                <h2>すぐ使えるチェックリスト</h2>
                                <ul className="list-disc pl-6 space-y-2">
                                {checklist_html}
                                </ul>
                                <h2>参考・参照</h2>
                                <ul className="list-disc pl-6 space-y-2 text-slate-700">
                                    {refs_html}
                                </ul>
                                <h2>次の一歩</h2>
                                <p dangerouslySetInnerHTML={{{{ __html: `{next_steps_escaped}` }}}} />
{nav_related_jsx}
                        </div>
                        <div className="not-prose mt-20 p-10 bg-slate-900 rounded-2xl text-center relative overflow-hidden">
                            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-brand-blue to-cyan-500"></div>
                            <h3 className="text-2xl font-bold text-white mb-4">AIガバナンスの設計・実装支援</h3>
                            <p className="text-slate-300 mb-8 max-w-2xl mx-auto text-sm leading-relaxed">利用規程の設計から評価・透明性・監査証跡まで、範囲を決めたうえで支援します。</p>
                            <a href="mailto:contact@riseby.net" className="inline-flex items-center justify-center gap-2 bg-brand-blue text-white px-8 py-3 rounded-full font-bold hover:bg-white hover:text-brand-blue transition-all"><Icon name="Mail" size={{18}} /> お問い合わせ</a>
                        </div>
                    </div>
                </article>
            </main>
        );
        const App = () => <div className="min-h-screen flex flex-col font-sans bg-slate-50 text-slate-800"><Header /><BlogArticle /><Footer /></div>;
        const root = ReactDOM.createRoot(document.getElementById("root"));
        root.render(<App />);
    </script>
</body>
</html>
'''
    return head


def append_figure_usage_history(no, slug, parsed, op):
    """図表使用履歴を更新する（既存の no は上書き、なければ追記）。形式（fmt）も記録。"""
    f1 = (parsed.get("fig1_type") or "").strip()
    f2 = (parsed.get("fig2_type") or "").strip()
    f3 = (parsed.get("fig3_type") or "").strip()
    f1_fmt = (parsed.get("fig1_fmt") or parsed.get("fig1_fmt_record") or "Mermaid").strip()
    f2_fmt = (parsed.get("fig2_fmt") or parsed.get("fig2_fmt_record") or "Mermaid").strip()
    f3_fmt = (parsed.get("fig3_fmt") or parsed.get("fig3_fmt_record") or "Mermaid").strip()
    if not (f1 and f2 and f3):
        return
    FIGURE_HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    base_fieldnames = ["no", "slug", "fig1", "fig2", "fig3", "fig1_fmt", "fig2_fmt", "fig3_fmt", "op"]
    rows = []
    if FIGURE_HISTORY_PATH.exists():
        with open(FIGURE_HISTORY_PATH, encoding="utf-8", newline="") as f:
            r = csv.DictReader(f)
            fieldnames = list(r.fieldnames) if r.fieldnames else base_fieldnames
            for fn in base_fieldnames:
                if fn not in fieldnames:
                    fieldnames.append(fn)
            for row in r:
                if row.get("no") == str(no):
                    continue
                for k in base_fieldnames:
                    if k not in row:
                        row[k] = ""
                rows.append(row)
    else:
        fieldnames = base_fieldnames
    rows.append({
        "no": no, "slug": slug,
        "fig1": f1, "fig2": f2, "fig3": f3,
        "fig1_fmt": f1_fmt, "fig2_fmt": f2_fmt, "fig3_fmt": f3_fmt,
        "op": op,
    })
    rows.sort(key=lambda r: int(r.get("no", 0)))
    with open(FIGURE_HISTORY_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print("Updated", FIGURE_HISTORY_PATH)


def main():
    if len(sys.argv) < 2:
        print("Usage: python apply_llm_article.py <article_no> [path_to_llm_output.md]", file=sys.stderr)
        sys.exit(1)
    no = int(sys.argv[1])
    meta = parse_design_for_article(no)
    if not meta:
        print(f"Article {no} not found in design.", file=sys.stderr)
        sys.exit(1)
    slug = meta["slug"]
    title_ja = meta["title_ja"]
    op = meta.get("op", "")
    if len(sys.argv) >= 3:
        md_path = Path(sys.argv[2])
        md_text = md_path.read_text(encoding="utf-8")
    else:
        md_text = sys.stdin.read()
    parsed = parse_llm_output(md_text)
    html = build_html_from_parsed(no, slug, title_ja, parsed)
    out_path = OUT_DIR / (slug + ".html")
    out_path.write_text(html, encoding="utf-8")
    print("Wrote", out_path)
    append_figure_usage_history(no, slug, parsed, op)


if __name__ == "__main__":
    main()
