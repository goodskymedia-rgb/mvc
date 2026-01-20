from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_weather():
    new_id = client.post("/weather", json={"location": "UA", "temperature": 25}).json()
    response = client.get(f"/weather?id={new_id}")
    assert response.status_code == 200
    assert response.json() == { "location": "UA", "temperature": 25 }


def test_get_weather():
    new_id = client.post("/weather", json={"location": "UA", "temperature": 25}).json()
    response = client.get(f"/weather?id={new_id}")
    assert response.status_code == 200
    assert response.json() == {
        "location": "UA",
        "temperature": 25
    }

def test_update_weather():
    new_id = client.post("/weather", json={"location": "UA", "temperature": 25}).json()
    response = client.put(f"/weather/{new_id}", json={"location": "UAE", "temperature": 26})
    assert response.status_code == 200
    assert {"status": f"item with an id of {new_id} was updated"}

def test_delete_weather():
    new_id = client.post("/weather", json={"location": "UA", "temperature": 25}).json()
    response = client.delete(f"/weather/{new_id}")
    assert response.status_code == 200
    assert response.json() == {"status": f"item with an id of {new_id} was deleted"}