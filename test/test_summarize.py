from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_summarize_page():
    # Example data
    test_data = {"text": "Sample page data", "url": "https://engineering.nyu.edu/"}

    response = client.post("/savepage", json=test_data)
    page_id = response.json()["id"]
    mock_summary = "This is a mock summary."

    # Use 'patch' to mock 'summarize_text' function
    with patch(
        "app.routers.summarize_endpoint.summarize_text", return_value=mock_summary
    ) as mock:
        response = client.get(f"/summarize/{page_id}")

        # Verify that the mock was called
        mock.assert_called_once()

        # Assert response status code and data
        assert response.status_code == 200
        assert response.json() == {"summary": mock_summary}
