from enum import Enum
from typing import List

from openweathermap import models  # type: ignore
from pydantic import BaseModel


class Wind(BaseModel):
    speed: float
    degree: str


class Weekly(BaseModel):
    dt: int
    high: int
    low: int
    icon: str


class Uvi(BaseModel):
    dt: int
    value: float


class Forecast(BaseModel):
    weather: List[models.Daily]
    air_pollution: List[models.AirPollution]
    uvi: List[Uvi]


class WidgetResponseModel(BaseModel):
    temps: List[int]
    wind: Wind
    weather: models.Weather
    forecast: Forecast


class WidgetOverviewOld(BaseModel):
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
