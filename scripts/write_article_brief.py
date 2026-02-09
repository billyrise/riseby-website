#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
記事1本ごとに、LLMへ渡す「十分な情報を全て含んだ」執筆ブリーフを生成する。
出力: docs/ai-governance-briefs/NN-slug.md
LLMはこのブリーフのみを読んで、本文＋インフォグラフィック3種（Mermaid）を生成する。
"""
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"
FIGURE_HISTORY_PATH = BRIEFS_DIR / "figure_usage_history.csv"

# 冒頭パターン（Op 1-10）— cursor prompt 3.1 より
OPENING_PATTERNS = {
    1: ("現場の声", "「監査で『AIのログが不完全』と指摘され、3ヶ月の是正対応を余儀なくされた」"),
    2: ("意外な事実", "「EU AI Actの透明性義務、実は日本企業の8割が対象になる可能性」"),
    3: ("問いかけ", "「あなたの会社のAI利用申請、承認者は誰か即答できますか？」"),
    4: ("対比", "「理想：AIガバナンスで競争優位。現実：規程が形骸化し誰も読まない」"),
    5: ("ストーリー", "「ある金融機関がAI導入を3回見送った理由—証跡設計の不備」"),
    6: ("統計インパクト", "「AIインシデント報告、73%が『証拠不足で原因特定不能』」※数値は出典付きのみ可"),
    7: ("タイムリミット", "「高リスクAIの適合性評価、2026年8月までに体制構築が必須」"),
    8: ("逆説", "「AI倫理原則を掲げる企業ほど、実装で躓く—理念と手続きの断絶」"),
    9: ("選択肢提示", "「集中型AI統制か、分散型か—あなたの組織に最適なのは？」"),
    10: ("失敗から学ぶ", "「なぜ多くの企業でAIガバナンスが『お飾り』化するのか」"),
}

# 結論パターン（Co 1-5）
CONCLUSION_PATTERNS = {
    1: ("行動への橋渡し", "「明日から始められる3つのステップ」"),
    2: ("判断軸の提供", "「あなたの組織がどの道を選ぶべきか、5つの質問」"),
    3: ("長期視点", "「いまの対応が、その後の競争力の基盤を決める」"),
    4: ("リスク喚起", "「放置した場合のワーストシナリオと、回避策」"),
    5: ("進化の視点", "「今日の『ベストプラクティス』は明日の『最低要件』になる」"),
}

# 図の型ライブラリ（A-J）— cursor prompt 4 より
FIGURE_TYPES = """
| 記号 | 型 |
|------|-----|
| A | レイヤー図（Policy→Process→Evidence→Continuous Monitoring） |
| B | フロー図（申請→審査→例外→更新→棚卸） |
| C | RACIチャート（Board/Legal/CISO/Audit/IT/Business） |
| D | マトリクス（Risk Domain × Control Type 等） |
| E | タイムライン（30/60/90日ロードマップ） |
| F | "監査で差し戻されるポイントTop5"（ランキング＋対策） |
| G | Evidence Chain（ログ→検証→ハッシュ→保全→提出） |
| H | ライフサイクル輪（Plan/Build/Deploy/Operate/Retire） |
| I | KPI/KRIダッシュボード（最小セット＋閾値） |
| J | サプライチェーン図（提供者/委託先/データ境界/責任） |
"""


def parse_design_tables():
    """設計図 3.2 と 3.3 をパース。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    table_32, table_33 = [], []
    in_32, in_33 = False, False
    for line in text.splitlines():
        if "### 3.2 163記事" in line:
            in_32, in_33 = True, False
            continue
        if "### 3.3 記事DNA" in line:
            in_32, in_33 = False, True
            continue
        if in_32 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 4 and parts[0].isdigit():
                table_32.append({"no": int(parts[0]), "slug": parts[1], "template_id": parts[2], "unique_focus": parts[3]})
        if in_33 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit():
                table_33.append({
                    "no": int(parts[0]), "slug": parts[1], "title_ja": parts[2], "T": parts[3],
                    "reader": parts[4], "purpose": parts[5], "depth": parts[6], "style": parts[7],
                    "Op": int(parts[8]), "Co": int(parts[9]),
                })
    by_slug_32 = {r["slug"]: r for r in table_32}
    by_slug_33 = {r["slug"]: r for r in table_33}
    merged = []
    for no in range(1, 164):
        r33 = next((r for r in table_33 if r["no"] == no), None)
        if not r33:
            continue
        r32 = by_slug_32.get(r33["slug"], {})
        merged.append({
            "no": no, "slug": r33["slug"], "title_ja": r33["title_ja"],
            "template_id": r32.get("template_id") or r33["T"],
            "unique_focus": r32.get("unique_focus", ""),
            "reader": r33["reader"], "purpose": r33["purpose"], "depth": r33["depth"], "style": r33["style"],
            "Op": r33["Op"], "Co": r33["Co"],
        })
    return merged


