import asyncio

from backend.clients import influxdb, openweather


async def fetch_data():
    client = openweather()
    data = await client.one_call()
    return data


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


print(asyncio.run(fetch_data()))
