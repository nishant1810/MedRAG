from fastapi import APIRouter
from fastapi import Depends
from backend_fastapi.logger import logger
from backend_fastapi.auth.auth_bearer import JWTBearer
from backend_fastapi.schemas.query_schema import QueryRequest
from backend_fastapi.services.rag_service import get_rag_response

router = APIRouter()

@router.post(
    "/query",
    dependencies=[Depends(JWTBearer())]
)
async def query_rag(req: QueryRequest):

    # Log incoming query
    logger.info(f"Query received: {req.question}")

    response = get_rag_response(req.question)

    # Log successful response
    logger.info("Response generated successfully")

    return {
        "answer": response
    }