def _flush(templates, current, current_key, current_lines):
    if not current or not current_key:
        return
    if current_key == "Points":
        templates[current]["points"] = "\n".join(current_lines).strip()
    elif current_key == "Infographics":
        templates[current]["infographics"] = "\n".join(current_lines).strip()
    elif current_key == "Outline":
        templates[current]["outline"] = "\n".join(current_lines).strip()


def parse_templates_from_design():
    """設計図セクション2から T01〜T32 の Points / Infographics / Outline を抽出。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    templates = {}
    current = None
    current_key = None
    current_lines = []
    for line in text.splitlines():
        m = re.match(r"^### (T\d{2})\s+(.+)$", line)
        if m:
            _flush(templates, current, current_key, current_lines)
            current = m.group(1)
            templates[current] = {"points": "", "infographics": "", "outline": ""}
            current_key = None
            current_lines = []
            continue
        if line.strip().startswith("- **Points**"):
            _flush(templates, current, current_key, current_lines)
            current_key = "Points"
            # 同一行に内容がある場合（- **Points**: 〜）
            rest = re.sub(r"^-\s*\*\*Points\*\*\s*:?\s*", "", line.strip(), flags=re.I).strip()
            current_lines = [rest] if rest else []
            continue
        if line.strip().startswith("- **Infographics**"):
            _flush(templates, current, current_key, current_lines)
            current_key = "Infographics"
            rest = re.sub(r"^-\s*\*\*Infographics\*\*\s*\(?\d*\)?\s*:?\s*", "", line.strip(), flags=re.I).strip()
            current_lines = [rest] if rest else []
            continue
        if line.strip().startswith("- **Outline**"):
            _flush(templates, current, current_key, current_lines)
            current_key = "Outline"
            rest = re.sub(r"^-\s*\*\*Outline\*\*\s*:?\s*", "", line.strip(), flags=re.I).strip()
            current_lines = [rest] if rest else []
            continue
        if current and current_key and (line.strip() or current_lines) and not line.strip().startswith("###"):
            current_lines.append(line)
    _flush(templates, current, current_key, current_lines)
    return templates


def load_figure_usage_history():
    """figure_usage_history.csv を読み、no → {fig1, fig2, fig3, fig1_fmt, fig2_fmt, fig3_fmt, op} の辞書を返す。"""
    hist = {}
    if not FIGURE_HISTORY_PATH.exists():
        return hist
    import csv
    with open(FIGURE_HISTORY_PATH, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                no = int(row.get("no", 0))
                if no:
                    hist[no] = {
                        "fig1": (row.get("fig1") or "").strip(),
                        "fig2": (row.get("fig2") or "").strip(),
                        "fig3": (row.get("fig3") or "").strip(),
                        "fig1_fmt": (row.get("fig1_fmt") or "").strip() or "Mermaid",
                        "fig2_fmt": (row.get("fig2_fmt") or "").strip() or "Mermaid",
                        "fig3_fmt": (row.get("fig3_fmt") or "").strip() or "Mermaid",
                        "op": (row.get("op") or "").strip(),
                    }
            except (ValueError, KeyError):
                continue
    return hist


def get_last_5_formats(articles, index, history):
    """直近5記事で使用された図の形式のリスト（各図ごと）。例: ['Mermaid','Mermaid','SVG','HTML','Mermaid',...]"""
    start = max(0, index - 5)
    slice_list = articles[start:index]
    out = []
    for a in slice_list:
        h = history.get(a["no"], {})
        for key in ("fig1_fmt", "fig2_fmt", "fig3_fmt"):
            fmt = (h.get(key) or "Mermaid").strip()
            if fmt:
                out.append(fmt)
    return out


def get_last_10_figure_usage(articles, index, history):
    """直前10記事の図表使用履歴（型＋形式）。history は load_figure_usage_history() の戻り値。"""
    start = max(0, index - 10)
    slice_list = articles[start:index]
    rows = []
    for a in slice_list:
        h = history.get(a["no"], {})
        f1 = h.get("fig1") or "(未記録)"
        f2 = h.get("fig2") or "(未記録)"
        f3 = h.get("fig3") or "(未記録)"
        f1_fmt = h.get("fig1_fmt") or ""
        f2_fmt = h.get("fig2_fmt") or ""
        f3_fmt = h.get("fig3_fmt") or ""
        rows.append(f"| {a['no']} | {a['slug']} | {f1}({f1_fmt}) | {f2}({f2_fmt}) | {f3}({f3_fmt}) |")
    if not rows:
        return "（この記事が先頭のため直前10件なし。テンプレの推奨3種から選ぶこと。）"
    return "\n".join(rows)


def build_brief(article, templates, articles, article_index, history):
    """1記事分の完全ブリーフ（Markdown）を組み立てる。history は load_figure_usage_history() の戻り値。"""
    t = article["template_id"]
    tmpl = templates.get(t, {"points": "", "infographics": "", "outline": ""})
    op_id = article["Op"]
    co_id = article["Co"]
    op_name, op_example = OPENING_PATTERNS.get(op_id, ("", ""))
    co_name, co_example = CONCLUSION_PATTERNS.get(co_id, ("", ""))
    last10 = get_last_10_figure_usage(articles, article_index, history)
    last5_formats_list = get_last_5_formats(articles, article_index, history)
    last5_formats = ", ".join(last5_formats_list) if last5_formats_list else "（なし）"

    return f"""# 記事執筆ブリーフ（全情報）

