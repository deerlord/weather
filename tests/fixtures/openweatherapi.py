ONE_CALL_API_RESPONSE_INPUT = {
    "lat": 40.12,
    "lon": -96.66,
    "timezone": "America/Chicago",
    "timezone_offset": -18000,
    "current": {
        "dt": 1595243443,
        "sunrise": 1595243663,
        "sunset": 1595296278,
        "temp": 293.28,
        "feels_like": 293.82,
        "pressure": 1016,
        "humidity": 100,
        "dew_point": 293.28,
        "uvi": 10.64,
        "clouds": 90,
        "visibility": 10000,
        "wind_speed": 4.6,
        "wind_deg": 310,
        "weather": [
            {"id": 501, "main": "Rain", "description": "moderate rain", "icon": "10n"},
            {
                "id": 201,
                "main": "Thunderstorm",
                "description": "thunderstorm with rain",
                "icon": "11n",
            },
        ],
        "rain": {"1h": 2.93},
    },
    "minutely": [
        {"dt": 1595243460, "precipitation": 2.928},
    ],
    "hourly": [
        {
            "dt": 1595242800,
            "temp": 293.28,
            "feels_like": 293.82,
            "pressure": 1016,
            "humidity": 100,
            "dew_point": 293.28,
            "clouds": 90,
            "visibility": 10000,
            "wind_speed": 4.6,
            "wind_deg": 123,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n",
                }
            ],
            "pop": 0.99,
            "rain": {"1h": 2.46},
        },
    ],
    "daily": [
        {
            "dt": 1595268000,
            "sunrise": 1595243663,
            "sunset": 1595296278,
            "temp": {
                "day": 298.82,
                "min": 293.25,
                "max": 301.9,
                "night": 293.25,
                "eve": 299.72,
                "morn": 293.48,
            },
            "feels_like": {
                "day": 300.06,
                "night": 292.46,
                "eve": 300.87,
                "morn": 293.75,
            },
            "pressure": 1014,
            "humidity": 82,
            "dew_point": 295.52,
            "wind_speed": 5.22,
            "wind_deg": 146,
            "weather": [
                {
                    "id": 502,
                    "main": "Rain",
                    "description": "heavy intensity rain",
                    "icon": "10d",
                }
            ],
            "clouds": 97,
            "pop": 1,
            "rain": 12.57,
            "uvi": 10.64,
        },
    ],
    "alerts": [
        {
            "sender_name": "NWS Tulsa (Eastern Oklahoma)",
            "event": "Heat Advisory",
            "start": 1597341600,
            "end": 1597366800,
            "description": "...HEAT ADVISORY REMAINS IN EFFECT FROM 1 PM THIS AFTERNOON TO\n8 PM CDT THIS EVENING...\n* WHAT...Heat index values of 105 to 109 degrees expected.\n* WHERE...Creek, Okfuskee, Okmulgee, McIntosh, Pittsburg,\nLatimer, Pushmataha, and Choctaw Counties.\n* WHEN...From 1 PM to 8 PM CDT Thursday.\n* IMPACTS...The combination of hot temperatures and high\nhumidity will combine to create a dangerous situation in which\nheat illnesses are possible.",
        },
    ],
}

