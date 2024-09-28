import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # 環境変数からデータベースURLを取得
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # 環境変数からシークレットキーを取得

# Flask設定を適用
