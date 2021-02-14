import asyncio
from dataclasses import dataclass
from functools import lru_cache, wraps
from typing import Callable

from fastapi import HTTPException
from openweathermap import api  # type: ignore

from backend import settings


@dataclass
class Cacheable:
    co: Callable
    done = False
    result = None
    lock = asyncio.Lock()

    def __await__(self):
        with (yield from self.lock):
            if self.done:
                return self.result
            self.result = yield from self.co.__await__()
            self.done = True
            return self.result


def cacheable(func: Callable):
    @wraps(func)
    def wrapped(*args, **kwargs):
        r = func(*args, **kwargs)
        return Cacheable(r)

    return wrapped


@lru_cache(maxsize=16)
@cacheable
async def location(lat: float, lon: float):
    client = api.OpenWeatherGeocoding(appid=settings.OPEN_WEATHER_MAP_API_KEY)
    result = await client.reverse(lat=lat, lon=lon, limit=1)
    if len(result) == 0:
        raise HTTPException(
            status_code=500, detail="Could not find location for {lat} {lon}"
        )
    return result[0]
