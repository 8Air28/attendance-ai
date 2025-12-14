# 勤怠管理 × 月次レポート生成アプリ（API 連携ポートフォリオ）

## 概要

本アプリは **業務系システムを想定した勤怠管理 API** と、
**外部 API（AI 想定）と連携した月次レポート生成機能** を組み合わせた
ポートフォリオ用アプリケーションです。

バックエンドは FastAPI、
フロントエンドはシンプルな HTML + JavaScript で構成し、
**「業務システム + API 連携」の理解を重視**して作成しています。

---

## 主な機能

### 1. 勤怠データ管理（業務システム想定）

- 出勤日、開始時刻、終了時刻、備考を登録
- SQLite に保存
- REST API 経由で取得・登録

### 2. 月次レポート生成（API 連携想定）

- 勤怠データを集計
- 月単位で勤務状況を要約
- 本来は外部 AI API を利用する想定
- 現在は **ダミー AI ロジック** により文章を生成

### 3. フロントエンド連携

- HTML + JavaScript から FastAPI を `fetch` で呼び出し
- API レスポンスを画面に表示
- Swagger UI だけでなく「実際に使う画面」を用意

---

## 使用技術

### バックエンド

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

### フロントエンド

- HTML
- JavaScript（fetch API）

---

## ディレクトリ構成

```
attendance_ai/
├─ backend/
│  ├─ main.py            # FastAPI エントリーポイント
│  ├─ models.py          # ORMモデル
│  ├─ schemas.py         # Pydanticスキーマ
│  ├─ database.py        # DB接続設定
│  └─ services/
│     └─ report_service.py  # レポート生成ロジック（ダミーAI）
│
├─ frontend/
│  └─ index.html         # フロントエンド画面
│
└─ README.md
```

---

## API 一覧（抜粋）

### 勤怠一覧取得

```
GET /attendances
```

### 勤怠登録

```
POST /attendances
```

### 月次レポート生成

```
POST /report?month=2025-12
```

---

## 起動方法

### 1. 仮想環境作成・有効化

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. 依存関係インストール

```bash
pip install fastapi uvicorn sqlalchemy
```

### 3. サーバー起動

```bash
python -m uvicorn backend.main:app --reload
```

### 4. 動作確認

- API Docs

  - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- フロントエンド

  - Live Server 等で `frontend/index.html` を起動

---

![勤怠レポート画面](docs/screenshot-report.png)

## 工夫した点・アピールポイント

- **業務システムを意識した API 設計**
- FastAPI の **依存性注入（Depends）** を使用
- クエリパラメータによる月指定処理
- フロントとバックエンドを分離した構成
- エラー（422, 500）の原因切り分けを重視

---

## 今後の拡張予定

- 月指定をフロント画面から入力可能にする
- 実際の外部 AI API への差し替え
- レポート内容の詳細化
- 簡単な UI 改善

---

## 作成目的

本ポートフォリオは、

- API 連携の理解
- バックエンドとフロントエンドの役割分担
- 実務を想定した構成力

を示すことを目的として作成しました。

## システム構成

```
[ ブラウザ (HTML / JavaScript) ]
        |
        | fetch (HTTP)
        v
[ FastAPI (backend/main.py) ]
        |
        | ORM (SQLAlchemy)
        v
[ SQLite Database ]
        |
        | 勤怠データ取得
        v
[ レポート生成サービス ]
  （現在：ダミー実装）
  （将来：外部AI APIに差し替え可能）
```

### 構成のポイント

- フロントエンドはシンプルな HTML + JavaScript で実装
- FastAPI が API サーバーとしてリクエストを受け付ける
- SQLAlchemy を利用して勤怠データを管理
- レポート生成処理は service 層に分離し、
  将来的に外部 API（AI）へ差し替えやすい構成にしている

## 工夫した点

### 1. 業務システムを想定した API 設計

- 勤怠登録（POST /attendances）と一覧取得（GET /attendances）を分離
- 月次レポート生成（POST /report）を独立した API として設計
- フロントエンドから API を呼び出す構成にし、
  実務でよくある「画面 + API」構成を意識した

### 2. レイヤー分離による保守性

- FastAPI のルーティング処理と、
  レポート生成ロジックを service 層に分離
- レポート生成部分は現在ダミー実装だが、
  将来的に外部 AI API へ差し替えやすい構成にしている

### 3. 課金不要で動作確認できる工夫

- 外部 API を使わなくても動作するダミー実装を採用
- 課金や API 制限に依存せず、
  誰でもローカル環境で再現できるようにした

### 4. API 動作が視覚的に確認できる

- FastAPI の Swagger UI（/docs）を活用し、
  API の動作確認ができるようにしている
- フロントエンド画面と API の両方から挙動を確認可能

## 今後の改善案

- 月別・個人別など、条件指定によるレポート生成機能の追加
- 勤怠データの集計ロジックを拡張し、
  残業時間や平均勤務時間などの指標を算出
- 外部 AI API と連携し、
  勤務傾向に対するコメントや改善提案を自動生成
- フロントエンドを React などのフレームワークに置き換え、
  実務に近い構成へ発展させる
- 認証機能を追加し、ユーザーごとに勤怠データを管理可能にする
