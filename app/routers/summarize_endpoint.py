from fastapi import APIRouter, HTTPException
from ..shared_resources import page_data_store

router = APIRouter()

@router.get("/{page_id}")
async def summarize_page(page_id: str):
    """
    Current implemention is intended solely to test the shared_resources set up. 
    It does not implement the summarize endpoint.
    """
    page_data = page_data_store.get(page_id)
    if page_data is None:
        raise HTTPException(status_code=404, detail="Page not found")
    # Logic to summarize the page_data
    return {"summary": page_data}