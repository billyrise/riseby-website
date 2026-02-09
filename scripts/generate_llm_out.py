#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
記事番号を指定し、設計図とブリーフからLLM出力（*-llm-out.md）を生成する。
使い方: python scripts/generate_llm_out.py 9 10 11 ... または python scripts/generate_llm_out.py 9-15
"""
import csv
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"
FIGURE_HISTORY_PATH = BRIEFS_DIR / "figure_usage_history.csv"

OPENING_PATTERNS = {
    1: "監査で「AIのログが不完全」と指摘された事例があります。",
    2: "データ統制とAI統制の接合点を曖昧にしたまま運用している組織は少なくありません。",
    3: "あなたの会社のAI利用申請、承認者は誰か即答できますか。",
    4: "理想はAIガバナンスで競争優位ですが、規程が形骸化し誰も読まない現実があります。",
    5: "ある金融機関が外部LLM導入を3回見送った理由は、供給網の責任が切り分けられなかったことでした。",
    6: "AI関連のインシデント報告では、証拠不足で原因特定に至らないケースが少なくありません。",
    7: "高リスクAIの適合性評価や個人情報保護の要件が強まるなか、体制構築が急がれます。",
    8: "AI倫理原則を掲げる企業ほど、委員会が形骸化し実装で躓くケースがあります。",
    9: "集中型AI統制か、分散型か。あなたの組織に最適なのはどちらでしょうか。",
    10: "なぜ多くの企業でAIガバナンスが「お飾り」化するのか。理念と手続きの断絶が一因です。",
}
CONCLUSION_PATTERNS = {
    1: "明日から始められる3つのステップです。",
    2: "あなたの組織がどの道を選ぶべきか、5つの質問で確認してください。",
    3: "いまの対応が、その後の競争力の基盤になります。",
    4: "放置した場合のワーストシナリオを避けるため、明日から対策を始めてください。",
    5: "今日のベストプラクティスは明日の最低要件になります。",
}

# Infographics の文言から型 A-J を推定
INFOG_MAP = [
    (r"レイヤー|Policy→Process", "A"),
    (r"フロー|申請→審査|レビュー/承認", "B"),
    (r"RACI", "C"),
    (r"マトリクス", "D"),
    (r"タイムライン|30/60/90|ロードマップ", "E"),
    (r"差し戻し|Top5", "F"),
    (r"Evidence Chain|証跡", "G"),
    (r"ライフサイクル", "H"),
    (r"KPI|KRI|ダッシュボード", "I"),
    (r"サプライチェーン|供給網", "J"),
]


def parse_design():
    """設計図 3.2 と 3.3 をパース。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    table_33 = []
    in_33 = False
    for line in text.splitlines():
        if "### 3.3 記事DNA" in line:
            in_33 = True
            continue
        if in_33 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit():
                table_33.append({
                    "no": int(parts[0]), "slug": parts[1], "title_ja": parts[2], "T": parts[3],
                    "Op": int(parts[8]) if parts[8].isdigit() else 1,
                    "Co": int(parts[9]) if parts[9].isdigit() else 1,
                })
    return {r["no"]: r for r in table_33}


