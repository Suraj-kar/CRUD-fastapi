import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/1", json={"name": "Test Item", "description": "Test Desc"})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "description": "Test Desc"}

def test_read_item():
    # First create
    client.post("/items/2", json={"name": "Test", "description": "Desc"})
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {"name": "Test", "description": "Desc"}

def test_read_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    # Assuming items are there from previous testss

def test_update_item():
    client.post("/items/3", json={"name": "Old", "description": "Old"})
    response = client.put("/items/3", json={"name": "New", "description": "New"})
    assert response.status_code == 200
    assert response.json() == {"name": "New", "description": "New"}

def test_delete_item():
    client.post("/items/4", json={"name": "Del", "description": "Del"})
    response = client.delete("/items/4")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    # Check not found
    response = client.get("/items/4")
    assert response.status_code == 404