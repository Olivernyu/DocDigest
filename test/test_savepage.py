from fastapi.testclient import TestClient
from app.main import app
from app.shared_resources import page_data_store

client = TestClient(app)


def test_save_page():
    test_data = {"text": "Sample page data", "url": "https://engineering.nyu.edu/"}

    response = client.post("/savepage", json=test_data)
    # Print the response content if the status code is not 200
    if response.status_code != 200:
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
    assert response.status_code == 200
    assert response.json()["message"] == "Page saved successfully!"

    assert response.json()["id"] in page_data_store
    assert "text" in page_data_store[response.json()["id"]]
    assert "text_from_html" in page_data_store[response.json()["id"]]
