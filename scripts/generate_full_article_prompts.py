#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全163記事について、本文・チェックリスト・次の一歩・図・参考文献を Cursor 内で1から作成するための
依頼文（プロンプト）を生成し、Cursor の出力を llm-out.md に適用する。

原因: 現行の llm-out は gen_llm_out_31_163.py がテンプレのみで生成しており、
      本文は1文程度・チェックリストは全記事同一。Cursor 内で全文を作成し直すための手順を提供する。

使い方:
  1. 依頼文を163件生成する:
     python scripts/generate_full_article_prompts.py --prompts
     → docs/ai-governance-briefs/full_article_prompts/ に 001-slug-prompt.md ができる。

  2. 各依頼文を Cursor 内で渡し、出力を 001-slug-response.md として同じディレクトリに保存する。
     （これまで同様、Cursor の中で作成。）

  3. Cursor の出力を llm-out.md に一括適用する:
     python scripts/generate_full_article_prompts.py --apply-responses docs/ai-governance-briefs/full_article_prompts

  4. 記事HTMLを再生成する:
     for no in $(seq 1 163); do
       f=$(ls docs/ai-governance-briefs/$(printf "%03d" $no)-*-llm-out.md 2>/dev/null)
       [ -n "$f" ] && python scripts/apply_llm_article.py $no "$f"
     done
"""
import argparse
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"
PROMPTS_DIR = BRIEFS_DIR / "full_article_prompts"

# テンプレ別 Outline（gen_llm_out_31_163 と同期。セクション見出しのみ）
TEMPLATE_OUTLINES = {
    "T01": ["なぜAIで三線が崩れるか", "RACI最小セット", "例外が燃える構造と封じ方", "実装チェックリスト"],
    "T02": ["取締役会で聞かれる5問", "指標と運用", "雛形"],
    "T03": ["モデル選定", "ガードレール", "移行計画", "失敗例"],
    "T04": ["今年やるべき5領域", "予算と人材", "レビュー"],
    "T05": ["文書が形骸化する理由", "版管理", "教育", "監査視点"],
    "T06": ["許容度設計", "承認運用", "例外", "KRI"],
    "T07": ["評価設計", "実施と記録", "継続評価"],
    "T08": ["用語定義", "分界", "成果物", "実装の勘所"],
    "T09": ["所見の型", "原因", "是正テンプレ", "追跡KPI"],
    "T10": ["なぜ年1では不足か", "継続評価", "自動化", "運用設計"],
    "T11": ["開発での落とし穴", "統制", "証跡", "チェックリスト"],
    "T12": ["承認ゲート", "証跡", "失敗例", "テンプレ"],
    "T13": ["例外が増える理由", "抑制", "教育", "KRI"],
    "T14": ["何を測るか", "いつ測るか", "閾値", "証跡", "運用"],
    "T15": ["退役が監査で燃える理由", "手順", "証跡", "チェックリスト"],
    "T16": ["監査で必要なログ", "設計", "保全", "検証"],
    "T17": ["最小セット", "例", "落とし穴", "テンプレ"],
    "T18": ["連鎖設計", "実装", "運用", "監査提示"],
    "T19": ["争点シナリオ", "必要証拠", "保全", "テンプレ"],
    "T20": ["何を見るか", "誰が見るか", "閾値", "アクション"],
    "T21": ["リスク", "設計", "運用", "証跡"],
    "T22": ["漏えい経路", "統制", "運用", "監査提示"],
    "T23": ["脅威分類", "統制", "監視", "演習"],
    "T24": ["攻撃パターン", "対策", "評価", "運用"],
    "T25": ["選定基準", "評価プロセス", "契約・SLA", "継続監視", "証跡・監査"],
    "T26": ["何が論点か", "運用", "証跡", "チェックリスト"],
    "T27": ["境界定義", "統制", "契約", "運用"],
    "T28": ["品質が壊れる点", "測定", "是正", "証跡"],
    "T29": ["典型契約論点", "統制", "証跡", "雛形"],
    "T30": ["使い所", "限界", "運用", "証跡"],
    "T31": ["何が争点か", "方針", "手続き", "証跡", "チェック"],
    "T32": ["なぜ今か", "要求", "運用", "証跡"],
}


def parse_design():
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
                op_val = parts[8].strip() if len(parts) > 8 else "1"
                co_val = parts[9].strip() if len(parts) > 9 else "1"
                table_33.append({
                    "no": int(parts[0]), "slug": parts[1], "title_ja": parts[2], "T": parts[3],
                    "reader": parts[4], "purpose": parts[5], "depth": parts[6], "style": parts[7],
                    "Op": int(op_val) if op_val.isdigit() else 1,
                    "Co": int(co_val) if co_val.isdigit() else 1,
                })
    by_slug_32 = {r["slug"]: r for r in table_32}
    merged = []
    for r33 in table_33:
        no = r33["no"]
        if no < 1 or no > 163:
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


def build_prompt(article):
    """1記事分の Cursor 用プロンプト（依頼文）を組み立てる。"""
    no = article["no"]
    slug = article["slug"]
    title_ja = article["title_ja"]
    focus = article["unique_focus"]
    tid = article["template_id"]
    sections = (TEMPLATE_OUTLINES.get(tid) or ["論点の整理", "運用", "証跡", "まとめとアクション"])[:4]
    reader = article.get("reader", "Pract")
    purpose = article.get("purpose", "Impl")
    depth = article.get("depth", "Quick")
    style = article.get("style", "Prescriptive")

    s = f"""# 記事 No. {no}：{title_ja}

