import pytest

from apps.weather.services.openweather_service import OpenWeatherService


@pytest.mark.django_db
def test_get_current_weather(mocker):
    mock_openweather_get_weather = mocker.patch('apps.weather.services.openweather_service.OpenWeatherService.get_weather')
    mock_openweather_get_weather.return_value.json.return_value = {
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
            "temp": 291.86,
            "humidity": 61,
            "pressure": 1024,
            "temp_max": 292.12,
            "temp_min": 289.11,
            "sea_level": 1024,
            "feels_like": 291.38,
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
    openweather_service = OpenWeatherService({
        'city': 'Rio de Janeiro', 
        'state': 'RJ', 
        'country': 'BR'
    })
    assert openweather_service.get_weather()
    mock_openweather_get_weather.assert_called_once()


@pytest.mark.django_db
def test_get_lat_lon_from_search_data(mocker):
    mock_openweather_get_lat_lon = mocker.patch('apps.weather.services.openweather_service.OpenWeatherService.get_lat_lon_from_search_data')
    mock_openweather_get_lat_lon.return_value.get_lat_lon_from_search_data.return_value = (-22.911, -43.2094)
    openweather_service = mock_openweather_get_lat_lon({
        'city': 'Rio de Janeiro', 
        'state': 'RJ', 
        'country': 'BR'
    })
    assert openweather_service.get_lat_lon_from_search_data()
    mock_openweather_get_lat_lon.assert_called_once()
