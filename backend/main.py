from os import environ as ENV

from fastapi import FastAPI

from openweatherapi import api, models

app = FastAPI()


@app.get(
    "/weather/data",
    response_model=models.OneCallAPIResponse
)
async def weather_data():
    client = api.OpenWeatherAPI(
        api_key=str(ENV["openweather_api_key"]),
        lat=float(ENV["latitude"]),
        lon=float(ENV["longitude"]),
    )
    result = await client.one_call()
    return result.dict()
