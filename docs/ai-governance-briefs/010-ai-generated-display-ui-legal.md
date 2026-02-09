# 記事執筆ブリーフ（全情報）

## CRITICAL：この記事の固定値（設計図3.3の該当行）

- **No.**: 10 / 163
- **slug**: ai-generated-display-ui-legal
- **title_ja**: AI生成コンテンツのUI表示と誤認防止
- **template_id**: T32
- **unique_focus**: “UI表示の具体（誤認防止）”に特化
- **対象読者**: Pract（Exec=経営層 / Pract=実務 / Audit=監査 / Legal=法務・コンプラ / Multi=複数）
- **目的**: Impl（Decide=意思決定 / Impl=実装 / Understand=理解 / Audit=監査対応 / Navigate=方向探索）
- **深さ**: Quick（Overview=1,500–2,000語 / Deep=2,500–3,500語 / Quick=800–1,200語）
- **スタイル**: Prescriptive（Narrative=物語調 / Analytical=分析調 / Prescriptive=処方箋調 / Comparative=比較調）
- **冒頭パターン（Op）**: 10 — 失敗から学ぶ
  - 例: 「なぜ多くの企業でAIガバナンスが『お飾り』化するのか」
- **結論パターン（Co）**: 5 — 進化の視点
  - 例: 「今日の『ベストプラクティス』は明日の『最低要件』になる」

---

## テンプレ（設計図セクション2）— 必須セクション・書くべきポイント

### Points（書くべきポイント）
generated/edited分類、UI表示、watermark/metadataの限界、deepfake対策

### Infographics（使うべきインフォグラフィック3種の「型」）
1) マトリクス（コンテンツ×義務） 2) フロー（公開前チェック） 3) 差し戻しTop5
上記をこの記事の図1・図2・図3の**推奨型**とする。直前3記事と重複しなければ推奨を優先すること。

### Outline（必須セクション見出し。順序・厚さは記事DNAに応じて調整可）
なぜ今→要求→運用→証跡

> ※テンプレは必要に応じて追加してよいが、まずは T01〜T32 で163件を必ず割当てる。

---

## 3. 記事→テンプレ割当（163件 + カテゴリトップ）

> 形式：No. URL — TemplateID — 記事固有の **unique_focus**（1行）  
> （差分ポイントは「その記事だけの焦点」を決め、同一化を防ぐ）


| No. | URL | Template | unique_focus |
|-----|-----|----------|--------------|
| TOP | https://riseby.net/blog/ai-governance/index.html | T02 | “読む順（90日）”と“最小要件の1枚図”を追加 |


