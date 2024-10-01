# main.py
from user_manager import register_user, create_tables

# テーブル作成（最初に一度だけ実行）
create_tables()

# ユーザー登録
try:
    response = register_user('example_user', 'secure_password', 'user@example.com')
    print(response)
except Exception as e:
    print(f'Error: {e}')
