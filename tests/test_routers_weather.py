import asyncio
from unittest import TestCase, mock

from openweathermap import models

from backend.models import weather as w_models
from backend.routers import weather
from tests.fixtures import openweatherapi as fixtures
from tests.fixtures.routers import weather as router_fixtures

ONE_CALL_RETURN_VALUE = models.OneCallAPIResponse(**fixtures.ONE_CALL_API_AS_DICT)
AIR_POLLUTION_RETURN_VALUE = models.AirPollutionAPIResponse(**fixtures.AIR_POLLUTION)
UVI_FORECAST_RETURN_VALUE = models.UviAPIResponse(**fixtures.UVI_FORECAST)


class TestWeatherEndpoints(TestCase):
    @mock.patch(
        "backend.routers.weather.api.OpenWeatherData.one_call",
        return_value=ONE_CALL_RETURN_VALUE,
    )
    @mock.patch(
        "backend.routers.weather.api.OpenWeatherData.air_pollution_forecast",
        return_value=AIR_POLLUTION_RETURN_VALUE,
    )
    @mock.patch(
        "backend.routers.weather.api.OpenWeatherData.uvi_forecast",
        return_value=UVI_FORECAST_RETURN_VALUE,
    )
    @mock.patch(
        "backend.routers.weather.cache.location", return_value=fixtures.CACHE_LOCATION
    )
    def test_widget_overview(
        self, location_mock, uvi_forecast_mock, air_pollution_mock, one_call_mock
    ):
        result = asyncio.run(weather.widget_overview(lat=0.0, lon=0.0))
        model = w_models.WidgetOverviewResponse(**result)
        print(model.dict())
        self.assertDictEqual(result, router_fixtures.WIDGET_OVERVIEW_RESPONSE)
