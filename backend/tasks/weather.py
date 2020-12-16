from backend.clients import openweather, influxdb
from openweatherapi import models


async def periodic_weather():
    data = await openweather().one_call()
    current = data.current.dict()
    current_time = current.pop('dt')
    weather_points = current.pop('weather')
    rain_points = [current.pop('rain', [])]
    snow_points = [current.pop('snow', [])]
    current_points = [
        {
            "measurement": "current",
            "time": current_time,
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


def parse_current(current: models.Current):
    current = current.dict()
    time = current.pop('dt')
    rain = current.pop('rain', {})
    snow = current.pop('snow', {})
    rain_one_hour = rain.get('1h', None)
    rain_three_hour = rain.get('3h', None)
    snow_one_hour = snow.get('1h', None)
    snow_three_hour = snow.get('3h', None)
    weather_points = [
        w
        for w in current.pop('weather')
    ]
    current_measurement = {
        "measurement": "current",
        "time": time,
        "fields": 


import asyncio
asyncio.run(periodic_weather())
