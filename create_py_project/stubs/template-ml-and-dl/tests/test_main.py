from app import api
from fastapi.testclient import TestClient

client = TestClient(api.app)


def test_read_main():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
