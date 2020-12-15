from fastapi import FastAPI

from backend import clients
from openweatherapi import models

app = FastAPI()


@app.get("/weather/data", response_model=models.OneCallAPIResponse)
async def weather_data():
    result = await clients.openweather().one_call()
    return result.dict()


@app.get("/weather/icon/{icon_id}")
async def icon(icon_id: str):
    result = await clients.openweather().icon(icon_id)
    return result
