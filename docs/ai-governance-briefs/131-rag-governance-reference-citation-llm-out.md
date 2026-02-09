## リード（1段落）

現場では、AI利用の責任分界が曖昧なまま運用され、監査で指摘されるケースがあります。

本稿の焦点は「“参照/引用の監査性”」です。参照・引用の監査性について、責任分界・証跡・監査提出の目次を具体化します。文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。 リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。

## 本文

### 1. 監査で必要なログ

本稿の焦点は「“参照/引用の監査性”」です。監査で必要なログでは、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。 リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。

さらに、争点シナリオに必要な証拠を洗い出し、保全と提出の責任者を決めます。 論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。

加えて、当局報告の責任分界を事前に決め、インシデント設計に反映させます。 定性・定量の使い分けとリスク評価の手順を文書化し、継続評価を回します。

ここに図1を挿入

### 2. 設計

出力物の権利・責任を方針に落とし、手続きと証跡を揃えます。 取締役会向けの最小KRIとダッシュボードを用意し、閾値とアクションを決めます。

あわせて、議題テンプレを毎四半期で回し、証跡と次のアクションを残します。 継続評価の記録を四半期ごとに残し、是正の流れをテンプレ化しておきます。

また、データの境界（入力・出力・学習）を定義し、漏えい経路に統制を置きます。 ベンダー・委託先との責任分界を契約と証跡で明示し、四半期で棚卸します。

ここに図2を挿入

### 3. 保全

契約・SLAにBOMやログ提供の義務を盛り込み、責任分界を明確にします。 学習データの権利処理と出力物の責任範囲を方針に落とし、手続き化します。

あわせて、アクセス制御を申請・承認・付与のフローに落とし、最小権限を適用します。 法域ごとの義務をマトリクス化し、契約条項と証跡でカバーします。

また、年次で優先5領域を決め、予算・人材・レビューのサイクルを回します。 開発段階の統制と承認ゲートを設け、証跡を切らさない設計にします。

ここに図3を挿入

### 4. 検証

定性・定量の評価設計を実施し、記録と継続評価をセットにします。 何をいつ測るか、閾値、証跡、運用責任者を決め、ゲートで通過記録を残します。

あわせて、主体・権限・データのマトリクスでアクセスを設計し、付与・剥奪の記録を残します。 品質KRIと閾値、是正率を記録し、データとリスクの対応を監視します。

また、ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを設計します。

## 図1（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">監査で必要なログと運用</p>
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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">設計・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図3（SVG）

```
<svg viewBox="0 0 420 70" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="18" width="88" height="32" rx="4" fill="#e0f2fe"/><text x="52" y="38" text-anchor="middle" font-size="8">ログ</text>
  <rect x="108" y="18" width="88" height="32" rx="4" fill="#dcfce7"/><text x="152" y="38" text-anchor="middle" font-size="8">検証</text>
  <rect x="208" y="18" width="88" height="32" rx="4" fill="#fef9c3"/><text x="252" y="38" text-anchor="middle" font-size="8">保全</text>
  <rect x="308" y="18" width="88" height="32" rx="4" fill="#f1f5f9"/><text x="352" y="38" text-anchor="middle" font-size="8">提出</text>
  <text x="210" y="62" text-anchor="middle" font-size="8" fill="#64748b">保全</text>
</svg>
```

## 図の型（記録用・必須）
図1: A, 図2: E, 図3: G

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“参照/引用の監査性”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、申請フローと例外の基準を1つ決め、承認記録を必ず残すルールにすると、他領域の設計の基準になります。

## チェックリスト（10項目）

- 版管理と変更記録を残し、文書の形骸化を防いでいるか
- ボード・監査向けの最小KRIと閾値 breach 時のアクションを決めているか
- 教育・周知の記録を残しているか
- 品質指標・閾値・是正を継続的に追っているか
- 申請―審査―承認のフローを文書化し、証跡を残しているか
- データ境界と漏えい経路に統制を置いているか
- 廃止・退役の手順と記録を決めているか
- 継続評価の記録を残し、是正の流れをテンプレ化しているか
- 契約にBOM・ログ提供義務を盛り込み、責任分界を明示しているか
- Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf


## 次の一歩（結論パターン Co に沿って）

明日から始められる3つのステップです。 版管理と変更記録のルールを決め、文書の形骸化を防ぐための教育を1回行う。 争点化を想定した証拠のリストを作り、日付・責任者・版の整合を保つ手順を決める。
