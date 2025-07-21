from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="Hiredly Backend API")

# 👇 Add CORS middleware
origins = [
    "https://gleaming-kulfi-152438.netlify.app",  # Your Netlify frontend
    "http://localhost:3000"  # For local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
