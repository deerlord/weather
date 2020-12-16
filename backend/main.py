from fastapi import FastAPI
from starlette.responses import StreamingResponse

from backend import clients
from openweatherapi import models

app = FastAPI()


@app.get("/weather/data", response_model=models.OneCallAPIResponse)
async def weather_data():
    result = await clients.openweather().one_call()
    return result.dict()


@app.get("/weather/icon/{icon_id}")
async def icon(icon_id: str):
    client = clients.openweather()
    result = await client.icon(icon_id)
    return StreamingResponse(result, media_type="image/png")
