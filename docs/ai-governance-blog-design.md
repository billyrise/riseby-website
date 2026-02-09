# RISEby AI Governance Blog — カテゴリ全体設計図

> 本ドキュメントは AIガバナンスカテゴリ（163記事＋カテゴリトップ）の **SSOT（Single Source of Truth）** として運用する。  
> 記事の書き直し・生成・改稿はすべてこの設計に従う。

**最終更新**: 2026-02-09

---

## 背骨フレーム（全記事共通の整合軸）

全記事は以下の枠組みと整合させる。断定は避け、条件・前提を明示する。

| 枠組み | 役割 |
|--------|------|
| **NIST AI RMF** | GOVERN / MAP / MEASURE / MANAGE — 「運用へ落とす」強制軸 |
| **ISO/IEC 42001** | AIMS（方針・目的・プロセス・継続改善） |
| **EU AI Act** | リスク区分（禁止 / 高リスク / 透明性 / GPAI 等） |
| **OECD AI Principles** | 信頼できるAI（価値・原則の上位概念） |

### 用語（記事内で初出時に説明するもの）

| 略称・用語 | 説明（初出時に括弧書きで記載する推奨文） |
|------------|------------------------------------------|
| **三線（3LoD）** | 三線防衛（1線＝業務、2線＝リスク・コンプラ、3線＝監査）。 |

---

## 0. カテゴリトップ（index.html）— 役割

- **目的**: 163記事を「重複なく」辿れるナビ＋「何が新しいのか（運用視点）」を1画面で示す
- **必須要素**:
  1. **ツリー**（下記セクション1）をクリック可能に（章レベルまで）
  2. **運用の最小要件の1枚図**: RACI / 申請-審査-例外-更新 / 証跡 / 継続評価 / インシデント
  3. 各記事の **「読むべき順（90日ロードマップ）」** 導線

---

## 1. 超高精細テーマツリー（MECE）

### A. Governance OS（統治OS）— “回る仕組み”

| ID | テーマ |
|----|--------|
| A1 | 役割・権限・三線防衛 |
| A2 | ボード/経営アジェンダ・意思決定 |
| A3 | 組織モデル（集中/分散/グローバル） |
| A4 | 年次計画・投資・ROI・人材 |
| A5 | 文書統制（版管理/変更管理/抵抗への対処） |

### B. Risk & Assurance（リスクと保証）— “何をどこまで担保するか”

| ID | テーマ |
|----|--------|
| B1 | リスク許容度（Risk Appetite） |
| B2 | リスク評価方法（定性/定量、バイアス含む） |
| B3 | Assurance vs Audit（保証の分界） |
| B4 | 監査期待・監査所見の構造 |
| B5 | 継続的適合性評価（continuous conformity） |

### C. Lifecycle & Control（ライフサイクル統制）— “作る→出す→運用→終わる”

| ID | テーマ |
|----|--------|
| C1 | 開発フェーズ統制（設計レビュー、HITL、機密入力） |
| C2 | リリース承認・デプロイチェックリスト |
| C3 | 運用統制（例外管理、変更、教育） |
| C4 | 評価（Evals/CI/CD/ドリフト/レッドチーミング） |
| C5 | 廃止（retirement/decommission/記録保全） |

### D. Evidence & Auditability（証跡と監査可能性）— “後から再現できる”

| ID | テーマ |
|----|--------|
| D1 | 監査証跡（audit trail）とログ設計 |
| D2 | 証跡最小要件（Evidence minimum） |
| D3 | Evidence Bundle / 証拠連鎖（Integrity/Retention） |
| D4 | 争点化（dispute）に耐える証拠設計 |
| D5 | ダッシュボード（ボード/監査向け指標） |

### E. Security（AIセキュリティ）— “攻撃面と統制”

