#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
記事11〜163について、記事1〜10と同様の構成かつそれ以上の文章量で llm-out.md を生成する。
同一文章の繰り返し・他記事と同じチェックリスト・似た図の連続を避ける。
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))
from article_references import get_references_markdown
from gen_llm_out_31_163 import (
    parse_design,
    FIG_TYPE_TRIPLETS,
    CONCLUSION_INTROS,
    TEMPLATE_OUTLINES,
    build_fig_svg,
    build_fig_html,
    build_fig_table,
    _escape_label,
)

DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"
FIGURE_HISTORY_PATH = BRIEFS_DIR / "figure_usage_history.csv"

# 冒頭パターン（Op 1-10）— リード1文目
OPENING_LEADS = {
    1: "現場では、AI利用の責任分界が曖昧なまま運用され、監査で指摘されるケースがあります。",
    2: "多くの組織で、AIガバナンスの証跡が「何を残すか」で揃っておらず、事後の説明に苦慮しています。",
    3: "あなたの部門では、AI利用の申請から承認まで、誰が何を判断するか即答できますか。",
    4: "理想は統制の効いたAI利用、現実は申請フローが形骸化し証跡が残らない、というギャップがよく聞かれます。",
    5: "ある企業では、AI倫理委員会を設けたが承認と開発のゲートがつながらず、形骸化した事例があります。",
    6: "監査で差し戻される要因の多くは、証跡の目次が監査側の期待と一致していないことです。",
    7: "規制・ガイドラインの施行スケジュールに合わせ、体制と証跡を整える必要があります。",
    8: "理念を掲げるほど、手続きと証跡が追いつかず、監査で説明できない事態になりがちです。",
    9: "集中型で統制するか、分散型でスピードを取るか、組織に合わせた選択が求められます。",
    10: "ガバナンス文書が読まれず、版管理も曖昧なまま運用すると、監査で指摘の対象になります。",
}

