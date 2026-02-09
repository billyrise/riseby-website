#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全記事の「すぐ使えるチェックリスト」を記事内容に沿ったものにLLMで更新する。

使い方:
  1. プロンプトを生成し、LLMに送ってチェックリストを生成させる:
     python scripts/update_checklist_llm.py --prompts
     → docs/ai-governance-briefs/checklist_prompts.md を生成する。
     このファイルの内容をLLMに送り、出力を checklist_responses.md に保存する。

  2. LLMの出力を各 llm-out.md に適用する:
     python scripts/update_checklist_llm.py --apply docs/ai-governance-briefs/checklist_responses.md

  3. 記事HTMLを再生成する（任意）:
     for i in $(seq 1 163); do python scripts/apply_llm_article.py $i docs/ai-governance-briefs/$(ls docs/ai-governance-briefs/*-llm-out.md | head -n $i | tail -n 1 | xargs basename); done
     または apply_llm_article を 1..163 で一括実行する既存の方法を使う。
"""
import argparse
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"


def parse_design():
    """設計図から 3.2 と 3.3 をパースし、no, slug, title_ja, unique_focus の一覧を返す。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    table_32 = []
    table_33 = []
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
            if len(parts) >= 4 and parts[0].isdigit():
                no = int(parts[0])
                if 1 <= no <= 163:
                    table_32.append({"no": no, "slug": parts[1], "template_id": parts[2], "unique_focus": parts[3]})
        if in_33 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit():
                no = int(parts[0])
                if 1 <= no <= 163:
                    table_33.append({"no": no, "slug": parts[1], "title_ja": parts[2]})
    by_no_32 = {r["no"]: r for r in table_32}
    by_no_33 = {r["no"]: r for r in table_33}
    merged = []
    for no in range(1, 164):
        r33 = by_no_33.get(no)
        r32 = by_no_32.get(no)
        if not r33:
            continue
        merged.append({
            "no": no,
            "slug": r33["slug"],
            "title_ja": r33["title_ja"],
            "unique_focus": (r32 or {}).get("unique_focus", ""),
        })
    return merged


def cmd_prompts():
    """LLMに送るプロンプトを生成し、checklist_prompts.md に書き出す。"""
    articles = parse_design()
    out_path = BRIEFS_DIR / "checklist_prompts.md"
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 記事別「すぐ使えるチェックリスト」生成",
        "",
        "以下は163記事のタイトルと焦点（unique_focus）です。",
        "**各記事について、その内容に沿った「すぐ使えるチェックリスト」を8〜10項目で作成してください。**",
        "",
        "ルール:",
        "- 各項目は「〜しているか」「〜を決めているか」「〜を文書化しているか」などの短文にすること。",
        "- 汎用的なRACI・証跡・四半期棚卸などの一般論だけでなく、**そのテーマに特化した項目**を必ず含めること。",
        "- 全記事で同じ項目リストにならないよう、記事の焦点に合わせて中身を変えること。",
        "",
        "出力形式（記事No.ごとに必ずこの形式で出力すること）:",
        "```",
        "## 1",
        "- 項目1",
        "- 項目2",
        "...",
        "",
        "## 2",
        "- 項目1",
        "...",
        "```",
        "",
        "---",
        "",
        "## 記事一覧（No. / title_ja / unique_focus）",
        "",
    ]
    for a in articles:
        lines.append(f"### No. {a['no']}")
        lines.append(f"- **title_ja**: {a['title_ja']}")
        lines.append(f"- **unique_focus**: {a['unique_focus']}")
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path}")
    print("このファイルの内容をLLMに送り、出力を checklist_responses.md として保存してください。")
    print("その後、以下で適用: python scripts/update_checklist_llm.py --apply docs/ai-governance-briefs/checklist_responses.md")


def parse_llm_response(response_path):
    """LLM出力ファイルをパースし、no -> [item1, item2, ...] の辞書を返す。"""
    text = Path(response_path).read_text(encoding="utf-8")
    # コードブロックがあればその中身だけを使う
    m = re.search(r"```(?:markdown)?\s*\n(.*?)```", text, re.DOTALL)
    if m:
        text = m.group(1).strip()
    by_no = {}
    current_no = None
    current_items = []
    for line in text.splitlines():
        # "## 1" または "## No. 1" 形式
        m = re.match(r"^##\s*(?:No\.?\s*)?(\d+)\s*$", line.strip())
        if m:
            if current_no is not None and current_items:
                by_no[current_no] = current_items
            current_no = int(m.group(1))
            current_items = []
            continue
        line = line.strip()
        if (line.startswith("- ") or line.startswith("* ")) and current_no is not None:
            current_items.append(line[2:].strip())
    if current_no is not None and current_items:
        by_no[current_no] = current_items
    return by_no


def cmd_apply(response_path):
    """LLM出力を各 *-llm-out.md のチェックリスト欄に適用する。"""
    by_no = parse_llm_response(response_path)
    articles = parse_design()
    updated = 0
    missing = []
    for a in articles:
        no = a["no"]
        slug = a["slug"]
        items = by_no.get(no)
        if not items:
            missing.append(no)
            continue
        # ファイル名: 001-accountability-incident-design-llm-out.md
        fname = f"{no:03d}-{slug}-llm-out.md"
        path = BRIEFS_DIR / fname
        if not path.exists():
            missing.append(f"{no}(file not found)")
            continue
        text = path.read_text(encoding="utf-8")
        # "## チェックリスト（10項目）" または "## チェックリスト" から次の "## " までを置換（ヘッダー行は維持）
        pattern = re.compile(
            r"(## チェックリスト[^\n]*\s*\n)(.*?)(?=\n## |\Z)",
            re.DOTALL,
        )
        if not pattern.search(text):
            print(f"Warning: No checklist section in {path.name}", file=sys.stderr)
            continue
        new_text = pattern.sub(
            lambda m: m.group(1) + "\n".join("- " + it for it in items) + "\n",
            text,
            count=1,
        )
        path.write_text(new_text, encoding="utf-8")
        updated += 1
        print(path.name)
    print(f"Updated: {updated}")
    if missing:
        print(f"Missing or no checklist for No.: {missing[:20]}{'...' if len(missing) > 20 else ''}", file=sys.stderr)


def _theme_to_checklist(no, title_ja, unique_focus):
    """テーマに沿ったチェックリスト項目をヒューリスティックに生成（LLM未使用時のフォールバック）。"""
    focus = (unique_focus or "").replace("に特化", "").strip("「」\"'")
    # テーマキーワードに応じた項目テンプレ＋共通1〜2項目
    items = []
    if "Accountability" in focus or "説明責任" in title_ja or "誰が何を" in focus:
        items = [
            "インシデント時の一次責任者をRACIで決めているか",
            "報告・エスカレーションの受け手を文書化しているか",
            "証憑の提出先（監査・当局）を決めているか",
            "例外承認の権限者を決めているか",
            "証跡の保管責任者を決めているか",
            "継続評価の担当を決めているか",
            "監査対応の窓口を決めているか",
            "申請―審査―承認のフローを文書化しているか",
        ]
    elif "Zero Trust" in focus or "アクセス制御" in title_ja:
        items = [
            "AI利用の申請フローを決めているか",
            "最小権限でアクセスを付与しているか",
            "利用者と用途の紐付けを記録しているか",
            "承認者と付与ログを残しているか",
            "定期的なアクセス棚卸を予定しているか",
            "例外利用の有効期限を決めているか",
            "オンボーディング/オフボーディング手順を文書化しているか",
            "監査で提出するアクセス証跡の形式を決めているか",
        ]
    elif "Assurance" in focus or "証憑" in focus or "監査の分界" in title_ja:
        items = [
            "保証（内部）と監査（外部）の成果物を分けて定義しているか",
            "証憑の形式を監査と事前合意しているか",
            "証跡の完全性（改ざん耐性）を確保しているか",
            "サンプリング方針を文書化しているか",
            "是正の記録と追跡を残しているか",
            "監査提出用のバンドル形式を決めているか",
            "継続評価の記録を保全しているか",
            "責任分界をRACIで明示しているか",
        ]
    elif "AI-BOM" in focus or "BOM" in title_ja:
        items = [
            "AI-BOMの構成要素（モデル・データ・ツール）を定義しているか",
            "90日以内の実装ステップを決めているか",
            "供給元と版を記録しているか",
            "更新・棚卸の頻度を決めているか",
            "監査提出用のBOM形式を決めているか",
            "責任分界（自社/ベンダー）を文書化しているか",
            "変更時の承認フローを決めているか",
            "証跡を改ざん耐性で保全しているか",
        ]
    elif "供給網" in focus or "責任分界" in focus:
        items = [
            "ベンダー・自社の責任範囲を契約で明示しているか",
            "受け渡し成果物と証跡を決めているか",
            "インシデント時の連携窓口を決めているか",
            "監査提出物の出所を整理しているか",
            "SLAとエスカレーションを文書化しているか",
            "継続監視の担当を決めているか",
            "契約条項と運用の対応表を一覧化しているか",
            "四半期の棚卸を予定しているか",
        ]
    elif "脅威" in focus or "サイバー" in title_ja:
        items = [
            "AI関連の脅威を分類し優先順位を付けているか",
            "脅威ごとの統制を文書化しているか",
            "検知・対応の手順を決めているか",
            "演習やテストを予定しているか",
            "KRIと閾値を決めているか",
            "インシデント時の隔離手順を決めているか",
            "監査で説明できる証跡を残しているか",
            "継続評価の記録を残しているか",
        ]
    elif "データ統制" in focus or "接合点" in focus:
        items = [
            "データガバナンスとAIガバナンスの担当を接合しているか",
            "個人データ・機密データの取り扱い境界を決めているか",
            "DPIAとAIリスク評価の連携を決めているか",
            "証跡の保管場所と形式を統一しているか",
            "規制・標準との対応を一覧化しているか",
            "継続評価の記録を残しているか",
            "監査提出の窓口を決めているか",
            "四半期の棚卸を予定しているか",
        ]
    elif "委員会" in focus or "形骸化" in focus:
        items = [
            "倫理委員会の権限と議題を決めているか",
            "委員の構成と役割を文書化しているか",
            "議事録と承認記録を残しているか",
            "例外案件の提出形式を決めているか",
            "是正フォローアップの担当を決めているか",
            "年次・四半期のレビューを予定しているか",
            "監査で説明できる証跡を残しているか",
            "教育・周知の記録を残しているか",
        ]
    elif "理念" in focus or "手続き" in focus or "倫理原則" in title_ja:
        items = [
            "倫理原則を承認フローに落とし込んでいるか",
            "例外の基準と有効期限を決めているか",
            "証跡を改ざん耐性で保全しているか",
            "継続評価の記録を残しているか",
            "監査で説明できる証憑の形式を決めているか",
            "規制・標準との対応を一覧化しているか",
            "四半期の棚卸を予定しているか",
            "教育・周知の記録を残しているか",
        ]
    elif "UI表示" in focus or "誤認防止" in focus or "生成コンテンツ" in title_ja:
        items = [
            "AI生成である旨の表示方針を決めているか",
            "表示場所・表示文言を文書化しているか",
            "誤認防止のチェックをリリース前に実施しているか",
            "表示の証跡を残しているか",
            "規制・ガイドラインとの対応を確認しているか",
            "監査で説明できる形式を決めているか",
            "教育・周知の記録を残しているか",
            "四半期の見直しを予定しているか",
        ]
    else:
        # 汎用：焦点・タイトルからキーワードを抜き出し、テーマに沿った8項目を組み立てる
        kw = focus.replace("「", "").replace("」", "").replace(""", "").replace(""", "").strip() or title_ja[:20]
        items = [
            f"{kw}について責任者・担当を決めているか",
            f"{kw}の申請―審査―承認フローを文書化しているか",
            "例外の基準と有効期限を決めているか",
            "証跡を改ざん耐性で保全しているか",
            "継続評価の記録を残しているか",
            "インシデント時の報告・エスカレーション手順があるか",
            "規制・標準との対応を一覧化しているか（断定は避ける）",
            "監査で説明できる証憑の形式を決めているか",
        ]
    return items[:10]


def cmd_generate():
    """設計図からテーマ別チェックリストをヒューリスティックに生成し、checklist_responses.md に出力する。LLM未使用。"""
    articles = parse_design()
    out_path = BRIEFS_DIR / "checklist_responses.md"
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    lines = []
    for a in articles:
        lines.append(f"## {a['no']}")
        items = _theme_to_checklist(a["no"], a["title_ja"], a["unique_focus"])
        for it in items:
            lines.append(f"- {it}")
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path} ({len(articles)} articles)")
    print("Apply with: python scripts/update_checklist_llm.py --apply docs/ai-governance-briefs/checklist_responses.md")


def main():
    parser = argparse.ArgumentParser(description="記事別チェックリストをLLMで更新する")
    parser.add_argument("--prompts", action="store_true", help="LLM用プロンプトを checklist_prompts.md に出力")
    parser.add_argument("--generate", action="store_true", help="設計図からテーマ別チェックリストを生成（LLM未使用・ヒューリスティック）")
    parser.add_argument("--apply", metavar="FILE", help="LLM出力ファイルを各 llm-out.md に適用")
    args = parser.parse_args()
    if args.prompts:
        cmd_prompts()
    elif args.generate:
        cmd_generate()
    elif args.apply:
        cmd_apply(args.apply)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
