# user_manager.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask import Flask
import config as config

# Flaskアプリの初期化
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ユーザーモデル
class TodoListUser(db.Model):
    __tablename__ = 'todo_list_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# ユーザー登録関数
def register_user(username, password, email):
    if not username or not password:
        raise ValueError('Missing data!')

    # パスワードをハッシュ化
    password_hash = generate_password_hash(password)

    new_user = TodoListUser(username=username, password_hash=password_hash, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully!'}
    except Exception as e:
        db.session.rollback()
        raise Exception(f'Error occurred: {str(e)}')

# テーブルを作成
def create_tables():
    with app.app_context():
        db.create_all()
