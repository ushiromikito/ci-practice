from pathlib import Path

from calc import add, tax_included


def main() -> None:
    out = Path("dist")
    out.mkdir(exist_ok=True)
    html = f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><title>ci-practice</title></head>
<body>
<h1>CI/CD 練習ページ</h1>
<p>2 + 3 = {add(2, 3)}</p>
<p>1000円の税込み価格: {tax_included(1000)}円</p>
</body></html>
"""
    (out / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
