from fastapi import APIRouter
from pydantic import BaseModel
from backend_fastapi.logger import logger

from backend_fastapi.auth.password_handler import (
    hash_password,
    verify_password
)

from backend_fastapi.auth.jwt_handler import (
    create_access_token
)

router = APIRouter()

# Temporary in-memory user storage
fake_db = {}

class UserSignup(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/signup")
def signup(user: UserSignup):

    if user.username in fake_db:
        
        logger.warning(
            f"Signup failed - user already exists: {user.username}"
        )

        return {
            "message": "User already exists"
        }

    hashed_password = hash_password(
        user.password
    )

    fake_db[user.username] = hashed_password

    logger.info(
        f"New user signup: {user.username}"
    )

    return {
        "message": "User created successfully"
    }


@router.post("/login")
def login(user: UserLogin):

    if user.username not in fake_db:
        logger.warning(
            f"Invalid username login attempt: {user.username}"
        )

        return {
            "message": "Invalid username"
        }

    stored_password = fake_db[user.username]

    if not verify_password(
        user.password,
        stored_password
    ):
        logger.warning(
            f"Invalid password attempt: {user.username}"
        )

        return {
            "message": "Invalid password"
        }

    token = create_access_token(
        data={
            "sub": user.username
        }
    )

    logger.info(
        f"User login successful: {user.username}"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }