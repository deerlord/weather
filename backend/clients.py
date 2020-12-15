from os import environ as ENV

from openweatherapi.api import OpenWeatherAPI


def openweather():
    return OpenWeatherAPI(
        api_key=str(ENV["openweather_api_key"]),
        lat=float(ENV["latitude"]),
        lon=float(ENV["longitude"]),
    )
