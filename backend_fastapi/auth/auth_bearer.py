from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from backend_fastapi.auth.jwt_handler import verify_access_token


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):

        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:

            token = credentials.credentials

            username = verify_access_token(token)

            if username is None:

                raise HTTPException(
                    status_code=403,
                    detail="Invalid or expired token"
                )

            return token

        raise HTTPException(
            status_code=403,
            detail="Invalid authorization code"
        )