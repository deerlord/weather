from copy import deepcopy
from typing import List

from backend.clients import influxdb, openweather
from openweatherapi import models


def weather_points(measurement: str, data: List[models.WeatherDataBaseModel]):
    for point in data:
        _data = deepcopy(point.dict())
        _data.pop("dt")
        yield {"measurement": measurement, "time": point.dt, "fields": _data}


async def weather_data():
    data = await openweather().one_call()
    current_points = weather_points(measurement="current", data=[data.current])
    hourly_points = weather_points(measurement="hourly", data=data.hourly)
    minutely_points = weather_points(measurement="minutely", data=data.minutely)
    daily_points = weather_points(measurement="daily", data=data.minutely)
    for points in [current_points, hourly_points, minutely_points, daily_points]:
        influxdb().write_points(points=points)