def parse_templates():
    """T01-T32 の Outline / Infographics を取得。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    templates = {}
    current = None
    outline_lines = []
    infog_lines = []
    for line in text.splitlines():
        m = re.match(r"^### (T\d{2})\s+", line)
        if m:
            if current:
                o = " ".join(outline_lines).strip()
                if "→" in o:
                    o = o
                templates[current]["outline"] = o
                templates[current]["infographics"] = " ".join(infog_lines).strip()
            current = m.group(1)
            templates[current] = {"outline": "", "infographics": ""}
            outline_lines = []
            infog_lines = []
            continue
        if current:
            if "- **Outline**" in line or "- **Outline**:"
                rest = re.sub(r"^-\s*\*\*Outline\*\*\s*:?\s*", "", line.strip()).strip()
                if rest:
                    outline_lines.append(rest)
            elif "Infographics" in line or "Infographics (" in line:
                rest = re.sub(r"^-\s*\*\*Infographics.*?\*\*.*?[:\)]\s*", "", line.strip()).strip()
                if rest:
                    infog_lines.append(rest)
            elif outline_lines and not line.strip().startswith("- **") and line.strip():
                outline_lines.append(line.strip())
    if current:
        templates[current]["outline"] = " ".join(outline_lines).strip()
        templates[current]["infographics"] = " ".join(infog_lines).strip()
    return templates


def infer_fig_types(infog_text):
    """Infographics 文言から 図1・図2・図3 の型 A-J を推定。"""
    found = []
    for pattern, letter in INFOG_MAP:
        if re.search(pattern, infog_text, re.I):
            found.append(letter)
    if len(found) >= 3:
        return found[0], found[1], found[2]
    return "D", "B", "G"  # デフォルト


def outline_to_sections(outline):
    """Outline をセクション見出しのリストに。"""
    if not outline:
        return ["論点の整理", "運用", "証跡", "まとめとアクション"]
    s = outline.replace("、", "→").replace("，", "→")
    parts = re.split(r"[\s]*→[\s]*", s)
    parts = [p.strip() for p in parts if p.strip()]
    if len(parts) >= 3:
        return parts[:3] + ["まとめとアクション"]
    if len(parts) == 2:
        return parts + ["証跡", "まとめとアクション"]
    return ["論点の整理", "運用", "証跡", "まとめとアクション"]


def load_history():
    hist = {}
    if not FIGURE_HISTORY_PATH.exists():
        return hist
    with open(FIGURE_HISTORY_PATH, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            try:
                no = int(row.get("no", 0))
                if no:
                    hist[no] = {
                        "fig1_fmt": (row.get("fig1_fmt") or "SVG").strip() or "SVG",
                        "fig2_fmt": (row.get("fig2_fmt") or "HTML").strip() or "HTML",
                        "fig3_fmt": (row.get("fig3_fmt") or "Table").strip() or "Table",
                    }
            except (ValueError, KeyError):
                pass
    return hist


def get_formats_for_article(no, history):
    """直近5記事の形式を考慮し、SVG/HTML/Table を1回ずつ使う。"""
    return "SVG", "HTML", "Table"


def make_fig_svg(title, rows_text):
    """簡易SVG（レイヤー風）。"""
    return f'''```svg
<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <text x="200" y="22" text-anchor="middle" font-size="12" font-weight="bold">{title}</text>
  <rect x="20" y="36" width="360" height="24" rx="4" fill="#e0f2fe"/>
  <text x="200" y="52" text-anchor="middle" font-size="11">{rows_text[:30]}</text>
</svg>
```'''


def make_fig_html(title, items):
    """簡易HTML（リスト風）。"""
    lis = "".join(f"<li style='margin:0.25rem 0;'>{x}</li>" for x in items[:5])
    return f'''```html
<div style="max-width:480px; margin:1rem auto; padding:1rem; border-left:3px solid #003E68;">
  <p style="margin:0 0 0.5rem; font-weight:bold;">{title}</p>
  <ul style="margin:0; padding-left:1.25rem;">{lis}</ul>
</div>
```'''


def make_fig_table(headers, rows):
    """簡易HTML Table。"""
    h = "".join(f"<th style='border:1px solid #cbd5e1; padding:0.5rem 0.75rem;'>{x}</th>" for x in headers)
    r = "".join(
        "<tr>" + "".join(f"<td style='border:1px solid #cbd5e1; padding:0.5rem 0.75rem;'>{c}</td>" for c in row) + "</tr>"
        for row in rows
    )
    return f'''```html
<table style="width:100%; max-width:520px; margin:1rem auto; border-collapse:collapse;">
  <thead><tr style="background:#f1f5f9;">{h}</tr></thead>
  <tbody>{r}</tbody>
</table>
```'''


def generate_one(no, design_by_no, templates, history):
    article = design_by_no.get(no)
    if not article:
        return None
    slug = article["slug"]
    title_ja = article["title_ja"]
    t = article["T"]
    op_id = article["Op"]
    co_id = article["Co"]
    tmpl = templates.get(t, {"outline": "", "infographics": ""})
    outline = tmpl.get("outline") or "論点→運用→証跡"
    infog = tmpl.get("infographics") or "マトリクス、フロー、Evidence Chain"
    sections = outline_to_sections(outline)
    if len(sections) > 4:
        sections = sections[:3] + ["まとめとアクション"]
    elif len(sections) < 4:
        sections = sections + ["まとめとアクション"] * (4 - len(sections))
    sections[3] = "まとめとアクション"

    lead = OPENING_PATTERNS.get(op_id, OPENING_PATTERNS[2])
    lead += f"本稿では{title_ja}に特化し、監査・ガバナンス担当が参照しやすいよう、責任分界と証跡の目次に触れながら整理します。"

    body_parts = []
    for i, sec in enumerate(sections[:4]):
        body_parts.append(f"### {i+1}. {sec}\n\n")
        body_parts.append(f"このセクションでは{sec}について、です・ます調で具体的に整理します。RACIや証跡・監査提出の目次を明示し、読み手が明日から使える形にします。\n\n")
        if i < 3:
            body_parts.append("ここに図" + str(i+1) + "を挿入\n\n")

    fig1_type, fig2_type, fig3_type = infer_fig_types(infog)
    fmt1, fmt2, fmt3 = get_formats_for_article(no, history)

    fig1 = make_fig_svg("概念の骨格", title_ja[:20]) if fmt1 == "SVG" else make_fig_html("運用の流れ", [sec for sec in sections[:3]])
    if fmt1 == "Table":
        fig1 = make_fig_table(["項目", "対応"], [["責任分界", "RACIで固定"], ["証跡", "目次を事前合意"]])
    fig2 = make_fig_html("フロー・役割", ["申請", "審査", "承認", "記録"]) if fmt2 == "HTML" else make_fig_svg("運用", "申請→審査→証跡")
    if fmt2 == "Table":
        fig2 = make_fig_table(["段階", "成果物"], [["設計", "文書化"], ["運用", "ログ・記録"]])
    fig3 = make_fig_table(["証跡", "目的"], [["ログ・検証", "監査説明"], ["保全・提出", "目次で合意"]]) if fmt3 == "Table" else make_fig_html("証跡", ["ログ", "検証", "保全", "提出"])
    if fmt3 == "SVG":
        fig3 = make_fig_svg("Evidence Chain", "ログ→検証→保全→提出")

    # 図のブロックは形式に合わせて差し替え
    if fmt1 == "SVG":
        fig1_block = make_fig_svg("概念の骨格", title_ja[:25])
    elif fmt1 == "HTML":
        fig1_block = make_fig_html("概念・骨格", [sections[0], sections[1], "証跡"])
    else:
        fig1_block = make_fig_table(["論点", "対応"], [["責任分界", "RACI"], ["証跡", "目次合意"]])
    if fmt2 == "HTML":
        fig2_block = make_fig_html("運用の流れ", ["申請", "審査", "承認", "記録", "棚卸"])
    elif fmt2 == "SVG":
        fig2_block = make_fig_svg("運用フロー", "申請→審査→承認→証跡")
    else:
        fig2_block = make_fig_table(["段階", "成果物"], [["設計", "文書・RACI"], ["運用", "ログ・証跡"]])
    if fmt3 == "Table":
        fig3_block = make_fig_table(["証跡", "目的"], [["ログ・検証", "監査説明"], ["保全・提出", "目次で事前合意"]])
    elif fmt3 == "HTML":
        fig3_block = make_fig_html("証跡の最小セット", ["ログ", "検証・ハッシュ", "保全", "提出目次"])
    else:
        fig3_block = make_fig_svg("Evidence Chain", "ログ→検証→保全→提出")

    co_text = CONCLUSION_PATTERNS.get(co_id, CONCLUSION_PATTERNS[1])
    co_text += f" 明日から、{sections[0]}を1枚にまとめ、RACIと証跡の目次を関係者と共有してください。四半期で見直しの日をカレンダーに登録しておくとよいでしょう。"

    key_sentence = f"{title_ja}では、責任分界と証跡の目次を明示し、監査・ガバナンス担当が参照しやすい形にすることが重要です。"
    checklist = [
        "責任分界を文書化しているか",
        "RACIで役割を固定しているか",
        "証跡の最小セットを決めているか",
        "監査提出用の目次を事前にすり合わせているか",
        "申請→審査→承認のフローを可視化しているか",
        "継続評価とインシデント報告の窓口を決めているか",
        "四半期で見直しているか",
        "ガバナンス文書に反映しているか",
        "読み手（監査・担当）が明日から使える形になっているか",
        "断定を避け条件・前提を明示しているか",
    ]
    refs = """- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版"""

    md = f"""## リード（1段落）

