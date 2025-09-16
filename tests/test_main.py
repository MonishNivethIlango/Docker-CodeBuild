
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

def test_hello():
    response = client.get("/hello/World")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_add():
    response = client.post("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_fail():
    response = client.get("/fail")
    assert response.status_code == 400
    assert response.json()["detail"] == "This endpoint always fails."
