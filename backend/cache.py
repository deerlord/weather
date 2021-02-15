import asyncio
from dataclasses import dataclass
from functools import lru_cache, wraps
from typing import Callable

from fastapi import HTTPException
from openweathermap import api  # type: ignore

from backend import settings


@dataclass
class async_cache:
    _cache = dict

    def __call__(self, func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            arg_sig = f"{args},{kwargs}"
            if arg_sig not in self._cache:
                self._cache[arg_sig] = await func(*args, **kwargs)
            return self._cache[arg_sig]

        return wrapper


async def location(lat: float, lon: float):
    client = api.OpenWeatherGeocoding(appid=settings.OPEN_WEATHER_MAP_API_KEY)
    result = await client.reverse(lat=lat, lon=lon, limit=1)
    if len(result) == 0:
        raise HTTPException(
            status_code=500, detail="Could not find location for {lat} {lon}"
        )
    return result[0]
