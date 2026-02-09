## リード（1段落）

あなたの部門では、AI利用の申請から承認まで、誰が何を判断するか即答できますか。

本稿の焦点は「“ヒートマップ”」です。リスクヒートマップについて、責任分界・証跡・監査提出の目次を具体化します。廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。 漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。

## 本文

### 1. 許容度設計

本稿の焦点は「“ヒートマップ”」です。許容度設計では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。 漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。

さらに、PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。 文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。

加えて、リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。 争点シナリオに必要な証拠を洗い出し、保全と提出の責任者を決めます。

ここに図1を挿入

### 2. 承認運用

退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。 入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。

あわせて、典型契約論点を条項と証跡でカバーし、雛形で効率化します。 出力物の権利・責任を方針に落とし、手続きと証跡を揃えます。

また、取締役会向けの最小KRIとダッシュボードを用意し、閾値とアクションを決めます。 議題テンプレを毎四半期で回し、証跡と次のアクションを残します。

ここに図2を挿入

### 3. 例外

BCPとAI依存の停止・代替・復旧手順を決め、証跡を残します。 責任の所在（RACI）を一枚にまとめ、関係者と共有しておくことが第一歩です。

あわせて、規制・標準との対応関係は一覧化しつつ、断定は避け条件を明示します。 契約・SLAにBOMやログ提供の義務を盛り込み、責任分界を明確にします。

また、学習データの権利処理と出力物の責任範囲を方針に落とし、手続き化します。 アクセス制御を申請・承認・付与のフローに落とし、最小権限を適用します。

ここに図3を挿入

### 4. KRI

証跡の最小セットを「目次」として固定し、欠落しやすい項目をチェックします。 選定基準と評価プロセスを文書化し、契約・継続監視・証跡を一貫させます。

あわせて、表示義務と公開前チェックを運用に落とし、証跡の目次に含めます。 定性・定量の評価設計を実施し、記録と継続評価をセットにします。

また、何をいつ測るか、閾値、証跡、運用責任者を決め、ゲートで通過記録を残します。 主体・権限・データのマトリクスでアクセスを設計し、付与・剥奪の記録を残します。

## 図1（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">許容度設計と運用</p>
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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認運用・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
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
  <text x="110" y="115" text-anchor="middle" font-size="8" fill="#64748b">例外</text>
</svg>
```

## 図の型（記録用・必須）
図1: C, 図2: H, 図3: I

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“ヒートマップ”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、継続評価の頻度と是正の流れをテンプレ化し、四半期の棚卸日をカレンダーに登録することを推奨します。

## チェックリスト（10項目）

- 申請―審査―承認のフローを文書化し、証跡を残しているか
- データ境界と漏えい経路に統制を置いているか
- 廃止・退役の手順と記録を決めているか
- 継続評価の記録を残し、是正の流れをテンプレ化しているか
- 契約にBOM・ログ提供義務を盛り込み、責任分界を明示しているか
- Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか
- 監査提出の目次を監査法人と事前にすり合わせているか
- レッドチーム・演習の計画・結果・是正を記録しているか
- アクセス制御を申請・承認・付与のフローに落としているか
- 成果物ごとに作成者・承認者・保管場所を決めているか

## 参考文献（3つ以上、発行年または一次資料明記）

- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001


## 次の一歩（結論パターン Co に沿って）

いまの対応が、その後の監査対応と競争力の基盤になります。 透明性表示と公開前チェックの手順を文書化し、記録を必ず残すルールにする。 廃止・退役の手順と記録の形を決め、保持と再現性を確保する。
