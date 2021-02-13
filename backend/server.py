from typing import Any, Dict

from fastapi import FastAPI
from openweathermap import api
from starlette.responses import StreamingResponse  # type: ignore

from backend import cache, clients
from backend.models import weather as models

app = FastAPI()


@app.get("/weather/icon/{icon_id}")
async def icon(icon_id: str):
    result = await api.icon(icon_id)
    return StreamingResponse(result, media_type="image/png")


# needs caching around endpoint?
@app.get(
    "/weather/widget/overview",
   response_model=models.WidgetOverview
)
async def current(lat: float, lon: float):
    """
    see https://openweathermap.org/widgets-constructor for example
    """
    client = api.OpenWeatherData(appid="")  # pull appid from settings
    data = await client.one_call(
        lat=lat, lon=lon, units="imperial"
    )  # pull units from settings
    air_pollution_forecast = await client.air_pollution_forecast(lat=lat, lon=lon)
    uvi_forecast = await client.uvi_forecast(lat=lat, lon=lon, cnt=8)
    location = await cache.location(lat=lat, lon=lon)
    result = {
        "data": data,
        "air_pollution_forecast": air_pollution_forecast.list,
        "uvi_forecast": uvi_forecast,
        "location": location,
    }  # type: Dict[str, Any]
    return result


@app.get("/weather/map/{layer}")
async def map(layer: models.MapLayer, lat: float, lon: float, zoom: int):
    client = api.OpenWeatherMap(appid="")  # pull appid from settings
    method = getattr(client, layer)
    # find tile from lat/lon
    x = 0
    y = 0
    return method(x=x, y=y, z=zoom).dict()
