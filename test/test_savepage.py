from fastapi.testclient import TestClient
from app.main import app
from app.shared_resources import page_data_store  

client = TestClient(app)


def test_save_page():
    test_data = {"text": "Sample page data"}

    response = client.post("/savepage", json=test_data)

    assert response.status_code == 200
    assert response.json()["message"] == "Page saved successfully!"

    assert response.json()["id"] in page_data_store
    assert page_data_store[response.json()["id"]] == test_data["text"]

