#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blog/ai/*.html の SEO を強化する。
- meta robots (index, follow)
- twitter:title, twitter:description, twitter:image
- BlogPosting 強化 (publisher, image, description, mainEntityOfPage, articleSection, url)
- BreadcrumbList 追加
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
AI_DIR = BASE_DIR / "blog" / "ai"


def esc_json(s: str) -> str:
    if not s:
        return ""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")


def patch_one(path: Path) -> str:
    if path.name == "index.html":
        return "skip"
    text = path.read_text(encoding="utf-8")

    # 既に twitter:title と BreadcrumbList があればスキップ
    if 'name="twitter:title"' in text and "BreadcrumbList" in text:
        return "skip"

    # canonical URL
    m_canonical = re.search(r'<link rel="canonical" href="(https://[^"]+)"', text)
    if not m_canonical:
        return "no_canonical"
    canonical_url = m_canonical.group(1)

    # og:title, meta description
    m_og_title = re.search(r'<meta property="og:title" content="([^"]+)"', text)
    title_attr = m_og_title.group(1) if m_og_title else path.stem
    m_desc = re.search(r'<meta name="description" content="([^"]*)"', text)
    description_attr = m_desc.group(1) if m_desc else ""
    title_ja = title_attr.replace(" | RISEby Blog", "").strip()
    title_ja_json = esc_json(title_ja)
    description_json = esc_json(description_attr)

    # 既存 BlogPosting から datePublished を取得（なければ 2026-02-09）
    date_published = "2026-02-09"
    m_date = re.search(r'"datePublished"\s*:\s*"([^"]+)"', text)
    if m_date:
        date_published = m_date.group(1)

    # 1) canonical の直後に robots を挿入
    if 'name="robots"' not in text:
        text = re.sub(
            r'(<link rel="canonical" href="[^"]+"\s*>)',
            r'\1\n    <meta name="robots" content="index, follow">',
            text,
            count=1,
        )

    # 2) twitter:card の直後に twitter:title, description, image を挿入
    if 'name="twitter:title"' not in text:
        twitter_block = f'''
    <meta name="twitter:title" content="{title_attr}">
    <meta name="twitter:description" content="{description_attr}">
    <meta name="twitter:image" content="https://riseby.net/assets/images/og-image.jpg">'''
        text = re.sub(
            r'(<meta name="twitter:card" content="summary_large_image">)',
            re.escape(r'\1') + twitter_block.replace("\\", "\\\\"),
            text,
            count=1,
        )
        # 上記で re.escape が \1 を壊すので、別のやり方で
        text = re.sub(
            r'<meta name="twitter:card" content="summary_large_image">',
            '<meta name="twitter:card" content="summary_large_image">' + twitter_block,
            text,
            count=1,
        )

    # 3) 既存の BlogPosting を強化版 + BreadcrumbList に置換
    blog_posting_ld = (
        '{"@context":"https://schema.org","@type":"BlogPosting",'
        f'"headline":"{title_ja_json}","description":"{description_json}",'
        f'"datePublished":"{date_published}","dateModified":"{date_published}",'
        '"author":{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net"},'
        '"publisher":{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net","logo":{"@type":"ImageObject","url":"https://riseby.net/assets/images/logo.svg"}},'
        '"image":"https://riseby.net/assets/images/og-image.jpg",'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical_url}"}},'
        '"articleSection":"AI・生成AI",'
        f'"url":"{canonical_url}"}}'
    )
    breadcrumb_ld = (
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"ホーム","item":"https://riseby.net/"},'
        '{"@type":"ListItem","position":2,"name":"ブログ","item":"https://riseby.net/blog/"},'
        '{"@type":"ListItem","position":3,"name":"AI・生成AI","item":"https://riseby.net/blog/ai/"},'
        f'{{"@type":"ListItem","position":4,"name":"{title_ja_json}","item":"{canonical_url}"}}]}}'
    )
    new_ld = f'    <script type="application/ld+json">\n    {blog_posting_ld}\n    </script>\n    <script type="application/ld+json">\n    {breadcrumb_ld}\n    </script>'

    # 既存の BlogPosting スクリプト（複数行の可能性）を置換
    text = re.sub(
        r'<script type="application/ld\+json">\s*\{.*?"@type"\s*:\s*"BlogPosting".*?\}\s*</script>',
        new_ld,
        text,
        count=1,
        flags=re.DOTALL,
    )

    path.write_text(text, encoding="utf-8")
    return "patched"


def main():
    ok = skip = err = 0
    for path in sorted(AI_DIR.glob("*.html")):
        try:
            result = patch_one(path)
            if result == "patched":
                ok += 1
                print(path.name)
            elif result == "skip":
                skip += 1
            else:
                err += 1
        except Exception as e:
            err += 1
            print(path.name, "ERROR", e)
    print(f"Patched: {ok}, skipped: {skip}, other/error: {err}")


if __name__ == "__main__":
    main()