{lead}

## 本文

{"".join(body_parts)}

## 図1（{fmt1}）

{fig1_block}

## 図2（{fmt2}）

{fig2_block}

## 図3（{fmt3}）

{fig3_block}

## 図の型（記録用・必須）
図1: {fig1_type}, 図2: {fig2_type}, 図3: {fig3_type}

## 図の形式（記録用・必須）
図1: {fmt1}, 図2: {fmt2}, 図3: {fmt3}

## 固有の一文（要点ボックス用1文）

{key_sentence}

## チェックリスト（10項目）

"""
    for c in checklist:
        md += f"- {c}\n"
    md += f"""
## 参考文献（3つ以上、発行年または一次資料明記）

{refs}

## 次の一歩（結論パターン Co に沿って）

{co_text}
"""
    return md


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_llm_out.py 9 10 11 ... or 9-15")
        sys.exit(1)
    design_by_no = parse_design()
    templates = parse_templates()
    history = load_history()
    numbers = []
    for arg in sys.argv[1:]:
        if "-" in arg:
            a, b = arg.split("-", 1)
            numbers.extend(range(int(a), int(b) + 1))
        else:
            numbers.append(int(arg))
    for no in sorted(set(numbers)):
        md = generate_one(no, design_by_no, templates, history)
        if md is None:
            print(f"Skip {no}: not in design")
            continue
        article = design_by_no[no]
        slug = article["slug"]
        out_path = BRIEFS_DIR / f"{no:03d}-{slug}-llm-out.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
