from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..shared_resources import page_data_store
from uuid import uuid4
import requests

router = APIRouter()  # Change this line


class PageData(BaseModel):
    text: str
    url: str


def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()


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
    text = page_data.text
    url = page_data.url
    html_content = fetch_html(url)
    try:
        unique_id = str(uuid4())
        page_data_store[unique_id] = {"text": text, "html_content": html_content}
        return {"message": "Page saved successfully!", "id": unique_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