## CRITICAL：この記事の固定値（設計図3.3の該当行）

- **No.**: {article['no']} / 163
- **slug**: {article['slug']}
- **title_ja**: {article['title_ja']}
- **template_id**: {t}
- **unique_focus**: {article['unique_focus']}
- **対象読者**: {article['reader']}（Exec=経営層 / Pract=実務 / Audit=監査 / Legal=法務・コンプラ / Multi=複数）
- **目的**: {article['purpose']}（Decide=意思決定 / Impl=実装 / Understand=理解 / Audit=監査対応 / Navigate=方向探索）
- **深さ**: {article['depth']}（Overview=1,500–2,000語 / Deep=2,500–3,500語 / Quick=800–1,200語）
- **スタイル**: {article['style']}（Narrative=物語調 / Analytical=分析調 / Prescriptive=処方箋調 / Comparative=比較調）
- **冒頭パターン（Op）**: {op_id} — {op_name}
  - 例: {op_example}
- **結論パターン（Co）**: {co_id} — {co_name}
  - 例: {co_example}

---

## テンプレ（設計図セクション2）— 必須セクション・書くべきポイント

### Points（書くべきポイント）
{tmpl['points'] or '（未取得）'}

### Infographics（使うべきインフォグラフィック3種の「型」）
{tmpl['infographics'] or '（未取得）'}
上記をこの記事の図1・図2・図3の**推奨型**とする。直前3記事と重複しなければ推奨を優先すること。

