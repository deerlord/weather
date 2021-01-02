import asyncio

from backend.tasks.weather import weather_data

asyncio.run(weather_data())
