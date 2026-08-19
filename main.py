from fastapi import FastAPI
from app.api.router import api_router
app = FastAPI(title="Data Privacy API")
app.include_router(api_router)
print("Data Privacy Engine API Server Started Successfully!")
