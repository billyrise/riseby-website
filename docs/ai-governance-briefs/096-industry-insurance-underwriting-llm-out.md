## リード（1段落）

監査で差し戻される要因の多くは、証跡の目次が監査側の期待と一致していないことです。

本稿の焦点は「“保険引受の論点”」です。保険引受の論点について、責任分界・証跡・監査提出の目次を具体化します。バイアス評価の手法選択と実施・記録・継続評価をセットにします。 申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。

## 本文

### 1. 評価設計

本稿の焦点は「“保険引受の論点”」です。評価設計では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。バイアス評価の手法選択と実施・記録・継続評価をセットにします。 申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。

さらに、誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。 DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。

加えて、廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。 漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。

ここに図1を挿入

### 2. 実施と記録

Evidence Bundleの形（ログ→検証→保全→提出）を揃え、ハッシュで改ざんを検知します。 データ種類と義務の対応をマトリクス化し、DPIA・承認の記録を保全します。

あわせて、三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。 ProofとAssuranceの分界を決め、監査が求める証憑の形と揃えます。

また、退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。 入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。

ここに図2を挿入

### 3. 継続評価

連鎖（生成→保管→提出→検証）を設計し、監査提示の形を事前に合意します。 選定基準と評価プロセス、契約・SLA、継続監視、証跡を一貫して設計します。

あわせて、コンテンツ種別と義務、表示、チェック、公開、記録のフローを決めます。 レッドラインを定義し、許容度設計と承認運用、例外・KRIを決めます。

また、BCPとAI依存の停止・代替・復旧手順を決め、証跡を残します。 責任の所在（RACI）を一枚にまとめ、関係者と共有しておくことが第一歩です。

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
図1: B, 図2: C, 図3: I

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“保険引受の論点”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、申請フローと例外の基準を1つ決め、承認記録を必ず残すルールにすると、他領域の設計の基準になります。

## チェックリスト（10項目）

- データ境界と漏えい経路に統制を置いているか
- 廃止・退役の手順と記録を決めているか
- 継続評価の記録を残し、是正の流れをテンプレ化しているか
- 契約にBOM・ログ提供義務を盛り込み、責任分界を明示しているか
- Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか
- 監査提出の目次を監査法人と事前にすり合わせているか
- レッドチーム・演習の計画・結果・是正を記録しているか
- アクセス制御を申請・承認・付与のフローに落としているか
- 成果物ごとに作成者・承認者・保管場所を決めているか
- 透明性表示・公開前チェックの記録を残しているか

## 参考文献（3つ以上、発行年または一次資料明記）

- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001


## 次の一歩（結論パターン Co に沿って）

明日から始められる3つのステップです。 データ境界と統制の対応表を作り、担当とAI統制の責任分界を1回決める。 脅威と統制の対応表を更新し、演習の計画・結果・是正を記録する。
