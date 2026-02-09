## リード（1段落）

ある企業では、AI倫理委員会を設けたが承認と開発のゲートがつながらず、形骸化した事例があります。

本稿の焦点は「“分類タクソノミー”」です。生成・編集の分類タクソノミーについて、責任分界・証跡・監査提出の目次を具体化します。申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。 誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。

## 本文

### 1. なぜ今か

本稿の焦点は「“分類タクソノミー”」です。なぜ今かでは、理念で終わらせず運用・証跡・監査可能性に落とすための要件を整理します。RACI、申請―審査―例外―更新、証跡、継続評価、インシデントの5要素のうち、このテーマに応じた項目を押さえます。申請から審査、承認、例外、棚卸までのフローを文書化し、証跡を残す設計にします。 誰が承認者（A）で誰が実行責任者（R）かをRACIで明示し、曖昧にしないようにします。

さらに、DPIAや利用目的の承認フローをデータ担当と連携させ、証跡を紐づけます。 廃止・退役時の手順と記録を決め、データ保持と再現性を確保します。

加えて、漏えい経路ごとにDLP・IDP・CASB等の統制を設計し、境界を守ります。 PETsや合成データの使い所と限界を文書化し、監査で説明できるようにします。

ここに図1を挿入

### 2. 要求

データ種類と義務の対応をマトリクス化し、DPIA・承認の記録を保全します。 三線防衛が崩れないよう、1線・2線・3線の役割と証跡の接続を決めます。

あわせて、ProofとAssuranceの分界を決め、監査が求める証憑の形と揃えます。 退役手順と証跡を決め、記録なし・責任不明・再現不能を防ぎます。

また、入力・境界・出力・学習データの経路を図化し、統制の抜け穴をなくします。 典型契約論点を条項と証跡でカバーし、雛形で効率化します。

ここに図2を挿入

### 3. 運用

選定基準と評価プロセス、契約・SLA、継続監視、証跡を一貫して設計します。 コンテンツ種別と義務、表示、チェック、公開、記録のフローを決めます。

あわせて、レッドラインを定義し、許容度設計と承認運用、例外・KRIを決めます。 BCPとAI依存の停止・代替・復旧手順を決め、証跡を残します。

また、責任の所在（RACI）を一枚にまとめ、関係者と共有しておくことが第一歩です。 規制・標準との対応関係は一覧化しつつ、断定は避け条件を明示します。

ここに図3を挿入

### 4. 証跡

証跡は改ざん耐性（ハッシュやアクセス制御）を確保し、保持期間を明示します。 開発フェーズとリリース承認のゲートを設け、通過記録を証跡として残します。

あわせて、レッドチームや演習の計画・結果・是正を記録し、脅威モデルを更新します。 証跡の最小セットを「目次」として固定し、欠落しやすい項目をチェックします。

また、選定基準と評価プロセスを文書化し、契約・継続監視・証跡を一貫させます。 表示義務と公開前チェックを運用に落とし、証跡の目次に含めます。

## 図1（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">なぜ今かと運用</p>
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
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">要求・計画</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止</td></tr>
  </tbody>
</table>
```

## 図3（SVG）

```
<svg viewBox="0 0 260 140" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="12" width="180" height="32" rx="4" fill="#e0f2fe"/>
  <text x="130" y="32" text-anchor="middle" font-size="10">方針</text>
  <rect x="40" y="52" width="180" height="32" rx="4" fill="#dcfce7"/>
  <text x="130" y="72" text-anchor="middle" font-size="10">プロセス</text>
  <rect x="40" y="92" width="180" height="32" rx="4" fill="#fef9c3"/>
  <text x="130" y="112" text-anchor="middle" font-size="10">運用・証跡</text>
</svg>
```

## 図の型（記録用・必須）
図1: E, 図2: D, 図3: F

## 図の形式（記録用・必須）
図1: HTML, 図2: Table, 図3: SVG

## 固有の一文（要点ボックス用1文）

監査で問われやすいのは「“分類タクソノミー”」に関して、責任分界と証跡の目次が揃っていないことです。明日から、自部門で責任者と証跡の保管者を1人ずつ決め、証跡の目次を1枚にまとめて監査と1回確認することをお勧めします。

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

- EU AI Act（欧州委員会）. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf
- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework


## 次の一歩（結論パターン Co に沿って）

今日のベストプラクティスは明日の最低要件になり得ます。明日から、 自部門で「誰が承認者か」「証跡をどこに残すか」を1つ決め、監査法人に証憑の形を事前に1回確認する。 証跡の目次を1枚にまとめ、保管責任者を1人決め、四半期の棚卸日をカレンダーに登録する。
