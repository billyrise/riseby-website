# デプロイ時の公開範囲（Cloudflare Pages）

## 概要

GitHub にはリポジトリ全体（`docs/`、`scripts/`、各種 `.py` など）をプッシュできますが、**Cloudflare Pages で公開されるのは「サイト用コンテンツ」だけ**です。

- **公開されるもの**: 次のみが https://aimoaas.com に配信されます。
  - ルート: `index.html`, `about.html`, `privacy.html`, `404.html`, `robots.txt`, `sitemap.xml`, `_headers`, `_redirects`
  - ディレクトリ: `assets/`, `blog/`, `en/`, `services/`
- **公開されないもの**: 上記以外はすべて非公開です。
  - `docs/`（設計書・ブリーフ・メモなど）
  - `scripts/`（Python スクリプト）
  - ルートの `.py` や `.md`
  - `.github/` など

## 仕組み

`.github/workflows/deploy.yml` で以下を行っています。

1. リポジトリをチェックアウト
2. **Prepare site directory** ステップで、上記「公開するファイル・ディレクトリ」だけを `_site/` にコピー
3. Cloudflare Pages には `directory: _site` を指定してデプロイ

そのため、GitHub 上に置いた `docs/` や `scripts/` はリポジトリには残りますが、サイトには含まれず、URL でアクセスできません。

## 公開対象を増やす場合

新しい HTML やディレクトリを「サイトに載せたい」場合は、ワークフローの **Prepare site directory** の `cp` / `cp -r` に追加してください。逆に、公開したくないものを誤って含めないよう、公開リストはこのワークフローで明示的に管理しています。
