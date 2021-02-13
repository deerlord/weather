from openweathermap import api


# cache this for lat/lon
async def location(lat: float, lon: float):
    client = api.OpenWeatherGeocoding(appid="")  # pull from settings
    result = await client.reverse(lat=lat, lon=lon, limit=1)
    if len(result) == 0:
        pass  # problem
    return result[0]
