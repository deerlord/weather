from backend.models import weather


WIDGET_OVERVIEW_RESPONSE = {
    "temps": [293.28, 293.28],
    "wind": {"speed": 4.6, "degree": 310},
    "weather": weather.models.Weather(
        id=501, main="Rain", description="moderate rain", icon="10n"
    ),
    "forecast": {
        "weather": [
            weather.models.Daily(
                dt=1595268000,
                sunrise=1595243663,
                sunset=1595296278,
                temp=weather.models.DailyTemp(
                    day=298.82,
                    min=293.25,
                    max=301.9,
                    night=293.25,
                    eve=299.72,
                    morn=293.48,
                ),
                feels_like=weather.models.DailyFeelsLike(
                    day=300.06, night=292.46, eve=300.87, morn=293.75
                ),
                pressure=1014.0,
                humidity=82.0,
                dew_point=295.52,
                wind_speed=5.22,
                wind_deg=146,
                weather=[
                    weather.models.Weather(
                        id=502,
                        main="Rain",
                        description="heavy intensity rain",
                        icon="10d",
                    )
                ],
                clouds=97.0,
                pop=1.0,
                rain=12.57,
                uvi=10.64,
            )
        ],
        "air_pollution": [
            weather.models.AirPollution(
                dt=1605916800,
                main={"aqi": 1.0},
                components=weather.models.AirPollutionComponents(
                    co=211.954,
                    no=0.0,
                    no2=0.217,
                    o3=72.956,
                    so2=0.514,
                    pm2_5=2.563,
                    pm10=5.757,
                    nh3=0.216,
                ),
            ),
            weather.models.AirPollution(
                dt=1605920400,
                main={"aqi": 1.0},
                components=weather.models.AirPollutionComponents(
                    co=211.954,
                    no=0.0,
                    no2=0.201,
                    o3=72.241,
                    so2=0.469,
                    pm2_5=2.662,
                    pm10=5.622,
                    nh3=0.224,
                ),
            ),
            weather.models.AirPollution(
                dt=1605924000,
                main={"aqi": 1.0},
                components=weather.models.AirPollutionComponents(
                    co=213.623,
                    no=0.0,
                    no2=0.185,
                    o3=71.526,
                    so2=0.443,
                    pm2_5=2.724,
                    pm10=5.51,
                    nh3=0.23,
                ),
            ),
            weather.models.AirPollution(
                dt=1605927600,
                main={"aqi": 1.0},
                components=weather.models.AirPollutionComponents(
                    co=213.623,
                    no=0.0,
                    no2=0.17,
                    o3=72.241,
                    so2=0.432,
                    pm2_5=2.812,
                    pm10=5.687,
                    nh3=0.234,
                ),
            ),
        ],
        "uvi": [
            weather.models.Uvi(dt=1234567890, uvi=10.0),
            weather.models.Uvi(dt=1234567891, uvi=11.0),
        ],
    },
}
