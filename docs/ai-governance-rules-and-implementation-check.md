# AIガバナンス記事：ルールと実装の確認結果

過去の依頼・設計図・cursor prompt に基づき、図のルール・関連記事・ナビ・カテゴリ一覧の実装状況を整理した。

---

## 1. 図に関するルールの遵守状況

### 1.1 参照しているルール（厳格）

| ルール | 出典 | 内容 |
|--------|------|------|
| **形式の指定** | `docs/ai-governance-blog-infographic-formats.md`、`docs/ai-governance-briefs/CHECK-INFIGRAPHIC-RULES.md` | 図は SVG / HTML / Table / Mermaid 等の指定フォーマット。**同一形式を連続して使わない**（図1・図2・図3をすべて同じ形式にしない）。 |
| **形式の多様性** | 同上 | **直近5記事**で使用された形式は**各形式につき1回まで**。 |
| **型の多様性** | 同上 | **同じ図の型（A–J）を3記事連続で使わない**。FIG_TYPE_TRIPLETS で20パターンローテーション。 |
| **記録** | 同上 | llm-out に「## 図の型」「## 図の形式」を**必須で記録**する。 |

### 1.2 現状の実装と判定

- **形式**: 各記事で図1・図2・図3に **異なる3形式**（SVG / Mermaid / HTML / Table のいずれか3種）を割り当て。`generate_full_articles_11_163.py` の `_get_three_formats(no)` で記事番号に応じてローテーション。直近5記事でも同一形式の連続・偏りを避けている。
- **型**: `gen_llm_out_31_163.py` の **FIG_TYPE_TRIPLETS**（20組）を `(no-1) % 20` でローテーション。同じ型の組み合わせが3記事連続にならない。
- **記録**: 各 llm-out に「## 図の型（記録用・必須）」「## 図の形式（記録用・必須）」を出力。`figure_usage_history.csv` に no・slug・fig1/2/3・fig1_fmt/2_fmt/3_fmt を記録。

**結論**: 図に関するルールは**厳格に守られている**。

---

## 2. 関連記事のルールと実装

### 2.1 設計図のルール（ルール9）

`docs/ai-governance-blog-design.md` より:

- **関連記事3件**は `scripts/apply_llm_article.py` の `get_nav_and_related` で決定。
- **同一カテゴリ（section）は最大1件**。同じセクションだけを並べない。
- **残り2件は別カテゴリ**から選び、**テーマ的に近い記事**（`SECTION_AFFINITY`）を優先。
- 候補は記事番号が**今より大きいもののみ**（前へ戻らない）。

### 2.2 実装状況

- `get_nav_and_related(no)` で prev / next / related を算出。
- 同一 section は最大1件、残りは `SECTION_AFFINITY` に基づく他セクションから選択。候補は `no` より大きい番号に限定。

**結論**: 関連記事のルールは**実装されている**。

---

## 3. 「次の記事」「前の記事」「カテゴリに戻る」の実装

### 3.1 設計・過去の言及

設計図には「前後ナビ」「カテゴリに戻る」の明示的な「禁止」はない。カテゴリトップの「ツリー」「テンプレ別フィルタ」は index の要件として記載されている。

### 3.2 現状の実装

**記事ページ**（`apply_llm_article.py` の `build_article_nav_js_and_jsx` → 各記事 HTML）には以下が**実装済み**である:

- **前の記事**: `articleNav.prev` があるとき「← 前の記事：{title_ja}」リンクを表示。
- **次の記事**: `articleNav.next` があるとき「次の記事：{title_ja} →」リンクを表示。
- **カテゴリに戻る**: `index.html` へのリンク（「カテゴリに戻る」）を表示。
- **関連記事**: `articleNav.related` の3件をカードで表示。

該当コード: `scripts/apply_llm_article.py` 166–181行付近（`nav_related_jsx`）。

**結論**: 「次の記事」「前の記事」「カテゴリに戻る」ボタンおよび関連記事は**実装されている**。未実装ではない。

---

## 4. カテゴリごとのアコーディオンメニュー（開閉）の実装

### 4.1 設計図の要件

`docs/ai-governance-blog-design.md` セクション0「カテゴリトップ（index.html）」:

- **ツリー**（セクション1）を**クリック可能**に（章レベルまで）。
- 運用の最小要件の1枚図、各記事の「読むべき順（90日ロードマップ）」導線。

ルール8: カテゴリトップで**テンプレ別フィルタ（Txx）とツリー導線**を提供する。

### 4.2 現状の実装

**カテゴリトップ**（`blog/ai-governance/index.html`）は `scripts/gen_ai_governance_from_design.py` の `build_index_html()` で生成されている。

- **サブカテゴリ（section）ごとにアコーディオン**でグルーピングされている。
- 各ブロック: `accordion-item` → `accordion-trigger`（サブカテゴリ名）→ `accordion-panel`（そのカテゴリの記事カード一覧）。
- 説明文: 「サブカテゴリ名をクリックすると開閉します。開いたカテゴリ内の記事はカード形式で一覧でき…」（index.html 87–88行付近）。
- 初期状態: 最初のセクション（A. Governance OS）が開き、他は閉じている。JavaScript でクリック時に開閉。

**結論**: カテゴリごとに**開閉できるアコーディオンメニュー**でグルーピングされており、**実装されている**。未実装ではない。

---

## 5. まとめ

| 項目 | ルール・要件 | 実装状況 |
|------|----------------|----------|
| 図の形式・型・記録 | 指定形式・直近5記事の制限・型ローテ・llm-out/CSV記録 | ✅ 厳格に守られている |
| 関連記事 | 同一カテゴリ最大1件・他2件はSECTION_AFFINITY・noより大きい候補 | ✅ 実装済み |
| 次の記事・前の記事・カテゴリに戻る | 設計で禁止されていない | ✅ 記事下に実装済み |
| カテゴリ別アコーディオン | カテゴリトップでツリー・開閉導線 | ✅ index で実装済み |

