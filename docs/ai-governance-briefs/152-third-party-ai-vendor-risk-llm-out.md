## リード（1段落）

多くの組織で、AIガバナンスの証跡が「何を残すか」で揃っておらず、事後の説明に苦慮しています。

本稿の焦点は「“第三者リスク”」です。第三者・ベンダーリスクについて、責任分界・証跡・監査提出の目次を具体化します。PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。 文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。

## 本文

### 1. 選定基準

本稿の焦点は「“第三者リスク”」です。選定基準では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。 文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。

さらに、リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。 争点シナリオに必要な証拠を洗い出し、保全と提出の責任者を決めます。

加えて、論点を「何が論点か」で整理し、運用・証跡・チェックリストに落とします。 当局報告の責任分界を事前に決め、インシデント設計に反映させます。

ここに図1を挿入

### 2. 評価プロセス

典型契約論点を条項と証跡でカバーし、雛形で効率化します。 出力物の権利・責任を方針に落とし、手続きと証跡を揃えます。

あわせて、取締役会向けの最小KRIとダッシュボードを用意し、閾値とアクションを決めます。 議題テンプレを毎四半期で回し、証跡と次のアクションを残します。

また、継続評価の記録を四半期ごとに残し、是正の流れをテンプレ化しておきます。 データの境界（入力・出力・学習）を定義し、漏えい経路に統制を置きます。

ここに図2を挿入

### 3. 契約・SLA

規制・標準との対応関係は一覧化しつつ、断定は避け条件を明示します。 契約・SLAにBOMやログ提供の義務を盛り込み、責任分界を明確にします。

あわせて、学習データの権利処理と出力物の責任範囲を方針に落とし、手続き化します。 アクセス制御を申請・承認・付与のフローに落とし、最小権限を適用します。

また、法域ごとの義務をマトリクス化し、契約条項と証跡でカバーします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを回します。

ここに図3を挿入

### 4. 継続監視

表示義務と公開前チェックを運用に落とし、証跡の目次に含めます。 定性・定量の評価設計を実施し、記録と継続評価をセットにします。

あわせて、何をいつ測るか、閾値、証跡、運用責任者を決め、ゲートで通過記録を残します。 主体・権限・データのマトリクスでアクセスを設計し、付与・剥奪の記録を残します。

また、品質KRIと閾値、是正率を記録し、データとリスクの対応を監視します。 ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。

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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選定基準・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
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
  <text x="190" y="72" text-anchor="middle" font-size="8" fill="#64748b">評価プロセス</text>
</svg>
```

## 図3（Mermaid）

```
graph LR
  L[ログ] --> V[検証]
  V --> S[保全]
  S --> P[提出]
  style S fill:#dcfce7
```

## 図の型（記録用・必須）
図1: D, 図2: B, 図3: I

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“第三者リスク”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、監査提出に必要な証跡の目次をリスト化し、監査法人に事前に1回提示して問題ないか確認してください。

## チェックリスト（10項目）

- KRI・閾値・エスカレーション先を決めているか
- 証跡の最小目次を固定し、欠落をチェックしているか
- 規制・標準との対応関係を一覧化しているか（断定は避ける）
- 版管理と変更記録を残し、文書の形骸化を防いでいるか
- ボード・監査向けの最小KRIと閾値 breach 時のアクションを決めているか
- 教育・周知の記録を残しているか
- 品質指標・閾値・是正を継続的に追っているか
- 申請―審査―承認のフローを文書化し、証跡を残しているか
- データ境界と漏えい経路に統制を置いているか
- 廃止・退役の手順と記録を決めているか

## 参考文献（3つ以上、発行年または一次資料明記）

- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework


## 次の一歩（結論パターン Co に沿って）

あなたの組織がどの道を選ぶべきか、判断軸を1つ決めてください。 申請―審査―承認のフローを文書化し、例外の基準と有効期限を明文化する。 RACIを一枚にまとめ関係者と共有し、継続評価とインシデント窓口を固定する。
