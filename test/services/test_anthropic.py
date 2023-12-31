from unittest.mock import patch, MagicMock
from app.services.anthropic import AnthropicService


def test_summarize_text():
    with patch("app.services.anthropic.AnthropicService.__new__") as mock_new:
        # Prevent creating actual instance and reading API Key
        # Create a mock instance with a mocked summarize_text method
        mock_instance = MagicMock()
        mock_instance.summarize_text.return_value = "This is a test summary."
        mock_new.return_value = mock_instance

        anthropic_service = AnthropicService()

        # Call the summarize_text method
        result = anthropic_service.summarize_text("Test text for summarization.")

        # Assert that the mock was called and the result is as expected
        mock_instance.summarize_text.assert_called_once()
        assert result == "This is a test summary."
