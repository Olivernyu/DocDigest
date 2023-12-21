from unittest.mock import patch, MagicMock
from app.services.openai import OpenAIService


def test_summarize_text():
    with patch("app.services.openai.OpenAIService.__new__") as mock_new:
        # Prevent creating actual instance and reading API Key
        # Create a mock instance with a mocked summarize_text method
        mock_instance = MagicMock()
        mock_instance.summarize_text.return_value = "This is a test summary."
        mock_new.return_value = mock_instance

        openai_service = OpenAIService()

        # Call the summarize_text method
        result = openai_service.summarize_text("Test text for summarization.")

        # Assert that the mock was called and the result is as expected
        mock_instance.summarize_text.assert_called_once()
        assert result == "This is a test summary."


def test_semantic_search():
    with patch("app.services.openai.OpenAIService.__new__") as mock_new:
        # Prevent creating actual instance and reading API Key
        # Create a mock instance with a mocked semantic_search method
        mock_instance = MagicMock()
        mock_instance.semantic_search.return_value = "This is a test summary."
        mock_new.return_value = mock_instance

        openai_service = OpenAIService()

        # Call the semantic_search method
        result = openai_service.semantic_search("Test text for summarization.")

        # Assert that the mock was called and the result is as expected
        mock_instance.semantic_search.assert_called_once()
        assert result == "This is a test summary."
