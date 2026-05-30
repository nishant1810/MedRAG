from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend_fastapi.logger import logger
from backend_fastapi.routes.query_routes import router
from backend_fastapi.auth.auth_routes import router as auth_router
from backend_fastapi.routes.health_routes import router as health_router
from backend_fastapi.exception_handler import (
    global_exception_handler,
    http_exception_handler
)

app = FastAPI()

# Exception Handlers
app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Route
@app.get("/")
def home():

    logger.info("Home route accessed")

    return {
        "message": "MedRAG FastAPI Backend Running"
    }

# Query Routes
app.include_router(router)

# Auth Routes
app.include_router(auth_router)

# Health Routes
app.include_router(health_router)