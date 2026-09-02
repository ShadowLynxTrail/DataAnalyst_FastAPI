
def test_get_summary_requires_auth(client):
    response = client.get("/analytics/summary")
    assert response.status_code == 401