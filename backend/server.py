from typing import Any, Dict

from fastapi import APIRouter, FastAPI, HTTPException
from openweathermap import api  # type: ignore
from starlette.responses import StreamingResponse  # type: ignore

from backend import cache, clients, settings
from backend.models import weather as models

router = APIRouter()
app = FastAPI()


@router.get("/icon/{icon_id}")
async def icon(icon_id: str):
    result = await api.icon(icon_id)
    return StreamingResponse(result, media_type="image/png")


@router.get("/map/{layer}")
async def map(layer: models.MapLayer, lat: float, lon: float, zoom: int):
    client = api.OpenWeatherMap(appid=settings.OPEN_WEATHER_MAP_API_KEY)
    method = getattr(client, layer)
    # find tile from lat/lon
    x = 0
    y = 0
    result = method(x=x, y=y, z=zoom)
    return StreamingResponse(result, media_type="image/png")


@router.get("/widget/overview", response_model=models.WidgetResponseModel)
async def widget_overview(lat: float, lon: float):
    client = api.OpenWeatherData(appid=settings.OPEN_WEATHER_MAP_API_KEY)
    one_call = await client.one_call(
        lat=lat, lon=lon, units=settings.OPEN_WEATHER_MAP_UNITS
    )
    air_pollution_forecast = await client.air_pollution_forecast(lat=lat, lon=lon)
    uvi_forecast = await client.uvi_forecast(lat=lat, lon=lon, cnt=8)
    location = await cache.location(lat=lat, lon=lon)
    temps = [hour.temp for hour in one_call.hourly]
    uvis = ({"value": uvi.value, "date": uvi.date} for uvi in uvi_forecast)
    result = {
        "temps": [one_call.current.temp] + temps,
        "wind": {
            "speed": one_call.current.wind_speed,
            "degree": one_call.current.wind_deg,
        },
        "weather": one_call.current.weather[0],
        "forecast": {
            "weather": one_call.daily,
            "air_pollution": air_pollution_forecast.list,
            "uvi": uvis,
        },
    }
    return result


app.include_router(router, prefix="/weather")
