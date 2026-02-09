# RISEby.net コンテンツ棚卸し（2026-02-09）

## 1) ページ一覧（CSV風）

| URL（推定） | ファイルパス | 言語 | 種別 | タイトル（抜粋） |
|------------|--------------|------|------|------------------|
| https://riseby.net/ | index.html | ja | LP | RISEby inc. \| AI・DX・経営戦略の実行特化型コンサルティング |
| https://riseby.net/about.html | about.html | ja | company | 会社概要 |
| https://riseby.net/privacy.html | privacy.html | ja | legal | プライバシーポリシー |
| https://riseby.net/404.html | 404.html | ja | other | ページが見つかりません |
| https://riseby.net/blog/index.html | blog/index.html | ja | blog | Insights |
| https://riseby.net/blog/ai/index.html | blog/ai/index.html | ja | blog_ai | AI・生成AIの記事一覧 |
| https://riseby.net/blog/ai-governance/index.html | blog/ai-governance/index.html | ja | blog_ai_governance | AIガバナンス記事一覧 |
| https://riseby.net/services/index.html | services/index.html | ja | service | サービス一覧 |
| https://riseby.net/services/ai_governance.html | services/ai_governance.html | ja | service | AIガバナンス・リスク管理 |
| … | services/*.html | ja | service | 各サービス名（計28本） |
| … | blog/ai-governance/*.html | ja | blog_ai_governance | 各記事タイトル（計155本） |
| … | blog/ai/*.html | ja | blog_ai | 各記事タイトル（計68本） |

**集計**
- **LP/コーポ**: 1（index）, 1（about）, 1（privacy）, 1（404）
- **サービス（日本語）**: 29（index + 28サービス）
- **ブログ（日本語）**: ブログトップ 1、AIガバナンス 155、AI一般 68 → 計 224 ブログURL
- **英語サイト**: en/index, en/about, en/privacy, en/services/* → 別枠（本改稿では対象外とする場合あり）

※ 日本語メインサイトの本文が含まれるファイルは、上記のうち **index.html, about.html, privacy.html, services/*.html, blog/index.html, blog/ai/index.html, blog/ai-governance/index.html, blog/ai-governance/*.html（155）, blog/ai/*.html（68）** で約 **260 ファイル**。

---

## 2) AIガバナンス記事一覧（タイトル / 日付 / ファイル / 問題タグ）

全記事とも **datePublished: 2026-02-05**（一括生成と推測）。問題タグは次のとおり。

- **template**: 冒頭・「2.設計のポイント」・「3.監査接続」・CTA が他記事とほぼ同一テンプレ
- **ng_phrase**: 「一気通貫」「包括的」「サポートします」「回せるようにします」等のNG表現を含む
- **en_heading**: 本文またはフッターに英語見出し（Key Point, Services, Company）が残る
- **compliance_risk**: 準拠・保証・コンプライアンス達成の断定リスク（該当時は明記）
- **citation**: 出典不明の数値・罰金表現の有無
- **reference_ok**: 参考資料セクションに権威ソースが3つ以上ある → 多くの記事でOK

以下、**タイトル / 日付 / ファイル / 問題タグ** を一覧化（抜粋は先頭40件＋末尾で件数のみ。全155件はファイルパス一覧で補足）。

| タイトル | 日付 | ファイル | 問題タグ |
|----------|------|----------|----------|
| AIアクセス制御：ゼロトラストでどう守るか | 2026-02-05 | blog/ai-governance/ai-access-control-zerotrust.html | template, ng_phrase, en_heading |
| セキュリティ教育：現場が守れるルール化 | 2026-02-05 | blog/ai-governance/security-education-rules.html | template, ng_phrase, en_heading |
| 合成データ：有効性とプライバシーリスク | 2026-02-05 | blog/ai-governance/synthetic-data-privacy.html | template, ng_phrase, en_heading |
| 倫理×セキュリティ：統合統制の作り方 | 2026-02-05 | blog/ai-governance/ethics-security-unified-control.html | template, ng_phrase, en_heading |
| 変更管理：導入時の抵抗と対処 | 2026-02-05 | blog/ai-governance/change-management-resistance.html | template, ng_phrase, en_heading |
| インセンティブ設計：スピードと統制の両立 | 2026-02-05 | blog/ai-governance/incentive-design-speed-control.html | template, ng_phrase, en_heading |
| 継続的評価：モデル更新とドリフトの監督 | 2026-02-05 | blog/ai-governance/continuous-evaluation-drift.html | template, ng_phrase, en_heading |
| データ品質（GIGO対策）：統制に落とす方法 | 2026-02-05 | blog/ai-governance/data-quality-gigo.html | template, ng_phrase, en_heading |
| コントロールテストの自動化：継続的監査（CCM） | 2026-02-05 | blog/ai-governance/control-test-automation-ccm.html | template, ng_phrase, en_heading |
| 金融業界：AIガバナンス（規制×MRM×説明責任） | 2026-02-05 | blog/ai-governance/industry-finance-ai-governance.html | template, ng_phrase, en_heading |
| インシデント対応：業界別の"報告/説明"の癖 | 2026-02-05 | blog/ai-governance/incident-response-by-industry.html | template, ng_phrase, en_heading |
| Evidence Bundle：監査法人が欲しい"束ね方" | 2026-02-05 | blog/ai-governance/evidence-bundle-audit.html | template, ng_phrase, en_heading |
| デプロイ前チェックリストとリリース承認 | 2026-02-05 | blog/ai-governance/deploy-checklist-release-approval.html | template, ng_phrase, en_heading |
| 英国・シンガポール等：ソフトロー型ガバナンスの実装比較 | 2026-02-05 | blog/ai-governance/uk-singapore-soft-law.html | template, ng_phrase, en_heading |
| AIインシデント対応：エスカレーションと当局/顧客説明 | 2026-02-05 | blog/ai-governance/ai-incident-response-escalation.html | template, ng_phrase, en_heading |
| バイアスと公平性：人事・与信・医療での実務 | 2026-02-05 | blog/ai-governance/bias-fairness-hr-credit-healthcare.html | template, ng_phrase, en_heading |
| EU AI Act 透明性義務：通知・表示・情報提供の設計 | 2026-02-05 | blog/ai-governance/eu-ai-act-transparency.html | template, ng_phrase, en_heading |
| 例外管理：現場スピードを落とさない統制 | 2026-02-05 | blog/ai-governance/exception-management-control.html | template, ng_phrase, en_heading |
| AI×サイバー：脅威モデルの作り方 | 2026-02-05 | blog/ai-governance/ai-cyber-threat-model.html | template, ng_phrase, en_heading |
| ガバナンスの継続的改善：監査→改善→再評価の循環 | 2026-02-05 | blog/ai-governance/governance-continuous-improvement.html | template, ng_phrase, en_heading |
| 子会社・中小向け軽量ガバナンス：ミニマム統制 | 2026-02-05 | blog/ai-governance/subsidiary-sme-lightweight-governance.html | template, ng_phrase, en_heading |
| 翌年度計画：規制追随と改善サイクルの作り方 | 2026-02-05 | blog/ai-governance/next-year-planning-cycle.html | template, ng_phrase, en_heading |
| データ共有（共同研究/共同開発）：契約と統制 | 2026-02-05 | blog/ai-governance/data-sharing-joint-research.html | template, ng_phrase, en_heading |
| 特許・知財とAI開発：ガバナンスの要点 | 2026-02-05 | blog/ai-governance/ip-patent-ai-development.html | template, ng_phrase, en_heading |
| EU AI Act 禁止領域：禁止規定と設計上の回避策 | 2026-02-05 | blog/ai-governance/eu-ai-act-prohibited.html | template, ng_phrase, en_heading |
| 顧客提供AI（B2B）：SLA・説明・監査要求への対応 | 2026-02-05 | blog/ai-governance/customer-facing-ai-b2b.html | template, ng_phrase, en_heading |
| 公共セクター：透明性と説明責任の設計 | 2026-02-05 | blog/ai-governance/industry-public-sector.html | template, ng_phrase, en_heading |
| 継続的適合性評価：監査対応を運用に組み込む | 2026-02-05 | blog/ai-governance/continuous-conformity-assessment.html | template, ng_phrase, en_heading |
| 監査ダッシュボード：取締役会に刺さる指標 | 2026-02-05 | blog/ai-governance/audit-dashboard-board-metrics.html | template, ng_phrase, en_heading |
| データ漏えい：入力・出力・ログの統制設計 | 2026-02-05 | blog/ai-governance/data-leakage-control-design.html | template, ng_phrase, en_heading |
| ディープフェイク対策：企業ブランドを守る統制 | 2026-02-05 | blog/ai-governance/deepfake-countermeasures.html | template, ng_phrase, en_heading |
| インシデント対応：AIの切り離し手順と説明責任 | 2026-02-05 | blog/ai-governance/incident-response-ai-isolation.html | template, ng_phrase, en_heading |
| バージョン管理：変更時の再評価とロールバック | 2026-02-05 | blog/ai-governance/version-management-reroll.html | template, ng_phrase, en_heading |
| "ガバナンス運用OS"総まとめ：最短導入ロードマップ | 2026-02-05 | blog/ai-governance/governance-os-summary-roadmap.html | template, ng_phrase, en_heading |
| 次年度計画：規制追随・人材・投資の優先順位（総括） | 2026-02-05 | blog/ai-governance/next-year-plan-priority-summary.html | template, ng_phrase, en_heading |
| 外部委託（BPO/SI）とAI：責任分担と証跡 | 2026-02-05 | blog/ai-governance/outsourcing-bpo-si-ai.html | template, ng_phrase, en_heading |
| モデル改ざん・毒入れ：検知と防止の実装 | 2026-02-05 | blog/ai-governance/model-poisoning-detection.html | template, ng_phrase, en_heading |
| 中央集権 vs 連邦型：グローバル企業の最適解 | 2026-02-05 | blog/ai-governance/centralized-federated-global.html | template, ng_phrase, en_heading, 「最適解」最大級 |
| 越境データ契約：法域ごとの契約設計 | 2026-02-05 | blog/ai-governance/cross-border-data-contract.html | template, ng_phrase, en_heading |
| 機密情報：入力禁止だけで終わらせない設計 | 2026-02-05 | blog/ai-governance/confidential-input-design.html | template, ng_phrase, en_heading |
| …（以下同様のタグが続く） | 2026-02-05 | blog/ai-governance/*.html | template, ng_phrase, en_heading |
| EU AI Act 総論：義務の全体像と段階適用の読み方 | 2026-02-05 | blog/ai-governance/eu-ai-act-overview.html | template, ng_phrase, en_heading, reference_ok |
| ISO/IEC 42001（AIMS）導入の要点と落とし穴 | 2026-02-05 | blog/ai-governance/iso-42001-aims-introduction.html | template, ng_phrase, en_heading, reference_ok |
| AI保証（Assurance）と監査の違い：使い分け | 2026-02-05 | blog/ai-governance/ai-assurance-vs-audit.html | template, ng_phrase, en_heading, タイトルに「保証」固有名詞 |

**重大リスク抽出（AIガバナンス記事）**
- **規制・標準の誤記**: 現状、明らかな誤記は未検出。表記ゆれ（ISO 42001 / ISO/IEC 42001）は統一推奨。
- **過剰断定**: 「準拠できます」「対応したガバナンスを実現」はサービスページ（ai_governance.html）の説明に近い表現が要注意。ブログ本文では「推奨」「〜につながります」程度に留まっている記事が多数。
- **出典不明の数値**: 主に blog/ai/ 側（ai-healthcare-pharma の「10年・1,000億円」「数億円規模」等）。AIガバナンス記事内では根拠なしの罰金・億円表記は少数。
- **曖昧な定義・責任分界**: 多くの記事で「誰が何を記録し、誰が説明するか」には言及あり。RACI や「監査可能性」まで落ちている記事と、抽象で終わっている記事が混在 → 改稿時に「運用（証跡・継続評価・是正）」へ寄せる。

**AIガバナンス 全ファイルパス（155本）**  
`blog/ai-governance/` 配下の .html はすべて上記「問題タグ」の対象。一覧は `content-inventory-2026-02-09.md` と同じリポジトリ内で、必要なら `blog/ai-governance/*.html` のリストを別CSVで出力可能。

---

## 3) NG表現の頻出ランキング（上位20）

全日本語HTML（en/ 除く）を対象にカウントした結果。

| 順位 | 出現回数 | NG表現 | 備考 |
|------|----------|--------|------|
| 1 | 351 | 一気通貫 | ブログ本文・CTAで「一気通貫で回せる」「一気通貫でサポート」 |
| 2 | 269 | 包括的 | フッター「包括的に解決するコンサルティングファーム」等 |
| 3 | 265 | Services | フッター見出し（英語） |
| 4 | 240 | Company | フッター見出し（英語） |
| 5 | 186 | Key Point | ブログ記事内コンポーネント見出し（英語） |
| 6 | 174 | サポートします | CTA「一気通貫でサポートします」 |
| 7 | 153 | 回せるようにします | 「申請・承認・記録・例外管理を一気通貫で回せるようにします」 |
| 8 | 46 | 実現 | 「実現します」「実現する」 |
| 9 | 43 | 最適化 | ブログ・サービスで「最適化」 |
| 10 | 40 | できます | 「〜できます」連打 |
| 11 | 22 | 3つの | 箇条書き・「3つの〜」テンプレ |
| 12 | 16 | 保証 | 固有名詞（Assurance）含む。断定の「保証」は要置換 |
| 13 | 13 | 可能に | 「〜を可能に」 |
| 14 | 13 | するだけ | 「〜するだけ」煽り型 |
| 15 | 9 | 伴走 | 「伴走支援」等 |
| 16 | 3 | シームレス | カタカナ過密 |
| 17 | 3 | 完全に | 最大級・断定 |
| 18 | 3 | 必ず | 断定 |
| 19 | 2 | 準拠 | 準拠断定リスク |
| 20 | 1 | 革新的 | バズワード |
| （同率） | 1 | 最先端 | バズワード |
| （同率） | 1 | 今すぐ | 煽りテンプレ |

**0件だったが禁止リストに入れておく表現**  
迅速に、世界水準、変革を加速、コンプライアンス達成

---

## 4) 次のアクション（改稿手順への入力）

1. **全ページ**: 上記「ページ一覧」の日本語ファイルを対象に、NG表現の置換・削除と「固有の一文」の追加。
2. **AIガバナンス記事**: まず 155 本を Type C テンプレ（実務の問い→定義→運用要件5点→マッピング→失敗パターン→チェックリスト→参考資料）に沿って改稿し、準拠断定・出典なし数値・英語見出しを解消。
3. **共通コンポーネント**: フッターの「包括的に解決」「Services」「Company」、ブログ共通の「一気通貫でサポートします」「Key Point」を一括で日本語化・表現変更する候補とする。
4. **サービス・LP**: index.html, about.html, services/ai_governance.html 等は Type A に沿って改稿。

以上で、棚卸→分類→問題タグ付け→NG表現ランキングまでを完了とする。