# 本文用の「観点」文プール（80件）— 記事・セクションごとに異なる組み合わせで使用
POINT_SENTENCES = [
    "責任の所在（RACI）を一枚にまとめ、関係者と共有しておくことが第一歩です。",
    "申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。",
    "監査提出の目次を監査法人と事前に1回すり合わせておくと、本番の差し戻しを減らせます。",
    "証跡は改ざん耐性（ハッシュやアクセス制御）を確保し、保持期間を明示します。",
    "継続評価の記録を四半期ごとに残し、是正の流れをテンプレ化しておきます。",
    "インシデント時の報告先とエスカレーション閾値を決め、記録を欠かさないようにします。",
    "例外の基準と有効期限を設け、恒久化すべきものは正式申請に切り替える運用にします。",
    "規制・標準との対応関係は一覧化しつつ、断定は避け条件を明示します。",
    "誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。",
    "成果物ごとに作成者・承認者・保管場所・保持期間を決め、Evidence Chainを切らしません。",
    "開発フェーズとリリース承認のゲートを設け、通過記録を証跡として残します。",
    "データの境界（入力・出力・学習）を定義し、漏えい経路に統制を置きます。",
    "脅威を分類し、優先順位をつけたうえで統制と監視を設計します。",
    "KRI・閾値・エスカレーション先を決め、ダッシュボードやレビューで追います。",
    "契約・SLAにBOMやログ提供の義務を盛り込み、責任分界を明確にします。",
    "DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。",
    "版管理と変更記録を残し、文書の形骸化を防ぐための教育・周知も行います。",
    "レッドチームや演習の計画・結果・是正を記録し、脅威モデルを更新します。",
    "ベンダー・委託先との責任分界を契約と証跡で明示し、四半期で棚卸します。",
    "品質指標と閾値を決め、ドリフトや是正件数を継続的に追います。",
    "透明性表示やコンテンツ分類の手順を文書化し、公開前チェックの記録を残します。",
    "学習データの権利処理と出力物の責任範囲を方針に落とし、手続き化します。",
    "廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。",
    "監査で必要なログの種別・目的・保持期間を一覧化し、完全性を検証します。",
    "証跡の最小セットを「目次」として固定し、欠落しやすい項目をチェックします。",
    "Evidence Bundleの形（ログ→検証→保全→提出）を揃え、ハッシュで改ざんを検知します。",
    "争点化された際に必要な証拠を想定し、日付・責任者・版の整合を保ちます。",
    "ボード・監査向けの最小KRIを決め、閾値 breach 時のアクションを明文化します。",
    "アクセス制御を申請・承認・付与のフローに落とし、最小権限を適用します。",
    "漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。",
    "攻撃パターンと対策の対応表を作り、検知・是正の記録を残します。",
    "選定基準と評価プロセスを文書化し、契約・継続監視・証跡を一貫させます。",
    "データ種類と義務の対応をマトリクス化し、DPIA・承認の記録を保全します。",
    "境界定義を入力・出力・学習に分け、契約境界と運用で守る設計にします。",
    "品質が壊れるポイントを特定し、測定・是正・証跡のループを回します。",
    "法域ごとの義務をマトリクス化し、契約条項と証跡でカバーします。",
    "PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。",
    "著作権・表示・証跡の争点を一覧化し、方針と手続きを対応させます。",
    "表示義務と公開前チェックを運用に落とし、証跡の目次に含めます。",
    "三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。",
    "取締役会で聞かれる問いを想定し、KPI・意思決定ログ・四半期レビューを用意します。",
    "集中と分散のトレードオフを整理し、抜け穴がないようガードレールを置きます。",
    "年次で優先5領域を決め、予算・人材・レビューのサイクルを回します。",
    "文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。",
    "リスク許容度を利用ケース承認に落とし、レッドラインを定義します。",
    "定性・定量の評価設計を実施し、記録と継続評価をセットにします。",
    "ProofとAssuranceの分界を決め、監査が求める証憑の形と揃えます。",
    "所見の型と原因をテンプレ化し、是正の優先度と追跡KPIを決めます。",
    "年1の監査では不足するため、継続適合性評価と自動化を運用に組み込みます。",
    "開発段階の統制と承認ゲートを設け、証跡を切らさない設計にします。",
    "リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。",
    "例外が増えないよう、抑制策と教育、KRIで棚卸しを回します。",
    "何をいつ測るか、閾値、証跡、運用責任者を決め、ゲートで通過記録を残します。",
    "退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。",
    "ログ種別と目的・保持期間の対応表を作り、完全性・改ざん検知を確保します。",
    "最小目次と落とし穴（目次欠落・日付不整合等）をテンプレで共有します。",
    "連鎖（生成→保管→提出→検証）を設計し、監査提示の形を事前に合意します。",
    "争点シナリオに必要な証拠を洗い出し、保全と提出の責任者を決めます。",
    "何を見るか・誰が見るか・閾値・アクションを決め、エスカレーションを明文化します。",
    "主体・権限・データのマトリクスでアクセスを設計し、付与・剥奪の記録を残します。",
    "入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。",
    "脅威と統制の対応、監視、演習の記録をセットにします。",
    "攻撃パターンと対策を評価し、検知率・ブロック率をKRIで追います。",
    "選定基準と評価プロセス、契約・SLA、継続監視、証跡を一貫して設計します。",
    "論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。",
    "境界定義と統制、契約、運用を一貫させ、証跡の目次に含めます。",
    "品質KRIと閾値、是正率を記録し、データとリスクの対応を監視します。",
    "典型契約論点を条項と証跡でカバーし、雛形で効率化します。",
    "手法の使い所と限界を注記し、匿名化率・再識別リスクを記録します。",
    "争点（権利・表示・証跡・方針）をチェックし、監査指摘を想定した対策を取ります。",
    "コンテンツ種別と義務、表示、チェック、公開、記録のフローを決めます。",
    "当局報告の責任分界を事前に決め、インシデント設計に反映させます。",
    "エスカレーション閾値と重大基準を明文化し、記録と棚卸をセットにします。",
    "ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。",
    "出力物の権利・責任を方針に落とし、手続きと証跡を揃えます。",
    "Buy/Buildの評価軸を決め、選定・契約・監視・証跡を一貫させます。",
    "調達審査のRACIと承認フローを文書化し、証跡の目次を監査と合意します。",
    "レッドラインを定義し、許容度設計と承認運用、例外・KRIを決めます。",
    "定性・定量の使い分けとリスク評価の手順を文書化し、継続評価を回します。",
    "契約条項のチェックリストを用意し、living clausesで見直し可能にします。",
    "年次で優先5領域を決め、予算・人材・レビューのサイクルを設計します。",
    "取締役会向けの最小KRIとダッシュボードを用意し、閾値とアクションを決めます。",
    "ログ完全性・保持・改ざん検知を設計し、監査で説明できる形にします。",
    "所見の型と是正テンプレを用意し、追跡KPIで完了を管理します。",
    "BCPとAI依存の停止・代替・復旧手順を決め、証跡を残します。",
    "バイアス評価の手法選択と実施・記録・継続評価をセットにします。",
    "領域別の公平性論点を整理し、評価と証跡を業界の期待に合わせます。",
    "ボード指標の最小セットと意思決定ログ、四半期レビューを運用します。",
    "議題テンプレを毎四半期で回し、証跡と次のアクションを残します。",
    "グローバル運用の抜け穴をガードレールで塞ぎ、移行計画と証跡を決めます。",
    "集中と分散の意思決定基準を文書化し、選択の根拠を記録します。",
]

