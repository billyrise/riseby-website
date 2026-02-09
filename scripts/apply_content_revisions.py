#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RISEby 全ページ改稿スクリプト
- NG表現・英語見出しの一括置換
- AIガバナンスブログの冒頭テンプレ置換
"""
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'en', 'node_modules', '.git', '__pycache__'}

def should_skip(path: Path) -> bool:
    return any(s in path.parts for s in SKIP_DIRS)

def collect_html(base: Path):
    for f in base.rglob('*.html'):
        if not should_skip(f) and f.is_file():
            yield f

# 置換ペア (before, after) - 順序注意（長いもの優先）
REPLACEMENTS = [
    # フッター・共通
    (
        '企業の複合的な経営課題を、AI・戦略・テクノロジー・人の観点から包括的に解決するコンサルティングファーム。',
        '複合的な経営課題を、AI・戦略・テクノロジー・人の観点から整理し、実行に落とすコンサルティングファーム。'
    ),
    ('>Services</h3>', '>サービス</h3>'),
    ('>Company</h3>', '>会社</h3>'),
    # Key Point デフォルト表記
    ('{title || "Key Point"}', '{title || "要点"}'),
    # 本文・CTA
    (
        'ポリシーとプロセスを分けて設計し、プロセスでは申請・承認・記録・例外管理を一気通貫で回せるようにします。ツールで自動化できる部分と、人の判断が必要な部分を切り分け、証跡が残る設計にします。',
        'ポリシーと手続きを分け、申請・承認・記録・例外管理を一つの流れで扱えるよう設計します。自動化する部分と人の判断が必要な部分を切り分け、証跡が残る形にします。'
    ),
    (
        '利用規程、評価・透明性の設計から監査証跡まで、一気通貫でサポートします。',
        '利用規程の設計から評価・透明性・監査証跡まで、範囲を決めたうえで支援します。'
    ),
    # index.html / FAQ 等
    ('戦略立案から実装・定着を一気通貫で支援します', '戦略立案から実装・定着まで、範囲と役割を決めたうえで支援します'),
    ('戦略立案から実装・定着まで一気通貫で支援。', '戦略立案から実装・定着まで、範囲を決めたうえで支援。'),
    ('一気通貫のコンサルティングサービス', '戦略から実装まで一つの流れで扱えるコンサルティング'),
    ('実行まで責任を持って伴走します', '実行まで責任範囲を決めて支援します'),
    ('生成AI導入を包括的に支援しています', '生成AI導入を、利用範囲と統制の設計から支援しています'),
    # 英語見出し（日本語ページ）
    ('Contact Us', 'お問い合わせ'),
    ('Market Insight', '市場の示唆'),
    ('Trusted By Leading Companies', '導入実績'),
    ('Service Not Found', 'サービスが見つかりません'),
    ('For Executives & Leaders', '経営層・リーダー向け'),
]

# 冒頭リード段落のパターン（AIガバナンスブログ用）
LEAD_OLD_PATTERN = re.compile(
    r'([^。]+?)は、企業のAIガバナンスにおいて経営・法務・監査が意思決定するうえで重要なテーマです。'
    r'規制・フレームワークの動向をふまえ、実装と証跡の両面で使える形に整理します。'
    r'本稿では背景、設計のポイント、監査・説明責任への接続まで一通り押さえ、次のアクションに繋げられるようにします。',
    re.DOTALL
)
LEAD_NEW_TEMPLATE = (
    r'\1について、実務に落とすうえで「何を証跡として残し、誰が責任を負うか」を明確にすることが、'
    r'監査と説明責任の前提になる。本稿では背景・設計・監査接続の順に整理する。'
)

def apply_replacements(content: str) -> str:
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    return content

def apply_lead_replacement(content: str) -> str:
    """AIガバナンスブログの冒頭リードを置換"""
    return LEAD_OLD_PATTERN.sub(LEAD_NEW_TEMPLATE, content)

def main():
    count_files = 0
    count_lead = 0
    for f in collect_html(BASE):
        try:
            raw = f.read_text(encoding='utf-8')
            orig = raw
            raw = apply_replacements(raw)
            # blog/ai-governance の記事本文のみリード置換（index.html除く）
            if 'blog/ai-governance' in str(f) and f.name != 'index.html' and 'BlogArticle' in raw:
                raw = apply_lead_replacement(raw)
                if raw != orig:
                    count_lead += 1
            if raw != orig:
                count_files += 1
                f.write_text(raw, encoding='utf-8')
        except Exception as e:
            print(f"Error {f}: {e}")
    print(f"Updated {count_files} files, lead paragraph in {count_lead} ai-governance articles.")

if __name__ == '__main__':
    main()
