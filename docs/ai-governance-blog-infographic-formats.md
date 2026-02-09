# AIガバナンスブログ：インフォグラフィック形式（30種類）

**Cursorへの強制ルール（冒頭）**  
図は必ず **指定フォーマット**（SVG / HTML / Table / **Mermaid** 等）で出力すること。同一形式を連続して使わない。記事HTMLにインラインで埋め込むか `/assets/diagrams/` に保存すること。  
**直前に生成された5記事で使用されているインフォグラフィック形式は、各形式につき1つまでしか使えない。**  
**図の幅・改行**: 図の横幅は記事幅の**90%まで**表示される。おかしな改行（単語の途中・括弧だけの行）を防ぐため、SVG では **viewBox を広めに取る**（例：`0 0 1000 320`）、ラベルを短くする、括弧の前後に半角スペースを入れる等を検討すること。  
**括弧のサイズ**: 図の中で**括弧とカッコ内の文字は1pt小さく**表示する（apply 側で SVG の括弧部分を 0.9em に変換する。執筆時は括弧はそのまま書く）。

---

## 01) SVG（インライン：基本図形）

**いつ使う**: レイヤー図、責任分界の箱図、簡単なフロー。

```html
<svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="40" width="220" height="70" rx="12"/>
  <text x="60" y="85">Policy</text>
  <rect x="290" y="40" width="220" height="70" rx="12"/>
  <text x="310" y="85">Process</text>
  <line x1="260" y1="75" x2="290" y2="75" stroke-width="2"/>
</svg>
```

---

## 02) SVG（矢印・マーカー定義：defs）

**いつ使う**: フロー図の矢印を統一したいとき。

```html
<svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L9,3 L0,6 Z"/>
    </marker>
  </defs>
  <line x1="100" y1="100" x2="700" y2="100" stroke-width="3" marker-end="url(#arrow)"/>
</svg>
```

---

## 03) SVG（Pathで自由図形）

**いつ使う**: 境界・バリア・曲線矢印・ブレースなど。

```html
<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
  <path d="M20 60 C80 10, 140 110, 200 60" fill="none" stroke-width="3"/>
</svg>
```

---

## 04) HTML+CSS（カードレイアウト図）

**いつ使う**: 3列比較（中央集権/連邦制/ハイブリッド）、メリデメ整理。

```html
<div class="grid">
  <div class="card"><h3>Option A</h3><p>When...</p></div>
  <div class="card"><h3>Option B</h3><p>When...</p></div>
  <div class="card"><h3>Option C</h3><p>When...</p></div>
</div>
<style>
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.card{border:1px solid #ddd;border-radius:12px;padding:14px}
</style>
```

---

## 05) HTML Table（RACI表）

**いつ使う**: 役割分担（Board/Legal/CISO/Audit/BU）。

```html
<table>
  <tr><th>Task</th><th>Board</th><th>Legal</th><th>CISO</th><th>Audit</th></tr>
  <tr><td>Use-case approval</td><td>A</td><td>C</td><td>R</td><td>I</td></tr>
</table>
```

---

## 06) Canvas 2D（HTML5 Canvas）

**いつ使う**: 軽量な図を動的に生成。

```html
<canvas id="c" width="800" height="240"></canvas>
<script>
const ctx = document.getElementById('c').getContext('2d');
ctx.strokeRect(40,40,220,70); ctx.fillText("Policy",60,80);
ctx.beginPath(); ctx.moveTo(260,75); ctx.lineTo(290,75); ctx.stroke();
</script>
```

---

## 07) Chart.js（棒・折れ線・円）

**いつ使う**: KPI/KRI、推移、内訳。

```html
<canvas id="kri"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
new Chart(document.getElementById('kri'),{
  type:'bar',
  data:{labels:['W1','W2'],datasets:[{label:'KRI',data:[3,5]}]}
});
</script>
```

---

## 08) Vega-Lite（宣言的JSON）

**いつ使う**: 監査/証跡で仕様（JSON）を残したい可視化。

```html
<div id="vis"></div>
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
<script>
const spec = {"data":{"values":[{"x":"W1","y":3},{"x":"W2","y":5}]},
"mark":"bar","encoding":{"x":{"field":"x"},"y":{"field":"y"}}};
vegaEmbed('#vis', spec);
</script>
```

---

## 09) Plotly（宣言的JSON・対話）

**いつ使う**: ドリフト/分布、ホバー、ズーム。

```html
<div id="p"></div>
<script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>
<script>
Plotly.newPlot('p', [{x:['W1','W2'], y:[3,5], type:'bar'}], {title:'KRI'});
</script>
```

---

## 10) D3.js（SVGをコードで組み立て）

**いつ使う**: 独自の図（境界、ネットワーク、軸付き）。

