from fastapi import FastAPI
from .routers.save_endpoint import router as save_page_router
from .routers.search_endpoint import semantic_search as search_router
from .routers.summarize_endpoint import router as summarize_router

app = FastAPI()

app.include_router(save_page_router, prefix="/savepage", tags=["savepage"])

app.include_router(summarize_router, prefix="/summarize")
app.include_router(search_router, prefix="/search")


@app.get("/")
def read_root():
    return {"message": "Welcome to DocDigest API!"}
