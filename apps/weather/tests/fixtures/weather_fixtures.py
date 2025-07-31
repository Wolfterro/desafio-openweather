import pytest
from rest_framework.response import Response
from rest_framework import status

from apps.weather.models import WeatherEntry

@pytest.fixture()
def weather_entry():
    return WeatherEntry.objects.create(
        city='Rio de Janeiro',
        state='RJ',
        country='BR',
        latitude=-22.911,
        longitude=-43.2094,
        response_data={
            "dt": 1753915658,
            "id": 3451190,
            "cod": 200,
            "sys": {
                "id": 2098643,
                "type": 2,
                "sunset": 1753907436,
                "country": "BR",
                "sunrise": 1753867664
            },
            "base": "stations",
            "main": {
                "humidity": 61,
                "pressure": 1024,
                'temp': 300,
                'temp_min': 295,
                'temp_max': 305,
                'feels_like': 298,
                "sea_level": 1024,
                "grnd_level": 1027
            },
            "name": "Rio de Janeiro",
            "wind": {
                "deg": 220,
                "speed": 3.6
            },
            "coord": {
                "lat": -22.911,
                "lon": -43.2094
            },
            "clouds": {
                "all": 20
            },
            "weather": [
                {
                "id": 801,
                "icon": "02n",
                "main": "Clouds",
                "description": "few clouds"
                }
            ],
            "timezone": -10800,
            "visibility": 10000
            }
        )

@pytest.fixture()
def weather_entry_creation_response():
    return Response({
        "id": 2,
        "city": "São Paulo",
        "state": "SP",
        "country": "Brasil",
        "latitude": -23.5507,
        "longitude": -46.6334,
        "created_at": "2025-07-30T20:38:21.329401-03:00",
        "response_data": {
            "dt": 1753918455,
            "id": 3458611,
            "cod": 200,
            "sys": {
                "id": 8394,
                "type": 1,
                "sunset": 1753908198,
                "country": "BR",
                "sunrise": 1753868546
            },
            "base": "stations",
            "main": {
                "temp": 283.75,
                "humidity": 80,
                "pressure": 1025,
                "temp_max": 284.25,
                "temp_min": 283.03,
                "sea_level": 1025,
                "feels_like": 282.95,
                "grnd_level": 934
            },
            "name": "Liberdade",
            "wind": {
                "deg": 130,
                "speed": 4.63
            },
            "coord": {
                "lat": -23.5507,
                "lon": -46.6334
            },
            "clouds": {
                "all": 0
            },
            "weather": [
                {
                    "id": 800,
                    "icon": "01n",
                    "main": "Clear",
                    "description": "clear sky"
                }
            ],
            "timezone": -10800,
            "visibility": 10000
        },
        "temperature": {
            "min": 283.03,
            "max": 284.25,
            "temp": 283.75,
            "feels_like": 282.95
        },
        "temperature_celsius": {
            "min": 9.879999999999995,
            "max": 11.100000000000023,
            "temp": 10.600000000000023,
            "feels_like": 9.800000000000011
        },
        "temperature_fahrenheit": {
            "min": 49.78399999999999,
            "max": 51.98000000000005,
            "temp": 51.08000000000004,
            "feels_like": 49.64000000000002
        },
        "weather_description": "clear sky",
        "weather": "Clear",
        "icon_url": "https://openweathermap.org/img/wn/01n@2x.png",
        "pressure": 1025,
        "humidity": 80,
        "wind_speed": 4.63,
        "wind_direction": 130,
        "visibility": 10000
    },
    status=status.HTTP_201_CREATED)