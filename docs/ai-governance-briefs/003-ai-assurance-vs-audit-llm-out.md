## リード（1段落）

「保証（Assurance）と監査（Audit）の違いを説明できますか」と監査人に問われ、答えに詰まる担当は少なくありません。本稿の焦点は**Assuranceの限界と、監査が求める証憑の形**にあります。内部保証の成果物と外部監査の期待をすり合わせないと、差し戻しや重複作業が増えます。用語定義、分界、成果物、実装の勘所を整理し、明日から使える形に落とします。

## 本文

### 1. 用語定義

**Proof**は組織が自ら「やった」と示す証拠づくり、**Assurance**はその証拠に基づく保証（内部または外部）、**Audit**は独立した第三者が証拠を検証し意見を表明する活動です。AIガバナンスでは、Proof（方針・プロセス・証跡）を整え、Assurance（適合性評価・継続的適合性）で担保し、監査では「証憑の形と完全性」が問われます。用語を揃えないと、監査人が求める「証跡の目次」と社内の成果物が噛み合ず、差し戻しの原因になります。

ここに図1を挿入

### 2. 分界

保証と監査の分界では、**誰が保証の責任者で、誰が監査提出物をまとめるか**を決めます。保証は2線（リスク・コンプラ）や内部監査が担い、監査提出は証跡の保管責任者と監査担当が連携します。分界が曖昧だと、保証で出した成果物と監査で求める証憑の形式がずれ、事後の再構成や説明の重複が発生します。あらかじめ「監査提出の目次」を監査法人と1回すり合わせ、Proof/Assuranceの成果物をその目次にマッピングしておくことを推奨します。

ここに図2を挿入

### 3. 成果物

監査で求められやすい成果物は、**方針・規程の版管理記録、申請―審査―承認のログ、証跡の完全性（ハッシュ・保持期間）、継続評価・是正の記録**です。成果物ごとに「誰が作成し、誰が承認し、どこに何年保持するか」を決め、Evidence Chain（ログ→検証→保全→提出）が切れないようにします。成果物の形式（ファイル形式・メタデータ・目次）を監査側の期待と合わせておくと、提出時の差し戻しを減らせます。

ここに図3を挿入

### 4. 実装の勘所

実装では、**証憑形式の不一致、責任者欠落、事後再構成、サンプル説明なし、継続評価の記録なし**が監査で差し戻されやすいポイントです。これらを避けるため、証跡の目次を1枚にまとめ、各項目の責任者と形式を決め、四半期ごとに棚卸と継続評価の記録を残します。是正の流れ（発見→原因→是正→再発防止）をテンプレ化し、記録を欠かさないようにしてください。

## 図1（SVG）

```
<svg viewBox="0 0 260 140" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="12" width="180" height="32" rx="4" fill="#e0f2fe"/>
  <text x="130" y="32" text-anchor="middle" font-size="10">Proof（証拠づくり）</text>
  <rect x="40" y="52" width="180" height="32" rx="4" fill="#dcfce7"/>
  <text x="130" y="72" text-anchor="middle" font-size="10">Assurance（保証）</text>
  <rect x="40" y="92" width="180" height="32" rx="4" fill="#fef9c3"/>
  <text x="130" y="112" text-anchor="middle" font-size="10">Audit（監査）</text>
</svg>
```

## 図2（HTML）

```
<div style="max-width: 520px; margin: 1rem auto; border-left: 3px solid #003E68; padding-left: 1rem;">
  <p style="margin: 0 0 0.5rem; font-weight: bold;">分界と運用</p>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li style="margin: 0.25rem 0;">保証責任者と監査提出担当を決め、証跡の目次で接続</li>
    <li style="margin: 0.25rem 0;">監査提出の目次を監査法人と事前合意</li>
    <li style="margin: 0.25rem 0;">継続評価・是正の記録を欠かさない</li>
  </ul>
</div>
```

## 図3（Table）

```
<table style="width:100%; max-width: 520px; margin: 1rem auto; border-collapse: collapse;">
  <thead>
    <tr style="background: #f1f5f9;">
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">証跡</th>
      <th style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">目的</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">方針・版管理記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">選択の根拠</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">申請・承認記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">通過判断の説明</td></tr>
    <tr><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">是正・継続評価記録</td><td style="border: 1px solid #cbd5e1; padding: 0.5rem 0.75rem;">再発防止・説明</td></tr>
  </tbody>
</table>
```

## 図の型（記録用・必須）
図1: A, 図2: B, 図3: G

## 図の形式（記録用・必須）
図1: SVG, 図2: HTML, 図3: Table

## 固有の一文（要点ボックス用1文）

監査で差し戻される典型は、**「保証で出した成果物と監査が求める証憑の形式が一致しておらず、事後に目次の再構成を求められる」**ケースです。事前に証跡の目次を監査法人と1回すり合わせておくだけで、本番の負荷を大きく減らせます。

## チェックリスト（10項目）

- Proof/Assurance/Auditの用語を社内で統一しているか
- 保証責任者と監査提出担当の分界を文書化しているか
- 監査提出の目次を監査法人と事前にすり合わせているか
- 申請―審査―承認の証跡を改ざん耐性で保全しているか
- 証憑の形式（ファイル形式・メタデータ）を監査期待と合わせているか
- 継続評価・是正の記録を残しているか
- 責任者欠落・事後再構成が起きないようRACIを決めているか
- 四半期の棚卸を予定し、記録を残しているか
- 是正の流れをテンプレ化し記録しているか
- 教育・周知の記録を残しているか

## 参考文献（3つ以上、発行年または一次資料明記）

- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001
- OECD AI原則. https://oecd.ai/en/ai-principles


## 次の一歩（結論パターン Co に沿って）

いまの対応が、その後の監査対応と競争力の基盤になります。明日から、保証の成果物一覧と監査提出に必要な証跡の目次を1枚にまとめ、監査法人に「この形で提出して問題ないか」を1回確認してください。あわせて、証跡の保管責任者と提出時の窓口を1人決めておくと、本番がスムーズになります。
