from typing import List

from pydantic import BaseModel


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Hourly(BaseModel):
    dt: int
    temp: float
    feels_like: float
    pressure: float
    humidity: float
    dew_point: float
    clouds: float
    visibility: float
    wind_speed: float
    wind_deg: int
    weather: List[Weather]
    pop: float
    rain: dict = {"1h": 0.0}
    snow: dict = {"1h": 0.0}


class Current(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    pressure: float
    humidity: float
    uvi: float
    clouds: float
    visibility: float
    wind_speed: float
    wind_deg: int
    weather: List[Weather]
    rain: dict = {"1h": 0.0}
    snow: dict = {"1h": 0.0}


class Minutely(BaseModel):
    dt: int
    precipitation: float


class DailyTemp(BaseModel):
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float


class DailyFeelsLike(BaseModel):
    day: float
    night: float
    eve: float
    morn: float


class Daily(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: DailyTemp
    feels_like: DailyFeelsLike
    pressure: float
    humidity: float
    dew_point: float
    wind_speed: float
    wind_deg: int
    weather: List[Weather]
    clouds: float
    pop: float
    rain: float = 0.0
    uvi: float = 0.0


class Alert(BaseModel):
    sender_name: str
    event: str
    start: int
    end: int
    description: str


class OneCallAPIResponse(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: Current
    minutely: List[Minutely] = []
    hourly: List[Hourly] = []
    daily: List[Daily] = []
    alerts: List[Alert] = []
