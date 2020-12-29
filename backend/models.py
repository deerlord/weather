from enum import Enum


class Measurement(str, Enum):
    current = "current"
    hourly = "hourly"
    minutely = "minutely"
    daily = "daily"
