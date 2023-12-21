from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, MagicMock

client = TestClient(app)

def test_semantic_search():
    test_query = "Sample search query"
    test_documents = [
        {"id": "1", "text": "Document about technology"},
        {"id": "2", "text": "Another document about health"},
    ]

    with patch("app.shared_resources.document_data_store", test_documents):

        with patch("app.services.openai.OpenAIService.semantic_search") as mock_search:
            mock_search.return_value = [test_documents[0]]  # Return first document as a result

            response = client.get(f"/search?query={test_query}")

            # Asserts
            mock_search.assert_called_once()
            assert response.status_code == 200
            assert response.json() == [test_documents[0]]
