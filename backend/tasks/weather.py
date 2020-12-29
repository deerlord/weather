from typing import List

from pydantic import BaseModel

from backend.clients import influxdb, openweather
from openweatherapi import models


class TableData(BaseModel):
    measurement: str
    time: int
    fields: dict


async def munge_one_call(data: models.OneCallAPIResponse):
    current = [munge(measurement="current", data=data.current.flatten())]
    minutely = [
        munge(measurement="minutely", data=minutely.flatten())
        for minutely in data.minutely
    ]
    hourly = [
        munge(measurement="hourly", data=hourly.flatten()) for hourly in data.hourly
    ]
    daily = [munge(measurement="daily", data=daily.flatten()) for daily in data.daily]
    return (current, minutely, hourly, daily)


def munge(measurement: str, data: dict):
    data.pop("weather", [])
    return {"measurement": measurement, "time": data.pop("dt"), "fields": data}


async def write_points(points: List[TableData]):
    for point in points:
        influxdb().write_points(point.dict())


async def create_points(measurement: str, data: List[BaseModel]):
    for point in data:
        yield TableData(measurement=measurement, time=point.dt, fields=point.dict())


async def periodic_weather():
    data = await openweather().one_call()
    current_points = create_points(measurement="current", data=[data.current])
    hourly_points = create_points(measurement="hourly", data=data.hourly)
    minutely_points = create_points(measurement="minutely", data=data.minutely)
    daily_points = create_points(measurement="daily", data=data.minutely)
    for points in [current_points, hourly_points, minutely_points, daily_points]:
        write_points(points=points)
