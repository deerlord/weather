from os import environ as ENV

from influxdb import InfluxDBClient

from openweatherapi.api import OpenWeatherAPI


def openweather():
    return OpenWeatherAPI(
        api_key=str(ENV["openweather_api_key"]),
        lat=float(ENV["latitude"]),
        lon=float(ENV["longitude"]),
    )


def influx():
    return InfluxDBClient(
        str(ENV["influx_host"]),
        int(ENV["influx_port"]),
        str(ENV["influx_user"]),
        str(ENV["influx_pass"]),
        str(ENV["influx_database"]),
    )