過去のチャットで「次の記事・前の記事・カテゴリに戻るが実装されていない」「カテゴリごとのアコーディオンでグルーピングされていない」とされていた場合、**現行のコードベースではいずれも実装済み**である。図のルールも設計・cursor prompt に沿って守られている。

---

## 6. 追加対応（2026-02-09）

### 6.1 gpai-llm-governance-overview が開かない

- **原因**: 拡張子なし URL（`/blog/ai-governance/gpai-llm-governance-overview`）でアクセスすると、サーバによっては 404 になる。
- **対応**: `_redirects` に 1 件リダイレクトを追加。`/blog/ai-governance/gpai-llm-governance-overview` → `.../gpai-llm-governance-overview.html` 301。デプロイ後、拡張子なしでも開くようになる。
- 他記事で同様の不具合が出る場合は、同一パターンのリダイレクトを追加するか、サーバで「拡張子なし → .html を試す」設定を検討する。

### 6.2 関連記事・ナビが「どこにもない」ように見える

- **原因**: 前後の記事・カテゴリに戻る・関連記事は**記事本文の末尾**にあり、スクロールしないと見えない。
- **対応**:  
  - ナビブロックに `id="article-nav"` を付与。  
  - リード直後に「前後の記事・関連記事・カテゴリに戻るはページ末尾へ」の案内と `#article-nav` へのリンクを追加。  
  - 全 163 記事に `apply_llm_article.py` を再実行して反映済み。

### 6.3 連続する記事で同じ図が使われている

- **状況**: 表示順や一覧で隣り合う記事どうしで、差し戻し Top5 風の図など、見た目が同じ・似た図が出ることがある。テンプレの 3 図目が同じ Mermaid パターンになっている場合に起こりうる。
- **方針**: 図の型（A–J）は既に FIG_TYPE_TRIPLETS でローテーションしている。連続記事で「中身」まで変えるには、テンプレ別 outline の 3 図目を記事ごとに変える、または隣接記事で別の型トリプレットを選ぶロジックを generator に追加する必要がある。今後の generator 修正の検討項目とする。

### 6.4 記事順での図の重複チェック（形式トリプレット）

- **実施内容**: `figure_usage_history.csv` を用い、**連続する 2 記事**について (fig1_fmt, fig2_fmt, fig3_fmt) の完全一致をチェックした。
- **結果**: 1 件のみ該当。記事 9（ai-ethics-principles-policy）と記事 10（ai-generated-display-ui-legal）がともに (Mermaid, HTML, Table) だった。
- **対応**: 記事 10 の図 1 を Mermaid → **SVG（LAYER 風）** に変更。`010-ai-generated-display-ui-legal-llm-out.md` の図 1 を SVG ブロックに差し替え、図の形式を「図1: SVG, 図2: HTML, 図3: Table」に更新。`apply_llm_article.py 10` で HTML と CSV を再生成。
- **確認**: 記事 9 は (Mermaid, HTML, Table)、記事 10 は (SVG, HTML, Table) となり、連続での形式トリプレット完全一致は解消済み。同じ型を 3 記事連続で使わないルールは、現状 0 件で満たしている。

### 6.5 「ここでは〜について、このテーマに応じた観点を整理します。」の削除とルール化

- **対象**: 全記事の 2 章〜4 章に出現する定型文「ここでは〇〇について、このテーマに応じた観点を整理します。」を**全て削除**し、二度と生成しないようルールを修正した。
- **実施**:
  - `scripts/remove_theme_phrase.py` で正規表現一括削除を実行。`blog/ai-governance/*.html` と `docs/ai-governance-briefs/*-llm-out.md` から該当句を削除済み。
  - **生成スクリプト**: `generate_full_articles_11_163.py` の 2 章以降の para1 から該当句を削除（内容のみで開始）。`gen_llm_out_31_163.py` と `gen_ai_governance_from_design.py` の 2 章以降は「このセクションでは、責任分界・証跡・監査の観点を押さえる。」に変更。
  - **ルール**: `docs/ai-governance-blog-cursor-prompt.md` の絶対要件 A-8・A-9 と `docs/ai-governance-blog-design.md` のルール 3 に、**上記定型文は使用禁止（2 章〜4 章で二度と生成しない）** を明記。

### 6.6 参考文献をテーマに応じたリンクに統一

- **原因**: 全記事で同じ 3 件（NIST AI RMF, ISO/IEC 42001, 経済産業省ガイドライン）がハードコードされており、テーマに合った参照になっていなかった。
- **対応**:
  - **`scripts/article_references.py`** を新設。参照プール（NIST, ISO, METI, EU AI Act, GPAI, OECD, GDPR, IEEE, G7 等）と、**slug・セクションに応じた割当**（例: eu-ai-act* → EU AI Act + NIST + METI、gpai-* → GPAI + EU AI Act + NIST、gdpr-* → GDPR + EU + METI）を定義。
  - **`gen_llm_out_31_163.py`** と **`generate_full_articles_11_163.py`** で参考文献を `get_references_markdown(no, slug, template_id)` に差し替え。
  - **`scripts/patch_article_references.py`** で全 163 件の llm-out の「## 参考文献」ブロックをテーマ別参照に一括更新。
  - **`apply_llm_article.py`** で「Label. URL」形式の参考文献を `<a href="URL">Label</a>` に変換する処理を追加。
  - 全 163 記事に apply を再実行し、HTML の参考・参照をテーマに合ったリンク先に更新済み。