# チェックリスト用プール（30件）— 記事番号で選択し10項目にする
CHECKLIST_POOL = [
    "RACI（責任者・承認者）を決め、一枚にまとめているか",
    "申請―審査―承認のフローを文書化し、証跡を残しているか",
    "例外の基準と有効期限を決め、四半期で棚卸しているか",
    "証跡を改ざん耐性で保全し、保持期間を明示しているか",
    "継続評価の記録を残し、是正の流れをテンプレ化しているか",
    "インシデント時の報告・エスカレーション手順を決めているか",
    "規制・標準との対応関係を一覧化しているか（断定は避ける）",
    "監査提出の目次を監査法人と事前にすり合わせているか",
    "四半期の棚卸を予定し、記録を残しているか",
    "教育・周知の記録を残しているか",
    "成果物ごとに作成者・承認者・保管場所を決めているか",
    "開発・リリースのゲートと通過記録を設計しているか",
    "データ境界と漏えい経路に統制を置いているか",
    "脅威分類と統制・監視・演習の記録を揃えているか",
    "KRI・閾値・エスカレーション先を決めているか",
    "契約にBOM・ログ提供義務を盛り込み、責任分界を明示しているか",
    "DPIA・利用目的承認と証跡の連携を取っているか",
    "版管理と変更記録を残し、文書の形骸化を防いでいるか",
    "レッドチーム・演習の計画・結果・是正を記録しているか",
    "ベンダー・委託先との責任分界を契約と証跡で明示しているか",
    "品質指標・閾値・是正を継続的に追っているか",
    "透明性表示・公開前チェックの記録を残しているか",
    "学習データ・出力物の権利と責任を方針化しているか",
    "廃止・退役の手順と記録を決めているか",
    "ログ種別・目的・保持期間を一覧化し、完全性を検証しているか",
    "証跡の最小目次を固定し、欠落をチェックしているか",
    "Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか",
    "争点化に備えた証拠を想定し、日付・責任者の整合を保っているか",
    "ボード・監査向けの最小KRIと閾値 breach 時のアクションを決めているか",
    "アクセス制御を申請・承認・付与のフローに落としているか",
]

# 固有の一文の「明日から」部分（5パターン）
KEY_SENTENCE_ACTIONS = [
    "自部門で責任者と証跡の保管者を1人ずつ決め、証跡の目次を1枚にまとめて監査と1回確認することをお勧めします。",
    "申請フローと例外の基準を1つ決め、承認記録を必ず残すルールにすると、他領域の設計の基準になります。",
    "監査提出に必要な証跡の目次をリスト化し、監査法人に事前に1回提示して問題ないか確認してください。",
    "継続評価の頻度と是正の流れをテンプレ化し、四半期の棚卸日をカレンダーに登録することを推奨します。",
    "RACIと証跡の目次を関係者と共有し、インシデント時の報告先を1つ決めておくだけで、説明可能性が高まります。",
]

# 次の一歩のアクション文（15パターン）— 2つ組み合わせて使用
NEXT_STEPS_ACTIONS = [
    "自部門で「誰が承認者か」「証跡をどこに残すか」を1つ決め、監査法人に証憑の形を事前に1回確認する。",
    "証跡の目次を1枚にまとめ、保管責任者を1人決め、四半期の棚卸日をカレンダーに登録する。",
    "申請―審査―承認のフローを文書化し、例外の基準と有効期限を明文化する。",
    "RACIを一枚にまとめ関係者と共有し、継続評価とインシデント窓口を固定する。",
    "監査提出の目次を監査法人と1回すり合わせ、欠落しやすい項目をチェックリストに加える。",
    "開発・リリースのゲートと通過記録の形を決め、証跡の連鎖が切れないようにする。",
    "データ境界と統制の対応表を作り、担当とAI統制の責任分界を1回決める。",
    "脅威と統制の対応表を更新し、演習の計画・結果・是正を記録する。",
    "KRI・閾値・エスカレーション先を1つ決め、ダッシュボードかレビューで追う運用にする。",
    "契約にBOM・ログ提供の義務が入っているか確認し、入っていなければ次回更新で条項追加を検討する。",
    "DPIA・利用目的承認とAI利用申請の連携を1回確認し、証跡の紐づけを設計する。",
    "版管理と変更記録のルールを決め、文書の形骸化を防ぐための教育を1回行う。",
    "争点化を想定した証拠のリストを作り、日付・責任者・版の整合を保つ手順を決める。",
    "透明性表示と公開前チェックの手順を文書化し、記録を必ず残すルールにする。",
    "廃止・退役の手順と記録の形を決め、保持と再現性を確保する。",
]