ONE_CALL_API_AS_DICT = {
    "lat": 40.12,
    "lon": -96.66,
    "timezone": "America/Chicago",
    "timezone_offset": -18000,
    "current": {
        "dt": 1595243443,
        "sunrise": 1595243663,
        "sunset": 1595296278,
        "temp": 293.28,
        "feels_like": 293.82,
        "pressure": 1016.0,
        "humidity": 100.0,
        "uvi": 10.64,
        "clouds": 90.0,
        "visibility": 10000.0,
        "wind_speed": 4.6,
        "wind_deg": 310,
        "weather": [
            {"id": 501, "main": "Rain", "description": "moderate rain", "icon": "10n"},
            {
                "id": 201,
                "main": "Thunderstorm",
                "description": "thunderstorm with rain",
                "icon": "11n",
            },
        ],
        "rain": {"1h": 2.93},
        "snow": {"1h": 0.0},
    },
    "minutely": [{"dt": 1595243460, "precipitation": 2.928}],
    "hourly": [
        {
            "dt": 1595242800,
            "temp": 293.28,
            "feels_like": 293.82,
            "pressure": 1016.0,
            "humidity": 100.0,
            "dew_point": 293.28,
            "clouds": 90.0,
            "visibility": 10000.0,
            "wind_speed": 4.6,
            "wind_deg": 123,
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10n",
                }
            ],
            "pop": 0.99,
            "rain": {"1h": 2.46},
            "snow": {"1h": 0.0},
        }
    ],
    "daily": [
        {
            "dt": 1595268000,
            "sunrise": 1595243663,
            "sunset": 1595296278,
            "temp": {
                "day": 298.82,
                "min": 293.25,
                "max": 301.9,
                "night": 293.25,
                "eve": 299.72,
                "morn": 293.48,
            },
            "feels_like": {
                "day": 300.06,
                "night": 292.46,
                "eve": 300.87,
                "morn": 293.75,
            },
            "pressure": 1014.0,
            "humidity": 82.0,
            "dew_point": 295.52,
            "wind_speed": 5.22,
            "wind_deg": 146,
            "weather": [
                {
                    "id": 502,
                    "main": "Rain",
                    "description": "heavy intensity rain",
                    "icon": "10d",
                }
            ],
            "clouds": 97.0,
            "pop": 1.0,
            "rain": 12.57,
            "uvi": 10.64,
        }
    ],
    "alerts": [
        {
            "sender_name": "NWS Tulsa (Eastern Oklahoma)",
            "event": "Heat Advisory",
            "start": 1597341600,
            "end": 1597366800,
            "description": "...HEAT ADVISORY REMAINS IN EFFECT FROM 1 PM THIS AFTERNOON TO\n8 PM CDT THIS EVENING...\n* WHAT...Heat index values of 105 to 109 degrees expected.\n* WHERE...Creek, Okfuskee, Okmulgee, McIntosh, Pittsburg,\nLatimer, Pushmataha, and Choctaw Counties.\n* WHEN...From 1 PM to 8 PM CDT Thursday.\n* IMPACTS...The combination of hot temperatures and high\nhumidity will combine to create a dangerous situation in which\nheat illnesses are possible.",
        }
    ],
}

