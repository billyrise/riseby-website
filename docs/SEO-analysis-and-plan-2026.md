# RISEby.net サイト全体 SEO 分析・計画書（2026年2月）

**目的**: アクセス数の大幅増加と、サイトの広告効果（問い合わせ・成約）の最大化。  
**対象**: 全公開ページ（LP・会社概要・サービス・ブログ 約260+ URL）。  
**視点**: 検索流入の増加 ＋ 流入後のコンバージョン（CVR）向上。

---

## 1. 現状サマリ

### 1.1 サイト構成

| 種別 | URL数 | 主な役割 |
|------|--------|----------|
| LP・コーポ | 4 | トップ、会社概要、プライバシー、404 |
| サービス（ja） | 29 | サービス一覧 + 28サービス詳細（AIガバナンス含む） |
| ブログ | 224+ | ブログトップ、AIガバナンス 163+、AI一般 68 |
| 英語サイト | en/* | トップ・about・privacy・サービス群 |
| **合計** | **260+** |  |

### 1.2 強み（すでにできていること）

- **技術基盤**
  - 全ページ canonical 設定済み
  - OGP（og:title, og:description, og:image）・Twitter Card 設定
  - トップ・about・サービスは hreflang（ja / en / x-default）対応
  - JSON-LD: Organization, WebSite, LocalBusiness, FAQPage（トップ）、Service（サービス）、BlogPosting + BreadcrumbList（AIガバナンス記事）、CollectionPage（カテゴリ）
  - sitemap.xml に全HTMLを包含、priority / changefreq 設定
  - robots.txt で Sitemap 指定、不要パスの Disallow
- **コンテンツ**
  - AIガバナンス特化で 163 本の記事＝ロングテール・専門キーワードの土台が大きい
  - 規制・フレームワーク（EU AI Act, NIST, ISO 42001 等）への言及と参考リンク
  - 記事ごとに前後・関連記事の内部リンク、カテゴリ一覧でのリンク
- **改稿済み**
  - NG表現・英語見出しの一括置換、準拠断定の抑制（revision-report 反映）

### 1.3 課題（アクセス増・広告効果の妨げになっている点）

| 区分 | 課題 | 影響 |
|------|------|------|
| **メタ・OG** | 多数の AIガバナンス記事で description に **Markdown の太字** が残存（例: **Accountability＝…**） | SERP 表示が不自然、クリック率（CTR）低下 |
| **メタ・OG** | 一部記事で description が改行で切れている（development-phase-control, xai-explainability-scope 等） | メタが不正、リッチリザルトや OGP の品質低下 |
| **メタ・OG** | ブログトップの title が「Insights」のみでキーワードが弱い | 検索での露出・ブランド検索以外の流入が取りにくい |
| **構造化** | blog/ai/* は BlogPosting が簡素（publisher, image, articleSection 等なし） | リッチリザルト・記事の評価が弱い |
| **構造化** | blog/ai/* に BreadcrumbList・robots・twitter:title/description/image が未整備の記事あり | クロール効率・SNS シェア時の見え方・パンくず表示の機会損失 |
| **コンバージョン** | 記事内 CTA が「お問い合わせ」のみで、サービス詳細（例: ai_governance.html）へ誘導していない | 興味→検討の導線が弱く、広告効果が限定的 |
| **コンバージョン** | 全ページで og:image が共通 1 枚 | 記事・サービス別のサムネで CTR を上げる余地なし |
| **計測** | GA が GA_MEASUREMENT_ID のまま未設定 | 流入・CVR の可視化ができず改善の根拠がない |
| **計測** | Search Console が YOUR_VERIFICATION_CODE のまま未設定 | 検索クエリ・インデックス状況の把握ができない |
| **コンテンツ** | カテゴリ一覧のカード説明が「本稿の焦点は…」型で類似しがち | 薄い重複コンテンツと見なされるリスク |
| **技術** | トップの WebSite SearchAction が /blog/?q= を指すが検索機能の実装要確認 | 構造化データと実態の不一致 |

---

## 2. ページ種別ごとの詳細分析

### 2.1 トップ（index.html）

| 項目 | 状態 | 推奨 |
|------|------|------|
| title | 「RISEby inc. \| AI・DX・経営戦略の実行特化型コンサルティング \| 東京」 | 問題なし。必要なら「生成AI」「コンサル」を1語追加も可 |
| description | 大手ファーム出身・実行特化・AI戦略等を記載 | 120〜160字程度でキーワード含む現状でOK |
| OGP / Twitter | 設定済み | 問題なし |
| 構造化 | Organization, WebSite, LocalBusiness, FAQPage | 問題なし。WebSite の potentialAction のみ、検索URL実装と一致させる |
| GA / GSC | プレースホルダのまま | **最優先** で実 ID に差し替え |
| hreflang | ja / en / x-default | 問題なし |

### 2.2 サービスページ（例: services/ai_governance.html）

| 項目 | 状態 | 推奨 |
|------|------|------|
| title / description | サービス名・役割が明確 | 問題なし |
| canonical / hreflang | 設定済み | 問題なし |
| JSON-LD Service | 設定済み | 問題なし |
| 内部リンク | フッターから「サービス一覧」→ index#services | ブログ記事からの「AIガバナンス支援はこちら」などコンテキストリンクを増やす |

### 2.3 ブログトップ（blog/index.html）

| 項目 | 状態 | 推奨 |
|------|------|------|
| title | 「Insights \| RISEby Blog」 | **変更推奨**: 「AI・DX・経営戦略 \| RISEby ブログ」などキーワード入り |
| description | あり | キーワード（AI、生成AI、DX、経営戦略）を維持しつつ 120〜155 字 |
| canonical | あり | 問題なし |
| hreflang | なし | en ブログがある場合のみ追加 |
| 構造化 | なし | ItemList で「最新記事」を 5〜10 本列挙するとリッチリザルトの可能性 |
| 内部リンク | カテゴリ・記事へのリンク多数 | 問題なし |

### 2.4 カテゴリページ（blog/ai-governance/index.html, blog/ai/index.html）

| 項目 | 状態 | 推奨 |
|------|------|------|
| title / description | カテゴリ名・役割が分かる | 問題なし |
| CollectionPage / BreadcrumbList | あり | 問題なし |
| カード説明文 | 「本稿の焦点は…」の繰り返しが多い | 記事ごとに要約を 1〜2 文で差別化（手動 or 生成スクリプトで更新） |

### 2.5 AIガバナンス記事（blog/ai-governance/*.html）

| 項目 | 状態 | 推奨 |
|------|------|------|
| canonical / robots | あり | 問題なし |
| title | 「記事名 \| RISEby Blog」 | 問題なし |
| description | **多数で \*\*〜\*\* が残存** | **一括除去**（スクリプト推奨）。155 本程度 |
| description | 一部で改行で切れ・閉じクォート欠落 | **該当ファイルを特定して修正**（development-phase-control, xai-explainability-scope 等） |
| og:description / twitter:description | 上記と同じ問題 | description 修正と同時に統一 |
| BlogPosting / BreadcrumbList | 充実 | 問題なし |
| CTA | 記事下「AIガバナンスの設計・実装支援」→ mailto のみ | **サービスページへのリンクを追加**（/services/ai_governance.html） |
| 本文 | 「要点」など日本語化済み | 問題なし |

### 2.6 AI一般記事（blog/ai/*.html）

| 項目 | 状態 | 推奨 |
|------|------|------|
| BlogPosting | 簡素（author のみ等） | **publisher, image, mainEntityOfPage, articleSection, description** を追加 |
| BreadcrumbList | なし | **追加**（ホーム→ブログ→AI・生成AI→記事名） |
| meta robots | なしの記事あり | **index, follow を明示** |
| twitter:title / twitter:description / twitter:image | なしの記事あり | **追加**（og と同値で可） |
| CTA | 記事ごとに要確認 | テーマに応じて「AI戦略」「生成AI導入」「AIガバナンス」など該当サービスへリンクを増やす |

---

## 3. アクセス数「爆発的増加」のための SEO 計画

### 3.1 フェーズ1: 即時修正（1〜2週間）

| 優先度 | 施策 | 対象 | 期待効果 |
|--------|------|------|----------|
| P0 | **GA ・ GSC の本番設定** | index.html（他ページで共通 head なら1箇所） | 流入・CVR・検索クエリの可視化、今後の改善の前提 |
| P0 | **description の Markdown（\*\*）一括除去** | 全 AIガバナンス記事 | SERP 表示の正常化、CTR 改善 |
| P0 | **description の改行・欠落修正** | development-phase-control, xai-explainability-scope 等、該当全件 | メタの妥当性、クロール・OG の安定 |
| P1 | **ブログトップ title のキーワード化** | blog/index.html | 検索での露出向上（「AI ブログ」「DX 事例」等） |
| P1 | **blog/ai/* の SEO メタ・構造化の統一** | 68 本 | リッチリザルト・SNS シェア・評価の底上げ |

### 3.2 フェーズ2: コンテンツ・内部リンク（1〜2ヶ月）

| 優先度 | 施策 | 対象 | 期待効果 |
|--------|------|------|----------|
| P1 | **ピラーページの整備** | 「AIガバナンスとは」「EU AI Act とは」等のハブ記事を作成し、既存記事へリンク | トピッククラスター化、オーソリティ向上、検索ポテンシャル増 |
| P1 | **カテゴリ一覧のカード説明の差別化** | blog/ai-governance/index.html の各カード | 重複感の軽減、各記事の検索ニーズとの一致 |
| P2 | **記事間のコンテキストリンク増** | 関連記事・サービスへの「詳しくは〇〇」「当社の支援はこちら」 | 滞在時間・PV/セッション・内部リンクの伝播 |
| P2 | **検索キーワードの棚卸し** | 主要 50〜100 クエリを想定し、タイトル・見出し・リードに自然に織り込む | 検索意図との一致、ランキングの安定 |

### 3.3 フェーズ3: リッチリザルト・体験（2〜3ヶ月）

| 優先度 | 施策 | 対象 | 期待効果 |
|--------|------|------|----------|
| P2 | **ブログトップに ItemList（最新記事）** | blog/index.html | リッチリザルトでの表示機会 |
| P2 | **記事ごとに FAQ や HowTo がある場合は構造化** | 該当記事 | FAQ/HowTo リッチリザルトの可能性 |
| P2 | **ページ別 og:image の検討** | 重要記事・サービス（まずは 5〜10 ページ） | SNS・検索プレビューの CTR 向上 |
| P3 | **Core Web Vitals の計測と軽量化** | 全ページ（特に LCP・INP） | ランキング要因・直帰率の改善 |

---

## 4. 広告効果（コンバージョン）最大化の計画

### 4.1 導線設計

| 現状 | 課題 | 施策 |
|------|------|------|
| 記事→mailto のみ | 興味の段階に合った「次の一歩」が足りない | **記事テーマに応じたランディングを追加** |
| フッター「サービス一覧」→ index#services | カテゴリ・記事とサービスが紐づきにくい | **AIガバナンス記事からは /services/ai_governance.html を明示** |

**推奨 CTA の分岐:**

- **AIガバナンス記事**
  - 本文下 CTA: 「AIガバナンスの設計・実装支援」→ **/services/ai_governance.html**（同一ウィンドウ）＋「お問い合わせ」→ mailto（または contact ページ）
