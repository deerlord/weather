from enum import Enum
from typing import List

from openweathermap import models  # type: ignore
from pydantic import BaseModel


class Wind(BaseModel):
    speed: float
    degree: str


class Forecast(BaseModel):
    weather: List[models.Daily]
    air_pollution: List[models.AirPollution]
    uvi: List[models.Uvi]


class WidgetOverviewResponse(BaseModel):
    temps: List[float]
    wind: Wind
    weather: models.Weather
    forecast: Forecast


class MapLayer(str, Enum):
    clouds = "clouds"
    precipitation = "precipitation"
    pressure = "pressure"
    wind = "wind"
    temp = "temp"
