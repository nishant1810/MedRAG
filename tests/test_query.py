from fastapi.testclient import TestClient
from unittest.mock import patch

from backend_fastapi.main import app

client = TestClient(app)


@patch(
    "backend_fastapi.routes.query_routes.get_rag_response"
)
def test_protected_query(mock_rag):

    # Fake AI response
    mock_rag.return_value = (
        "Diabetes is a chronic condition."
    )

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

    # Query request
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

    assert response.json() == {
        "answer": "Diabetes is a chronic condition."
    }