- **AI戦略・生成AI導入系（blog/ai）**
  - 該当するサービス（ai_strategy.html, gen_ai_implementation.html 等）へのリンクを CTA または関連リンクに追加
- **ブログトップ・カテゴリ**
  - 目立つ位置に「企業のAIガバナンス支援」「AI・DX コンサルティング」等→サービス一覧 or 代表サービス

### 4.2 ランディング・計測の整理

| 施策 | 内容 |
|------|------|
| **問い合わせを「コンバージョン」として定義** | メール送信 or フォーム送信を 1 CVR に（GA4 でイベント設定） |
| **サービスページ閲覧を「マイクロコンバージョン」に** | 記事→サービス詳細の遷移をイベント or 目標にすると、どの記事が「商談に近い」かを分析可能 |
| **UTM の運用** | 外部広告から来る場合、utm_source / medium / campaign を付与し、どのチャネル・記事が CVR に寄与しているかを見る |

### 4.3 記事内 CTA の具体的変更例

- **現状（例）**  
  「AIガバナンスの設計・実装支援」→ `mailto:contact@riseby.net`
- **推奨**  
  - 主 CTA: 「AIガバナンス支援の詳細を見る」→ `https://riseby.net/services/ai_governance.html`  
  - 副 CTA: 「お問い合わせ」→ `mailto:contact@riseby.net`  