### Outline（必須セクション見出し。順序・厚さは記事DNAに応じて調整可）
{tmpl['outline'] or '（未取得）'}

---

## 直前10記事の図表使用履歴（参照必須）

| No. | slug | 図1 | 図2 | 図3 |
|-----|------|-----|-----|-----|
{last10}

## 直前5記事で使用された形式（各形式1回までしか使えない）

直近5記事の図で使われた形式: **{last5_formats}**  
→ この記事では、上記の各形式を**最大1回まで**しか使ってよい。それ以外の形式を必ず含めること。

**RULE**: 多様なインフォグラフィックを必ず使用すること。**Mermaidは禁止**。図は **指定フォーマット**（SVG / HTML / HTML Table / Canvas / Vega-Lite / Plotly / DOT / PlantUML 等）で出力すること。詳細は **docs/ai-governance-blog-infographic-formats.md** を参照。図の型（A–J）は上記履歴と3図セットの役割に従って選ぶこと。

---

## 3図セットの役割（必ず守ること）

| 図 | 役割 | 選ぶ型の例 |
|----|------|------------|
| **図1** | 概念の骨格 | レイヤー図（A）／マトリクス（D） |
| **図2** | 運用の流れ | フロー図（B）／タイムライン（E） |
| **図3** | 監査・証跡 | Evidence Chain（G）／差し戻しTop5（F）／KPI（I） |

同じ図の型を3記事連続で使わないこと。直前10件の履歴を参照して選ぶこと。

---

## 図の型ライブラリ（A–J）

{FIGURE_TYPES}

- 上記「3図セットの役割」に従い、図1・図2・図3で役割分担を守ること。
- 1図＝1メッセージ。ラベルは「名詞句＋動詞1つ」まで。注釈に「断定回避（条件/前提）」を1行入れる。
- **インフォグラフィックはビジネスプロフェッショナルとして最高品質のものを作成すること。**（簡潔・明確・説得力のある図に仕上げる。）

---

## 執筆ルール（厳守）

### 固有の一文（冒頭2段落以内に1つ以上必須）
- **具体性**: 固有名詞的要素（「RACI表のA欄」「例外承認フロー」「証跡の欠落点」等）を含む。
- **意外性**: 読者が「そうだったのか」と感じる盲点・落とし穴。
- **非代替性**: この記事の unique_focus に直結する洞察。

### 断定の使い分け
- **断定禁止**: 法的効果（「準拠すれば違反にならない」）、将来予測（「規制は必ず施行される」）、普遍的効果（「この手法で問題は解決する」）。
- **断定可**: 定義・分類、確立した事実（出典・年明記）、手続き的事実。

### 数値・統計
- 許可: 一次資料の直接引用（法令・条項・発行年明記）、条件付き推定（前提明示）、相対表現（「多くの企業で」）。
- 禁止: 出典なしの「〇〇%」「調査によれば」等。

### 運用5要素
RACI / 申請→審査→例外→更新→棚卸 / 証跡 / 継続評価 / インシデント — のうち、このテーマに応じた項目を本文に含める。

### 禁止
- 抽象スローガンで段落を終わらせない（具体的行動/判断軸で締める）。
- 3点箇条書きの連打は2回まで。散文とリストを混ぜる。
- 一般的でない「日本語＋英語」の混在（例：閾値 breach）は避ける。カタカナ表記（閾値ブリーチ）にするか、括弧で日本語の説明を付記する。

---

## 出力形式（このとおりに出力すること）

以下を**マークダウン**で出力してください。見出しレベルとブロックを厳守。

