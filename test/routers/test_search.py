from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch, MagicMock

client = TestClient(app)


def test_semantic_search():
    # Example data
    test_query = "Sample search query"
    test_documents = [
        {"id": "1", "text": "Document about technology"},
        {"id": "2", "text": "Another document about health"},
    ]

    # Mock response for semantic search
    mock_search_response = test_documents
    # TODO
    # with patch("app.services.openai.OpenAIService.semantic_search", return_value=mock_search_response) as mock_search:
    # response = client.post("/search", json={"query": test_query})

    # Asserts
    # mock_search.assert_called_once()
    # assert response.status_code == 200
    # assert response.json() == mock_search_response
