#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
設計図（docs/ai-governance-blog-design.md）と cursor プロンプトに基づき、
AIガバナンスカテゴリの index.html と 163 記事を生成する。
"""
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
OUT_DIR = BASE_DIR / "blog" / "ai-governance"

# テンプレ → セクション（ツリー用）
TEMPLATE_TO_SECTION = {
    "T01": "A", "T02": "A", "T03": "A", "T04": "A", "T05": "A",
    "T06": "B", "T07": "B", "T08": "B", "T09": "B", "T10": "B",
    "T11": "C", "T12": "C", "T13": "C", "T14": "C", "T15": "C",
    "T16": "D", "T17": "D", "T18": "D", "T19": "D", "T20": "D",
    "T21": "E", "T22": "E", "T23": "E", "T24": "E", "T25": "I",
    "T26": "F", "T27": "F", "T28": "F", "T29": "F", "T30": "F",
    "T31": "G", "T32": "G",
}

# テンプレ別 Outline（必須セクション見出し）と Mermaid 3種
TEMPLATE_OUTLINES = {
    "T01": (["なぜAIで三線が崩れるか", "RACI最小セット", "例外が燃える構造と封じ方", "実装チェックリスト"], "graph LR\n  Board[Board] --> Legal[Legal]\n  Legal --> CISO[CISO]\n  CISO --> Audit[Audit]\n  style Audit fill:#fef9c3", "graph TD\n  申請 --> 審査\n  審査 --> 承認\n  承認 --> 例外申請\n  例外申請 --> 棚卸\n  style 承認 fill:#e0f2fe", "graph TD\n  T1[責任者不明]\n  T2[証跡欠落]\n  T3[例外だらけ]\n  T4[境界曖昧]\n  T5[継続評価なし]\n  style T1 fill:#fee2e2"),
    "T02": (["取締役会で聞かれる5問", "指標と運用", "雛形"], "graph TD\n  K1[KPI/KRI]\n  K2[意思決定ログ]\n  K3[四半期レビュー]\n  style K1 fill:#e0f2fe", "graph LR\n  Q1[四半期1] --> Q2[四半期2]\n  Q2 --> Q3[四半期3]\n  Q3 --> Q4[四半期4]\n  style Q2 fill:#dcfce7", "graph LR\n  Board[Board]\n  Legal[Legal]\n  CISO[CISO]\n  Audit[Audit]\n  style Board fill:#e0f2fe"),
    "T03": (["モデル選定", "ガードレール", "移行計画", "失敗例"], "graph TD\n  集中 --> 統制A\n  分散 --> 統制B\n  統制A --> 抜け穴\n  統制B --> 抜け穴\n  style 抜け穴 fill:#fee2e2", "graph TD\n  P[Policy] --> Pr[Process]\n  Pr --> E[Evidence]\n  style E fill:#fef9c3", "graph LR\n  Now[現状] --> 移行\n  移行 --> Target[目標]\n  style 移行 fill:#e0f2fe"),
    "T04": (["今年やるべき5領域", "予算と人材", "レビュー"], "graph LR\n  Y[年次] --> Q1[Q1]\n  Q1 --> Q2[Q2]\n  Q2 --> Q3[Q3]\n  Q3 --> Q4[Q4]\n  style Q2 fill:#dcfce7", "graph TD\n  K1[KPI]\n  K2[KRI]\n  K3[ROI]\n  style K1 fill:#e0f2fe", "graph TD\n  投資 --> 効果\n  効果 --> 再作業削減\n  効果 --> 差し戻し削減\n  style 効果 fill:#dcfce7"),
    "T05": (["文書が形骸化する理由", "版管理", "教育", "監査視点"], "graph LR\n  文書 --> 承認\n  承認 --> 配布\n  配布 --> 証跡\n  style 証跡 fill:#dcfce7", "graph TD\n  変更申請 --> 審査\n  審査 --> 承認\n  承認 --> 版更新\n  style 版更新 fill:#e0f2fe", "graph TD\n  T1[版不明]\n  T2[変更記録なし]\n  T3[読まれない]\n  T4[抵抗未対処]\n  T5[監査指摘]\n  style T1 fill:#fee2e2"),
    "T06": (["許容度設計", "承認運用", "例外", "KRI"], "graph TD\n  影響 --> 確率\n  確率 --> 許容\n  許容 --> 承認\n  style 許容 fill:#fef9c3", "graph TD\n  申請 --> 審査\n  審査 --> 承認/却下\n  承認/却下 --> 記録\n  style 記録 fill:#dcfce7", "graph TD\n  P[Policy] --> Pr[Process]\n  Pr --> E[Evidence]\n  style E fill:#e0f2fe"),
    "T07": (["評価設計", "実施と記録", "継続評価"], "graph TD\n  リスク領域 --> 定性\n  リスク領域 --> 定量\n  定量 --> バイアス\n  style 定量 fill:#e0f2fe", "graph LR\n  P[Plan] --> B[Build]\n  B --> D[Deploy]\n  D --> O[Operate]\n  O --> R[Retire]\n  style O fill:#dcfce7", "graph TD\n  K1[評価完了率]\n  K2[是正件数]\n  K3[ドリフト検知]\n  style K1 fill:#fef9c3"),
    "T08": (["用語定義", "分界", "成果物", "実装の勘所"], "graph TD\n  P[Policy] --> Proof[Proof]\n  Proof --> Assurance[Assurance]\n  Assurance --> Audit[Audit]\n  style Audit fill:#fef9c3", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7", "graph TD\n  T1[証憑形式不一致]\n  T2[責任者欠落]\n  T3[事後再構成]\n  T4[サンプル説明なし]\n  T5[継続評価なし]\n  style T1 fill:#fee2e2"),
    "T09": (["所見の型", "原因", "是正テンプレ", "追跡KPI"], "graph TD\n  T1[設計不備]\n  T2[運用ずれ]\n  T3[証跡欠落]\n  T4[境界不明]\n  T5[継続評価なし]\n  style T1 fill:#fee2e2", "graph TD\n  K1[是正率]\n  K2[完了日数]\n  K3[再発件数]\n  style K1 fill:#e0f2fe", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style P fill:#dcfce7"),
    "T10": (["なぜ年1では不足か", "継続評価", "自動化", "運用設計"], "graph TD\n  Dev[開発] --> Test[テスト]\n  Test --> Gate[ゲート]\n  Gate --> Deploy[デプロイ]\n  style Gate fill:#fef9c3", "graph TD\n  K1[適合率]\n  K2[自動化率]\n  K3[是正日数]\n  style K1 fill:#e0f2fe", "graph LR\n  P[Plan] --> B[Build]\n  B --> D[Deploy]\n  D --> O[Operate]\n  O --> R[Retire]\n  style O fill:#dcfce7"),
    "T11": (["開発での落とし穴", "統制", "証跡", "チェックリスト"], "graph TD\n  P[方針] --> Pr[プロセス]\n  Pr --> E[証跡]\n  style E fill:#fef9c3", "graph TD\n  申請 --> 審査\n  審査 --> 承認\n  承認 --> 記録\n  style 記録 fill:#dcfce7", "graph LR\n  Board[Board]\n  Legal[Legal]\n  CISO[CISO]\n  Audit[Audit]\n  BU[BU]\n  IT[IT]\n  style Audit fill:#e0f2fe"),
    "T12": (["承認ゲート", "証跡", "失敗例", "テンプレ"], "graph TD\n  申請 --> 審査\n  審査 --> 承認\n  承認 --> デプロイ\n  デプロイ --> 記録\n  style 記録 fill:#dcfce7", "graph LR\n  P[Plan] --> B[Build]\n  B --> D[Deploy]\n  D --> O[Operate]\n  O --> R[Retire]\n  style D fill:#e0f2fe", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7"),
    "T13": (["例外が増える理由", "抑制", "教育", "KRI"], "graph TD\n  例外申請 --> 審査\n  審査 --> 承認/却下\n  承認/却下 --> 有効期限\n  有効期限 --> 棚卸\n  style 棚卸 fill:#e0f2fe", "graph TD\n  K1[例外件数]\n  K2[是正率]\n  K3[教育完了]\n  style K1 fill:#fef9c3", "graph TD\n  行動 --> 統制\n  統制 --> インセンティブ\n  style 統制 fill:#dcfce7"),
    "T14": (["何を測るか", "いつ測るか", "閾値", "証跡", "運用"], "graph TD\n  Dev --> Test\n  Test --> Gate\n  Gate --> Deploy\n  style Gate fill:#fef9c3", "graph TD\n  K1[品質指標]\n  K2[安全指標]\n  K3[ドリフト]\n  style K1 fill:#e0f2fe", "graph LR\n  P[Plan] --> B[Build]\n  B --> D[Deploy]\n  D --> O[Operate]\n  O --> R[Retire]\n  style O fill:#dcfce7"),
    "T15": (["退役が監査で燃える理由", "手順", "証跡", "チェックリスト"], "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7", "graph LR\n  D[廃止決定] --> 手順\n  手順 --> 記録\n  記録 --> 保管\n  style 記録 fill:#e0f2fe", "graph TD\n  T1[記録なし]\n  T2[責任不明]\n  T3[再現不能]\n  T4[保持違反]\n  T5[監査指摘]\n  style T1 fill:#fee2e2"),
    "T16": (["監査で必要なログ", "設計", "保全", "検証"], "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7", "graph TD\n  ログ種別 --> 目的\n  目的 --> 保持期間\n  style 目的 fill:#e0f2fe", "graph TD\n  K1[完全性]\n  K2[保持率]\n  K3[改ざん検知]\n  style K1 fill:#fef9c3"),
    "T17": (["最小セット", "例", "落とし穴", "テンプレ"], "graph TD\n  P[Policy] --> M[Minimum set]\n  M --> E[Evidence]\n  style M fill:#e0f2fe", "graph TD\n  T1[目次欠落]\n  T2[日付不整合]\n  T3[責任者なし]\n  T4[版なし]\n  T5[ハッシュなし]\n  style T1 fill:#fee2e2", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style P fill:#dcfce7"),
    "T18": (["連鎖設計", "実装", "運用", "監査提示"], "graph LR\n  L[ログ] --> V[検証]\n  V --> H[ハッシュ]\n  H --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7", "graph TD\n  生成 --> 保管\n  保管 --> 提出\n  提出 --> 検証\n  style 提出 fill:#e0f2fe", "graph TD\n  要件 --> 成果物\n  成果物 --> 形式\n  style 成果物 fill:#fef9c3"),
    "T19": (["争点シナリオ", "必要証拠", "保全", "テンプレ"], "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style P fill:#e0f2fe", "graph TD\n  T1[証拠欠落]\n  T2[日付不整合]\n  T3[責任不明]\n  T4[文書矛盾]\n  T5[改ざん疑い]\n  style T1 fill:#fee2e2", "graph LR\n  Board[Board]\n  Legal[Legal]\n  Audit[Audit]\n  style Legal fill:#e0f2fe"),
    "T20": (["何を見るか", "誰が見るか", "閾値", "アクション"], "graph TD\n  K1[KRI1]\n  K2[KRI2]\n  K3[KRI3]\n  閾値 --> エスカレーション\n  style 閾値 fill:#fee2e2", "graph LR\n  Q1[四半期1] --> Q2[四半期2]\n  Q2 --> レビュー\n  レビュー --> アクション\n  style レビュー fill:#e0f2fe", "graph LR\n  Board[Board]\n  Audit[Audit]\n  BU[BU]\n  style Board fill:#e0f2fe"),
    "T21": (["リスク", "設計", "運用", "証跡"], "graph TD\n  主体 --> 権限\n  権限 --> データ\n  データ --> 最小権限\n  style 最小権限 fill:#dcfce7", "graph TD\n  申請 --> 審査\n  審査 --> 承認\n  承認 --> 付与\n  付与 --> 記録\n  style 記録 fill:#e0f2fe", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7"),
    "T22": (["漏えい経路", "統制", "運用", "監査提示"], "graph TD\n  入力 --> 境界\n  境界 --> 出力\n  境界 --> 学習データ\n  style 境界 fill:#e0f2fe", "graph TD\n  経路 --> DLP\n  経路 --> IDP\n  経路 --> CASB\n  style DLP fill:#dcfce7", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style P fill:#e0f2fe"),
    "T23": (["脅威分類", "統制", "監視", "演習"], "graph TD\n  脅威1 --> 統制1\n  脅威2 --> 統制2\n  脅威3 --> 統制3\n  style 統制1 fill:#dcfce7", "graph LR\n  P[Plan] --> B[Build]\n  B --> D[Deploy]\n  D --> O[Operate]\n  O --> R[Retire]\n  style O fill:#e0f2fe", "graph TD\n  K1[検知率]\n  K2[インシデント]\n  K3[是正日数]\n  style K1 fill:#fef9c3"),
    "T24": (["攻撃パターン", "対策", "評価", "運用"], "graph TD\n  Dev --> Test\n  Test --> Gate\n  Gate --> Deploy\n  style Gate fill:#fef9c3", "graph TD\n  攻撃 --> 対策\n  対策 --> 検知\n  検知 --> 是正\n  style 対策 fill:#dcfce7", "graph TD\n  K1[検知率]\n  K2[ブロック率]\n  K3[インシデント]\n  style K1 fill:#e0f2fe"),
    "T25": (["選定基準", "評価プロセス", "契約・SLA", "継続監視", "証跡・監査"], "graph LR\n  提供者 --> 自社\n  委託先 --> 自社\n  自社 --> 責任分界\n  style 責任分界 fill:#fef9c3", "graph TD\n  要件 --> ベンダー選定\n  ベンダー選定 --> 契約\n  契約 --> 監視\n  style 契約 fill:#e0f2fe", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7"),
    "T26": (["何が論点か", "運用", "証跡", "チェックリスト"], "graph TD\n  データ種類 --> 義務\n  義務 --> DPIA\n  DPIA --> 承認\n  style 承認 fill:#dcfce7", "graph TD\n  P[Policy] --> Pr[Process]\n  Pr --> E[Evidence]\n  style E fill:#e0f2fe", "graph TD\n  申請 --> DPIA\n  DPIA --> 承認\n  承認 --> 利用\n  利用 --> 記録\n  style 記録 fill:#dcfce7"),
    "T27": (["境界定義", "統制", "契約", "運用"], "graph TD\n  入力 --> 境界\n  境界 --> 出力\n  学習 --> 境界\n  style 境界 fill:#e0f2fe", "graph LR\n  提供者 --> 自社\n  自社 --> 契約境界\n  style 契約境界 fill:#fef9c3", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style P fill:#dcfce7"),
    "T28": (["品質が壊れる点", "測定", "是正", "証跡"], "graph TD\n  K1[品質KRI]\n  K2[閾値]\n  K3[是正率]\n  style K1 fill:#e0f2fe", "graph LR\n  P[Plan] --> B[Build]\n  B --> D[Deploy]\n  D --> O[Operate]\n  O --> R[Retire]\n  style O fill:#dcfce7", "graph TD\n  データ --> リスク\n  リスク --> 統制\n  style リスク fill:#fee2e2"),
    "T29": (["典型契約論点", "統制", "証跡", "雛形"], "graph LR\n  提供者 --> 自社\n  委託先 --> 自社\n  自社 --> 法域\n  style 法域 fill:#fef9c3", "graph TD\n  データ --> 法域\n  法域 --> 条項\n  style 条項 fill:#e0f2fe", "graph LR\n  L[ログ] --> V[検証]\n  V --> S[保全]\n  S --> P[提出]\n  style S fill:#dcfce7"),
    "T30": (["使い所", "限界", "運用", "証跡"], "graph TD\n  手法 --> 効果\n  効果 --> 限界\n  限界 --> 注記\n  style 限界 fill:#fef9c3", "graph TD\n  P[Policy] --> Pr[Process]\n  Pr --> E[Evidence]\n  style E fill:#e0f2fe", "graph TD\n  K1[匿名化率]\n  K2[再識別リスク]\n  K3[監査記録]\n  style K1 fill:#e0f2fe"),
    "T31": (["何が争点か", "方針", "手続き", "証跡", "チェック"], "graph TD\n  用途 --> リスク\n  リスク --> 対応\n  style 対応 fill:#dcfce7", "graph TD\n  P[Policy] --> Pr[Process]\n  Pr --> E[Evidence]\n  style E fill:#e0f2fe", "graph TD\n  T1[権利未確認]\n  T2[表示欠落]\n  T3[証跡なし]\n  T4[方針矛盾]\n  T5[監査指摘]\n  style T1 fill:#fee2e2"),
    "T32": (["なぜ今か", "要求", "運用", "証跡"], "graph TD\n  コンテンツ種別 --> 義務\n  義務 --> 表示\n  style 表示 fill:#e0f2fe", "graph TD\n  作成 --> 分類\n  分類 --> チェック\n  チェック --> 公開\n  公開 --> 記録\n  style 記録 fill:#dcfce7", "graph TD\n  T1[表示なし]\n  T2[分類曖昧]\n  T3[チェックなし]\n  T4[証跡なし]\n  T5[Watermark過信]\n  style T1 fill:#fee2e2"),
}

def parse_design():
    """設計図から 3.2 と 3.3 の表をパースする。"""
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
                no, slug, template_id, focus = parts[0], parts[1], parts[2], parts[3]
                table_32.append({"no": int(no), "slug": slug, "template_id": template_id, "unique_focus": focus})
        if in_33 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit():
                no, slug, title_ja, t, reader, purpose, depth, style, op, co = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8], parts[9]
                table_33.append({"no": int(no), "slug": slug, "title_ja": title_ja, "T": t, "reader": reader, "purpose": purpose, "depth": depth, "style": style, "Op": int(op), "Co": int(co)})
    # merge by slug
    by_slug_32 = {r["slug"]: r for r in table_32}
    by_slug_33 = {r["slug"]: r for r in table_33}
    merged = []
    for no in range(1, 164):
        slug_33 = next((r["slug"] for r in table_33 if r["no"] == no), None)
        if not slug_33:
            continue
        r33 = by_slug_33[slug_33]
        r32 = by_slug_32.get(slug_33, {})
        merged.append({
            "no": no,
            "slug": slug_33,
            "title_ja": r33["title_ja"],
            "template_id": r32.get("template_id") or r33["T"],
            "unique_focus": r32.get("unique_focus", ""),
            "reader": r33["reader"],
            "purpose": r33["purpose"],
            "depth": r33["depth"],
            "style": r33["style"],
            "Op": r33["Op"],
            "Co": r33["Co"],
        })
    return merged


def esc(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${").replace("\n", "\\n")


def section_body_from_focus(focus, section_title, template_id, section_index=0):
    """unique_focus とセクション見出しから1段落の本文を生成。同一長文繰り返し禁止のため、定型句は第1セクションのみ。"""
    focus_short = focus.replace("に特化", "").strip("「」\"'")
    base = "理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理する。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえる。"
    if section_index == 0:
        return f"本稿の焦点は「{focus_short}」である。{section_title}では、{base}"
    # 「ここでは〜について、このテーマに応じた観点を整理する。」は使わない（ルールで禁止）
    return f"このセクションでは、責任分界・証跡・監査の観点を押さえる。"


def checklist_generic(template_id):
    """テンプレに応じた汎用チェックリスト10項目。"""
    base = [
        "RACI（責任者）を決めているか",
        "申請―審査―承認のフローを文書化しているか",
        "例外の基準と有効期限を決めているか",
        "証跡を改ざん耐性で保全しているか",
        "継続評価の記録を残しているか",
        "インシデント時の報告・エスカレーション手順があるか",
        "規制・標準との対応関係を一覧化しているか（断定は避ける）",
        "監査で説明できる証憑の形式を決めているか",
        "四半期の棚卸を予定しているか",
        "教育・周知の記録を残しているか",
    ]
    return base


def build_article_html(article):
    """1記事分のHTMLを組み立てる。"""
    slug = article["slug"]
    title = article["title_ja"]
    focus = article["unique_focus"]
    template_id = article["template_id"]
    op = article["Op"]
    outline_and_mermaid = TEMPLATE_OUTLINES.get(template_id, (["概要", "設計", "運用", "証跡"], "graph LR\n  A --> B\n  B --> C", "graph TD\n  X --> Y\n  Y --> Z", "graph TD\n  T1[差し戻し1]\n  T2[差し戻し2]\n  T3[差し戻し3]"))
    section_titles, m1, m2, m3 = outline_and_mermaid[0], outline_and_mermaid[1], outline_and_mermaid[2], outline_and_mermaid[3]
    # リード: unique_focus を冒頭に
    focus_clean = focus.replace("に特化", "").strip("「」\"'")
    lead = f"本稿の焦点は「{focus_clean}」である。理念で終わらせず、運用・証跡・監査可能性に落とすための要件を整理する。"
    description = title + "。運用に落とすための要件・証跡・チェックリストを整理する。"
    m1_esc, m2_esc, m3_esc = esc(m1), esc(m2), esc(m3)
    sections_html = []
    for i, st in enumerate(section_titles[:5]):
        body = section_body_from_focus(focus, st, template_id, section_index=i)
        sections_html.append(f'<h2>{i+1}. {st}</h2><p>{body}</p>')
    checklist_items = "\n".join(f"<li>{c}</li>" for c in checklist_generic(template_id))
    badge_spans = '<span className="bg-red-100 text-red-800 text-xs px-3 py-1 rounded-full font-bold tracking-wide uppercase font-display">AIガバナンス</span>\n                                <span className="bg-slate-100 text-slate-600 text-xs px-3 py-1 rounded-full font-bold tracking-wide">実装・証跡</span>'
    content = f'''
        const BlogArticle = () => (
            <main className="pt-24 pb-16">
                <article className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-100">
                        <header className="text-center mb-12 border-b border-slate-100 pb-10">
                            <div className="flex justify-center flex-wrap gap-2 mb-4">
                                {badge_spans}
                            </div>
                            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-6 leading-tight">{title}</h1>
                            <div className="flex items-center justify-center space-x-4 text-sm text-slate-500">
                                <time dateTime="2026-02-09">2026.02.09</time><span>&middot;</span>
                                <span className="flex items-center gap-1"><Icon name="User" size={{14}} /> RISEby Editorial Team</span>
                            </div>
                        </header>
                        <div className="prose prose-lg prose-slate prose-headings:font-bold prose-a:text-brand-blue hover:prose-a:text-blue-500 mx-auto">
                                <p className="lead text-xl text-slate-600 mb-10 leading-relaxed font-medium">{lead}</p>
                                {sections_html[0] if sections_html else ""}
                                <div className="not-prose my-8"><MermaidDiagram chart={{`{m1_esc}`}} /></div>
                                {sections_html[1] if len(sections_html) > 1 else ""}
                                <div className="not-prose my-8"><MermaidDiagram chart={{`{m2_esc}`}} /></div>
                                {"".join(sections_html[2:])}
                                <div className="not-prose my-8"><MermaidDiagram chart={{`{m3_esc}`}} /></div>
                                <div className="my-8 bg-blue-50 border-l-4 border-brand-blue p-6 rounded-r-lg not-prose">
                                    <h5 className="font-bold text-brand-blue mb-2 flex items-center gap-2"><Icon name="Lightbulb" size={20} />要点</h5>
                                    <div className="text-slate-700 text-base leading-relaxed">この記事の焦点は運用・証跡・監査可能性である。明日からRACIの確認、申請フローの文書化、証跡の保全のいずれかに着手できる。</div>
                                </div>
                                <h2>すぐ使えるチェックリスト</h2>
                                <ul className="list-disc pl-6 space-y-2">
                                {checklist_items}
                                </ul>
                                <h2>参考・参照</h2>
                                <ul className="list-disc pl-6 space-y-2 text-slate-700">
                                    <li><a href="https://www.nist.gov/itl/ai-risk-management-framework" target="_blank" rel="noopener noreferrer" className="text-brand-blue hover:underline">NIST AI RMF</a></li>
                                    <li><a href="https://www.iso.org/standard/42001" target="_blank" rel="noopener noreferrer" className="text-brand-blue hover:underline">ISO/IEC 42001（AIMS）</a></li>
                                    <li><a href="https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf" target="_blank" rel="noopener noreferrer" className="text-brand-blue hover:underline">AI事業者ガイドライン（経済産業省）</a></li>
                                </ul>
                                <h2>次の一歩</h2>
                                <p>明日からできること：自部門のAI利用申請の承認者が誰か確認する。証跡の保管場所と保持期間を一覧化する。四半期の棚卸日をカレンダーに登録する。</p>
                        </div>
                        <div className="not-prose mt-20 p-10 bg-slate-900 rounded-2xl text-center relative overflow-hidden">
                            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-brand-blue to-cyan-500"></div>
                            <h3 className="text-2xl font-bold text-white mb-4">AIガバナンスの設計・実装支援</h3>
                            <p className="text-slate-300 mb-8 max-w-2xl mx-auto text-sm leading-relaxed">利用規程の設計から評価・透明性・監査証跡まで、範囲を決めたうえで支援します。</p>
                            <a href="mailto:contact@riseby.net" className="inline-flex items-center justify-center gap-2 bg-brand-blue text-white px-8 py-3 rounded-full font-bold hover:bg-white hover:text-brand-blue transition-all"><Icon name="Mail" size={18} /> お問い合わせ</a>
                        </div>
                    </div>
                </article>
            </main>
        );
'''
    head = SHARED_HEAD.replace("__SLUG__", slug).replace("__TITLE__", title).replace("__DESCRIPTION__", description)
    return head + content + SHARED_TAIL


SHARED_HEAD = r'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="canonical" href="https://riseby.net/blog/ai-governance/__SLUG__.html">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="RISEby inc.">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="https://riseby.net/blog/ai-governance/__SLUG__.html">
    <meta property="og:title" content="__TITLE__ | RISEby Blog">
    <meta property="og:description" content="__DESCRIPTION__">
    <meta property="og:image" content="https://riseby.net/assets/images/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <title>__TITLE__ | RISEby Blog</title>
    <meta name="description" content="__DESCRIPTION__">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>tailwind.config = { theme: { extend: { colors: { brand: { blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' } }, fontFamily: { sans: ['"Noto Sans JP"', 'sans-serif'], display: ['"Montserrat"', 'sans-serif'] } } } }</script>
    <style>body { font-family: "Noto Sans JP", sans-serif; }
    .mermaid { display: flex; justify-content: center; margin: 2rem 0; background: #f8fafc; padding: 1rem; border-radius: 0.5rem; }
    .mermaid svg { max-width: 100%; }
    .mermaid .nodeLabel, .mermaid .edgeLabel { font-size: 1.125rem !important; }</style>
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"__TITLE__","datePublished":"2026-02-09","author":{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net"}}</script>
</head>
<body class="bg-slate-50 text-slate-800">
    <div id="root"></div>
    <script type="text/babel">
        const { useState, useEffect } = React;
        const Icon = ({ name, size = 24, className = "" }) => {
            if (typeof lucide !== 'undefined' && lucide.icons && lucide.icons[name])
                return React.createElement('svg', { xmlns: "http://www.w3.org/2000/svg", width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 2, strokeLinecap: "round", strokeLinejoin: "round", className }, lucide.icons[name].map(([tag, attrs], i) => React.createElement(tag, { ...attrs, key: i })));
            return <span className="inline-block w-4 h-4 bg-gray-300 rounded-full"></span>;
        };
        const Header = () => {
            const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
            const [scrolled, setScrolled] = useState(false);
            useEffect(() => { const h = () => setScrolled(window.scrollY > 20); window.addEventListener('scroll', h); return () => window.removeEventListener('scroll', h); }, []);
            return (
                <header className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${scrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-white/80 backdrop-blur-sm py-4 shadow-sm'}`}>
                    <div className="container mx-auto px-4 flex items-center justify-between max-w-7xl">
                        <a href="../../index.html" className="flex items-center gap-3 hover:opacity-80"><img src="../../assets/images/logo.svg" alt="RISEby" className="h-8 md:h-9" /></a>
                        <nav className="hidden md:flex items-center gap-8">
                            <a href="../../index.html#services" className="font-bold tracking-wide hover:opacity-70 text-slate-800">サービス</a>
                            <a href="../index.html" className="font-bold tracking-wide text-slate-800">ブログ</a>
                            <a href="../../about.html" className="font-bold tracking-wide hover:opacity-70 text-slate-800">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white hover:bg-slate-800 px-6 py-2.5 rounded-full font-bold">お問い合わせ</a>
                        </nav>
                        <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="md:hidden p-2 text-slate-800"><Icon name={mobileMenuOpen ? "X" : "Menu"} size={24} /></button>
                    </div>
                    {mobileMenuOpen && (
                        <div className="md:hidden absolute top-full left-0 right-0 bg-white border-t shadow-xl p-4 flex flex-col gap-4">
                            <a href="../../index.html#services" className="text-slate-800 font-bold py-3 border-b border-slate-50">サービス</a>
                            <a href="../index.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">ブログ</a>
                            <a href="../../about.html" className="text-slate-800 font-bold py-3 border-b border-slate-50">会社概要</a>
                            <a href="mailto:contact@riseby.net" className="bg-brand-blue text-white text-center py-3.5 rounded-lg font-bold mt-2">お問い合わせ</a>
                        </div>
                    )}
                </header>
            );
        };
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
                                <a href="mailto:contact@riseby.net" className="hover:text-white flex items-center gap-2 mt-6 group"><span className="bg-slate-800 p-2 rounded-full group-hover:bg-slate-700"><Icon name="Mail" size={16} /></span>contact@riseby.net</a>
                            </div>
                            <p className="text-slate-600 text-xs">&copy; {new Date().getFullYear()} RISEby Inc.</p>
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
        const MermaidDiagram = ({ chart }) => {
            useEffect(() => { if (typeof mermaid !== 'undefined') { mermaid.initialize({ theme: 'base', themeVariables: { fontSize: '18px', primaryTextColor: '#334155' } }); mermaid.init(); } }, []);
            return <div className="mermaid overflow-x-auto max-w-4xl mx-auto text-lg">{chart}</div>;
        };
'''

SHARED_TAIL = r'''
        const App = () => <div className="min-h-screen flex flex-col font-sans bg-slate-50 text-slate-800"><Header /><BlogArticle /><Footer /></div>;
        const root = ReactDOM.createRoot(document.getElementById("root"));
        root.render(<App />);
    </script>
</body>
</html>
'''


def _html_esc(s):
    """HTMLエスケープ（属性・本文用）。"""
    if not s:
        return ""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def strip_title_from_summary(summary, title_ja):
    """カード要約ルール: タイトルと同一の文言を要約に表示しない。要約の先頭がタイトルと一致する場合はその部分を除く。"""
    if not summary or not title_ja:
        return summary or ""
    s = summary.strip()
    t = title_ja.strip()
    if not t or not s.startswith(t):
        return s
    rest = s[len(t):].lstrip("。、 ")
    return rest if rest else s


def get_article_description(slug):
    """記事HTMLから meta name=\"description\" の content を取得。無ければ None。"""
    path = OUT_DIR / (slug + ".html")
    if not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8")
        m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', text)
        if m:
            return m.group(1).strip()
        m = re.search(r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']description["\']', text)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return None


