from fastapi.testclient import TestClient

from backend_fastapi.main import app

client = TestClient(app)


def test_signup():

    response = client.post(
        "/signup",
        json={
            "username": "testuser",
            "password": "123456"
        }
    )

    assert response.status_code == 200


def test_login():

    response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data