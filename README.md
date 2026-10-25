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

pre-commit のフックを Git に登録します。登録すると、コミット時に `.pre-commit-config.yaml` のチェック（`poe check`）が自動で実行されます。

```bash
uv run pre-commit install
```

## 実行

```bash
uv run python tests/github_serarch.py
```

```bash
uv run pytest tests/testcase/tests/test_python_org_search.py --headed
```

```bash
uv run pytest tests/ecomtestcase/tests/test_account_registration.py --headed
```

- trace viewer 必ず記録する

```bash
uv run pytest tests/ecomtestcase/tests/test_account_registration.py --tracing on
```

- trace viewer 失敗したとき、記録する

```bash
uv run pytest tests/ecomtestcase/tests/test_account_registration.py --tracing retain-on-failure
```

- trace viewerの結果確認

```bash
uv run playwright show-trace test-results/tests-ecomtestcase-tests-test-account-registration-py-test-register-account-chromium/trace.zip
```

- test結果をhtml出力

```bash
uv run pytest --tracing retain-on-failure --html=test-reports/report.html --self-contained-html
```
