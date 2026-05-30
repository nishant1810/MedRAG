from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from backend_fastapi.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        f"Unhandled exception occurred: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )


async def http_exception_handler(
    request: Request,
    exc: HTTPException
):

    logger.warning(
        f"HTTP exception: {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail
        }
    )