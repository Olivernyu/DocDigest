from openai import OpenAI
from ..prompt_template import apply_prompt_template
import os


class OpenAIService:
    """
    A Singleton class for OpenAI services. Instance is only initialized on first use.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAIService, cls).__new__(cls)
            # Initialize only once
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def summarize_text(self, text, model="gpt-3.5-turbo"):
        """
        Summarizes the given text using the OpenAI chat completions API.

        Args:
            text (str): The input text to be summarized.
            model (str, optional): The model to use for summarization.

        Returns:
            str: The summarized text.
        """
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": apply_prompt_template("summarizer", text),
                    }
                ],
                model=model,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during summarization: {e}")
            raise

    def highlight_text(self, text, model="gpt-3.5-turbo"):
        """
        Highlights the given text using the OpenAI chat completions API.

        Args:
            text (str): The input text to be highlighted.
            model (str, optional): The model to use for highlighting.

        Returns:
            str: The highlighted text.
        """
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": apply_prompt_template("highlighter", text),
                    }
                ],
                model=model,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during highlighting: {e}")
            raise
