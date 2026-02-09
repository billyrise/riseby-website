## リード（1段落）

理念を掲げるほど、手続きと証跡が追いつかず、監査で説明できない事態になりがちです。

本稿の焦点は「“例外管理の設計”」です。例外管理の設計について、責任分界・証跡・監査提出の目次を具体化します。論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。 当局報告の責任分界を事前に決め、インシデント設計に反映させます。

## 本文

### 1. 例外が増える理由

本稿の焦点は「“例外管理の設計”」です。例外が増える理由では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。 当局報告の責任分界を事前に決め、インシデント設計に反映させます。

さらに、定性・定量の使い分けとリスク評価の手順を文書化し、継続評価を回します。 バイアス評価の手法選択と実施・記録・継続評価をセットにします。

加えて、申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。 誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。

ここに図1を挿入

### 2. 抑制

継続評価の記録を四半期ごとに残し、是正の流れをテンプレ化しておきます。 データの境界（入力・出力・学習）を定義し、漏えい経路に統制を置きます。

あわせて、ベンダー・委託先との責任分界を契約と証跡で明示し、四半期で棚卸します。 Evidence Bundleの形（ログ→検証→保全→提出）を揃え、ハッシュで改ざんを検知します。

また、データ種類と義務の対応をマトリクス化し、DPIA・承認の記録を保全します。 三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。

ここに図2を挿入

### 3. 教育

法域ごとの義務をマトリクス化し、契約条項と証跡でカバーします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを回します。

あわせて、開発段階の統制と承認ゲートを設け、証跡を切らさない設計にします。 連鎖（生成→保管→提出→検証）を設計し、監査提示の形を事前に合意します。

また、選定基準と評価プロセス、契約・SLA、継続監視、証跡を一貫して設計します。 コンテンツ種別と義務、表示、チェック、公開、記録のフローを決めます。

ここに図3を挿入

### 4. KRI

品質KRIと閾値、是正率を記録し、データとリスクの対応を監視します。 ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。

あわせて、年次で優先5領域を決め、予算・人材・レビューのサイクルを設計します。 ボード指標の最小セットと意思決定ログ、四半期レビューを運用します。

また、証跡は改ざん耐性（ハッシュやアクセス制御）を確保し、保持期間を明示します。 開発フェーズとリリース承認のゲートを設け、通過記録を証跡として残します。

## 図1（Table）

```
<table style="width:100%; max-width: 520px; margin: 1rem auto; border-collapse: collapse;">
  <thead>
    <tr style="background: #f1f5f9;">
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">証跡</th>
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">目的</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">例外が増える理由・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図2（SVG）

```
<svg viewBox="0 0 380 80" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="22" width="95" height="36" rx="4" fill="#e0f2fe"/><text x="62" y="44" text-anchor="middle" font-size="9">入力</text>
  <path d="M115 40 L145 40" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>
  <rect x="150" y="22" width="95" height="36" rx="4" fill="#dcfce7"/><text x="197" y="44" text-anchor="middle" font-size="9">審査</text>
  <path d="M250 40 L280 40" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <defs><marker id="arrow2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>
  <rect x="285" y="22" width="95" height="36" rx="4" fill="#fef9c3"/><text x="332" y="44" text-anchor="middle" font-size="9">出力</text>
  <text x="190" y="72" text-anchor="middle" font-size="8" fill="#64748b">抑制</text>
</svg>
```

## 図3（Mermaid）

```
graph TD
  行動 --> 統制
  統制 --> インセンティブ
  style 統制 fill:#dcfce7
```

## 図の型（記録用・必須）
図1: G, 図2: A, 図3: D

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“例外管理の設計”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、継続評価の頻度と是正の流れをテンプレ化し、四半期の棚卸日をカレンダーに登録することを推奨します。

## チェックリスト（10項目）

- Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか
- 監査提出の目次を監査法人と事前にすり合わせているか
- レッドチーム・演習の計画・結果・是正を記録しているか
- アクセス制御を申請・承認・付与のフローに落としているか
- 成果物ごとに作成者・承認者・保管場所を決めているか
- 透明性表示・公開前チェックの記録を残しているか
- 例外の基準と有効期限を決め、四半期で棚卸しているか
- 脅威分類と統制・監視・演習の記録を揃えているか
- ログ種別・目的・保持期間を一覧化し、完全性を検証しているか
- インシデント時の報告・エスカレーション手順を決めているか

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- G7広島AIプロセス. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20231030_3.pdf


## 次の一歩（結論パターン Co に沿って）

いまの対応が、その後の監査対応と競争力の基盤になります。 KRI・閾値・エスカレーション先を1つ決め、ダッシュボードかレビューで追う運用にする。 契約にBOM・ログ提供の義務が入っているか確認し、入っていなければ次回更新で条項追加を検討する。
