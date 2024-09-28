import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, World!'
