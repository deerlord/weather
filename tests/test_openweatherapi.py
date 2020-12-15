# testing tools
import asyncio
import unittest

from aioresponses import aioresponses as responses

from openweatherapi import api, models, exceptions
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

    def test_api_request_error(self):
        with responses() as resps:
            resps.get(
                "https://api.openweathermap.org/data/2.5/?units=imperial",
                payload={},
                status=500
            )
            result = asyncio.run(self.client._api_request(url=''))
        self.assertDictEqual(result, {})

    def test_units(self):
        self.client.units = 'METRIC'
        self.assertEqual(self.client.units, 'metric')

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

    def test_one_call_response_malformed(self):
        with responses() as resps:
            resps.get(
                "https://api.openweathermap.org/data/2.5/"
                "onecall?lat=0.0&lon=0.0&units=imperial",
                payload={},
                status=200
            )
            with self.assertRaises(exceptions.ResponseMalformed):
                asyncio.run(self.client.one_call())

    def test_icon(self):
        with responses() as resps:
            resps.get(
                "http://openweathermap.org/img/wn/01d@2x.png",
                body=fixtures.ICON_BINARY,
                status=200
            )
            result = asyncio.run(self.client.icon('01d'))
        self.assertEqual(result, fixtures.ICON_BINARY)

    def test_icon_error(self):
        with responses() as resps:
            resps.get(
                "http://openweathermap.org/img/wn/01d@2x.png",
                body=fixtures.ICON_BINARY,
                status=404
            )
            with self.assertRaises(exceptions.IconNotFound):
                asyncio.run(self.client.icon('01d'))

