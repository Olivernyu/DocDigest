from fastapi import FastAPI
from .routers.save_endpoint import router as save_page_router
from .routers.summarize_endpoint import router as summarize_router
from .routers.highlight_endpoint import router as highlight_router

app = FastAPI()

app.include_router(save_page_router, prefix="/savepage", tags=["savepage"])

app.include_router(summarize_router, prefix="/summarize")
app.include_router(highlight_router, prefix="/highlight")


@app.get("/")
def read_root():
    return {"message": "Welcome to DocDigest API!"}
