# services/openai.py

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os


class AnthropicService:
    """
    A Singleton class for Anthropic services. Instance is only initialized on first use.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnthropicService, cls).__new__(cls)
            # Initialize only once
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.client = Anthropic(api_key=self.api_key)

    def summarize_text(self, text, model="claude-2.1"):
        try:
            response = self.client.completions.create(
                model=model,
                max_tokens_to_sample=300,
                prompt=f"{HUMAN_PROMPT} \
                    Summarize the following text: \n\n {text} \
                    {AI_PROMPT}",
            )
            return response.completion
        except Exception as e:
            print(f"Error during summarization: {e}")
            raise

    def semantic_search(self, text, model="claude-2.1"):
        try:
            response = self.client.completions.create(
                model=model,
                max_tokens_to_sample=300,
                prompt=f"{HUMAN_PROMPT} \
                    Search through the text with the query: \n\n {text} \
                    {AI_PROMPT}",
            )
            return response.completion
        except Exception as e:
            print(f"Error during semantic search: {e}")
            raise
