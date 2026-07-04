from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.services.file_service import save_file
#from app.services.file_service import UPLOAD_DIR

app = FastAPI(
    title = "Document Intelligence Engine",
    description = "Document Intelligence Engine is a powerful tool for extracting insights from documents using advanced AI models. It provides endpoints for health checks, model information retrieval, and document processing.",
    version = "1.0.0",
)

app.include_router(health_router)
app.include_router(upload_router)


@app.get("/")
def root():
    return {"message": "Welcome to Document Intelligence Engine"}

