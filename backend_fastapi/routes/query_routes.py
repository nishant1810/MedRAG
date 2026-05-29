from fastapi import APIRouter

from backend_fastapi.schemas.query_schema import QueryRequest
from backend_fastapi.services.rag_service import get_rag_response

router = APIRouter()

@router.post("/query")
async def query_rag(req: QueryRequest):

    response = get_rag_response(req.question)

    return {
        "answer": response
    }