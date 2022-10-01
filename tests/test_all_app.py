from fastapi.testclient import TestClient

from main import app

test_client = TestClient(app)


def test_root():
    response = test_client.get("/", params="token=my-token")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}


def test_read_users():
    response = test_client.get("/users/", params="token=my-token")
    assert response.status_code == 200
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]


def test_read_user_me():
    response = test_client.get("/users/me", params="token=my-token")
    assert response.status_code == 200
    assert response.json() == {"username": "fakecurrentuser"}


def test_read_user():
    user_name = "fake_user_name"
    response = test_client.get(f"/users/{user_name}", params="token=my-token")
    assert response.status_code == 200
    assert response.json() == {"username": user_name}


def test_read_items():
    response = test_client.get("/items/", params="token=my-token", headers={"x-token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


def test_read_item():
    response = test_client.get("/items/plumbus", params="token=my-token", headers={"x-token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"item_id": "plumbus", "name": "Plumbus"}


def test_update_item():
    response = test_client.put("/items/plumbus", params="token=my-token", headers={"x-token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"item_id": "plumbus", "name": "The great Plumbus"}

