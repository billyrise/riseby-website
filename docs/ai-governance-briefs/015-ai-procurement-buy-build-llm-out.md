## リード（1段落）

ある企業では、AI倫理委員会を設けたが承認と開発のゲートがつながらず、形骸化した事例があります。

本稿の焦点は「“Buy/Build判断の評価軸”」です。Buy/Build判断の評価軸について、責任分界・証跡・監査提出の目次を具体化します。ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを設計します。

## 本文

### 1. 選定基準

本稿の焦点は「“Buy/Build判断の評価軸”」です。選定基準では、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。ライフサイクルに評価ゲートを埋め込み、通過記録を証跡にします。 年次で優先5領域を決め、予算・人材・レビューのサイクルを設計します。

さらに、ボード指標の最小セットと意思決定ログ、四半期レビューを運用します。 証跡は改ざん耐性（ハッシュやアクセス制御）を確保し、保持期間を明示します。

加えて、開発フェーズとリリース承認のゲートを設け、通過記録を証跡として残します。 レッドチームや演習の計画・結果・是正を記録し、脅威モデルを更新します。

ここに図1を挿入

### 2. 評価プロセス

KRI・閾値・エスカレーション先を決め、ダッシュボードやレビューで追います。 透明性表示やコンテンツ分類の手順を文書化し、公開前チェックの記録を残します。

あわせて、ボード・監査向けの最小KRIを決め、閾値 breach 時のアクションを明文化します。 品質が壊れるポイントを特定し、測定・是正・証跡のループを回します。

また、集中と分散のトレードオフを整理し、抜け穴がないようガードレールを置きます。 年1の監査では不足するため、継続適合性評価と自動化を運用に組み込みます。

ここに図2を挿入

### 3. 契約・SLA

リスク許容度を利用ケース承認に落とし、レッドラインを定義します。 例外が増えないよう、抑制策と教育、KRIで棚卸しを回します。

あわせて、何を見るか・誰が見るか・閾値・アクションを決め、エスカレーションを明文化します。 境界定義と統制、契約、運用を一貫させ、証跡の目次に含めます。

また、エスカレーション閾値と重大基準を明文化し、記録と棚卸をセットにします。 契約条項のチェックリストを用意し、living clausesで見直し可能にします。

ここに図3を挿入

### 4. 継続監視

Buy/Buildの評価軸を決め、選定・契約・監視・証跡を一貫させます。 ログ完全性・保持・改ざん検知を設計し、監査で説明できる形にします。

あわせて、グローバル運用の抜け穴をガードレールで塞ぎ、移行計画と証跡を決めます。 インシデント時の報告先とエスカレーション閾値を決め、記録を欠かさないようにします。

また、脅威を分類し、優先順位をつけたうえで統制と監視を設計します。 品質指標と閾値を決め、ドリフトや是正件数を継続的に追います。

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
図1: E, 図2: D, 図3: F

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“Buy/Build判断の評価軸”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、自部門で責任者と証跡の保管者を1人ずつ決め、証跡の目次を1枚にまとめて監査と1回確認することをお勧めします。

## チェックリスト（10項目）

- 契約にBOM・ログ提供義務を盛り込み、責任分界を明示しているか
- Evidence Bundleの形を設計し、ハッシュで改ざん検知しているか
- 監査提出の目次を監査法人と事前にすり合わせているか
- レッドチーム・演習の計画・結果・是正を記録しているか
- アクセス制御を申請・承認・付与のフローに落としているか
- 成果物ごとに作成者・承認者・保管場所を決めているか
- 透明性表示・公開前チェックの記録を残しているか
- 例外の基準と有効期限を決め、四半期で棚卸しているか
- 脅威分類と統制・監視・演習の記録を揃えているか
- ログ種別・目的・保持期間を一覧化し、完全性を検証しているか

## 参考文献（3つ以上、発行年または一次資料明記）

- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework


## 次の一歩（結論パターン Co に沿って）

今日のベストプラクティスは明日の最低要件になり得ます。明日から、 自部門で「誰が承認者か」「証跡をどこに残すか」を1つ決め、監査法人に証憑の形を事前に1回確認する。 証跡の目次を1枚にまとめ、保管責任者を1人決め、四半期の棚卸日をカレンダーに登録する。
