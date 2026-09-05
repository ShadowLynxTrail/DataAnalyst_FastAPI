from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_predict_requires_auth(client):
    response = client.post("/predict/sales", json={
        "date": "2023-01-01",
        "category": "Расходные материалы",
        "region": "Москва",
        "product_name": "Шприцы 5 мл",
        "price": 15.0
    })
    assert response.status_code == 401


def test_predict_with_auth(client):
    email = f"test_{uuid.uuid4().hex}@example.com"
    password = "password"

    response = client.post("/auth/register", json={
        "email": email,
        "name": "Test",
        "password": password
    })
    assert response.status_code == 200, response.text

    response = client.post("/auth/login", json={
        "email": email,
        "password": password
    })
    assert response.status_code == 200, response.text
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/predict/sales", headers=headers, json={
        "date": "2023-01-01",
        "category": "Расходные материалы",
        "region": "Москва",
        "product_name": "Шприцы 5 мл",
        "price": 15.0
    })
    assert response.status_code == 200, response.text
    assert "predicted_quantity" in response.json()


