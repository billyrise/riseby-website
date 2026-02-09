# AIガバナンス記事 執筆ブリーフ

各記事を **1本ずつ**、Cursor に **十分な情報を全て渡して** 本文とインフォグラフィック（Mermaid）を生成するためのブリーフを格納するディレクトリです。（記事は Cursor 内で作成。）

## 記事生成の統一フロー（1–163）

全163記事の **llm-out と HTML** は次の1本のロジックで生成する。

1. **llm-out の一括生成**（設計図・テンプレ別図1・同一フォーマット）:
   ```bash
   python3 scripts/gen_llm_out_31_163.py
   ```
2. **HTML への反映**（1–163 を順に apply）:
   ```bash
   for no in $(seq 1 163); do pad=$(printf "%03d" $no); f=$(ls docs/ai-governance-briefs/${pad}-*-llm-out.md 2>/dev/null | head -1); [ -n "$f" ] && python3 scripts/apply_llm_article.py $no "$f"; done
   ```
3. **カテゴリトップ index.html** のみ別スクリプト:
   ```bash
   python3 scripts/gen_ai_governance_from_design.py
   ```

- 記事の直接HTML生成（旧 gen_first10_ai_governance / gen_ai_governance_from_design の記事ループ）は廃止し、上記に統一済み。

## 使い方

### 1. ブリーフの生成

**1記事分だけ**（例: 記事番号 1）:

```bash
# ファイルに出力
python3 scripts/write_article_brief.py 1

# 標準出力に出力（Cursor 内でそのまま渡す）
python3 scripts/write_article_brief.py 1 --stdout
```

**全163件を一括**:

```bash
python3 scripts/write_article_brief.py
```

生成されるファイル: `NNN-<slug>.md`（例: `001-accountability-incident-design.md`）

### 2. 記事＋インフォグラフィックの生成（Cursor 内で作成）

記事本文とインフォグラフィックは **Cursor 内で** 作成する。

1. ブリーフ（`NNN-<slug>.md`）を開き、その内容を **そのまま** Cursor の AI に渡す。
2. ブリーフ内の「出力形式」に従い、**マークダウン**で以下を出力させる:
   - リード（1段落）
   - 本文（見出しと段落。図1・図2・図3の直前に「ここに図Nを挿入」と記載）
   - 図1・図2・図3は **指定フォーマット**（SVG / HTML / Table / **Mermaid** / Canvas / Vega-Lite / Plotly / DOT / PlantUML 等）で出力。**同一形式を連続して使わない**。形式は **docs/ai-governance-blog-infographic-formats.md**（30種類の書き方）を参照。
   - 「図の型（記録用・必須）」（例: 図1: D, 図2: B, 図3: G）と「図の形式（記録用・必須）」（例: 図1: SVG, 図2: HTML, 図3: Table）
   - 固有の一文、チェックリスト、参考文献、次の一歩
3. **直前に生成された5記事で使用された形式は、各形式につき1つまでしか使えない**。多様なインフォグラフィックを必ず使用すること。
4. 出力を `docs/ai-governance-briefs/NNN-<slug>-llm-out.md` に保存する。

Cursor の AI には「**ビジネスプロフェッショナルとして最高品質**のものを作成する」「図は指定フォーマット（SVG/HTML/Table/Mermaid等、同一形式の連続使用禁止）で書く」ことを指示すること。

### 3. HTML への反映

Cursor で作成した出力をファイルに保存したあと:

```bash
python3 scripts/apply_llm_article.py <記事番号> <作成した出力ファイル（*-llm-out.md）>
```

例:

```bash
python3 scripts/apply_llm_article.py 1 docs/ai-governance-briefs/001-accountability-incident-design-llm-out.md
```

標準入力から渡す場合:

```bash
python3 scripts/apply_llm_article.py 1 < llm_output.md
```

## ブリーフに含まれる情報

- 設計図 3.3 の該当行（slug, title_ja, unique_focus, 読者・目的・深さ・スタイル, Op, Co）
- テンプレ（T01–T32）の Points / Infographics / Outline（設計図セクション2）
- 冒頭パターン（Op 1–10）・結論パターン（Co 1–5）の説明と例
- 直前10記事の図表使用履歴（重複回避用）
- 図の型ライブラリ（A–J）
- 執筆ルール（固有の一文、断定、数値、運用5要素、禁止事項）
- 出力形式（マークダウンの見出し・ブロックの指定）

## 参照

- 設計図: `docs/ai-governance-blog-design.md`
- Cursor 執筆プロンプト: `docs/ai-governance-blog-cursor-prompt.md`
