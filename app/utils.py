import random
from jose import jwt
from datetime import datetime, timedelta
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"

def fake_ats_score(resume, jd):
    """Simulate ATS score calculation (placeholder logic)"""
    return random.randint(50, 90)

def create_jwt_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    """Create JWT token for authentication"""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
