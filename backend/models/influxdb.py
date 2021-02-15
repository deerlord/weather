from enum import Enum


class Measurement(str, Enum):
    current = "current"
    current_rain = "current_rain"
    current_snow = "current_snow"
    current_weather = "current_weather"
    hourly = "hourly"
    hourly_rain = "hourly_rain"
    hourly_snow = "hourly_snow"
    hourly_weather = "hourly_weather"
    minutely = "minutely"
    daily = "daily"
