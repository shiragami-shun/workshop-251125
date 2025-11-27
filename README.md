# プロダクトゴール : 受験生や資格取得、就職活動を行っている人たちに使ってもらって、目標を達成してもらう。
<<<<<<< dashboard_syake27

## ダッシュボード機能
ダッシュボードには以下の機能が含まれています:


### 実行方法
```bash
# 1. 依存パッケージをインストール
cd GoalManagementApplication
python -m pip install -r requirements.txt

# 2. マイグレーションを作成し、適用
python manage.py makemigrations
python manage.py migrate

# 3. 開発サーバを起動
python manage.py runserver
```

ログイン後、`/dashboard/` にアクセスするとダッシュボードが表示されます。管理サイトやユーザー作成も行えます。

新規アカウント作成:
- サインアップ URL: `/accounts/signup/` — ログインページからもリンクがあります。

=======
# サイトのデザイン
- フォントサイズ 通常が16、h1,h2,h3の大きさは後から決める。
- サイトデザイン ナビを左側に配置して、要素を右側に配置する。
- サイトの背景 要素の背景が白で、ナビの背景が青色。
>>>>>>> main
