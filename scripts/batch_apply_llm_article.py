#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
記事11〜163の llm-out を順に apply_llm_article.py に渡し、HTML と figure_usage_history を更新する。
"""
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BRIEFS_DIR = BASE_DIR / "docs" / "ai-governance-briefs"
APPLY_SCRIPT = BASE_DIR / "scripts" / "apply_llm_article.py"

sys.path.insert(0, str(BASE_DIR / "scripts"))
from gen_llm_out_31_163 import parse_design


def main():
    articles = parse_design()
    target = [a for a in articles if 11 <= a["no"] <= 163]
    target.sort(key=lambda a: a["no"])
    applied = 0
    skipped = 0
    for a in target:
        no = a["no"]
        slug = a["slug"]
        path = BRIEFS_DIR / f"{no:03d}-{slug}-llm-out.md"
        if not path.exists():
            print(f"Skip {no}: {path.name} not found", file=sys.stderr)
            skipped += 1
            continue
        try:
            subprocess.run(
                [sys.executable, str(APPLY_SCRIPT), str(no), str(path)],
                cwd=BASE_DIR,
                check=True,
            )
            applied += 1
        except subprocess.CalledProcessError as e:
            print(f"Failed no={no}: {e}", file=sys.stderr)
            raise
    print(f"Applied {applied} articles (11-163), skipped {skipped}.")


if __name__ == "__main__":
    main()
