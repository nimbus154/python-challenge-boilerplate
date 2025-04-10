import pytest

from rest_api import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_crud(client):
    res = client.get(f"/items/an-id-that-doesnt-exist")
    assert res.status_code == 404

    res = client.post("/items", json={"description": "stuff"})
    assert res.status_code == 200
    item = res.get_json()
    assert item["description"] == "stuff"
    assert "id" in item

    res = client.get(f"/items/{item["id"]}")
    assert res.status_code == 200
    item2 = res.get_json()
    assert item2 == item

    res = client.get("/items")
    assert res.status_code == 200
    items = res.get_json()
    assert len(items) == 1
    assert items[0] == item

    res = client.put(f"/items/{item["id"]}", json={"description": "aaaaaa"})
    assert res.status_code == 200
    item_updated = res.get_json()
    assert item["description"] != item_updated["description"]

    res = client.delete(f"/items/{item["id"]}")
    assert res.status_code == 200

    res = client.get("/items")
    assert res.status_code == 200
    items = res.get_json()
    assert len(items) == 0
