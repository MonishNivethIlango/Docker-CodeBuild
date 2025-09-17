import sys
import os
import unittest
from fastapi.testclient import TestClient
from app.main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def test_ping(self):
        response = client.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "pong"})

    def test_hello(self):
        response = client.get("/hello/World")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})

    def test_add(self):
        response = client.post("/add?a=2&b=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5})

    def test_fail(self):
        response = client.get("/fail")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "This endpoint always fails.")

if __name__ == '__main__':
    unittest.main()