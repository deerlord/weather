from fastapi import FastAPI
from starlette.responses import StreamingResponse  # type: ignore

from backend import clients
from backend.models import Measurement

app = FastAPI()


@app.get("/weather/icon/{icon_id}")
async def icon(icon_id: str):
    result = await clients.openweather().icon(icon_id)
    return StreamingResponse(result, media_type="image/png")


@app.get("/weather/{measurement}")
async def weather(time: int, delta: int, measurement: Measurement):
    query = (
        f"select * from {measurement} "
        f"where (time >= {time}) and (time <= ({time} + {delta}))"
    )
    retval = clients.influxdb().query(query)
    return retval[(f"{measurement}", None)]
