from fastapi import APIRouter, HTTPException
from app.utils import fake_ats_score, create_jwt_token

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hiredly Backend API is live!"}

@router.post("/analyze")
def analyze_resume(resume: str, job_description: str):
    score = fake_ats_score(resume, job_description)
    return {"score": score}

@router.post("/login")
def login(email: str, password: str):
    if email == "admin@hiredly.app" and password == "Admin@123":
        token = create_jwt_token({"user": email})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
