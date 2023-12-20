# services/openai.py

from openai import OpenAI
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
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "Summarize the following text: \n\n" + text,
                    }
                ],
                model=model,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during summarization: {e}")
            raise