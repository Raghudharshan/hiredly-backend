from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Hiredly Backend API")
app.include_router(router)
