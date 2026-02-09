## リード（1段落）

理想は統制の効いたAI利用、現実は申請フローが形骸化し証跡が残らない、というギャップがよく聞かれます。

本稿の焦点は「“RMF実装（プロファイル）”」です。NIST RMF実装（プロファイル）について、責任分界・証跡・監査提出の目次を具体化します。DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。 廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。

## 本文

### 1. 評価設計

本稿の焦点は「“RMF実装（プロファイル）”」です。評価設計では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。 廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。

さらに、漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。 PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。

加えて、文書のコード化と版管理で形骸化を防ぎ、抵抗への対処も手順化します。 リリース承認のチェックリストと失敗例を文書化し、テンプレとして使います。

ここに図1を挿入

### 2. 実施と記録

ProofとAssuranceの分界を決め、監査が求める証憑の形と揃えます。 退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。

あわせて、入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。 典型契約論点を条項と証跡でカバーし、雛形で効率化します。

また、出力物の権利・責任を方針に落とし、手続きと証跡を揃えます。 取締役会向けの最小KRIとダッシュボードを用意し、閾値とアクションを決めます。

ここに図2を挿入

### 3. 継続評価

レッドラインを定義し、許容度設計と承認運用、例外・KRIを決めます。 BCPとAI依存の停止・代替・復旧手順を決め、証跡を残します。

あわせて、責任の所在（RACI）を一枚にまとめ、関係者と共有しておくことが第一歩です。 規制・標準との対応関係は一覧化しつつ、断定は避け条件を明示します。

また、契約・SLAにBOMやログ提供の義務を盛り込み、責任分界を明確にします。 学習データの権利処理と出力物の責任範囲を方針に落とし、手続き化します。

ここに図3を挿入

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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">評価設計・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図2（SVG）

```
<svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="95" height="45" rx="4" fill="#e0f2fe"/><text x="57" y="34" text-anchor="middle" font-size="8">軸A</text>
  <rect x="115" y="10" width="95" height="45" rx="4" fill="#dcfce7"/><text x="162" y="34" text-anchor="middle" font-size="8">軸B</text>
  <rect x="10" y="65" width="95" height="45" rx="4" fill="#fef9c3"/><text x="57" y="89" text-anchor="middle" font-size="8">統制</text>
  <rect x="115" y="65" width="95" height="45" rx="4" fill="#f1f5f9"/><text x="162" y="89" text-anchor="middle" font-size="8">証跡</text>
  <text x="110" y="115" text-anchor="middle" font-size="8" fill="#64748b">実施と記録</text>
</svg>
```

## 図3（Mermaid）

```
graph TD
  K1[評価完了率]
  K2[是正件数]
  K3[ドリフト検知]
  style K1 fill:#fef9c3
```

## 図の型（記録用・必須）
図1: J, 図2: A, 図3: F

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“RMF実装（プロファイル）”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、RACIと証跡の目次を関係者と共有し、インシデント時の報告先を1つ決めておくだけで、説明可能性が高まります。

## チェックリスト（10項目）

- ボード・監査向けの最小KRIと閾値 breach 時のアクションを決めているか
- 教育・周知の記録を残しているか
- 品質指標・閾値・是正を継続的に追っているか
- 申請―審査―承認のフローを文書化し、証跡を残しているか
- データ境界と漏えい経路に統制を置いているか
- 廃止・退役の手順と記録を決めているか
- 継続評価の記録を残し、是正の流れをテンプレ化しているか
- 契約にBOM・ログ提供義務を盛り込み、責任分界を明示しているか
- Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか
- 監査提出の目次を監査法人と事前にすり合わせているか

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf


## 次の一歩（結論パターン Co に沿って）

放置した場合のワーストシナリオ（監査指摘・証跡欠落）を避けるため、明日から対策を始めてください。 監査提出の目次を監査法人と1回すり合わせ、欠落しやすい項目をチェックリストに加える。 開発・リリースのゲートと通過記録の形を決め、証跡の連鎖が切れないようにする。