| No. | slug | template_id | unique_focus |
|-----|------|-------------|--------------|
| 1 | accountability-incident-design | T08 | “Accountability＝誰が何を証明するか”に特化 |
| 2 | ai-access-control-zerotrust | T21 | “Zero TrustをAI利用申請へ翻訳”に特化 |
| 3 | ai-assurance-vs-audit | T08 | “Assuranceの限界と証憑の形”に特化 |
| 4 | ai-bom-implementation | T25 | “AI-BOM実装手順（90日）”に特化 |
| 5 | ai-bom-supply-chain | T25 | “供給網の責任分界”に特化 |
| 6 | ai-cyber-threat-model | T23 | “脅威分類の優先順位付け”に特化 |
| 7 | ai-data-governance-integration | T26 | “データ統制とAI統制の接合点”に特化 |
| 8 | ai-ethics-committee-design | T11 | “委員会が形骸化しない設計”に特化 |
| 9 | ai-ethics-principles-policy | T01 | “理念→手続きへ変換”に特化 |
| 10 | ai-generated-display-ui-legal | T32 | “UI表示の具体（誤認防止）”に特化 |
| 11 | ai-incident-reporting-authority | T01 | “当局報告の責任分界”に特化 |
| 12 | ai-incident-response-escalation | T13 | “エスカレーション閾値”に特化 |
| 13 | ai-lifecycle-overview | T14 | “ライフサイクルに評価ゲートを埋め込む”に特化 |
| 14 | ai-output-copyright | T31 | “出力物の権利・責任”に特化 |
| 15 | ai-procurement-buy-build | T25 | “Buy/Build判断の評価軸”に特化 |
| 16 | ai-procurement-decision-control | T25 | “調達審査ゲート（RACI）”に特化 |
| 17 | ai-risk-appetite-framework | T06 | “レッドライン定義”に特化 |
| 18 | ai-risk-assessment-method | T07 | “定性/定量の使い分け”に特化 |
| 19 | ai-vendor-contract-clauses | T25 | “契約条項チェックリスト”に特化 |
| 20 | annual-plan-focus-areas | T04 | “年次優先5領域”に特化 |
| 21 | audit-dashboard-board-metrics | T20 | “取締役会向け最小KRI”に特化 |
| 22 | audit-trail-logs | T16 | “ログ完全性/保持”に特化 |
| 23 | auditor-ai-security-findings | T09 | “監査所見→是正テンプレ”に特化 |
| 24 | bcp-ai-dependency-failsafe | T15 | “停止/代替手段/復旧”に特化 |
| 25 | bias-evaluation-qualitative-quantitative | T07 | “バイアス評価の手法選択”に特化 |
| 26 | bias-fairness-hr-credit-healthcare | T07 | “領域別の公平性論点”に特化 |
| 27 | board-ai-agenda-metrics | T02 | “ボード指標の最小セット”に特化 |
| 28 | board-ai-governance-agenda | T02 | “議題テンプレ（毎四半期）”に特化 |
| 29 | centralized-federated-global | T03 | “グローバル運用の抜け穴”に特化 |
| 30 | centralized-vs-federated | T03 | “集中/分散の意思決定基準”に特化 |
| 31 | change-management-resistance | T05 | “抵抗の類型と対処”に特化 |
| 32 | china-genai-regulation | T26 | “中国規制の運用影響（断定回避）”に特化 |
| 33 | cloud-ai-contract-data-sovereignty | T29 | “クラウド契約×主権”に特化 |
| 34 | compliance-as-code | T05 | “規程のコード化”に特化 |
| 35 | confidential-input-design | T22 | “機密入力の境界設計”に特化 |
| 36 | content-transparency-why-now | T32 | “なぜ今（誤情報/深層偽造）”に特化 |
| 37 | continuous-conformity-assessment | T10 | “適合性評価の継続運用”に特化 |
| 38 | continuous-evaluation-drift | T14 | “ドリフト検知→是正”に特化 |
| 39 | control-test-automation-ccm | T10 | “CCM自動化の最小実装”に特化 |
| 40 | cross-border-data-contract | T29 | “契約条項の最小セット”に特化 |
| 41 | cross-border-data-sovereignty | T29 | “法域マトリクス”に特化 |
| 42 | customer-facing-ai-b2b | T13 | “対外AIの例外/承認”に特化 |
| 43 | cxo-roles-ai-governance | T02 | “CXO役割分担（RACI）”に特化 |
| 44 | cxo-roles-summary | T02 | “要点1枚化”に特化 |
| 45 | data-artifacts-audit-trail | T16 | “データ成果物＝監査証跡”に特化 |
| 46 | data-leakage-control-design | T22 | “漏えい統制の設計パターン”に特化 |
| 47 | data-quality-gigo | T28 | “品質KRIと閾値”に特化 |
| 48 | data-retention-model-retirement | T15 | “保持と退役の整合”に特化 |
| 49 | data-sharing-joint-research | T29 | “共同研究の責任分界”に特化 |
| 50 | decommission-record-risk | T15 | “退役時のリスク記録”に特化 |
| 51 | deepfake-countermeasures | T32 | “deepfake対策の運用ゲート”に特化 |
| 52 | deploy-checklist-release-approval | T12 | “リリース承認チェックリスト”に特化 |
| 53 | development-phase-control | T11 | “開発統制の必須点”に特化 |
| 54 | dispute-evidence-log-document | T19 | “争点化の証拠欠落”に特化 |
| 55 | dlp-idp-casb-design | T22 | “ツール設計（DLP/IDP/CASB）”に特化 |
| 56 | documentation-audit-artifacts | T17 | “監査成果物の目次”に特化 |
| 57 | dpia-ai-risk-integration | T07 | “DPIA統合の手順”に特化 |
| 58 | ethics-risk-monitoring-remediation | T10 | “倫理リスクの継続改善”に特化 |
| 59 | ethics-security-unified-control | T01 | “倫理×セキュリティ統制統合”に特化 |
| 60 | eu-ai-act-high-risk | T26 | “高リスクの運用要件（断定回避）”に特化 |
| 61 | eu-ai-act-overview | T26 | “全体像→実装の導線”に特化 |
| 62 | eu-ai-act-prohibited | T26 | “禁止類型の整理（マトリクス）”に特化 |
| 63 | eu-ai-act-transparency | T32 | “透明性表示の実装”に特化 |
| 64 | eval-automation-cicd | T14 | “CI/CD統合”に特化 |
| 65 | evals-basics | T14 | “評価の最小セット”に特化 |
| 66 | evidence-bundle-audit | T18 | “監査提出の形”に特化 |
| 67 | evidence-minimum-requirements | T17 | “最小要件”に特化 |
| 68 | exception-management-control | T13 | “例外管理の設計”に特化 |
| 69 | external-audit-expectations | T09 | “外部監査の期待”に特化 |
| 70 | external-communication-design | T32 | “外部説明の設計”に特化 |
| 71 | extra-territorial-brussels-effect | T26 | “域外適用の運用影響”に特化 |
| 72 | g7-oecd-hiroshima-ai-reporting | T02 | “報告の運用（ボード向け）”に特化 |
| 73 | gdpr-genai-personal-data | T26 | “個人データ論点”に特化 |
| 74 | genai-red-line-boundaries | T06 | “レッドライン（禁止境界）”に特化 |
| 75 | generated-edited-classification-taxonomy | T32 | “分類タクソノミー”に特化 |
| 76 | global-baseline-local-adaptation | T03 | “グローバル基準×ローカル”に特化 |
| 77 | governance-continuous-improvement | T10 | “継続改善ループ”に特化 |
| 78 | governance-doc-version-control | T05 | “規程の版管理”に特化 |
| 79 | governance-investment-roi | T04 | “ROIの測り方”に特化 |
| 80 | governance-maturity-model | T04 | “成熟度モデル”に特化 |
| 81 | governance-maturity-roadmap | T04 | “ロードマップ（90日）”に特化 |
| 82 | governance-os-summary-roadmap | T02 | “OS全体の要約”に特化 |
| 83 | governance-talent-roles | T04 | “人材・役割設計”に特化 |
| 84 | gpai-llm-governance-overview | T27 | “GPAI/LLMの境界と責任”に特化 |
| 85 | harmful-unlawful-output-control | T31 | “有害出力の統制”に特化 |
| 86 | human-in-the-loop-design | T11 | “HITL設計”に特化 |
| 87 | ieee-international-standards | T02 | “標準の読み解き方”に特化 |
| 88 | incentive-design-speed-control | T13 | “スピードと統制”に特化 |
| 89 | incident-response-ai-isolation | T15 | “隔離/停止手順”に特化 |
| 90 | incident-response-by-industry | T09 | “業界別所見→対応”に特化 |
| 91 | industry-ai-audit-comparison | T09 | “業界比較”に特化 |
| 92 | industry-automotive-mobility | T07 | “自動車の評価論点”に特化 |
| 93 | industry-finance-ai-governance | T07 | “金融のリスク評価”に特化 |
| 94 | industry-healthcare-regulation | T26 | “医療規制×運用”に特化 |
| 95 | industry-hr-recruitment-ai | T07 | “採用AIの公平性”に特化 |
| 96 | industry-insurance-underwriting | T07 | “保険引受の論点”に特化 |
| 97 | industry-kri-minimum-set | T20 | “業界別KRI最小セット”に特化 |
| 98 | industry-manufacturing-quality | T28 | “品質KRI”に特化 |
| 99 | industry-marketing-ad-ai | T32 | “広告の透明性”に特化 |
| 100 | industry-pharma-life-science | T26 | “医薬のデータ統制”に特化 |
| 101 | industry-public-sector | T02 | “公共の説明責任”に特化 |
| 102 | industry-retail-ec-recommendation | T14 | “推薦の評価/ドリフト”に特化 |
| 103 | industry-risk-heatmap | T06 | “ヒートマップ”に特化 |
| 104 | industry-templates-control-package | T17 | “テンプレ（最小要件）”に特化 |
| 105 | internal-ai-b2e-shadow | T21 | “社内Shadow AI”に特化 |
| 106 | internal-audit-ai-controls | T09 | “内部監査の統制セット”に特化 |
| 107 | ip-patent-ai-development | T31 | “特許/IP論点”に特化 |
| 108 | iso-42001-aims-introduction | T02 | “AIMS導入手順”に特化 |
| 109 | japan-ai-guidelines | T02 | “国内ガイドライン運用化”に特化 |
| 110 | japan-pip-genai | T26 | “個人情報法×GenAI”に特化 |
| 111 | legal-governance-three-lines | T01 | “法務×三線”に特化 |
| 112 | liability-disclaimer-limits | T31 | “免責と限界”に特化 |
| 113 | llm-data-boundary | T27 | “LLM境界”に特化 |
| 114 | llm-use-policy-internal-customer | T13 | “利用方針→手続き化”に特化 |
| 115 | log-integrity-retention | T16 | “ログ完全性/保持”に特化 |
| 116 | major-incident-criteria-escalation | T13 | “重大基準”に特化 |
| 117 | model-card-datasheet-audit | T17 | “モデルカードの監査用途”に特化 |
| 118 | model-poisoning-detection | T24 | “poisoning検知”に特化 |
| 119 | monitoring-alert-kri-design | T20 | “アラート設計”に特化 |
| 120 | multi-framework-integration | T03 | “複数枠組み統合”に特化 |
| 121 | next-gen-regulation-preparation | T02 | “次の規制への備え”に特化 |
| 122 | next-year-plan-priority-summary | T04 | “来年の優先”に特化 |
| 123 | next-year-planning-cycle | T04 | “計画サイクル”に特化 |
| 124 | nist-ai-rmf-implementation | T07 | “RMF実装（プロファイル）”に特化 |
| 125 | oecd-ai-principles-policy | T02 | “OECD原則→運用”に特化 |
| 126 | offensive-governance-trust | T02 | “信頼を攻めの資産へ（具体化）”に特化 |
| 127 | outsourcing-bpo-si-ai | T25 | “委託/BPO/SIの責任分界”に特化 |
| 128 | pets-privacy-enhancing | T30 | “PETs活用”に特化 |
| 129 | production-monitoring-drift | T14 | “本番ドリフト”に特化 |
| 130 | prompt-injection-control | T24 | “prompt injection”に特化 |
| 131 | rag-governance-reference-citation | T16 | “参照/引用の監査性”に特化 |
| 132 | red-teaming-guide | T14 | “レッドチーム手順”に特化 |
| 133 | regulatory-horizon-scan-ops | T02 | “ホライズンスキャン運用”に特化 |
| 134 | regulatory-horizon-scan | T02 | “スキャンの設計”に特化 |
| 135 | regulatory-splinternet | T29 | “分断×越境設計”に特化 |
| 136 | reputation-risk-prevention | T32 | “評判リスクと透明性”に特化 |
| 137 | saas-apocalypse-cowork-shock-part1 | T25 | “SaaS依存の統制論点”に特化 |
| 138 | saas-apocalypse-cowork-shock-part2 | T25 | “契約/ログ/証跡”に特化 |
| 139 | saas-apocalypse-cowork-shock-part3 | T25 | “是正ロードマップ”に特化 |
| 140 | safety-case-accountability | T08 | “Safety caseの証拠構造”に特化 |
| 141 | sbom-integration-security | T25 | “SBOM統合”に特化 |
| 142 | security-education-rules | T13 | “教育ルール”に特化 |
| 143 | security-eval-vendor-open-model | T25 | “外部モデル評価”に特化 |
| 144 | security-investment-roi | T04 | “セキュリティROI”に特化 |
| 145 | security-kri-monitoring | T20 | “セキュリティKRI”に特化 |
| 146 | shadow-ai-countermeasures | T21 | “Shadow AI対策”に特化 |
| 147 | subsidiary-sme-lightweight-governance | T03 | “軽量統制モデル”に特化 |
| 148 | supervisor-authority-alignment | T01 | “監督権限の整合”に特化 |
| 149 | supply-chain-security-ai | T25 | “供給網セキュリティ”に特化 |
| 150 | sustainability-environmental-ai | T07 | “環境影響の評価枠”に特化 |
| 151 | synthetic-data-privacy | T30 | “合成データの限界”に特化 |
| 152 | third-party-ai-vendor-risk | T25 | “第三者リスク”に特化 |
| 153 | training-data-copyright-licensing | T31 | “学習データ権利”に特化 |
| 154 | training-data-rights-licensing | T31 | “権利処理の運用”に特化 |
| 155 | transparency-accountability | T08 | “透明性と説明責任の分界”に特化 |
| 156 | uk-singapore-soft-law | T26 | “ソフトローの運用”に特化 |
| 157 | us-ai-regulation-overview | T26 | “米国動向（断定回避）”に特化 |
| 158 | use-case-approval-process | T13 | “ユースケース承認”に特化 |
| 159 | vendor-contract-living-clauses | T25 | “living clauses運用”に特化 |
| 160 | version-management-reroll | T05 | “版戻し（reroll）”に特化 |
| 161 | watermark-metadata-limits | T32 | “watermark限界”に特化 |
| 162 | worker-consumer-protection-genai | T26 | “消費者/労働者保護”に特化 |
| 163 | xai-explainability-scope | T07 | “説明可能性のスコープ”に特化 |


