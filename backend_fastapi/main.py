from fastapi import FastAPI
from pydantic import BaseModel
from backend_fastapi.routes.query_routes import router
from fastapi.middleware.cors import CORSMiddleware

from backend_fastapi.services.rag_service import get_rag_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Schema
class QueryRequest(BaseModel):
    question: str

# Root Route
@app.get("/")
def home():
    return {
        "message": "MedRAG FastAPI Backend Running"
    }

# Query Route
@app.post("/query")
async def query_rag(req: QueryRequest):

    response = get_rag_response(req.question)

    return {
        "answer": response
    }

app.include_router(router)