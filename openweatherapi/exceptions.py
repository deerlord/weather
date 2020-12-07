

class OpenWeatherAPIException(BaseException):
    pass


class NoCoordinates(OpenWeatherAPIException):
    pass