| ID | テーマ |
|----|--------|
| E1 | アクセス制御（Zero Trust） |
| E2 | データ漏えい対策（DLP/IDP/CASB、境界） |
| E3 | 脅威モデル（AI cyber threat model） |
| E4 | Prompt Injection / Model Poisoning 等のAI特有攻撃 |
| E5 | サプライチェーン/外部モデル評価 |

### F. Privacy & Data Governance（プライバシーとデータ統制）

| ID | テーマ |
|----|--------|
| F1 | GDPR/個人情報（PIPL含む） |
| F2 | データ境界（LLM data boundary） |
| F3 | データ品質（GIGO） |
| F4 | 共同研究・データ共有・越境 |
| F5 | PETs / Synthetic data |

### G. Legal & Content Integrity（法務・コンテンツ健全性）

| ID | テーマ |
|----|--------|
| G1 | 著作権（出力/学習データ） |
| G2 | 特許/IP（AI開発） |
| G3 | 透明性表示（生成/編集分類、UI表示） |
| G4 | Deepfake / Watermark / Metadata の限界 |
| G5 | 免責・責任範囲（liability limits） |

### H. Regulation & Standards（規制・標準・ソフトロー）

| ID | テーマ |
|----|--------|
| H1 | EU AI Act（overview/prohibited/high-risk/transparency） |
| H2 | ISO/IEC 42001（AIMS導入） |
| H3 | NIST AI RMF（実装） |
| H4 | OECD/G7広島（報告/原則） |
| H5 | 国別：日本/米国/中国/UK/SG 等 |

### I. Procurement & Third-Party（調達・委託・第三者）

| ID | テーマ |
|----|--------|
| I1 | Buy vs Build / 調達判断 |
| I2 | 契約条項（living clauses、データ主権） |
| I3 | ベンダーリスク（第三者、BPO/SI） |
| I4 | AI-BOM / SBOM 統合 |
| I5 | 供給網（supply chain security） |

### J. Operations & Monitoring（運用・監視）

| ID | テーマ |
|----|--------|
| J1 | KRI/KPI（最小セット、閾値） |
| J2 | 監視・アラート設計 |
| J3 | 継続改善（continuous improvement） |
| J4 | 規制ホライズンスキャン（Ops） |
| J5 | 外部コミュニケーション（透明性、顧客向け） |

### K. Incident & Resilience（インシデントと事業継続）

| ID | テーマ |
|----|--------|
| K1 | インシデント分類・重大基準 |
| K2 | 報告・当局・エスカレーション |
| K3 | 隔離・停止・復旧（AI isolation） |
| K4 | BCP（AI依存 failsafe） |
| K5 | 業界別インシデント対応 |

### L. Industry Packs（業界別パッケージ）

| ID | テーマ |
|----|--------|
| L1 | 金融/保険 |
| L2 | 医療/ヘルスケア |
| L3 | 人事/採用 |
| L4 | 製造/品質/自動車 |
| L5 | マーケ/広告/小売/EC |
| L6 | 公共/規制産業 |
| L7 | 業界比較/テンプレ/ヒートマップ/KRI最小セット |

---

## 2. 末端テンプレライブラリ（T01〜T32）

> 163記事は下記テンプレに **必ず割当てる**。  
> 各テンプレは「書くべきポイント」「使うべきインフォグラフィックス3種」と、**必須セクション**（章のテーマの最小セット）を定める。  
> **執筆時**: Outline は「必須セクション」として扱い、**記事DNAに応じて順序・厚さを調整してよい**（例：Exec×Decide では判断軸を厚く、Pract×Impl では手順を厚く）。本文が同一化しないようにする。

### T01 三線防衛と法務ガバナンス（A1）

- **Points**:
  - 3LoD（1線=現場、2線=リスク/コンプラ、3線=監査）のAI版
  - Legal/Compliance/Securityの境界（“誰が最終判断するか”）
  - 典型的な揉めどころ（例外、承認、証跡）
