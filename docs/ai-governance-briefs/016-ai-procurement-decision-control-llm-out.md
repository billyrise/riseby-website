## リード（1段落）

監査で差し戻される要因の多くは、証跡の目次が監査側の期待と一致していないことです。

本稿の焦点は「“調達審査ゲート（RACI）”」です。調達審査ゲート（RACI）と承認フローについて、責任分界・証跡・監査提出の目次を具体化します。集中と分散の意思決定基準を文書化し、選択の根拠を記録します。 例外の基準と有効期限を設け、恒久化すべきものは正式申請に切り替える運用にします。

## 本文

### 1. 選定基準

本稿の焦点は「“調達審査ゲート（RACI）”」です。選定基準では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。集中と分散の意思決定基準を文書化し、選択の根拠を記録します。 例外の基準と有効期限を設け、恒久化すべきものは正式申請に切り替える運用にします。

さらに、KRI・閾値・エスカレーション先を決め、ダッシュボードやレビューで追います。 透明性表示やコンテンツ分類の手順を文書化し、公開前チェックの記録を残します。

加えて、ボード・監査向けの最小KRIを決め、閾値 breach 時のアクションを明文化します。 品質が壊れるポイントを特定し、測定・是正・証跡のループを回します。

ここに図1を挿入

### 2. 評価プロセス

攻撃パターンと対策の対応表を作り、検知・是正の記録を残します。 著作権・表示・証跡の争点を一覧化し、方針と手続きを対応させます。

あわせて、リスク許容度を利用ケース承認に落とし、レッドラインを定義します。 例外が増えないよう、抑制策と教育、KRIで棚卸しを回します。

また、何を見るか・誰が見るか・閾値・アクションを決め、エスカレーションを明文化します。 境界定義と統制、契約、運用を一貫させ、証跡の目次に含めます。

ここに図2を挿入

### 3. 契約・SLA

脅威と統制の対応、監視、演習の記録をセットにします。 手法の使い所と限界を注記し、匿名化率・再識別リスクを記録します。

あわせて、Buy/Buildの評価軸を決め、選定・契約・監視・証跡を一貫させます。 ログ完全性・保持・改ざん検知を設計し、監査で説明できる形にします。

また、グローバル運用の抜け穴をガードレールで塞ぎ、移行計画と証跡を決めます。 インシデント時の報告先とエスカレーション閾値を決め、記録を欠かさないようにします。

ここに図3を挿入

### 4. 継続監視

申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。 誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。

あわせて、DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。 廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。

また、漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。 PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。

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
図1: B, 図2: C, 図3: I

## 図の形式（記録用・必須）
図1: Table, 図2: SVG, 図3: Mermaid

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“調達審査ゲート（RACI）”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、申請フローと例外の基準を1つ決め、承認記録を必ず残すルールにすると、他領域の設計の基準になります。

## チェックリスト（10項目）

- 学習データ・出力物の権利と責任を方針化しているか
- 証跡を改ざん耐性で保全し、保持期間を明示しているか
- KRI・閾値・エスカレーション先を決めているか
- 証跡の最小目次を固定し、欠落をチェックしているか
- 規制・標準との対応関係を一覧化しているか（断定は避ける）
- 版管理と変更記録を残し、文書の形骸化を防いでいるか
- ボード・監査向けの最小KRIと閾値 breach 時のアクションを決めているか
- 教育・周知の記録を残しているか
- 品質指標・閾値・是正を継続的に追っているか
- 申請―審査―承認のフローを文書化し、証跡を残しているか

## 参考文献（3つ以上、発行年または一次資料明記）

- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework


## 次の一歩（結論パターン Co に沿って）

明日から始められる3つのステップです。 証跡の目次を1枚にまとめ、保管責任者を1人決め、四半期の棚卸日をカレンダーに登録する。 申請―審査―承認のフローを文書化し、例外の基準と有効期限を明文化する。
