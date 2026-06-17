import os
import time
from typing import Any, Dict

from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "120"))

# ✅ FIX: use argon2 instead of bcrypt (no 72-byte limit)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

security = HTTPBearer()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(user_id: int) -> Dict[str, Any]:
    payload = {
        "user_id": user_id,
        "exp": int(time.time()) + ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }
    return {
        "token": jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    }


def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        if payload.get("exp") < int(time.time()):
            raise HTTPException(status_code=401, detail="Token has expired")

        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security)
) -> int:
    token = credentials.credentials
    payload = decode_token(token)

    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    return int(user_id)