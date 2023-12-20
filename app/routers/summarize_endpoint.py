# summarize.py

from fastapi import APIRouter, HTTPException, Query
from app.services import OpenAIService

from ..shared_resources import page_data_store

router = APIRouter()

@router.get("/{page_id}")
async def summarize_page(page_id: str, ai_provider: str = Query("openai", description="AI provider for summarization")):
    """
    Summarize the page by providing the page_id and an optional AI provider
    """
    try:
        page_data = page_data_store.get(page_id)
        if page_data is None:
            raise HTTPException(status_code=404, detail="Page not found")
        text_from_html = page_data.get("text_from_html")
        if text_from_html is None:
            raise Exception("Text from html is not in page_data.")

        if ai_provider == "openai":
            openai_service = OpenAIService()
            summary = openai_service.summarize_text(text_from_html)
        else:
            raise HTTPException(status_code=400, detail="Unsupported AI provider")

        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))