- **Infographics (3)**:
  1. RACIチャート（Board/Legal/CISO/Audit/BU/IT）
  2. レイヤー図（Policy→Process→Evidence→Monitoring）
  3. 監査差し戻しTop5（境界不明確由来）
- **Outline**:
  1. なぜAIで三線が崩れるか
  2. RACI最小セット
  3. “例外”が燃える構造と封じ方
  4. 実装チェックリスト（10項目）
  5. 参考：規制/標準へのマッピング（断定しない）

### T02 Board/CXOアジェンダと意思決定（A2）

- **Points**: ボードに上げるKPI/KRI最小、意思決定ログ、四半期レビュー運用
- **Infographics**: 1) KPI/KRIダッシュボード 2) タイムライン（年次計画） 3) RACI
- **Outline**: 取締役会で聞かれる5問→指標→運用→雛形

### T03 組織モデル：集中/分散/グローバル（A3）

- **Points**: 集中vs分散のトレードオフ、グローバル基準×ローカル適用、統制の“抜け穴”
- **Infographics**: 1) マトリクス（モデル×統制） 2) レイヤー図 3) タイムライン（移行）
- **Outline**: モデル選定→ガードレール→移行計画→失敗例

### T04 年次計画・投資・ROI・人材（A4）

- **Points**: 年次優先領域、投資対効果の測り方（再作業/差し戻し/事故コスト）、役割設計
- **Infographics**: 1) タイムライン（年次） 2) KPI/KRI 3) マトリクス（投資×効果）
- **Outline**: 今年やるべき5領域→予算→人材→レビュー

### T05 文書統制/版管理/抵抗対処（A5）

- **Points**: ガバナンス文書の“コード化”、版管理、変更抵抗の扱い
- **Infographics**: 1) Evidence Chain（文書→承認→配布→証跡） 2) フロー（変更管理） 3) 差し戻しTop5
- **Outline**: 文書が形骸化する理由→版管理→教育→監査視点

### T06 リスク許容度（B1）

- **Points**: Risk Appetiteを“利用ケース承認”に落とす、レッドライン（禁止境界）
- **Infographics**: 1) マトリクス（影響×確率×許容） 2) フロー（承認） 3) レイヤー図
- **Outline**: 許容度設計→承認運用→例外→KRI

### T07 リスク評価方法（B2）

- **Points**: 定性/定量、バイアス評価、業界差分、DPIA統合
- **Infographics**: 1) マトリクス（リスク領域×評価手法） 2) ライフサイクル輪 3) KPI/KRI
- **Outline**: 評価設計→実施→記録→継続評価

### T08 Assurance vs Audit（B3/D領域横断）

- **Points**: Proof/Assurance分界、監査で求める証憑の形、外部監査との接続
- **Infographics**: 1) レイヤー図（Proof→Assurance） 2) Evidence Chain 3) 監査差し戻しTop5
- **Outline**: 用語定義→分界→成果物→実装の勘所

### T09 監査期待/所見の構造（B4）

- **Points**: 監査人が見る“統制設計/運用/証跡”、所見パターン、是正の優先度
- **Infographics**: 1) 差し戻しTop5 2) KPI/KRI 3) Evidence Chain
- **Outline**: 所見の型→原因→是正テンプレ→追跡KPI

### T10 継続的適合性評価（B5/J）

- **Points**: continuous conformity、コントロールテスト自動化、CCM
- **Infographics**: 1) CI/CDゲート図（Evals含む） 2) KPI/KRI 3) ライフサイクル輪
- **Outline**: なぜ年1監査では不足→継続評価→自動化→運用設計

### T11 開発統制（C1）

- **Points**: 機密入力設計、HITL、倫理委員会設計、開発段階の統制
- **Infographics**: 1) レイヤー図 2) フロー（レビュー/承認） 3) RACI
- **Outline**: 開発での落とし穴→統制→証跡→チェックリスト

### T12 リリース/デプロイ承認（C2）

