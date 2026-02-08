#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIガバナンスブログ 155記事（#6-#160）を docs/ai-governance-blog-plan.md の掲載順で生成する。
既存5本（#1-#5）は手動作成済みのため対象外。
"""

import os
import re
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "blog" / "ai-governance"
BASE_URL = "https://riseby.net/blog/ai-governance"
# 記事の公開日（日付表示用）。新規3本は「今日の日付」で公開する想定。
ARTICLE_PUBLISH_DATE = "2026-02-05"
# Coworkショック3本のCTA：AIMOaaSへのリンク
AIMOaaS_URL = "https://aimoaas.com/ja/"
COWORK_SLUGS_FOR_AIMOaaS_CTA = {"saas-apocalypse-cowork-shock-part1.html", "saas-apocalypse-cowork-shock-part2.html", "saas-apocalypse-cowork-shock-part3.html"}

def escape_html(s):
    if s is None or s == "": return ""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def escape_attr(s):
    if s is None or s == "": return ""
    return escape_html(s).replace('"', "&quot;")

# カテゴリ → Tailwind バッジクラス（計画書 8.1 に準拠）
CATEGORY_STYLES = {
    "規制": "bg-rose-100 text-rose-800",
    "リスク": "bg-orange-100 text-orange-800",
    "倫理": "bg-indigo-100 text-indigo-800",
    "体制": "bg-emerald-100 text-emerald-800",
    "ライフサイクル": "bg-sky-100 text-sky-800",
    "データ": "bg-teal-100 text-teal-800",
    "監査": "bg-purple-100 text-purple-800",
    "業界": "bg-pink-100 text-pink-800",
    "標準": "bg-slate-100 text-slate-800",
    "戦略": "bg-lime-100 text-lime-800",
    "法務": "bg-amber-100 text-amber-800",
    "セキュリティ": "bg-red-100 text-red-800",
    "生成AI・GPAI": "bg-violet-100 text-violet-700",
    "Safety・評価": "bg-amber-100 text-amber-800",
    "透明性・真正性": "bg-cyan-100 text-cyan-800",
    "運用OS": "bg-blue-100 text-blue-800",
}

# 計画書 7.1 優先60本（#6-#60）と 7.2 残り100本（#61-#160）の順序で定義
# 各要素: (title, slug, category, living, lead, sections, keypoint_title, keypoint_text, meta_description)
# sections = [ (h2, [p1, p2, ...]), ... ]
# Coworkショック3本は 2026年2月初旬の日付で公開（参照は16要素目でカスタム指定）
COWORK_REFERENCES = [
    ("Anthropic、Claude Coworkを発表（Business Insider）", "https://www.businessinsider.com/anthropic-claude-cowork-release-ai-vibecoded-2026-1"),
    ("SaaS株への波及・モルガン・スタンレー指数（Bloomberg / Ben's Bites）", "https://news.bensbites.com/posts/55738-anthropics-claude-cowork-launch-has-revived-fears-about-disruption-that-weighed-on-saas-stocks-in-2025-morgan-stanley-saas-index-is-down-15-so-far-in-2026"),
    ("NIST AI RMF・生成AIプロファイル", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ("AI事業者ガイドライン（経済産業省）", "https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf"),
]
ARTICLES = [
    # SaaSアポカリプス（Coworkショック）前編・中編・後編（2026年2月初旬）
    (
        "SaaSアポカリプスとCoworkショック（前編）：なぜ「AIが仕事を奪う」恐慌が起きたか",
        "saas-apocalypse-cowork-shock-part1.html",
        "戦略",
        True,
        "2026年2月初旬、Anthropicの自律型AIエージェント「Claude Cowork」のリリースをきっかけに、SaaS株が急落し、いわゆる「SaaSアポカリプス」「Coworkショック」が報じられました。前編では、この問題が起きた背景を整理します。",
        [
            ("1. 自律型AIエージェントの台頭と「知識労働の自動化」", [
                "Claude Coworkは、デスクトップ上でファイル整理・データ抽出・タスク自動化など、これまでSaaSや社内ツールが担ってきた知識労働を自律的に実行するエージェントとして発表されました。重要なのは、Coworkの「ほとんどがAI自身によって2週間弱で構築された」と報じられた点です。AIがAIを組み、プロダクトが短期間でリリースされる構図が、従来のソフトウェア開発・SaaSビジネスモデルへの脅威として受け止められました。",
                "2025年を通じて、生成AIが個別タスクを補助する段階から、エージェントがワークフロー全体を代替しうる段階へと議論が移っていました。Coworkは、その象徴的な一歩として位置づけられ、投資家の懸念を一気に顕在化させました。"
            ]),
            ("2. SaaS依存と「置き換えリスク」の認識", [
                "企業の業務は、CRM・ERP・コラボツール・分析SaaSなどに深く依存しています。これらが「AIエージェント1体で代替される」と見なされると、従来のSaaSの収益モデルと株価は大きなプレッシャーを受けます。モルガン・スタンレーのSaaS指数が2026年序盤に前年比で大きく下落した背景には、こうした置き換えリスクの再評価があります。",
                "一方で、AIエージェント自体がSaaSやAPIと連携して動くため、「すべてが消える」のではなく、役割の再編とガバナンスの重要性が増すという見方もあります。前編では、恐慌が起きた構造的要因を押さえ、中編・後編へつなげます。"
            ]),
            ("3. ガバナンスの観点で何が問われるか", [
                "AIエージェントが業務を実行する場合、入力データの範囲・出力の検証・誰が責任を負うか・証跡をどう残すかが、規制と監査の両面で問われます。Coworkショックは、技術的な「できる」が先行するなか、説明責任と証跡（Evidence）の設計が追いついていないという課題を浮き彫りにしました。このテーマは後編のEvidence bundleで詳述します。"
            ]),
            ("まとめ", [
                "Coworkショックは、自律型AIエージェントの実用化が、SaaS業界と資本市場に「置き換えリスク」として一気に認識された出来事です。背景には、知識労働の自動化の加速と、AIがAIを組み短期でプロダクトを出す構図への不安があります。中編では市場の反応とAnthropicのレポート、後編ではEvidence bundleの重要性を扱います。"
            ]),
        ],
        "恐慌の背景には「誰が何を説明するか」の設計不足がある",
        "AIエージェントが業務を実行する以上、入力・出力・責任・証跡を事前に設計しておくことが、次の規制と監査の波に備えるうえで不可欠です。自社の利用形態を整理し、Evidenceをどう束ねるかから相談したい場合は、お気軽にご連絡ください。",
        "SaaSアポカリプス・Coworkショックの背景を解説。自律型AIと知識労働の置き換えリスク、ガバナンスの観点を整理します。",
        "graph LR\n        A[自律型AIエージェント] --> B[知識労働の自動化]\n        B --> C[SaaS置き換えリスク]\n        C --> D[市場の再評価]\n        style A fill:#e0f2fe,stroke:#003E68\n        style B fill:#e0f2fe,stroke:#003E68\n        style C fill:#fef9c3,stroke:#ca8a04\n        style D fill:#fee2e2,stroke:#b91c1c",
        "Coworkショックが起きた構造",
        "技術・プロダクト",
        ["AIがAIを構築（短期リリース）", "デスクトップエージェントの実用化", "ワークフロー単位の代替"],
        "市場・ガバナンス",
        ["SaaS株の下落・置き換え懸念", "説明責任・証跡の設計の遅れ", "規制・監査の追い上げ"],
        COWORK_REFERENCES,
    ),
    (
        "SaaSアポカリプスとCoworkショック（中編）：世界の市場反応とAnthropic Coworkレポート",
        "saas-apocalypse-cowork-shock-part2.html",
        "生成AI・GPAI",
        True,
        "Coworkショックの中編では、世界中の市場の反応を整理し、AnthropicのClaude Coworkに関する詳細レポートのポイントを押さえます。投資家・アナリストの見方と、プロダクトの位置づけを理解することで、自社のAIガバナンスとSaaS戦略の議論に役立てられます。",
        [
            ("1. 世界の市場反応：SaaS指数とセクターの動き", [
                "モルガン・スタンレーのSaaS指数は、2026年序盤に前年比で約15％下落し、ここ数年で最も厳しいスタートとなったと報じられました。Coworkのリリースが、2025年から続いていた「AIによるSaaS disruption」への懸念を再燃させたとされています。北米だけでなく、欧州・アジアのテック株も、生成AIエージェントの普及が既存ソフトウェアの収益を圧迫するというシナリオを織り込み始めました。",
                "一方で、AIインフラやAIネイティブなサービスを提供する企業には、資金が流れる動きもあり、市場は「壊される側」と「再編の主役」を峻別しつつあります。"
            ]),
            ("2. AnthropicのClaude Coworkに関する詳細レポートの要点", [
                "Anthropicは、Claude Coworkを「デスクトップネイティブな自律型AIエージェント」として位置づけ、ファイル整理・データ抽出・タスク自動化といった知識労働を支援すると説明しています。特筆すべきは、Coworkの大部分がAI（Claude）によって構築され、約2週間で開発されたと公表された点です。これは、開発スピードとスケールの観点で、従来のソフトウェア開発やSaaSのリリースサイクルとは異なるパラダイムを示しています。",
                "現時点ではClaude Max加入者向けのmacOSリサーチプレビューとして提供され、利用範囲やデータの扱い・証跡の取り方について、ガバナンスの観点から注目が集まっています。"
            ]),
            ("3. 企業が取るべきアクション", [
                "自社がSaaS提供側であれば、AIエージェントとの差別化・連携・説明責任の設計が急務です。利用側であれば、Coworkのようなエージェントを業務に組み込む場合の利用規程・入力制限・出力検証・証跡の保持を、事前にガバナンスに落とす必要があります。中編で得た市場とレポートの知見を、後編のEvidence bundleの議論に接続します。"
            ]),
            ("まとめ", [
                "世界中の市場は、CoworkをきっかけにSaaSの置き換えリスクを再評価し、指数は大きく揺れました。Anthropicのレポートは、自律型エージェントの開発スピードとスコープを示し、企業には利用規程と証跡の設計が求められています。後編では、今後のAIガバナンスにおけるEvidence bundleの重要性拡大を論じます。"
            ]),
        ],
        "市場とレポートを踏まえ、自社の利用と証跡の設計を急ぐ",
        "Coworkのようなエージェントを導入する場合、何を記録し誰が説明するかを決めておくことが、規制と監査に対応する第一歩です。Evidence bundleの設計から相談したい場合は、お気軽にご連絡ください。",
        "Coworkショックの中編。世界の市場反応とAnthropic Coworkレポートの要点、企業のアクションを整理します。",
        "graph LR\n        A[Coworkリリース] --> B[市場の反応]\n        B --> C[SaaS指数下落]\n        B --> D[AIインフラ・再編]\n        style A fill:#e0f2fe,stroke:#003E68\n        style B fill:#fef9c3,stroke:#ca8a04\n        style C fill:#fee2e2,stroke:#b91c1c\n        style D fill:#dcfce7,stroke:#15803d",
        "市場とレポートの整理",
        "市場の反応",
        ["SaaS指数の下落・置き換え懸念", "地域別のテック株の動き", "AIネイティブへの資金シフト"],
        "Coworkレポートの要点",
        ["自律型エージェントの位置づけ", "AIによる短期開発の実例", "リサーチプレビューとガバナンス"],
        COWORK_REFERENCES,
    ),
    (
        "SaaSアポカリプスとCoworkショック（後編）：Evidence bundleの重要性拡大とAIガバナンス",
        "saas-apocalypse-cowork-shock-part3.html",
        "監査",
        True,
        "Coworkショックの後編では、自律型AIエージェントの普及が進むなか、今後のAIガバナンスにおいてEvidence bundle（証跡の束）の重要性がどう拡大するかを論じます。監査・規制対応・説明責任を一気通貫で支える設計を整理します。",
        [
            ("1. なぜEvidence bundleがこれまで以上に重要になるか", [
                "AIエージェントがファイル操作・データ抽出・意思決定に近いタスクを実行する場合、「何を・いつ・どの条件で行ったか」を証跡として残さないと、監査や規制当局・顧客からの説明要求に応えられません。Coworkのようなツールが社内に広がると、従来の「人が操作したログ」に加え、「エージェントが実行したアクションのログ」「入力・出力・承認の記録」を束ねたEvidence bundleが、説明責任の要になります。",
                "EU AI Actをはじめとする規制では、高リスク用途や透明性義務に伴い、技術文書・ログ・評価結果を保持することが求められます。Evidence bundleは、それらを一括で管理・提示する考え方です。"
            ]),
            ("2. Evidence bundleに含めるべき要素", [
                "最低限、次の要素を束ねる設計が推奨されます。利用規程と承認履歴、エージェントの入力・出力・実行ログ、評価（Evals）の結果と日付、インシデントや例外の記録、そして規制・監査要件ごとのマッピングです。Coworkのような自律型エージェントを利用する場合は、どのタスクを許可したか・どのデータにアクセスさせたか・出力を誰が確認したかを、証跡として残すプロセスが欠かせません。",
                "これらを「監査法人が欲しい束ね方」で整え、四半期やリリース単位で更新できるようにしておくと、突発的な説明要求にも対応しやすくなります。"
            ]),
            ("3. 今後のAIガバナンス：設計と運用の両輪", [
                "Evidence bundleは一度作って終わりではなく、プロダクトの変更・規制のLivingな更新・監査サイクルに合わせて更新し続ける必要があります。Coworkショックを経て、企業は「AIエージェントをどう統制し、どう説明するか」をガバナンスの中心に据える動きを強めています。設計の段階で証跡の取り方を組み込み、運用でログと承認をためていく両輪が、今後のAIガバナンスの標準になっていくでしょう。"
            ]),
            ("まとめ", [
                "自律型AIエージェントの普及に伴い、Evidence bundleの重要性はさらに高まります。利用規程・ログ・評価・例外記録を束ね、監査と規制対応に耐える証跡を設計しておくことが、Coworkショック以降のAIガバナンスでは不可欠です。本シリーズで扱った背景・市場・Evidenceの三点を、自社のロードマップに落とし込む際は、お気軽にご相談ください。"
            ]),
        ],
        "証跡を束ね、説明責任を設計の中心に置く",
        "Evidence bundleを事前に設計し、エージェント利用の承認・ログ・評価を運用でためていくことで、規制と監査の波に後手を取らずに済みます。設計から相談したい場合は、お気軽にご連絡ください。",
        "Coworkショック後編。Evidence bundleの重要性拡大と、AIガバナンスにおける証跡の設計・運用を解説します。",
        "graph LR\n        A[エージェント利用] --> B[ログ・承認]\n        B --> C[Evidence bundle]\n        C --> D[監査・規制対応]\n        style A fill:#e0f2fe,stroke:#003E68\n        style B fill:#e0f2fe,stroke:#003E68\n        style C fill:#dcfce7,stroke:#15803d\n        style D fill:#e0f2fe,stroke:#003E68",
        "Evidence bundleの構成",
        "記録・証跡",
        ["利用規程・承認履歴", "入力・出力・実行ログ", "Evals結果と日付"],
        "監査・規制",
        ["インシデント・例外の記録", "規制要件とのマッピング", "四半期・リリース単位の更新"],
        COWORK_REFERENCES,
    ),
    # #6
    (
        "LLMの利用規程：社内/顧客提供で分けるべき要件",
        "llm-use-policy-internal-customer.html",
        "生成AI・GPAI",
        True,
        "LLMを社内でだけ使う場合と、顧客に提供する場合では、求められる統制と契約要件が異なります。EU AI Actの透明性義務やGPAI Code of Practiceをふまえ、社内利用と顧客提供で分けるべき要件を整理し、利用規程の設計に落とし込みます。",
        [
            ("1. 社内利用と顧客提供の違い", [
                "社内利用（B2E）では、入力の制限（機密・個人情報の禁止）、出力の検証（人間の確認範囲）、再配布・外部提供の禁止などが規程の中心になります。一方、顧客提供（B2B/B2C）では、AIであることの表示、生成コンテンツのラベリング、SLA・責任分担・監査権が契約と規程の両方で必要です。",
                "同じLLM基盤でも、利用形態によって「誰に説明責任を負うか」「どの証跡を残すか」が変わるため、規程は利用形態ごとに分けて定義するか、一つの規程の中でセクションを分けて明示する設計が望ましいです。"
            ]),
            ("2. 社内利用規程で押さえる項目", [
                "機密情報・個人情報の入力禁止、許可された用途の列挙、出力の人間確認が必要な範囲、ログと監査証跡の保持期間、禁止行為（再配布・改変・商用転用の制限）を明文化します。シャドウAI対策として「正規ルート」の申請・承認フローも規程に含めると、禁止だけでなく誘導ができます。"
            ]),
            ("3. 顧客提供で分けるべき要件", [
                "顧客向けには、AI利用の開示、生成物の表示、苦情対応窓口、データの取り扱い（学習に使わない等）、監査権・情報提供義務を契約と利用規約の両方で定めます。業界規制（金融・医療等）がかかる場合は、その要件を満たす表示・説明・証跡を追加します。"
            ]),
            ("まとめ", [
                "LLMの利用規程は、社内と顧客提供で分けて設計し、それぞれに必要な禁止・開示・証跡・契約を明示します。規制と監査の期待に合わせて四半期ごとに見直すと、Livingな運用ができます。"
            ]),
        ],
        "社内と顧客提供で「要件のセット」を分けて明文化する",
        "利用形態ごとに説明責任と証跡の範囲が変わるため、一つの規程で「社内用」と「顧客提供用」のセクションを分け、それぞれに必須項目をそろえる設計が実務的です。",
        "LLMの利用規程で社内と顧客提供を分けるべき要件を整理。規制・契約・証跡の観点で設計します。",
        "graph LR\n        A[利用規程] --> B[社内/顧客の分離]\n        B --> C[開示・証跡]\n        C --> D[契約・監査]\n        style A fill:#e0f2fe,stroke:#003E68\n        style B fill:#e0f2fe,stroke:#003E68\n        style C fill:#e0f2fe,stroke:#003E68\n        style D fill:#e0f2fe,stroke:#003E68",
        "社内利用と顧客提供で分ける要件",
        "社内利用（B2E）",
        ["入力制限・機密禁止", "出力の人間確認範囲", "ログ・証跡の保持"],
        "顧客提供（B2B/B2C）",
        ["AI利用の開示・表示", "SLA・責任分担", "監査権・情報提供"],
    ),
    # #7
    (
        "RAGとガバナンス：参照・出典・更新の統制",
        "rag-governance-reference-citation.html",
        "生成AI・GPAI",
        False,
        "RAG（Retrieval-Augmented Generation）では、参照したドキュメントと出典の管理、およびナレッジベースの更新がガバナンスの焦点になります。ハルシネーションの抑制と説明責任の両立のため、参照・出典・更新の統制をどう設計するかを整理します。",
        [
            ("1. RAGがガバナンスに載せるべき理由", [
                "RAGは外部ナレッジを参照して回答を生成するため、「何を根拠にしたか」を説明できることが顧客・監査・規制の期待に応えるうえで重要です。参照元の記録と出典の表示、ナレッジの鮮度・権限管理が不十分だと、誤情報の伝播や説明責任の欠如につながります。"
            ]),
            ("2. 参照・出典の統制", [
                "どのドキュメントをどのタイミングで参照したかをログに残し、回答と紐づけます。UIでは出典を表示する設計にし、表示ルール（必ず表示するか、オプションか）を規程で定めます。参照範囲のアクセス権・機密区分もナレッジベースの設計に組み込みます。"
            ]),
            ("3. ナレッジの更新と検証", [
                "ナレッジベースの更新頻度、更新時の検証（品質・正確性）、古い情報の扱いをプロセス化します。更新履歴とバージョンを記録し、いつどの版を参照したかを証跡として残すと、監査やインシデント時の説明に使えます。"
            ]),
            ("まとめ", [
                "RAGのガバナンスでは参照・出典の記録と表示、ナレッジの更新・検証・版管理を統制に落とし、説明責任と品質を両立させます。"
            ]),
        ],
        "参照元と出典を「証跡」として残し、更新をプロセス化する",
        "RAGの説明責任は、何を参照したかの記録と出典表示、そしてナレッジの更新ルールの三点で支えられます。",
        "RAGの参照・出典・ナレッジ更新をガバナンスに載せる設計。説明責任と品質の両立を整理します。",
        "graph LR\n        A[参照元記録] --> B[出典表示]\n        B --> C[ナレッジ更新]\n        C --> D[証跡・監査]\n        style A fill:#e0f2fe,stroke:#003E68\n        style B fill:#e0f2fe,stroke:#003E68\n        style C fill:#e0f2fe,stroke:#003E68\n        style D fill:#e0f2fe,stroke:#003E68",
        "RAGガバナンスの整理",
        "参照・出典",
        ["参照ドキュメントのログ", "UIでの出典表示", "アクセス権・機密区分"],
        "更新・検証",
        ["ナレッジ更新頻度", "更新時の検証", "版管理・履歴"],
    ),
]

# 記事仕様：1記事につき必ず3つのインフォグラフィック（Mermaid・カード・KeyPoint 各1）
# 計画書 1.2 / 4.1 / 4.2 / 4.3 に準拠。AIカテゴリ（global-ai-governance, fine-tuning-vs-rag, ai-data-privacy 等）を参考に、
# テーマごとに異なる図表・十分な文量・参照リンク・CTA を組み込む。

# 計画書「6. 参考になる"最新トレンドの根拠"」より。参考・参照セクションで使用する公式URL
REFERENCE_URLS = [
    ("EU AI Act（欧州デジタル戦略）", "https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act"),
    ("GPAI Code of Practice（欧州委員会）", "https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai"),
    ("NIST AI RMF・生成AIプロファイル", "https://www.nist.gov/itl/ai-risk-management-framework"),
    ("OECD AI Transparency（G7広島AIプロセス）", "https://transparency.oecd.ai/"),
    ("AI事業者ガイドライン（経済産業省）", "https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf"),
    ("ISO/IEC 42001（AIMS）", "https://www.iso.org/standard/42001"),
]

# カテゴリごとに異なる Mermaid パターン（計画書4.2・AIブログを参考に記事ごとに中身を変える）
# ルール: 暗い背景（#003E68 等）のノードには必ず color:#fff を指定し、視認性を確保する（計画書4.4）
MERMAID_BY_CATEGORY = {
    "規制": [
        """graph TD
        Input[AIシステムの特定] --> Classify{リスク分類}
        Classify --> Prohibited[禁止]
        Classify --> High[高リスク]
        Classify --> Limited[限定的リスク]
        Classify --> Minimal[最小リスク]
        High --> Heavy[適合性評価・QMS]
        Limited --> Light[透明性確保]
        style Prohibited fill:#fee2e2,stroke:#b91c1c
        style High fill:#fef9c3,stroke:#ca8a04
        style Limited fill:#e0f2fe,stroke:#003E68
        style Minimal fill:#dcfce7,stroke:#15803d""",
        """graph LR
        A[要件把握] --> B[域外適用の確認]
        B --> C[本社責任の明確化]
        C --> D[ローカル適応]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "リスク": [
        """graph TD
        Risk[リスク特定] --> Assess{影響度}
        Assess --> High[高：即時対応]
        Assess --> Mid[中：計画対応]
        Assess --> Low[低：監視]
        High --> Record[記録・エスカレーション]
        Mid --> Record
        style High fill:#fee2e2,stroke:#b91c1c
        style Mid fill:#fef9c3,stroke:#ca8a04
        style Low fill:#dcfce7,stroke:#15803d""",
        """graph LR
        A[アセスメント] --> B[記録]
        B --> C[監査証跡]
        C --> D[見直し]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "Safety・評価": [
        """graph TD
        Eval[評価設計] --> Purpose{目的}
        Purpose --> Quality[品質評価]
        Purpose --> Risk[リスク評価]
        Quality --> Bench[ベンチマーク/テスト]
        Risk --> Harm[有害性/バイアス/セキュリティ]
        style Quality fill:#dcfce7,stroke:#15803d
        style Risk fill:#fef9c3,stroke:#ca8a04""",
        """graph LR
        A[テスト設計] --> B[実施]
        B --> C[記録]
        C --> D[継続モニタリング]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "データ": [
        """graph LR
        Data[データ取得] --> Gov[ガバナンス]
        Gov --> Quality[品質・権利処理]
        Quality --> Train[学習/利用]
        Train --> Log[記録・証跡]
        style Data fill:#e0f2fe,stroke:#003E68
        style Gov fill:#e0f2fe,stroke:#003E68
        style Quality fill:#e0f2fe,stroke:#003E68
        style Train fill:#e0f2fe,stroke:#003E68
        style Log fill:#e0f2fe,stroke:#003E68""",
        """graph TD
        Input[入力データ] --> Check{PII・機密}
        Check -->|あり| Mask[マスキング/除外]
        Check -->|安全| Model[モデル]
        Mask --> Model
        Model --> Output[出力]
        style Check fill:#fef9c3,stroke:#ca8a04
        style Mask fill:#fee2e2,stroke:#b91c1c""",
    ],
    "監査": [
        """graph LR
        A[統制の把握] --> B[証跡の収集]
        B --> C[テスト・サンプリング]
        C --> D[報告・改善]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
        """graph TD
        Scope[監査範囲] --> Eval[評価]
        Eval --> Finding[指摘]
        Finding --> Action[是正・フォロー]
        style Eval fill:#e0f2fe,stroke:#003E68
        style Finding fill:#fef9c3,stroke:#ca8a04""",
    ],
    "体制": [
        """graph TD
        Board[取締役会] --> Policy[方針]
        Policy --> Committee[委員会]
        Committee --> Ops[現場運用]
        Ops --> Report[報告]
        Report --> Board
        style Board fill:#003E68,stroke:#0f172a,color:#fff
        style Committee fill:#e0f2fe,stroke:#003E68
        style Ops fill:#e0f2fe,stroke:#003E68""",
        """graph LR
        A[ガバナンス設計] --> B[役割分担]
        B --> C[承認フロー]
        C --> D[例外管理]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "法務": [
        """graph LR
        A[契約・条項] --> B[責任分担]
        B --> C[監査権]
        C --> D[紛争時証拠]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "セキュリティ": [
        """graph TD
        Threat[脅威モデル] --> Control[統制設計]
        Control --> Test[テスト]
        Test --> Monitor[監視・アラート]
        style Threat fill:#fee2e2,stroke:#b91c1c
        style Control fill:#e0f2fe,stroke:#003E68
        style Monitor fill:#fef9c3,stroke:#ca8a04""",
        """graph LR
        A[入力制御] --> B[出力検証]
        B --> C[ログ保全]
        C --> D[インシデント対応]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "倫理": [
        """graph LR
        A[原則の採用] --> B[バイアス評価]
        B --> C[ヒューマン監督]
        C --> D[モニタリング]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "運用OS": [
        """graph LR
        A[申請] --> B[審査]
        B --> C[例外管理]
        C --> D[証跡・更新]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
        """graph TD
        Req[要件] --> Build[構築]
        Build --> Test[テスト]
        Test --> Deploy[デプロイ]
        Deploy --> Monitor[監視]
        Monitor --> Req
        style Req fill:#e0f2fe,stroke:#003E68
        style Monitor fill:#fef9c3,stroke:#ca8a04""",
    ],
    "生成AI・GPAI": [
        """graph LR
        A[利用規程] --> B[データ境界]
        B --> C[評価・Evals]
        C --> D[透明性・表示]
        D --> E[証跡・ログ]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68
        style E fill:#e0f2fe,stroke:#003E68""",
        """graph TD
        Use[利用形態] --> Sep{社内/顧客}
        Sep --> Internal[社内: 入力制限・証跡]
        Sep --> External[顧客: 開示・SLA]
        style Internal fill:#dcfce7,stroke:#15803d
        style External fill:#e0f2fe,stroke:#003E68""",
    ],
    "透明性・真正性": [
        """graph LR
        A[表示ルール] --> B[ラベリング]
        B --> C[検証プロセス]
        C --> D[証跡]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "標準": [
        """graph LR
        A[フレームワーク選定] --> B[自社への落とし込み]
        B --> C[優先順位]
        C --> D[統合・運用]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "戦略": [
        """graph LR
        A[現状評価] --> B[ロードマップ]
        B --> C[人材・投資]
        C --> D[継続改善]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "業界": [
        """graph LR
        A[業界規制] --> B[統制設計]
        B --> C[証跡・報告]
        C --> D[当局対応]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68""",
    ],
    "ライフサイクル": [
        """graph LR
        A[企画] --> B[開発]
        B --> C[リリース]
        C --> D[モニタリング]
        D --> E[廃止]
        style A fill:#e0f2fe,stroke:#003E68
        style B fill:#e0f2fe,stroke:#003E68
        style C fill:#e0f2fe,stroke:#003E68
        style D fill:#e0f2fe,stroke:#003E68
        style E fill:#e0f2fe,stroke:#003E68""",
    ],
}

# カテゴリ別のカード文言パターン（テーマに即した具体語。計画書4.2）
CARD_BY_CATEGORY = {
    "規制": [
        ("禁止・高リスクの整理", "禁止・許容できないリスク", ["ソーシャルスコアリング", "実在しないリスクの悪用", "特定の脆弱者層への悪用"], "適合性評価の流れ", ["リスク分類の記録", "QMS・技術文書", "市場監督当局対応"]),
        ("域外適用と本社責任", "適用される法域", ["EU域内提供", "ブリュッセル効果", "本社の説明責任"], "ローカル適応", ["各国の追加要件", "現地法人の役割", "報告ライン"]),
    ],
    "リスク": [
        ("リスクの観点", "法務・コンプライアンス", ["規制違反", "契約・責任", "レピュテーション"], "運用・戦略", ["業務影響", "投資判断", "サードパーティ連鎖"]),
        ("アセスメントと記録", "実施内容", ["手法・粒度", "記録の保持", "監査耐性"], "次のアクション", ["是正計画", "エスカレーション", "見直し頻度"]),
    ],
    "Safety・評価": [
        ("品質評価の観点", "タスク達成度", ["精度・一貫性", "ベンチマーク", "テストセット"], "リスク評価の観点", ["有害出力", "バイアス", "セキュリティ（脱獄・漏えい）"]),
        ("評価設計と運用", "設計", ["目的の分離", "閾値の設定", "テストケース"], "証跡", ["実施日・条件", "合格基準", "結果の要約"]),
    ],
    "データ": [
        ("データの観点", "ガバナンス", ["権利処理", "品質・GIGO", "保持期間"], "実装・証跡", ["DPIA連動", "越境の設計", "監査証跡"]),
        ("学習と利用", "入力側", ["学習データの許諾", "個人データの扱い", "合成データの位置づけ"], "出力側", ["生成物の記録", "参照元の表示", "削除権対応"]),
    ],
    "監査": [
        ("内部監査の観点", "評価対象", ["統制の有無", "証跡の十分性", "例外の扱い"], "外部監査への準備", ["Evidence Bundle", "サンプリング可能性", "説明会の準備"]),
        ("統制と証跡", "統制", ["ポリシー", "プロセス", "ツール"], "証跡", ["ログ", "承認履歴", "文書バージョン"]),
    ],
    "体制": [
        ("ガバナンスの層", "方針・役割", ["取締役会の議題", "委員会の権限", "CxOの分担"], "運用", ["申請・承認", "例外管理", "成熟度の評価"]),
        ("中央とローカル", "グローバルベースライン", ["最低限のルール", "報告要件", "共通指標"], "ローカル適応", ["各国の追加", "現地の実装", "エスカレーション"]),
    ],
    "法務": [
        ("契約の観点", "必須条項", ["監査権", "透明性", "責任分担"], "運用", ["免責の限界", "紛争時の証拠", "規制変更条項"]),
    ],
    "セキュリティ": [
        ("脅威と統制", "脅威", ["プロンプトインジェクション", "データ漏えい", "モデル改ざん"], "統制", ["入力制御", "出力検証", "ログ保全"]),
        ("設計と運用", "設計", ["ゼロトラスト", "DLP連携", "Red Line"], "運用", ["KRI・アラート", "インシデント手順", "教育"]),
    ],
    "倫理": [
        ("原則と実装", "採用する原則", ["公平性", "説明可能性", "人間の監督"], "運用", ["バイアス評価", "是正の回し方", "モニタリング"]),
    ],
    "運用OS": [
        ("運用の流れ", "申請・審査", ["ユースケース登録", "リスク閾値", "例外申請"], "証跡・更新", ["ログ", "Evidence Bundle", "四半期見直し"]),
        ("自動化と人", "自動化できる部分", ["申請フォーム", "チェックリスト", "ログ収集"], "人が担う部分", ["例外判断", "取締役会報告", "規制の解釈"]),
    ],
    "生成AI・GPAI": [
        ("社内と顧客提供", "社内利用（B2E）", ["入力制限", "出力の人間確認", "ログ・証跡"], "顧客提供（B2B/B2C）", ["AIの開示", "SLA・責任", "監査権"]),
        ("データ境界", "学習・微調整", ["学習データの権利", "微調整データの範囲"], "推論・ログ", ["プロンプトの扱い", "ログの保持", "証跡"]),
    ],
    "透明性・真正性": [
        ("表示と検証", "表示ルール", ["AI生成の明示", "加工度の分類", "UI/UX"], "検証・証跡", ["表示判断の根拠", "監査証跡", "苦情対応"]),
    ],
    "標準": [
        ("フレームワークの位置づけ", "採用する枠組み", ["ISO 42001", "NIST AI RMF", "業界ガイド"], "自社への落とし込み", ["優先順位", "重複の排除", "文書の版管理"]),
    ],
    "戦略": [
        ("ロードマップと人", "計画", ["90日/180日/1年", "規制追随", "改善サイクル"], "人・投資", ["必要ロール", "ROIの語り方", "経営報告"]),
    ],
    "業界": [
        ("業界の焦点", "規制・倫理", ["業界別規制", "説明責任", "当局対応"], "実装", ["統制パッケージ", "KRIの業界差", "報告の癖"]),
    ],
    "ライフサイクル": [
        ("ライフサイクルと統制", "企画〜開発", ["要件", "設計", "検証の証跡"], "リリース〜廃止", ["デプロイ承認", "モニタリング", "廃止時の記録"]),
    ],
}

def _get_mermaid_for(category, index):
    opts = MERMAID_BY_CATEGORY.get(category, MERMAID_BY_CATEGORY["体制"])
    if isinstance(opts, str):
        opts = [opts]
    return opts[index % len(opts)]

def _get_card_for(category, index):
    opts = CARD_BY_CATEGORY.get(category, CARD_BY_CATEGORY["体制"])
    if opts and isinstance(opts[0], (list, tuple)) and len(opts[0]) == 5:
        one = opts[index % len(opts)]
        return one[0], one[1], one[2], one[3], one[4]
    return "本テーマの整理：観点と実装", "観点・要件", ["規制・ガイドラインの要件整理", "リスクと責任の明確化", "証跡として残す範囲の定義"], "実装・証跡", ["ポリシーとプロセスの設計", "申請・承認・記録の運用", "監査・説明責任への接続"]

def _get_references_for(category):
    """カテゴリに応じて2〜4本の参照リンクを返す"""
    # 規制・Living系は EU, OECD, METI を多めに。データは GDPR 系。監査・標準は NIST, ISO 等。
    refs = []
    if category in ("規制", "生成AI・GPAI", "透明性・真正性"):
        refs = [0, 1, 4]  # EU AI Act, GPAI Code, METI
    elif category in ("データ", "法務"):
        refs = [0, 2, 4]  # EU, NIST, METI
    elif category in ("監査", "運用OS", "標準"):
        refs = [2, 4, 5]  # NIST, METI, ISO
    elif category in ("Safety・評価", "リスク"):
        refs = [2, 4]  # NIST, METI
    elif category in ("体制", "戦略", "倫理"):
        refs = [3, 4]  # OECD, METI
    elif category in ("セキュリティ", "ライフサイクル"):
        refs = [2, 4]
    else:
        refs = [2, 4]
    return [(REFERENCE_URLS[i][0], REFERENCE_URLS[i][1]) for i in refs if i < len(REFERENCE_URLS)]

# #8-#160: (title, slug, category, living [, index]) → 本文は make_template_article で生成
def make_template_article(title, slug, category, living, index=0):
    """タイトル・カテゴリ・indexからリード・本論・KeyPoint・meta と、3要素（Mermaid・カード・KeyPoint）・参照リンクを生成（計画書4.2/4.3）"""
    # リード：2〜3文で読み応えを出す
    lead = f"{title}は、企業のAIガバナンスにおいて経営・法務・監査が意思決定するうえで重要なテーマです。"
    lead += "規制・フレームワークの動向をふまえ、実装と証跡の両面で使える形に整理します。"
    lead += "本稿では背景、設計のポイント、監査・説明責任への接続まで一通り押さえ、次のアクションに繋げられるようにします。"
    # 各h2は2〜3段落（計画書4.3）
    sections = [
        ("1. 背景と求められる統制", [
            "規制や業界の期待は年々具体化しており、同じテーマでも「何を証跡として残すか」「誰が責任を負うか」を明確にしておくことが、監査と説明責任に対応するうえで不可欠です。",
            "本テーマに関連する主な規制・ガイドライン（EU AI Act、NIST AI RMF、各国ガイドライン等）を参照し、自社の利用形態に合わせて統制の粒度を決めます。",
            "Living（生きている文書）として更新される規制には、四半期ごとの棚卸しやホライズンスキャンを組み込むと、後手に回りにくくなります。"
        ]),
        ("2. 設計のポイント", [
            "ポリシーとプロセスを分けて設計し、プロセスでは申請・承認・記録・例外管理を一気通貫で回せるようにします。ツールで自動化できる部分と、人の判断が必要な部分を切り分け、証跡が残る設計にします。",
            "特に高リスク用途や対外的な提供では、適合性評価・技術文書・QMSの要件を満たす設計を前もって組み込んでおくことが、規制対応と監査の効率化につながります。"
        ]),
        ("3. 監査・説明責任への接続", [
            "内部監査や外部監査が期待する「何をどこまで残すか」を事前に整理し、ログ・文書・承認履歴を束ねたEvidence Bundleを定期的に更新できるようにします。",
            "規制がLivingに更新される場合は、四半期ごとの棚卸しを推奨します。自社の状況を整理したい、証跡の設計から相談したい場合は、専門家への相談も有効です。"
        ]),
        ("まとめ", [
            f"{title}について、背景・設計・監査接続の三点を押さえ、実装と証跡を両立させる設計が重要です。規制追随と改善サイクルを組み込んだ運用を推奨します。",
            "次の一歩として、自社の利用形態と規制の適用範囲を洗い出し、どこから統制を強化するか優先順位をつけるところから始めることをお勧めします。ご不明点や具体的な設計の相談は、お気軽に問い合わせください。"
        ]),
    ]
    kp_title = "証跡と責任の範囲を事前に決め、運用で回す"
    kp_text = "どの統制も「誰が何を記録し、誰が説明するか」を明示し、監査と規制対応に耐える証跡を残す設計にすると、後から追いかけずに済みます。自社で確認したい点やロードマップの整理について、相談したい場合はお気軽にご連絡ください。"
    meta = f"{title}。規制・実装・監査の観点で整理し、企業が取り組むべきポイントを解説します。"
    # インフォグラフィック：カテゴリ・indexで多様なMermaid・カードを選択（計画書4.2）
    mermaid_chart = _get_mermaid_for(category, index)
    card_caption, card_left_title, card_left_items, card_right_title, card_right_items = _get_card_for(category, index)
    references = _get_references_for(category)
    return (title, slug, category, living, lead, sections, kp_title, kp_text, meta,
            mermaid_chart, card_caption, card_left_title, card_left_items, card_right_title, card_right_items, references)

# 計画書 7.1 Phase1 #8-#20, Phase2 #21-#40, Phase3 #41-#60 / 7.2 Phase4 #61-#80 … Phase8 #141-#160
SHORT_LIST = [
    ("有害出力・違法支援：統制の設計（ポリシー/運用/監視）", "harmful-unlawful-output-control.html", "Safety・評価", False),
    ("AI生成表示：UI/UXと法務の接続点", "ai-generated-display-ui-legal.html", "透明性・真正性", False),
    ('セーフティケース：説明責任を"構造"で作る', "safety-case-accountability.html", "Safety・評価", False),
    ("監視とアラート：運用で回るKRI設計", "monitoring-alert-kri-design.html", "Safety・評価", False),
    ("バイアス評価：定性/定量の現実解", "bias-evaluation-qualitative-quantitative.html", "Safety・評価", False),
    ("透かし/メタデータ：限界と期待値調整", "watermark-metadata-limits.html", "透明性・真正性", False),
    ("LLMのデータ境界：学習/微調整/推論/ログ", "llm-data-boundary.html", "生成AI・GPAI", False),
    ("重大インシデント基準：どこからエスカレーションか", "major-incident-criteria-escalation.html", "Safety・評価", False),
    ("評価の自動化：CI/CDに統制を埋め込む", "eval-automation-cicd.html", "Safety・評価", False),
    ("生成/加工度の分類：運用で破綻しないタキソノミー", "generated-edited-classification-taxonomy.html", "透明性・真正性", False),
    ("ディープフェイク対策：企業ブランドを守る統制", "deepfake-countermeasures.html", "透明性・真正性", False),
    ("継続的評価：モデル更新とドリフトの監督", "continuous-evaluation-drift.html", "Safety・評価", False),
    ("対外コミュニケーション：顧客・投資家・当局への説明設計", "external-communication-design.html", "戦略", False),
    # Phase2 #21-#40
    ("EU AI Act 総論：義務の全体像と段階適用の読み方", "eu-ai-act-overview.html", "規制", True),
    ("EU AI Act 透明性義務：通知・表示・情報提供の設計", "eu-ai-act-transparency.html", "規制", True),
    ("EU AI Act 高リスクAI：適合性評価・QMS・技術文書の実務", "eu-ai-act-high-risk.html", "規制", True),
    ("EU AI Act 禁止領域：禁止規定と設計上の回避策", "eu-ai-act-prohibited.html", "規制", True),
    ("域外適用（ブリュッセル効果）と本社責任：誰が何を担うか", "extra-territorial-brussels-effect.html", "規制", False),
    ("規制スプリンターネット：グローバル統制の設計原則", "regulatory-splinternet.html", "規制", False),
    ("規制ホライズンスキャン：追跡の仕組み化（Living運用）", "regulatory-horizon-scan.html", "規制", True),
    ("G7/OECD：広島AIプロセスの報告枠組みと企業対応", "g7-oecd-hiroshima-ai-reporting.html", "規制", True),
    ("日本：AI事業者ガイドラインの位置づけと企業実装（Living対応）", "japan-ai-guidelines.html", "規制", True),
    ("米国AI規制の全体像：連邦・州・業界の分散統治", "us-ai-regulation-overview.html", "規制", False),
    ("中国の生成AI規制：域内提供・モデル管理・留意点", "china-genai-regulation.html", "規制", False),
    ("英国・シンガポール等：ソフトロー型ガバナンスの実装比較", "uk-singapore-soft-law.html", "規制", False),
    ("AIリスクアセスメント：手法・粒度・記録（監査耐性）", "ai-risk-assessment-method.html", "リスク", False),
    ("AIリスクアペタイト：経営判断に落とすフレーム", "ai-risk-appetite-framework.html", "リスク", False),
    ("取締役会のAIガバナンス：議題テンプレと年間計画", "board-ai-governance-agenda.html", "体制", False),
    ("CxOの役割分担：CISO・法務・DPO・CDO・監査", "cxo-roles-ai-governance.html", "体制", False),
    ("中央集権 vs 連邦型：グローバル企業の最適解", "centralized-vs-federated.html", "体制", False),
    ("シャドウAI対策：禁止だけでなく正規ルートを作る", "shadow-ai-countermeasures.html", "体制", False),
    ("例外管理：現場スピードを落とさない統制", "exception-management-control.html", "運用OS", False),
    ("ガバナンス成熟度：自己評価と改善ロードマップ", "governance-maturity-roadmap.html", "体制", False),
    # Phase3 #41-#60
    ("内部監査が見るAI統制：評価観点と頻度", "internal-audit-ai-controls.html", "監査", False),
    ("外部監査の期待：企業が準備すべき証跡", "external-audit-expectations.html", "監査", False),
    ("AI保証（Assurance）と監査の違い：使い分け", "ai-assurance-vs-audit.html", "監査", False),
    ("監査証跡としてのログ：何を残せば足りるか", "audit-trail-logs.html", "監査", False),
    ("文書化と監査証跡：必要十分なアーティファクトとは", "documentation-audit-artifacts.html", "監査", False),
    ('Evidence Bundle：監査法人が欲しい"束ね方"', "evidence-bundle-audit.html", "運用OS", False),
    ("証跡の最小要件：何を残せば監査に耐えるか", "evidence-minimum-requirements.html", "運用OS", False),
    ("AI-BOM（モデル/データ/依存関係）：供給網透明性", "ai-bom-supply-chain.html", "運用OS", False),
    ("コントロールテストの自動化：継続的監査（CCM）", "control-test-automation-ccm.html", "運用OS", False),
    ("ルールのコード化（Compliance-as-Code）：設計パターン", "compliance-as-code.html", "運用OS", False),
    ("監査ダッシュボード：取締役会に刺さる指標", "audit-dashboard-board-metrics.html", "運用OS", False),
    ("AIインシデント対応：エスカレーションと当局/顧客説明", "ai-incident-response-escalation.html", "リスク", False),
    ("本番モニタリング：ドリフト・品質・リスクの検知", "production-monitoring-drift.html", "ライフサイクル", False),
    ("バージョン管理：変更時の再評価とロールバック", "version-management-reroll.html", "ライフサイクル", False),
    ("デプロイ前チェックリストとリリース承認", "deploy-checklist-release-approval.html", "ライフサイクル", False),
    ("AI調達（Buy/Build）：意思決定と統制", "ai-procurement-buy-build.html", "ライフサイクル", False),
    ("サードパーティAIベンダーリスク：評価観点と契約連動", "third-party-ai-vendor-risk.html", "リスク", False),
    ("学習データの権利処理：ライセンスと記録", "training-data-rights-licensing.html", "データ", False),
    ("機密情報：入力禁止だけで終わらせない設計", "confidential-input-design.html", "法務", False),
    ("翌年度計画：規制追随と改善サイクルの作り方", "next-year-planning-cycle.html", "運用OS", False),
    # Phase4 #61-#80
    ("AIとデータガバナンスの接点：統合設計の要点", "ai-data-governance-integration.html", "データ", False),
    ("GDPRと生成AI：学習データ・個人データ処理の論点整理", "gdpr-genai-personal-data.html", "データ", True),
    ("日本の個人情報保護×生成AI：実務で詰むポイント", "japan-pip-genai.html", "データ", False),
    ("合成データ：有効性とプライバシーリスク", "synthetic-data-privacy.html", "データ", False),
    ("データ品質（GIGO対策）：統制に落とす方法", "data-quality-gigo.html", "データ", False),
    ("データ保持期間：モデル廃止時の取り扱いと監査証跡", "data-retention-model-retirement.html", "データ", False),
    ("越境データ：法域差・データ主権の設計", "cross-border-data-sovereignty.html", "データ", False),
    ("PETs（プライバシー強化技術）：導入判断と統制", "pets-privacy-enhancing.html", "データ", False),
    ("DPIAとAIリスク：統合評価の進め方", "dpia-ai-risk-integration.html", "データ", False),
    ("監査証跡としてのデータ系アーティファクト：最低限セット", "data-artifacts-audit-trail.html", "データ", False),
    ("AI生成物の著作権：企業リスクの現実解", "ai-output-copyright.html", "法務", False),
    ("学習データの著作権・利用許諾：整理の型", "training-data-copyright-licensing.html", "法務", False),
    ("AIベンダー契約：必須条項（監査権・透明性・責任分担）", "ai-vendor-contract-clauses.html", "法務", False),
    ("責任分担と免責の限界：事故時の落としどころ", "liability-disclaimer-limits.html", "法務", False),
    ("特許・知財とAI開発：ガバナンスの要点", "ip-patent-ai-development.html", "法務", False),
    ("クラウドAI利用時の契約：データ主権・監査対応", "cloud-ai-contract-data-sovereignty.html", "法務", False),
    ("越境データ契約：法域ごとの契約設計", "cross-border-data-contract.html", "法務", False),
    ("紛争時の証拠：ログと文書の証明力（eDiscovery含む）", "dispute-evidence-log-document.html", "法務", False),
    ("法務部門とガバナンス体制：三線防御の接続", "legal-governance-three-lines.html", "法務", False),
    ("サードパーティ契約更新：規制変化（Living）を織り込む条項", "vendor-contract-living-clauses.html", "法務", True),
    # Phase5 #81-#100
    ("AI×サイバー：脅威モデルの作り方", "ai-cyber-threat-model.html", "セキュリティ", False),
    ("AIアクセス制御：ゼロトラストでどう守るか", "ai-access-control-zerotrust.html", "セキュリティ", False),
    ("プロンプトインジェクション：統制（人/ルール/技術）の分担", "prompt-injection-control.html", "セキュリティ", False),
    ("データ漏えい：入力・出力・ログの統制設計", "data-leakage-control-design.html", "セキュリティ", False),
    ("モデル改ざん・毒入れ：検知と防止の実装", "model-poisoning-detection.html", "セキュリティ", False),
    ("サプライチェーンセキュリティ：AIで増幅する論点", "supply-chain-security-ai.html", "セキュリティ", False),
    ("事業継続（BCP）：AI依存リスクとフェイルセーフ", "bcp-ai-dependency-failsafe.html", "セキュリティ", False),
    ("インシデント対応：AIの切り離し手順と説明責任", "incident-response-ai-isolation.html", "セキュリティ", False),
    ("セキュリティKRI：監視・アラートの設計", "security-kri-monitoring.html", "セキュリティ", False),
    ("セキュリティ評価：ベンダー/オープンモデル採用時の要件", "security-eval-vendor-open-model.html", "セキュリティ", False),
    ("AI-BOM（モデル/データ/依存関係）：供給網透明性の実装", "ai-bom-implementation.html", "運用OS", False),
    ("SBOMとの統合：既存セキュリティ運用に繋ぐ", "sbom-integration-security.html", "セキュリティ", False),
    ("社内DLP/IdP/CASB連携：最小開発で守る設計", "dlp-idp-casb-design.html", "セキュリティ", False),
    ("ログ保全：真正性（改ざん耐性）と保管要件", "log-integrity-retention.html", "セキュリティ", False),
    ("監査法人が見るAIセキュリティ：指摘になりやすい点", "auditor-ai-security-findings.html", "監査", False),
    ("倫理×セキュリティ：統合統制の作り方", "ethics-security-unified-control.html", "セキュリティ", False),
    ("セキュリティ教育：現場が守れるルール化", "security-education-rules.html", "セキュリティ", False),
    ("生成AI利用のRed Line：機密・個人・規制産業の境界", "genai-red-line-boundaries.html", "セキュリティ", False),
    ("セキュリティ投資ROI：損失回避の定量化", "security-investment-roi.html", "セキュリティ", False),
    ("年次計画：翌年度の重点（監査×セキュリティ×規制）", "annual-plan-focus-areas.html", "運用OS", False),
    # Phase6 #101-#120
    ("ISO/IEC 42001（AIMS）導入の要点と落とし穴", "iso-42001-aims-introduction.html", "標準", False),
    ("NIST AI RMF：企業ガバナンスへの落とし込み", "nist-ai-rmf-implementation.html", "標準", False),
    ("OECD AI原則：企業ポリシーへ翻訳する方法", "oecd-ai-principles-policy.html", "標準", False),
    ("IEEE等の国際標準動向：企業が追うべき範囲", "ieee-international-standards.html", "標準", False),
    ("モデルカード・データシート：監査証跡としての実務", "model-card-datasheet-audit.html", "標準", False),
    ("複数フレームワーク統合：重複排除と優先順位", "multi-framework-integration.html", "標準", False),
    ("ガバナンス文書のバージョン管理：公開と内部統制の両立", "governance-doc-version-control.html", "運用OS", False),
    ("規制ホライズンスキャン：運用の型（四半期更新）", "regulatory-horizon-scan-ops.html", "規制", True),
    ("取締役会のAIアジェンダ：議題例と報告指標", "board-ai-agenda-metrics.html", "体制", False),
    ("AI倫理/ガバナンス委員会：形骸化を防ぐ設計", "ai-ethics-committee-design.html", "倫理", False),
    ("CxOの役割分担：CISO・法務・DPO・CDO・監査", "cxo-roles-summary.html", "体制", False),
    ("中央集権 vs 連邦型：グローバル企業の最適解", "centralized-federated-global.html", "体制", False),
    ("グローバルベースラインとローカル適応：二層統制", "global-baseline-local-adaptation.html", "体制", False),
    ("ユースケース承認プロセス：閾値と例外管理", "use-case-approval-process.html", "体制", False),
    ("ガバナンス成熟度モデル：自己評価と改善ロードマップ", "governance-maturity-model.html", "体制", False),
    ("子会社・中小向け軽量ガバナンス：ミニマム統制", "subsidiary-sme-lightweight-governance.html", "体制", False),
    ("変更管理：導入時の抵抗と対処", "change-management-resistance.html", "戦略", False),
    ("インセンティブ設計：スピードと統制の両立", "incentive-design-speed-control.html", "戦略", False),
    ("ガバナンス人材：必要ロール（LLMOps/監査/法務）", "governance-talent-roles.html", "戦略", False),
    ("ガバナンス投資のROI：経営報告の型", "governance-investment-roi.html", "戦略", False),
    # Phase7 #121-#140
    ("金融業界：AIガバナンス（規制×MRM×説明責任）", "industry-finance-ai-governance.html", "業界", False),
    ("保険業界：引受・不正検知・顧客説明の統制", "industry-insurance-underwriting.html", "業界", False),
    ("医療・ヘルスケア：規制・倫理・安全性評価", "industry-healthcare-regulation.html", "業界", False),
    ("医薬品・ライフサイエンス：研究AIと規制の接点", "industry-pharma-life-science.html", "業界", False),
    ("製造業：品質・安全・サプライチェーンAI", "industry-manufacturing-quality.html", "業界", False),
    ("小売・EC：顧客データ・レコメンドの統制", "industry-retail-ec-recommendation.html", "業界", False),
    ("公共セクター：透明性と説明責任の設計", "industry-public-sector.html", "業界", False),
    ("人事・採用AI：差別防止と監査可能性", "industry-hr-recruitment-ai.html", "業界", False),
    ("マーケティング・広告AI：透明性・消費者保護", "industry-marketing-ad-ai.html", "業界", False),
    ("自動車・モビリティ：安全規格とAI（ソフト更新含む）", "industry-automotive-mobility.html", "業界", False),
    ("業界別AI監査：注目点の違い（横断まとめ）", "industry-ai-audit-comparison.html", "業界", False),
    ("業界別リスク比較：ヒートマップで見る共通/固有リスク", "industry-risk-heatmap.html", "業界", False),
    ("業界別KRI：最小セットと閾値", "industry-kri-minimum-set.html", "業界", False),
    ("外部委託（BPO/SI）とAI：責任分担と証跡", "outsourcing-bpo-si-ai.html", "業界", False),
    ("データ共有（共同研究/共同開発）：契約と統制", "data-sharing-joint-research.html", "データ", False),
    ("顧客提供AI（B2B）：SLA・説明・監査要求への対応", "customer-facing-ai-b2b.html", "業界", False),
    ("社内利用AI（B2E）：シャドウAI対策と普及の両立", "internal-ai-b2e-shadow.html", "業界", False),
    ("監督当局対応：業界規制との整合を作る", "supervisor-authority-alignment.html", "業界", False),
    ('インシデント対応：業界別の"報告/説明"の癖', "incident-response-by-industry.html", "業界", False),
    ("業界別テンプレ：最短で整備する統制パッケージ", "industry-templates-control-package.html", "業界", False),
    # Phase8 #141-#160
    ("AI倫理原則の採用：企業方針へ落とす方法", "ai-ethics-principles-policy.html", "倫理", False),
    ("バイアスと公平性：人事・与信・医療での実務", "bias-fairness-hr-credit-healthcare.html", "倫理", False),
    ("説明可能性（XAI）：どこまで求めるべきか", "xai-explainability-scope.html", "倫理", False),
    ("人間の監督（Human-in-the-loop）：設計と証跡化", "human-in-the-loop-design.html", "倫理", False),
    ("アカウンタビリティ：誰が責任を負うか（事故時設計）", "accountability-incident-design.html", "倫理", False),
    ("サステナビリティ：環境負荷とAIガバナンス", "sustainability-environmental-ai.html", "倫理", False),
    ("労働者・消費者保護：生成AIの境界線", "worker-consumer-protection-genai.html", "倫理", False),
    ('倫理リスクのモニタリング：是正の"回し方"', "ethics-risk-monitoring-remediation.html", "倫理", False),
    ("レピュテーションリスク：炎上パターンと予防線", "reputation-risk-prevention.html", "リスク", False),
    ("AIインシデント報告：当局通知・顧客説明の実務", "ai-incident-reporting-authority.html", "リスク", False),
    ("AIライフサイクル俯瞰：企画〜廃止までの統制", "ai-lifecycle-overview.html", "ライフサイクル", False),
    ("開発フェーズ統制：要件・設計・検証の最小証跡", "development-phase-control.html", "ライフサイクル", False),
    ("AI調達（Buy/Build）：意思決定と統制", "ai-procurement-decision-control.html", "ライフサイクル", False),
    ("廃止・停止：記録保持とリスクの終端処理", "decommission-record-risk.html", "ライフサイクル", False),
    ("継続的適合性評価：監査対応を運用に組み込む", "continuous-conformity-assessment.html", "運用OS", False),
    ("ガバナンスの継続的改善：監査→改善→再評価の循環", "governance-continuous-improvement.html", "運用OS", False),
    ("攻めのガバナンス：信頼獲得と競争優位", "offensive-governance-trust.html", "戦略", False),
    ("次世代規制を見据えた準備：拡張可能な統制設計", "next-gen-regulation-preparation.html", "戦略", False),
    ('"ガバナンス運用OS"総まとめ：最短導入ロードマップ', "governance-os-summary-roadmap.html", "運用OS", False),
    ("次年度計画：規制追随・人材・投資の優先順位（総括）", "next-year-plan-priority-summary.html", "運用OS", False),
]

# フル記事 = 既存2本 + テンプレート展開153本（indexでMermaid・カードを記事ごとに多様化）
ARTICLES = ARTICLES + [make_template_article(*s, index=i) for i, s in enumerate(SHORT_LIST)]

def build_body_html(article):
    (title, slug, category, living, lead, sections, kp_title, kp_text, meta,
     mermaid_chart, card_caption, card_left_title, card_left_items, card_right_title, card_right_items) = article[:15]
    references = article[15] if len(article) >= 16 else _get_references_for(category)
    cat_style = CATEGORY_STYLES.get(category, "bg-slate-100 text-slate-800")
    liv_badge = '<span className="bg-amber-50 text-amber-700 text-xs px-3 py-1 rounded-full font-bold tracking-wide">Living</span>' if living else ""
    summary_section = None
    if sections and sections[-1][0] == "まとめ":
        summary_section = sections[-1]
        sections = sections[:-1]
    body_parts = [f'<p className="lead text-xl text-slate-600 mb-10 leading-relaxed font-medium">\n{escape_html(lead)}\n</p>']
    for i, (h2, paras) in enumerate(sections):
        body_parts.append(f'<h2>{escape_html(h2)}</h2>')
        for p in paras:
            body_parts.append(f'<p>{escape_html(p)}</p>')
        if i == 0:
            body_parts.append("__MERMAID__")
        elif i == 1:
            body_parts.append("__CARD__")
    body_content = "\n                                ".join(body_parts)
    summary_html = ""
    if summary_section:
        _, summary_paras = summary_section
        summary_html = "\n                            ".join(
            ['<h2>まとめ</h2>'] + [f'<p>{escape_html(p)}</p>' for p in summary_paras]
        )
    # 参考・参照セクション（計画書4.3：公式リンク2〜4本）
    refs_li = "\n                                ".join(
        f'<li><a href="{escape_attr(url)}" target="_blank" rel="noopener noreferrer" className="text-brand-blue hover:underline">{escape_html(label)}</a></li>'
        for label, url in references
    )
    refs_section = f'\n                            <h2>参考・参照</h2>\n                            <ul className="list-disc pl-6 space-y-2 text-slate-700">\n                                {refs_li}\n                            </ul>'
    # カードJSX（計画書・サンプル記事のfigure/figcaption＋2列カード形式に準拠）
    left_lis = "\n".join("                            <li>" + escape_html(item) + "</li>" for item in card_left_items)
    right_lis = "\n".join("                            <li>" + escape_html(item) + "</li>" for item in card_right_items)
    card_jsx = f'''<figure className="my-10 p-6 bg-white rounded-xl shadow-sm border border-slate-100 not-prose max-w-4xl mx-auto">
                <figcaption className="text-lg font-bold mb-6 text-slate-800 text-center">{escape_html(card_caption)}</figcaption>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 overflow-x-auto">
                    <div className="bg-slate-50 p-4 rounded-lg border border-slate-200">
                        <h5 className="font-bold text-slate-700 mb-3 flex items-center gap-2"><Icon name="List" size={18} /> {escape_html(card_left_title)}</h5>
                        <ul className="text-sm text-slate-700 space-y-1.5">
{left_lis}
                        </ul>
                    </div>
                    <div className="bg-blue-50 p-4 rounded-lg border border-brand-blue/30">
                        <h5 className="font-bold text-brand-blue mb-3 flex items-center gap-2"><Icon name="CheckCircle" size={18} /> {escape_html(card_right_title)}</h5>
                        <ul className="text-sm text-slate-700 space-y-1.5">
{right_lis}
                        </ul>
                    </div>
                </div>
            </figure>'''
    return body_content, summary_html, cat_style, liv_badge, mermaid_chart, card_jsx, refs_section

def escape_js_template(s):
    """JavaScript テンプレートリテラル内に埋め込むためのエスケープ（\\ と `）"""
    if not s:
        return ""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

def render_article(article):
    title, slug, category, living, lead, sections, kp_title, kp_text, meta = article[:9]
    mermaid_chart, card_caption, card_left_title, card_left_items, card_right_title, card_right_items = article[9:15]
    body_content, summary_html, cat_style, liv_badge, mermaid_chart_out, card_jsx, refs_section = build_body_html(article)
    safe_title = escape_attr(title)
    kp_part = f'<KeyPoint title="{escape_attr(kp_title)}">\n                {escape_html(kp_text)}\n            </KeyPoint>'
    mermaid_escaped = escape_js_template(mermaid_chart_out)
    body_final = body_content.replace("__MERMAID__", "<MermaidDiagram chart={mermaidChart} />").replace("__CARD__", card_jsx)

    # Coworkショック3本はCTAにAIMOaaSへのリンクを追加
    if slug in COWORK_SLUGS_FOR_AIMOaaS_CTA:
        cta_block = f'''<div className="not-prose mt-20 p-10 bg-slate-900 rounded-2xl text-center relative overflow-hidden">
                            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-brand-blue to-cyan-500"></div>
                            <h3 className="text-2xl font-bold text-white mb-4">AIガバナンスの設計・実装支援</h3>
                            <p className="text-slate-300 mb-8 max-w-2xl mx-auto text-sm leading-relaxed">利用規程、評価・透明性の設計から監査証跡まで、一気通貫でサポートします。AIMOaaSでガバナンス運用を効率化。</p>
                            <div className="flex flex-wrap justify-center gap-4">
                                <a href="{escape_attr(AIMOaaS_URL)}" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 bg-brand-blue text-white px-8 py-3 rounded-full font-bold hover:bg-white hover:text-brand-blue transition-all">AIMOaaSをみる</a>
                                <a href="mailto:contact@riseby.net" className="inline-flex items-center gap-2 border-2 border-white text-white px-8 py-3 rounded-full font-bold hover:bg-white hover:text-slate-900 transition-all"><Icon name="Mail" size={18} /> お問い合わせ</a>
                            </div>
                        </div>'''
    else:
        cta_block = '''<div className="not-prose mt-20 p-10 bg-slate-900 rounded-2xl text-center relative overflow-hidden">
                            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-brand-blue to-cyan-500"></div>
                            <h3 className="text-2xl font-bold text-white mb-4">AIガバナンスの設計・実装支援</h3>
                            <p className="text-slate-300 mb-8 max-w-2xl mx-auto text-sm leading-relaxed">利用規程、評価・透明性の設計から監査証跡まで、一気通貫でサポートします。</p>
                            <a href="mailto:contact@riseby.net" className="inline-flex items-center justify-center gap-2 bg-brand-blue text-white px-8 py-3 rounded-full font-bold hover:bg-white hover:text-brand-blue transition-all"><Icon name="Mail" size={18} /> お問い合わせ</a>
                        </div>'''

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="canonical" href="{BASE_URL}/{slug}">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="RISEby inc.">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="{BASE_URL}/{slug}">
    <meta property="og:title" content="{safe_title} | RISEby Blog">
    <meta property="og:description" content="{escape_attr(meta)}">
    <meta property="og:image" content="https://riseby.net/assets/images/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <title>{safe_title} | RISEby Blog</title>
    <meta name="description" content="{escape_attr(meta)}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script>tailwind.config = {{ theme: {{ extend: {{ colors: {{ brand: {{ blue: '#003E68', red: '#ED1C24', dark: '#0B0F19' }} }}, fontFamily: {{ sans: ['\"Noto Sans JP\"', 'sans-serif'], display: ['\"Montserrat\"', 'sans-serif'] }} }} }} }}</script>
    <style>body {{ font-family: "Noto Sans JP", sans-serif; }}
    .mermaid {{ display: flex; justify-content: center; margin: 2rem 0; background: #f8fafc; padding: 1rem; border-radius: 0.5rem; }}
    .mermaid svg {{ max-width: 100%; }}
    .mermaid svg text {{ font-size: 1.125rem !important; }}
    .mermaid .nodeLabel, .mermaid .edgeLabel {{ font-size: 1.125rem !important; }}</style>
    <script type="application/ld+json">{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{escape_attr(title)}","datePublished":"{ARTICLE_PUBLISH_DATE}","author":{{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net"}}}}</script>
</head>
<body class="bg-slate-50 text-slate-800">
    <div id="root"></div>
    <script type="text/babel">
        const {{ useState, useEffect }} = React;
        const Icon = ({{ name, size = 24, className = "" }}) => {{
            if (typeof lucide !== 'undefined' && lucide.icons && lucide.icons[name])
                return React.createElement('svg', {{ xmlns: "http://www.w3.org/2000/svg", width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: 2, strokeLinecap: "round", strokeLinejoin: "round", className }}, lucide.icons[name].map(([tag, attrs], i) => React.createElement(tag, {{ ...attrs, key: i }})));
            return <span className="inline-block w-4 h-4 bg-gray-300 rounded-full"></span>;
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
                            <p className="text-slate-400 text-sm mb-8">企業の複合的な経営課題を、AI・戦略・テクノロジー・人の観点から包括的に解決するコンサルティングファーム。</p>
                            <div className="mb-10 text-sm text-slate-400 space-y-3">
                                <p>〒150-6115 東京都渋谷区渋谷2-24-12</p>
                                <p>渋谷スクランブルスクエア 15階</p>
                                <a href="mailto:contact@riseby.net" className="hover:text-white flex items-center gap-2 mt-6 group"><span className="bg-slate-800 p-2 rounded-full group-hover:bg-slate-700"><Icon name="Mail" size={{16}} /></span>contact@riseby.net</a>
                            </div>
                            <p className="text-slate-600 text-xs">&copy; {{new Date().getFullYear()}} RISEby Inc.</p>
                        </div>
                        <div className="lg:w-2/3 grid grid-cols-2 md:grid-cols-3 gap-8">
                            <div><h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">Services</h3>
                                <ul className="space-y-3"><li><a href="../../index.html#services" className="text-slate-400 hover:text-white text-xs">サービス一覧</a></li><li><a href="../../index.html" className="text-slate-400 hover:text-white text-xs">新規事業開発</a></li><li><a href="../../index.html" className="text-slate-400 hover:text-white text-xs">DXコンサルティング</a></li></ul></div>
                            <div><h3 className="font-bold text-sm mb-5 text-white tracking-wider font-display">Company</h3>
                                <ul className="space-y-3"><li><a href="../../about.html" className="text-slate-400 hover:text-white text-xs">会社概要</a></li><li><a href="../index.html" className="text-slate-400 hover:text-white text-xs">ブログ</a></li><li><a href="mailto:contact@riseby.net" className="text-slate-400 hover:text-white text-xs">お問い合わせ</a></li></ul></div>
                        </div>
                    </div>
                    <div className="border-t border-slate-800 pt-10 flex flex-wrap gap-8 justify-center text-xs text-slate-500">
                        <a href="../../about.html" className="hover:text-white">会社概要</a><a href="../../privacy.html" className="hover:text-white">プライバシーポリシー</a>
                    </div>
                </div>
            </footer>
        );
        const MermaidDiagram = ({{ chart }}) => {{
            useEffect(() => {{ if (typeof mermaid !== 'undefined') {{ mermaid.initialize({{ theme: 'base', themeVariables: {{ fontSize: '18px', primaryTextColor: '#334155', primaryFontSize: '18px' }} }}); mermaid.init(); }} }}, []);
            return <div className="mermaid overflow-x-auto max-w-4xl mx-auto text-lg">{{chart}}</div>;
        }};
        const KeyPoint = ({{ title, children }}) => (
            <div className="my-8 bg-blue-50 border-l-4 border-brand-blue p-6 rounded-r-lg not-prose">
                <h5 className="font-bold text-brand-blue mb-2 flex items-center gap-2"><Icon name="Lightbulb" size={{20}} />{{title || "Key Point"}}</h5>
                <div className="text-slate-700 text-sm leading-relaxed">{{children}}</div>
            </div>
        );
        const mermaidChart = `{mermaid_escaped}`;
        const BlogArticle = () => (
            <main className="pt-24 pb-16">
                <article className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-100">
                        <header className="text-center mb-12 border-b border-slate-100 pb-10">
                            <div className="flex justify-center flex-wrap gap-2 mb-4">
                                <span className="{cat_style} text-xs px-3 py-1 rounded-full font-bold tracking-wide uppercase font-display">{escape_html(category)}</span>
                                <span className="bg-slate-100 text-slate-600 text-xs px-3 py-1 rounded-full font-bold tracking-wide">実装向け</span>
                                {liv_badge}
                            </div>
                            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-6 leading-tight">{escape_html(title)}</h1>
                            <div className="flex items-center justify-center space-x-4 text-sm text-slate-500">
                                <time dateTime="{ARTICLE_PUBLISH_DATE}">{ARTICLE_PUBLISH_DATE.replace("-", ".")}</time><span>&middot;</span>
                                <span className="flex items-center gap-1"><Icon name="User" size={{14}} /> RISEby Editorial Team</span>
                            </div>
                        </header>
                        <div className="prose prose-lg prose-slate prose-headings:font-bold prose-a:text-brand-blue hover:prose-a:text-blue-500 mx-auto">
                                {body_final}
                                {kp_part}
                                {refs_section}
                                {summary_html}
                        </div>
                        {cta_block}
                    </div>
                </article>
            </main>
        );
        const App = () => <div className="min-h-screen flex flex-col font-sans bg-slate-50 text-slate-800"><Header /><BlogArticle /><Footer /></div>;
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

# index.html 用カテゴリ色（span class）
CATEGORY_INDEX_COLOR = {
    "規制": "rose", "リスク": "orange", "倫理": "indigo", "体制": "emerald", "ライフサイクル": "sky",
    "データ": "teal", "監査": "purple", "業界": "pink", "標準": "slate", "戦略": "lime", "法務": "amber",
    "セキュリティ": "red", "生成AI・GPAI": "violet", "Safety・評価": "amber", "透明性・真正性": "cyan", "運用OS": "blue",
}

def build_index_cards():
    """155本分の index カードHTMLを返す（既存5本の後ろに挿入する用）"""
    lines = []
    for article in ARTICLES:
        title, slug, category, living, lead, sections, kp_title, kp_text, meta = article[:9]
        color = CATEGORY_INDEX_COLOR.get(category, "slate")
        liv = ' <span class="text-xs text-amber-600 font-medium ml-2">Living</span>' if living else ""
        title_esc = escape_html(title)
        meta_esc = escape_html(meta)
        lines.append(f'''          <a href="./{slug}" class="group bg-white rounded-xl shadow-md hover:shadow-lg transition-all overflow-hidden">
            <div class="p-6">
              <span class="text-xs text-{color}-600 font-medium">{escape_html(category)}</span>{liv}
              <h3 class="text-lg font-bold text-gray-900 mt-2 group-hover:text-navy transition">{title_esc}</h3>
              <p class="text-gray-600 text-sm mt-3 line-clamp-3">{meta_esc}</p>
            </div>
          </a>''')
    return "\n\n".join(lines)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for article in ARTICLES:
        slug = article[1]
        html = render_article(article)
        out_path = OUTPUT_DIR / slug
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Wrote {out_path.name}")
    # index.html に155本のカードを追加
    index_path = OUTPUT_DIR / "index.html"
    index_content = index_path.read_text(encoding="utf-8")
    new_cards = build_index_cards()
    old_grid_end = """          <a href="./transparency-accountability.html" class="group bg-white rounded-xl shadow-md hover:shadow-lg transition-all overflow-hidden">
            <div class="p-6">
              <span class="text-xs text-indigo-600 font-medium">倫理</span>
              <h3 class="text-lg font-bold text-gray-900 mt-2 group-hover:text-navy transition">透明性義務：AI利用の開示と説明責任（顧客・規制・監査）</h3>
              <p class="text-gray-600 text-sm mt-3 line-clamp-3">顧客・規制・監査のそれぞれに説明責任を果たす開示設計。何を誰にどう開示し、証跡をどう残すかを整理します。</p>
            </div>
          </a>

        </div>"""
    new_grid_end = """          <a href="./transparency-accountability.html" class="group bg-white rounded-xl shadow-md hover:shadow-lg transition-all overflow-hidden">
            <div class="p-6">
              <span class="text-xs text-indigo-600 font-medium">倫理</span>
              <h3 class="text-lg font-bold text-gray-900 mt-2 group-hover:text-navy transition">透明性義務：AI利用の開示と説明責任（顧客・規制・監査）</h3>
              <p class="text-gray-600 text-sm mt-3 line-clamp-3">顧客・規制・監査のそれぞれに説明責任を果たす開示設計。何を誰にどう開示し、証跡をどう残すかを整理します。</p>
            </div>
          </a>

""" + new_cards + """

        </div>"""
    if old_grid_end in index_content:
        index_content = index_content.replace(old_grid_end, new_grid_end, 1)
        index_path.write_text(index_content, encoding="utf-8")
        print("Updated index.html with 155 article cards.")
    else:
        print("Warning: index.html pattern not found; skipping index update.")
    print(f"Done. Generated {len(ARTICLES)} articles.")

if __name__ == "__main__":
    main()
