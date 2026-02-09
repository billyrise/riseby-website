#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIガバナンス記事の description を修正する。
- meta description / og:description / twitter:description / JSON-LD から ** を除去
- 改行を含む content を1行に正規化（SERP・OG 表示の安定化）
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GOV_DIR = BASE_DIR / "blog" / "ai-governance"


def normalize(s: str) -> str:
    if not s:
        return s
    s = s.replace("**", "")
    s = s.replace("\n", " ").replace("\r", " ")
    s = re.sub(r"  +", " ", s)
    return s.strip()


def fix_one(path: Path) -> tuple[bool, str]:
    if path.name == "index.html":
        return False, "skip"
    text = path.read_text(encoding="utf-8")

    # 1) 全体で ** を除去（メタ・JSON-LD 用）
    text = text.replace("**", "")

    # 2) meta name="description" の content を1行に（改行含む場合）
    def fix_meta_content(match):
        pre, content, post = match.group(1), match.group(2), match.group(3)
        return pre + normalize(content) + post

    text = re.sub(
        r'(<meta name="description" content=")((?:.|\n)*?)(">)',
        fix_meta_content,
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(
        r'(<meta property="og:description" content=")((?:.|\n)*?)(">)',
        fix_meta_content,
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(
        r'(<meta name="twitter:description" content=")((?:.|\n)*?)(">)',
        fix_meta_content,
        text,
        count=1,
        flags=re.DOTALL,
    )

    # 3) JSON-LD BlogPosting 内の "description":"値" を正規化（\n と \n をスペースに）
    def fix_ld_description(m):
        val = m.group(1).replace("\\n", " ").replace("\n", " ")
        val = re.sub(r"  +", " ", val).strip()
        return '"description":"' + val + '"'

    text = re.sub(
        r'"description"\s*:\s*"((?:[^"\\]|\\.)*)"',
        fix_ld_description,
        text,
        count=1,
    )

    path.write_text(text, encoding="utf-8")
    return True, "ok"


def main():
    ok = err = skip = 0
    for path in sorted(GOV_DIR.glob("*.html")):
        try:
            done, msg = fix_one(path)
            if done:
                ok += 1
                print(path.name)
            else:
                skip += 1
        except Exception as e:
            err += 1
            print(path.name, "ERROR", e)
    print(f"Fixed: {ok}, skipped: {skip}, errors: {err}")


if __name__ == "__main__":
    main()
