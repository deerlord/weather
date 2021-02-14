from fastapi import FastAPI
from starlette.responses import StreamingResponse  # type: ignore

from backend import clients
from backend.models.influxdb import Measurement

app = FastAPI()


@app.get("/weather/icon/{icon_id}")
async def icon(icon_id: str):
    result = await clients.openweather().icon(icon_id)
    return StreamingResponse(result, media_type="image/png")


@app.get("/weather/{measurement}")
async def weather(time: str, delta: str, measurement: Measurement):
    time = time + "000000000"
    delta = delta + "000000000"
    query = (
        f"select * from {measurement} "
        f"where (time >= {time}) and (time <= ({time} + {delta}))"
    )
    retval = clients.influxdb().query(
        query=query,
        epoch="s",
        database="weather",
    )
    return retval[(f"{measurement}", None)]