各記事の **タイトル（title_ja）** と **記事DNA**（対象読者・目的・深さ・スタイル）、**冒頭パターン（opening）**・**結論パターン（conclusion）** を下表で固定する。執筆時は [docs/ai-governance-blog-cursor-prompt.md](./ai-governance-blog-cursor-prompt.md) の「記事DNA」「多様性ルール」に従う。

**記号**

- **読者**: Exec=経営層 / Pract=実務 / Audit=監査 / Legal=法務・コンプラ / Multi=複数
- **目的**: Decide=意思決定 / Impl=実装 / Understand=理解 / Audit=監査対応 / Navigate=方向探索
- **深さ**: Overview=全体俯瞰 / Deep=詳細 / Quick=要点
- **スタイル**: Narrative=物語調 / Analytical=分析調 / Prescriptive=処方箋調 / Comparative=比較調
- **Op**: 冒頭パターン 1–10（3連続重複禁止）
- **Co**: 結論パターン 1–5（ローテーション）

| No. | slug | title_ja | T | 読者 | 目的 | 深さ | スタイル | Op | Co |
|-----|------|----------|---|------|------|------|----------|----|----|
| 1 | accountability-incident-design | インシデント設計と説明責任：誰が何を証明するか | T08 | Multi | Audit | Deep | Analytical | 1 | 1 |
| 2 | ai-access-control-zerotrust | AIアクセス制御：ゼロトラストを利用申請に落とす | T21 | Pract | Impl | Deep | Prescriptive | 2 | 2 |
| 3 | ai-assurance-vs-audit | 保証と監査の分界：証憑の形 | T08 | Audit | Audit | Quick | Analytical | 3 | 3 |
| 4 | ai-bom-implementation | AI-BOM実装手順（90日） | T25 | Pract | Impl | Deep | Prescriptive | 4 | 4 |
| 5 | ai-bom-supply-chain | AI-BOMと供給網の責任分界 | T25 | Pract | Understand | Overview | Comparative | 5 | 5 |
| 6 | ai-cyber-threat-model | AIサイバー脅威モデルと優先順位付け | T23 | Pract | Decide | Overview | Analytical | 6 | 1 |
| 7 | ai-data-governance-integration | データ統制とAI統制の接合点 | T26 | Multi | Understand | Overview | Analytical | 7 | 2 |
| 8 | ai-ethics-committee-design | AI倫理委員会が形骸化しない設計 | T11 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 9 | ai-ethics-principles-policy | AI倫理原則を手続きに変換する | T01 | Multi | Impl | Overview | Prescriptive | 9 | 4 |
| 10 | ai-generated-display-ui-legal | AI生成コンテンツのUI表示と誤認防止 | T32 | Pract | Impl | Quick | Prescriptive | 10 | 5 |
| 11 | ai-incident-reporting-authority | 当局報告の責任分界とインシデント設計 | T01 | Legal | Audit | Quick | Analytical | 1 | 1 |
| 12 | ai-incident-response-escalation | エスカレーション閾値と重大基準の設計 | T13 | Pract | Impl | Deep | Prescriptive | 2 | 2 |
| 13 | ai-lifecycle-overview | ライフサイクルに評価ゲートを埋め込む | T14 | Pract | Understand | Overview | Analytical | 3 | 3 |
| 14 | ai-output-copyright | 出力物の権利・責任と著作権 | T31 | Legal | Understand | Quick | Analytical | 4 | 4 |
| 15 | ai-procurement-buy-build | Buy/Build判断の評価軸 | T25 | Exec | Decide | Overview | Comparative | 5 | 5 |
| 16 | ai-procurement-decision-control | 調達審査ゲート（RACI）と承認フロー | T25 | Pract | Impl | Deep | Prescriptive | 6 | 1 |
| 17 | ai-risk-appetite-framework | レッドライン定義とリスク許容度 | T06 | Exec | Decide | Overview | Analytical | 7 | 2 |
| 18 | ai-risk-assessment-method | 定性/定量の使い分けとリスク評価 | T07 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 19 | ai-vendor-contract-clauses | 契約条項チェックリスト | T25 | Legal | Impl | Quick | Prescriptive | 9 | 4 |
| 20 | annual-plan-focus-areas | 年次優先5領域の決め方 | T04 | Exec | Decide | Overview | Prescriptive | 10 | 5 |
| 21 | audit-dashboard-board-metrics | 取締役会向け最小KRIとダッシュボード | T20 | Exec | Decide | Quick | Prescriptive | 1 | 1 |
| 22 | audit-trail-logs | ログ完全性・保持と監査証跡 | T16 | Audit | Audit | Deep | Analytical | 2 | 2 |
| 23 | auditor-ai-security-findings | 監査所見と是正テンプレ | T09 | Audit | Audit | Quick | Prescriptive | 3 | 3 |
| 24 | bcp-ai-dependency-failsafe | BCPとAI依存：停止・代替・復旧 | T15 | Pract | Impl | Overview | Prescriptive | 4 | 4 |
| 25 | bias-evaluation-qualitative-quantitative | バイアス評価の手法選択 | T07 | Pract | Impl | Deep | Analytical | 5 | 5 |
| 26 | bias-fairness-hr-credit-healthcare | 領域別の公平性論点（人事・与信・医療） | T07 | Multi | Understand | Overview | Comparative | 6 | 1 |
| 27 | board-ai-agenda-metrics | ボード指標の最小セット | T02 | Exec | Decide | Quick | Prescriptive | 7 | 2 |
| 28 | board-ai-governance-agenda | 議題テンプレ（毎四半期） | T02 | Exec | Decide | Quick | Prescriptive | 8 | 3 |
| 29 | centralized-federated-global | グローバル運用の抜け穴と統制 | T03 | Exec | Navigate | Overview | Comparative | 9 | 4 |
| 30 | centralized-vs-federated | 集中/分散の意思決定基準 | T03 | Exec | Decide | Overview | Comparative | 10 | 5 |
| 31 | change-management-resistance | 抵抗の類型と対処 | T05 | Pract | Impl | Quick | Narrative | 1 | 1 |
| 32 | china-genai-regulation | 中国規制の運用影響（断定回避） | T26 | Legal | Navigate | Overview | Analytical | 2 | 2 |
| 33 | cloud-ai-contract-data-sovereignty | クラウド契約とデータ主権 | T29 | Legal | Understand | Overview | Analytical | 3 | 3 |
| 34 | compliance-as-code | 規程のコード化 | T05 | Pract | Impl | Quick | Prescriptive | 4 | 4 |
| 35 | confidential-input-design | 機密入力の境界設計 | T22 | Pract | Impl | Deep | Prescriptive | 5 | 5 |
| 36 | content-transparency-why-now | なぜ今、コンテンツ透明性か | T32 | Multi | Understand | Quick | Narrative | 6 | 1 |
| 37 | continuous-conformity-assessment | 適合性評価の継続運用 | T10 | Pract | Impl | Deep | Prescriptive | 7 | 2 |
| 38 | continuous-evaluation-drift | ドリフト検知と是正 | T14 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 39 | control-test-automation-ccm | CCM自動化の最小実装 | T10 | Pract | Impl | Deep | Prescriptive | 9 | 4 |
| 40 | cross-border-data-contract | 越境データの契約条項最小セット | T29 | Legal | Impl | Quick | Prescriptive | 10 | 5 |
| 41 | cross-border-data-sovereignty | 法域マトリクスとデータ主権 | T29 | Legal | Understand | Overview | Analytical | 1 | 1 |
| 42 | customer-facing-ai-b2b | 対外AIの例外と承認 | T13 | Pract | Impl | Quick | Prescriptive | 2 | 2 |
| 43 | cxo-roles-ai-governance | CXO役割分担（RACI） | T02 | Exec | Decide | Overview | Prescriptive | 3 | 3 |
| 44 | cxo-roles-summary | ガバナンス役割の要点1枚 | T02 | Exec | Understand | Quick | Prescriptive | 4 | 4 |
| 45 | data-artifacts-audit-trail | データ成果物と監査証跡 | T16 | Audit | Audit | Quick | Analytical | 5 | 5 |
| 46 | data-leakage-control-design | 漏えい統制の設計パターン | T22 | Pract | Impl | Deep | Prescriptive | 6 | 1 |
| 47 | data-quality-gigo | データ品質KRIと閾値 | T28 | Pract | Impl | Quick | Prescriptive | 7 | 2 |
| 48 | data-retention-model-retirement | 保持と退役の整合 | T15 | Pract | Impl | Quick | Analytical | 8 | 3 |
| 49 | data-sharing-joint-research | 共同研究の責任分界 | T29 | Legal | Understand | Overview | Analytical | 9 | 4 |
| 50 | decommission-record-risk | 退役時のリスク記録 | T15 | Pract | Impl | Quick | Prescriptive | 10 | 5 |
| 51 | deepfake-countermeasures | deepfake対策の運用ゲート | T32 | Pract | Impl | Quick | Prescriptive | 1 | 1 |
| 52 | deploy-checklist-release-approval | リリース承認チェックリスト | T12 | Pract | Impl | Deep | Prescriptive | 2 | 2 |
| 53 | development-phase-control | 開発統制の必須点 | T11 | Pract | Impl | Deep | Prescriptive | 3 | 3 |
| 54 | dispute-evidence-log-document | 争点化に耐える証拠と証跡欠落 | T19 | Legal | Audit | Deep | Analytical | 4 | 4 |
| 55 | dlp-idp-casb-design | ツール設計（DLP/IDP/CASB） | T22 | Pract | Impl | Deep | Prescriptive | 5 | 5 |
| 56 | documentation-audit-artifacts | 監査成果物の目次 | T17 | Audit | Audit | Quick | Prescriptive | 6 | 1 |
| 57 | dpia-ai-risk-integration | DPIA統合の手順 | T07 | Pract | Impl | Deep | Prescriptive | 7 | 2 |
| 58 | ethics-risk-monitoring-remediation | 倫理リスクの継続改善 | T10 | Pract | Impl | Overview | Prescriptive | 8 | 3 |
| 59 | ethics-security-unified-control | 倫理×セキュリティ統制統合 | T01 | Multi | Understand | Overview | Analytical | 9 | 4 |
| 60 | eu-ai-act-high-risk | 高リスクAIの運用要件（断定回避） | T26 | Multi | Understand | Overview | Analytical | 10 | 5 |
| 61 | eu-ai-act-overview | EU AI Act 全体像と実装の導線 | T26 | Multi | Navigate | Overview | Analytical | 1 | 1 |
| 62 | eu-ai-act-prohibited | 禁止類型の整理（マトリクス） | T26 | Legal | Understand | Quick | Analytical | 2 | 2 |
| 63 | eu-ai-act-transparency | 透明性表示の実装 | T32 | Pract | Impl | Quick | Prescriptive | 3 | 3 |
| 64 | eval-automation-cicd | 評価のCI/CD統合 | T14 | Pract | Impl | Deep | Prescriptive | 4 | 4 |
| 65 | evals-basics | 評価の最小セット | T14 | Pract | Understand | Quick | Prescriptive | 5 | 5 |
| 66 | evidence-bundle-audit | 監査提出の形（Evidence Bundle） | T18 | Audit | Audit | Deep | Prescriptive | 6 | 1 |
| 67 | evidence-minimum-requirements | 証跡最小要件 | T17 | Audit | Audit | Quick | Prescriptive | 7 | 2 |
| 68 | exception-management-control | 例外管理の設計 | T13 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 69 | external-audit-expectations | 外部監査の期待 | T09 | Audit | Audit | Quick | Analytical | 9 | 4 |
| 70 | external-communication-design | 外部説明の設計 | T32 | Pract | Impl | Quick | Prescriptive | 10 | 5 |
| 71 | extra-territorial-brussels-effect | 域外適用の運用影響 | T26 | Legal | Navigate | Overview | Analytical | 1 | 1 |
| 72 | g7-oecd-hiroshima-ai-reporting | G7/OECD報告の運用（ボード向け） | T02 | Exec | Decide | Quick | Prescriptive | 2 | 2 |
| 73 | gdpr-genai-personal-data | GDPR×GenAI：個人データ論点 | T26 | Legal | Understand | Overview | Analytical | 3 | 3 |
| 74 | genai-red-line-boundaries | レッドライン（禁止境界） | T06 | Exec | Decide | Quick | Prescriptive | 4 | 4 |
| 75 | generated-edited-classification-taxonomy | 生成・編集の分類タクソノミー | T32 | Pract | Understand | Quick | Analytical | 5 | 5 |
| 76 | global-baseline-local-adaptation | グローバル基準×ローカル適用 | T03 | Multi | Navigate | Overview | Comparative | 6 | 1 |
| 77 | governance-continuous-improvement | 継続改善ループ | T10 | Pract | Impl | Overview | Prescriptive | 7 | 2 |
| 78 | governance-doc-version-control | 規程の版管理 | T05 | Pract | Impl | Quick | Prescriptive | 8 | 3 |
| 79 | governance-investment-roi | ROIの測り方 | T04 | Exec | Decide | Overview | Analytical | 9 | 4 |
| 80 | governance-maturity-model | 成熟度モデル | T04 | Multi | Understand | Overview | Analytical | 10 | 5 |
| 81 | governance-maturity-roadmap | ロードマップ（90日） | T04 | Pract | Impl | Deep | Prescriptive | 1 | 1 |
| 82 | governance-os-summary-roadmap | ガバナンスOS全体の要約 | T02 | Exec | Understand | Quick | Prescriptive | 2 | 2 |
| 83 | governance-talent-roles | 人材・役割設計 | T04 | Exec | Decide | Overview | Prescriptive | 3 | 3 |
| 84 | gpai-llm-governance-overview | GPAI/LLMの境界と責任 | T27 | Multi | Understand | Overview | Analytical | 4 | 4 |
| 85 | harmful-unlawful-output-control | 有害出力の統制 | T31 | Legal | Impl | Quick | Prescriptive | 5 | 5 |
| 86 | human-in-the-loop-design | HITL設計 | T11 | Pract | Impl | Deep | Prescriptive | 6 | 1 |
| 87 | ieee-international-standards | 標準の読み解き方 | T02 | Pract | Understand | Quick | Analytical | 7 | 2 |
| 88 | incentive-design-speed-control | スピードと統制の両立 | T13 | Pract | Impl | Quick | Prescriptive | 8 | 3 |
| 89 | incident-response-ai-isolation | 隔離・停止手順 | T15 | Pract | Impl | Deep | Prescriptive | 9 | 4 |
| 90 | incident-response-by-industry | 業界別所見と対応 | T09 | Audit | Audit | Overview | Comparative | 10 | 5 |
| 91 | industry-ai-audit-comparison | 業界別監査比較 | T09 | Audit | Navigate | Overview | Comparative | 1 | 1 |
| 92 | industry-automotive-mobility | 自動車の評価論点 | T07 | Pract | Understand | Overview | Analytical | 2 | 2 |
| 93 | industry-finance-ai-governance | 金融のリスク評価 | T07 | Pract | Understand | Overview | Analytical | 3 | 3 |
| 94 | industry-healthcare-regulation | 医療規制と運用 | T26 | Legal | Understand | Overview | Analytical | 4 | 4 |
| 95 | industry-hr-recruitment-ai | 採用AIの公平性 | T07 | Pract | Understand | Overview | Analytical | 5 | 5 |
| 96 | industry-insurance-underwriting | 保険引受の論点 | T07 | Pract | Understand | Overview | Analytical | 6 | 1 |
| 97 | industry-kri-minimum-set | 業界別KRI最小セット | T20 | Pract | Impl | Quick | Prescriptive | 7 | 2 |
| 98 | industry-manufacturing-quality | 製造・品質KRI | T28 | Pract | Impl | Quick | Prescriptive | 8 | 3 |
| 99 | industry-marketing-ad-ai | 広告の透明性 | T32 | Pract | Impl | Quick | Prescriptive | 9 | 4 |
| 100 | industry-pharma-life-science | 医薬のデータ統制 | T26 | Legal | Understand | Overview | Analytical | 10 | 5 |
| 101 | industry-public-sector | 公共の説明責任 | T02 | Exec | Understand | Quick | Prescriptive | 1 | 1 |
| 102 | industry-retail-ec-recommendation | 推薦の評価とドリフト | T14 | Pract | Impl | Overview | Prescriptive | 2 | 2 |
| 103 | industry-risk-heatmap | リスクヒートマップ | T06 | Exec | Decide | Quick | Analytical | 3 | 3 |
| 104 | industry-templates-control-package | 業界テンプレ（最小要件） | T17 | Pract | Impl | Quick | Prescriptive | 4 | 4 |
| 105 | internal-ai-b2e-shadow | 社内Shadow AI対策 | T21 | Pract | Impl | Deep | Prescriptive | 5 | 5 |
| 106 | internal-audit-ai-controls | 内部監査の統制セット | T09 | Audit | Audit | Deep | Prescriptive | 6 | 1 |
| 107 | ip-patent-ai-development | 特許・IP論点 | T31 | Legal | Understand | Quick | Analytical | 7 | 2 |
| 108 | iso-42001-aims-introduction | AIMS導入手順 | T02 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 109 | japan-ai-guidelines | 国内ガイドラインの運用化 | T02 | Multi | Navigate | Overview | Analytical | 9 | 4 |
| 110 | japan-pip-genai | 個人情報法×GenAI | T26 | Legal | Understand | Quick | Analytical | 10 | 5 |
| 111 | legal-governance-three-lines | 法務と三線防衛 | T01 | Legal | Understand | Overview | Analytical | 1 | 1 |
| 112 | liability-disclaimer-limits | 免責と責任の限界 | T31 | Legal | Understand | Quick | Analytical | 2 | 2 |
| 113 | llm-data-boundary | LLMのデータ境界 | T27 | Pract | Understand | Overview | Analytical | 3 | 3 |
| 114 | llm-use-policy-internal-customer | 利用方針の手続き化 | T13 | Pract | Impl | Quick | Prescriptive | 4 | 4 |
| 115 | log-integrity-retention | ログ完全性・保持 | T16 | Pract | Impl | Quick | Prescriptive | 5 | 5 |
| 116 | major-incident-criteria-escalation | 重大基準とエスカレーション | T13 | Pract | Impl | Quick | Prescriptive | 6 | 1 |
| 117 | model-card-datasheet-audit | モデルカードの監査用途 | T17 | Audit | Audit | Quick | Prescriptive | 7 | 2 |
| 118 | model-poisoning-detection | モデルポイズニング検知 | T24 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 119 | monitoring-alert-kri-design | アラート・KRI設計 | T20 | Pract | Impl | Deep | Prescriptive | 9 | 4 |
| 120 | multi-framework-integration | 複数枠組みの統合 | T03 | Multi | Navigate | Overview | Comparative | 10 | 5 |
| 121 | next-gen-regulation-preparation | 次の規制への備え | T02 | Exec | Navigate | Quick | Prescriptive | 1 | 1 |
| 122 | next-year-plan-priority-summary | 来年の優先領域 | T04 | Exec | Decide | Quick | Prescriptive | 2 | 2 |
| 123 | next-year-planning-cycle | 計画サイクルの設計 | T04 | Pract | Impl | Overview | Prescriptive | 3 | 3 |
| 124 | nist-ai-rmf-implementation | NIST RMF実装（プロファイル） | T07 | Pract | Impl | Deep | Prescriptive | 4 | 4 |
| 125 | oecd-ai-principles-policy | OECD原則の運用化 | T02 | Multi | Understand | Overview | Analytical | 5 | 5 |
| 126 | offensive-governance-trust | 信頼を攻めの資産に（具体化） | T02 | Exec | Decide | Quick | Narrative | 6 | 1 |
| 127 | outsourcing-bpo-si-ai | 委託・BPO/SIの責任分界 | T25 | Legal | Understand | Overview | Analytical | 7 | 2 |
| 128 | pets-privacy-enhancing | PETs活用と限界 | T30 | Pract | Understand | Quick | Analytical | 8 | 3 |
| 129 | production-monitoring-drift | 本番ドリフト監視 | T14 | Pract | Impl | Deep | Prescriptive | 9 | 4 |
| 130 | prompt-injection-control | プロンプトインジェクション対策 | T24 | Pract | Impl | Deep | Prescriptive | 10 | 5 |
| 131 | rag-governance-reference-citation | 参照・引用の監査性 | T16 | Pract | Impl | Quick | Prescriptive | 1 | 1 |
| 132 | red-teaming-guide | レッドチーム手順 | T14 | Pract | Impl | Deep | Prescriptive | 2 | 2 |
| 133 | regulatory-horizon-scan-ops | ホライズンスキャン運用 | T02 | Pract | Impl | Quick | Prescriptive | 3 | 3 |
| 134 | regulatory-horizon-scan | スキャンの設計 | T02 | Pract | Impl | Overview | Prescriptive | 4 | 4 |
| 135 | regulatory-splinternet | 分断と越境設計 | T29 | Legal | Navigate | Overview | Analytical | 5 | 5 |
| 136 | reputation-risk-prevention | 評判リスクと透明性 | T32 | Multi | Understand | Quick | Prescriptive | 6 | 1 |
| 137 | saas-apocalypse-cowork-shock-part1 | SaaS依存の統制論点（1） | T25 | Pract | Understand | Overview | Narrative | 7 | 2 |
| 138 | saas-apocalypse-cowork-shock-part2 | 契約・ログ・証跡（2） | T25 | Pract | Impl | Overview | Prescriptive | 8 | 3 |
| 139 | saas-apocalypse-cowork-shock-part3 | 是正ロードマップ（3） | T25 | Pract | Impl | Deep | Prescriptive | 9 | 4 |
| 140 | safety-case-accountability | Safety caseの証拠構造 | T08 | Audit | Audit | Deep | Analytical | 10 | 5 |
| 141 | sbom-integration-security | SBOM統合とセキュリティ | T25 | Pract | Impl | Deep | Prescriptive | 1 | 1 |
| 142 | security-education-rules | 教育ルールと定着 | T13 | Pract | Impl | Quick | Prescriptive | 2 | 2 |
| 143 | security-eval-vendor-open-model | 外部モデル評価 | T25 | Pract | Impl | Deep | Prescriptive | 3 | 3 |
| 144 | security-investment-roi | セキュリティROI | T04 | Exec | Decide | Quick | Analytical | 4 | 4 |
| 145 | security-kri-monitoring | セキュリティKRI監視 | T20 | Pract | Impl | Quick | Prescriptive | 5 | 5 |
| 146 | shadow-ai-countermeasures | Shadow AI対策 | T21 | Pract | Impl | Deep | Prescriptive | 6 | 1 |
| 147 | subsidiary-sme-lightweight-governance | 子会社・SME向け軽量統制 | T03 | Exec | Navigate | Overview | Comparative | 7 | 2 |
| 148 | supervisor-authority-alignment | 監督権限の整合 | T01 | Legal | Understand | Quick | Analytical | 8 | 3 |
| 149 | supply-chain-security-ai | 供給網セキュリティ | T25 | Pract | Impl | Overview | Prescriptive | 9 | 4 |
| 150 | sustainability-environmental-ai | 環境影響の評価枠 | T07 | Multi | Understand | Overview | Analytical | 10 | 5 |
| 151 | synthetic-data-privacy | 合成データの限界 | T30 | Pract | Understand | Quick | Analytical | 1 | 1 |
| 152 | third-party-ai-vendor-risk | 第三者・ベンダーリスク | T25 | Legal | Understand | Overview | Analytical | 2 | 2 |
| 153 | training-data-copyright-licensing | 学習データの権利処理 | T31 | Legal | Understand | Quick | Analytical | 3 | 3 |
| 154 | training-data-rights-licensing | 権利処理の運用 | T31 | Pract | Impl | Quick | Prescriptive | 4 | 4 |
| 155 | transparency-accountability | 透明性と説明責任の分界 | T08 | Multi | Understand | Quick | Analytical | 5 | 5 |
| 156 | uk-singapore-soft-law | UK・シンガポールのソフトロー | T26 | Legal | Navigate | Overview | Analytical | 6 | 1 |
| 157 | us-ai-regulation-overview | 米国AI規制の動向（断定回避） | T26 | Legal | Navigate | Overview | Analytical | 7 | 2 |
| 158 | use-case-approval-process | ユースケース承認プロセス | T13 | Pract | Impl | Deep | Prescriptive | 8 | 3 |
| 159 | vendor-contract-living-clauses | living clausesの運用 | T25 | Legal | Impl | Quick | Prescriptive | 9 | 4 |
| 160 | version-management-reroll | 版戻し（reroll）と変更管理 | T05 | Pract | Impl | Quick | Prescriptive | 10 | 5 |
| 161 | watermark-metadata-limits | ウォーターマークの限界 | T32 | Pract | Understand | Quick | Analytical | 1 | 1 |
| 162 | worker-consumer-protection-genai | 消費者・労働者保護とGenAI | T26 | Legal | Understand | Overview | Analytical | 2 | 2 |
| 163 | xai-explainability-scope | 説明可能性のスコープ | T07 | Pract | Understand | Quick | Analytical | 3 | 3 |

