## Django会議室予約システム
Djangoの勉強として簡単な会議室予約システムを作成した。  
実装機能：予約、予約者確認  

1.HOME画面では会議室ボタンをAからDまで用意し、ボタン押下後、予約者を確認できるページに遷移する。  
2.予約者確認ページでは、誰が何時から何時まで予約しているか確認可能。  
3.また予約者確認ページに、予約ボタンを用意し、ボタンを押下すると予約ページに遷移する。  
4.予約ページでは、名前、開始時間、終了時間を入力する。  
5.予約後、予約確認ページに入力内容がリストで表示される。  


■ファイル構造  
meeting_reservation/           # プロジェクト全体のフォルダ  
├── meeting_reservation/       # プロジェクトの設定ファイル  
│   ├── __init__.py  
│   ├── asgi.py  
│   ├── settings.py            # プロジェクト全体の設定ファイル  
│   ├── urls.py                # プロジェクト全体のURLルーティング  
│   ├── wsgi.py  
├── reservations/              # アプリケーションのフォルダ  
│   ├── migrations/            # マイグレーションファイル（Djangoが自動生成）  
│   ├── __init__.py  
│   ├── admin.py               # 管理画面にモデルを登録する  
│   ├── apps.py  
│   ├── models.py              # データベースのモデル（テーブル定義）  
│   ├── views.py               # ビュー（リクエストを処理し、レスポンスを返す）  
│   ├── urls.py                # アプリケーション内のURLルーティング  
│   ├── forms.py               # フォームの定義（ユーザーからの入力を処理）  
│   ├── templates/             # テンプレート（HTMLファイル）を保存  
│   │   └── reservations/  
│   │       ├── room_selection.html        # 会議室選択ページ  
│   │       ├── room_reservation_list.html # 会議室の予約リストページ  
│   │       └── create_reservation.html    # 予約作成ページ  
├── db.sqlite3                 # データベース（SQLiteの場合）  
├── manage.py                  # Djangoプロジェクトを管理するスクリプト  