## 入力

- **slug**: {slug}
- **title_ja**: {title_ja}
- **unique_focus**: {focus}
- **template_id**: {tid}
- **記事DNA**: 読者={reader}, 目的={purpose}, 深さ={depth}, スタイル={style}
- **必須セクション見出し**: {', '.join(sections)}

## 依頼

上記の1記事分について、**ブログ記事の全文**を次の形式で生成してください。  
文体は**です・ます調**で、断定を避け条件・前提を明示してください。  
**記事内で章をまたいで同一の長文を繰り返さない**でください（「理念で終わらせず…5要素のうち」のような定型句はリードまたは第1セクションに1回のみ。第2セクション以降は言い換えのみ）。

### 出力形式（この見出し・コードブロック形式を厳守）

```markdown
## リード（1段落）

（1段落で、本稿の焦点と読者に役立つ導入。unique_focus を必ず反映すること。）

## 本文

### 1. {sections[0] if len(sections) > 0 else '概要'}

（2〜4段落で、このセクションの内容を具体的に記述。抽象的なスローガンで終わらせず、判断軸・手順・証跡など具体論を書く。）

ここに図1を挿入

### 2. {sections[1] if len(sections) > 1 else '運用'}

（2〜4段落。第1セクションと同一の長文を繰り返さない。）

ここに図2を挿入

### 3. {sections[2] if len(sections) > 2 else '証跡'}

（2〜4段落。）

ここに図3を挿入

### 4. {sections[3] if len(sections) > 3 else 'まとめとアクション'}

（1〜2段落。見出しは「次の一歩」にしない。）

## 図1（SVG）

```
<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
  （この記事のテーマに沿った簡潔なSVG。Mermaidは禁止。）
</svg>
```

## 図2（HTML）

```
<div style="max-width:520px; margin:1rem auto; border-left:3px solid #003E68; padding-left:1rem;">
  <p style="margin:0 0 0.5rem; font-weight:bold;">（キャプション）</p>
  <ul style="margin:0; padding-left:1.25rem;">（リスト項目）</ul>
</div>
```

## 図3（Table）

```
<table style="width:100%; max-width:520px; margin:1rem auto; border-collapse:collapse;">
  <thead><tr style="background:#f1f5f9;">（ヘッダ）</tr></thead>
  <tbody>（行）</tbody>
