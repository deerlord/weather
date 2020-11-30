from pydantic import BaseModel
from typing import List


class Coordinates(BaseModel):
    lon: float
    lat: float


class Weather(BaseModel):
    id: str
    main: str
    desctription: str
    icon: str


class Periodic(BaseModel):
    one_hour: float = 0.0
    three_hour: float = 0.0


class Current(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    pressure: float
    humidity: float
    dew_point: float
    uvi: float
    clouds: float
    visibility: float
    wind_speed: float
    wind_deg: float
    weather: List[Weather]
    rain: Periodic
    snow: Periodic
    pop: float = None


class Minutely(BaseModel):
    dt: int
    precipitation: float


class DataDaily(BaseModel):
    day: float
    min: float = None
    max: float = None
    night: float
    eve: float
    morn: float


class Daily(BaseModel):
    dt: int
    sunrise: int
    sunset: int
    temp: DataDaily
    feels_like: DataDaily
    pressure: float
    humidity: float
    dew_point: float
    wind_speed: float
    wind_deg: float
    weather: List[Weather]
    clouds: float
    pop: float
    rain: float = 0.0
    snow: float = 0.0
    uvi: float


class Alerts(BaseModel):
    sender_name: str
    event: str
    start: int
    end: int
    description:  str

# found at https://openweathermap.org/api/one-call-api
class APIResponse(BaseModel):
    lat: float
    lon: float
    timezone: str
    current: Current
    minutely: List[Minutely]
    hourly: List[Current]
    daily: List[Daily]
    alerts: List[Alerts]
