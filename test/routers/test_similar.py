from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def find_similar_pages():
    # Example data
    query_param = "Sample query"

    # Mock embeddings for the query and documents
    mock_query_embedding = [1, 0, 0]  # Example embedding
    mock_doc_embedding = [0.8, 0.2, 0]  # Another example embedding

    with patch("app.routers.find_similar_pages.encode") as mock_encode:
        # Setting up the side effect for the mocked encode function
        mock_encode.side_effect = [
            mock_query_embedding,
            mock_doc_embedding,
            mock_doc_embedding,
        ]

        # Making a POST request to the find_similar_pages endpoint
        response = client.post(f"/find_similar_pages?query={query_param}")

        # Asserts
        if response.status_code == 422:
            print(response.json())

        # Asserts
        assert response.status_code == 200
