## リード（1段落）

ある企業では、AI倫理委員会を設けたが承認と開発のゲートがつながらず、形骸化した事例があります。

本稿の焦点は「“採用AIの公平性”」です。採用AIの公平性について、責任分界・証跡・監査提出の目次を具体化します。手法の使い所と限界を注記し、匿名化率・再識別リスクを記録します。 Buy/Buildの評価軸を決め、選定・契約・監視・証跡を一貫させます。

## 本文

### 1. 評価設計

本稿の焦点は「“採用AIの公平性”」です。評価設計では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。手法の使い所と限界を注記し、匿名化率・再識別リスクを記録します。 Buy/Buildの評価軸を決め、選定・契約・監視・証跡を一貫させます。

さらに、ログ完全性・保持・改ざん検知を設計し、監査で説明できる形にします。 グローバル運用の抜け穴をガードレールで塞ぎ、移行計画と証跡を決めます。

加えて、インシデント時の報告先とエスカレーション閾値を決め、記録を欠かさないようにします。 脅威を分類し、優先順位をつけたうえで統制と監視を設計します。

ここに図1を挿入

### 2. 実施と記録

誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。 DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。

あわせて、廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。 漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。

また、PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。 文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。

ここに図2を挿入

### 3. 継続評価

三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。 ProofとAssuranceの分界を決め、監査が求める証憑の形と揃えます。

あわせて、退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。 入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。

また、典型契約論点を条項と証跡でカバーし、雛形で効率化します。 出力物の権利・責任を方針に落とし、手続きと証跡を揃えます。

ここに図3を挿入

## 図1（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">評価設計と運用</p>
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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">実施と記録・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
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
  <text x="110" y="115" text-anchor="middle" font-size="8" fill="#64748b">継続評価</text>
</svg>
```

## 図の型（記録用・必須）
図1: E, 図2: D, 図3: F

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“採用AIの公平性”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、自部門で責任者と証跡の保管者を1人ずつ決め、証跡の目次を1枚にまとめて監査と1回確認することをお勧めします。

## チェックリスト（10項目）

- インシデント時の報告・エスカレーション手順を決めているか
- DPIA・利用目的承認と証跡の連携を取っているか
- 争点化に備えた証拠を想定し、日付・責任者の整合を保っているか
- 四半期の棚卸を予定し、記録を残しているか
- ベンダー・委託先との責任分界を契約と証跡で明示しているか
- RACI（責任者・承認者）を決め、一枚にまとめているか
- 開発・リリースのゲートと通過記録を設計しているか
- 学習データ・出力物の権利と責任を方針化しているか
- 証跡を改ざん耐性で保全し、保持期間を明示しているか
- KRI・閾値・エスカレーション先を決めているか

## 参考文献（3つ以上、発行年または一次資料明記）

- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001


## 次の一歩（結論パターン Co に沿って）

今日のベストプラクティスは明日の最低要件になり得ます。明日から、 開発・リリースのゲートと通過記録の形を決め、証跡の連鎖が切れないようにする。 データ境界と統制の対応表を作り、担当とAI統制の責任分界を1回決める。
