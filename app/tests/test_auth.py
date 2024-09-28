import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_authentication(client):
    # 認証に関連するテストを実装
    pass
