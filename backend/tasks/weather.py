import asyncio

from backend.clients import influxdb, openweather
from openweatherapi import models


async def munge_one_call(data: models.OneCallAPIResponse):
    current = [munge(measurement="current", data=data.current.flatten())]
    minutely = [
        munge(measurement="minutely", data=minutely.flatten())
        for minutely in data.minutely
    ]
    hourly = [
        munge(measurement="hourly", data=hourly.flatten()) for hourly in data.hourly
    ]
    print(data.daily[0].flatten())
    daily = [
        munge(measurement="daily", data=daily.flatten()) for daily in data.daily
    ]
    return (current, minutely, hourly)


def munge(measurement: str, data: dict):
    data.pop('weather', [])
    return {"measurement": measurement, "time": data.pop("dt"), "fields": data}


async def periodic_weather():
    data = await openweather().one_call()
    current = data.current.dict()
    current_points = [
        {
            "measurement": "current",
            "time": current["dt"],
            "fields": current,
        }
    ]
    print(current_points)
    influxdb().write_points(current_points)
    return
    hourly_points = [
        {"measurement": "hourly", "time": hourly.dt, "fields": hourly.dict()}
        for hourly in data.hourly
    ]
    influxdb().write_points(hourly_points)
    minutely_points = [
        {"measurement": "minutely", "time": minutely.dt, "fields": minutely.dict()}
        for minutely in data.minutely
    ]
    influxdb().write_points(minutely_points)
    daily_points = [
        {"measurement": "daily", "time": daily.dt, "fields": daily.dict()}
        for daily in data.daily
    ]
    influxdb().write_points(daily_points)



import pprint

pp = pprint.PrettyPrinter(indent=4)
client = openweather()
data = asyncio.run(client.one_call())
result = asyncio.run(munge_one_call(data))
pp.pprint(result)
