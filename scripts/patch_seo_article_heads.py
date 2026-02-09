#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
既存の AIガバナンス記事 HTML の <head> に SEO 強化タグを一括で追加・更新する。
- meta robots (index, follow)
- Twitter: twitter:title, twitter:description, twitter:image
- Schema.org BlogPosting 強化 (dateModified, publisher, image, description, mainEntityOfPage, articleSection)
- BreadcrumbList の追加
"""
import html as html_module
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "blog" / "ai-governance"


def esc_json(s):
    if not s or not isinstance(s, str):
        return ""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")


def patch_one(path):
    text = path.read_text(encoding="utf-8")
    # 既に robots と twitter:title があればスキップ（既にパッチ済み）
    if 'name="robots"' in text and 'name="twitter:title"' in text:
        return "skip"
    # canonical から URL と slug を取得
    m_canonical = re.search(r'<link rel="canonical" href="(https://[^"]+)"', text)
    if not m_canonical:
        return "no_canonical"
    canonical_url = m_canonical.group(1)
    slug = path.stem
    # og:title からタイトル取得（ | RISEby Blog を除去）
    m_og_title = re.search(r'<meta property="og:title" content="([^"]+)"', text)
    title_attr = m_og_title.group(1) if m_og_title else path.stem
    title_ja = title_attr.replace(" | RISEby Blog", "").strip() if title_attr else slug
    # meta description から取得（HTML属性のため &quot; 等が入っている可能性）
    m_desc = re.search(r'<meta name="description" content="([^"]*)"', text)
    description_attr = m_desc.group(1) if m_desc else ""
    description_for_json = html_module.unescape(description_attr) if description_attr else ""
    description_json = esc_json(description_for_json)
    title_ja_json = esc_json(title_ja)
    # 挿入する robots
    robots_meta = '\n    <meta name="robots" content="index, follow">'
    # 挿入する Twitter 用 meta（twitter:card の直後）
    # og:title が既に "タイトル | RISEby Blog" なのでそのまま使用
    twitter_metas = f'''
    <meta name="twitter:title" content="{title_attr}">
    <meta name="twitter:description" content="{description_attr}">
    <meta name="twitter:image" content="https://riseby.net/assets/images/og-image.jpg">'''
    # 強化した BlogPosting + BreadcrumbList
    blog_posting_ld = (
        '{"@context":"https://schema.org","@type":"BlogPosting",'
        f'"headline":"{title_ja_json}","description":"{description_json}",'
        '"datePublished":"2026-02-09","dateModified":"2026-02-09",'
        '"author":{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net"},'
        '"publisher":{"@type":"Organization","name":"RISEby Inc.","url":"https://riseby.net","logo":{"@type":"ImageObject","url":"https://riseby.net/assets/images/logo.svg"}},'
        '"image":"https://riseby.net/assets/images/og-image.jpg",'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical_url}"}},'
        '"articleSection":"AIガバナンス",'
        f'"url":"{canonical_url}"}}'
    )
    breadcrumb_ld = (
        '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        '{"@type":"ListItem","position":1,"name":"ホーム","item":"https://riseby.net/"},'
        '{"@type":"ListItem","position":2,"name":"ブログ","item":"https://riseby.net/blog/"},'
        '{"@type":"ListItem","position":3,"name":"AIガバナンス","item":"https://riseby.net/blog/ai-governance/index.html"},'
        f'{{"@type":"ListItem","position":4,"name":"{title_ja_json}","item":"{canonical_url}"}}]}}'
    )
    new_ld_scripts = f'    <script type="application/ld+json">{blog_posting_ld}</script>\n    <script type="application/ld+json">{breadcrumb_ld}</script>'

    # 1) canonical の直後に robots を挿入（まだ無い場合）
    if 'name="robots"' not in text:
        text = re.sub(
            r'(<link rel="canonical" href="[^"]+"\s*>)',
            r'\1' + robots_meta,
            text,
            count=1,
        )
    # 2) twitter:card の直後に twitter:title, twitter:description, twitter:image を挿入
    if 'name="twitter:title"' not in text:
        text = re.sub(
            r'(<meta name="twitter:card" content="summary_large_image">)',
            r'\1' + twitter_metas,
            text,
            count=1,
        )
    # 3) 既存の BlogPosting 単体の ld+json を 強化版 + BreadcrumbList に置換
    text = re.sub(
        r'<script type="application/ld\+json">[^<]*BlogPosting[^<]*</script>',
        new_ld_scripts,
        text,
        count=1,
    )
    path.write_text(text, encoding="utf-8")
    return "patched"


def main():
    patched = skipped = no_canonical = 0
    for path in sorted(OUT_DIR.glob("*.html")):
        if path.name == "index.html":
            continue
        result = patch_one(path)
        if result == "patched":
            patched += 1
            print(path.name)
        elif result == "skip":
            skipped += 1
        else:
            no_canonical += 1
    print(f"Patched: {patched}, skipped (already had): {skipped}, no_canonical: {no_canonical}")


if __name__ == "__main__":
    main()
