from fastapi import FastAPI
from pydantic import BaseModel
from routes.query_routes import router

from services.rag_service import get_rag_response

app = FastAPI()

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