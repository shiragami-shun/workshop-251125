# プロダクトゴール : 受験生や資格取得、就職活動を行っている人たちに使ってもらって、目標を達成してもらう。

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

