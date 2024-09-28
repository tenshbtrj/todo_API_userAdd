from flask import Flask
from .routes import register_routes
from .auth import configure_auth

def create_app():
    app = Flask(__name__)
    
    # 設定の読み込み
    app.config.from_pyfile('../config.py')

    # ルーティングの登録
    register_routes(app)

    # 認証の設定
    configure_auth(app)

    return app
