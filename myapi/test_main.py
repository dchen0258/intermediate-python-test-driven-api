from fastapi.testclient import TestClient
from main import app
from database import DataBase

client = TestClient(app)

db = DataBase()
bird_data = {"name": "Hello", "species": "Passeridae"}
db.put("Hello", bird_data) 
app.db = db

# Test GET /birds endpoint
def test_get_all_birds():
    response = client.get("/birds")
    assert response.status_code == 200
    assert response.json() == {"Hello" : {"name": "Hello", "species": "Passeridae"}}

# Test GET /birds/{name} endpoint
def test_get_bird():
    # Test getting the existing bird
    response = client.get(f"/birds/{"Hello"}")
    assert response.status_code == 200
    assert response.json() == {"name": "Hello", "species": "Passeridae"}

# Test POST /birds endpoint
def test_add_bird():
    # Test adding a new bird
    response = client.post("/birds", json=bird_data)
    assert response.status_code == 200, f"Failed with response: {response.json()}"
    assert response.json()["name"] == bird_data["name"]

# Test DELETE /birds/{name} endpoint
def test_delete_bird():
    # Test deleting the existing bird
    response = client.delete(f"/birds/\"Hello\"")
    assert response.status_code == 200
    assert response.json()["detail"] == "Bird deleted"
