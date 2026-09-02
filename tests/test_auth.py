
def test_register(client):
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "name": "Test User",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"