from openweatherapi  import models

# testing tools
import unittest 

from tests.fixtures import openweatherapi_models



class TestModels(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_call(self):
        data = models.OneCallAPIResponse(
            **openweatherapi_models.ONE_CALL_API_RESPONSE_INPUT
        )
        print(data)
