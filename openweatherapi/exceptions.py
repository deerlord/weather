class OpenWeatherAPIException(BaseException):
    pass


class NoCoordinates(OpenWeatherAPIException):
    pass


class ResponseMalformed(OpenWeatherAPIException):
    pass
