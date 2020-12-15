from os import environ as ENV

from fastapi import FastAPI

from openweatherapi import api, models

app = FastAPI()


@app.get("/weather/data")
async def weather_data():
    client = OpenWeatherAPI(
        api_key=str(ENV["openweather_api_key"]),
        lat=float(ENV["latitude"]),
        lon=float(ENV["longitude"]),
    )
    return client.one_call()
