## リード（1段落）

理想は統制の効いたAI利用、現実は申請フローが形骸化し証跡が残らない、というギャップがよく聞かれます。

本稿の焦点は「“要点1枚化”」です。ガバナンス役割の要点1枚について、責任分界・証跡・監査提出の目次を具体化します。透明性表示やコンテンツ分類の手順を文書化し、公開前チェックの記録を残します。 ボード・監査向けの最小KRIを決め、閾値 breach 時のアクションを明文化します。

## 本文

### 1. 取締役会で聞かれる5問

本稿の焦点は「“要点1枚化”」です。取締役会で聞かれる5問では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。透明性表示やコンテンツ分類の手順を文書化し、公開前チェックの記録を残します。 ボード・監査向けの最小KRIを決め、閾値 breach 時のアクションを明文化します。

さらに、品質が壊れるポイントを特定し、測定・是正・証跡のループを回します。 集中と分散のトレードオフを整理し、抜け穴がないようガードレールを置きます。

加えて、年1の監査では不足するため、継続適合性評価と自動化を運用に組み込みます。 最小目次と落とし穴（目次欠落・日付不整合等）をテンプレで共有します。

ここに図1を挿入

### 2. 指標と運用

例外が増えないよう、抑制策と教育、KRIで棚卸しを回します。 何を見るか・誰が見るか・閾値・アクションを決め、エスカレーションを明文化します。

あわせて、境界定義と統制、契約、運用を一貫させ、証跡の目次に含めます。 エスカレーション閾値と重大基準を明文化し、記録と棚卸をセットにします。

また、契約条項のチェックリストを用意し、living clausesで見直し可能にします。 領域別の公平性論点を整理し、評価と証跡を業界の期待に合わせます。

ここに図2を挿入

### 3. 雛形

ログ完全性・保持・改ざん検知を設計し、監査で説明できる形にします。 グローバル運用の抜け穴をガードレールで塞ぎ、移行計画と証跡を決めます。

あわせて、インシデント時の報告先とエスカレーション閾値を決め、記録を欠かさないようにします。 脅威を分類し、優先順位をつけたうえで統制と監視を設計します。

また、品質指標と閾値を決め、ドリフトや是正件数を継続的に追います。 争点化された際に必要な証拠を想定し、日付・責任者・版の整合を保ちます。

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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">取締役会で聞かれる5・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図2（SVG）

```
<svg viewBox="0 0 320 70" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="18" width="88" height="34" rx="4" fill="#e0f2fe"/><text x="59" y="38" text-anchor="middle" font-size="8">KRI1</text>
  <rect x="116" y="18" width="88" height="34" rx="4" fill="#dcfce7"/><text x="160" y="38" text-anchor="middle" font-size="8">KRI2</text>
  <rect x="217" y="18" width="88" height="34" rx="4" fill="#fef9c3"/><text x="261" y="38" text-anchor="middle" font-size="8">KRI3</text>
  <text x="160" y="62" text-anchor="middle" font-size="8" fill="#64748b">指標と運用</text>
</svg>
```

## 図3（Mermaid）

```
graph LR
  Board[Board]
  Legal[Legal]
  CISO[CISO]
  Audit[Audit]
  style Board fill:#e0f2fe
```

## 図の型（記録用・必須）
図1: J, 図2: A, 図3: F

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“要点1枚化”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、RACIと証跡の目次を関係者と共有し、インシデント時の報告先を1つ決めておくだけで、説明可能性が高まります。

## チェックリスト（10項目）

- 四半期の棚卸を予定し、記録を残しているか
- ベンダー・委託先との責任分界を契約と証跡で明示しているか
- RACI（責任者・承認者）を決め、一枚にまとめているか
- 開発・リリースのゲートと通過記録を設計しているか
- 学習データ・出力物の権利と責任を方針化しているか
- 証跡を改ざん耐性で保全し、保持期間を明示しているか
- KRI・閾値・エスカレーション先を決めているか
- 証跡の最小目次を固定し、欠落をチェックしているか
- 規制・標準との対応関係を一覧化しているか（断定は避ける）
- 版管理と変更記録を残し、文書の形骸化を防いでいるか

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf


## 次の一歩（結論パターン Co に沿って）

放置した場合のワーストシナリオ（監査指摘・証跡欠落）を避けるため、明日から対策を始めてください。 廃止・退役の手順と記録の形を決め、保持と再現性を確保する。 自部門で「誰が承認者か」「証跡をどこに残すか」を1つ決め、監査法人に証憑の形を事前に1回確認する。
