from enum import Enum
from typing import List

from openweathermap import models
from pydantic import BaseModel


class WidgetOverview(BaseModel):
    data: models.OneCallAPIResponse
    air_pollution_forecast: List[models.AirPollution]
    uvi_forecast: List[models.UviAPIResponse]
    location: models.GeocodingAPIResponse


class MapLayer(str, Enum):
    clouds = "clouds"
    precipitation = "precipitation"
    pressure = "pressure"
    wind = "wind"
    temp = "temp"