---

## 4. Cursor実装指示（重複根絶のための必須手順）

> **記事執筆・レビュー時のルール** は [docs/ai-governance-blog-cursor-prompt.md](./ai-governance-blog-cursor-prompt.md) に記載。**実装フロー（Phase 1–4）**・**執筆プロンプトのCRITICAL（3.3の該当行参照必須）**・**直前10記事の図表使用履歴の明示的受け渡し**に従うこと。

1. **URL一覧のslugをSSOT** にして、記事本文ファイルを1:1で対応付ける（漏れ禁止）。
2. 各記事の **frontmatter**（またはメタデータ）に `template_id: Txx`・`unique_focus: "…"`・**記事DNA**（読者/目的/深さ/スタイル）・**title_ja**（3.3の表を参照）を付与する。
3. **生成/改稿** はテンプレの**必須セクション**を基にしつつ、**設計図3.3の該当No.行を必ず参照**してDNA・冒頭・結論パターンを使用する。記憶や推測で補完しない。本文は **unique_focus を冒頭2段落に必ず反映** する。
4. バッチ執筆時は**直前10記事の図表使用履歴**を執筆プロンプトに含め、同じ図の型を3記事連続で使わない。
5. **本文の見出しに「次の一歩」を使わない**。記事末尾の結論ブロック「## 次の一歩」と重複するため。最後の本文セクションは「まとめとアクション」「実装のポイント」等とする（apply_llm_article.py でも本文見出しが「次の一歩」の場合は「まとめとアクション」に置換する）。
6. **文体は全記事でです・ます調**とする。クレバーでプロフェッショナルなトーンを保ち、である調・だ調は使わない。
7. “途中から同一化”の原因（共通パーシャル/include、CMSの本文参照ミス等）を特定し、**テンプレ別に本文を分離** する。
8. 仕上げに、**カテゴリトップ** でテンプレ別フィルタ（Txx）とツリー導線を提供する。