ICON_BINARY = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00d\x00\x00\x00d\x08\x06\x00\x00\x00p\xe2\x95T\x00\x00\x03{IDATx\x9c\xed\xdcY\xa8MQ\x1c\xc7\xf1\xaf)\x89\xc85\x86\xa2\xc4\x0b\x85\x0c\x19\xee\x83)\xf3\x03\x85\xa4$\xa2<)E\x94\x07\xc5\x9b7<(R\xba/\x9e\x94d\x96\x90y\xccL\x1eLWI\x94!$\x14\xad,\xba\xc4\xed\xb8g\xaf\xff\x7f\xed\xfc>u\xba\xb7\xeem\xff\xd69\xbfs\xf6\xb8\xf6ADDDDDDDDDDDDDDDDDDD\xc4L3\xab\xa0\x97\xcbg\x14\xb5\xa8\x1a\xa0\x16\x18\n\x0c\x04z\x00\x1d\xe3\xdf\x9a\x03o\x80\x17\xc0M\xe0:p\x06x\\Dp\xe7\xcd\xfb\x8aXL\xa3Z&O(F\x7f`"0\x1e\x98\x02\xb4\xad`\xa9S\x1b\xfc~\x02\x08\xaf\xe6i\xe0B\xceO4\xf7B\xfa\x00\xeb\x81\x05U.gl|\x04\xc7\x81\xb5\xc0\xb9\x02\xc6W\xb8\xe69\x0e\n\xe8\x02\xd4\x01\x0f\n(\xe3w\xe3\x80\xb3\xc01`x\xc1\xcb\xaeZ\x8e\x85\xcc\x03\xee\xc4"Rn\xe3\xc2\xea\xef"\xb0*a\xc6?\xcb\xad\x90m\xc0\xae\xb0\xfd4\xcc\xdc\x08\x9c\xcae\xf5\x9dS!\x87\x80\xa5N\xd9\xb5\xf1S\xd9\xdb)\xff\xa7\x1c\ni\x197\xb4\x93\x9d\xc7\xd1/\xae\xc2\\K\xc9\xa1\x90\xc3\r\xf6\x80\xbcu\x05\xce{\xae\xbe\xbc\x0b\xd9\x1e7\xae9\xe9\x0e\\\x02Zy\x8c\xc9\xb3\x90Y\xc0\x12\xc7\xfc\xc6\x0c\x066x\x04{\x15\xd2\x1e\xd8\xe9\x94]\xa9\xd5\x1e\xabR\xafB\xb6\xc7Rrg\xfe\xa6\xf1(\xa4\x130\xd7!\xb7)\xc2\x1e\xd7t\xcb@\x8fB\xb6:dVc\x07\xd0\xc2*\xcc\xba\x90\xf0\x8e\x9bc\x9cY\xadn\xc0$\xab0\xebB\xa6V\xf0?9\x9af5&\xebB\xa6\x18\xe7\x15e\xbe\xd5\xc1\xa2e!\xed\xac7\x90\x05\xaa\x89\xa7\xed\x93\xb3,dl\x89\xaeP\xfe\x89\xc9\xa7\xdb\xb2\x90\x91\x86Y)\x0c\xb1\x08\xb1,d\x80aV\n],B,\x0b\xe9i\x98\x95B%\x13+\xaafYH\x07\xc3\xac\x14Z[\x84X\x16\xf2\xd50\xab\xb4,\x0b\xc9u\x86KV,_\xa4\xf7%x=\x1a\xf3\xc5"\xc4\xb2\x90g\x86Y)\xbc\xb3\x08\xb1,\xe4\x9eaV\n\xaf-B,\x0b\xb9l\x98\x95\xc2\x1d\x8b\x10\xcbB\x8e\x19f\xa5p\xd4"\xc4\xb2\x90\xe7q\xf6y\x19}\x8a\x13\xf9\x92\xb3\xde\x15\xdd[\xd2Bv\x03o-\x82\xac\x0b1\xf9\xd8\'\xb0\xdf*\xc8\xba\x90kq\xbaf\x99|\x06\x0eX\x8d\xd7\xe3\xe8y\xb1Cf5\xc2\xed\n\xaf\xac\xc2<\n\xb9]\xa2]\xe0\x0f\xc0&\xcb@\xaf\xf3K\x8b\x9cr\xff\xd5r\xeb@\xafBn\x01k\x9c\xb2+\xb5\'\xce\xc92\xe5y\x06vc\xbc\xd7/G\xe1\xd6\xeae\x1e\xe3\xf2,$\\\x1f\x19\x03\xd4;\x8e\xe1oF\xc5\x03Ys9\\\xa3\x18\x1d\xbeW \x83q\xfc\x10\xee\xe4\xba\xeb\x15\x9eC!O\x81\x11\xc0\xa3\x0c\xc6\x12\xe6\x8d\x1d\xf1\x1c@.W\xf1\x1e\xc6Y)W\x9d\xf2\xc3q\xc6 \xcb\x03\xc0\xbf\xc9\xe9\xb2j\xd8\xe7\x1f\x19\xbf\xb9\xc1R]\xbcc\xea\x86\xef\xd3\xff.\xb7\xeb\xdc\xe14\xc5\xba8K\xf0J\xe2\xac\xfax\x9c\xb1\x10x\x928\xabb\xb9N<\x08w\xe6\x0e\x03f\x03\xf7\x0b^v8k\xbb\x12\xe8\x0bl)x\xd9U\xcb}\xae\xed\xee\xf8\x98\tL\x88?{5a9\xef\xe2\x81^\xd8`\x1f\xccl\xaf\xee\x17e\x99\xfc\xbc\'>V4\xf8\x9a\xa6!qzg\x98U\xdf&\xfe_\xf8n\x94\x8fq{\xf42^v=\x19\xafVf[\x82\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\x88\xc8\xff\x01\xf8\x06\xa7Dt6D$\xae(\x00\x00\x00\x00IEND\xaeB`\x82'

FLATTEN_HOURLY = {
    "dt": 123456,
    "temp": 0.0,
    "feels_like": 0.0,
    "pressure": 0.0,
    "humidity": 0.0,
    "dew_point": 0.0,
    "clouds": 0.0,
    "visibility": 0.0,
    "wind_speed": 0.0,
    "wind_deg": 0,
    "weather": [],
    "pop": 0.0,
    "rain_1h": 0.0,
    "snow_1h": 0.0,
}


AIR_POLLUTION = {
    "coord": {"lat": 50.0, "lon": 50.0},
    "list": [
        {
            "dt": 1605916800,
            "main": {"aqi": 1.0},
            "components": {
                "co": 211.954,
                "no": 0.0,
                "no2": 0.217,
                "o3": 72.956,
                "so2": 0.514,
                "pm2_5": 2.563,
                "pm10": 5.757,
                "nh3": 0.216,
            },
        },
        {
            "dt": 1605920400,
            "main": {"aqi": 1.0},
            "components": {
                "co": 211.954,
                "no": 0.0,
                "no2": 0.201,
                "o3": 72.241,
                "so2": 0.469,
                "pm2_5": 2.662,
                "pm10": 5.622,
                "nh3": 0.224,
            },
        },
        {
            "dt": 1605924000,
            "main": {"aqi": 1.0},
            "components": {
                "co": 213.623,
                "no": 0.0,
                "no2": 0.185,
                "o3": 71.526,
                "so2": 0.443,
                "pm2_5": 2.724,
                "pm10": 5.51,
                "nh3": 0.23,
            },
        },
        {
            "dt": 1605927600,
            "main": {"aqi": 1.0},
            "components": {
                "co": 213.623,
                "no": 0.0,
                "no2": 0.17,
                "o3": 72.241,
                "so2": 0.432,
                "pm2_5": 2.812,
                "pm10": 5.687,
                "nh3": 0.234,
            },
        },
    ],
}


UVI_FORECAST = [
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-06-27T12:00:00Z",
        "date": 1498564800,
        "value": 10.1,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-06-28T12:00:00Z",
        "date": 1498651200,
        "value": 10.19,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-06-29T12:00:00Z",
        "date": 1498737600,
        "value": 10.2,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-06-30T12:00:00Z",
        "date": 1498824000,
        "value": 9.01,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-07-01T12:00:00Z",
        "date": 1498910400,
        "value": 9.46,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-07-02T12:00:00Z",
        "date": 1498996800,
        "value": 10.16,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-07-03T12:00:00Z",
        "date": 1499083200,
        "value": 9.85,
    },
    {
        "lat": 37.75,
        "lon": -122.37,
        "date_iso": "2017-07-04T12:00:00Z",
        "date": 1499169600,
        "value": 10.05,
    },
]

CACHE_LOCATION = {
        "name": "City of London",
        "local_names": {
            "ar": "مدينة لندن",
            "ascii": "City of London",
            "bg": "Сити",
            "ca": "La City",
            "de": "London City",
            "el": "Σίτι του Λονδίνου",
            "en": "City of London",
            "fa": "سیتی لندن",
            "feature_name": "City of London",
            "fi": "Lontoon City",
            "fr": "Cité de Londres",
            "gl": "Cidade de Londres",
            "he": "הסיטי של לונדון",
            "hi": "सिटी ऑफ़ लंदन",
            "id": "Kota London",
            "it": "Londra",
            "ja": "シティ・オブ・ロンドン",
            "la": "Civitas Londinium",
            "lt": "Londono Sitis",
            "pt": "Cidade de Londres",
            "ru": "Сити",
            "sr": "Сити",
            "th": "นครลอนดอน",
            "tr": "Londra Şehri",
            "vi": "Thành phố Luân Đôn",
            "zu": "Idolobha weLondon",
        },
        "lat": 51.5128,
        "lon": -0.0918,
        "country": "GB",
        "state": "",
}

