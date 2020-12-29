from fastapi import FastAPI
from starlette.responses import StreamingResponse  # type: ignore

from backend import clients
from openweatherapi import models

from backend.models import Measurement


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


@app.get("/weather/current/")
async def current(time: int, delta: int):
    client = clients.influxdb()
    query = f"select * from current where (time >= {time}) and (time <= (time + delta))"
    return client.query(query)


@app.get("/weather/{measurement}/")
async def hourly(time: int, delta: int, measurement: Measurement):
    query = f"select * from {measurement} where (time >= {time}) and (time <= ({time} + {delta}))"
    return clients.influxdb().query(query)
