from fastapi import APIRouter
import requests

from backend_fastapi.logger import logger

router = APIRouter()


@router.get("/health")
def health_check():

    logger.info("Health check endpoint accessed")

    return {
        "status": "healthy"
    }


@router.get("/health/ollama")
def ollama_health_check():

    try:

        response = requests.get(
            "http://localhost:11434/api/tags"
        )

        if response.status_code == 200:

            logger.info("Ollama health check successful")

            return {
                "ollama": "running"
            }

        logger.warning("Ollama returned non-200 response")

        return {
            "ollama": "not responding"
        }

    except Exception as e:

        logger.error(f"Ollama health check failed: {str(e)}")

        return {
            "ollama": "offline"
        }
    
# @router.get("/test-error")
# def test_error():

#     raise Exception("Test exception triggered")