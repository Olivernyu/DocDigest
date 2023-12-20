from fastapi import APIRouter, HTTPException
from openai import OpenAI

# import os

from ..shared_resources import page_data_store

router = APIRouter()
# api_key = os.getenv("OPENAI_API_KEY")
api_key = "Sample api key"
client = OpenAI(api_key=api_key)


def summarize_text(text):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Summarize the following text: \n\n" + text,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error during summarization: {e}")
        raise


@router.get("/{page_id}")
async def summarize_page(page_id: str):
    """
    Summarize the page by providing the page_id
    """
    try:
        page_data = page_data_store.get(page_id)
        if page_data is None:
            raise HTTPException(status_code=404, detail="Page not found")
        # Logic to summarize the page_data
        text_from_html = page_data.get("text_from_html")
        if text_from_html is None:
            raise Exception("Text from html is not in page_data.")
        summary = summarize_text(text_from_html)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
