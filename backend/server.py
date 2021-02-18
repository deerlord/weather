from fastapi import FastAPI

from backend.routers import weather

app = FastAPI()
app.include_router(weather.router, prefix="/api/weather")
