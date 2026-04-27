from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_habit():
    response = client.post("/habits/", json={"name": "Estudar"})
    assert response.status_code == 200

def test_list_habits():
    response = client.get("/habits/")
    assert response.status_code == 200
