from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_requires_auth():
    response = client.post("/predict/sales", json={
        "date": "2023-01-01",
        "category": "Расходные материалы",
        "region": "Москва",
        "product_name": "Шприцы 5 мл",
        "price": 15.0
    })
    assert response.status_code == 401


def test_predict_with_auth():
    # Регистрируем пользователя
    client.post("/auth/register", json={
        "email": "test@example.com",
        "name": "Test",
        "password": "password"
    })
    # Логинимся
    login = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "password"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/predict/sales", headers=headers, json={
        "date": "2023-01-01",
        "category": "Расходные материалы",
        "region": "Москва",
        "product_name": "Шприцы 5 мл",
        "price": 15.0
    })
    assert response.status_code == 200
    assert "predicted_quantity" in response.json()