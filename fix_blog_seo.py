#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ブログページのSEO修正スクリプト
- 各ブログ記事にCanonical URLを追加
- OGPタグを追加
"""

import os
import re
from datetime import datetime

BASE_URL = "https://riseby.net"
BLOG_DIR = "blog"

def extract_title_and_description(html):
    """HTMLからタイトルとdescriptionを抽出"""
    title_match = re.search(r'<title>([^<]+)</title>', html)
    title = title_match.group(1) if title_match else "RISEby Blog"
    
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', html)
    description = desc_match.group(1) if desc_match else ""
    
    return title, description


def fix_blog_html(filepath):
    """ブログHTMLのSEOを修正"""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 相対パスからURLを計算
    relative_path = filepath.replace('\\', '/')
    canonical_url = f"{BASE_URL}/{relative_path}"
    
    # タイトルとdescriptionを抽出
    title, description = extract_title_and_description(html)
    
    # 既にcanonicalがあるかチェック
    if 'rel="canonical"' in html:
        # 既存のcanonicalを正しいURLに置換
        html = re.sub(
            r'<link rel="canonical" href="[^"]*">',
            f'<link rel="canonical" href="{canonical_url}">',
            html
        )
    else:
        # canonicalを追加
        canonical_tag = f'\n    <link rel="canonical" href="{canonical_url}">'
        html = html.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0">{canonical_tag}'
        )
    
    # OGPタグがあるかチェック
    if 'og:url' in html:
        # 既存のog:urlを正しいURLに置換
        html = re.sub(
            r'<meta property="og:url" content="[^"]*">',
            f'<meta property="og:url" content="{canonical_url}">',
            html
        )
    else:
        # OGPタグを追加
        ogp_tags = f'''
    <!-- OGP -->
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="RISEby inc.">
    <meta property="og:locale" content="ja_JP">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description[:200] if len(description) > 200 else description}">
    <meta property="og:image" content="{BASE_URL}/assets/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">'''
        
        # <title>の前にOGPを挿入
        html = html.replace(
            f'<title>{title}</title>',
            f'{ogp_tags}\n    <title>{title}</title>'
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return canonical_url


def main():
    print("=== Fixing Blog SEO ===\n")
    
    count = 0
    for root, dirs, files in os.walk(BLOG_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                url = fix_blog_html(filepath)
                print(f"Fixed: {filepath}")
                print(f"  -> Canonical: {url}")
                count += 1
    
    print(f"\n=== Complete! Fixed {count} blog pages ===")


if __name__ == "__main__":
    main()
