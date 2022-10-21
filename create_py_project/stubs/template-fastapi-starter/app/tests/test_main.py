from app import main
from fastapi.testclient import TestClient

client = TestClient(main.app)


def test_read_main():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
