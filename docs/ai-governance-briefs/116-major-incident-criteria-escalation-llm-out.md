## リード（1段落）

監査で差し戻される要因の多くは、証跡の目次が監査側の期待と一致していないことです。

本稿の焦点は「“重大基準”」です。重大基準とエスカレーションについて、責任分界・証跡・監査提出の目次を具体化します。脅威と統制の対応、監視、演習の記録をセットにします。 手法の使い所と限界を注記し、匿名化率・再識別リスクを記録します。

## 本文

### 1. 例外が増える理由

本稿の焦点は「“重大基準”」です。例外が増える理由では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。脅威と統制の対応、監視、演習の記録をセットにします。 手法の使い所と限界を注記し、匿名化率・再識別リスクを記録します。

さらに、Buy/Buildの評価軸を決め、選定・契約・監視・証跡を一貫させます。 ログ完全性・保持・改ざん検知を設計し、監査で説明できる形にします。

加えて、グローバル運用の抜け穴をガードレールで塞ぎ、移行計画と証跡を決めます。 インシデント時の報告先とエスカレーション閾値を決め、記録を欠かさないようにします。

ここに図1を挿入

### 2. 抑制

申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。 誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。

あわせて、DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。 廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。

また、漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。 PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。

ここに図2を挿入

### 3. 教育

データ種類と義務の対応をマトリクス化し、DPIA・承認の記録を保全します。 三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。

あわせて、ProofとAssuranceの分界を決め、監査が求める証憑の形と揃えます。 退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。

また、入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。 典型契約論点を条項と証跡でカバーし、雛形で効率化します。

ここに図3を挿入

### 4. KRI

選定基準と評価プロセス、契約・SLA、継続監視、証跡を一貫して設計します。 コンテンツ種別と義務、表示、チェック、公開、記録のフローを決めます。

あわせて、レッドラインを定義し、許容度設計と承認運用、例外・KRIを決めます。 BCPとAI依存の停止・代替・復旧手順を決め、証跡を残します。

また、責任の所在（RACI）を一枚にまとめ、関係者と共有しておくことが第一歩です。 規制・標準との対応関係は一覧化しつつ、断定は避け条件を明示します。

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
図1: B, 図2: C, 図3: I

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“重大基準”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、申請フローと例外の基準を1つ決め、承認記録を必ず残すルールにすると、他領域の設計の基準になります。

## チェックリスト（10項目）

- 例外の基準と有効期限を決め、四半期で棚卸しているか
- 脅威分類と統制・監視・演習の記録を揃えているか
- ログ種別・目的・保持期間を一覧化し、完全性を検証しているか
- インシデント時の報告・エスカレーション手順を決めているか
- DPIA・利用目的承認と証跡の連携を取っているか
- 争点化に備えた証拠を想定し、日付・責任者の整合を保っているか
- 四半期の棚卸を予定し、記録を残しているか
- ベンダー・委託先との責任分界を契約と証跡で明示しているか
- RACI（責任者・承認者）を決め、一枚にまとめているか
- 開発・リリースのゲートと通過記録を設計しているか

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- G7広島AIプロセス. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20231030_3.pdf


## 次の一歩（結論パターン Co に沿って）

明日から始められる3つのステップです。 版管理と変更記録のルールを決め、文書の形骸化を防ぐための教育を1回行う。 争点化を想定した証拠のリストを作り、日付・責任者・版の整合を保つ手順を決める。
