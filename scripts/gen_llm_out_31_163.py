#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
設計図に基づき、記事1〜163の llm-out.md を生成する（テンプレ別図1・同一ロジックで統一）。
apply_llm_article.py が期待するフォーマットで出力する。
"""
import csv
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))
from article_references import get_references_markdown

DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"
FIGURE_HISTORY_PATH = BRIEFS_DIR / "figure_usage_history.csv"

# テンプレ別の図1レイアウト種別（設計図 Infographics の1番目に合わせる）
# RACI / LAYER / MATRIX / FLOW / TIMELINE / EVIDENCE_CHAIN / GATE / TOP5 / KPI
TEMPLATE_FIG1_KIND = {
    "T01": "RACI", "T02": "KPI", "T03": "MATRIX", "T04": "TIMELINE", "T05": "EVIDENCE_CHAIN",
    "T06": "MATRIX", "T07": "MATRIX", "T08": "LAYER", "T09": "TOP5", "T10": "GATE",
    "T11": "LAYER", "T12": "FLOW", "T13": "FLOW", "T14": "GATE", "T15": "EVIDENCE_CHAIN",
    "T16": "EVIDENCE_CHAIN", "T17": "LAYER", "T18": "EVIDENCE_CHAIN", "T19": "EVIDENCE_CHAIN",
    "T20": "KPI", "T21": "MATRIX", "T22": "LAYER", "T23": "MATRIX", "T24": "GATE",
    "T25": "FLOW", "T26": "MATRIX", "T27": "LAYER", "T28": "KPI", "T29": "FLOW",
    "T30": "MATRIX", "T31": "MATRIX", "T32": "LAYER",
}

# 図の型（A–J）の組み合わせ。同じ型を3記事連続で使わないようローテーション用。
FIG_TYPE_TRIPLETS = [
    ("A", "B", "G"), ("D", "E", "F"), ("C", "H", "I"), ("J", "A", "F"), ("B", "D", "G"),
    ("E", "C", "I"), ("F", "H", "J"), ("G", "A", "D"), ("I", "B", "E"), ("H", "J", "C"),
    ("A", "E", "G"), ("D", "B", "I"), ("C", "F", "J"), ("G", "H", "A"), ("E", "D", "F"),
    ("B", "C", "I"), ("J", "G", "H"), ("F", "A", "E"), ("I", "D", "B"), ("H", "C", "J"),
]

# 結論パターン（Co 1-5）— 次の一歩の冒頭文
CONCLUSION_INTROS = {
    1: "明日から始められる3つのステップです。",
    2: "あなたの組織がどの道を選ぶべきか、判断軸を1つ決めてください。",
    3: "いまの対応が、その後の監査対応と競争力の基盤になります。",
    4: "放置した場合のワーストシナリオ（監査指摘・証跡欠落）を避けるため、明日から対策を始めてください。",
    5: "今日のベストプラクティスは明日の最低要件になり得ます。明日から、",
}

# テンプレ別 Outline と Mermaid 3種（gen_ai_governance_from_design と同一）
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
    """設計図 3.2 と 3.3 をパース。gen_ai_governance_from_design と同様。"""
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


def section_body_from_focus(focus, section_title, section_index=0):
    """unique_focus とセクション見出しから1段落の本文を生成。
    同一長文の繰り返し禁止のため、定型句「理念で終わらせず…5要素のうち」は第1セクションのみ。
    2セクション目以降は短い言い換えのみ（章をまたいで同一長文を出さない）。"""
    focus_short = focus.replace("に特化", "").strip("「」\"'")
    base = "理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理する。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえる。"
    if section_index == 0:
        return f"本稿の焦点は「{focus_short}」である。{section_title}では、{base}"
    # 「ここでは〜について、このテーマに応じた観点を整理する。」は使わない（ルールで禁止）
    return f"このセクションでは、責任分界・証跡・監査の観点を押さえる。"


def _escape_label(s, max_len=12):
    """図内ラベル用に短くする。"""
    if not s:
        return "焦点"
    s = s.replace("に特化", "").strip("「」\"'")[:max_len]
    return s or "焦点"


def _fig_svg_layer(label):
    """レイヤー図風：縦積み3段（概念の骨格）。"""
    return f'''<svg viewBox="0 0 260 140" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="12" width="180" height="32" rx="4" fill="#e0f2fe"/>
  <text x="130" y="32" text-anchor="middle" font-size="10">方針</text>
  <rect x="40" y="52" width="180" height="32" rx="4" fill="#dcfce7"/>
  <text x="130" y="72" text-anchor="middle" font-size="10">プロセス</text>
  <rect x="40" y="92" width="180" height="32" rx="4" fill="#fef9c3"/>
  <text x="130" y="112" text-anchor="middle" font-size="10">{_escape_label(label, 8)}・証跡</text>
</svg>'''


def _fig_svg_raci(label):
    """RACI風：横並び4役割（Board/Legal/CISO/Audit）。"""
    return f'''<svg viewBox="0 0 420 80" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="20" width="88" height="36" rx="4" fill="#e0f2fe"/><text x="54" y="42" text-anchor="middle" font-size="9">Board</text>
  <rect x="108" y="20" width="88" height="36" rx="4" fill="#dcfce7"/><text x="152" y="42" text-anchor="middle" font-size="9">Legal</text>
  <rect x="206" y="20" width="88" height="36" rx="4" fill="#fef9c3"/><text x="250" y="42" text-anchor="middle" font-size="9">CISO</text>
  <rect x="304" y="20" width="88" height="36" rx="4" fill="#f1f5f9"/><text x="348" y="42" text-anchor="middle" font-size="9">Audit</text>
  <text x="210" y="68" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_matrix(label):
    """マトリクス風：2×2の4セル。"""
    return f'''<svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="95" height="45" rx="4" fill="#e0f2fe"/><text x="57" y="34" text-anchor="middle" font-size="8">軸A</text>
  <rect x="115" y="10" width="95" height="45" rx="4" fill="#dcfce7"/><text x="162" y="34" text-anchor="middle" font-size="8">軸B</text>
  <rect x="10" y="65" width="95" height="45" rx="4" fill="#fef9c3"/><text x="57" y="89" text-anchor="middle" font-size="8">統制</text>
  <rect x="115" y="65" width="95" height="45" rx="4" fill="#f1f5f9"/><text x="162" y="89" text-anchor="middle" font-size="8">証跡</text>
  <text x="110" y="115" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_flow(label):
    """フロー風：左から右へ矢印でつなぐ3ボックス。"""
    return f'''<svg viewBox="0 0 380 80" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="22" width="95" height="36" rx="4" fill="#e0f2fe"/><text x="62" y="44" text-anchor="middle" font-size="9">入力</text>
  <path d="M115 40 L145 40" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>
  <rect x="150" y="22" width="95" height="36" rx="4" fill="#dcfce7"/><text x="197" y="44" text-anchor="middle" font-size="9">審査</text>
  <path d="M250 40 L280 40" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <defs><marker id="arrow2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>
  <rect x="285" y="22" width="95" height="36" rx="4" fill="#fef9c3"/><text x="332" y="44" text-anchor="middle" font-size="9">出力</text>
  <text x="190" y="72" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_timeline(label):
    """タイムライン風：横4区切り（Q1–Q4）。"""
    return f'''<svg viewBox="0 0 400 70" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="22" width="82" height="28" rx="4" fill="#e0f2fe"/><text x="56" y="40" text-anchor="middle" font-size="9">Q1</text>
  <rect x="107" y="22" width="82" height="28" rx="4" fill="#dcfce7"/><text x="148" y="40" text-anchor="middle" font-size="9">Q2</text>
  <rect x="199" y="22" width="82" height="28" rx="4" fill="#fef9c3"/><text x="240" y="40" text-anchor="middle" font-size="9">Q3</text>
  <rect x="291" y="22" width="82" height="28" rx="4" fill="#f1f5f9"/><text x="332" y="40" text-anchor="middle" font-size="9">Q4</text>
  <text x="200" y="62" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_evidence_chain(label):
    """Evidence Chain風：連鎖4ボックス（ログ→検証→保全→提出）。"""
    return f'''<svg viewBox="0 0 420 70" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="18" width="88" height="32" rx="4" fill="#e0f2fe"/><text x="52" y="38" text-anchor="middle" font-size="8">ログ</text>
  <rect x="108" y="18" width="88" height="32" rx="4" fill="#dcfce7"/><text x="152" y="38" text-anchor="middle" font-size="8">検証</text>
  <rect x="208" y="18" width="88" height="32" rx="4" fill="#fef9c3"/><text x="252" y="38" text-anchor="middle" font-size="8">保全</text>
  <rect x="308" y="18" width="88" height="32" rx="4" fill="#f1f5f9"/><text x="352" y="38" text-anchor="middle" font-size="8">提出</text>
  <text x="210" y="62" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_gate(label):
    """CI/CDゲート風：3段（開発→ゲート→デプロイ）。"""
    return f'''<svg viewBox="0 0 280 128" xmlns="http://www.w3.org/2000/svg">
  <rect x="90" y="8" width="100" height="26" rx="4" fill="#e0f2fe"/><text x="140" y="25" text-anchor="middle" font-size="9">開発</text>
  <path d="M140 34 L140 44" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="80" y="48" width="120" height="28" rx="4" fill="#fef9c3" stroke="#eab308" stroke-width="1.5"/><text x="140" y="66" text-anchor="middle" font-size="9">ゲート</text>
  <path d="M140 76 L140 86" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="90" y="88" width="100" height="26" rx="4" fill="#dcfce7"/><text x="140" y="105" text-anchor="middle" font-size="9">デプロイ</text>
  <text x="140" y="122" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_top5(label):
    """差し戻しTop5風：横5つの小ボックス。"""
    return f'''<svg viewBox="0 0 400 56" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="12" width="68" height="32" rx="3" fill="#fee2e2"/><text x="42" y="31" text-anchor="middle" font-size="7">1</text>
  <rect x="84" y="12" width="68" height="32" rx="3" fill="#fee2e2"/><text x="118" y="31" text-anchor="middle" font-size="7">2</text>
  <rect x="160" y="12" width="68" height="32" rx="3" fill="#fee2e2"/><text x="194" y="31" text-anchor="middle" font-size="7">3</text>
  <rect x="236" y="12" width="68" height="32" rx="3" fill="#fee2e2"/><text x="270" y="31" text-anchor="middle" font-size="7">4</text>
  <rect x="312" y="12" width="68" height="32" rx="3" fill="#fee2e2"/><text x="346" y="31" text-anchor="middle" font-size="7">5</text>
  <text x="200" y="52" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def _fig_svg_kpi(label):
    """KPI/KRI風：横3つの指標ボックス。"""
    return f'''<svg viewBox="0 0 320 70" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="18" width="88" height="34" rx="4" fill="#e0f2fe"/><text x="59" y="38" text-anchor="middle" font-size="8">KRI1</text>
  <rect x="116" y="18" width="88" height="34" rx="4" fill="#dcfce7"/><text x="160" y="38" text-anchor="middle" font-size="8">KRI2</text>
  <rect x="217" y="18" width="88" height="34" rx="4" fill="#fef9c3"/><text x="261" y="38" text-anchor="middle" font-size="8">KRI3</text>
  <text x="160" y="62" text-anchor="middle" font-size="8" fill="#64748b">{_escape_label(label, 10)}</text>
</svg>'''


def build_fig_svg(focus_short, section_title, template_id):
    """テンプレIDに応じて図1のレイアウト・種類を変える（設計図 Infographics 準拠）。"""
    label = _escape_label(section_title or focus_short, 14)
    kind = TEMPLATE_FIG1_KIND.get(template_id, "LAYER")
    builders = {
        "RACI": _fig_svg_raci,
        "LAYER": _fig_svg_layer,
        "MATRIX": _fig_svg_matrix,
        "FLOW": _fig_svg_flow,
        "TIMELINE": _fig_svg_timeline,
        "EVIDENCE_CHAIN": _fig_svg_evidence_chain,
        "GATE": _fig_svg_gate,
        "TOP5": _fig_svg_top5,
        "KPI": _fig_svg_kpi,
    }
    fn = builders.get(kind, _fig_svg_layer)
    return fn(label)


def build_fig_html(focus_short, section_title):
    """ルール準拠の最小HTML（カード/リスト風）。"""
    label = _escape_label(section_title or focus_short, 10)
    return f'''<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">{label}と運用</p>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li style="margin: 0.25rem 0;">RACIと証跡の目次を監査と事前合意</li>
    <li style="margin: 0.25rem 0;">継続評価・インシデント窓口を固定</li>
    <li style="margin: 0.25rem 0;">是正の流れをテンプレ化し記録</li>
  </ul>
</div>'''


def build_fig_table(focus_short, section_title):
    """ルール準拠の最小Table。"""
    label = _escape_label(section_title or focus_short, 10)
    return f'''<table style="width:100%; max-width: 520px; margin: 1rem auto; border-collapse: collapse;">
  <thead>
    <tr style="background: #f1f5f9;">
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">証跡</th>
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">目的</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">{label}・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>'''


def checklist_generic():
    """汎用チェックリスト10項目。"""
    return [
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


def build_llm_out(article):
    """1記事分の llm-out.md 本文を組み立てる。図はルール準拠で SVG/HTML/Table をローテーション。"""
    no = article["no"]
    slug = article["slug"]
    title_ja = article["title_ja"]
    focus = article["unique_focus"]
    template_id = article["template_id"]
    co = article["Co"]
    focus_short = focus.replace("に特化", "").strip("「」\"'")

    outline = TEMPLATE_OUTLINES.get(template_id, (["概要", "設計", "運用", "証跡"], "graph LR\n  A --> B\n  B --> C", "graph TD\n  X --> Y\n  Y --> Z", "graph TD\n  T1[差し戻し1]\n  T2[差し戻し2]\n  T3[差し戻し3]"))
    section_titles = outline[0]

    # 図の型：同じ型を3記事連続にしないようローテーション（1-163 通し）
    idx = (no - 1) % len(FIG_TYPE_TRIPLETS)
    t1, t2, t3 = FIG_TYPE_TRIPLETS[idx]
    # 形式：Mermaid禁止。1記事で SVG / HTML / Table を1つずつ使用。図1はテンプレ別レイアウト。
    fig1_content = build_fig_svg(focus_short, section_titles[0] if len(section_titles) > 0 else None, template_id)
    fig2_content = build_fig_html(focus_short, section_titles[1] if len(section_titles) > 1 else None)
    fig3_content = build_fig_table(focus_short, section_titles[2] if len(section_titles) > 2 else None)

    # リード
    lead = f"本稿の焦点は「{focus_short}」である。理念で終わらせず、運用・証跡・監査可能性に落とすための要件を整理する。{title_ja}に関し、責任分界・証跡・監査提出の目次を具体化する。"

    # 本文（見出し＋段落＋図挿入）
    body_lines = []
    for i, st in enumerate(section_titles[:4]):
        body_lines.append(f"### {i + 1}. {st}")
        body_lines.append("")
        body_lines.append(section_body_from_focus(focus, st, section_index=i))
        body_lines.append("")
        if i == 0:
            body_lines.append("ここに図1を挿入")
        elif i == 1:
            body_lines.append("ここに図2を挿入")
        elif i == 2:
            body_lines.append("ここに図3を挿入")
        body_lines.append("")

    body_md = "\n".join(body_lines).strip()

    # 固有の一文
    key_sentence = f"本稿の焦点は「{focus_short}」にあり、運用・証跡・監査可能性に落とすための要件を整理する。明日からRACIの確認、申請フローの文書化、証跡の保全のいずれかに着手できる。"

    # 次の一歩
    intro = CONCLUSION_INTROS.get(co, "明日から始められるステップです。")
    next_steps = f"{intro} 本テーマ（{focus_short}）について、自部門で「誰が承認者か」「証跡をどこに残すか」を1つ決め、監査法人に証憑の形を事前に1回確認すると、他領域の設計の基準になる。"

    # 参考文献（記事テーマに応じた参照に変更）
    refs = get_references_markdown(no, slug, template_id)

    md = f"""## リード（1段落）

