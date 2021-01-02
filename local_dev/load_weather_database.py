from backend.tasks.weather import weather_data
import asyncio

asyncio.run(weather_data())