- **Points**: リリース承認、チェックリスト、段階的ロールアウト、ロールバック
- **Infographics**: 1) フロー（release approval） 2) ライフサイクル輪 3) Evidence Chain
- **Outline**: 承認ゲート→証跡→失敗例→テンプレ

### T13 運用統制：例外/教育/インセンティブ（C3）

- **Points**: 例外管理、教育、スピードと統制の両立（インセンティブ設計）
- **Infographics**: 1) フロー（例外） 2) KPI/KRI 3) マトリクス（行動×統制）
- **Outline**: 例外が増える理由→抑制→教育→KRI

### T14 評価（Evals/ドリフト/CI/CD/レッドチーム）（C4）

- **Points**: evals basics、継続評価、ドリフト、評価自動化、レッドチーム
- **Infographics**: 1) CI/CDゲート図 2) KPI/KRI（品質・安全） 3) ライフサイクル輪
- **Outline**: 何を測る→いつ測る→閾値→証跡→運用

### T15 廃止/Retirement/Decommission（C5）

- **Points**: データ保持、モデル退役、リスク記録、再現性確保
- **Infographics**: 1) Evidence Chain 2) タイムライン（退役手順） 3) 監査差し戻しTop5
- **Outline**: 退役が監査で燃える理由→手順→証跡→チェックリスト

### T16 監査証跡とログ設計（D1）

- **Points**: audit trail、ログ完全性、保持、改ざん検知
- **Infographics**: 1) Evidence Chain 2) マトリクス（ログ種別×目的） 3) KPI/KRI
- **Outline**: 監査で必要なログ→設計→保全→検証

### T17 証跡最小要件（D2）

- **Points**: evidence minimum、何が欠けるとNGか、最小目次
- **Infographics**: 1) レイヤー図（Minimum set） 2) 差し戻しTop5 3) Evidence Chain
- **Outline**: 最小セット→例→落とし穴→テンプレ

### T18 Evidence Bundle/証拠連鎖（D3）

- **Points**: evidence bundle、ハッシュ、保全、提出、検証
- **Infographics**: 1) Evidence Chain（必須） 2) フロー（生成→保管→提出） 3) マトリクス（要件×成果物）
- **Outline**: 連鎖設計→実装→運用→監査提示

### T19 争点化（dispute）に耐える証拠（D4）

- **Points**: dispute、責任帰属、ログと文書の整合、証拠の“欠落点”
- **Infographics**: 1) Evidence Chain 2) 差し戻しTop5 3) RACI
- **Outline**: 争点シナリオ→必要証拠→保全→テンプレ

### T20 ダッシュボード（ボード/監査向け）（D5/J1）

- **Points**: audit dashboard、最小KRI、閾値、エスカレーション
- **Infographics**: 1) KPI/KRIダッシュボード 2) タイムライン（レビュー） 3) RACI
- **Outline**: 何を見る→誰が見る→閾値→アクション

### T21 Zero Trustアクセス制御（E1）

- **Points**: AIアクセス制御、最小権限、B2E shadow対策
- **Infographics**: 1) マトリクス（主体×権限×データ） 2) フロー（申請/承認） 3) Evidence Chain
- **Outline**: リスク→設計→運用→証跡

### T22 データ漏えい対策（DLP/IDP/CASB、境界）（E2）

- **Points**: leakage control、DLP/IDP/CASB設計、機密入力設計
- **Infographics**: 1) レイヤー図（境界） 2) マトリクス（経路×統制） 3) Evidence Chain
- **Outline**: 漏えい経路→統制→運用→監査提示

### T23 脅威モデル（E3）

- **Points**: AI cyber threat model、攻撃面、優先統制
- **Infographics**: 1) マトリクス（脅威×統制） 2) ライフサイクル輪 3) KPI/KRI
- **Outline**: 脅威分類→統制→監視→演習

### T24 Prompt Injection / Poisoning 等（E4）

