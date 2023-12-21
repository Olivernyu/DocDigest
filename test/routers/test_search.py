# from fastapi.testclient import TestClient
# from app.main import app
# from unittest.mock import patch, MagicMock

# client = TestClient(app)

# def test_semantic_search():
#     # Example data
#     test_data = {"text": "Sample page data", "url": "https://engineering.nyu.edu/"}

#     response = client.post("/savepage", json=test_data)
#     page_id = response.json()["id"]
#     mock_summary = "This is a mock summary."

#     with patch("app.services.openai.OpenAIService.__new__") as mock_new:
#         # Prevent creating actual instance and reading API Key
#         # Create a mock instance with a mocked summarize_text method
#         mock_instance = MagicMock()
#         mock_instance.summarize_text.return_value = mock_summary
#         mock_new.return_value = mock_instance

#         response = client.get(f"/summarize/{page_id}")

#         # Asserts
#         mock_new.assert_called_once()
#         mock_instance.summarize_text.assert_called_once()
#         assert response.status_code == 200
#         assert response.json() == {"summary": mock_summary}
