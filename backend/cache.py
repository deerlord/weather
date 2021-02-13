from openweathermap import api


# cache this for lat/lon
async def location(lat: float, lon: float):
    client = api.OpenWeatherGeocoding(appid="299a2d64a6e4c6f29287f2d58f66bcb3")  # pull from settings
    result = await client.reverse(lat=lat, lon=lon, limit=1)
    if len(result) == 0:
        pass  # problem
    return result[0]