</table>
```

## 図の型（記録用・必須）
図1: A, 図2: B, 図3: G

## 図の形式（記録用・必須）
図1: SVG, 図2: HTML, 図3: Table

## 固有の一文（要点ボックス用1文）

（この記事だけの要点を1文で。明日から使える行動を1つ含む。）

## チェックリスト（10項目）

- （このテーマに特化した項目。「〜しているか」「〜を決めているか」形式。全記事で同じ汎用10項目にしないこと。8〜10項目。）
- …

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- （このテーマに合う文献を1つ以上追加）

## 次の一歩（結論パターン Co に沿って）

（明日から始められる2〜3文。本テーマの焦点と、自部門で「誰が承認者か」「証跡をどこに残すか」を1つ決め、監査法人に証憑の形を事前に1回確認する、といった具体的な一歩を含む。）
```

上記の ```markdown から ``` までを**そのまま**出力してください。図はSVG/HTML/Tableのいずれかで、この記事のテーマに沿った内容にしてください。チェックリストは**この記事の unique_focus に特化した項目**にし、他記事と同一の汎用リストにしないでください。
"""
    return s.strip()


def cmd_prompts():
    """163件のプロンプトを full_article_prompts/ に書き出す。"""
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    articles = parse_design()
    for a in articles:
        no, slug = a["no"], a["slug"]
        prompt = build_prompt(a)
        path = PROMPTS_DIR / f"{no:03d}-{slug}-prompt.md"
        path.write_text(prompt, encoding="utf-8")
        print(path.name)
    print(f"Wrote {len(articles)} prompts to {PROMPTS_DIR}")


def cmd_apply_responses(responses_dir):
    """responses_dir 内の *-response.md（Cursor 出力）を対応する *-llm-out.md に書き出す。"""
    responses_dir = Path(responses_dir)
    if not responses_dir.is_dir():
        print(f"Not a directory: {responses_dir}", file=sys.stderr)
        sys.exit(1)
    articles = parse_design()
    by_no_slug = {(a["no"], a["slug"]): a for a in articles}
    applied = 0
    for path in sorted(responses_dir.glob("*-response.md")):
        # 001-accountability-incident-design-response.md → 001-accountability-incident-design-llm-out.md
        name = path.stem  # 001-accountability-incident-design-response
        if not name.endswith("-response"):
            continue
        base = name[: -len("-response")]  # 001-accountability-incident-design
        parts = base.split("-", 1)
        if len(parts) != 2 or not parts[0].isdigit():
            continue
        no = int(parts[0])
        slug = parts[1]
        if (no, slug) not in by_no_slug:
            continue
        content = path.read_text(encoding="utf-8")
        # Cursor が「```markdown ... ```」で返した場合はその中身だけを llm-out にする
        m = re.search(r"```(?:markdown)?\s*\n(.*?)```", content, re.DOTALL)
        if m:
            content = m.group(1).strip()
        # それ以外は全文を llm-out として使う
        out_path = BRIEFS_DIR / f"{no:03d}-{slug}-llm-out.md"
        out_path.write_text(content, encoding="utf-8")
        applied += 1
        print(out_path.name)
    print(f"Applied {applied} responses to llm-out.md files in {BRIEFS_DIR}")


def main():
    parser = argparse.ArgumentParser(description="全記事を Cursor 内で1から作成する依頼文生成と出力の適用")
    parser.add_argument("--prompts", action="store_true", help="163件のプロンプトを full_article_prompts/ に生成")
    parser.add_argument("--apply-responses", metavar="DIR", help="DIR 内の *-response.md を *-llm-out.md に適用")
    args = parser.parse_args()
    if args.prompts:
        cmd_prompts()
    elif args.apply_responses:
        cmd_apply_responses(args.apply_responses)
    else:
        parser.print_help()
        print("\n例: python scripts/generate_full_article_prompts.py --prompts")
        print("     python scripts/generate_full_article_prompts.py --apply-responses docs/ai-governance-briefs/full_article_prompts")


if __name__ == "__main__":
    main()
