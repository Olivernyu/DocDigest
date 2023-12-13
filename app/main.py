from fastapi import FastAPI
from .routers.save_endpoint import router as save_page_router

app = FastAPI()

app.include_router(save_page_router, prefix="/savepage", tags=["savepage"])


@app.get("/")
def read_root():
    return {"message": "Welcome to DocDigest API!"}
