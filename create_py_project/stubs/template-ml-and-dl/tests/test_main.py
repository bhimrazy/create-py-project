from fastapi.testclient import TestClient
from app import api

client = TestClient(api.app)


def test_read_main():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
