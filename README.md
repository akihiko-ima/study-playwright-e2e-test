# study-e2e-test

Playwright（Python）を使った E2E テストの学習用リポジトリです。

## 必要なもの

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/)

## セットアップ

依存パッケージをインストールします。

```bash
uv sync
```

Playwright で使う Chromium をインストールします。

```bash
uv run playwright install chromium
```

Linux で Chromium の動作に必要なシステムライブラリが足りない場合は、`--with-deps` を付けて一緒にインストールします（sudo 権限が必要です）。

```bash
uv run playwright install --with-deps chromium
```

## 実行

```bash
uv run python tests/github_serarch.py
```
