from typing import List
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Weather():
    id: int
    main: str
    desctription: str
    icon: str


@dataclass
class Periodic():
    one_hour: float = None
    three_hour: float = None


@dataclass
class Current():
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

    @property
    def datetime(self) -> datetime:
        return datetime.utcfromtimestamp(self.dt)


@dataclass
class Minutely():
    dt: int
    precipitation: float


@dataclass
class DataDaily():
    day: float
    min: float = None
    max: float = None
    night: float
    eve: float
    morn: float


@dataclass
class Daily():
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


@dataclass
class Alerts():
    sender_name: str
    event: str
    start: int
    end: int
    description:  str

# found at https://openweathermap.org/api/one-call-api
@dataclass
class OneCallAPIResponse():
    lat: float
    lon: float
    timezone: str
    current: Current
    minutely: List[Minutely]
    hourly: List[Current]
    daily: List[Daily]
    alerts: List[Alerts]


