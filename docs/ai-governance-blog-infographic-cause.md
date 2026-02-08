# AIガバナンスブログ：インフォグラフィック欠如の原因

## 計画書の要件（1.2 記事仕様）

| 項目 | 方針 |
|------|------|
| **図表** | 1記事あたり **2〜4要素**（Mermaid/SVG/カード/KeyPoint）。"箇条書きだけ"にしない。 |

## 原因の整理

155本のほとんどにインフォグラフィックが含まれていない理由は、**生成スクリプト（`generate_ai_governance_blog.py`）が「図表」を1要素しか出力していない**ためです。

### 1. データ側：`make_template_article` が図表データを返していない

- **現状**: 返しているのは `(title, slug, category, living, lead, sections, kp_title, kp_text, meta)` のみ。
- **不足**: Mermaid のチャート文字列、カード用の見出し・項目リスト、SVG 用のパラメータなど、**図表用のデータを一切持っていない**。
- そのため、テンプレート側で「どこに何を描くか」を決められない。

### 2. テンプレート側：`render_article` に図表コンポーネントがない

- **現状**: 生成される HTML の React 部分には **KeyPoint コンポーネントだけ** が定義されている。
- **不足**:
  - **MermaidDiagram** コンポーネントが定義されていない（サンプル記事の `gpai-llm-governance-overview.html` にはあるが、生成テンプレートには含めていない）。
  - **カード／figure（figcaption 付き）** のようなインフォグラフィック用コンポーネントもない。
- mermaid.min.js と .mermaid の CSS は読み込んでいるが、**Mermaid を表示する React コンポーネントが存在しない**ため、図は一切描画されない。

### 3. 本文組み立て：`build_body_html` が図表を挿入していない

- **現状**: `body_content` は「リード ＋ h2/段落」のみ。その後に KeyPoint とまとめを追加している。
- **不足**: 本文のどこにも、MermaidDiagram やカード用の JSX を差し込む処理がない。  
  → 結果として、図表要素は **KeyPoint の 1 つだけ** になり、計画書の「2〜4要素」を満たしていない。

## サンプル記事との対比

| 要素 | サンプル（例: gpai-llm-governance-overview.html） | 生成記事（#8〜#160） |
|------|---------------------------------------------------|----------------------|
| KeyPoint | ✅ あり | ✅ あり |
| MermaidDiagram | ✅ 定義＋使用（chart を渡して表示） | ❌ コンポーネント未定義・未使用 |
| カード（CompareCards 等） | ✅ 定義＋使用（figure/figcaption） | ❌ コンポーネント未定義・未使用 |
| SVG（ControlLayersSvg 等） | ✅ 定義＋使用 | ❌ コンポーネント未定義・未使用 |
| **図表要素の数** | **2〜4** | **1（KeyPoint のみ）** |

## 結論

- **根本原因**: 155本分の記事を生成する際、
  1. 図表用の**データ**（Mermaid コード・カード内容など）を用意していない。
  2. 生成 HTML に **MermaidDiagram / カード / SVG 用の React コンポーネント** を含めていない。
  3. 本文組み立てで、それら図表を **挿入する処理** をしていない。

そのため、計画書で求めている「1記事あたり 2〜4 要素（Mermaid/SVG/カード/KeyPoint）」のうち、**KeyPoint 以外のインフォグラフィックがほぼ全ての記事で欠けている**状態になっている。

## 対応済み（2026年2月）

- **計画書**（1.2・4.1）：1記事あたり **必ず3要素**（Mermaid・カード・KeyPoint を各1つ）と明記。
- **生成プログラム**（`generate_ai_governance_blog.py`）：
  1. テンプレートに **MermaidDiagram** コンポーネントを追加。`const mermaidChart = \`...\`` でチャートを渡し、本文に `<MermaidDiagram chart={mermaidChart} />` を挿入。
  2. 記事データに **mermaid_chart, card_caption, card_left_title, card_left_items, card_right_title, card_right_items** を追加。`make_template_article` および #6・#7 のフル記事でこれらを返す／持つようにした。
  3. **カード**は figure/figcaption ＋ 2列（観点・要件 / 実装・証跡）のJSXを `build_body_html` で組み立て、`__CARD__` プレースホルダーを本文に差し替え。
  4. 本文は「セクション1 → Mermaid → セクション2 → カード → セクション3 → KeyPoint → まとめ」の順で、必ず3つのインフォグラフィックが含まれる。
