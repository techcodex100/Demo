from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .generator import router as generator_router

app = FastAPI(
    title="PDF Generator API",
    description="API for generating PDF invoices",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the generator routes
app.include_router(generator_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to PDF Generator API",
        "endpoints": {
            "generate_pdf": "/generate-pdf",
            "docs": "/docs"
        }
    } 