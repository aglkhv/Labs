def test_register_login_and_get_profile(client):
    # Регистрация
    r = client.post("/auth/register", json={"email": "demo@user.com", "password": "123"})
    assert r.status_code == 201

    # Логин
    r = client.post("/auth/login", json={"email": "demo@user.com", "password": "123"})
    assert r.status_code == 200
    token = r.json["token"]
    assert token

    # Обращение к /profile с токеном
    r = client.get("/profile", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json["email"] == "demo@user.com"