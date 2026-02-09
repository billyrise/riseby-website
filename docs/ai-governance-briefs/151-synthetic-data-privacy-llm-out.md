## リード（1段落）

現場では、AI利用の責任分界が曖昧なまま運用され、監査で指摘されるケースがあります。

本稿の焦点は「“合成データの限界”」です。合成データの限界について、責任分界・証跡・監査提出の目次を具体化します。品質指標と閾値を決め、ドリフトや是正件数を継続的に追います。 争点化された際に必要な証拠を想定し、日付・責任者・版の整合を保ちます。

## 本文

### 1. 使い所

本稿の焦点は「“合成データの限界”」です。使い所では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。品質指標と閾値を決め、ドリフトや是正件数を継続的に追います。 争点化された際に必要な証拠を想定し、日付・責任者・版の整合を保ちます。

さらに、境界定義を入力・出力・学習に分け、契約境界と運用で守る設計にします。 取締役会で聞かれる問いを想定し、KPI・意思決定ログ・四半期レビューを用意します。

加えて、所見の型と原因をテンプレ化し、是正の優先度と追跡KPIを決めます。 ログ種別と目的・保持期間の対応表を作り、完全性・改ざん検知を確保します。

ここに図1を挿入

### 2. 限界

リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。 争点シナリオに必要な証拠を洗い出し、保全と提出の責任者を決めます。

あわせて、論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。 当局報告の責任分界を事前に決め、インシデント設計に反映させます。

また、定性・定量の使い分けとリスク評価の手順を文書化し、継続評価を回します。 バイアス評価の手法選択と実施・記録・継続評価をセットにします。

ここに図2を挿入

### 3. 運用

取締役会向けの最小KRIとダッシュボードを用意し、閾値とアクションを決めます。 議題テンプレを毎四半期で回し、証跡と次のアクションを残します。

あわせて、継続評価の記録を四半期ごとに残し、是正の流れをテンプレ化しておきます。 データの境界（入力・出力・学習）を定義し、漏えい経路に統制を置きます。

また、ベンダー・委託先との責任分界を契約と証跡で明示し、四半期で棚卸します。 Evidence Bundleの形（ログ→検証→保全→提出）を揃え、ハッシュで改ざんを検知します。

ここに図3を挿入

### 4. 証跡

学習データの権利処理と出力物の責任範囲を方針に落とし、手続き化します。 アクセス制御を申請・承認・付与のフローに落とし、最小権限を適用します。

あわせて、法域ごとの義務をマトリクス化し、契約条項と証跡でカバーします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを回します。

また、開発段階の統制と承認ゲートを設け、証跡を切らさない設計にします。 連鎖（生成→保管→提出→検証）を設計し、監査提示の形を事前に合意します。

## 図1（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">使い所と運用</p>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li style="margin: 0.25rem 0;">RACIと証跡の目次を監査と事前合意</li>
    <li style="margin: 0.25rem 0;">継続評価・インシデント窓口を固定</li>
    <li style="margin: 0.25rem 0;">是正の流れをテンプレ化し記録</li>
  </ul>
</div>
```

## 図2（Table）

```
<table style="width:100%; max-width: 520px; margin: 1rem auto; border-collapse: collapse;">
  <thead>
    <tr style="background: #f1f5f9;">
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">証跡</th>
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">目的</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">限界・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図3（SVG）

```
<svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="95" height="45" rx="4" fill="#e0f2fe"/><text x="57" y="34" text-anchor="middle" font-size="8">軸A</text>
  <rect x="115" y="10" width="95" height="45" rx="4" fill="#dcfce7"/><text x="162" y="34" text-anchor="middle" font-size="8">軸B</text>
  <rect x="10" y="65" width="95" height="45" rx="4" fill="#fef9c3"/><text x="57" y="89" text-anchor="middle" font-size="8">統制</text>
  <rect x="115" y="65" width="95" height="45" rx="4" fill="#f1f5f9"/><text x="162" y="89" text-anchor="middle" font-size="8">証跡</text>
  <text x="110" y="115" text-anchor="middle" font-size="8" fill="#64748b">運用</text>
</svg>
```

## 図の型（記録用・必須）
図1: A, 図2: E, 図3: G

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“合成データの限界”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、申請フローと例外の基準を1つ決め、承認記録を必ず残すルールにすると、他領域の設計の基準になります。

## チェックリスト（10項目）

- 監査提出の目次を監査法人と事前にすり合わせているか
- レッドチーム・演習の計画・結果・是正を記録しているか
- アクセス制御を申請・承認・付与のフローに落としているか
- 成果物ごとに作成者・承認者・保管場所を決めているか
- 透明性表示・公開前チェックの記録を残しているか
- 例外の基準と有効期限を決め、四半期で棚卸しているか
- 脅威分類と統制・監視・演習の記録を揃えているか
- ログ種別・目的・保持期間を一覧化し、完全性を検証しているか
- インシデント時の報告・エスカレーション手順を決めているか
- DPIA・利用目的承認と証跡の連携を取っているか

## 参考文献（3つ以上、発行年または一次資料明記）

- GDPR（EU一般データ保護規則）. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework


## 次の一歩（結論パターン Co に沿って）

明日から始められる3つのステップです。 証跡の目次を1枚にまとめ、保管責任者を1人決め、四半期の棚卸日をカレンダーに登録する。 申請―審査―承認のフローを文書化し、例外の基準と有効期限を明文化する。
