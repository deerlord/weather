import aiohttp
import logging
from dataclasses import dataclass
from openweatherapi import models



@dataclass
class OpenWeatherAPI():
    api_key: str
    version: str = '2.5'
    lat: float = None
    lon: float = None
    
    def __post_init__(self):
        self._base_url = f'https://api.openwather.org/data/{self.version}'

    def _url_formatter(self, url: str) -> str:
        url = url[1:] if url.startswith('/') else url
        return f'{self._base_url}/{url}'

    async def _response_handler(self, resp) -> dict:
        result = {}
        try:
            result = await resp.json()
        except RuntimeError:
            logging.error('Attempted to decode a non-existent body')
        except aiohttp.ContentTypeError:
            logging.error('Response not JSON encoded')
        return result

    async def _api_request(
        self,
        url: str,
        verb: str='GET',
        data: dict={}
    ) -> dict:
        result = {}
        async with aiohttp.ClientSession() as session:
            http_method = getattr(session, verb.lower())
            async with http_method(
                self._url_formatter(url),
                params=data
            ) as resp:
                if resp.status == 200:
                    result = await resp.json()
                else:
                    message = f'HTTP ERROR {resp.status}'
                    logging.warning(message)
        return result

    async def one_call(
        self,
        exclude: set=set()
    ) -> models.OneCallAPIResponse:
        if self.lat == None or self.lon == None:
            raise exceptions.NoCoordinates(
                'Did not provide latitude or longitude'
            )
        data = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key
        }
        
        if exclude:
            exclude = set(exclude)
            if exclude.issubset({
                'minutely',
                'hourly',
                'daily'
            }):
                data['exclude'] = str(exclude).replace(' ', '')[1:-1]
        result = self._api_request(url='/onecall', verb='GET', data=data)
        return models.OneCallAPIResponse(**result) if result else result
