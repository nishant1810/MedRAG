from fastapi.testclient import TestClient

from backend_fastapi.main import app

client = TestClient(app)


def test_protected_query():

    # Signup
    client.post(
        "/signup",
        json={
            "username": "queryuser",
            "password": "123456"
        }
    )

    # Login
    login_response = client.post(
        "/login",
        json={
            "username": "queryuser",
            "password": "123456"
        }
    )

    token = login_response.json()["access_token"]

    # Protected query request
    response = client.post(
        "/query",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "question": "What is diabetes?"
        }
    )

    assert response.status_code == 200