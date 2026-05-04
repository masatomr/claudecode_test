# 近くの図書館を探す

[CALIL 図書館 API](https://calil.jp/doc/api_ref.html) を使って、現在地または地域から近くの図書館を検索する Web サービスです。

## 機能

- **現在地から検索** — ブラウザの位置情報 API で自動取得した座標を元に近くの図書館を一覧表示
- **地域から検索** — 都道府県・市区町村名で図書館を絞り込み
- 図書館名・住所・電話番号・カテゴリを表示
- 各図書館のウェブサイトリンク・Google マップへのリンク

## セットアップ

```bash
cd library-search
pip install -r requirements.txt
```

## 起動

```bash
python app.py
```

ブラウザで `http://localhost:5000` を開いてください。

## 環境変数

| 変数名 | 説明 | デフォルト |
|--------|------|-----------|
| `CALIL_API_KEY` | CALIL API キー | コード内の値 |

## 使用 API

- [CALIL 図書館 API](https://calil.jp/doc/api_ref.html) — `https://api.calil.jp/library`
