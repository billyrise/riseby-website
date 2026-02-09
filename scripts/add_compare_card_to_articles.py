#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AIガバナンス記事に CompareCard コンポーネントを追加（未追加のファイルのみ）。"""
from pathlib import Path

BLOG_DIR = Path(__file__).resolve().parent.parent / "blog" / "ai-governance"

COMPARE_CARD_BLOCK = r'''        const CompareCard = ({ caption, leftTitle, leftItems, rightTitle, rightItems }) => (
            <figure className="my-8 not-prose">
                <figcaption className="font-bold text-slate-700 mb-3 text-base">{caption}</figcaption>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="bg-slate-50 border border-slate-200 rounded-lg p-4">
                        <h6 className="font-bold text-slate-800 mb-2 text-base">{leftTitle}</h6>
                        <ul className="list-disc pl-5 space-y-1 text-base text-slate-700">{(leftItems || '').split('\\n').filter(Boolean).map((item, i) => <li key={i}>{item}</li>)}</ul>
                    </div>
                    <div className="bg-slate-50 border border-slate-200 rounded-lg p-4">
                        <h6 className="font-bold text-slate-800 mb-2 text-base">{rightTitle}</h6>
                        <ul className="list-disc pl-5 space-y-1 text-base text-slate-700">{(rightItems || '').split('\\n').filter(Boolean).map((item, i) => <li key={i}>{item}</li>)}</ul>
                    </div>
                </div>
            </figure>
        );
        '''

# KeyPoint の直後で const mermaidChart の直前（KeyPoint の {children}</div> で一意化）
OLD = """                <div className="text-slate-700 text-base leading-relaxed">{children}</div>
            </div>
        );
        const mermaidChart = `"""

NEW = """                <div className="text-slate-700 text-base leading-relaxed">{children}</div>
            </div>
        );
""" + COMPARE_CARD_BLOCK + """        const mermaidChart = `"""


def main():
    count = 0
    for path in sorted(BLOG_DIR.glob("*.html")):
        if path.name == "index.html":
            continue
        text = path.read_text(encoding="utf-8")
        if "const CompareCard" in text:
            continue
        if OLD not in text:
            print(f"Pattern not found: {path.name}")
            continue
        text = text.replace(OLD, NEW, 1)
        path.write_text(text, encoding="utf-8")
        count += 1
    print(f"Added CompareCard to {count} files.")


if __name__ == "__main__":
    main()
