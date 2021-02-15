from os import environ as ENV

from influxdb import InfluxDBClient  # type: ignore


def influxdb():
    return InfluxDBClient(
        str(ENV["influx_host"]),
        int(ENV["influx_port"]),
        str(ENV["influx_user"]),
        str(ENV["influx_pass"]),
        str(ENV["influx_database"]),
    )