def build_index_html(articles):
    """カテゴリトップ index.html を組み立てる。サブカテゴリはアコーディオン、カードはAIカテゴリデザイン・記事要約表示。SEO対応。"""
    section_order = "ABCDEFGHIJKL"
    section_titles = {
        "A": "Governance OS（統治OS）",
        "B": "Risk & Assurance（リスクと保証）",
        "C": "Lifecycle & Control（ライフサイクル統制）",
        "D": "Evidence & Auditability（証跡と監査可能性）",
        "E": "Security（AIセキュリティ）",
        "F": "Privacy & Data Governance",
        "G": "Legal & Content Integrity",
        "H": "Regulation & Standards",
        "I": "Procurement & Third-Party",
        "J": "Operations & Monitoring",
        "K": "Incident & Resilience",
        "L": "Industry Packs",
    }
    # 存在するHTMLのみ表示（削除済み記事へのリンクを防ぐ）
    existing_slugs = {p.stem for p in OUT_DIR.glob("*.html") if p.name != "index.html"}
    by_section = {s: [] for s in section_order}
    for a in articles:
        if a["slug"] not in existing_slugs:
            continue
        sec = TEMPLATE_TO_SECTION.get(a["template_id"], "A")
        by_section.setdefault(sec, []).append(a)

    # サブカテゴリごとにアコーディオン＋カード（記事要約は各HTMLのmeta descriptionから取得）
    sections_html = []
    for idx, sec in enumerate(section_order):
        items = by_section.get(sec) or []
        if not items:
            continue
        title = section_titles.get(sec, sec)
        cards = []
        for a in items:
            summary = get_article_description(a["slug"])
            if not summary:
                focus_short = (a.get("unique_focus") or "").replace("に特化", "").strip("「」\"'\u201c\u201d")[:80]
                summary = focus_short if focus_short else "運用・証跡・監査可能性に落とすための要件を整理する。"
            # ルール: カードの要約に記事タイトルと同一の文言を表示しない（先頭一致時は除く）
            summary = strip_title_from_summary(summary, a["title_ja"])
            summary_esc = _html_esc(summary)
            title_esc = _html_esc(a["title_ja"])
            # AIカテゴリ同様: navy, gray-900/gray-600, p-6, text-lg, line-clamp-3
            cards.append(
                f'<a href="{a["slug"]}.html" class="group bg-white rounded-xl shadow-md hover:shadow-lg transition-all overflow-hidden">'
                f'<div class="p-6"><span class="text-xs text-navy font-medium">{sec}</span>'
                f'<h3 class="text-lg font-bold text-gray-900 mt-2 group-hover:text-navy transition">{title_esc}</h3>'
                f'<p class="text-gray-600 text-sm mt-3 line-clamp-3">{summary_esc}</p></div></a>'
            )
        grid = "\n          ".join(cards)
        is_first = len(sections_html) == 0
        open_attr = " open" if is_first else ""
        sections_html.append(
            f'<div class="accordion-item border-b border-gray-200" data-accordion-sec="{sec}">'
            f'<button type="button" class="accordion-trigger w-full text-left py-5 flex items-center justify-between gap-4 font-bold text-lg text-gray-900 hover:text-navy transition focus:outline-none focus:ring-2 focus:ring-navy/30 rounded" aria-expanded="{"true" if is_first else "false"}" aria-controls="panel-{sec}" id="trigger-{sec}" data-sec="{sec}">'
            f'<span id="heading-{sec}">{sec}. {_html_esc(title)}</span>'
            f'<svg class="accordion-chevron w-5 h-5 flex-shrink-0 text-navy transition-transform duration-200" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>'
            f'</button>'
            f'<div id="panel-{sec}" class="accordion-panel overflow-hidden" role="region" aria-labelledby="trigger-{sec}" style="display:{"block" if is_first else "none"}">'
            f'<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 pb-8">{grid}</div></div></div>'
        )
    categories_html = "\n                ".join(sections_html)

    roadmap_articles = [a for a in articles[:12] if a["slug"] in existing_slugs]
    roadmap_html = "\n                    ".join(
        f'<li><a href="{a["slug"]}.html" class="text-brand-blue hover:underline">Week {(i+1)}: {_html_esc(a["title_ja"])}</a></li>'
        for i, a in enumerate(roadmap_articles)
    )

    article_count = sum(len(by_section.get(s, [])) for s in section_order)
    index_content = f'''<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIガバナンス | RISEby Blog</title>
    <meta name="description" content="AIガバナンスカテゴリ。運用・証跡・監査可能性に落とすための記事一覧と読む順（90日）ロードマップ。サブカテゴリ別に全記事をカードで表示。">
    <meta name="keywords" content="AIガバナンス,AI倫理,リスク管理,監査,証跡,EU AI Act,NIST,ISO 42001,生成AIガバナンス">
    <link rel="canonical" href="https://riseby.net/blog/ai-governance/index.html">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="RISEby inc.">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="https://riseby.net/blog/ai-governance/index.html">
    <meta property="og:title" content="AIガバナンス | RISEby Blog">
    <meta property="og:description" content="AIガバナンスカテゴリ。運用・証跡・監査可能性に落とすための記事一覧と読む順（90日）ロードマップ。">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">
{{"@context":"https://schema.org","@type":"CollectionPage","name":"AIガバナンス記事一覧","description":"AIガバナンスに関する記事一覧。サブカテゴリ別に全記事を表示。","url":"https://riseby.net/blog/ai-governance/index.html","isPartOf":{{"@type":"Blog","name":"RISEby Blog","url":"https://riseby.net/blog/"}}}}
    </script>
    <script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"ホーム","item":"https://riseby.net/"}},{{"@type":"ListItem","position":2,"name":"ブログ","item":"https://riseby.net/blog/"}},{{"@type":"ListItem","position":3,"name":"AIガバナンス","item":"https://riseby.net/blog/ai-governance/index.html"}}]}}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script>tailwind.config = {{ theme: {{ extend: {{ colors: {{ brand: {{ blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' }}, navy: {{ DEFAULT: '#003E68', light: '#004D82', dark: '#00314F' }} }}, fontFamily: {{ sans: ['"Noto Sans JP"', 'sans-serif'], display: ['"Montserrat"', 'sans-serif'] }} }} }} }}</script>
    <style>body {{ font-family: "Noto Sans JP", sans-serif; }}
    .mermaid {{ display: flex; justify-content: center; margin: 2rem 0; background: #f8fafc; padding: 1rem; border-radius: 0.5rem; }}
    .line-clamp-3 {{ display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}</style>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</head>
<body class="bg-gray-50 text-gray-800">
    <header class="bg-white/95 backdrop-blur-sm border-b border-gray-100 fixed top-0 left-0 right-0 z-50">
        <nav class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
            <a href="../../index.html" class="flex items-center gap-3"><img src="../../assets/images/logo.svg" alt="RISEby" class="h-8 md:h-9" /></a>
            <div class="flex items-center gap-4">
                <a href="../index.html" class="text-gray-600 hover:text-navy transition">ブログ一覧</a>
                <a href="mailto:contact@riseby.net" class="hidden md:inline-flex items-center px-5 py-2 bg-navy text-white rounded-full text-sm font-medium hover:bg-navy-light transition">お問い合わせ</a>
            </div>
        </div>
        </nav>
    </header>
    <main class="pt-24 pb-16 min-h-screen">
        <div class="max-w-7xl mx-auto px-6">
            <div class="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-gray-100">
                <nav class="text-sm text-slate-500 mb-4" aria-label="パンくず">
                    <a href="../../index.html" class="hover:text-brand-blue">ホーム</a>
                    <span class="mx-2">/</span>
                    <a href="../index.html" class="hover:text-brand-blue">ブログ</a>
                    <span class="mx-2">/</span>
                    <span class="text-slate-700">AIガバナンス</span>
                </nav>
                <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-4">AIガバナンス</h1>
                <p class="text-slate-600 mb-8">サブカテゴリ別に全{article_count}記事を掲載。運用視点の最小要件と読む順（90日）ロードマップをまとめています。</p>
                <div class="my-8 p-6 bg-slate-50 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-slate-900 mb-4">運用の最小要件（1枚図）</h3>
                    <div class="mermaid">graph TD
  RACI[RACI] --> FLOW[申請-審査-例外-更新]
  FLOW --> EVD[証跡]
  EVD --> EVAL[継続評価]
  EVAL --> INC[インシデント]
  style RACI fill:#e0f2fe
  style EVD fill:#dcfce7
  style INC fill:#fef9c3</div>
                    <p class="text-xs text-slate-500 mt-2">注：組織の規模・規制に応じて範囲は調整してください。</p>
                </div>
                <h2 class="text-xl font-bold text-slate-900 mt-12 mb-4">読むべき順（90日ロードマップ）</h2>
                <p class="text-slate-600 mb-2">週1本のペースで進める場合の推奨順です。</p>
                <ul class="list-disc pl-6 space-y-2 mb-12">
                    {roadmap_html}
                </ul>
                <h2 class="text-xl font-bold text-gray-900 mb-2">サブカテゴリ別記事一覧</h2>
                <p class="text-gray-600 text-sm mb-8">サブカテゴリ名をクリックすると開閉します。開いたカテゴリ内の記事はカード形式で一覧でき、タイトル下に記事の要約を表示しています。</p>
                {categories_html}
                <div class="mt-12 p-8 bg-slate-900 rounded-2xl text-center text-white">
                    <h3 class="text-xl font-bold mb-4">AIガバナンスの設計・実装支援</h3>
                    <p class="text-slate-300 text-sm mb-6">利用規程の設計から評価・透明性・監査証跡まで、範囲を決めたうえで支援します。</p>
                    <a href="mailto:contact@riseby.net" class="inline-flex items-center gap-2 bg-brand-blue text-white px-8 py-3 rounded-full font-bold hover:bg-white hover:text-brand-blue transition-all">お問い合わせ</a>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-[#0B0F19] text-white pt-16 pb-8 mt-24">
        <div class="container mx-auto px-4 max-w-7xl text-center text-sm text-slate-400">
            <p>&copy; 2026 RISEby Inc.</p>
        </div>
    </footer>
    <script>mermaid.initialize({{ startOnLoad: true, theme: 'base' }});</script>
    <script>
(function() {{
  var triggers = document.querySelectorAll('.accordion-trigger');
  var panels = document.querySelectorAll('.accordion-panel');
  triggers.forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var sec = this.getAttribute('data-sec');
      var openPanel = document.getElementById('panel-' + sec);
      panels.forEach(function(p) {{ p.style.display = 'none'; }});
      triggers.forEach(function(t) {{ t.setAttribute('aria-expanded', 'false'); t.querySelector('.accordion-chevron').style.transform = ''; }});
      openPanel.style.display = 'block';
      this.setAttribute('aria-expanded', 'true');
      this.querySelector('.accordion-chevron').style.transform = 'rotate(180deg)';
    }});
  }});
  var firstTrigger = document.querySelector('.accordion-trigger[aria-expanded="true"]');
  if (firstTrigger && firstTrigger.querySelector('.accordion-chevron')) firstTrigger.querySelector('.accordion-chevron').style.transform = 'rotate(180deg)';
}})();
    </script>
</body>
</html>
'''
    return index_content


def main():
    """AIガバナンスカテゴリの index.html のみ生成する。記事HTMLは gen_llm_out_31_163.py + apply_llm_article.py で統一生成すること。"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    articles = parse_design()
    if len(articles) < 163:
        print(f"WARNING: parsed {len(articles)} articles, expected 163")
    index_html = build_index_html(articles)
    (OUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print("Wrote", OUT_DIR / "index.html")
    print("Done. Index only. For articles 1-163 use: python scripts/gen_llm_out_31_163.py then apply_llm_article.py 1..163.")


if __name__ == "__main__":
    main()
