from copy import deepcopy
from typing import Callable, List

from backend.clients import influxdb, openweather
from openweatherapi import models


def weather_points(data: List[models.WeatherDataBaseModel], munge: Callable):
    for each in data:
        dt, munged = munge(data=each)
        for measurement, fields in munged.items():
            yield {"measurement": measurement, "time": dt, "fields": fields}


def munge_weather_data(data: models.WeatherDataBaseModel) -> tuple:
    """
    Returns a 2-tuple;

    (
      epoch_timestamp,
      {
        'measurement_name': {
          'field': 'value',
          ...
        },
        ...
      }
    )
    """
    # get name from model
    measurement = type(data).__name__.lower()
    # deep copy so we dont mess up the model
    data = deepcopy(data.dict())
    # find fields that area dicts
    flatten_keys = [field for field, value in data.items() if isinstance(value, dict)]
    # create {measurement: fields} map
    retval = {f"{measurement}_{field}": data.pop(field) for field in flatten_keys}
    # check for weather
    weather = data.pop("weather", {})
    # get weather IDs and serialize them
    if weather:
        ids = [each["id"] for each in weather]
        retval.update({f"{measurement}_weather": {"ids": str(ids)}})
    # include rest of model data (int/float/str fields)
    retval.update({measurement: data})
    # include 'dt' value once
    return (data.pop("dt"), retval)


def munge_alert_data(data: models.Alert) -> tuple:
    data = deepcopy(data.dict())
    return (data["start"], {"alert": data})


async def weather_data():
    data = await openweather().one_call()
    current_points = weather_points(data=[data.current], munge=munge_weather_data)
    hourly_points = weather_points(data=data.hourly, munge=munge_weather_data)
    minutely_points = weather_points(data=data.minutely, munge=munge_weather_data)
    daily_points = weather_points(data=data.daily, munge=munge_weather_data)
    alert_points = weather_points(data=data.alerts, munge=munge_alert_data)
    for points in [
        current_points,
        hourly_points,
        minutely_points,
        daily_points,
        alert_points,
    ]:
        influxdb().write_points(points=points, time_precision="s")
