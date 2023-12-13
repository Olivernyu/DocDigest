from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()  # Change this line


class PageData(BaseModel):
    text: str


@router.post("/", tags=["savepage"])  # Change the path to "/"
async def save_page(page_data: PageData):
    # TODO: Logic to save the page's to db
    try:
        # save_to_database(page_data.text)
        return {"message": "Page saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
