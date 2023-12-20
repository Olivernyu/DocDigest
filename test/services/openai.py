import pytest
from unittest.mock import patch, MagicMock
from app.services import OpenAIService

# Sample mock response for the OpenAI API
mock_response = {
    "choices": [
        {
            "message": {
                "content": "This is a test summary."
            }
        }
    ]
}

@pytest.fixture
def openai_service():
    # Create an instance of the OpenAIService
    return OpenAIService()

def test_summarize_text(openai_service):
    # Mocking the OpenAI API call
    with patch('services.openai.OpenAI.chat.completions.create') as mock_create:
        mock_create.return_value = MagicMock(**mock_response)

        # Call the summarize_text method
        result = openai_service.summarize_text("Test text for summarization.")

        # Assert that the mock was called and the result is as expected
        mock_create.assert_called_once()
        assert result == "This is a test summary."
