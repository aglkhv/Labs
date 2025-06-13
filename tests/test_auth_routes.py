def test_register_and_login(client):
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "pass123"
    })
    assert response.status_code == 201

    response = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "token" in response.json

def test_login_invalid_credentials(client):
    response = client.post("/auth/login", json={
        "email": "nosuchuser@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401