- **Points**: prompt injection、model poisoning、検知/防止/監視
- **Infographics**: 1) CI/CDゲート図 2) マトリクス（攻撃×対策） 3) KPI/KRI
- **Outline**: 攻撃パターン→対策→評価→運用

### T25 外部モデル評価・供給網（E5/I4）

- **Points**: open model/vendor eval、SBOM統合、供給網
- **Infographics**: 1) サプライチェーン図 2) マトリクス（要件×ベンダー） 3) Evidence Chain
- **必須セクション**（記事DNAに応じて順序・深さを調整可）:
  1. 選定基準（評価軸）
  2. 評価プロセス（手順）
  3. 契約・SLA
  4. 継続監視
  5. 証跡・監査対応
- **記事DNA別の重点配分例**:
  - Exec×Decide: セクション1を厚く、2–4を薄く
  - Pract×Impl: セクション2–5を均等に、1は簡潔に
  - Legal×Understand: セクション3・5を厚く

### T26 GDPR/個人情報（F1）

- **Points**: GDPR×GenAI、個人情報、目的外利用、権利対応（断定禁止）
- **Infographics**: 1) マトリクス（データ種類×義務） 2) レイヤー図 3) フロー（DPIA/承認）
- **Outline**: 何が論点→運用→証跡→チェックリスト

### T27 データ境界（F2）

- **Points**: LLM data boundary、入力/出力/学習境界、契約境界
- **Infographics**: 1) レイヤー図（境界） 2) サプライチェーン図 3) Evidence Chain
- **Outline**: 境界定義→統制→契約→運用

### T28 データ品質（GIGO）（F3）

- **Points**: data quality、評価、監視、責任分界
- **Infographics**: 1) KPI/KRI（品質） 2) ライフサイクル輪 3) マトリクス（データ×リスク）
- **Outline**: 品質が壊れる点→測定→是正→証跡

### T29 共同研究・越境データ（F4）

- **Points**: cross-border contract、data sharing、joint research
- **Infographics**: 1) サプライチェーン図（関係者） 2) マトリクス（データ×法域） 3) Evidence Chain
- **Outline**: 典型契約論点→統制→証跡→雛形

### T30 PETs / Synthetic Data（F5）

- **Points**: PETs、synthetic data、プライバシー強化と限界
- **Infographics**: 1) マトリクス（手法×効果×限界） 2) レイヤー図 3) KPI/KRI
- **Outline**: 使い所→限界→運用→証跡

### T31 著作権/学習データ/出力（G1）

- **Points**: output copyright、training data licensing、表示義務
- **Infographics**: 1) マトリクス（用途×リスク×対応） 2) レイヤー図 3) 差し戻しTop5（法務観点）
- **Outline**: 何が争点→方針→手続き→証跡→チェック

### T32 透明性表示/Deepfake/Watermark（G3/G4）

- **Points**: generated/edited分類、UI表示、watermark/metadataの限界、deepfake対策
- **Infographics**: 1) マトリクス（コンテンツ×義務） 2) フロー（公開前チェック） 3) 差し戻しTop5
- **Outline**: なぜ今→要求→運用→証跡

> ※テンプレは必要に応じて追加してよいが、まずは T01〜T32 で163件を必ず割当てる。

---

## 3. 記事→テンプレ割当（163件 + カテゴリトップ）

> 形式：No. URL — TemplateID — 記事固有の **unique_focus**（1行）  
> （差分ポイントは「その記事だけの焦点」を決め、同一化を防ぐ）

### 3.1 カテゴリトップ

| No. | URL | Template | unique_focus |
|-----|-----|----------|--------------|
| TOP | https://riseby.net/blog/ai-governance/index.html | T02 | “読む順（90日）”と“最小要件の1枚図”を追加 |

### 3.2 163記事

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

