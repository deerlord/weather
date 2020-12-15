from openweatherapi import models

# testing tools
import unittest

from tests.fixtures import openweatherapi as fixtures


class TestModels(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_call(self):
        data = models.OneCallAPIResponse(**fixtures.ONE_CALL_API_RESPONSE_INPUT)
        self.assertDictEqual(
            data.dict(),
            fixtures.ONE_CALL_API_AS_DICT
        )
