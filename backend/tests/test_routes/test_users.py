import json


def test_create_user(client):
    data = {"username": "John Snox",
            "email": "john@snox.com", "password": "123456"}
    response = client.post("users/add-user", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["is_active"] == True
    assert response.json()["email"] == "john@snox.com"
