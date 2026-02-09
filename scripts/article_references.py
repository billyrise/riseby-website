#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
記事テーマに応じた参考文献を返す。全記事で同じ3件にしない。
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DESIGN_PATH = BASE_DIR / "docs" / "ai-governance-blog-design.md"

# 参照プール（key -> (表示ラベル, URL)）
REFS_POOL = {
    "nist": ("NIST AI RMF (2023)", "https://www.nist.gov/itl/ai-risk-management-framework"),
    "iso": ("ISO/IEC 42001 (AIMS)", "https://www.iso.org/standard/42001"),
    "meti": ("経済産業省「AI事業者ガイドライン」2025年3月公表版", "https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf"),
    "eu_act": ("EU AI Act（欧州委員会）", "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai"),
    "gpai": ("GPAI Code of Practice（欧州委員会）", "https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai"),
    "oecd": ("OECD AI原則", "https://oecd.ai/en/ai-principles"),
    "gdpr": ("GDPR（EU一般データ保護規則）", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679"),
    "ieee": ("IEEE Ethically Aligned Design", "https://standards.ieee.org/wp-content/uploads/import/documents/other/ead_v2.pdf"),
    "g7": ("G7広島AIプロセス", "https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20231030_3.pdf"),
}

TEMPLATE_TO_SECTION = {
    "T01": "A", "T02": "A", "T03": "A", "T04": "A", "T05": "A",
    "T06": "B", "T07": "B", "T08": "B", "T09": "B", "T10": "B",
    "T11": "C", "T12": "C", "T13": "C", "T14": "C", "T15": "C",
    "T16": "D", "T17": "D", "T18": "D", "T19": "D", "T20": "D",
    "T21": "E", "T22": "E", "T23": "E", "T24": "E", "T25": "I",
    "T26": "F", "T27": "F", "T28": "F", "T29": "F", "T30": "F",
    "T31": "G", "T32": "G",
}

# セクション別デフォルト参照（3つ）— 全記事が同じ3リンクにならないようセクションで差をつける
SECTION_DEFAULT_REFS = {
    "A": ["nist", "iso", "meti"],       # 統治
    "B": ["nist", "iso", "oecd"],       # リスク → OECD原則
    "C": ["nist", "iso", "g7"],         # ライフサイクル → G7広島
    "D": ["nist", "iso", "meti"],       # 証跡
    "E": ["nist", "iso", "ieee"],       # セキュリティ → IEEE
    "F": ["gdpr", "iso", "meti"],       # プライバシー
    "G": ["eu_act", "meti", "nist"],    # 法務・規制
    "I": ["iso", "meti", "nist"],       # 調達
}

# slug プレフィックス/含む → テーマに合う参照3つ（上書き）
SLUG_REF_OVERRIDES = [
    # EU・欧州
    ("eu-ai-act", ["eu_act", "nist", "meti"]),
    ("gpai-llm-governance", ["gpai", "eu_act", "nist"]),
    ("extra-territorial-brussels", ["eu_act", "meti", "nist"]),
    # 日本
    ("japan-pip", ["meti", "g7", "nist"]),
    ("japan-ai-guidelines", ["meti", "g7", "iso"]),
    # 各国・地域
    ("us-ai-regulation", ["nist", "meti", "iso"]),
    ("china-genai", ["meti", "nist", "iso"]),
    ("uk-singapore", ["oecd", "meti", "nist"]),
    # 規格・フレームワーク
    ("iso-42001", ["iso", "nist", "meti"]),
    ("nist-ai-rmf", ["nist", "iso", "meti"]),
    ("multi-framework", ["nist", "iso", "eu_act"]),
    # OECD・国際
    ("oecd-ai-principles", ["oecd", "nist", "meti"]),
    ("g7-oecd-hiroshima", ["g7", "oecd", "meti"]),
    # プライバシー・GDPR
    ("gdpr-genai", ["gdpr", "eu_act", "meti"]),
    ("pets-privacy", ["gdpr", "iso", "meti"]),
    ("synthetic-data-privacy", ["gdpr", "meti", "nist"]),
    # 透明性・表示
    ("content-transparency", ["eu_act", "meti", "nist"]),
    ("ai-generated-display", ["eu_act", "meti", "nist"]),
    ("generated-edited-classification", ["eu_act", "meti", "nist"]),
    ("watermark-metadata", ["eu_act", "meti", "nist"]),
    ("deepfake-countermeasures", ["eu_act", "meti", "nist"]),
    # 評価・レッドチーム
    ("red-teaming-guide", ["nist", "iso", "meti"]),
    ("evals-basics", ["nist", "iso", "meti"]),
    ("eval-automation", ["nist", "iso", "meti"]),
    ("continuous-evaluation-drift", ["nist", "iso", "meti"]),
    # 監査・証跡
    ("audit-", ["nist", "iso", "meti"]),
    ("evidence-", ["nist", "iso", "meti"]),
    ("dispute-evidence", ["nist", "iso", "meti"]),
    ("external-audit", ["nist", "iso", "meti"]),
    ("internal-audit", ["nist", "iso", "meti"]),
    # 業界別
    ("industry-", ["meti", "nist", "iso"]),
]


def _get_ref_keys_for_article(no: int, slug: str, template_id: str) -> list:
    """記事の no, slug, template_id から参照キー3つを返す。"""
    section = TEMPLATE_TO_SECTION.get(template_id, "A")
    default = SECTION_DEFAULT_REFS.get(section, ["nist", "iso", "meti"])

    for prefix, keys in SLUG_REF_OVERRIDES:
        if prefix in slug and len(keys) >= 3:
            # キーがプールに存在するものだけに限定
            return [k for k in keys if k in REFS_POOL][:3]
    return default


def get_references_markdown(no: int, slug: str, template_id: str) -> str:
    """記事用の参考文献ブロック（Markdown）を返す。3つ以上、発行年または一次資料明記。"""
    keys = _get_ref_keys_for_article(no, slug, template_id)
    lines = []
    for k in keys[:3]:
        if k not in REFS_POOL:
            continue
        label, url = REFS_POOL[k]
        lines.append(f"- {label}. {url}")
    if not lines:
        lines = [
            "- NIST AI RMF (2023). https://www.nist.gov/itl/ai-risk-management-framework",
            "- ISO/IEC 42001 (AIMS). https://www.iso.org/standard/42001",
            "- 経済産業省「AI事業者ガイドライン」2025年3月公表版. https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20250328_2.pdf",
        ]
    return "\n".join(lines)


def get_references_for_design_list():
    """設計図から全163記事の (no, slug, template_id) を取得し、各記事の参考文献Markdownを返す。"""
    text = DESIGN_PATH.read_text(encoding="utf-8")
    table_32 = []
    table_33 = []
    in_32 = in_33 = False
    for line in text.splitlines():
        if "### 3.2 163記事" in line:
            in_32, in_33 = True, False
            continue
        if "### 3.3 記事DNA" in line:
            in_32, in_33 = False, True
            continue
        if in_32 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3 and parts[0].isdigit():
                no = int(parts[0])
                if 1 <= no <= 163:
                    table_32.append({"no": no, "slug": parts[1], "template_id": parts[2] if len(parts) > 2 else "T01"})
        if in_33 and line.strip().startswith("|") and "| No. |" not in line and "|---" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 10 and parts[0].isdigit():
                no = int(parts[0])
                if 1 <= no <= 163:
                    table_33.append({"no": no, "slug": parts[1]})
    by_no_32 = {r["no"]: r for r in table_32}
    by_no_33 = {r["no"]: r for r in table_33}
    out = {}
    for no in range(1, 164):
        r33 = by_no_33.get(no)
        r32 = by_no_32.get(no)
        if not r33:
            continue
        slug = r33["slug"]
        tid = (r32 or {}).get("template_id", "T01")
        out[no] = get_references_markdown(no, slug, tid)
    return out
