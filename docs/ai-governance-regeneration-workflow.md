# AIガバナンス記事 全163件の1から生成し直し（同一ルール）

## ルール監査結果（実施済み）

- **1〜163まで同一ルール**: 記事番号による例外は設けない旨、`docs/ai-governance-blog-cursor-prompt.md` に明記済み。**矛盾する別ルールは見つかっていません。**
- **修正した不一致**: `docs/ai-governance-briefs/CHECK-INFIGRAPHIC-RULES.md` に「全133記事」という古い記述があったため、**163記事**に合わせて修正済み。

## 厳守ルール（全記事共通）

- **作成方針**: 外部LLM（API・他サービス）は使わない。Cursor 内で1から作成。Cursor が自動的に使う LLM は制限しない。1〜163まで同一ルール。
- **文体**: です・ます調。断定を避け条件・前提を明示。
- **章をまたぐ同一長文の禁止**: 「理念で終わらせず…5要素のうち」はリードまたは第1セクションに**1回のみ**。第2セクション以降は言い換えのみ。
- **本稿の焦点は〜**: 複数セクションで同じ文言のまま繰り返さない。リードまたは1セクション目で1回のみ。
- **各セクション**: 2〜4段落で具体論。1文だけのセクションにしない。
- **固有の一文**: 冒頭2段落以内に、具体性・意外性・非代替性を満たす1文を1つ以上。
- **チェックリスト**: その記事の **unique_focus** に特化した8〜10項目。全記事で同じ汎用10項目にしない。
- **次の一歩**: 記事ごとに固有の内容。汎用フレーズの繰り返し禁止。設計図3.3の結論パターン（Co）に沿う。
- **図**: 指定フォーマット（SVG/HTML/Table/**Mermaid**等）。**同一形式を連続して使わない**。直近5記事で使った形式は各形式1回まで。同じ図の型を3記事連続で使わない。`figure_usage_history.csv` と直前10記事の llm-out の「図の型」「図の形式」を参照。
- **参照**: 設計図 `docs/ai-governance-blog-design.md` セクション3.3の該当No.行（DNA・Op・Co・title_ja・unique_focus）を必ず参照。記憶で補完しない。

## 生成済み（この回）

| No. | slug | 状態 |
|-----|------|------|
| 1 | accountability-incident-design | 生成済み・HTML反映済み |
| 2 | ai-access-control-zerotrust | 生成済み・HTML反映済み |
| 3 | ai-assurance-vs-audit | 生成済み・HTML反映済み |
| 4 | ai-bom-implementation | 生成済み・HTML反映済み |
| 5〜163 | （各 slug） | 未生成。下記手順で Cursor 内で同様に生成する |

## 残り 5〜163 の生成手順（Cursor 内で繰り返し）

1. **プロンプトを開く**: `docs/ai-governance-briefs/full_article_prompts/NNN-slug-prompt.md`（NNNは3桁ゼロ埋め）
2. **設計図を参照**: `docs/ai-governance-blog-design.md` の **3.3 記事DNA** の表で No.N の行を確認（読者・目的・深さ・スタイル・Op・Co・title_ja）。
3. **図表履歴を参照**: 直近10記事の `docs/ai-governance-briefs/*-llm-out.md` の「図の型」「図の形式」、または `figure_usage_history.csv`。同じ型を3記事連続にしない・直近5記事の形式を各1回までにする。
4. **記事全文を生成**: 上記ルールに従い、リード・本文（必須セクション見出しはプロンプト通り）・図1〜3（SVG/HTML/Table等）・図の型/形式・固有の一文・チェックリスト（記事特化）・参考文献・次の一歩 を書く。
5. **保存**: `docs/ai-governance-briefs/NNN-slug-llm-out.md` に上記形式で保存。
6. **HTML反映**: `python3 scripts/apply_llm_article.py NNN docs/ai-governance-briefs/NNN-slug-llm-out.md`（全件終了後は一括ループ可）。

## 一括HTML反映（全163件）

```bash
for no in $(seq 1 163); do
  f=$(ls docs/ai-governance-briefs/$(printf "%03d" $no)-*-llm-out.md 2>/dev/null | head -1)
  [ -n "$f" ] && python3 scripts/apply_llm_article.py $no "$f"
done
```

## 参照ドキュメント

- 執筆ルール・多様性ルール: `docs/ai-governance-blog-cursor-prompt.md`
- 設計図・テンプレ・記事DNA: `docs/ai-governance-blog-design.md`
- インフォグラフィック形式: `docs/ai-governance-blog-infographic-formats.md`
