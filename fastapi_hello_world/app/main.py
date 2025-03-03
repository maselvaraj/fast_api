from fastapi import FastAPI
import uvicorn
import logging
from app.routes import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Hello World API", version="1.0.0")

app.include_router(router)

@app.get("/", tags=["Root"])
def read_root():
    logger.info("Root endpoint was accessed")
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