### 3.3 記事DNA・タイトル・付帯情報（多様性確保）

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
3. **生成/改稿** はテンプレの**必須セクション**を基にしつつ、**設計図3.3の該当No.行を必ず参照**してDNA・冒頭・結論パターンを使用する。記憶や推測で補完しない。本文は **unique_focus を冒頭2段落に必ず反映** する。**「本稿の焦点は〇〇である」を本文の複数セクションで同じ文言のまま繰り返さない**（リードまたは1セクション目で1回のみ。2セクション目以降は「本セクションでは」「〇〇の観点から」等の言い換えで始める。**「ここでは〇〇について、このテーマに応じた観点を整理します。」は使用禁止**）。**記事内で章をまたいで同一の長文を繰り返してはならない**。とくに「理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理する。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえる。」は**リードまたは第1セクションに1回のみ**。第2セクション以降はこの定型句を使わず、**「ここでは〇〇について、このテーマに応じた観点を整理します。」の一文は使用禁止**（2章〜4章で二度と生成しない）。セクション冒頭は具体的な内容（あわせて、また、等）で始める。**再発防止**：llm-out 生成スクリプト（gen_llm_out_31_163.py / generate_full_articles_11_163.py）および gen_ai_governance_from_design.py で、2セクション目以降に上記禁止句を出力しない実装とする。
4. バッチ執筆時は**直前10記事の図表使用履歴**を執筆プロンプトに含め、同じ図の型を3記事連続で使わない。
5. **本文の見出しに「次の一歩」を使わない**。記事末尾の結論ブロック「## 次の一歩」と重複するため。最後の本文セクションは「まとめとアクション」「実装のポイント」等とする（apply_llm_article.py でも本文見出しが「次の一歩」の場合は「まとめとアクション」に置換する）。
6. **文体は全記事でです・ます調**とする。クレバーでプロフェッショナルなトーンを保ち、である調・だ調は使わない。
7. “途中から同一化”の原因（共通パーシャル/include、CMSの本文参照ミス等）を特定し、**テンプレ別に本文を分離** する。
8. 仕上げに、**カテゴリトップ** でテンプレ別フィルタ（Txx）とツリー導線を提供する。
9. **関連記事リンクマップ**（各記事の「関連記事」3件）は次のルールで決める（実装: `scripts/apply_llm_article.py` の `get_nav_and_related`）。
   - **同一カテゴリ（section）は最大1件**。同じセクションだけを並べず、他カテゴリへ飛べるようにする。
   - **残り2件は別カテゴリ**から選び、**テーマ的に近い記事**（設計図のセクション親和性 `SECTION_AFFINITY`）を優先する。
   - 候補は記事番号が「今より大きい」もののみ（前へ戻らない）。新規生成・ナビ差し替え時は `patch_article_nav.py --refresh` で一括反映する。

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
| **カテゴリトップのカード要約** | サブカテゴリを開いた際の記事カードに表示する要約では、**記事タイトルと同一の文言を表示しない**。要約の先頭がタイトルと一致する場合はその部分を除いて表示する（重複防止）。meta description はリード段落から生成し、カード表示時に上記ルールで整形する。 |

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
| 2026-02-09 | 記事要約（meta description）をAIカテゴリと同様にリード段落から生成。apply_llm_article.py を変更し全163記事のHTMLを再適用。カード要約ルール追加：タイトルと同一文言を表示しない。strip_title_from_summary で index カードを更新。 |
| 2026-02-09 | 関連記事リンクマップ見直し：同一カテゴリは最大1件、残り2件は別カテゴリでテーマ親和性を優先。SECTION_AFFINITY を追加し get_nav_and_related を変更。patch_article_nav.py に --refresh を追加。設計図にルール9を追記。 |
| 2026-02-09 | 章をまたぐ同一長文の禁止：定型句「理念で終わらせず…5要素のうち」をリード/第1セクションに1回のみに制限。gen_llm_out_31_163.py と gen_ai_governance_from_design.py で2セクション目以降は短い言い換えのみ出力。設計図・cursor prompt にルールと再発防止を追記。全163記事の llm-out 再生成と HTML 再適用を実施。 |
