#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全 llm-out の「## 参考文献」ブロックを、記事テーマに応じた参照に差し替え、HTML を再生成する。
"""
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "scripts"))

from article_references import get_references_markdown
from gen_llm_out_31_163 import parse_design

BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"


def patch_one_llm_out(no: int, slug: str, template_id: str) -> bool:
    path = BRIEFS_DIR / f"{no:03d}-{slug}-llm-out.md"
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    new_refs = get_references_markdown(no, slug, template_id)
    # ## 参考文献（3つ以上...）から次の ## または末尾までを置換
    pattern = re.compile(
        r"(## 参考文献[^\n]*\s*\n)(.*?)(?=\n## |\Z)",
        re.DOTALL,
    )
    new_text, n = pattern.subn(lambda m: m.group(1) + new_refs + "\n\n", text, count=1)
    if n == 0:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    articles = parse_design()
    patched = 0
    for a in articles:
        if patch_one_llm_out(a["no"], a["slug"], a["template_id"]):
            patched += 1
            print(f"Patched {a['no']:03d}-{a['slug']}")
    print(f"\n{patched} files updated. Run batch_apply_llm_article to refresh HTML.")


if __name__ == "__main__":
    main()
