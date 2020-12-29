from enum import enum


class Measurement(str, Enum):
    current = 'current'
    hourly = 'hourly'
    minutely = 'minutely'
    daily = 'daily'
