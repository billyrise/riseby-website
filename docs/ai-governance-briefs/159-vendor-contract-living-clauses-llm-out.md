## リード（1段落）

集中型で統制するか、分散型でスピードを取るか、組織に合わせた選択が求められます。

本稿の焦点は「“living clauses運用”」です。living clausesの運用について、責任分界・証跡・監査提出の目次を具体化します。論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。 当局報告の責任分界を事前に決め、インシデント設計に反映させます。

## 本文

### 1. 選定基準

本稿の焦点は「“living clauses運用”」です。選定基準では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。 当局報告の責任分界を事前に決め、インシデント設計に反映させます。

さらに、定性・定量の使い分けとリスク評価の手順を文書化し、継続評価を回します。 バイアス評価の手法選択と実施・記録・継続評価をセットにします。

加えて、申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。 誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。

ここに図1を挿入

### 2. 評価プロセス

継続評価の記録を四半期ごとに残し、是正の流れをテンプレ化しておきます。 データの境界（入力・出力・学習）を定義し、漏えい経路に統制を置きます。

あわせて、ベンダー・委託先との責任分界を契約と証跡で明示し、四半期で棚卸します。 Evidence Bundleの形（ログ→検証→保全→提出）を揃え、ハッシュで改ざんを検知します。

また、データ種類と義務の対応をマトリクス化し、DPIA・承認の記録を保全します。 三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。

ここに図2を挿入

### 3. 契約・SLA

法域ごとの義務をマトリクス化し、契約条項と証跡でカバーします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを回します。

あわせて、開発段階の統制と承認ゲートを設け、証跡を切らさない設計にします。 連鎖（生成→保管→提出→検証）を設計し、監査提示の形を事前に合意します。

また、選定基準と評価プロセス、契約・SLA、継続監視、証跡を一貫して設計します。 コンテンツ種別と義務、表示、チェック、公開、記録のフローを決めます。

ここに図3を挿入

### 4. 継続監視

品質KRIと閾値、是正率を記録し、データとリスクの対応を監視します。 ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。

あわせて、年次で優先5領域を決め、予算・人材・レビューのサイクルを設計します。 ボード指標の最小セットと意思決定ログ、四半期レビューを運用します。

また、証跡は改ざん耐性（ハッシュやアクセス制御）を確保し、保持期間を明示します。 開発フェーズとリリース承認のゲートを設け、通過記録を証跡として残します。

## 図1（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">選定基準と運用</p>
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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">評価プロセス・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図3（SVG）

```
<svg viewBox="0 0 380 80" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="22" width="95" height="36" rx="4" fill="#e0f2fe"/><text x="62" y="44" text-anchor="middle" font-size="9">入力</text>
  <path d="M115 40 L145 40" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>
  <rect x="150" y="22" width="95" height="36" rx="4" fill="#dcfce7"/><text x="197" y="44" text-anchor="middle" font-size="9">審査</text>
  <path d="M250 40 L280 40" stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <defs><marker id="arrow2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>
  <rect x="285" y="22" width="95" height="36" rx="4" fill="#fef9c3"/><text x="332" y="44" text-anchor="middle" font-size="9">出力</text>
  <text x="190" y="72" text-anchor="middle" font-size="8" fill="#64748b">契約・SLA</text>
</svg>
```

## 図の型（記録用・必須）
図1: I, 図2: D, 図3: B

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“living clauses運用”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、RACIと証跡の目次を関係者と共有し、インシデント時の報告先を1つ決めておくだけで、説明可能性が高まります。

## チェックリスト（10項目）

- 証跡を改ざん耐性で保全し、保持期間を明示しているか
- KRI・閾値・エスカレーション先を決めているか
- 証跡の最小目次を固定し、欠落をチェックしているか
- 規制・標準との対応関係を一覧化しているか（断定は避ける）
- 版管理と変更記録を残し、文書の形骸化を防いでいるか
- ボード・監査向けの最小KRIと閾値 breach 時のアクションを決めているか
- 教育・周知の記録を残しているか
- 品質指標・閾値・是正を継続的に追っているか
- 申請―審査―承認のフローを文書化し、証跡を残しているか
- データ境界と漏えい経路に統制を置いているか

## 参考文献（3つ以上、発行年または一次資料明記）

- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework


## 次の一歩（結論パターン Co に沿って）

放置した場合のワーストシナリオ（監査指摘・証跡欠落）を避けるため、明日から対策を始めてください。 契約にBOM・ログ提供の義務が入っているか確認し、入っていなければ次回更新で条項追加を検討する。 DPIA・利用目的承認とAI利用申請の連携を1回確認し、証跡の紐づけを設計する。
