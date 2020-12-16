from backend.clients import influxdb, openweather


def periodic_weather():
    data = await openweather().one_call()
    points = [
        {
            "measurement": "current",
            "time": data.current.dt,
            "fields": data.current.as_dict(),
        }
    ]
    points += [
        {"measurement": "hourly", "time": hourly.dt, "fields": hourly.as_dict()}
        for hourly in data.hourly
    ]
    points += [
        {"measurement": "minutely", "time": minutely.dt, "fields": minutely.as_dict()}
        for minutely in data.minutely
    ]
    points += [
        {"measurement": "daily", "time": daily.dt, "fields": daily.as_dict()}
        for daily in data.daily
    ]
    influxdb().write_points(points)