```html
<svg id="s" width="800" height="240"></svg>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
const svg=d3.select("#s");
svg.append("rect").attr("x",40).attr("y",40).attr("width",220).attr("height",70).attr("rx",12);
</script>
```

---

## 11) Graphviz DOT

**いつ使う**: Evidence Chain、責任の有向グラフ。※DOTはSVGに変換して埋め込む。

```
digraph G {
  rankdir=LR;
  Policy -> Process -> Evidence -> Monitoring;
}
```

---

## 12) PlantUML（Sequence）

**いつ使う**: 承認フローの「誰が何をいつ」。

```
@startuml
actor Requester
participant Reviewer
Requester -> Reviewer: Submit use-case
Reviewer --> Requester: Approve/Reject
@enduml
```

---

## 13) PlantUML（Activity）

**いつ使う**: 申請→審査→例外→更新→棚卸。

```
@startuml
start
:Submit;
if (Risk high?) then (yes)
  :Escalate;
endif
:Decision;
stop
@enduml
```

---

## 14) PlantUML（C4-PlantUML）

**いつ使う**: アーキテクチャ、監査証跡パイプラインの構成。

---

## 15) draw.io（XML）

**いつ使う**: デザイナーが編集する前提。.drawio または XML で保存。

---

## 16) Excalidraw（.excalidraw JSON）

**いつ使う**: 手書き風で人間味を出したいとき。

```json
{
  "type":"excalidraw",
  "version":2,
  "elements":[
    {"type":"rectangle","x":40,"y":40,"width":220,"height":70,"roundness":{"type":3}},
    {"type":"text","x":60,"y":60,"text":"Policy","fontSize":20}
  ]
}
```

---

## 17) Excalidraw SVG出力

**いつ使う**: SEO/表示の安定性が必要なブログ。.excalidraw → SVG/PNG 変換して配置。

---

## 18) LaTeX TikZ

**いつ使う**: 論文品質・監査資料・ホワイトペーパー寄り。

```latex
\begin{tikzpicture}
\node[draw,rounded corners] (p) at (0,0) {Policy};
\node[draw,rounded corners] (q) at (4,0) {Process};
\draw[->] (p) -- (q);
\end{tikzpicture}
```

---

## 19) LaTeX PGFPlots

**いつ使う**: KRI推移を版管理できるコードで。

---

## 20) ASCII/Unicodeアート

**いつ使う**: 概念の骨格だけ軽く示す。

```
Policy -> Process -> Evidence -> Monitoring
```

---

## 21) Markdown表＋CSS（擬似ダッシュボード）

**いつ使う**: 軽量KPIカード。CSSで見せ方を統一。

---

## 22) SVGスパークライン

**いつ使う**: 各記事冒頭に指標の変化だけ添える。小さな折れ線を SVG path で。

---

## 23) SVGサンキー

**いつ使う**: データ流通/責任分界の量感。D3のSankey等で静的SVGを出力。

---

## 24) SVGスイムレーン

**いつ使う**: Legal/CISO/BU/Audit に跨る手続きをレーンで固定。`<rect>` と `<line>` で実装。

---

## 25) マトリクス図（HTML Grid）

**いつ使う**: EU AI Act 義務×対象、リスク×統制。CSS grid で表＋色。

---

## 26) タイムライン（HTML/CSS）

**いつ使う**: 90日導入、年次計画、インシデント時系列。`<ol>` + CSS。

---

## 27) チェックリスト図（カード＋アイコン：HTML）

**いつ使う**: 最小要件・監査差し戻しTop5。箇条書きを図化。

---

## 28) ツリーマップ（Vega-Lite/Plotly）

**いつ使う**: リスク領域の構成比、統制の投資配分。

---

## 29) ヒートマップ（Vega-Lite/Plotly）

**いつ使う**: リスクヒートマップ、業界別論点。

---

## 30) Evidence Chain 専用（SVG/Graphviz）

**いつ使う**: Evidence Bundle、改ざん耐性、提出物。Graphviz で関係、SVG で固定レイアウト。

---

## 記事出力時のルール

- **多様なインフォグラフィックを必ず使用**：3つの図のうち、少なくとも2種類以上の**形式**（SVG / HTML / Canvas / Chart.js / Vega-Lite / DOT / PlantUML / Table 等）を使うこと。
- **直近5記事で使用された形式は各1回まで**：直前に生成された5記事の図で使われた形式は、この記事では**各形式につき1つまで**しか使ってよい。例：直近5記事で SVG が4回使われていれば、この記事で SVG は1つまで。
- 図は **指定フォーマット**（SVG / HTML / Table / Mermaid 等）で出力。同一形式を連続して使わない。記事にインライン埋め込みまたは `/assets/diagrams/` に保存すること。
