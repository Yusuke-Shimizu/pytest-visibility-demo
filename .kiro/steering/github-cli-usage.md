# GitHub CLI (gh) コマンドの使い方

## 基本ルール

GitHub CLIコマンドを実行する際は、インタラクティブモードを回避するために必ず `| cat` をパイプで追加する。

## よく使うコマンド

### ワークフロー実行一覧の確認
```bash
gh run list --limit 5 | cat
```

### 特定のワークフロー実行の詳細ログ確認
```bash
gh run view [RUN_ID] --log | cat
```

### 最新の実行状況確認
```bash
gh run list --limit 1 --json status,conclusion,url,createdAt,headSha | cat
```

## 注意点

- `gh` コマンドは通常インタラクティブモードで動作するため、自動化やスクリプトでは `| cat` を必ず追加する
- ログが長い場合は適切に処理する
- 認証が必要な場合は事前に `gh auth login` を実行しておく

## 認証

初回使用時は以下で認証：
```bash
gh auth login --web
```