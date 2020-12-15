# testing tools
import asyncio
import unittest

from aioresponses import aioresponses as responses

from openweatherapi import api, models
from tests.fixtures import openweatherapi as fixtures


class TestModels(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_call(self):
        data = models.OneCallAPIResponse(**fixtures.ONE_CALL_API_RESPONSE_INPUT)
        self.assertDictEqual(data.dict(), fixtures.ONE_CALL_API_AS_DICT)


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = api.OpenWeatherAPI("", 0.0, 0.0)

    def tearDown(self):
        pass

    def test_one_call(self):
        with responses() as resps:
            resps.get(
                "https://api.openweathermap.org/data/2.5/"
                "onecall?lat=0.0&lon=0.0&units=imperial",
                payload=fixtures.ONE_CALL_API_RESPONSE_INPUT,
                status=200,
            )
            result = asyncio.run(self.client.one_call())
        self.assertDictEqual(result.dict(), fixtures.ONE_CALL_API_AS_DICT)
