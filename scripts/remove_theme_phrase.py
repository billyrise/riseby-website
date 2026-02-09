#!/usr/bin/env python3
"""全記事の2〜4章から「ここでは〜について、このテーマに応じた観点を整理します。」を削除する。"""
import re
from pathlib import Path

# 削除するパターン（句点まで含む。直後のスペース・全角スペースも削除）
PATTERN = re.compile(
    r"ここでは[^。]+?について、このテーマに応じた観点を整理します。[ \u3000]*"
)

def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new_text, n = PATTERN.subn("", text)
    if n == 0:
        return False
    path.write_text(new_text, encoding="utf-8")
    print(f"{path}: {n} 件削除")
    return True

def main():
    base = Path(__file__).resolve().parent.parent
    html_dir = base / "blog" / "ai-governance"
    briefs_dir = base / "docs" / "ai-governance-briefs"

    count = 0
    for path in html_dir.glob("*.html"):
        if process_file(path):
            count += 1
    for path in briefs_dir.glob("*-llm-out.md"):
        if process_file(path):
            count += 1
    print(f"\n合計 {count} ファイルを更新しました。")

if __name__ == "__main__":
    main()
