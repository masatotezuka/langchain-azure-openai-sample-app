## 実行環境

- Python 3.12.6

## 環境構築

1. リポジトリのクローン

```
git clone XXX
```

2. 環境変数の設定

```
cp .env.template .env
```

自前で用意したエンドポイントと API キーを.env に設定する

3. パッケージのインストール

```
poetry install --no-root --only main
```

## 実行

```
poetry run python [path]
# ./src/test_llm/json_mode.py
```
