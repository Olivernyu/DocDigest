from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..shared_resources import page_data_store
from uuid import uuid4

router = APIRouter()  # Change this line


class PageData(BaseModel):
    text: str


@router.post("/", tags=["savepage"])  # Change the path to "/"
async def save_page(page_data: PageData):
    """
    Saves the page data to in-memory shared resource, under a unique id.
    The unique id is returned in the json object.
    All endpoints that uses page data should set the route as such:
        @router.get("/{page_id}")
        async def some_func(page_id: str):
            page_data = page_data_store.get(page_id)
            ...
    """
    try:
        unique_id = str(uuid4())
        page_data_store[unique_id] = page_data.text
        return {"message": "Page saved successfully!", "id": unique_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
