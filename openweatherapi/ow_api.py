import aiohttp  # type: ignore
import logging
from dataclasses import dataclass
from openweatherapi import models, exceptions


@dataclass
class OpenWeatherAPI():
    api_key: str
    lat: float
    lon: float
    version: str = '2.5'

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
        params: dict = {}
    ) -> dict:
        result = {}
        params['appid'] = self.api_key
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self._url_formatter(url),
                params=params
            ) as resp:
                if resp.status == 200:
                    result = await resp.json()
                else:
                    message = f'HTTP ERROR {resp.status}'
                    logging.warning(message)
        return result

    async def one_call(self) -> models.OneCallAPIResponse:
        """
        params:
          exclude: any subset of {'minutely', 'hourly', 'daily'}

        Raises openweatherapi.exceptions.ResponseMalformed
        """
        result = await self._api_request(
            url='onecall',
            params={'lat': self.lat, 'lon': self.lon}
        )
        try:
            response = models.OneCallAPIResponse(**result)
        except TypeError as error:
            message = (
                f'Error: Unable to parse One Call API body - {error} ; '
                f'Called with arguments: {result}'
            )
            logging.error(message)
            raise exceptions.ResponseMalformed()
        return response