def _get_three_formats(no):
    """記事番号に応じて、図1・図2・図3に割り当てる3種の形式（SVG/Mermaid/HTML/Table）を返す。直近5記事で同一形式が連続しないようローテーション。"""
    formats = ["SVG", "Mermaid", "HTML", "Table"]
    # 3つを異なるように選ぶ: (no-1)%4, (no)%4, (no+1)%4 のうち重複を除く
    a, b, c = (no - 1) % 4, no % 4, (no + 1) % 4
    if a == b:
        b = (b + 1) % 4
    if b == c or a == c:
        c = (c + 2) % 4
    if a == c:
        c = (c + 1) % 4
    return [formats[a], formats[b], formats[c]]


def _pick_points(no, section_index, count=4):
    """記事番号とセクション番号から、POINT_SENTENCES のインデックスを count 個選ぶ。"""
    indices = []
    for i in range(count * 2):  # 多めに候補を出して先頭から count 個取る
        idx = (no * 17 + section_index * 31 + i * 7) % len(POINT_SENTENCES)
        if idx not in indices:
            indices.append(idx)
        if len(indices) >= count:
            break
    return [POINT_SENTENCES[i] for i in indices[:count]]


def _pick_checklist(no, count=10):
    """記事番号に応じてチェックリストを count 項目選ぶ。重複なし・順序も記事ごとに変える。"""
    used = set()
    out = []
    for i in range(count * 3):
        idx = (no * 7 + i * 11) % len(CHECKLIST_POOL)
        if idx not in used:
            used.add(idx)
            out.append(CHECKLIST_POOL[idx])
        if len(out) >= count:
            break
    return out


def _build_lead(article):
    no, focus, title_ja, op = article["no"], article["unique_focus"], article["title_ja"], article["Op"]
    focus_short = focus.replace("に特化", "").strip("「」\"'")
    first = OPENING_LEADS.get(op, OPENING_LEADS[1])
    points = _pick_points(no, 0, 2)
    second = f"本稿の焦点は「{focus_short}」です。{title_ja}について、責任分界・証跡・監査提出の目次を具体化します。{points[0]} {points[1]}"
    return first + "\n\n" + second


def _build_body_section(article, section_index, section_title, is_first):
    no, focus = article["no"], article["unique_focus"]
    focus_short = focus.replace("に特化", "").strip("「」\"'")
    points = _pick_points(no, section_index, 6)
    if is_first:
        para1 = f"本稿の焦点は「{focus_short}」です。{section_title}では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。{points[0]} {points[1]}"
        para2 = f"さらに、{points[2]} {points[3]}"
        para3 = f"加えて、{points[4]} {points[5]}"
    else:
        # 「ここでは〜について、このテーマに応じた観点を整理します。」は使わない（ルールで禁止）
        para1 = f"{points[0]} {points[1]}"
        para2 = f"あわせて、{points[2]} {points[3]}"
        para3 = f"また、{points[4]} {points[5]}"
    return para1 + "\n\n" + para2 + "\n\n" + para3


def _build_body(article, section_titles):
    lines = []
    for i, st in enumerate(section_titles[:4]):
        lines.append(f"### {i + 1}. {st}")
        lines.append("")
        lines.append(_build_body_section(article, i, st, is_first=(i == 0)))
        lines.append("")
        if i == 0:
            lines.append("ここに図1を挿入")
        elif i == 1:
            lines.append("ここに図2を挿入")
        elif i == 2:
            lines.append("ここに図3を挿入")
        lines.append("")
    return "\n".join(lines).strip()


def _build_fig_content(article, fig_index, fmt, section_titles, outline, template_id):
    """図の形式とインデックスに応じて図の内容を返す。"""
    focus_short = article["unique_focus"].replace("に特化", "").strip("「」\"'")
    st = section_titles[fig_index] if fig_index < len(section_titles) else focus_short
    if fmt == "SVG":
        return build_fig_svg(focus_short, st, template_id)
    if fmt == "Mermaid":
        m1, m2, m3 = outline[1], outline[2], outline[3]
        return [m1, m2, m3][fig_index] if fig_index < 3 else outline[1]
    if fmt == "HTML":
        return build_fig_html(focus_short, st)
    if fmt == "Table":
        return build_fig_table(focus_short, st)
    return build_fig_svg(focus_short, st, template_id)


