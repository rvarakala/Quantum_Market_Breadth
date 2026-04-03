"""
Main FastAPI application for Quantum Market Breadth
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from .api.main_api import api_router
from .database.connection import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_database()
    print("🚀 Quantum Market Breadth started successfully")
    yield
    # Shutdown
    print("🛑 Quantum Market Breadth shutting down")


app = FastAPI(
    title="Quantum Market Breadth",
    description="Historical-first market breadth intelligence platform",
    version="0.1.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

# Serve static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
