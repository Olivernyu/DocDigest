from fastapi import APIRouter, HTTPException
from transformers import pipeline
from ..shared_resources import page_data_store

router = APIRouter()

summarizer = pipeline("summarization")


def summarize_text(text):
    summary = summarizer(text, max_length=500, min_length=30, do_sample=False)
    return summary[0]["summary_text"]


@router.get("/{page_id}")
async def summarize_page(page_id: str):
    """
    Current implemention is intended solely to test the shared_resources set up.
    It does not implement the summarize endpoint.
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