これにより「まず内容を確認してから問い合わせ」という流れを増やし、成約品質と CVR の両方を狙う。

---

## 5. 技術・運用のチェックリスト

### 5.1 すぐ実施可能

- [ ] index.html: `GA_MEASUREMENT_ID` → 本番 GA4 測定ID に変更
- [ ] index.html: `YOUR_VERIFICATION_CODE` → Search Console のメタタグに変更
- [ ] 全 AIガバナンス記事: meta description / og:description / twitter:description / JSON-LD description から `**` を除去（スクリプト一括推奨）
- [ ] 該当記事: description の改行・クォート欠落の修正（development-phase-control, xai-explainability-scope 等）
- [ ] blog/index.html: title を「AI・DX・経営戦略 \| RISEby ブログ」等に変更
- [ ] blog/ai/*.html: robots, twitter:title/description/image, BreadcrumbList, BlogPosting 強化を一括適用（patch_seo 系スクリプトの拡張）

### 5.2 スクリプトで対応推奨

- **description の \*\* 除去**  
  - 対象: blog/ai-governance/*.html の `<meta name="description" content="…">` および og:description, twitter:description, JSON-LD 内の description  
  - 置換: `**` を空文字に（または太字意図の語だけ残して他を削除）
- **blog/ai の head 統一**  
  - patch_seo_article_heads.py のロジックを blog/ai 用に流用し、robots / Twitter / BreadcrumbList / BlogPosting（publisher, image, articleSection 等）を付与

### 5.3 継続運用

- **Sitemap**  
  - 新規・更新時に generate_sitemap.py を実行し、lastmod を更新
- **Search Console**  
  - インデックス状況・検索クエリ・クリック数を月次で確認し、description やタイトルの A/B 感覚の調整
- **GA4**  
  - イベント（問い合わせ、サービスページ閲覧）を設定し、参照元・ランディングページ別の CVR を確認

---

## 6. 期待される効果（目安）

| 施策群 | 想定効果 |
|--------|----------|
| メタ修正（\*\* 除去・改行修正） | SERP 表示の正常化 → CTR の数〜十% 改善の余地 |
| ブログトップ・blog/ai の SEO 統一 | インデックス・評価の安定、ロングテール検索の取りこぼし削減 |
| ピラーページ・内部リンク | 中期的に「AIガバナンス」「EU AI Act」等の検索で上位表示されるページが増える可能性 |
| CTA のサービスページ誘導 | 記事→サービス詳細→問い合わせの割合増、広告効果の可視化 |
| GA・GSC 本番設定 | 上記すべての効果測定と、次打ち手の根拠が得られる |

---

## 7. 次のアクション（優先順）

1. **P0**: GA ・ GSC の本番ID反映（1日）
2. **P0**: AIガバナンス記事の description から `**` 一括除去 ＋ 改行・欠落の修正（スクリプト＋手動、2〜3日）
3. **P1**: ブログトップ title 変更（0.5日）
4. **P1**: blog/ai の SEO メタ・構造化の一括パッチ（スクリプト拡張、1〜2日）
5. **P1**: AIガバナンス記事の CTA に「サービス詳細」リンクを追加（テンプレ修正 or スクリプト、1日）
6. **P2**: ピラーページ・カード説明の差別化・ItemList 等は、上記が落ち着いたあとで実施

以上で、アクセス数拡大と広告効果の最大化に向けた「詳細レベル」の分析と計画を一通りカバーしています。実装時は `docs/ai-governance-rules-and-implementation-check.md` や既存の `patch_seo_article_heads.py` と整合させると運用しやすいです。