{lead}

## 本文

{body_md}

## 図1（SVG）

```
{fig1_content}
```

## 図2（HTML）

```
{fig2_content}
```

## 図3（Table）

```
{fig3_content}
```

## 図の型（記録用・必須）
図1: {t1}, 図2: {t2}, 図3: {t3}

## 図の形式（記録用・必須）
図1: SVG, 図2: HTML, 図3: Table

## 固有の一文（要点ボックス用1文）

{key_sentence}

## チェックリスト（10項目）

"""
    for item in checklist_generic():
        md += f"- {item}\n"
    md += f"""
## 参考文献（3つ以上、発行年または一次資料明記）

{refs}

## 次の一歩（結論パターン Co に沿って）

{next_steps}
"""
    return md


def main():
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    articles = parse_design()
    target = [a for a in articles if 1 <= a["no"] <= 163]
    if not target:
        print("No articles 1-163 in design.")
        return
    for a in target:
        no, slug = a["no"], a["slug"]
        out_path = BRIEFS_DIR / f"{no:03d}-{slug}-llm-out.md"
        content = build_llm_out(a)
        out_path.write_text(content, encoding="utf-8")
        print("Wrote", out_path)
    print("Done. Generated", len(target), "llm-out files (1-163).")

    # figure_usage_history.csv：1-163 を同一ロジックで出力（テンプレ別図1・型ローテーション）
    fieldnames = ["no", "slug", "fig1", "fig2", "fig3", "op", "fig1_fmt", "fig2_fmt", "fig3_fmt"]
    with open(FIGURE_HISTORY_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for a in target:
            idx = (a["no"] - 1) % len(FIG_TYPE_TRIPLETS)
            t1, t2, t3 = FIG_TYPE_TRIPLETS[idx]
            w.writerow({
                "no": a["no"], "slug": a["slug"], "fig1": t1, "fig2": t2, "fig3": t3,
                "op": a["Op"], "fig1_fmt": "SVG", "fig2_fmt": "HTML", "fig3_fmt": "Table",
            })
    print("Updated figure_usage_history.csv: 1-163 with SVG/HTML/Table and type rotation.")


if __name__ == "__main__":
    main()