---

## 5. デザイン統一ルール（全インフォグラフィック共通）

| ルール | 内容 |
|--------|------|
| **1図＝1メッセージ** | 1つの図で伝えるメッセージは1つに絞る。 |
| **ラベル** | 図中ラベルは「名詞句＋動詞1つ」まで（長文禁止）。 |
| **注釈** | “断定回避（条件/前提）”を必ず1行入れる。 |
| **3図セットの役割** |  |
|  | **#1** = 概念の骨格（レイヤー/マトリクス） |
|  | **#2** = 運用の流れ（フロー/タイムライン） |
|  | **#3** = 監査・証跡（Evidence Chain / 差し戻しTop5 / KPI） |
| **マトリクス・表のセル** | 概念でマトリクスや表を作る場合は各セルに**有意な内容をできるだけ埋める**。サンプルの場合は「サンプル」と表記し、**どのように埋めるべきかガイド**を書き添える。空セルのみのマトリクスは避ける。 |
| **日本語＋英語の混在** | 一般的でない「日本語＋英語」の組み合わせ（例：閾値 breach）は避け、カタカナ表記（閾値ブリーチ）にするか括弧で日本語説明を付記する。日本人が読んで違和感のない表記にする。 |

---

## 変更履歴

| 日付 | 内容 |
|------|------|
| 2026-02-09 | 初版作成。MECEツリー・テンプレT01–T32・163記事割当・実装指示・デザインルールを記載。 |
| 2026-02-09 | 記事執筆・レビュー用Cursorプロンプトを docs/ai-governance-blog-cursor-prompt.md に分離し、セクション4から参照を追加。 |
| 2026-02-09 | 多様性確保のため記事DNA・冒頭/結論パターン・インフォグラフィック選択ルールを cursor prompt に追加。設計図に 3.3 記事DNA・タイトル・付帯情報（163件）を追加。 |
| 2026-02-09 | 手順改善：執筆時の設計図3.3参照強制（CRITICAL）・図表使用履歴の明示的受け渡し・固有の一文チェックリスト・数値/出典/断定の厳格化・冒頭パターン選択ルール・実装フロー4段階・テンプレ必須セクション（T25を例にDNA別重点配分を追加）。 |
| 2026-02-09 | 見出し重複防止：本文の見出しに「次の一歩」を使わないルールを追加（結論ブロックと重複するため）。apply_llm_article.py で本文見出し「次の一歩」→「まとめとアクション」に自動置換。ブリーフ・Cursorプロンプト・設計図に明記。 |
| 2026-02-09 | 文体の統一：全記事で**です・ます調**を必須とし、クレバーでプロフェッショナルなトーンを明記。執筆ルール（cursor prompt・設計図・ブリーフ出力形式）に反映。記事001〜005は Cursor で作成した出力をです・ます調に改稿しHTMLを再適用済み。その他既存記事は改稿・再生成時にです・ます調で統一する。 |
| 2026-02-09 | マトリクス・表のルール：概念でマトリクスや表を作る場合は各セルに有意な内容をできるだけ埋める。サンプルの場合は「サンプル」と表記し、埋め方のガイドを書き添える。空セルのみのマトリクスは避ける。記事006の脅威×統制マトリクスをセル埋め＋ガイド付きに更新。 |
| 2026-02-09 | 日本語＋英語混在用語のルール：「閾値 breach」など一般的でない組み合わせは避け、カタカナ表記（閾値ブリーチ）または括弧で日本語説明を付記。記事006を「閾値ブリーチ」に修正。執筆ルールに反映。 |