```markdown
## リード（1段落）
（冒頭パターン Op に沿った導入＋unique_focus を明示。2段落目までに「固有の一文」を1つ含む。**です・ます調で、クレバーでプロフェッショナルな文体**にすること。）

## 本文
（Outline の見出しを h2 として使う。各セクションに1〜3段落。図1・図2・図3の直前に「ここに図Nを挿入」と書く。**全文です・ます調**。**本文の見出しに「次の一歩」を使わないこと**。結論用の「## 次の一歩」ブロックと重複するため、最後の本文セクションは「まとめとアクション」「実装のポイント」等とする。）

### 1. [Outline の1つ目の見出し]
（段落…）

ここに図1を挿入

### 2. [Outline の2つ目]
（段落…）

ここに図2を挿入

（以降、Outline に従いセクション＋図3の挿入位置）

## 図1（形式名）
（形式は SVG / HTML / Table / Canvas / Vega-Lite / Plotly / DOT / PlantUML 等から選択。Mermaidは禁止。該当するコードブロックのみ。**マトリクス・表**の場合は各セルに有意な内容をできるだけ埋める。サンプルなら「サンプル」と表記し、埋め方のガイドを書き添える。空セルのみは避ける。）

## 図2（形式名）
（別の形式を選ぶこと。上記「直前5記事で使用された形式」の各形式は1回まで。）

## 図3（形式名）
（3つ目も形式を変えること。）

## 図の型（記録用・必須）
図1: [A–Jの記号], 図2: [A–Jの記号], 図3: [A–Jの記号]
（例: 図1: D, 図2: B, 図3: G）

## 図の形式（記録用・必須）
図1: [形式名], 図2: [形式名], 図3: [形式名]
（例: 図1: SVG, 図2: HTML, 図3: Table）

## 固有の一文（要点ボックス用1文）
（この記事だけの洞察を1文で。）

## チェックリスト（10項目）
- （運用・証跡・監査に即した具体的な質問形式で10個）

## 参考文献（3つ以上、発行年または一次資料明記）
- （例: NIST AI RMF, 2023）
- （例: ISO/IEC 42001, 発行年）
- （例: 経済産業省 AI事業者ガイドライン, 2025）

## 次の一歩（結論パターン Co に沿って）
（**記事ごとに固有の内容**にすること。他記事と同形の「〇〇を1枚にまとめ、証跡の目次をすり合わせ、四半期で見直し」の繰り返しは禁止。この記事の unique_focus に直結する、本当に重要な1〜3のアクションを書く。結論パターン Co のトーンは活かしつつ、中身は他記事と被らせない。）
```
"""


def main():
    import argparse
    p = argparse.ArgumentParser(description="記事用のLLM執筆ブリーフを生成する")
    p.add_argument("article_no", type=int, nargs="?", help="記事番号 1–163。省略時は全件生成")
    p.add_argument("--stdout", action="store_true", help="1件のみ指定時、ファイルではなく標準出力に出す")
    args = p.parse_args()

    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    articles = parse_design_tables()
    templates = parse_templates_from_design()
    history = load_figure_usage_history()

    if args.article_no is not None:
        one = next((a for a in articles if a["no"] == args.article_no), None)
        if not one:
            print(f"Article {args.article_no} not found.", file=sys.stderr)
            sys.exit(1)
        idx = next(i for i, a in enumerate(articles) if a["no"] == args.article_no)
        brief = build_brief(one, templates, articles, idx, history)
        if args.stdout:
            print(brief)
        else:
            path = BRIEFS_DIR / f"{args.article_no:03d}-{one['slug']}.md"
            path.write_text(brief, encoding="utf-8")
            print("Wrote", path)
        return

    for i, a in enumerate(articles):
        brief = build_brief(a, templates, articles, i, history)
        path = BRIEFS_DIR / f"{a['no']:03d}-{a['slug']}.md"
        path.write_text(brief, encoding="utf-8")
        print("Wrote", path)
    print("Done. Generated", len(articles), "briefs in", BRIEFS_DIR)


if __name__ == "__main__":
    main()
