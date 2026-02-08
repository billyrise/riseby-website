#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
サイト全体の sitemap.xml を生成するスクリプト。
全言語（ja/en）・全HTMLを走査し、lastmod はファイルの更新日時を使用。
"""
import os
from datetime import datetime

BASE_URL = "https://riseby.net"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 除外するパス（404、リダイレクト専用など）
EXCLUDE = {
    "404.html",
    "en/404.html",
    "en/services/index.html",  # リダイレクトのみ
}


def priority_and_freq(rel_path):
    """URLの種別に応じて priority と changefreq を返す"""
    if rel_path in ("index.html", ""):
        return "1.0", "weekly"
    if rel_path == "en/index.html":
        return "0.95", "weekly"
    if rel_path in ("about.html", "privacy.html"):
        return "0.8", "monthly"
    if rel_path in ("en/about.html", "en/privacy.html"):
        return "0.8", "monthly"
    if rel_path == "services/" or rel_path == "services/index.html":
        return "0.9", "weekly"
    if rel_path.startswith("services/") and rel_path.endswith(".html"):
        return "0.85", "monthly"
    if rel_path.startswith("en/services/") and rel_path.endswith(".html"):
        return "0.85", "monthly"
    if rel_path in ("blog/", "blog/index.html"):
        return "0.9", "daily"
    if rel_path in ("blog/ai/", "blog/ai/index.html"):
        return "0.85", "weekly"
    if rel_path in ("blog/ai-governance/", "blog/ai-governance/index.html"):
        return "0.85", "weekly"
    if rel_path.startswith("blog/") and rel_path.endswith(".html"):
        return "0.7", "monthly"
    return "0.5", "monthly"


def collect_urls():
    urls = []
    for root_dir, dirs, files in os.walk(ROOT):
        # scripts, .github, docs, node_modules 等はスキップ
        rel_root = os.path.relpath(root_dir, ROOT)
        if rel_root.startswith((".git", "scripts", "docs", "node_modules", ".github")):
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            path = os.path.join(root_dir, f)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            if rel in EXCLUDE:
                continue
            # URL: ディレクトリの index.html は / で終わるパスにする
            if f == "index.html":
                seg = rel[:-11].rstrip("/")  # remove "/index.html" (11 chars)
                loc = f"{BASE_URL}/{seg}/" if seg else f"{BASE_URL}/"
            else:
                loc = f"{BASE_URL}/{rel}"
            try:
                mtime = os.path.getmtime(path)
                lastmod = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
            except OSError:
                lastmod = datetime.now().strftime("%Y-%m-%d")
            priority, changefreq = priority_and_freq(rel)
            urls.append({
                "loc": loc,
                "lastmod": lastmod,
                "changefreq": changefreq,
                "priority": priority,
            })
    return urls


def main():
    os.chdir(ROOT)
    urls = collect_urls()
    urls.sort(key=lambda u: (u["loc"].count("/"), u["loc"]))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{u['loc']}</loc>")
        lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        lines.append(f"    <priority>{u['priority']}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Generated {sitemap_path} with {len(urls)} URLs.")


if __name__ == "__main__":
    main()