---

## 直前10記事の図表使用履歴（参照必須）

| No. | slug | 図1 | 図2 | 図3 |
|-----|------|-----|-----|-----|
| 1 | accountability-incident-design | A(Mermaid) | G(Mermaid) | F(Mermaid) |
| 2 | ai-access-control-zerotrust | D(Mermaid) | B(Mermaid) | G(Mermaid) |
| 3 | ai-assurance-vs-audit | A(Mermaid) | E(Mermaid) | F(Mermaid) |
| 4 | ai-bom-implementation | J(SVG) | E(HTML) | G(Table) |
| 5 | ai-bom-supply-chain | J(SVG) | D(HTML) | G(Table) |
| 6 | ai-cyber-threat-model | D(SVG) | H(HTML) | I(Table) |
| 7 | ai-data-governance-integration | (未記録)() | (未記録)() | (未記録)() |
| 8 | ai-ethics-committee-design | (未記録)() | (未記録)() | (未記録)() |
| 9 | ai-ethics-principles-policy | (未記録)() | (未記録)() | (未記録)() |

## 直前5記事で使用された形式（各形式1回までしか使えない）

直近5記事の図で使われた形式: **SVG, HTML, Table, SVG, HTML, Table, Mermaid, Mermaid, Mermaid, Mermaid, Mermaid, Mermaid, Mermaid, Mermaid, Mermaid**  
→ この記事では、上記の各形式を**最大1回まで**しか使ってよい。それ以外の形式を必ず含めること。

**RULE**: 多様なインフォグラフィックを必ず使用すること。図は **指定フォーマット**（SVG / HTML / Table / **Mermaid** / Canvas / Vega-Lite / Plotly / DOT / PlantUML 等）で出力する。**同一形式を連続して使わない**。詳細は **docs/ai-governance-blog-infographic-formats.md** を参照。図の型（A–J）は上記履歴と3図セットの役割に従って選ぶこと。

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
（形式は SVG / HTML / Table / **Mermaid** / Canvas / Vega-Lite / Plotly / DOT / PlantUML 等から選択。同一形式の連続使用は禁止。該当するコードブロックのみ。**マトリクス・表**の場合は各セルに有意な内容をできるだけ埋める。サンプルなら「サンプル」と表記し、埋め方のガイドを書き添える。空セルのみは避ける。）

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
（明日からできる具体的な行動を3つ以内。）
```
