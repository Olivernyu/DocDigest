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


def test_highlight_text():
    with patch("app.services.openai.OpenAIService.__new__") as mock_new:
        # Prevent creating actual instance and reading API Key
        # Create a mock instance with a mocked highlight_text method
        mock_instance = MagicMock()
        mock_instance.highlight_text.return_value = "This is a test highlighted html."
        mock_new.return_value = mock_instance

        openai_service = OpenAIService()

        # Call the highlight_text method
        result = openai_service.highlight_text("Test text for highlighting.")

        # Assert that the mock was called and the result is as expected
        mock_instance.highlight_text.assert_called_once()
        assert result == "This is a test highlighted html."