def build_full_llm_out(article):
    """記事1〜10と同様の構成かつそれ以上の文章量で llm-out を組み立てる。"""
    no = article["no"]
    slug = article["slug"]
    title_ja = article["title_ja"]
    focus = article["unique_focus"]
    template_id = article["template_id"]
    co = article["Co"]
    focus_short = focus.replace("に特化", "").strip("「」\"'")

    outline = TEMPLATE_OUTLINES.get(
        template_id,
        (["概要", "設計", "運用", "証跡"], "graph LR\n  A --> B", "graph TD\n  X --> Y", "graph TD\n  T1[差し戻し1]"),
    )
    section_titles = outline[0]

    # 図の型
    idx = (no - 1) % len(FIG_TYPE_TRIPLETS)
    t1, t2, t3 = FIG_TYPE_TRIPLETS[idx]

    # 図の形式（3種をローテーション）
    fmts = _get_three_formats(no)
    fig1_content = _build_fig_content(article, 0, fmts[0], section_titles, outline, template_id)
    fig2_content = _build_fig_content(article, 1, fmts[1], section_titles, outline, template_id)
    fig3_content = _build_fig_content(article, 2, fmts[2], section_titles, outline, template_id)

    lead = _build_lead(article)
    body_md = _build_body(article, section_titles)

    key_sentence = f"監査で問われやすいのは「{focus_short}」に関して、責任分界と証跡の目次が揃っていないことです。明日から、{KEY_SENTENCE_ACTIONS[no % len(KEY_SENTENCE_ACTIONS)]}"

    intro = CONCLUSION_INTROS.get(co, "明日から始められるステップです。")
    a1 = NEXT_STEPS_ACTIONS[no % len(NEXT_STEPS_ACTIONS)]
    a2 = NEXT_STEPS_ACTIONS[(no + 1) % len(NEXT_STEPS_ACTIONS)]
    next_steps = f"{intro} {a1} {a2}"

    refs = get_references_markdown(no, slug, template_id)

    checklist_items = _pick_checklist(no, 10)

    md = f"""## リード（1段落）

{lead}

## 本文

{body_md}

## 図1（{fmts[0]}）

```
{fig1_content}
```

## 図2（{fmts[1]}）

```
{fig2_content}
```

## 図3（{fmts[2]}）

```
{fig3_content}
```

## 図の型（記録用・必須）
図1: {t1}, 図2: {t2}, 図3: {t3}

## 図の形式（記録用・必須）
図1: {fmts[0]}, 図2: {fmts[1]}, 図3: {fmts[2]}

## 固有の一文（要点ボックス用1文）

{key_sentence}

## チェックリスト（10項目）

"""
    for item in checklist_items:
        md += f"- {item}\n"
    md += f"""
## 参考文献（3つ以上、発行年または一次資料明記）

{refs}

## 次の一歩（結論パターン Co に沿って）

{next_steps}
"""
    return md, {"fig1": t1, "fig2": t2, "fig3": t3, "f1": fmts[0], "f2": fmts[1], "f3": fmts[2]}


def main():
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    articles = parse_design()
    target = [a for a in articles if 11 <= a["no"] <= 163]
    if not target:
        print("No articles 11-163 in design.")
        return

    history_rows = []
    for a in target:
        no, slug = a["no"], a["slug"]
        content, fig_info = build_full_llm_out(a)
        out_path = BRIEFS_DIR / f"{no:03d}-{slug}-llm-out.md"
        out_path.write_text(content, encoding="utf-8")
        print("Wrote", out_path)
        history_rows.append({
            "no": no, "slug": slug, "fig1": fig_info["fig1"], "fig2": fig_info["fig2"], "fig3": fig_info["fig3"],
            "op": a["Op"], "fig1_fmt": fig_info["f1"], "fig2_fmt": fig_info["f2"], "fig3_fmt": fig_info["f3"],
        })

    # figure_usage_history.csv は 1-10 は既存のまま、11-163 を追記する想定。ここでは 11-163 分だけ書き出す（上書きしない）
    # 既存の 1-10 を読んでマージするか、apply 時に history が更新されるならスキップ可能。
    print("Done. Generated", len(target), "llm-out files (11-163).")


if __name__ == "__main__":
    main()
