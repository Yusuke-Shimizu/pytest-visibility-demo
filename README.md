# pytest GitHub Actions 見やすさ改善プロジェクト

このプロジェクトは、GitHub Actions で pytest の実行結果を見やすくするための設定例です。

## 🎯 実装済みの改善点

### 1. ⭐️⭐️⭐️⭐️⭐️ pytest-github-actions-annotate-failures
- PR上でテスト失敗箇所が赤字ハイライト表示
- 最も効果的な改善方法

### 2. ★★★★☆ カラー出力 + 簡潔なトレースバック
- `--color=yes --tb=short` でログが見やすく
- ANSI カラーコードがGHAでサポート

### 3. ★★★★☆ JUnit XML レポート
- テスト結果をXML形式で出力
- アーティファクトとして保存・共有可能

### 4. ★★★☆☆ カバレッジレポート
- `pytest-cov` でコードカバレッジを測定
- HTML/XML形式でレポート生成

### 5. ★★★☆☆ Slack通知（オプション）
- テスト失敗時にSlackへ自動通知
- `SLACK_WEBHOOK` シークレットの設定が必要

## 🚀 使い方

### ローカルでのテスト実行
```bash
# 依存関係のインストール
pip install -r requirements-dev.txt

# 基本的なテスト実行
pytest

# カバレッジ付きテスト実行
pytest --cov=. --cov-report=html

# 遅いテストを除外
pytest -m "not slow"
```

### GitHub Actions での自動実行
- Push/PR時に自動実行
- Python 3.9, 3.10, 3.11 でマトリックステスト
- 失敗時はPR上にアノテーション表示

## 📁 ファイル構成

```
.
├── .github/workflows/test.yml    # GitHub Actions ワークフロー
├── tests/test_sample.py          # サンプルテストファイル
├── pytest.ini                   # pytest 設定
├── requirements-dev.txt          # 開発用依存関係
└── README.md                     # このファイル
```

## 🔧 Slack通知の設定（オプション）

1. Slack Webhook URLを取得
2. GitHub リポジトリの Settings > Secrets で `SLACK_WEBHOOK` を設定
3. ワークフローが自動的にSlack通知を送信

## 📊 レポートの確認方法

### GitHub Actions
1. Actions タブでワークフロー実行結果を確認
2. Artifacts からレポートファイルをダウンロード

### ローカル
- `htmlcov/index.html` でカバレッジレポートを確認
- `pytest-report.xml` でJUnitレポートを確認

## 🎨 カスタマイズ

`pytest.ini` でさらに詳細な設定が可能：
- テストマーカーの追加
- カバレッジ除外パターン
- 出力フォーマットの調整