from  unittest import TestCase, mock
import asyncio

from backend import server

from tests.fixtures import openweatherapi
from openweathermap import models



ONE_CALL_RETURN_VALUE = models.OneCallAPIResponse(**openweatherapi.ONE_CALL_API_AS_DICT)
AIR_POLLUTION_RETURN_VALUE = models.AirPollutionAPIResponse(**openweatherapi.AIR_POLLUTION)
UVI_FORECAST_RETURN_VALUE = [
  models.UviAPIResponse(**data)
  for data in openweatherapi.UVI_FORECAST
]


class TestWeatherEndpoints(TestCase):

    @mock.patch(
        'backend.server.api.OpenWeatherData.one_call',
        return_value=ONE_CALL_RETURN_VALUE
    )
    @mock.patch(
        'backend.server.api.OpenWeatherData.air_pollution_forecast',
        return_value=AIR_POLLUTION_RETURN_VALUE
    )
    @mock.patch(
        'backend.server.api.OpenWeatherData.uvi_forecast',
        return_value=UVI_FORECAST_RETURN_VALUE
    )
    @mock.patch(
        'backend.server.cache.location',
        return_value=openweatherapi.CACHE_LOCATION
    )
    def test_current(self, location_mock, uvi_forecast_mock, air_pollution_mock, one_call_mock):
            result = asyncio.run(
                server.current(lat=0.0, lon=0.0)
            )
            self.assertDictEqual(
                result,
                {
                    "data": ONE_CALL_RETURN_VALUE,
                    "air_pollution_forecast": AIR_POLLUTION_RETURN_VALUE.list,
                    "uvi_forecast": UVI_FORECAST_RETURN_VALUE,
                    "location": openweatherapi.CACHE_LOCATION
                }
            )
