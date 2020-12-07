from dataclasses import dataclass, field
from typing import List


@dataclass
class Weather():
    id: int
    main: str
    description: str
    icon: str


@dataclass
class Current():
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
    rain: dict = field(default_factory={'1h': None})
    snow: dict = field(default_factory={'1h': None})


@dataclass
class Minutely():
    dt: int
    precipitation: float


@dataclass
class DailyTemp():
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float


@dataclass
class DailyFeelsLike():
    day:  float
    night: float
    eve: float
    morn: float


@dataclass
class Daily():
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
    rain: float
    uvi: float


@dataclass
class Alert():
    sender_name: str
    event: str
    start: int
    end: int
    description: str


@dataclass
class OneCallAPIResponse():
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: Current = field(default_factory={})
    minutely: List[Minutely] = field(default_factory=[])
    hourly: List[Current] = field(default_factory=[])
    daily: List[Daily] = field(default_factory=[])
    alerts: List[Alert] =  field(default_factory=[])
