from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_summarize():
    test_data = {"text": "Sample page data", "url": "https://engineering.nyu.edu/"}

    response = client.post("/savepage", json=test_data)

    summary_response = client.get(f"/summarize/{response.json()['id']}")

    assert summary_response.status_code == 200
    assert "text" in summary_response.json()["summary"]
    assert "html_content" in summary_response.json()["summary"]
